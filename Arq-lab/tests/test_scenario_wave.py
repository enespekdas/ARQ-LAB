from __future__ import annotations

from pathlib import Path

from tooling.env import load_config
from tooling.git_factory import GitFactory
from tooling.repo_builders import materialize_scenario
from tooling.scenarios import scenario_index, scenario_specs
from tooling.utils import run_command


NEW_SCENARIO_IDS = {
    "G-V2-HIST-006",
    "G-V2-HIST-007",
    "G-V2-HIST-008",
    "G-V2-HIST-009",
    "Q-V3-JAVA-005",
    "Q-V3-JAVA-006",
    "Q-V3-CS-004",
    "Q-V4-PY-005",
    "Q-V4-TS-005",
    "Q-V4-GO-003",
    "Q-V5-JAVA-005",
    "Q-V5-JAVA-006",
    "Q-V5-PY-003",
    "Q-V6-TS-002",
    "Q-V6-CS-003",
    "Q-V6-CONFIG-005",
    "N-V7-DOCS-009",
    "N-V7-DOCS-010",
    "N-V7-VENDOR-011",
    "N-V7-SAFE-012",
    "M-V8-005",
    "M-V8-006",
    "M-V8-007",
    "M-V8-008",
}


def _config(tmp_path: Path):
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
    return load_config(tmp_path)


def test_scenario_specs_include_24_new_ids_and_minimum_suite_size() -> None:
    ids = [scenario.id for scenario in scenario_specs()]

    assert len(ids) == len(set(ids))
    assert len(ids) >= 61
    assert NEW_SCENARIO_IDS.issubset(ids)


def test_materialize_new_mixed_monorepo_variants_with_history_and_negative_surfaces(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    repo_root_005, _ = materialize_scenario(config, scenarios["M-V8-005"], git_factory)
    assert (repo_root_005 / "vendor" / "third-party-sdk.js").exists()
    assert (repo_root_005 / "generated" / "openapi" / "mesh-client.ts").exists()
    assert (repo_root_005 / "packages" / "shared-fixtures" / "seed.json").exists()

    repo_root_007, _ = materialize_scenario(config, scenarios["M-V8-007"], git_factory)
    assert not (repo_root_007 / "shared" / "config" / "legacy.env").exists()
    branches = git_factory.branch_shas(repo_root_007)
    assert {"main", "feature/shared-lib-cleanup", "release/2026.05"}.issubset(branches)
    history = run_command(["git", "log", "--all", "--name-only", "--", "shared/config/legacy.env"], repo_root_007, check=True)
    assert "shared/config/legacy.env" in history.stdout


def test_materialize_new_mixed_infra_variants_with_overlay_noise_and_branches(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    repo_root_006, _ = materialize_scenario(config, scenarios["M-V8-006"], git_factory)
    assert (repo_root_006 / "deploy" / "examples" / "envoy.yaml").exists()
    assert (repo_root_006 / "kustomize" / "fixtures" / "dev.env").exists()
    assert (repo_root_006 / ".github" / "workflows" / "deploy.yml").exists()

    repo_root_008, _ = materialize_scenario(config, scenarios["M-V8-008"], git_factory)
    branches = git_factory.branch_shas(repo_root_008)
    assert {"main", "feature/hotfix-ssl", "release/2026.04", "feature/charts-cleanup"}.issubset(branches)
    assert (repo_root_008 / "deploy" / "examples" / "envoy.yaml").exists()
    assert (repo_root_008 / "generated" / "manifests" / "envoy-example.yaml").exists()


def test_materialize_history_cherrypick_wave_creates_expected_branches(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenario = scenario_index()["G-V2-HIST-007"]

    repo_root, _ = materialize_scenario(config, scenario, git_factory)

    branches = git_factory.branch_shas(repo_root)
    assert {"main", "feature/customer-hotfix", "release/2026.05", "hotfix/cherry-picked-docs"}.issubset(branches)
    assert not (repo_root / "src" / "modules" / "partner" / "bootstrap" / "featureBranchToken.ts").exists()
    history = run_command(["git", "log", "hotfix/cherry-picked-docs", "--name-only", "--", "docs/branch-chore.md"], repo_root, check=True)
    assert "docs/branch-chore.md" in history.stdout
