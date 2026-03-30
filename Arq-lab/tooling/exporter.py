from __future__ import annotations

from typing import Any

from .arq_client import ArqClient
from .models import LabConfig, ScenarioSpec


def fetch_scan_export(
    client: ArqClient,
    config: LabConfig,
    scenario: ScenarioSpec,
    application_id: str,
    branch_name: str | None = None,
) -> dict[str, Any]:
    return client.export_findings(
        application_id=application_id,
        module=None if scenario.module == "both" else scenario.module,
        branch_name=branch_name,
        limit=config.findings_export_limit,
    )


def fetch_finding_details(client: ArqClient, finding_ids: list[str]) -> dict[str, dict[str, Any]]:
    details: dict[str, dict[str, Any]] = {}
    for finding_id in finding_ids:
        details[finding_id] = client.get_finding(finding_id)
    return details

