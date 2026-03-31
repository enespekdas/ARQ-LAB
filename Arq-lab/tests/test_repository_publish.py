from __future__ import annotations

import json
from pathlib import Path

from tooling.env import load_config
from tooling.repository_publish import collect_published_repository_inventory


def test_load_config_defaults_to_github_org_and_repositories_root(tmp_path: Path) -> None:
    (tmp_path / ".env").write_text(
        "\n".join(
            [
                "ARQ_API_BASE_URL=http://localhost:8080",
                "ARQ_WORKSPACE_KEY=default",
                "ARQ_EMAIL=admin",
                "ARQ_PASSWORD=admin",
                "GIT_OWNER=ARQ-Sec",
                "REPOSITORIES_ROOT=repositories",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    config = load_config(tmp_path)

    assert config.git_owner == "ARQ-Sec"
    assert config.git_base_url == "https://github.com"
    assert config.repositories_root == tmp_path / "repositories"
    assert config.repositories_root.exists()


def test_collect_published_repository_inventory_reads_legacy_and_new_metadata(tmp_path: Path) -> None:
    runs_root = tmp_path / "runs" / "20260331T120000Z"
    legacy_root = runs_root / "M1" / "G-V1-PY-002"
    legacy_root.mkdir(parents=True)
    (legacy_root / "gitea-repository.json").write_text(
        json.dumps(
            {
                "name": "notification-worker-python-20260331t120000z",
                "full_name": "arq/notification-worker-python-20260331t120000z",
                "clone_url": "http://localhost:3001/arq/notification-worker-python-20260331t120000z.git",
                "html_url": "http://localhost:3001/arq/notification-worker-python-20260331t120000z",
                "default_branch": "main",
                "owner": {"login": "arq"},
            }
        ),
        encoding="utf-8",
    )
    (legacy_root / "scenario-metadata.json").write_text(
        json.dumps({"scenario": {"id": "G-V1-PY-002", "milestone": "M1", "repo_name": "notification-worker-python"}}),
        encoding="utf-8",
    )

    new_root = runs_root / "M1" / "G-V1-JAVA-001"
    new_root.mkdir(parents=True)
    (new_root / "published-repository.json").write_text(
        json.dumps(
            {
                "provider": "github",
                "name": "payments-service-java",
                "full_name": "ARQ-Sec/payments-service-java",
                "clone_url": "https://github.com/ARQ-Sec/payments-service-java.git",
                "html_url": "https://github.com/ARQ-Sec/payments-service-java",
                "default_branch": "main",
                "owner": {"login": "ARQ-Sec"},
            }
        ),
        encoding="utf-8",
    )
    (new_root / "scenario-metadata.json").write_text(
        json.dumps({"scenario": {"id": "G-V1-JAVA-001", "milestone": "M1", "repo_name": "payments-service-java"}}),
        encoding="utf-8",
    )

    (tmp_path / ".env").write_text("GIT_OWNER=ARQ-Sec\nREPOSITORIES_ROOT=repositories\n", encoding="utf-8")
    config = load_config(tmp_path)

    inventory = collect_published_repository_inventory(config)

    assert [item["sourceOwnerRepo"] for item in inventory] == [
        "ARQ-Sec/payments-service-java",
        "arq/notification-worker-python-20260331t120000z",
    ]
    assert inventory[0]["targetOwnerRepo"] == "ARQ-Sec/payments-service-java"
    assert inventory[1]["logicalRepoSlug"] == "notification-worker-python"
    assert inventory[1]["sourceProvider"] == "gitea"
