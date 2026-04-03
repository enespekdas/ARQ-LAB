from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .arq_client import ArqClient
from .comparator import compare_scenario
from .env import load_config
from .exporter import fetch_finding_details, fetch_scan_export
from .git_factory import GitFactory
from .github_client import GitHubClient
from .logging_utils import log_event
from .models import BuildStatus, ScenarioSpec
from .project_dossier import write_project_dossier
from .report_renderer import aggregate_comparisons, write_aggregate_reports, write_scenario_report
from .repo_builders import materialize_scenario
from .scan_runner import run_scan_plan
from .scenarios import milestone_order, milestone_specs, scenario_specs
from .utils import CommandResult, ensure_dir, read_json, run_command, timestamp_slug, write_json, write_text


MILESTONE_REPORT_NAMES = {
    "M1": "M1-guardian-live-surfaces",
    "M2": "M2-guardian-history-refstate",
    "M3": "M3-quantum-weak-crypto-java-csharp",
    "M4": "M4-quantum-weak-crypto-polyglot",
    "M5": "M5-quantum-tls-java-python",
    "M6": "M6-quantum-tls-node-csharp-config",
    "M7": "M7-adversarial-negatives",
    "M8": "M8-mixed-enterprise-repos",
}

NON_FAILING_VERDICTS = {"PASS", "PASS_CLEAN", "PASS_WITH_NOISE"}


def _application_key_for_scenario(scenario: ScenarioSpec) -> str:
    return f"arq-lab-{scenario.id.lower()}"


def _is_live_finding(item: dict[str, Any]) -> bool:
    detail = item.get("detail", {})
    if not isinstance(detail, dict):
        detail = {}
    detection_state = str(detail.get("detectionState") or item.get("detectionState") or "").strip().upper()
    if detection_state == "RESOLVED":
        return False
    resolved_at = detail.get("resolvedAt") or item.get("resolvedAt")
    return not (resolved_at and detection_state in {"", "RESOLVED"})


def _execute_plan(plan: list[list[str]], repo_root: Path, *, stage: str, log_root: Path) -> BuildStatus:
    if not plan:
        return BuildStatus(state="skipped", commands=[])
    command_records: list[dict[str, Any]] = []
    for index, command in enumerate(plan, start=1):
        result = run_command(command, repo_root, check=False)
        log_path = ensure_dir(log_root) / f"{stage}-{index:02d}.log"
        write_text(
            log_path,
            "\n".join(
                [
                    f"command: {' '.join(result.command)}",
                    f"cwd: {result.cwd}",
                    f"returncode: {result.returncode}",
                    "",
                    "[stdout]",
                    result.stdout,
                    "",
                    "[stderr]",
                    result.stderr,
                ]
            ).rstrip()
            + "\n",
        )
        command_records.append(
            {
                "command": result.command,
                "cwd": result.cwd,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "logPath": str(log_path),
            }
        )
        if result.returncode != 0:
            return BuildStatus(state="failed", commands=command_records)
    return BuildStatus(state="passed", commands=command_records)


def _bootstrap_foundation(config) -> None:
    scenario_catalog = [
        {
            "id": scenario.id,
            "milestone": scenario.milestone,
            "repo": scenario.repo_name,
            "module": scenario.module,
            "stack": scenario.stack,
            "summary": scenario.summary,
        }
        for scenario in scenario_specs()
    ]
    write_json(config.catalog_root / "scenario-index.json", scenario_catalog)
    write_json(
        config.catalog_root / "milestone-status.json",
        {
            "milestones": [{"id": milestone, "status": "pending"} for milestone in ["M0", *milestone_order(), "M9"]],
        },
    )
    write_text(
        config.catalog_root / "report-contract.md",
        "# Report Contract\n\nScenario reports, milestone reports, and aggregate reports are generated from the comparison.json outputs under `runs/`.\n",
    )
    write_text(
        config.reports_root / "M0-foundation.md",
        "# M0 Foundation\n\n- Created `Arq-lab/` scaffold\n- Added Python automation modules under `tooling/`\n- Added scenario catalog bootstrap files\n- Added report aggregation entrypoints\n",
    )
    write_json(config.runs_root / "empty-run" / "scenario-metadata.json", {"status": "foundation-only"})


def _milestone_report_path(config, milestone: str, suffix: str) -> Path:
    name = MILESTONE_REPORT_NAMES.get(milestone, f"{milestone}-summary")
    return config.reports_root / f"{name}.{suffix}"


def _scenario_dict(scenario: ScenarioSpec) -> dict[str, Any]:
    return {
        "id": scenario.id,
        "milestone": scenario.milestone,
        "repo_name": scenario.repo_name,
        "module": scenario.module,
        "stack": scenario.stack,
        "domain": scenario.domain,
    }


