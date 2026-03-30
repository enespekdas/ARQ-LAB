from __future__ import annotations

import csv
from io import StringIO
from pathlib import Path
from typing import Any

from .utils import ensure_dir, write_json, write_text
from .verdict_proof import PROOF_SCENARIO_ID, build_pass_with_noise_proof

STANDARD_VERDICTS = (
    "PASS_CLEAN",
    "PASS_WITH_NOISE",
    "FAIL_FN",
    "FAIL_FP",
    "FAIL_EXPLAINABILITY",
    "FAIL_REF_STATE",
    "INVALID_SCENARIO",
)


def _count(comparison: dict[str, Any], key: str) -> int:
    return len(comparison.get(key, []))


def _verdict_class(comparison: dict[str, Any]) -> str:
    return comparison.get("verdictClass") or comparison.get("verdict", "UNKNOWN")


def _noise_breakdown(comparison: dict[str, Any]) -> dict[str, int]:
    breakdown = comparison.get("noiseBreakdown", {})
    return breakdown if isinstance(breakdown, dict) else {}


def _noise_breakdown_text(comparison: dict[str, Any]) -> str:
    breakdown = _noise_breakdown(comparison)
    parts = [f"{key}={value}" for key, value in breakdown.items() if value]
    return ", ".join(parts) if parts else "none"


def _ordered_verdict_counts(counts: dict[str, int]) -> dict[str, int]:
    ordered = {verdict: int(counts.get(verdict, 0)) for verdict in STANDARD_VERDICTS}
    for verdict in sorted(counts):
        if verdict not in ordered:
            ordered[verdict] = int(counts[verdict])
    return ordered


def _scenario_summary(comparison: dict[str, Any]) -> dict[str, Any]:
    audit = comparison.get("auditArtifacts", {})
    loc = audit.get("locComposition", {})
    log_root = audit.get("runnabilityLogRootPath", "")
    return {
        "milestone": comparison["milestone"],
        "verdict": comparison["verdict"],
        "finalVerdict": comparison.get("finalVerdict") or _verdict_class(comparison),
        "verdictClass": _verdict_class(comparison),
        "runnability": comparison.get("runnability", {}),
        "cleanExpectedMatches": comparison.get("cleanExpectedMatches", comparison.get("mustFindMatched", 0)),
        "mustFindExpected": comparison.get("mustFindExpected", 0),
        "mustFindMissing": _count(comparison, "mustFindMissing"),
        "missingExpectedFindings": _count(comparison, "missingExpectedFindings") or _count(comparison, "mustFindMissing"),
        "mustNotFindViolations": _count(comparison, "mustNotFindViolations"),
        "unexpectedFindings": _count(comparison, "unexpectedFindings") or _count(comparison, "extraFindings"),
        "sameSurfaceExtraFindings": _count(comparison, "sameSurfaceExtraFindings"),
        "sameFileDifferentSignalFindings": _count(comparison, "sameFileDifferentSignalFindings"),
        "unexpectedRegexOnlyFindings": _count(comparison, "unexpectedRegexOnlyFindings"),
        "mayFindReview": _count(comparison, "mayFindReview"),
        "explainabilityFailures": _count(comparison, "explainabilityFailures"),
        "refStateFailures": _count(comparison, "refStateFailures"),
        "noiseCount": int(comparison.get("noiseCount", 0)),
        "noiseBreakdown": _noise_breakdown(comparison),
        "finalVerdictReason": comparison.get("finalVerdictReason", ""),
        "normalizationStats": comparison.get("normalizationStats", {}),
        "dossierPath": audit.get("dossierPath", ""),
        "projectLocalDossierPath": audit.get("projectLocalDossierPath", ""),
        "reportDossierPath": audit.get("reportDossierPath", ""),
        "generatedManifestPath": audit.get("generatedManifestPath", ""),
        "generatedTreePath": audit.get("generatedTreePath", ""),
        "runnabilityLogRootPath": log_root,
        "persistedLogsPath": log_root,
        "dossierMissing": audit.get("dossierMissing", True),
        "fillerRatio": audit.get("fillerRatio", 0.0),
        "realismScore": audit.get("realismScore"),
        "realismJustification": audit.get("realismJustification", ""),
        "locComposition": loc,
    }


