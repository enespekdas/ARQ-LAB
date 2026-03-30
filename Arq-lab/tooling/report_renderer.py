from __future__ import annotations

import csv
from io import StringIO
from pathlib import Path
from typing import Any

from .utils import ensure_dir, write_json, write_text


def render_scenario_report(scenario: dict[str, Any], comparison: dict[str, Any], scans: list[dict[str, Any]]) -> str:
    audit = comparison.get("auditArtifacts", {})
    lines = [
        f"# {scenario['id']} - {scenario['repo_name']}",
        "",
        f"- Milestone: `{scenario['milestone']}`",
        f"- Module: `{scenario['module']}`",
        f"- Verdict: `{comparison['verdict']}`",
        f"- Stack: `{scenario['stack']}`",
        f"- Domain: {scenario['domain']}",
        f"- Dossier: `{audit.get('reportDossierPath', 'n/a')}`",
        "",
        "## Scan summary",
    ]
    for scan in scans:
        completed = scan.get("completed", {})
        lines.append(f"- `{scan['plan']['name']}`: `{completed.get('status', 'UNKNOWN')}` on `{completed.get('scannedRefName') or completed.get('requestedRefName') or 'n/a'}`")
    lines.extend(
        [
            "",
            "## Comparison",
            f"- mustFindMatched: `{comparison['mustFindMatched']}` / `{comparison['mustFindExpected']}`",
            f"- mustFindMissing: `{len(comparison['mustFindMissing'])}`",
            f"- mustNotFindViolations: `{len(comparison['mustNotFindViolations'])}`",
            f"- extraFindings: `{len(comparison['extraFindings'])}`",
            f"- explainabilityFailures: `{len(comparison['explainabilityFailures'])}`",
            f"- refStateFailures: `{len(comparison['refStateFailures'])}`",
            "",
            "## Runnability",
            f"- build: `{comparison['runnability']['build']}`",
            f"- test: `{comparison['runnability']['test']}`",
            f"- smoke: `{comparison['runnability']['smoke']}`",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_scenario_report(destination: Path, scenario: dict[str, Any], comparison: dict[str, Any], scans: list[dict[str, Any]]) -> None:
    write_text(destination, render_scenario_report(scenario, comparison, scans))


def aggregate_comparisons(comparisons: list[dict[str, Any]]) -> dict[str, Any]:
    verdict_counts: dict[str, int] = {}
    by_milestone: dict[str, dict[str, Any]] = {}
    by_scenario: dict[str, dict[str, Any]] = {}
    for comparison in comparisons:
        verdict = comparison["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        milestone_summary = by_milestone.setdefault(
            comparison["milestone"],
            {
                "scenarios": 0,
                "mustFindMissing": 0,
                "mustNotFindViolations": 0,
                "extraFindings": 0,
                "explainabilityFailures": 0,
                "refStateFailures": 0,
            },
        )
        milestone_summary["scenarios"] += 1
        milestone_summary["mustFindMissing"] += len(comparison["mustFindMissing"])
        milestone_summary["mustNotFindViolations"] += len(comparison["mustNotFindViolations"])
        milestone_summary["extraFindings"] += len(comparison["extraFindings"])
        milestone_summary["explainabilityFailures"] += len(comparison["explainabilityFailures"])
        milestone_summary["refStateFailures"] += len(comparison["refStateFailures"])
        audit = comparison.get("auditArtifacts", {})
        loc = audit.get("locComposition", {})
        by_scenario[comparison["scenarioId"]] = {
            "milestone": comparison["milestone"],
            "verdict": comparison["verdict"],
            "mustFindMissing": len(comparison["mustFindMissing"]),
            "mustNotFindViolations": len(comparison["mustNotFindViolations"]),
            "extraFindings": len(comparison["extraFindings"]),
            "explainabilityFailures": len(comparison["explainabilityFailures"]),
            "refStateFailures": len(comparison["refStateFailures"]),
            "dossierPath": audit.get("dossierPath", ""),
            "projectLocalDossierPath": audit.get("projectLocalDossierPath", ""),
            "reportDossierPath": audit.get("reportDossierPath", ""),
            "generatedManifestPath": audit.get("generatedManifestPath", ""),
            "generatedTreePath": audit.get("generatedTreePath", ""),
            "dossierMissing": audit.get("dossierMissing", True),
            "fillerRatio": audit.get("fillerRatio", 0.0),
            "realismScore": audit.get("realismScore"),
            "realismJustification": audit.get("realismJustification", ""),
            "locComposition": loc,
        }
    return {"scenarioCount": len(comparisons), "verdicts": verdict_counts, "byMilestone": by_milestone, "byScenario": by_scenario}


def write_aggregate_reports(root: Path, comparisons: list[dict[str, Any]]) -> None:
    ensure_dir(root)
    aggregate = aggregate_comparisons(comparisons)
    write_json(root / "aggregate-summary.json", aggregate)

    markdown_lines = [
        "# Aggregate Validation Summary",
        "",
        f"- Scenario count: `{aggregate['scenarioCount']}`",
        "",
        "## Verdicts",
    ]
    for verdict, count in sorted(aggregate["verdicts"].items()):
        markdown_lines.append(f"- `{verdict}`: `{count}`")
    markdown_lines.extend(["", "## Milestones"])
    for milestone, summary in sorted(aggregate["byMilestone"].items()):
        markdown_lines.append(
            f"- `{milestone}`: scenarios=`{summary['scenarios']}`, missing=`{summary['mustFindMissing']}`, fp=`{summary['mustNotFindViolations']}`, noise=`{summary['extraFindings']}`, explainability=`{summary['explainabilityFailures']}`, ref-state=`{summary['refStateFailures']}`"
        )
    markdown_lines.extend(["", "## Scenario Auditability"])
    for scenario_id, summary in sorted(aggregate["byScenario"].items()):
        loc = summary.get("locComposition", {})
        markdown_lines.append(
            f"- `{scenario_id}`: verdict=`{summary['verdict']}`, realism=`{summary.get('realismScore', 'n/a')}`, fillerRatio=`{summary.get('fillerRatio', 0.0):.2%}`, dossierMissing=`{summary.get('dossierMissing', True)}`, dossier=`{summary.get('reportDossierPath', 'n/a')}`, liveCode=`{loc.get('live business code', 0)}`, liveConfig=`{loc.get('live config', 0)}`, tests=`{loc.get('tests', 0)}`, filler=`{loc.get('synthetic filler / inflation content', 0)}`"
        )
    write_text(root / "aggregate-summary.md", "\n".join(markdown_lines).rstrip() + "\n")

    csv_buffer = StringIO()
    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=[
            "scenarioId",
            "milestone",
            "verdict",
            "mustFindMissing",
            "mustNotFindViolations",
            "extraFindings",
            "explainabilityFailures",
            "refStateFailures",
            "dossierMissing",
            "fillerRatio",
            "realismScore",
            "dossierPath",
            "liveBusinessCode",
            "liveConfig",
            "tests",
            "docs",
            "scripts",
            "fixtures",
            "vendorGenerated",
            "syntheticFiller",
        ],
    )
    writer.writeheader()
    for scenario_id, summary in sorted(aggregate["byScenario"].items()):
        loc = summary.get("locComposition", {})
        writer.writerow(
            {
                "scenarioId": scenario_id,
                "milestone": summary["milestone"],
                "verdict": summary["verdict"],
                "mustFindMissing": summary["mustFindMissing"],
                "mustNotFindViolations": summary["mustNotFindViolations"],
                "extraFindings": summary["extraFindings"],
                "explainabilityFailures": summary["explainabilityFailures"],
                "refStateFailures": summary["refStateFailures"],
                "dossierMissing": summary["dossierMissing"],
                "fillerRatio": summary["fillerRatio"],
                "realismScore": summary["realismScore"],
                "dossierPath": summary["reportDossierPath"],
                "liveBusinessCode": loc.get("live business code", 0),
                "liveConfig": loc.get("live config", 0),
                "tests": loc.get("tests", 0),
                "docs": loc.get("docs", 0),
                "scripts": loc.get("scripts", 0),
                "fixtures": loc.get("fixtures", 0),
                "vendorGenerated": loc.get("vendor/generated", 0),
                "syntheticFiller": loc.get("synthetic filler / inflation content", 0),
            }
        )
    write_text(root / "aggregate-summary.csv", csv_buffer.getvalue())

    fail_buckets = [
        {
            "scenarioId": comparison["scenarioId"],
            "milestone": comparison["milestone"],
            "verdict": comparison["verdict"],
            "mustFindMissing": len(comparison["mustFindMissing"]),
            "mustNotFindViolations": len(comparison["mustNotFindViolations"]),
            "extraFindings": len(comparison["extraFindings"]),
            "explainabilityFailures": len(comparison["explainabilityFailures"]),
            "refStateFailures": len(comparison["refStateFailures"]),
            "reportDossierPath": comparison.get("auditArtifacts", {}).get("reportDossierPath", ""),
            "dossierMissing": comparison.get("auditArtifacts", {}).get("dossierMissing", True),
        }
        for comparison in comparisons
        if comparison["verdict"] != "PASS"
    ]
    write_json(root / "fail-buckets.json", fail_buckets)

    tuning_lines = ["# Tuning Backlog Seed", "", "Generated from current scenario comparison buckets.", ""]
    for bucket in fail_buckets:
        tuning_lines.append(
            f"- `{bucket['scenarioId']}` / `{bucket['verdict']}`: missing=`{bucket['mustFindMissing']}`, fp=`{bucket['mustNotFindViolations']}`, noise=`{bucket['extraFindings']}`, explainability=`{bucket['explainabilityFailures']}`, ref-state=`{bucket['refStateFailures']}`, dossier=`{bucket['reportDossierPath']}`"
        )
    write_text(root / "tuning-backlog-seed.md", "\n".join(tuning_lines).rstrip() + "\n")

    explainability_lines = [
        "# Explainability Scorecard",
        "",
        f"- Total scenarios: `{aggregate['scenarioCount']}`",
        f"- Scenarios with explainability failures: `{sum(1 for item in comparisons if item['explainabilityFailures'])}`",
    ]
    write_text(root / "explainability-scorecard.md", "\n".join(explainability_lines).rstrip() + "\n")

    dossier_count = sum(1 for item in comparisons if not item.get("auditArtifacts", {}).get("dossierMissing", True))
    final_lines = [
        "# FINAL VALIDATION STATUS",
        "",
        "ARQ-SEC validation summary generated from current milestone runs.",
        "",
        "## Verdict overview",
    ]
    for verdict, count in sorted(aggregate["verdicts"].items()):
        final_lines.append(f"- `{verdict}`: `{count}`")
    final_lines.extend(
        [
            "",
            "## Strengths and gaps",
            "- Strengths: scenarios with `PASS` indicate the current detector and explainability path met the declared contract.",
            "- Noise: scenarios with `PASS_WITH_NOISE` surfaced additional findings beyond the expected contract.",
            "- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, and `FAIL_REF_STATE` scenarios require follow-up.",
            f"- Dossier coverage: `{dossier_count}` / `{aggregate['scenarioCount']}` scenarios have required dossier, manifest, and tree artifacts.",
        ]
    )
    write_text(root / "FINAL_VALIDATION_STATUS.md", "\n".join(final_lines).rstrip() + "\n")
