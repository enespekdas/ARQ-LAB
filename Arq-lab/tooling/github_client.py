from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from .models import LabConfig


class GitHubClient:
    def __init__(self, config: LabConfig) -> None:
        self._config = config
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "arq-lab-publisher",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if config.git_token:
            self._headers["Authorization"] = f"Bearer {config.git_token}"

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        url = path if path.startswith("http") else f"{self._config.git_api_base_url}{path}"
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
            raise RuntimeError(f"GitHub {method} {url} failed: HTTP {exc.code} {body}") from exc

    def viewer(self) -> dict[str, Any] | None:
        return self._request("GET", "/user")

    def get_repo(self, repo_name: str) -> dict[str, Any] | None:
        encoded_owner = urllib.parse.quote(self._config.git_owner, safe="")
        encoded_repo = urllib.parse.quote(repo_name, safe="")
        return self._request("GET", f"/repos/{encoded_owner}/{encoded_repo}")

    def repo_exists(self, repo_name: str) -> bool:
        return self.get_repo(repo_name) is not None

    def list_org_repos(self) -> list[dict[str, Any]]:
        repos: list[dict[str, Any]] = []
        page = 1
        while True:
            payload = self._request("GET", f"/orgs/{urllib.parse.quote(self._config.git_owner, safe='')}/repos?per_page=100&page={page}")
            if not payload:
                break
            if not isinstance(payload, list):
                raise RuntimeError("GitHub org repo listing returned a non-list payload.")
            repos.extend(payload)
            if len(payload) < 100:
                break
            page += 1
        return repos

    def ensure_repo(self, repo_name: str, description: str = "") -> dict[str, Any]:
        existing = self.get_repo(repo_name)
        if existing:
            return existing
        payload = {
            "name": repo_name,
            "description": description,
            "private": self._config.git_repo_visibility.lower() != "public",
            "auto_init": False,
            "has_issues": True,
            "has_projects": False,
            "has_wiki": False,
        }
        created = self._request("POST", f"/orgs/{urllib.parse.quote(self._config.git_owner, safe='')}/repos", payload)
        return created

    def ensure_default_branch(self, repo_name: str, branch_name: str) -> dict[str, Any] | None:
        repo = self.get_repo(repo_name)
        if not repo:
            return None
        if repo.get("default_branch") == branch_name:
            return repo
        encoded_owner = urllib.parse.quote(self._config.git_owner, safe="")
        encoded_repo = urllib.parse.quote(repo_name, safe="")
        return self._request("PATCH", f"/repos/{encoded_owner}/{encoded_repo}", {"default_branch": branch_name})

    def clone_url(self, repo_name: str) -> str:
        return f"{self._config.git_base_url}/{self._config.git_owner}/{repo_name}.git"

    def html_url(self, repo_name: str) -> str:
        return f"{self._config.git_base_url}/{self._config.git_owner}/{repo_name}"

    def normalized_metadata(self, repo_name: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        repo = payload or self.get_repo(repo_name) or {}
        owner = repo.get("owner", {}) if isinstance(repo.get("owner"), dict) else {}
        return {
            "provider": "github",
            "name": repo.get("name", repo_name),
            "full_name": repo.get("full_name", f"{self._config.git_owner}/{repo_name}"),
            "html_url": repo.get("html_url", self.html_url(repo_name)),
            "clone_url": repo.get("clone_url", self.clone_url(repo_name)),
            "default_branch": repo.get("default_branch", self._config.arq_lab_default_branch),
            "private": repo.get("private", self._config.git_repo_visibility.lower() != "public"),
            "visibility": repo.get("visibility", self._config.git_repo_visibility),
            "owner": {
                "login": owner.get("login", self._config.git_owner),
                "html_url": owner.get("html_url", f"{self._config.git_base_url}/{self._config.git_owner}"),
            },
        }
