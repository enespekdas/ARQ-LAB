from __future__ import annotations

from pathlib import Path

from tooling.git_factory import GitFactory, GitPushError
from tooling.utils import CommandResult


def test_push_all_retries_until_repo_becomes_available(monkeypatch, tmp_path: Path) -> None:
    git_factory = GitFactory(workspace_root=tmp_path)
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    calls: list[list[str]] = []

    def fake_run_command(command, cwd, *, env=None, timeout=None, check=False):  # type: ignore[no-untyped-def]
        calls.append(command)
        if command[:4] == ["git", "push", "--force", "--all"] and len(calls) == 1:
            return CommandResult(command=command, cwd=str(cwd), returncode=128, stdout="", stderr="remote: Repository not found.")
        return CommandResult(command=command, cwd=str(cwd), returncode=0, stdout="", stderr="")

    monkeypatch.setattr("tooling.git_factory.run_command", fake_run_command)
    monkeypatch.setattr("tooling.git_factory.time.sleep", lambda _: None)

    git_factory.push_all(repo_root)

    assert calls == [
        ["git", "push", "--force", "--all", "origin"],
        ["git", "push", "--force", "--all", "origin"],
        ["git", "push", "--force", "--tags", "origin"],
    ]


def test_push_all_stops_retrying_for_non_retryable_error(monkeypatch, tmp_path: Path) -> None:
    git_factory = GitFactory(workspace_root=tmp_path)
    repo_root = tmp_path / "repo"
    repo_root.mkdir()

    def fake_run_command(command, cwd, *, env=None, timeout=None, check=False):  # type: ignore[no-untyped-def]
        return CommandResult(command=command, cwd=str(cwd), returncode=128, stdout="", stderr="fatal: some other error")

    monkeypatch.setattr("tooling.git_factory.run_command", fake_run_command)
    monkeypatch.setattr("tooling.git_factory.time.sleep", lambda _: None)

    try:
        git_factory.push_all(repo_root)
    except RuntimeError as exc:
        assert "some other error" in str(exc)
    else:
        raise AssertionError("Expected push_all to raise for non-retryable errors.")


def test_push_all_raises_git_push_error_with_stdout_stderr(monkeypatch, tmp_path: Path) -> None:
    git_factory = GitFactory(workspace_root=tmp_path)
    repo_root = tmp_path / "repo"
    repo_root.mkdir()

    def fake_run_command(command, cwd, *, env=None, timeout=None, check=False):  # type: ignore[no-untyped-def]
        return CommandResult(
            command=command,
            cwd=str(cwd),
            returncode=128,
            stdout="remote: blocked",
            stderr="remote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/AAA",
        )

    monkeypatch.setattr("tooling.git_factory.run_command", fake_run_command)
    monkeypatch.setattr("tooling.git_factory.time.sleep", lambda _: None)

    try:
        git_factory.push_all(repo_root)
    except GitPushError as exc:
        assert "remote: blocked" in exc.stdout
        assert "unblock-secret/AAA" in exc.stderr
    else:
        raise AssertionError("Expected push_all to raise GitPushError.")