def _scan_plan_dict(scan_plan) -> dict[str, Any]:
    return {
        "name": scan_plan.name,
        "modules": scan_plan.modules,
        "scanMode": scan_plan.scan_mode,
        "branchScope": scan_plan.branch_scope,
        "refName": scan_plan.ref_name,
    }


def _write_milestone_summary(config, milestone: str, comparisons: list[dict[str, Any]]) -> None:
    summary = aggregate_comparisons(comparisons)
    write_json(_milestone_report_path(config, milestone, "json"), summary)
    lines = [
        f"# {milestone} Summary",
        "",
        f"- Scenario count: `{summary['scenarioCount']}`",
        "",
    ]
    for verdict, count in sorted(summary["verdicts"].items()):
        lines.append(f"- `{verdict}`: `{count}`")
    write_text(_milestone_report_path(config, milestone, "md"), "\n".join(lines).rstrip() + "\n")


def _load_all_existing_comparisons(config) -> list[dict[str, Any]]:
    latest_by_scenario: dict[str, tuple[tuple[str, int], dict[str, Any]]] = {}
    for comparison_file in config.runs_root.rglob("comparison.json"):
        payload = read_json(comparison_file, {})
        if not payload:
            continue
        scenario_id = payload.get("scenarioId") or comparison_file.parent.name
        run_stamp = comparison_file.parts[-4] if len(comparison_file.parts) >= 4 else ""
        sort_key = (run_stamp, comparison_file.stat().st_mtime_ns)
        current = latest_by_scenario.get(str(scenario_id))
        if current is None or sort_key >= current[0]:
            latest_by_scenario[str(scenario_id)] = (sort_key, payload)
    return [item for _, item in sorted(latest_by_scenario.values(), key=lambda entry: entry[0])]


def _run_scenario(
    config,
    run_root: Path,
    scenario: ScenarioSpec,
    *,
    dry_run: bool,
    arq: ArqClient | None,
    publisher: GitHubClient | None,
    git_factory: GitFactory,
) -> dict[str, Any]:
    repo_root, repo_metadata = materialize_scenario(config, scenario, git_factory)
    scenario_run_root = ensure_dir(run_root / scenario.id)
    runnability_log_root = ensure_dir(repo_root / "validation" / "runnability-logs")
    build_status = _execute_plan(scenario.build_plan.build, repo_root, stage="build", log_root=runnability_log_root)
    test_status = _execute_plan(scenario.build_plan.test, repo_root, stage="test", log_root=runnability_log_root)
    smoke_status = _execute_plan(scenario.build_plan.smoke, repo_root, stage="smoke", log_root=runnability_log_root)
    runnability = {"build": build_status.state, "test": test_status.state, "smoke": smoke_status.state}
    application = None
    published_repo_metadata = None
    scan_records: list[dict[str, Any]] = []
    actual_findings: list[dict[str, Any]] = []

    if not dry_run and arq and publisher:
        run_repo_name = scenario.repo_name
        repo_payload = publisher.ensure_repo(run_repo_name, scenario.summary)
        git_factory.set_remote(repo_root, "origin", publisher.clone_url(run_repo_name))
        try:
            git_factory.push_all(repo_root)
        except RuntimeError as exc:
            bypasses = publisher.bypass_push_protection_from_error(run_repo_name, str(exc))
            if not bypasses:
                raise
            git_factory.push_all(repo_root)
        publisher.ensure_default_branch(run_repo_name, config.arq_lab_default_branch)
        published_repo_metadata = publisher.normalized_metadata(run_repo_name, repo_payload)

        project = arq.ensure_project(config.arq_lab_project_key, config.arq_lab_project_name, "ARQ Lab Validation")
        application = arq.ensure_application(
            project_id=project["projectId"],
            key=_application_key_for_scenario(scenario),
            name=run_repo_name,
            description=scenario.summary,
            repository_locator=publisher.clone_url(run_repo_name),
            default_branch=config.arq_lab_default_branch,
        )

        for scan_plan in scenario.scan_plans:
            scan_root = ensure_dir(scenario_run_root / scan_plan.name)
            scan_record = run_scan_plan(arq, config, application_id=application["applicationId"], scan_plan=scan_plan)
            branch_name = None if scan_plan.branch_scope == "ALL_BRANCHES" else scan_plan.ref_name
            export_payload = fetch_scan_export(arq, config, scenario, application["applicationId"], branch_name=branch_name)
            finding_ids = [str(item["findingId"]) for item in export_payload.get("items", [])]
            details = fetch_finding_details(arq, finding_ids)
            normalized_items = []
            for item in export_payload.get("items", []):
                normalized = dict(item)
                normalized["detail"] = details.get(str(item["findingId"]), {})
                if not _is_live_finding(normalized):
                    continue
                normalized["scanPlanName"] = scan_plan.name
                normalized_items.append(normalized)
            actual_findings.extend(normalized_items)
            write_json(scan_root / "scan-request.json", {"plan": _scan_plan_dict(scan_plan), "queued": scan_record["requested"]})
            write_json(scan_root / "scan-response.json", scan_record["completed"])
            write_json(scan_root / "findings-export.json", export_payload)
            write_json(scan_root / "finding-details.json", details)
            scan_records.append(
                {
                    "plan": _scan_plan_dict(scan_plan),
                    "requested": scan_record["requested"],
                    "completed": scan_record["completed"],
                    "exportedCount": export_payload.get("exportedCount", 0),
                }
            )

    comparison = compare_scenario(scenario, actual_findings, runnability=runnability)
    comparison.update(
        {
            "auditArtifacts": write_project_dossier(
                config=config,
                scenario=scenario,
                repo_root=repo_root,
                repo_metadata=repo_metadata,
                published_metadata=published_repo_metadata,
                build_status=build_status,
                test_status=test_status,
                smoke_status=smoke_status,
                comparison=comparison,
            )
        }
    )
    write_json(
        scenario_run_root / "scenario-metadata.json",
        {"scenario": _scenario_dict(scenario), "repoMetadata": repo_metadata, "publishedRepository": published_repo_metadata or {}},
    )
    write_json(scenario_run_root / "published-repository.json", published_repo_metadata or {})
    write_json(scenario_run_root / "application.json", application or {})
    write_json(scenario_run_root / "comparison.json", comparison)
    write_json(scenario_run_root / "findings-normalized.json", actual_findings)
    write_scenario_report(scenario_run_root / "report.md", _scenario_dict(scenario), comparison, scan_records)
    return comparison


