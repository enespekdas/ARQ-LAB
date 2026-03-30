from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .logging_utils import log_event
from .utils import run_command, safe_rmtree


class GitFactory:
    def __init__(self, *, workspace_root: Path, user_name: str = "ARQ Lab", user_email: str = "lab@arq.local") -> None:
        self.workspace_root = workspace_root
        self.user_name = user_name
        self.user_email = user_email

    def recreate_repository(self, repo_root: Path) -> None:
        safe_rmtree(repo_root, self.workspace_root)
        repo_root.mkdir(parents=True, exist_ok=True)

    def init(self, repo_root: Path, default_branch: str = "main") -> None:
        run_command(["git", "init", "-b", default_branch], repo_root, check=True)
        run_command(["git", "config", "user.name", self.user_name], repo_root, check=True)
        run_command(["git", "config", "user.email", self.user_email], repo_root, check=True)

    def add_all(self, repo_root: Path) -> None:
        run_command(["git", "add", "."], repo_root, check=True)

    def commit_all(self, repo_root: Path, message: str, *, allow_empty: bool = False) -> str:
        command = ["git", "commit", "-m", message]
        if allow_empty:
            command.insert(2, "--allow-empty")
        run_command(command, repo_root, check=True)
        return self.current_sha(repo_root)

    def current_sha(self, repo_root: Path) -> str:
        result = run_command(["git", "rev-parse", "HEAD"], repo_root, check=True)
        return result.stdout.strip()

    def checkout(self, repo_root: Path, branch: str, *, create: bool = False, start_point: str | None = None) -> None:
        command = ["git", "checkout"]
        if create:
            command.append("-b")
        command.append(branch)
        if start_point:
            command.append(start_point)
        run_command(command, repo_root, check=True)

    def merge(self, repo_root: Path, source_branch: str, *, message: str) -> None:
        run_command(["git", "merge", "--no-ff", source_branch, "-m", message], repo_root, check=True)

    def set_remote(self, repo_root: Path, name: str, url: str) -> None:
        existing = run_command(["git", "remote"], repo_root, check=False)
        if name in existing.stdout.split():
            run_command(["git", "remote", "set-url", name, url], repo_root, check=True)
        else:
            run_command(["git", "remote", "add", name, url], repo_root, check=True)

    def push_all(self, repo_root: Path, remote_name: str = "origin") -> None:
        run_command(["git", "push", "--force", "--all", remote_name], repo_root, check=True)
        run_command(["git", "push", "--force", "--tags", remote_name], repo_root, check=True)

    def branch_shas(self, repo_root: Path) -> dict[str, str]:
        result = run_command(["git", "for-each-ref", "--format=%(refname:short) %(objectname)", "refs/heads"], repo_root, check=True)
        mapping: dict[str, str] = {}
        for line in result.stdout.splitlines():
            if not line.strip():
                continue
            branch, sha = line.strip().split(" ", 1)
            mapping[branch] = sha
        return mapping

    def commit_timeline(self, repo_root: Path) -> list[dict[str, Any]]:
        result = run_command(
            ["git", "log", "--all", "--date=iso-strict", "--pretty=format:%H%x1f%an%x1f%ae%x1f%ad%x1f%s"],
            repo_root,
            check=True,
        )
        timeline = []
        for line in result.stdout.splitlines():
            sha, author_name, author_email, authored_at, message = line.split("\x1f")
            timeline.append(
                {
                    "sha": sha,
                    "authorName": author_name,
                    "authorEmail": author_email,
                    "authoredAt": authored_at,
                    "message": message,
                }
            )
        return timeline

    def manifest(self, repo_root: Path) -> dict[str, Any]:
        manifest = {
            "head": self.current_sha(repo_root),
            "branches": self.branch_shas(repo_root),
            "timeline": self.commit_timeline(repo_root),
        }
        log_event("git.manifest", repo=str(repo_root), branches=list(manifest["branches"].keys()))
        return manifest

    def write_manifest(self, repo_root: Path, destination: Path) -> None:
        destination.write_text(json.dumps(self.manifest(repo_root), indent=2, sort_keys=True), encoding="utf-8", newline="\n")

