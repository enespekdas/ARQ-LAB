from __future__ import annotations

import csv
from io import StringIO
from pathlib import Path
from typing import Any

from .utils import ensure_dir, write_json, write_text


def render_scenario_report(scenario: dict[str, Any], comparison: dict[str, Any], scans: list[dict[str, Any]]) -> str:
    lines = [
        f"# {scenario['id']} — {scenario['repo_name']}",
        "",
        f"- Milestone: `{scenario['milestone']}`",
        f"- Module: `{scenario['module']}`",
        f"- Verdict: `{comparison['verdict']}`",
        f"- Stack: `{scenario['stack']}`",
        f"- Domain: {scenario['domain']}",
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
    return {"scenarioCount": len(comparisons), "verdicts": verdict_counts, "byMilestone": by_milestone}


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
    markdown_lines.append("")
    markdown_lines.append("## Milestones")
    for milestone, summary in sorted(aggregate["byMilestone"].items()):
        markdown_lines.append(
            f"- `{milestone}`: scenarios=`{summary['scenarios']}`, missing=`{summary['mustFindMissing']}`, fp=`{summary['mustNotFindViolations']}`, noise=`{summary['extraFindings']}`, explainability=`{summary['explainabilityFailures']}`, ref-state=`{summary['refStateFailures']}`"
        )
    write_text(root / "aggregate-summary.md", "\n".join(markdown_lines).rstrip() + "\n")

    csv_buffer = StringIO()
    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=["milestone", "scenarios", "mustFindMissing", "mustNotFindViolations", "extraFindings", "explainabilityFailures", "refStateFailures"],
    )
    writer.writeheader()
    for milestone, summary in sorted(aggregate["byMilestone"].items()):
        writer.writerow({"milestone": milestone, **summary})
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
        }
        for comparison in comparisons
        if comparison["verdict"] != "PASS"
    ]
    write_json(root / "fail-buckets.json", fail_buckets)

    tuning_lines = [
        "# Tuning Backlog Seed",
        "",
        "Generated from current scenario comparison buckets.",
        "",
    ]
    for bucket in fail_buckets:
        tuning_lines.append(
            f"- `{bucket['scenarioId']}` / `{bucket['verdict']}`: missing=`{bucket['mustFindMissing']}`, fp=`{bucket['mustNotFindViolations']}`, noise=`{bucket['extraFindings']}`, explainability=`{bucket['explainabilityFailures']}`, ref-state=`{bucket['refStateFailures']}`"
        )
    write_text(root / "tuning-backlog-seed.md", "\n".join(tuning_lines).rstrip() + "\n")

    explainability_lines = [
        "# Explainability Scorecard",
        "",
        f"- Total scenarios: `{aggregate['scenarioCount']}`",
        f"- Scenarios with explainability failures: `{sum(1 for item in comparisons if item['explainabilityFailures'])}`",
    ]
    write_text(root / "explainability-scorecard.md", "\n".join(explainability_lines).rstrip() + "\n")

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
        ]
    )
    write_text(root / "FINAL_VALIDATION_STATUS.md", "\n".join(final_lines).rstrip() + "\n")
