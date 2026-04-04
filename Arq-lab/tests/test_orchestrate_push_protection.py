from __future__ import annotations

from pathlib import Path

from tooling.git_factory import GitPushError
from tooling.orchestrate import _push_repo_with_push_protection_bypass


class _StubGitFactory:
    def __init__(self) -> None:
        self.calls = 0

    def push_all(self, repo_root: Path) -> None:
        self.calls += 1
        if self.calls == 1:
            raise GitPushError(
                ["git", "push", "--force", "--all", "origin"],
                "",
                "remote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/AAA\n"
                "remote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/BBB\n",
            )
        if self.calls == 2:
            raise GitPushError(
                ["git", "push", "--force", "--all", "origin"],
                "",
                "remote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/CCC\n",
            )


class _StubPublisher:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, str]] = []

    @staticmethod
    def push_protection_placeholder_ids(error_text: str) -> list[str]:
        ids = []
        for token in ("AAA", "BBB", "CCC"):
            if token in error_text:
                ids.append(token)
        return ids

    def create_push_protection_bypass(self, repo_name: str, placeholder_id: str, *, reason: str = "used_in_tests") -> dict[str, str]:
        self.calls.append((repo_name, placeholder_id, reason))
        return {"repo": repo_name, "placeholder_id": placeholder_id, "reason": reason}


def test_push_repo_with_push_protection_bypass_loops_until_push_succeeds(tmp_path: Path) -> None:
    git_factory = _StubGitFactory()
    publisher = _StubPublisher()

    _push_repo_with_push_protection_bypass(git_factory, publisher, tmp_path, "guardian-coverage-automation")

    assert git_factory.calls == 3
    assert publisher.calls == [
        ("guardian-coverage-automation", "AAA", "used_in_tests"),
        ("guardian-coverage-automation", "BBB", "used_in_tests"),
        ("guardian-coverage-automation", "CCC", "used_in_tests"),
    ]
