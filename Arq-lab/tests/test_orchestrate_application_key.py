from __future__ import annotations

from tooling.models import BuildPlan, ScenarioSpec
from tooling.orchestrate import _application_key_for_scenario


def _scenario(scenario_id: str, repo_name: str) -> ScenarioSpec:
    return ScenarioSpec(
        id=scenario_id,
        milestone="M4",
        repo_name=repo_name,
        module="quantum",
        family="weak-crypto",
        stack="TypeScript / Node",
        domain="Test domain",
        summary="Test summary",
        line_target="small",
        scan_plans=[],
        build_plan=BuildPlan(),
    )


def test_application_key_is_stable_across_runs_for_same_scenario() -> None:
    scenario = _scenario("Q-V4-TS-003", "customer-portal-node")

    assert _application_key_for_scenario(scenario) == "arq-lab-q-v4-ts-003"


def test_application_key_ignores_repo_slug_churn_and_uses_scenario_identity() -> None:
    original = _scenario("M-V8-002", "infra-app-mixed-repo")
    renamed_slug = _scenario("M-V8-002", "infra-app-mixed-repo-v2")

    assert _application_key_for_scenario(original) == _application_key_for_scenario(renamed_slug)
