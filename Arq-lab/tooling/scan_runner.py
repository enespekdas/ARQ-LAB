from __future__ import annotations

from typing import Any

from .arq_client import ArqClient
from .models import LabConfig, ScanPlan


def run_scan_plan(
    client: ArqClient,
    config: LabConfig,
    *,
    application_id: str,
    scan_plan: ScanPlan,
) -> dict[str, Any]:
    queued = client.request_scan(
        application_id=application_id,
        modules=scan_plan.modules,
        scan_mode=scan_plan.scan_mode,
        branch_scope=scan_plan.branch_scope,
        ref_name=scan_plan.ref_name,
    )
    completed = client.poll_scan(
        queued["id"],
        timeout_seconds=config.scan_poll_timeout_seconds,
        interval_seconds=config.scan_poll_interval_seconds,
    )
    return {"requested": queued, "completed": completed, "plan": scan_plan}

