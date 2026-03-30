from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class LabConfig:
    arq_api_base_url: str
    arq_workspace_key: str
    arq_email: str
    arq_password: str
    gitea_base_url: str
    gitea_username: str
    gitea_password: str
    gitea_owner: str
    gitea_repo_visibility: str
    arq_lab_project_key: str
    arq_lab_project_name: str
    arq_lab_default_branch: str
    scan_poll_interval_seconds: int
    scan_poll_timeout_seconds: int
    findings_export_limit: int
    lab_root: Path
    generated_root: Path
    reports_root: Path
    runs_root: Path
    manifests_root: Path
    catalog_root: Path
    templates_root: Path
    prompts_root: Path
    docs_root: Path
    toolchains_root: Path


@dataclass(slots=True)
class ScanPlan:
    name: str
    modules: list[str]
    scan_mode: str
    branch_scope: str = "SINGLE_BRANCH"
    ref_name: str | None = "main"


@dataclass(slots=True)
class ExpectedFinding:
    key: str
    path_contains: str
    rule_key_contains: str | None = None
    resolved_value_contains: str | None = None
    query_family_contains: str | None = None
    branch_name: str | None = None
    present_on_head: bool | None = None
    present_in_history: bool | None = None
    exposure_scope: str | None = None
    finding_kind: str | None = None
    detection_source: str | None = None


@dataclass(slots=True)
class ExpectedAbsent:
    key: str
    path_contains: str
    rule_key_contains: str | None = None
    resolved_value_contains: str | None = None


@dataclass(slots=True)
class ExplainabilityExpectation:
    key: str
    path_contains: str
    resolved_value_contains: str | None = None
    query_family_contains: str | None = None
    resolution_scope_contains: str | None = None
    detection_source_contains: str | None = None


@dataclass(slots=True)
class BuildPlan:
    build: list[list[str]] = field(default_factory=list)
    test: list[list[str]] = field(default_factory=list)
    smoke: list[list[str]] = field(default_factory=list)


@dataclass(slots=True)
class ScenarioSpec:
    id: str
    milestone: str
    repo_name: str
    module: str
    family: str
    stack: str
    domain: str
    summary: str
    line_target: str
    scan_plans: list[ScanPlan]
    build_plan: BuildPlan
    expected_findings: list[ExpectedFinding] = field(default_factory=list)
    expected_absent: list[ExpectedAbsent] = field(default_factory=list)
    explainability_expectations: list[ExplainabilityExpectation] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class BuildStatus:
    state: str
    commands: list[dict[str, Any]]


@dataclass(slots=True)
class ScenarioRunArtifacts:
    scenario: ScenarioSpec
    repo_root: Path
    repo_line_count: int
    repo_metadata: dict[str, Any]
    build: BuildStatus
    test: BuildStatus
    smoke: BuildStatus
    gitea_metadata: dict[str, Any] | None = None
    application: dict[str, Any] | None = None
    scans: list[dict[str, Any]] = field(default_factory=list)
    comparison: dict[str, Any] | None = None