def run_milestone(config, milestone: str, *, dry_run: bool) -> list[dict[str, Any]]:
    scenarios = milestone_specs(milestone)
    if not scenarios:
        return []
    run_root = ensure_dir(config.runs_root / timestamp_slug() / milestone)
    git_factory = GitFactory(
        workspace_root=config.repositories_root,
        askpass_script=config.toolchains_root / "git-askpass.cmd",
        auth_token=config.git_token,
    )
    arq = None if dry_run else ArqClient(config)
    publisher = None if dry_run else GitHubClient(config)
    comparisons = []
    for scenario in scenarios:
        log_event("scenario.start", scenarioId=scenario.id, milestone=milestone)
        comparisons.append(
            _run_scenario(config, run_root, scenario, dry_run=dry_run, arq=arq, publisher=publisher, git_factory=git_factory)
        )
        log_event("scenario.finish", scenarioId=scenario.id, milestone=milestone)
    _write_milestone_summary(config, milestone, comparisons)
    return comparisons


def main() -> None:
    parser = argparse.ArgumentParser(description="ARQ Lab orchestration")
    parser.add_argument("--milestone", help="Run a single milestone (M0-M9)")
    parser.add_argument("--all", action="store_true", help="Run all milestones")
    parser.add_argument("--dry-run", action="store_true", help="Generate repositories and manifests without remote publish or ARQ execution")
    parser.add_argument("--report-only", action="store_true", help="Rebuild aggregate reports from existing comparisons")
    parser.add_argument("--resume-last-failed", action="store_true", help="Resume milestones that had failing verdicts in the last manifest")
    args = parser.parse_args()

    config = load_config()
    _bootstrap_foundation(config)

    if args.report_only:
        write_aggregate_reports(config.reports_root, _load_all_existing_comparisons(config))
        return

    milestones: list[str] = []
    if args.all:
        milestones = milestone_order()
    elif args.milestone:
        if args.milestone == "M0":
            write_aggregate_reports(config.reports_root, _load_all_existing_comparisons(config))
            return
        milestones = [args.milestone]
    elif args.resume_last_failed:
        last_manifest = read_json(config.manifests_root / "last-run.json", {"failedMilestones": []})
        milestones = last_manifest.get("failedMilestones", [])
    else:
        parser.error("Specify --milestone, --all, --report-only, or --resume-last-failed")

    all_comparisons: list[dict[str, Any]] = []
    for milestone in milestones:
        all_comparisons.extend(run_milestone(config, milestone, dry_run=args.dry_run))

    existing = _load_all_existing_comparisons(config)
    write_aggregate_reports(config.reports_root, existing)
    failed_milestones = sorted({item["milestone"] for item in existing if item.get("verdict") not in NON_FAILING_VERDICTS})
    write_json(config.manifests_root / "last-run.json", {"failedMilestones": failed_milestones, "completedMilestones": milestones})


if __name__ == "__main__":
    main()
