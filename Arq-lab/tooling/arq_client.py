from __future__ import annotations

import http.cookiejar
import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from .models import LabConfig
from .utils import now_utc


class ArqClient:
    def __init__(self, config: LabConfig) -> None:
        self._config = config
        self._cookie_jar = http.cookiejar.CookieJar()
        self._opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self._cookie_jar))
        self._authenticated = False

    def _request(
        self,
        method: str,
        path: str,
        *,
        payload: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        allow_reauth: bool = True,
    ) -> Any:
        if not self._authenticated and path != "/api/v2/auth/login":
            self.login()
        query = ""
        if params:
            filtered = {key: value for key, value in params.items() if value is not None}
            query = "?" + urllib.parse.urlencode(filtered, doseq=True)
        url = f"{self._config.arq_api_base_url}{path}{query}"
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        request = urllib.request.Request(url=url, data=data, headers=headers, method=method)
        try:
            with self._opener.open(request, timeout=60) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else None
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 401 and path != "/api/v2/auth/login" and allow_reauth:
                self._authenticated = False
                self._cookie_jar.clear()
                self.login()
                return self._request(method, path, payload=payload, params=params, allow_reauth=False)
            raise RuntimeError(f"ARQ {method} {url} failed: HTTP {exc.code} {body}") from exc

    def login(self) -> dict[str, Any]:
        session = self._request(
            "POST",
            "/api/v2/auth/login",
            payload={
                "workspaceKey": self._config.arq_workspace_key,
                "email": self._config.arq_email,
                "password": self._config.arq_password,
            },
        )
        self._authenticated = True
        return session

    def list_projects(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v2/projects")

    def ensure_project(self, key: str, name: str, description: str = "") -> dict[str, Any]:
        existing = next((item for item in self.list_projects() if item["key"] == key), None)
        payload = {
            "workspaceKey": self._config.arq_workspace_key,
            "projectId": existing["projectId"] if existing else None,
            "key": key,
            "name": name,
            "description": description,
            "active": True,
        }
        return self._request("POST", "/api/v2/projects", payload=payload)

    def list_applications(self) -> list[dict[str, Any]]:
        return self._request("GET", "/api/v2/applications")

    def ensure_application(
        self,
        *,
        project_id: str,
        key: str,
        name: str,
        description: str,
        repository_locator: str,
        default_branch: str,
    ) -> dict[str, Any]:
        existing = next((item for item in self.list_applications() if item["key"] == key), None)
        repository_source = {
            "providerType": "GENERIC_GIT",
            "repositoryLocator": repository_locator,
            "defaultBranch": default_branch,
            "active": True,
        }
        if existing:
            return self._request(
                "PATCH",
                f"/api/v2/applications/{existing['applicationId']}",
                payload={
                    "name": name,
                    "description": description,
                    "active": True,
                    "repositorySource": repository_source,
                },
            )
        return self._request(
            "POST",
            "/api/v2/applications",
            payload={
                "workspaceKey": self._config.arq_workspace_key,
                "projectId": project_id,
                "key": key,
                "name": name,
                "description": description,
                "active": True,
                "repositorySource": repository_source,
            },
        )

    def request_scan(
        self,
        *,
        application_id: str,
        modules: list[str],
        scan_mode: str,
        branch_scope: str,
        ref_name: str | None,
    ) -> dict[str, Any]:
        payload = {
            "applicationId": application_id,
            "modules": modules,
            "scanMode": scan_mode,
            "branchScope": branch_scope,
        }
        if ref_name:
            payload["refName"] = ref_name
        return self._request("POST", "/api/v2/scans/application", payload=payload)

    def get_scan(self, scan_run_id: str) -> dict[str, Any]:
        return self._request("GET", f"/api/v2/scans/{scan_run_id}")

    def poll_scan(self, scan_run_id: str, *, timeout_seconds: int, interval_seconds: int) -> dict[str, Any]:
        started = now_utc()
        while True:
            scan = self.get_scan(scan_run_id)
            status = scan.get("status", "")
            if status in {"SUCCEEDED", "FAILED", "CANCELLED", "SKIPPED"}:
                return scan
            elapsed = (now_utc() - started).total_seconds()
            if elapsed > timeout_seconds:
                raise TimeoutError(f"Timed out while waiting for scan {scan_run_id}")
            import time

            time.sleep(interval_seconds)

    def export_findings(
        self,
        *,
        application_id: str | None = None,
        project_id: str | None = None,
        module: str | None = None,
        branch_name: str | None = None,
        limit: int = 5000,
    ) -> dict[str, Any]:
        return self._request(
            "GET",
            "/api/v2/reports/findings",
            params={
                "applicationId": application_id,
                "projectId": project_id,
                "module": module,
                "branchName": branch_name,
                "limit": limit,
                "format": "json",
            },
        )

    def get_finding(self, finding_id: str) -> dict[str, Any]:
        return self._request("GET", f"/api/v2/findings/{finding_id}")

    def list_occurrences(self, finding_id: str) -> list[dict[str, Any]]:
        return self._request("GET", f"/api/v2/findings/{finding_id}/occurrences")

    def write_probe(self, destination: Path) -> None:
        payload = {
            "projects": self.list_projects(),
            "applications": self.list_applications(),
        }
        destination.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8", newline="\n")
