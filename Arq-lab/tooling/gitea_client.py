from __future__ import annotations

import base64
import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from .models import LabConfig


class GiteaClient:
    def __init__(self, config: LabConfig) -> None:
        self._config = config
        token = base64.b64encode(f"{config.gitea_username}:{config.gitea_password}".encode("utf-8")).decode("ascii")
        self._headers = {
            "Authorization": f"Basic {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        url = f"{self._config.gitea_base_url}{path}"
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url=url, data=data, method=method, headers=self._headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else None
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Gitea {method} {url} failed: HTTP {exc.code} {body}") from exc

    def get_repo(self, repo_name: str) -> dict[str, Any] | None:
        encoded_owner = urllib.parse.quote(self._config.gitea_owner, safe="")
        encoded_repo = urllib.parse.quote(repo_name, safe="")
        return self._request("GET", f"/api/v1/repos/{encoded_owner}/{encoded_repo}")

    def repo_exists(self, repo_name: str) -> bool:
        return self.get_repo(repo_name) is not None

    def ensure_repo(self, repo_name: str, description: str = "") -> dict[str, Any]:
        existing = self.get_repo(repo_name)
        if existing:
            return existing
        payload = {
            "name": repo_name,
            "description": description,
            "private": self._config.gitea_repo_visibility.lower() != "public",
            "auto_init": False,
            "default_branch": self._config.arq_lab_default_branch,
        }
        created = self._request("POST", "/api/v1/user/repos", payload)
        return created

    def clone_url(self, repo_name: str) -> str:
        return f"{self._config.gitea_base_url}/{self._config.gitea_owner}/{repo_name}.git"

    def push_url(self, repo_name: str) -> str:
        parsed = urllib.parse.urlparse(self._config.gitea_base_url)
        credentials = f"{urllib.parse.quote(self._config.gitea_username)}:{urllib.parse.quote(self._config.gitea_password)}@"
        netloc = f"{credentials}{parsed.netloc}"
        return urllib.parse.urlunparse((parsed.scheme, netloc, f"/{self._config.gitea_owner}/{repo_name}.git", "", "", ""))

