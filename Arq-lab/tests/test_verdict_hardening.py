from __future__ import annotations

from tooling.comparator import compare_scenario
from tooling.models import BuildPlan, ExplainabilityExpectation, ExpectedFinding, ScanPlan, ScenarioSpec
from tooling.report_renderer import aggregate_comparisons


def _scenario(*, module: str, expected_findings: list[ExpectedFinding], explainability_expectations: list[ExplainabilityExpectation] | None = None) -> ScenarioSpec:
    return ScenarioSpec(
        id="S-001",
        milestone="M1",
        repo_name="repo",
        module=module,
        family="unit",
        stack="unit",
        domain="unit",
        summary="unit",
        line_target="1",
        scan_plans=[ScanPlan(name="scan", modules=[module], scan_mode="HEAD_SNAPSHOT")],
        build_plan=BuildPlan(),
        expected_findings=expected_findings,
        explainability_expectations=explainability_expectations or [],
    )


def _finding(
    *,
    finding_id: str,
    path: str,
    rule_key: str,
    rule_name: str,
    detection_source: str = "SEMANTIC",
    resolved_value: str | None = None,
    query_family: str | None = None,
    semantic_key: str | None = None,
    severity: str = "HIGH",
    finding_kind: str = "VULNERABILITY",
) -> dict:
    return {
        "findingId": finding_id,
        "module": "quantum",
        "branchName": "main",
        "primaryFilePath": path,
        "ruleKey": rule_key,
        "ruleName": rule_name,
        "findingKind": finding_kind,
        "severity": severity,
        "detail": {
            "module": "quantum",
            "branchName": "main",
            "primaryFilePath": path,
            "ruleKey": rule_key,
            "ruleName": rule_name,
            "findingKind": finding_kind,
            "severity": severity,
            "presentOnHead": True,
            "presentInHistory": False,
            "exposureScope": "HEAD_ONLY",
            "detectionSource": detection_source,
            "explainability": {
                "detectionSource": detection_source,
                "queryFamily": query_family,
                "resolvedValue": resolved_value,
                "resolutionScope": "SAME_METHOD" if query_family else None,
                "semanticKey": semantic_key,
                "rawEvidenceJson": {"kind": "unit"} if semantic_key else None,
            },
        },
    }


def test_same_surface_extra_findings_are_not_hidden() -> None:
    scenario = _scenario(
        module="guardian",
        expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py")],
    )
    actual_findings = [
        _finding(finding_id="f1", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret"),
        _finding(finding_id="f2", path="src/config.py", rule_key="guardian.private-key", rule_name="Secondary secret family"),
    ]

    comparison = compare_scenario(scenario, actual_findings, runnability={"build": "passed", "test": "passed", "smoke": "passed"})

    assert comparison["verdict"] == "PASS_WITH_NOISE"
    assert comparison["cleanExpectedMatches"] == 1
    assert len(comparison["sameSurfaceExtraFindings"]) == 1
    assert comparison["noiseCount"] == 1
    assert "same-surface-extra=1" in comparison["finalVerdictReason"]


def test_quantum_regex_only_candidate_fails_explainability_instead_of_passing() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[ExpectedFinding(key="md5", path_contains="legacy.py", resolved_value_contains="MD5")],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy.py",
                resolved_value_contains="MD5",
                query_family_contains="python",
            )
        ],
    )
    actual_findings = [
        _finding(
            finding_id="f1",
            path="app/legacy.py",
            rule_key="quantum.arq-q-0001-python",
            rule_name="hashlib: MD5 usage",
            detection_source="REGEX",
            resolved_value=None,
            query_family=None,
            semantic_key=None,
        )
    ]

    comparison = compare_scenario(scenario, actual_findings, runnability={"build": "passed", "test": "passed", "smoke": "passed"})

    assert comparison["verdict"] == "FAIL_EXPLAINABILITY"
    assert comparison["mustFindMissing"] == []
    assert comparison["cleanExpectedMatches"] == 0
    assert len(comparison["explainabilityFailures"]) == 1
    assert len(comparison["unexpectedRegexOnlyFindings"]) == 1


def test_aggregate_comparisons_surfaces_verdict_reason_and_noise_fields() -> None:
    comparisons = [
        {
            "scenarioId": "S-CLEAN",
            "milestone": "M1",
            "verdict": "PASS_CLEAN",
            "verdictClass": "PASS_CLEAN",
            "mustFindExpected": 1,
            "cleanExpectedMatches": 1,
            "mustFindMatched": 1,
            "mustFindMissing": [],
            "missingExpectedFindings": [],
            "mustNotFindViolations": [],
            "sameSurfaceExtraFindings": [],
            "sameFileDifferentSignalFindings": [],
            "unexpectedFindings": [],
            "extraFindings": [],
            "mayFindReview": [],
            "unexpectedRegexOnlyFindings": [],
            "explainabilityFailures": [],
            "refStateFailures": [],
            "noiseCount": 0,
            "noiseBreakdown": {},
            "finalVerdictReason": "all expected findings matched cleanly with no unexpected noise",
            "auditArtifacts": {"dossierMissing": False, "reportDossierPath": "clean.md", "locComposition": {}},
        },
        {
            "scenarioId": "S-NOISY",
            "milestone": "M1",
            "verdict": "PASS_WITH_NOISE",
            "verdictClass": "PASS_WITH_NOISE",
            "mustFindExpected": 1,
            "cleanExpectedMatches": 1,
            "mustFindMatched": 1,
            "mustFindMissing": [],
            "missingExpectedFindings": [],
            "mustNotFindViolations": [],
            "sameSurfaceExtraFindings": [{"findingId": "x"}],
            "sameFileDifferentSignalFindings": [],
            "unexpectedFindings": [{"findingId": "x"}],
            "extraFindings": [],
            "mayFindReview": [],
            "unexpectedRegexOnlyFindings": [],
            "explainabilityFailures": [],
            "refStateFailures": [],
            "noiseCount": 1,
            "noiseBreakdown": {"sameSurfaceExtraFindings": 1},
            "finalVerdictReason": "1 unexpected/noisy finding remained after matching",
            "auditArtifacts": {"dossierMissing": False, "reportDossierPath": "noisy.md", "locComposition": {}},
        },
    ]

    aggregate = aggregate_comparisons(comparisons)

    assert aggregate["verdicts"]["PASS_CLEAN"] == 1
    assert aggregate["verdicts"]["PASS_WITH_NOISE"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["sameSurfaceExtraFindings"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["noiseCount"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["finalVerdictReason"] == "1 unexpected/noisy finding remained after matching"
