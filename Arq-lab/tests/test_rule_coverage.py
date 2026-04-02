from __future__ import annotations

from pathlib import Path

from tooling.rule_coverage import (
    BUCKET_EXPLAINABILITY,
    BUCKET_EXPECTED,
    BUCKET_NEVER,
    BUCKET_NOISY,
    classify_rule_coverage,
    load_latest_scenario_artifacts,
)
from tooling.utils import write_json


def _comparison(
    scenario_id: str,
    milestone: str,
    *,
    matched: list[dict] | None = None,
    unexpected: list[dict] | None = None,
    same_surface: list[dict] | None = None,
    same_file: list[dict] | None = None,
    explainability: list[dict] | None = None,
) -> dict:
    return {
        "scenarioId": scenario_id,
        "milestone": milestone,
        "verdict": "PASS_CLEAN",
        "matchedFindings": matched or [],
        "unexpectedFindings": unexpected or [],
        "sameSurfaceExtraFindings": same_surface or [],
        "sameFileDifferentSignalFindings": same_file or [],
        "mayFindReview": [],
        "mustNotFindViolations": [],
        "explainabilityFailures": explainability or [],
    }


def _finding(rule_key: str, module: str, detection_source: str) -> dict:
    return {
        "ruleKey": rule_key,
        "module": module,
        "detail": {
            "ruleKey": rule_key,
            "module": module,
            "explainability": {
                "detectionSource": detection_source,
            },
        },
        "detectionSource": detection_source,
    }


def test_load_latest_scenario_artifacts_uses_latest_run(tmp_path: Path) -> None:
    old_dir = tmp_path / "runs" / "20260401T100000Z" / "M3" / "Q-V3-JAVA-001"
    new_dir = tmp_path / "runs" / "20260401T110000Z" / "M3" / "Q-V3-JAVA-001"
    write_json(old_dir / "comparison.json", _comparison("Q-V3-JAVA-001", "M3"))
    write_json(old_dir / "findings-normalized.json", [])
    write_json(new_dir / "comparison.json", _comparison("Q-V3-JAVA-001", "M3"))
    write_json(new_dir / "findings-normalized.json", [{"ruleKey": "quantum.arq-q-0013-java"}])

    artifacts = load_latest_scenario_artifacts(tmp_path / "runs")

    assert len(artifacts) == 1
    assert artifacts[0].run_stamp == "20260401T110000Z"
    assert artifacts[0].findings == [{"ruleKey": "quantum.arq-q-0013-java"}]


