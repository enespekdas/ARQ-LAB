from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .logging_utils import log_event
from .utils import run_command, safe_rmtree


class GitPushError(RuntimeError):
    def __init__(self, command: list[str], stdout: str, stderr: str) -> None:
        self.command = command
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(
            "Command failed: %s\nstdout:\n%s\nstderr:\n%s"
            % (" ".join(command), stdout.strip(), stderr.strip())
        )


class GitFactory:
    def __init__(
        self,
        *,
        workspace_root: Path,
        user_name: str = "ARQ Lab",
        user_email: str = "lab@arq.local",
        askpass_script: Path | None = None,
        auth_username: str = "x-access-token",
        auth_token: str = "",
    ) -> None:
        self.workspace_root = workspace_root
        self.user_name = user_name
        self.user_email = user_email
        self.askpass_script = askpass_script
        self.auth_username = auth_username
        self.auth_token = auth_token

    def _git_auth_env(self) -> dict[str, str] | None:
        if not self.auth_token or not self.askpass_script:
            return None
        return {
            "GIT_TERMINAL_PROMPT": "0",
            "GCM_INTERACTIVE": "Never",
            "GIT_ASKPASS": str(self.askpass_script),
            "ARQ_GIT_ASKPASS_USERNAME": self.auth_username,
            "ARQ_GIT_ASKPASS_PASSWORD": self.auth_token,
        }

    def is_repository(self, repo_root: Path) -> bool:
        return (repo_root / ".git").exists()

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

    def current_branch(self, repo_root: Path) -> str:
        result = run_command(["git", "branch", "--show-current"], repo_root, check=True)
        return result.stdout.strip()

    def merge(self, repo_root: Path, source_branch: str, *, message: str) -> None:
        run_command(["git", "merge", "--no-ff", source_branch, "-m", message], repo_root, check=True)

    def clone(self, repo_url: str, destination: Path, *, remote_name: str = "origin") -> None:
        safe_rmtree(destination, self.workspace_root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        run_command(["git", "clone", "--origin", remote_name, repo_url, str(destination)], destination.parent, check=True)
        run_command(["git", "config", "user.name", self.user_name], destination, check=True)
        run_command(["git", "config", "user.email", self.user_email], destination, check=True)

    def fetch(self, repo_root: Path, remote_name: str) -> None:
        run_command(
            ["git", "fetch", "--prune", remote_name, f"+refs/heads/*:refs/remotes/{remote_name}/*"],
            repo_root,
            check=True,
        )
        run_command(["git", "fetch", "--tags", remote_name], repo_root, check=True)

    def list_remote_branches(self, repo_root: Path, remote_name: str) -> list[str]:
        result = run_command(
            ["git", "for-each-ref", "--format=%(refname:short)", f"refs/remotes/{remote_name}"],
            repo_root,
            check=True,
        )
        prefix = f"{remote_name}/"
        branches = []
        for line in result.stdout.splitlines():
            branch = line.strip()
            if not branch or branch == f"{remote_name}/HEAD" or not branch.startswith(prefix):
                continue
            branches.append(branch[len(prefix) :])
        return branches

    def sync_remote_branches_to_local_heads(self, repo_root: Path, remote_name: str) -> None:
        current_branch = self.current_branch(repo_root)
        branches = self.list_remote_branches(repo_root, remote_name)
        if current_branch and current_branch in branches:
            run_command(["git", "checkout", "--detach"], repo_root, check=True)
        for branch in branches:
            run_command(["git", "branch", "-f", branch, f"{remote_name}/{branch}"], repo_root, check=True)
        if current_branch and current_branch in branches:
            run_command(["git", "checkout", current_branch], repo_root, check=True)

    def set_remote(self, repo_root: Path, name: str, url: str) -> None:
        existing = run_command(["git", "remote"], repo_root, check=False)
        if name in existing.stdout.split():
            run_command(["git", "remote", "set-url", name, url], repo_root, check=True)
        else:
            run_command(["git", "remote", "add", name, url], repo_root, check=True)

    def push_all(self, repo_root: Path, remote_name: str = "origin") -> None:
        auth_env = self._git_auth_env()
        self._push_with_retry(["git", "push", "--force", "--all", remote_name], repo_root, auth_env)
        self._push_with_retry(["git", "push", "--force", "--tags", remote_name], repo_root, auth_env)

    def _push_with_retry(self, command: list[str], repo_root: Path, auth_env: dict[str, str] | None) -> None:
        attempts = 0
        max_attempts = 6
        while attempts < max_attempts:
            result = run_command(command, repo_root, env=auth_env, check=False)
            if result.ok():
                return
            attempts += 1
            if attempts >= max_attempts or not self._is_repo_not_ready_error(result):
                raise GitPushError(result.command, result.stdout, result.stderr)
            time.sleep(2)

    @staticmethod
    def _is_repo_not_ready_error(result) -> bool:
        stderr = (result.stderr or "").lower()
        stdout = (result.stdout or "").lower()
        combined = "\n".join([stdout, stderr])
        return "repository not found" in combined

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
