from __future__ import annotations

from pathlib import Path

from tooling.env import load_config
from tooling.github_client import GitHubClient


def _config(tmp_path: Path):
    (tmp_path / ".env").write_text(
        "\n".join(
            [
                "ARQ_API_BASE_URL=http://localhost:8080",
                "ARQ_WORKSPACE_KEY=default",
                "ARQ_EMAIL=admin",
                "ARQ_PASSWORD=admin",
                "GIT_BASE_URL=https://github.com",
                "GIT_API_BASE_URL=https://api.github.com",
                "GIT_OWNER=ARQ-Sec",
                "GIT_TOKEN=test-token",
                "REPOSITORIES_ROOT=repositories",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return load_config(tmp_path)


def test_push_protection_placeholder_ids_extracts_unique_ids() -> None:
    error_text = """
remote:
https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/ABC123
remote:
https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/ABC123
remote:
https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/XYZ987
"""

    assert GitHubClient.push_protection_placeholder_ids(error_text) == ["ABC123", "XYZ987"]


def test_bypass_push_protection_from_error_posts_each_placeholder(monkeypatch, tmp_path: Path) -> None:
    client = GitHubClient(_config(tmp_path))
    calls: list[tuple[str, str, dict[str, str]]] = []

    def fake_request(method: str, path: str, payload=None):  # type: ignore[no-untyped-def]
        calls.append((method, path, payload))
        return {"ok": True, "placeholder_id": payload["placeholder_id"]}

    monkeypatch.setattr(client, "_request", fake_request)

    payloads = client.bypass_push_protection_from_error(
        "guardian-coverage-cloud",
        "remote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/AAA\nremote: https://github.com/ARQ-Sec/example/security/secret-scanning/unblock-secret/BBB",
    )

    assert payloads == [{"ok": True, "placeholder_id": "AAA"}, {"ok": True, "placeholder_id": "BBB"}]
    assert calls == [
        ("POST", "/repos/ARQ-Sec/guardian-coverage-cloud/secret-scanning/push-protection-bypasses", {"reason": "used_in_tests", "placeholder_id": "AAA"}),
        ("POST", "/repos/ARQ-Sec/guardian-coverage-cloud/secret-scanning/push-protection-bypasses", {"reason": "used_in_tests", "placeholder_id": "BBB"}),
    ]