def test_classify_rule_coverage_builds_expected_buckets(tmp_path: Path) -> None:
    runs_root = tmp_path / "runs"
    active_rules = {
        "sourceOfTruth": {"kind": "runtime-db"},
        "guardian": [
            {"rule_key": "guardian.generic-api-key", "module": "guardian", "family": "generic-api-key", "language": "", "title": "", "severity": "", "finding_kind": "SECRET", "source_of_truth": "runtime-db", "pack_display_name": "", "bootstrap_resource": "", "active": True},
            {"rule_key": "guardian.private-key", "module": "guardian", "family": "private-key", "language": "", "title": "", "severity": "", "finding_kind": "SECRET", "source_of_truth": "runtime-db", "pack_display_name": "", "bootstrap_resource": "", "active": True},
        ],
        "quantum": [
            {"rule_key": "quantum.arq-q-0613-typescript", "module": "quantum", "family": "", "language": "typescript", "title": "", "severity": "", "finding_kind": "VULNERABILITY", "source_of_truth": "runtime-db", "pack_display_name": "", "bootstrap_resource": "", "active": True},
            {"rule_key": "quantum.arq-q-0449-csharp", "module": "quantum", "family": "", "language": "csharp", "title": "", "severity": "", "finding_kind": "VULNERABILITY", "source_of_truth": "runtime-db", "pack_display_name": "", "bootstrap_resource": "", "active": True},
            {"rule_key": "quantum.arq-q-unused", "module": "quantum", "family": "", "language": "", "title": "", "severity": "", "finding_kind": "VULNERABILITY", "source_of_truth": "runtime-db", "pack_display_name": "", "bootstrap_resource": "", "active": True},
        ],
    }

    s1 = runs_root / "20260401T100000Z" / "M8" / "M-V8-009"
    s2 = runs_root / "20260401T100100Z" / "M4" / "Q-V4-TS-006"
    s3 = runs_root / "20260401T100200Z" / "M7" / "N-V7-DOCS-013"
    s4 = runs_root / "20260401T100300Z" / "M6" / "Q-V6-CS-004"

    write_json(
        s1 / "comparison.json",
        _comparison(
            "M-V8-009",
            "M8",
            matched=[{"actual": {"ruleKey": "guardian.generic-api-key", "module": "guardian"}}],
            unexpected=[{"ruleKey": "guardian.private-key", "module": "guardian"}],
        ),
    )
    write_json(
        s1 / "findings-normalized.json",
        [
            _finding("guardian.generic-api-key", "guardian", "REGEX"),
            _finding("guardian.private-key", "guardian", "REGEX"),
        ],
    )

    write_json(
        s2 / "comparison.json",
        _comparison(
            "Q-V4-TS-006",
            "M4",
            explainability=[
                {
                    "candidates": [
                        {"ruleKey": "quantum.arq-q-0613-typescript", "module": "quantum", "detectionSource": "REGEX"}
                    ]
                }
            ],
            same_surface=[{"ruleKey": "quantum.arq-q-0613-typescript", "module": "quantum"}],
            unexpected=[{"ruleKey": "quantum.arq-q-0613-typescript", "module": "quantum"}],
        ),
    )
    write_json(
        s2 / "findings-normalized.json",
        [_finding("quantum.arq-q-0613-typescript", "quantum", "REGEX")],
    )

    write_json(
        s3 / "comparison.json",
        _comparison(
            "N-V7-DOCS-013",
            "M7",
            matched=[{"actual": {"ruleKey": "guardian.generic-api-key", "module": "guardian"}}],
        ),
    )
    write_json(
        s3 / "findings-normalized.json",
        [_finding("guardian.generic-api-key", "guardian", "REGEX")],
    )

    write_json(
        s4 / "comparison.json",
        _comparison(
            "Q-V6-CS-004",
            "M6",
            unexpected=[{"ruleKey": "quantum.arq-q-0449-csharp", "module": "quantum"}],
        ),
    )
    write_json(
        s4 / "findings-normalized.json",
        [_finding("quantum.arq-q-0449-csharp", "quantum", "REGEX")],
    )

    coverage = classify_rule_coverage(active_rules, load_latest_scenario_artifacts(runs_root))

    guardian_rows = {row["rule_key"]: row for row in coverage["modules"]["guardian"]["rows"]}
    quantum_rows = {row["rule_key"]: row for row in coverage["modules"]["quantum"]["rows"]}

    assert coverage["modules"]["guardian"]["bucketCounts"][BUCKET_EXPECTED] == 1
    assert coverage["modules"]["guardian"]["bucketCounts"][BUCKET_NOISY] == 1
    assert guardian_rows["guardian.generic-api-key"]["bucket"] == BUCKET_EXPECTED
    assert guardian_rows["guardian.private-key"]["bucket"] == BUCKET_NOISY

    assert coverage["modules"]["quantum"]["bucketCounts"][BUCKET_EXPLAINABILITY] == 1
    assert quantum_rows["quantum.arq-q-0613-typescript"]["bucket"] == BUCKET_EXPLAINABILITY
    assert quantum_rows["quantum.arq-q-0449-csharp"]["bucket"] == BUCKET_NOISY
    assert quantum_rows["quantum.arq-q-unused"]["bucket"] == BUCKET_NEVER

    hotspots = coverage["noisyRuleHotspots"]
    assert hotspots[0]["rule_key"] == "quantum.arq-q-0613-typescript"
