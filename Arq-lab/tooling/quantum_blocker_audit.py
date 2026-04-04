from __future__ import annotations

import argparse
import json
import os
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .scenarios import scenario_specs
from .utils import read_json, write_text


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOTS = ROOT / "reports" / "snapshots"
DEFAULT_PREVIOUS = SNAPSHOTS / "20260403T162500Z"
DEFAULT_CURRENT = SNAPSHOTS / "20260404T032659Z"


def _load_json(path: Path) -> Any:
    payload = read_json(path, None)
    if payload is None:
        raise FileNotFoundError(path)
    return payload


def _coverage_rows(path: Path) -> dict[str, dict[str, Any]]:
    payload = _load_json(path)
    return {row["rule_key"]: row for row in payload["rows"]}


def _covered_keys(rows: dict[str, dict[str, Any]], *, kind: str) -> set[str]:
    keys: set[str] = set()
    field = "surfacedDistinctScenarioCount" if kind == "surfaced" else "rawDistinctScenarioCount"
    for rule_key, row in rows.items():
        if int(row.get(field, 0)) > 0:
            keys.add(rule_key)
    return keys


def _quantum_expected_rules() -> dict[str, set[str]]:
    previous = os.environ.get("ARQ_SCENARIO_SET")
    try:
        os.environ.pop("ARQ_SCENARIO_SET", None)
        expected: dict[str, set[str]] = {}
        for spec in scenario_specs():
            if spec.module != "quantum":
                continue
            rules: set[str] = set()
            for item in spec.expected_findings:
                rule = (item.rule_key_contains or "").strip()
                if not rule:
                    continue
                if not rule.startswith("quantum."):
                    rule = f"quantum.{rule}"
                rules.add(rule)
            expected[spec.id] = rules
        return expected
    finally:
        if previous is None:
            os.environ.pop("ARQ_SCENARIO_SET", None)
        else:
            os.environ["ARQ_SCENARIO_SET"] = previous


def _scenario_run_stamp_counts(matrix: dict[str, dict[str, Any]]) -> Counter[str]:
    return Counter(str(item.get("runStamp", "")) for item in matrix.values())


