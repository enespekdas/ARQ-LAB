from __future__ import annotations

import argparse
import os
import shutil
from collections import Counter
from pathlib import Path
from typing import Any

from .scenarios import scenario_specs
from .utils import ensure_dir, read_json, timestamp_slug, write_json, write_text


ROOT = Path(__file__).resolve().parents[1]
REPORTS_ROOT = ROOT / "reports"
SNAPSHOTS_ROOT = REPORTS_ROOT / "snapshots"
DEFAULT_PREVIOUS_SNAPSHOT = SNAPSHOTS_ROOT / "20260403T162500Z"

BUCKET_EXPECTED = "expected_positive_exercised"
BUCKET_MIXED = "mixed_exercised"
BUCKET_NOISY = "noisy_only_exercised"
BUCKET_RAW_ONLY = "raw_only_not_surfaced"
BUCKET_EXPLAINABILITY = "explainability_problematic_exercised"
BUCKET_NEVER = "never_exercised"
BUCKET_UNCLASSIFIED = "unclassified_exercised"


def _load_json(path: Path) -> Any:
    payload = read_json(path, None)
    if payload is None:
        raise FileNotFoundError(path)
    return payload


def _copy_if_exists(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    ensure_dir(destination.parent)
    shutil.copy2(source, destination)


def _coverage_summary(payload: dict[str, Any]) -> dict[str, Any]:
    bucket_counts = payload.get("bucketCounts", {})
    active = int(payload.get("activeRuleCount", 0))
    surfaced = int(payload.get("exercisedDistinctRules", 0))
    expected = int(bucket_counts.get(BUCKET_EXPECTED, 0))
    mixed = int(bucket_counts.get(BUCKET_MIXED, 0))
    noisy = int(bucket_counts.get(BUCKET_NOISY, 0))
    raw_only = int(bucket_counts.get(BUCKET_RAW_ONLY, 0))
    explainability = int(bucket_counts.get(BUCKET_EXPLAINABILITY, 0))
    never = int(bucket_counts.get(BUCKET_NEVER, 0))
    truthful = expected + mixed
    truthful_percent = round((truthful / active) * 100, 2) if active else 0.0
    return {
        "denominator": active,
        "surfaced_exercised": surfaced,
        "surfaced_percent": float(payload.get("coveragePercent", 0.0)),
        "expected_positive": expected,
        "mixed": mixed,
        "truthful_covered": truthful,
        "truthful_percent": truthful_percent,
        "noisy_only": noisy,
        "raw_only_not_surfaced": raw_only,
        "explainability_problematic": explainability,
        "never_exercised": never,
    }


def _frozen85_ids() -> set[str]:
    previous = os.environ.get("ARQ_SCENARIO_SET")
    try:
        os.environ["ARQ_SCENARIO_SET"] = "frozen85"
        return {scenario.id for scenario in scenario_specs()}
    finally:
        if previous is None:
            os.environ.pop("ARQ_SCENARIO_SET", None)
        else:
            os.environ["ARQ_SCENARIO_SET"] = previous


def _render_module_section(name: str, current: dict[str, Any], previous: dict[str, Any] | None) -> list[str]:
    lines = [f"## {name}", ""]
    if previous is not None:
        lines.append(
            "- before: surfaced `%(surfaced_exercised)s / %(denominator)s` (`%(surfaced_percent)s%%`), truthful `%(truthful_covered)s / %(denominator)s` (`%(truthful_percent)s%%`)" % previous
        )
    lines.append(
        "- now: surfaced `%(surfaced_exercised)s / %(denominator)s` (`%(surfaced_percent)s%%`), truthful `%(truthful_covered)s / %(denominator)s` (`%(truthful_percent)s%%`)" % current
    )
    lines.append(f"- expected_positive_exercised: `{current['expected_positive']}`")
    lines.append(f"- mixed_exercised: `{current['mixed']}`")
    lines.append(f"- noisy_only_exercised: `{current['noisy_only']}`")
    lines.append(f"- raw_only_not_surfaced: `{current['raw_only_not_surfaced']}`")
    lines.append(f"- explainability_problematic_exercised: `{current['explainability_problematic']}`")
    lines.append(f"- never_exercised: `{current['never_exercised']}`")
    lines.append("")
    return lines


def _render_counted_rules(module_name: str, rows: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {module_name}", ""]
    for row in rows:
        scenario_hint = ", ".join(row.get("surfacedScenarios", [])[:5]) or "n/a"
        lines.append(
            "- `%s` | bucket=`%s` | expected=%s | unexpected=%s | surfaced_scenarios=%s"
            % (
                row.get("rule_key", ""),
                row.get("bucket", ""),
                row.get("expectedMatchCount", 0),
                row.get("unexpectedMatchCount", 0),
                scenario_hint,
            )
        )
    lines.append("")
    return lines


def _render_excluded_rules(module_name: str, rows: list[dict[str, Any]]) -> list[str]:
    lines = [f"## {module_name}", ""]
    for row in rows:
        lines.append(
            "- `%s` | bucket=`%s` | expected=%s | noisy=%s | raw_scenarios=%s | surfaced_scenarios=%s"
            % (
                row.get("rule_key", ""),
                row.get("bucket", ""),
                row.get("expectedMatchCount", 0),
                row.get("noisyMatchCount", 0),
                len(row.get("rawScenarios", [])),
                len(row.get("surfacedScenarios", [])),
            )
        )
    lines.append("")
    return lines


def _render_noisy_hotspots(payload: list[dict[str, Any]]) -> str:
    lines = ["# Noisy Hotspots After Pass", ""]
    for item in payload[:50]:
        lines.append(
            "- `%s` | module=`%s` | bucket=`%s` | noisy_score=%s | distinct_scenarios=%s"
            % (
                item.get("rule_key", ""),
                item.get("module", ""),
                item.get("bucket", ""),
                item.get("noisy_score", 0),
                item.get("distinct_scenarios", 0),
            )
        )
    lines.append("")
    return "\n".join(lines)


def _sorted_rows(rows: list[dict[str, Any]], include_buckets: set[str]) -> list[dict[str, Any]]:
    selected = [row for row in rows if str(row.get("bucket", "")) in include_buckets]
    return sorted(selected, key=lambda row: (str(row.get("module", "")), str(row.get("rule_key", ""))))


def build_snapshot(previous_snapshot: Path | None) -> Path:
    stamp = timestamp_slug()
    snapshot_root = ensure_dir(SNAPSHOTS_ROOT / stamp)

    aggregate = _load_json(REPORTS_ROOT / "aggregate-summary.json")
    final_status = (REPORTS_ROOT / "FINAL_VALIDATION_STATUS.md").read_text(encoding="utf-8")
    guardian_active = _load_json(REPORTS_ROOT / "guardian-active-rules.json")
    quantum_active = _load_json(REPORTS_ROOT / "quantum-active-rules.json")
    guardian_raw = _load_json(REPORTS_ROOT / "guardian-rule-coverage-raw.json")
    guardian_surfaced = _load_json(REPORTS_ROOT / "guardian-rule-coverage-surfaced.json")
    quantum_raw = _load_json(REPORTS_ROOT / "quantum-rule-coverage-raw.json")
    quantum_surfaced = _load_json(REPORTS_ROOT / "quantum-rule-coverage-surfaced.json")
    rule_to_scenario = _load_json(REPORTS_ROOT / "rule-to-scenario-matrix.json")
    scenario_to_rule = _load_json(REPORTS_ROOT / "scenario-to-rule-matrix.json")
    noisy_hotspots = _load_json(REPORTS_ROOT / "noisy-rule-hotspots.json")

    for filename in (
        "aggregate-summary.json",
        "aggregate-summary.md",
        "aggregate-summary.csv",
        "FINAL_VALIDATION_STATUS.md",
        "rule-coverage-scorecard.md",
        "uncovered-rules-summary.md",
        "guardian-active-rules.json",
        "guardian-active-rules.csv",
        "guardian-active-rules.md",
        "quantum-active-rules.json",
        "quantum-active-rules.csv",
        "quantum-active-rules.md",
        "guardian-rule-coverage.json",
        "guardian-rule-coverage.csv",
        "guardian-rule-coverage.md",
        "guardian-rule-coverage-raw.json",
        "guardian-rule-coverage-surfaced.json",
        "quantum-rule-coverage.json",
        "quantum-rule-coverage.csv",
        "quantum-rule-coverage.md",
        "quantum-rule-coverage-raw.json",
        "quantum-rule-coverage-surfaced.json",
        "rule-to-scenario-matrix.json",
        "scenario-to-rule-matrix.json",
        "noisy-rule-hotspots.json",
        "fail-buckets.json",
    ):
        _copy_if_exists(REPORTS_ROOT / filename, snapshot_root / filename)

    current_guardian = _coverage_summary(guardian_surfaced)
    current_quantum = _coverage_summary(quantum_surfaced)
    current_guardian_raw = _coverage_summary(guardian_raw)
    current_quantum_raw = _coverage_summary(quantum_raw)

    previous_guardian: dict[str, Any] | None = None
    previous_quantum: dict[str, Any] | None = None
    if previous_snapshot and previous_snapshot.exists():
        if (previous_snapshot / "guardian-rule-coverage-surfaced.json").exists():
            previous_guardian = _coverage_summary(_load_json(previous_snapshot / "guardian-rule-coverage-surfaced.json"))
        if (previous_snapshot / "quantum-rule-coverage-surfaced.json").exists():
            previous_quantum = _coverage_summary(_load_json(previous_snapshot / "quantum-rule-coverage-surfaced.json"))

    active_inventory_snapshot = {
        "source_snapshot": stamp,
        "source_of_truth": "runtime-db:rule_definitions@active rule_pack_versions (copied from current reports)",
        "guardian": {
            "active_count": len(guardian_active),
            "rules": guardian_active,
        },
        "quantum": {
            "active_count": len(quantum_active),
            "rules": quantum_active,
        },
    }
    write_json(snapshot_root / "active_inventory_snapshot.json", active_inventory_snapshot)

    frozen_ids = _frozen85_ids()
    by_scenario = aggregate.get("byScenario", {})
    frozen_counter = Counter()
    for scenario_id in sorted(frozen_ids):
        scenario_payload = by_scenario.get(scenario_id, {})
        frozen_counter[str(scenario_payload.get("finalVerdict", "MISSING"))] += 1
    frozen_lines = [
        "# Frozen85 Subset Status",
        "",
        f"- source snapshot: `{stamp}`",
        f"- frozen scenario count: `{len(frozen_ids)}`",
        f"- PASS_CLEAN: `{frozen_counter.get('PASS_CLEAN', 0)}`",
        f"- PASS_WITH_NOISE: `{frozen_counter.get('PASS_WITH_NOISE', 0)}`",
        f"- FAIL_FN: `{frozen_counter.get('FAIL_FN', 0)}`",
        f"- FAIL_FP: `{frozen_counter.get('FAIL_FP', 0)}`",
        f"- FAIL_EXPLAINABILITY: `{frozen_counter.get('FAIL_EXPLAINABILITY', 0)}`",
        f"- FAIL_REF_STATE: `{frozen_counter.get('FAIL_REF_STATE', 0)}`",
        f"- INVALID_SCENARIO: `{frozen_counter.get('INVALID_SCENARIO', 0)}`",
        "",
    ]
    write_text(snapshot_root / "frozen85-subset-status.md", "\n".join(frozen_lines))
    write_json(snapshot_root / "frozen85-subset-status.json", dict(frozen_counter))

    truthful_lines = [
        "# Truthful Coverage Proof",
        "",
        f"- snapshot: `{stamp}`",
        f"- scenario_count: `{len(by_scenario)}`",
        "",
    ]
    truthful_lines.extend(_render_module_section("Guardian", current_guardian, previous_guardian))
    truthful_lines.extend(_render_module_section("Quantum", current_quantum, previous_quantum))
    truthful_lines.append("## Acceptance Gate")
    truthful_lines.append("")
    truthful_lines.append(
        "- counted coverage excludes `noisy_only_exercised`, `raw_only_not_surfaced`, `never_exercised`, and `explainability_problematic_exercised`"
    )
    truthful_lines.append(
        "- counted truthful coverage = `expected_positive_exercised + mixed_exercised`"
    )
    truthful_lines.append("")
    write_text(snapshot_root / "truthful-coverage-proof.md", "\n".join(truthful_lines))

    parity_lines = [
        "# Raw vs Surfaced Parity Report",
        "",
        "## Guardian",
        "",
        f"- raw exercised: `{current_guardian_raw['surfaced_exercised']} / {current_guardian_raw['denominator']}`",
        f"- surfaced exercised: `{current_guardian['surfaced_exercised']} / {current_guardian['denominator']}`",
        f"- raw_only_not_surfaced: `{current_guardian['raw_only_not_surfaced']}`",
        "",
        "## Quantum",
        "",
        f"- raw exercised: `{current_quantum_raw['surfaced_exercised']} / {current_quantum_raw['denominator']}`",
        f"- surfaced exercised: `{current_quantum['surfaced_exercised']} / {current_quantum['denominator']}`",
        f"- raw_only_not_surfaced: `{current_quantum['raw_only_not_surfaced']}`",
        "",
    ]
    if current_guardian["raw_only_not_surfaced"] or current_quantum["raw_only_not_surfaced"]:
        parity_lines.append("## Raw-only Rules")
        parity_lines.append("")
        for module_name, rows in (
            ("guardian", _sorted_rows(guardian_surfaced["rows"], {BUCKET_RAW_ONLY})),
            ("quantum", _sorted_rows(quantum_surfaced["rows"], {BUCKET_RAW_ONLY})),
        ):
            parity_lines.append(f"### {module_name}")
            parity_lines.append("")
            for row in rows:
                parity_lines.append(f"- `{row['rule_key']}`")
            parity_lines.append("")
    write_text(snapshot_root / "raw-vs-surfaced-parity-report.md", "\n".join(parity_lines))

    write_json(snapshot_root / "rule-to-scenario-coverage-map.json", rule_to_scenario)
    write_json(snapshot_root / "scenario-to-rule-coverage-map.json", scenario_to_rule)

    counted_lines = ["# Counted Covered Rules", ""]
    counted_lines.extend(
        _render_counted_rules(
            "Guardian",
            _sorted_rows(guardian_surfaced["rows"], {BUCKET_EXPECTED, BUCKET_MIXED}),
        )
    )
    counted_lines.extend(
        _render_counted_rules(
            "Quantum",
            _sorted_rows(quantum_surfaced["rows"], {BUCKET_EXPECTED, BUCKET_MIXED}),
        )
    )
    write_text(snapshot_root / "counted-covered-rules.md", "\n".join(counted_lines))

    excluded_lines = ["# Excluded From Coverage Rules", ""]
    excluded_bucket_set = {BUCKET_NOISY, BUCKET_RAW_ONLY, BUCKET_NEVER, BUCKET_EXPLAINABILITY, BUCKET_UNCLASSIFIED}
    excluded_lines.extend(
        _render_excluded_rules(
            "Guardian",
            _sorted_rows(guardian_surfaced["rows"], excluded_bucket_set),
        )
    )
    excluded_lines.extend(
        _render_excluded_rules(
            "Quantum",
            _sorted_rows(quantum_surfaced["rows"], excluded_bucket_set),
        )
    )
    write_text(snapshot_root / "excluded-from-coverage-rules.md", "\n".join(excluded_lines))

    write_text(snapshot_root / "noisy-hotspots-after-pass.md", _render_noisy_hotspots(noisy_hotspots))

    return snapshot_root


def main() -> None:
    parser = argparse.ArgumentParser(description="Freeze current coverage state into an immutable truthful snapshot.")
    parser.add_argument(
        "--previous-snapshot",
        type=Path,
        default=DEFAULT_PREVIOUS_SNAPSHOT,
        help="Previous accepted snapshot used for before/after comparison.",
    )
    args = parser.parse_args()
    snapshot_root = build_snapshot(args.previous_snapshot)
    print(snapshot_root)


if __name__ == "__main__":
    main()