def render_scenario_report(scenario: dict[str, Any], comparison: dict[str, Any], scans: list[dict[str, Any]]) -> str:
    audit = comparison.get("auditArtifacts", {})
    lines = [
        f"# {scenario['id']} - {scenario['repo_name']}",
        "",
        f"- Milestone: `{scenario['milestone']}`",
        f"- Module: `{scenario['module']}`",
        f"- Verdict: `{comparison['verdict']}`",
        f"- Final verdict: `{comparison.get('finalVerdict') or _verdict_class(comparison)}`",
        f"- Verdict class: `{_verdict_class(comparison)}`",
        f"- Stack: `{scenario['stack']}`",
        f"- Domain: {scenario['domain']}",
        f"- Dossier: `{audit.get('reportDossierPath', 'n/a')}`",
        f"- Persisted logs path: `{audit.get('runnabilityLogRootPath', 'n/a')}`",
        "",
        "## Scan summary",
    ]
    for scan in scans:
        completed = scan.get("completed", {})
        lines.append(
            f"- `{scan['plan']['name']}`: `{completed.get('status', 'UNKNOWN')}` on `{completed.get('scannedRefName') or completed.get('requestedRefName') or 'n/a'}`"
        )
    lines.extend(
        [
            "",
            "## Comparison",
            f"- cleanExpectedMatches: `{comparison.get('cleanExpectedMatches', comparison['mustFindMatched'])}` / `{comparison['mustFindExpected']}`",
            f"- missingExpectedFindings: `{_count(comparison, 'missingExpectedFindings') or _count(comparison, 'mustFindMissing')}`",
            f"- mustNotFindViolations: `{_count(comparison, 'mustNotFindViolations')}`",
            f"- unexpectedFindings: `{_count(comparison, 'unexpectedFindings') or _count(comparison, 'extraFindings')}`",
            f"- sameSurfaceExtraFindings: `{_count(comparison, 'sameSurfaceExtraFindings')}`",
            f"- sameFileDifferentSignalFindings: `{_count(comparison, 'sameFileDifferentSignalFindings')}`",
            f"- unexpectedRegexOnlyFindings: `{_count(comparison, 'unexpectedRegexOnlyFindings')}`",
            f"- mayFindReview: `{_count(comparison, 'mayFindReview')}`",
            f"- explainabilityFailures: `{_count(comparison, 'explainabilityFailures')}`",
            f"- refStateFailures: `{_count(comparison, 'refStateFailures')}`",
            f"- noiseCount: `{comparison.get('noiseCount', 0)}`",
            f"- noiseBreakdown: `{_noise_breakdown_text(comparison)}`",
            f"- finalVerdict: `{comparison.get('finalVerdict') or _verdict_class(comparison)}`",
            f"- finalVerdictReason: {comparison.get('finalVerdictReason', 'n/a')}",
            "",
            "## Normalization",
            f"- rawFindings: `{comparison.get('normalizationStats', {}).get('rawFindings', 0)}`",
            f"- normalizedFindings: `{comparison.get('normalizationStats', {}).get('normalizedFindings', 0)}`",
            f"- collapsedDuplicates: `{comparison.get('normalizationStats', {}).get('collapsedDuplicates', 0)}`",
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


def _write_verdict_proof_artifacts(root: Path) -> dict[str, str]:
    proof_root = root / "verdict-proofs"
    ensure_dir(proof_root)
    proof = build_pass_with_noise_proof()
    comparison_path = proof_root / "pass-with-noise-comparison.json"
    report_path = proof_root / "pass-with-noise-scenario-report.md"
    summary_path = proof_root / "pass-with-noise-summary.md"
    write_json(comparison_path, proof["comparison"])
    write_text(report_path, render_scenario_report(proof["scenario"], proof["comparison"], proof["scans"]))
    summary_lines = [
        f"# {PROOF_SCENARIO_ID}",
        "",
        "Synthetic comparator proof that `PASS_WITH_NOISE` is reachable without relaxing strictness.",
        "",
        f"- finalVerdict: `{proof['proofChecks']['finalVerdict']}`",
        f"- cleanExpectedMatches: `{proof['proofChecks']['cleanExpectedMatches']}`",
        f"- missingExpectedFindings: `{proof['proofChecks']['missingExpectedFindings']}`",
        f"- mustNotFindViolations: `{proof['proofChecks']['mustNotFindViolations']}`",
        f"- explainabilityFailures: `{proof['proofChecks']['explainabilityFailures']}`",
        f"- noiseCount: `{proof['proofChecks']['noiseCount']}`",
        f"- sameSurfaceExtraFindings: `{proof['proofChecks']['sameSurfaceExtraFindings']}`",
        f"- unexpectedRegexOnlyFindings: `{proof['proofChecks']['unexpectedRegexOnlyFindings']}`",
        f"- reportPath: `{report_path}`",
        f"- comparisonPath: `{comparison_path}`",
    ]
    write_text(summary_path, "\n".join(summary_lines).rstrip() + "\n")
    return {
        "passWithNoiseComparisonPath": str(comparison_path),
        "passWithNoiseReportPath": str(report_path),
        "passWithNoiseSummaryPath": str(summary_path),
    }


def aggregate_comparisons(comparisons: list[dict[str, Any]]) -> dict[str, Any]:
    verdict_counts: dict[str, int] = {}
    by_milestone: dict[str, dict[str, Any]] = {}
    by_scenario: dict[str, dict[str, Any]] = {}
    for comparison in comparisons:
        verdict = _verdict_class(comparison)
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        scenario_summary = _scenario_summary(comparison)
        milestone_summary = by_milestone.setdefault(
            comparison["milestone"],
            {
                "scenarios": 0,
                "verdicts": {},
                "cleanExpectedMatches": 0,
                "missingExpectedFindings": 0,
                "mustNotFindViolations": 0,
                "unexpectedFindings": 0,
                "unexpectedRegexOnlyFindings": 0,
                "sameSurfaceExtraFindings": 0,
                "sameFileDifferentSignalFindings": 0,
                "mayFindReview": 0,
                "explainabilityFailures": 0,
                "refStateFailures": 0,
                "noiseCount": 0,
            },
        )
        milestone_summary["scenarios"] += 1
        milestone_summary["verdicts"][verdict] = milestone_summary["verdicts"].get(verdict, 0) + 1
        milestone_summary["cleanExpectedMatches"] += scenario_summary["cleanExpectedMatches"]
        milestone_summary["missingExpectedFindings"] += scenario_summary["missingExpectedFindings"]
        milestone_summary["mustNotFindViolations"] += scenario_summary["mustNotFindViolations"]
        milestone_summary["unexpectedFindings"] += scenario_summary["unexpectedFindings"]
        milestone_summary["unexpectedRegexOnlyFindings"] += scenario_summary["unexpectedRegexOnlyFindings"]
        milestone_summary["sameSurfaceExtraFindings"] += scenario_summary["sameSurfaceExtraFindings"]
        milestone_summary["sameFileDifferentSignalFindings"] += scenario_summary["sameFileDifferentSignalFindings"]
        milestone_summary["mayFindReview"] += scenario_summary["mayFindReview"]
        milestone_summary["explainabilityFailures"] += scenario_summary["explainabilityFailures"]
        milestone_summary["refStateFailures"] += scenario_summary["refStateFailures"]
        milestone_summary["noiseCount"] += scenario_summary["noiseCount"]
        by_scenario[comparison["scenarioId"]] = scenario_summary
    ordered_milestones = {}
    for milestone, summary in by_milestone.items():
        summary["verdicts"] = _ordered_verdict_counts(summary["verdicts"])
        ordered_milestones[milestone] = summary
    return {
        "scenarioCount": len(comparisons),
        "verdicts": _ordered_verdict_counts(verdict_counts),
        "byMilestone": ordered_milestones,
        "byScenario": by_scenario,
    }


def write_aggregate_reports(root: Path, comparisons: list[dict[str, Any]]) -> None:
    ensure_dir(root)
    aggregate = aggregate_comparisons(comparisons)
    proof_artifacts = _write_verdict_proof_artifacts(root)
    aggregate["proofArtifacts"] = proof_artifacts
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
    markdown_lines.extend(
        [
            "",
            "## Verdict Proofs",
            f"- `PASS_WITH_NOISE` proof summary: `{proof_artifacts['passWithNoiseSummaryPath']}`",
            f"- `PASS_WITH_NOISE` proof report: `{proof_artifacts['passWithNoiseReportPath']}`",
        ]
    )
    markdown_lines.extend(["", "## Milestones"])
    for milestone, summary in sorted(aggregate["byMilestone"].items()):
        verdict_text = ", ".join(f"{verdict}={count}" for verdict, count in sorted(summary["verdicts"].items()))
        markdown_lines.append(
            f"- `{milestone}`: scenarios=`{summary['scenarios']}`, verdicts=`{verdict_text}`, missing=`{summary['missingExpectedFindings']}`, fp=`{summary['mustNotFindViolations']}`, unexpected=`{summary['unexpectedFindings']}`, sameSurface=`{summary['sameSurfaceExtraFindings']}`, regexOnly=`{summary['unexpectedRegexOnlyFindings']}`, explainability=`{summary['explainabilityFailures']}`, ref-state=`{summary['refStateFailures']}`, noise=`{summary['noiseCount']}`"
        )
    markdown_lines.extend(["", "## Scenario Auditability"])
    for scenario_id, summary in sorted(aggregate["byScenario"].items()):
        loc = summary.get("locComposition", {})
        markdown_lines.append(
            f"- `{scenario_id}`: finalVerdict=`{summary['finalVerdict']}`, cleanMatches=`{summary['cleanExpectedMatches']}`/`{summary['mustFindExpected']}`, unexpected=`{summary['unexpectedFindings']}`, sameSurface=`{summary['sameSurfaceExtraFindings']}`, sameFile=`{summary['sameFileDifferentSignalFindings']}`, regexOnly=`{summary['unexpectedRegexOnlyFindings']}`, review=`{summary['mayFindReview']}`, explainability=`{summary['explainabilityFailures']}`, noise=`{summary['noiseCount']}`, runnability=`build:{summary.get('runnability', {}).get('build', 'n/a')},test:{summary.get('runnability', {}).get('test', 'n/a')},smoke:{summary.get('runnability', {}).get('smoke', 'n/a')}`, realism=`{summary.get('realismScore', 'n/a')}`, fillerRatio=`{summary.get('fillerRatio', 0.0):.2%}`, dossierMissing=`{summary.get('dossierMissing', True)}`, dossier=`{summary.get('reportDossierPath', 'n/a')}`, logs=`{summary.get('persistedLogsPath', 'n/a')}`, liveCode=`{loc.get('live business code', 0)}`, liveConfig=`{loc.get('live config', 0)}`, tests=`{loc.get('tests', 0)}`, filler=`{loc.get('synthetic filler / inflation content', 0)}`"
        )
    markdown_lines.extend(["", "## Noisy And Failed Scenarios"])
    noisy_or_failed = [
        (scenario_id, summary)
        for scenario_id, summary in sorted(aggregate["byScenario"].items())
        if summary["verdictClass"] != "PASS_CLEAN"
    ]
    if not noisy_or_failed:
        markdown_lines.append("- None.")
    for scenario_id, summary in noisy_or_failed:
        markdown_lines.append(
            f"- `{scenario_id}`: `{summary['verdictClass']}` because {summary['finalVerdictReason']}. Dossier=`{summary.get('reportDossierPath', 'n/a')}`"
        )
    write_text(root / "aggregate-summary.md", "\n".join(markdown_lines).rstrip() + "\n")

    csv_buffer = StringIO()
    writer = csv.DictWriter(
        csv_buffer,
        fieldnames=[
            "scenarioId",
            "milestone",
            "verdict",
            "finalVerdict",
            "verdictClass",
            "runnability",
            "cleanExpectedMatches",
            "mustFindExpected",
            "missingExpectedFindings",
            "mustNotFindViolations",
            "unexpectedFindings",
            "unexpectedRegexOnlyFindings",
            "sameSurfaceExtraFindings",
            "sameFileDifferentSignalFindings",
            "mayFindReview",
            "explainabilityFailures",
            "refStateFailures",
            "noiseCount",
            "noiseBreakdown",
            "finalVerdictReason",
            "dossierMissing",
            "fillerRatio",
            "realismScore",
            "dossierPath",
            "logsPath",
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
                "finalVerdict": summary["finalVerdict"],
                "verdictClass": summary["verdictClass"],
                "runnability": ",".join(
                    f"{stage}:{state}" for stage, state in sorted(summary.get("runnability", {}).items())
                ),
                "cleanExpectedMatches": summary["cleanExpectedMatches"],
                "mustFindExpected": summary["mustFindExpected"],
                "missingExpectedFindings": summary["missingExpectedFindings"],
                "mustNotFindViolations": summary["mustNotFindViolations"],
                "unexpectedFindings": summary["unexpectedFindings"],
                "unexpectedRegexOnlyFindings": summary["unexpectedRegexOnlyFindings"],
                "sameSurfaceExtraFindings": summary["sameSurfaceExtraFindings"],
                "sameFileDifferentSignalFindings": summary["sameFileDifferentSignalFindings"],
                "mayFindReview": summary["mayFindReview"],
                "explainabilityFailures": summary["explainabilityFailures"],
                "refStateFailures": summary["refStateFailures"],
                "noiseCount": summary["noiseCount"],
                "noiseBreakdown": _noise_breakdown_text(summary),
                "finalVerdictReason": summary["finalVerdictReason"],
                "dossierMissing": summary["dossierMissing"],
                "fillerRatio": summary["fillerRatio"],
                "realismScore": summary["realismScore"],
                "dossierPath": summary["reportDossierPath"],
                "logsPath": summary["persistedLogsPath"],
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
            "finalVerdict": comparison.get("finalVerdict") or _verdict_class(comparison),
            "verdictClass": _verdict_class(comparison),
            "missingExpectedFindings": _count(comparison, "missingExpectedFindings") or _count(comparison, "mustFindMissing"),
            "mustNotFindViolations": _count(comparison, "mustNotFindViolations"),
            "unexpectedFindings": _count(comparison, "unexpectedFindings") or _count(comparison, "extraFindings"),
            "sameSurfaceExtraFindings": _count(comparison, "sameSurfaceExtraFindings"),
            "sameFileDifferentSignalFindings": _count(comparison, "sameFileDifferentSignalFindings"),
            "unexpectedRegexOnlyFindings": _count(comparison, "unexpectedRegexOnlyFindings"),
            "mayFindReview": _count(comparison, "mayFindReview"),
            "explainabilityFailures": _count(comparison, "explainabilityFailures"),
            "refStateFailures": _count(comparison, "refStateFailures"),
            "noiseCount": int(comparison.get("noiseCount", 0)),
            "noiseBreakdown": _noise_breakdown(comparison),
            "finalVerdictReason": comparison.get("finalVerdictReason", ""),
            "reportDossierPath": comparison.get("auditArtifacts", {}).get("reportDossierPath", ""),
            "runnabilityLogRootPath": comparison.get("auditArtifacts", {}).get("runnabilityLogRootPath", ""),
            "persistedLogsPath": comparison.get("auditArtifacts", {}).get("runnabilityLogRootPath", ""),
            "dossierMissing": comparison.get("auditArtifacts", {}).get("dossierMissing", True),
        }
        for comparison in comparisons
        if _verdict_class(comparison) != "PASS_CLEAN"
    ]
    write_json(root / "fail-buckets.json", fail_buckets)

    tuning_lines = ["# Tuning Backlog Seed", "", "Generated from current scenario comparison buckets.", ""]
    if not fail_buckets:
        tuning_lines.append("- None.")
    for bucket in fail_buckets:
        tuning_lines.append(
            f"- `{bucket['scenarioId']}` / `{bucket['verdictClass']}`: missing=`{bucket['missingExpectedFindings']}`, fp=`{bucket['mustNotFindViolations']}`, unexpected=`{bucket['unexpectedFindings']}`, sameSurface=`{bucket['sameSurfaceExtraFindings']}`, sameFile=`{bucket['sameFileDifferentSignalFindings']}`, review=`{bucket['mayFindReview']}`, regexOnly=`{bucket['unexpectedRegexOnlyFindings']}`, explainability=`{bucket['explainabilityFailures']}`, ref-state=`{bucket['refStateFailures']}`, noise=`{bucket['noiseCount']}`. Reason: {bucket['finalVerdictReason']}"
        )
    write_text(root / "tuning-backlog-seed.md", "\n".join(tuning_lines).rstrip() + "\n")

    explainability_lines = [
        "# Explainability Scorecard",
        "",
        f"- Total scenarios: `{aggregate['scenarioCount']}`",
        f"- Scenarios with explainability failures: `{sum(1 for item in comparisons if _count(item, 'explainabilityFailures'))}`",
        f"- Unexpected regex-only findings total: `{sum(_count(item, 'unexpectedRegexOnlyFindings') for item in comparisons)}`",
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
            "## Verdict Proofs",
            f"- `PASS_WITH_NOISE` proof summary: `{proof_artifacts['passWithNoiseSummaryPath']}`",
            f"- `PASS_WITH_NOISE` proof report: `{proof_artifacts['passWithNoiseReportPath']}`",
            "",
            "## Strengths and gaps",
            "- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.",
            "- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.",
            "- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.",
            f"- Dossier coverage: `{dossier_count}` / `{aggregate['scenarioCount']}` scenarios have required dossier, manifest, and tree artifacts.",
            "",
            "## Noisy And Failed Scenario Reasons",
        ]
    )
    if not fail_buckets:
        final_lines.append("- None.")
    for bucket in fail_buckets:
        final_lines.append(f"- `{bucket['scenarioId']}` / `{bucket['verdictClass']}`: {bucket['finalVerdictReason']}")
    write_text(root / "FINAL_VALIDATION_STATUS.md", "\n".join(final_lines).rstrip() + "\n")