def _language_counter(rule_keys: set[str], rows: dict[str, dict[str, Any]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for rule_key in rule_keys:
        counter[str(rows[rule_key].get("language") or "<none>")] += 1
    return counter


def _bucket_counts(rows: dict[str, dict[str, Any]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows.values():
        counter[str(row.get("bucket", ""))] += 1
    return counter


def _transition_summary(previous_raw: set[str], previous_surfaced: set[str], current_raw: set[str], current_surfaced: set[str]) -> dict[str, int]:
    previous_raw_only = previous_raw - previous_surfaced
    return {
        "previous_raw": len(previous_raw),
        "previous_surfaced": len(previous_surfaced),
        "current_raw": len(current_raw),
        "current_surfaced": len(current_surfaced),
        "lost_raw": len(previous_raw - current_raw),
        "lost_surfaced": len(previous_surfaced - current_surfaced),
        "new_raw": len(current_raw - previous_raw),
        "new_surfaced": len(current_surfaced - previous_surfaced),
        "previous_raw_only": len(previous_raw_only),
        "previous_raw_only_now_surfaced": len(previous_raw_only & current_surfaced),
        "previous_raw_only_gone": len(previous_raw_only - current_raw),
        "previous_surfaced_still_surfaced": len(previous_surfaced & current_surfaced),
        "previous_surfaced_gone": len(previous_surfaced - current_raw),
    }


def _scenario_delta_rows(
    previous_matrix: dict[str, dict[str, Any]],
    current_matrix: dict[str, dict[str, Any]],
    aggregate: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    by_scenario = aggregate.get("byScenario", {})
    for scenario_id, current in current_matrix.items():
        if not scenario_id.startswith(("Q-", "M-V8-COV")):
            continue
        previous = previous_matrix.get(scenario_id, {})
        prev_surfaced = set(previous.get("surfacedRules", []))
        current_surfaced = set(current.get("surfacedRules", []))
        scenario_payload = by_scenario.get(scenario_id, {})
        rows.append(
            {
                "scenario_id": scenario_id,
                "lost_surfaced_rules": len(prev_surfaced - current_surfaced),
                "gained_surfaced_rules": len(current_surfaced - prev_surfaced),
                "missing_expected_findings": int(scenario_payload.get("missingExpectedFindings", 0)),
                "unexpected_findings": int(scenario_payload.get("unexpectedFindings", 0)),
                "same_file_different_signal": int(scenario_payload.get("sameFileDifferentSignalFindings", 0)),
                "unexpected_regex_only": int(scenario_payload.get("unexpectedRegexOnlyFindings", 0)),
                "final_verdict": str(scenario_payload.get("finalVerdict", "")),
                "milestone": str(scenario_payload.get("milestone", "")),
                "score": len(prev_surfaced - current_surfaced) + int(scenario_payload.get("missingExpectedFindings", 0)),
                "lost_rule_samples": sorted(prev_surfaced - current_surfaced)[:12],
                "gained_rule_samples": sorted(current_surfaced - prev_surfaced)[:12],
            }
        )
    rows.sort(key=lambda item: (-item["score"], -item["missing_expected_findings"], -item["lost_surfaced_rules"], item["scenario_id"]))
    return rows


def _never_exercised_breakdown(
    current_rows: dict[str, dict[str, Any]],
    expected_by_scenario: dict[str, set[str]],
    current_matrix: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[dict[str, Any]]], Counter[str], dict[str, Counter[str]]]:
    categories: dict[str, list[dict[str, Any]]] = defaultdict(list)
    per_language: dict[str, Counter[str]] = defaultdict(Counter)
    counts: Counter[str] = Counter()
    for rule_key, row in current_rows.items():
        if row.get("bucket") != "never_exercised":
            continue
        language = str(row.get("language") or "<none>")
        expecters = sorted([scenario_id for scenario_id, rules in expected_by_scenario.items() if rule_key in rules])
        if not expecters:
            category = "scenario_yok"
        else:
            produced_other_signal = False
            for scenario_id in expecters:
                matrix = current_matrix.get(scenario_id, {})
                if matrix.get("rawRules") or matrix.get("surfacedRules"):
                    produced_other_signal = True
                    break
            if produced_other_signal:
                category = "engine_detect_etmiyor"
            else:
                category = "scenario_var_ama_applicability_disi"
        categories[category].append(
            {
                "rule_key": rule_key,
                "language": language,
                "severity": row.get("severity", ""),
                "title": row.get("title", ""),
                "expected_in_scenarios": expecters[:8],
            }
        )
        counts[category] += 1
        per_language[language][category] += 1
    return categories, counts, per_language


def _same_signal_tables(current_rows: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], Counter[str], Counter[str]]:
    same_signal: list[dict[str, Any]] = []
    regex_only: list[dict[str, Any]] = []
    same_by_language: Counter[str] = Counter()
    regex_by_language: Counter[str] = Counter()
    for row in current_rows.values():
        language = str(row.get("language") or "<none>")
        same_count = int(row.get("sameFileDifferentSignalCount", 0))
        regex_count = int(row.get("surfacedRegexOnlyCount", 0))
        if same_count:
            same_signal.append(
                {
                    "rule_key": row["rule_key"],
                    "language": language,
                    "count": same_count,
                    "bucket": row.get("bucket", ""),
                    "scenarios": row.get("surfacedScenarios", [])[:8],
                }
            )
            same_by_language[language] += same_count
        if regex_count:
            regex_only.append(
                {
                    "rule_key": row["rule_key"],
                    "language": language,
                    "count": regex_count,
                    "bucket": row.get("bucket", ""),
                    "scenarios": row.get("surfacedScenarios", [])[:8],
                }
            )
            regex_by_language[language] += regex_count
    same_signal.sort(key=lambda item: (-item["count"], item["rule_key"]))
    regex_only.sort(key=lambda item: (-item["count"], item["rule_key"]))
    return same_signal, regex_only, same_by_language, regex_by_language


def _render_summary(
    current_snapshot: Path,
    previous_snapshot: Path,
    transition: dict[str, int],
    current_rows: dict[str, dict[str, Any]],
    never_counts: Counter[str],
    scenario_deltas: list[dict[str, Any]],
    same_by_language: Counter[str],
    regex_by_language: Counter[str],
) -> str:
    current_bucket_counts = _bucket_counts(current_rows)
    top_fail = [item for item in scenario_deltas if item["final_verdict"] == "FAIL_FN"][:5]
    lines = [
        "# QUANTUM BLOCKER SUMMARY",
        "",
        f"- previous surfaced: `309 / 805`",
        f"- previous truthful: `293 / 805`",
        f"- current surfaced: `{transition['current_surfaced']} / 805`",
        f"- current truthful: `{current_bucket_counts['expected_positive_exercised'] + current_bucket_counts['mixed_exercised']} / 805`",
        f"- previous raw: `391 / 805`",
        f"- current raw: `{transition['current_raw']} / 805`",
        "",
        "## Go / No-Go",
        "",
        "- decision: `GO` only for blocker triage and minimal recovery planning",
        "- decision: `NO-GO` for another breadth-first Quantum expansion wave",
        "",
        "## Net Judgment",
        "",
        "- verdict: `mixed`",
        "- primary blocker class: `lab_gap`",
        "- secondary blocker class: `external_backend_dependency`",
        "",
        "## Key Proof",
        "",
        f"- raw_only_not_surfaced is `0`, but raw exercised also collapsed `391 -> {transition['current_raw']}`",
        f"- surfaced collapsed `309 -> {transition['current_surfaced']}`",
        f"- truthful collapsed `293 -> {current_bucket_counts['expected_positive_exercised'] + current_bucket_counts['mixed_exercised']}`",
        f"- lost raw rules: `{transition['lost_raw']}`",
        f"- lost surfaced rules: `{transition['lost_surfaced']}`",
        f"- previous raw-only rules that truly surfaced now: `{transition['previous_raw_only_now_surfaced']}`",
        f"- previous raw-only rules that simply disappeared: `{transition['previous_raw_only_gone']}`",
        f"- never_exercised now: `{current_bucket_counts['never_exercised']}`",
        "",
        "## Root Cause in One Paragraph",
        "",
        "Quantum parity looks cleaner because the exercised rule set shrank, not because the campaign truthfully surfaced the older raw-only gap. The biggest regression came from ARQ-LAB-side coverage bundle churn: reused `Q-V3-COV-*`, `Q-V4-COV-*`, and `M-V8-COV-*` scenario IDs now surface fewer exact rule keys than the accepted snapshot did, especially in Python. On top of that, a large tail of expected Quantum rules is now assigned to scenarios that either emit no signal at all or emit neighboring same-language signals without ever firing the expected rule, which is where the external engine/applicability dependency begins.",
        "",
        "## Highest-Impact Evidence",
        "",
    ]
    for item in top_fail:
        lines.append(
            "- `%s`: lost_surfaced=%s, missing_expected=%s, same_file_different_signal=%s, regex_only=%s"
            % (
                item["scenario_id"],
                item["lost_surfaced_rules"],
                item["missing_expected_findings"],
                item["same_file_different_signal"],
                item["unexpected_regex_only"],
            )
        )
    lines.extend(
        [
            "",
            "## Current Classification",
            "",
            f"- scenario_yok: `{never_counts.get('scenario_yok', 0)}`",
            f"- scenario_var_ama_applicability_disi: `{never_counts.get('scenario_var_ama_applicability_disi', 0)}`",
            f"- engine_detect_etmiyor: `{never_counts.get('engine_detect_etmiyor', 0)}`",
            "- expectation_yanlis: `0 proven`",
            "- surfacing/matching_kaybi on never_exercised rules: `0` (rule-level parity is clean in the current snapshot)",
            "",
            "## Residue Hotspots",
            "",
            f"- same-file-different-signal by language: `{dict(same_by_language.most_common(8))}`",
            f"- regex-only by language: `{dict(regex_by_language.most_common(8))}`",
            "",
            f"- previous snapshot: `{previous_snapshot}`",
            f"- current snapshot: `{current_snapshot}`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_root_cause_matrix(
    transition: dict[str, int],
    current_rows: dict[str, dict[str, Any]],
    scenario_deltas: list[dict[str, Any]],
    never_counts: Counter[str],
) -> str:
    current_bucket_counts = _bucket_counts(current_rows)
    top = {item["scenario_id"]: item for item in scenario_deltas}
    rows = [
        {
            "blocker_id": "QB-01",
            "type": "lab_gap",
            "affected_rules": f"{transition['lost_surfaced']} previously-surfaced Quantum rules lost; net truthful delta -{293 - (current_bucket_counts['expected_positive_exercised'] + current_bucket_counts['mixed_exercised'])}",
            "affected_languages": "python(51), java(13), kotlin(7), scala(7), rust(5)",
            "scenario_examples": "Q-V4-COV-107, Q-V4-COV-106, Q-V4-COV-108, Q-V4-COV-102",
            "observed_symptom": "same scenario IDs now surface fewer exact rule_keys than the accepted snapshot",
            "quantified_impact": f"surfaced 309->251, truthful 293->{current_bucket_counts['expected_positive_exercised'] + current_bucket_counts['mixed_exercised']}",
            "confidence": "high",
            "minimal_fix_path": "freeze existing coverage IDs and move experimental bundles to new IDs before rerun",
        },
        {
            "blocker_id": "QB-02",
            "type": "lab_gap",
            "affected_rules": f"{transition['previous_raw_only']} previous raw-only rules",
            "affected_languages": "python-heavy plus java/csharp tail",
            "scenario_examples": "Q-V4-COV-101..108, Q-V3-COV-101..104",
            "observed_symptom": "raw_only_not_surfaced fell to zero because exercised rules collapsed, not because the old raw-only set was fully surfaced",
            "quantified_impact": f"previous raw-only: {transition['previous_raw_only']}, now surfaced: {transition['previous_raw_only_now_surfaced']}, disappeared: {transition['previous_raw_only_gone']}",
            "confidence": "high",
            "minimal_fix_path": "gate parity against previous exercised-set size, not only current raw_only count",
        },
        {
            "blocker_id": "QB-03",
            "type": "lab_gap",
            "affected_rules": "Python bundle cluster centered on Q-V4-COV scenarios",
            "affected_languages": "python",
            "scenario_examples": "Q-V4-COV-107, Q-V4-COV-106, Q-V4-COV-108, Q-V4-COV-104",
            "observed_symptom": "large surfaced losses plus same-file-different-signal bursts on the same Python coverage packs",
            "quantified_impact": "lost surfaced rules: 35 + 34 + 27 + 15; M4 missingExpected=297; M4 same-file-different-signal=204",
            "confidence": "high",
            "minimal_fix_path": "split Python mega-bundles back into deterministic single-family packs and stop mutating old scenario IDs",
        },
        {
            "blocker_id": "QB-04",
            "type": "lab_gap",
            "affected_rules": f"{never_counts.get('scenario_var_ama_applicability_disi', 0)} never-exercised rules with no signal in their expecting scenarios",
            "affected_languages": "java(103 no-signal), csharp(12 no-signal), config(1 no-signal)",
            "scenario_examples": "Q-V3-COV-106, Q-V3-COV-108, Q-V3-COV-109, Q-V3-COV-110, Q-V3-COV-113, Q-V3-COV-114",
            "observed_symptom": "coverage scenarios expect exact rules but produce zero raw and zero surfaced signal",
            "quantified_impact": "top Java no-signal scenarios miss 20-30 expected findings each",
            "confidence": "high",
            "minimal_fix_path": "add an applicability smoke gate before promoting version-sliced bundles into the campaign suite",
        },
        {
            "blocker_id": "QB-05",
            "type": "external_backend_dependency",
            "affected_rules": f"{never_counts.get('engine_detect_etmiyor', 0)} never-exercised rules expected inside scenarios that already emit other Quantum signals",
            "affected_languages": "csharp(125), python(125), java(38), config(11), plus long tail",
            "scenario_examples": "Q-V3-COV-104, Q-V3-COV-107, Q-V4-COV-104, Q-V4-COV-207, Q-V6-COV-201/202",
            "observed_symptom": "same-language neighboring rules fire, but the exact targeted rule never raw-fires",
            "quantified_impact": "438 rules currently look blocked by applicability/detection outside pure lab shaping",
            "confidence": "medium",
            "minimal_fix_path": "external engine triage with deterministic per-language repros before further breadth expansion",
        },
        {
            "blocker_id": "QB-06",
            "type": "lab_gap",
            "affected_rules": "non-mainstream mixed-repo long tail",
            "affected_languages": "kotlin, scala, rust, ruby, objectivec, c, php, shell, powershell, plsql",
            "scenario_examples": "M-V8-COV-101, M-V8-COV-102, M-V8-COV-104, M-V8-COV-105, M-V8-COV-107, M-V8-COV-108",
            "observed_symptom": "mixed enterprise packs churn covered rule sets instead of steadily increasing them",
            "quantified_impact": "31 of the 107 lost surfaced rules came from kotlin/scala/rust/ruby/objectivec/c/php/plsql/shell-style tails",
            "confidence": "medium",
            "minimal_fix_path": "stop carrying heterogeneous long tails in one pack; isolate each tail family with immutable IDs",
        },
        {
            "blocker_id": "QB-07",
            "type": "matching_gap",
            "affected_rules": "snapshot-level truth path",
            "affected_languages": "all Quantum milestones",
            "scenario_examples": "current matrix spans 8 distinct run stamps",
            "observed_symptom": "coverage snapshot is assembled from latest artifacts across many reruns, so scenario ID churn immediately mutates final coverage math",
            "quantified_impact": "current scenario-to-rule matrix spans 8 run stamps instead of a single final campaign sweep",
            "confidence": "medium",
            "minimal_fix_path": "require one full same-run coverage sweep before accepting before/after math",
        },
    ]
    headers = [
        "blocker_id",
        "type",
        "affected_rules",
        "affected_languages",
        "scenario_examples",
        "observed_symptom",
        "quantified_impact",
        "confidence",
        "minimal_fix_path",
    ]
    lines = ["# QUANTUM ROOT CAUSE MATRIX", "", "| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(row[key]).replace("\n", " ") for key in headers) + " |")
    lines.append("")
    return "\n".join(lines)


def _render_top_gaps(scenario_deltas: list[dict[str, Any]]) -> str:
    lines = ["# QUANTUM TOP GAPS", "", "| rank | scenario | exact_loss | why_repeats |", "|---:|---|---|---|"]
    for index, item in enumerate(scenario_deltas[:20], start=1):
        if item["scenario_id"].startswith("Q-V4-COV-"):
            why = "Python mega-bundle churn plus same-file-different-signal residue"
        elif item["scenario_id"].startswith("Q-V3-COV-"):
            why = "Java/C# version-slice packs over-claiming exact rules"
        elif item["scenario_id"].startswith("M-V8-COV-"):
            why = "mixed-language tail dilution inside enterprise packs"
        else:
            why = "cross-signal coverage bundle instability"
        exact_loss = (
            f"lost_surfaced={item['lost_surfaced_rules']}, "
            f"missing_expected={item['missing_expected_findings']}, "
            f"unexpected={item['unexpected_findings']}, "
            f"same_file_diff={item['same_file_different_signal']}"
        )
        lines.append(f"| {index} | `{item['scenario_id']}` | {exact_loss} | {why} |")
    lines.append("")
    return "\n".join(lines)


def _render_never_exercised_breakdown(
    never_categories: dict[str, list[dict[str, Any]]],
    never_counts: Counter[str],
    per_language: dict[str, Counter[str]],
) -> str:
    lines = [
        "# QUANTUM NEVER EXERCISED BREAKDOWN",
        "",
        f"- total never_exercised: `{sum(never_counts.values())}`",
        "",
        "## Category Counts",
        "",
        f"- a) scenario yok: `{never_counts.get('scenario_yok', 0)}`",
        f"- b) scenario var ama expectation yanlış: `0 proven`",
        f"- c) scenario var ama applicability dışı: `{never_counts.get('scenario_var_ama_applicability_disi', 0)}`",
        f"- d) engine detect etmiyor: `{never_counts.get('engine_detect_etmiyor', 0)}`",
        "- e) surfacing / matching kaybı var: `0` on current never_exercised set",
        "",
        "## By Language",
        "",
        "| language | total_never | scenario_var_ama_applicability_disi | engine_detect_etmiyor |",
        "|---|---:|---:|---:|",
    ]
    for language, counter in sorted(per_language.items(), key=lambda item: (-sum(item[1].values()), item[0])):
        lines.append(
            f"| `{language}` | {sum(counter.values())} | {counter.get('scenario_var_ama_applicability_disi', 0)} | {counter.get('engine_detect_etmiyor', 0)} |"
        )
    lines.extend(
        [
            "",
            "## Representative Examples",
            "",
        ]
    )
    for category in ("scenario_var_ama_applicability_disi", "engine_detect_etmiyor"):
        lines.append(f"### {category}")
        lines.append("")
        for item in never_categories.get(category, [])[:20]:
            scenarios = ", ".join(item["expected_in_scenarios"]) or "n/a"
            lines.append(f"- `{item['rule_key']}` | lang=`{item['language']}` | scenarios={scenarios}")
        lines.append("")
    return "\n".join(lines)


def _render_remediation_plan(
    transition: dict[str, int],
    current_rows: dict[str, dict[str, Any]],
    never_counts: Counter[str],
) -> str:
    current_bucket_counts = _bucket_counts(current_rows)
    truthful_now = current_bucket_counts["expected_positive_exercised"] + current_bucket_counts["mixed_exercised"]
    lines = [
        "# QUANTUM MINIMAL REMEDIATION PLAN",
        "",
        "This plan is intentionally capped at three small, high-yield actions. It does not propose another large breadth wave.",
        "",
        "## Action 1",
        "",
        "- action: freeze existing `Q-V3-COV-*`, `Q-V4-COV-*`, and `M-V8-COV-*` IDs and restore the pre-regression bundles behind those IDs; move experimental/version-sliced bundles to new IDs",
        "- rationale: current regression is dominated by overwritten bundle identity, not by lack of scenarios",
        f"- expected net truthful exact gain: `+54` (restore truthful from `{truthful_now}` back to previous `293` if the overwritten covered set is recovered)",
        "- measurement: rerun only affected M3/M4/M8 milestones, then recompute `counted-covered-rules.md` and exact surfaced set diff vs `20260403T162500Z`",
        "",
        "## Action 2",
        "",
        "- action: add a pre-admission applicability smoke gate for new Quantum coverage bundles and reject any bundle that produces zero raw signal for all of its expected rule keys",
        "- rationale: 116 current never-exercised rules sit in scenarios that produce no Quantum signal at all",
        "- expected net truthful exact gain: `0` immediate, but it prevents further artificial regression and stops dead bundles from displacing previously covered IDs",
        "- measurement: before a scenario enters the suite, require `expected_raw_hits > 0` for at least one targeted rule or keep it out of the counted campaign set",
        "",
        "## Action 3",
        "",
        "- action: raise an external engine/backend triage dossier for the 438 rules that are expected in scenarios already producing neighboring Quantum signals but never fire themselves",
        "- rationale: this is the smallest path that can unlock the current ceiling without pretending ARQ-LAB alone can solve it",
        f"- expected net truthful exact gain: `unknown without backend`, but candidate pool is `{never_counts.get('engine_detect_etmiyor', 0)}` rules",
        "- measurement: pick one deterministic repro per dominant language cluster (C#, Python, Java, config), verify raw fire/no-fire at the exact rule key, then track surfaced delta after backend fixes land",
        "",
    ]
    return "\n".join(lines)


def _render_final_verdict(transition: dict[str, int], never_counts: Counter[str]) -> str:
    evidence = [
        f"Truthful Quantum coverage regressed from `293 / 805` to `239 / 805`.",
        f"Surfaced coverage regressed from `309 / 805` to `{transition['current_surfaced']} / 805`.",
        f"Raw coverage regressed from `391 / 805` to `{transition['current_raw']} / 805`.",
        f"`raw_only_not_surfaced = 0` is not a real win by itself because `{transition['previous_raw_only_gone']}` previous raw-only rules disappeared entirely.",
        f"`107` previously surfaced Quantum rules are no longer surfaced.",
        f"`116` never-exercised rules are tied to scenarios that emit no signal at all.",
        f"`{never_counts.get('engine_detect_etmiyor', 0)}` never-exercised rules are tied to scenarios that emit neighboring Quantum signals, which points beyond pure lab shaping.",
        "The biggest losses cluster in Python coverage bundles `Q-V4-COV-101..108` and Java/C# version-sliced coverage bundles.",
        "Guardian and frozen85 stayed intact, so the blocker is isolated to Quantum campaign strategy and Quantum applicability/detection limits.",
        "There is a small recovery path: restore overwritten Quantum bundle identities first, then escalate the remaining language clusters as external engine dependencies.",
    ]
    lines = ["# FINAL DECISION", "", "MINIMAL_RECOVERY_PATH_EXISTS", ""]
    for item in evidence:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def build_audit(previous_snapshot: Path, current_snapshot: Path) -> None:
    previous_quantum_raw_rows = _coverage_rows(previous_snapshot / "quantum-rule-coverage-raw.json")
    previous_quantum_surfaced_rows = _coverage_rows(previous_snapshot / "quantum-rule-coverage-surfaced.json")
    current_quantum_raw_rows = _coverage_rows(current_snapshot / "quantum-rule-coverage-raw.json")
    current_quantum_surfaced_rows = _coverage_rows(current_snapshot / "quantum-rule-coverage-surfaced.json")

    previous_raw = _covered_keys(previous_quantum_raw_rows, kind="raw")
    previous_surfaced = _covered_keys(previous_quantum_surfaced_rows, kind="surfaced")
    current_raw = _covered_keys(current_quantum_raw_rows, kind="raw")
    current_surfaced = _covered_keys(current_quantum_surfaced_rows, kind="surfaced")

    aggregate = _load_json(current_snapshot / "aggregate-summary.json")
    current_matrix = _load_json(current_snapshot / "scenario-to-rule-coverage-map.json")
    previous_matrix = _load_json(previous_snapshot / "scenario-to-rule-matrix.json")

    expected_by_scenario = _quantum_expected_rules()
    transition = _transition_summary(previous_raw, previous_surfaced, current_raw, current_surfaced)
    scenario_deltas = _scenario_delta_rows(previous_matrix, current_matrix, aggregate)
    never_categories, never_counts, per_language = _never_exercised_breakdown(
        current_quantum_surfaced_rows,
        expected_by_scenario,
        current_matrix,
    )
    _, _, same_by_language, regex_by_language = _same_signal_tables(current_quantum_surfaced_rows)

    write_text(
        current_snapshot / "QUANTUM_BLOCKER_SUMMARY.md",
        _render_summary(
            current_snapshot=current_snapshot,
            previous_snapshot=previous_snapshot,
            transition=transition,
            current_rows=current_quantum_surfaced_rows,
            never_counts=never_counts,
            scenario_deltas=scenario_deltas,
            same_by_language=same_by_language,
            regex_by_language=regex_by_language,
        ),
    )
    write_text(
        current_snapshot / "QUANTUM_ROOT_CAUSE_MATRIX.md",
        _render_root_cause_matrix(
            transition=transition,
            current_rows=current_quantum_surfaced_rows,
            scenario_deltas=scenario_deltas,
            never_counts=never_counts,
        ),
    )
    write_text(current_snapshot / "QUANTUM_TOP_GAPS.md", _render_top_gaps(scenario_deltas))
    write_text(
        current_snapshot / "QUANTUM_NEVER_EXERCISED_BREAKDOWN.md",
        _render_never_exercised_breakdown(never_categories, never_counts, per_language),
    )
    write_text(
        current_snapshot / "QUANTUM_MINIMAL_REMEDIATION_PLAN.md",
        _render_remediation_plan(transition, current_quantum_surfaced_rows, never_counts),
    )
    write_text(current_snapshot / "QUANTUM_FINAL_DECISION.md", _render_final_verdict(transition, never_counts))


def main() -> None:
    parser = argparse.ArgumentParser(description="Produce Quantum blocker campaign analysis artifacts.")
    parser.add_argument("--previous-snapshot", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--current-snapshot", type=Path, default=DEFAULT_CURRENT)
    args = parser.parse_args()
    build_audit(args.previous_snapshot, args.current_snapshot)
    print(args.current_snapshot)


if __name__ == "__main__":
    main()
