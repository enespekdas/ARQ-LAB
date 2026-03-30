from __future__ import annotations

import json
from pathlib import Path

import pytest

from tooling.comparator import compare_scenario
from tooling.models import BuildPlan, ExpectedAbsent, ExpectedFinding, ExplainabilityExpectation, ScanPlan, ScenarioSpec
from tooling.report_renderer import aggregate_comparisons, render_scenario_report, write_aggregate_reports
from tooling.verdict_proof import PROOF_SCENARIO_ID, build_pass_with_noise_proof

PASSED_RUNNABILITY = {"build": "passed", "test": "passed", "smoke": "passed"}
FAILED_RUNNABILITY = {"build": "failed", "test": "passed", "smoke": "passed"}


def _scenario(
    *,
    module: str,
    scenario_id: str = "S-001",
    expected_findings: list[ExpectedFinding] | None = None,
    expected_absent: list[ExpectedAbsent] | None = None,
    explainability_expectations: list[ExplainabilityExpectation] | None = None,
) -> ScenarioSpec:
    return ScenarioSpec(
        id=scenario_id,
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
        expected_findings=expected_findings or [],
        expected_absent=expected_absent or [],
        explainability_expectations=explainability_expectations or [],
    )


def _finding(
    *,
    finding_id: str,
    path: str,
    rule_key: str,
    rule_name: str,
    module: str = "quantum",
    detection_source: str = "SEMANTIC",
    resolved_value: str | None = None,
    query_family: str | None = None,
    semantic_key: str | None = None,
    finding_kind: str = "VULNERABILITY",
    severity: str = "HIGH",
    evidence_excerpt: str | None = None,
) -> dict:
    excerpt = evidence_excerpt or rule_name
    return {
        "findingId": finding_id,
        "module": module,
        "branchName": "main",
        "primaryFilePath": path,
        "ruleKey": rule_key,
        "ruleName": rule_name,
        "findingKind": finding_kind,
        "severity": severity,
        "evidenceExcerpt": excerpt,
        "detail": {
            "module": module,
            "branchName": "main",
            "primaryFilePath": path,
            "ruleKey": rule_key,
            "ruleName": rule_name,
            "findingKind": finding_kind,
            "severity": severity,
            "evidenceExcerpt": excerpt,
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
                "rawEvidenceJson": {"kind": "unit", "findingId": finding_id} if semantic_key else None,
            },
        },
    }


def _compare(
    scenario: ScenarioSpec,
    findings: list[dict],
    *,
    runnability: dict[str, str] | None = None,
) -> dict:
    return compare_scenario(scenario, findings, runnability=runnability or PASSED_RUNNABILITY)


def _comparison_with_audit(
    *,
    comparison: dict,
    report_name: str,
) -> dict:
    comparison = dict(comparison)
    comparison["auditArtifacts"] = {
        "dossierMissing": False,
        "dossierPath": f"generated/{report_name}/validation/generated-project-dossier.md",
        "projectLocalDossierPath": f"generated/{report_name}/validation/generated-project-dossier.md",
        "reportDossierPath": f"reports/generated-project-dossiers/{report_name}.md",
        "generatedManifestPath": f"generated/{report_name}/validation/generated-file-manifest.json",
        "generatedTreePath": f"generated/{report_name}/validation/generated-tree.txt",
        "runnabilityLogRootPath": f"generated/{report_name}/validation/runnability-logs",
        "locComposition": {"live business code": 10, "live config": 2, "tests": 3, "synthetic filler / inflation content": 0},
        "fillerRatio": 0.0,
        "realismScore": 3,
        "realismJustification": "unit proof",
    }
    return comparison


def test_pass_clean_example() -> None:
    scenario = _scenario(
        module="guardian",
        expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py", rule_key_contains="generic-api-key")],
    )
    comparison = _compare(
        scenario,
        [_finding(finding_id="f1", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret", module="guardian")],
    )

    assert comparison["finalVerdict"] == "PASS_CLEAN"
    assert comparison["cleanExpectedMatches"] == 1
    assert comparison["noiseCount"] == 0


def test_pass_with_noise_example() -> None:
    proof = build_pass_with_noise_proof()
    comparison = proof["comparison"]

    assert comparison["finalVerdict"] == "PASS_WITH_NOISE"
    assert comparison["cleanExpectedMatches"] == 1
    assert comparison["missingExpectedFindings"] == []
    assert comparison["mustNotFindViolations"] == []
    assert comparison["explainabilityFailures"] == []
    assert comparison["noiseCount"] == 1


def test_fail_fn_example() -> None:
    scenario = _scenario(module="guardian", expected_findings=[ExpectedFinding(key="missing", path_contains="src/app.py")])
    comparison = _compare(scenario, [])

    assert comparison["finalVerdict"] == "FAIL_FN"
    assert len(comparison["missingExpectedFindings"]) == 1


def test_fail_fp_example() -> None:
    scenario = _scenario(
        module="guardian",
        expected_absent=[ExpectedAbsent(key="protected-mock", path_contains="mocks/mock.pem", rule_key_contains="private-key")],
    )
    comparison = _compare(
        scenario,
        [_finding(finding_id="fp1", path="mocks/mock.pem", rule_key="guardian.private-key", rule_name="Private key", module="guardian")],
    )

    assert comparison["finalVerdict"] == "FAIL_FP"
    assert len(comparison["mustNotFindViolations"]) == 1


def test_fail_explainability_example() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[ExpectedFinding(key="md5", path_contains="legacy.py", resolved_value_contains="MD5")],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy.py",
                resolved_value_contains="MD5",
                query_family_contains="python",
                detection_source_contains="SEMANTIC",
            )
        ],
    )
    comparison = _compare(
        scenario,
        [
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
        ],
    )

    assert comparison["finalVerdict"] == "FAIL_EXPLAINABILITY"
    assert comparison["mustFindMissing"] == []
    assert len(comparison["explainabilityFailures"]) == 1


def test_invalid_scenario_example() -> None:
    scenario = _scenario(
        module="guardian",
        expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py", rule_key_contains="generic-api-key")],
    )
    comparison = _compare(
        scenario,
        [_finding(finding_id="f1", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret", module="guardian")],
        runnability=FAILED_RUNNABILITY,
    )

    assert comparison["finalVerdict"] == "INVALID_SCENARIO"
    assert "runnability failed on build" in comparison["finalVerdictReason"]


def test_same_surface_extra_findings_bucket_behavior() -> None:
    proof = build_pass_with_noise_proof()
    comparison = proof["comparison"]

    assert len(comparison["sameSurfaceExtraFindings"]) == 1
    assert comparison["sameSurfaceExtraFindings"][0]["primaryFilePath"].endswith("legacyDigest.ts")
    assert comparison["noiseBreakdown"]["sameSurfaceExtraFindings"] == 1


def test_same_file_different_signal_findings_bucket_behavior() -> None:
    scenario = _scenario(
        module="guardian",
        expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py", rule_key_contains="generic-api-key")],
    )
    comparison = _compare(
        scenario,
        [
            _finding(finding_id="f1", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret", module="guardian"),
            _finding(finding_id="f2", path="src/config.py", rule_key="guardian.oauth-client-id", rule_name="OAuth client id", module="guardian"),
        ],
    )

    assert comparison["finalVerdict"] == "PASS_WITH_NOISE"
    assert len(comparison["sameFileDifferentSignalFindings"]) == 1
    assert comparison["noiseBreakdown"]["sameFileDifferentSignalFindings"] == 1


def test_unexpected_regex_only_findings_are_counted() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[ExpectedFinding(key="md5", path_contains="legacy.py", resolved_value_contains="MD5")],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy.py",
                resolved_value_contains="MD5",
                query_family_contains="python",
                detection_source_contains="SEMANTIC",
            )
        ],
    )
    comparison = _compare(
        scenario,
        [
            _finding(
                finding_id="f1",
                path="app/legacy.py",
                rule_key="quantum.arq-q-0001-python",
                rule_name="hashlib: MD5 usage",
                detection_source="SEMANTIC",
                resolved_value="MD5",
                query_family="crypto.python.hash",
                semantic_key="md5-call",
            ),
            _finding(
                finding_id="f2",
                path="app/legacy.py",
                rule_key="quantum.arq-q-0001-python",
                rule_name="hashlib: MD5 usage",
                detection_source="REGEX",
                resolved_value=None,
                query_family=None,
                semantic_key=None,
            ),
        ],
    )

    assert comparison["finalVerdict"] == "PASS_WITH_NOISE"
    assert len(comparison["unexpectedRegexOnlyFindings"]) == 1
    assert comparison["noiseBreakdown"]["unexpectedRegexOnlyFindings"] == 1


def test_verdict_precedence_prefers_fail_fp_over_missing_and_noise() -> None:
    scenario = _scenario(
        module="guardian",
        expected_findings=[ExpectedFinding(key="missing", path_contains="src/missing.py")],
        expected_absent=[ExpectedAbsent(key="mock", path_contains="mocks/mock.pem", rule_key_contains="private-key")],
    )
    comparison = _compare(
        scenario,
        [_finding(finding_id="fp1", path="mocks/mock.pem", rule_key="guardian.private-key", rule_name="Private key", module="guardian")],
    )

    assert comparison["finalVerdict"] == "FAIL_FP"


def test_verdict_precedence_prefers_fail_fn_over_explainability_and_noise() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[
            ExpectedFinding(key="missing", path_contains="src/missing.py"),
            ExpectedFinding(key="md5", path_contains="legacy.py", resolved_value_contains="MD5"),
        ],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy.py",
                resolved_value_contains="MD5",
                query_family_contains="python",
                detection_source_contains="SEMANTIC",
            )
        ],
    )
    comparison = _compare(
        scenario,
        [
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
        ],
    )

    assert comparison["finalVerdict"] == "FAIL_FN"


def test_semantic_required_regex_only_not_counted_as_success() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[ExpectedFinding(key="md5", path_contains="legacy.py", resolved_value_contains="MD5")],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy.py",
                resolved_value_contains="MD5",
                query_family_contains="python",
                detection_source_contains="SEMANTIC",
            )
        ],
    )
    comparison = _compare(
        scenario,
        [
            _finding(
                finding_id="regex-only",
                path="app/legacy.py",
                rule_key="quantum.arq-q-0001-python",
                rule_name="hashlib: MD5 usage",
                detection_source="REGEX",
                resolved_value=None,
                query_family=None,
                semantic_key=None,
            )
        ],
    )

    assert comparison["cleanExpectedMatches"] == 0
    assert comparison["matchedFindings"] == []
    assert len(comparison["unexpectedRegexOnlyFindings"]) == 1


def test_explainability_contracts_do_not_cross_match_same_path_expectations() -> None:
    scenario = _scenario(
        module="quantum",
        expected_findings=[
            ExpectedFinding(key="md5", path_contains="legacy_hash.go", resolved_value_contains="MD5"),
            ExpectedFinding(key="sha1", path_contains="legacy_hash.go", resolved_value_contains="SHA1"),
        ],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="md5",
                path_contains="legacy_hash.go",
                resolved_value_contains="MD5",
                query_family_contains="go",
            ),
            ExplainabilityExpectation(
                key="sha1",
                path_contains="legacy_hash.go",
                resolved_value_contains="SHA1",
                query_family_contains="go",
            ),
        ],
    )
    comparison = _compare(
        scenario,
        [
            _finding(
                finding_id="go-md5",
                path="internal/security/legacy_hash.go",
                rule_key="quantum.arq-q-0572-go",
                rule_name="Weak Hash (MD5)",
                detection_source="AST",
                resolved_value="MD5",
                query_family="go.crypto",
                semantic_key="go:crypto:md5.New:MD5",
            ),
            _finding(
                finding_id="go-sha1",
                path="internal/security/legacy_hash.go",
                rule_key="quantum.arq-q-0573-go",
                rule_name="Weak Hash (SHA1)",
                detection_source="AST",
                resolved_value="SHA1",
                query_family="go.crypto",
                semantic_key="go:crypto:sha1.New:SHA1",
            ),
        ],
    )

    assert comparison["finalVerdict"] == "PASS_CLEAN"
    assert comparison["cleanExpectedMatches"] == 2
    assert comparison["explainabilityFailures"] == []


@pytest.mark.parametrize(
    ("scenario", "findings", "expected_verdict"),
    [
        (
            _scenario(
                module="guardian",
                scenario_id="S-CLEAN",
                expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py", rule_key_contains="generic-api-key")],
            ),
            [_finding(finding_id="clean", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret", module="guardian")],
            "INVALID_SCENARIO",
        ),
        (
            _scenario(
                module="quantum",
                scenario_id="S-NOISY",
                expected_findings=[ExpectedFinding(key="proof-md5", path_contains="legacyDigest.ts", resolved_value_contains="MD5", query_family_contains="typescript")],
                explainability_expectations=[
                    ExplainabilityExpectation(
                        key="proof-md5",
                        path_contains="legacyDigest.ts",
                        resolved_value_contains="MD5",
                        query_family_contains="typescript",
                        detection_source_contains="SEMANTIC",
                    )
                ],
            ),
            [
                _finding(
                    finding_id="semantic",
                    path="src/security/legacyDigest.ts",
                    rule_key="quantum.arq-q-0613-typescript",
                    rule_name="Weak Hash (MD5)",
                    detection_source="SEMANTIC",
                    resolved_value="MD5",
                    query_family="crypto.typescript.hash",
                    semantic_key="md5-call",
                ),
                _finding(
                    finding_id="noise",
                    path="src/security/legacyDigest.ts",
                    rule_key="quantum.arq-q-0613-typescript",
                    rule_name="Weak Hash (MD5)",
                    detection_source="REGEX",
                    resolved_value=None,
                    query_family=None,
                    semantic_key=None,
                ),
            ],
            "INVALID_SCENARIO",
        ),
        (
            _scenario(module="guardian", scenario_id="S-FAIL", expected_findings=[ExpectedFinding(key="missing", path_contains="src/missing.py")]),
            [],
            "FAIL_FN",
        ),
    ],
)
def test_runnability_failure_only_invalidates_clean_or_noisy_candidates(
    scenario: ScenarioSpec,
    findings: list[dict],
    expected_verdict: str,
) -> None:
    comparison = _compare(scenario, findings, runnability=FAILED_RUNNABILITY)
    assert comparison["finalVerdict"] == expected_verdict


def test_render_scenario_report_shows_final_verdict_reason_and_noise_fields() -> None:
    proof = build_pass_with_noise_proof()
    report = render_scenario_report(proof["scenario"], proof["comparison"], proof["scans"])

    assert "Final verdict: `PASS_WITH_NOISE`" in report
    assert "- sameSurfaceExtraFindings: `1`" in report
    assert "- unexpectedRegexOnlyFindings: `1`" in report
    assert "- finalVerdict: `PASS_WITH_NOISE`" in report
    assert "- finalVerdictReason:" in report


def test_aggregate_summary_includes_required_fields_and_proof_artifacts(tmp_path: Path) -> None:
    clean_scenario = _scenario(
        module="guardian",
        scenario_id="S-CLEAN",
        expected_findings=[ExpectedFinding(key="secret", path_contains="src/config.py", rule_key_contains="generic-api-key")],
    )
    clean = _comparison_with_audit(
        comparison=_compare(
            clean_scenario,
            [_finding(finding_id="clean", path="src/config.py", rule_key="guardian.generic-api-key", rule_name="Primary secret", module="guardian")],
        ),
        report_name="S-CLEAN",
    )
    proof = build_pass_with_noise_proof()
    noisy = _comparison_with_audit(comparison=proof["comparison"], report_name="S-NOISY")
    noisy["scenarioId"] = "S-NOISY"
    noisy["milestone"] = "M1"

    write_aggregate_reports(tmp_path, [clean, noisy])

    aggregate = json.loads((tmp_path / "aggregate-summary.json").read_text(encoding="utf-8"))

    assert aggregate["verdicts"]["PASS_CLEAN"] == 1
    assert aggregate["verdicts"]["PASS_WITH_NOISE"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["finalVerdict"] == "PASS_WITH_NOISE"
    assert aggregate["byScenario"]["S-NOISY"]["unexpectedFindings"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["unexpectedRegexOnlyFindings"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["sameSurfaceExtraFindings"] == 1
    assert aggregate["byScenario"]["S-NOISY"]["mayFindReview"] == 0
    assert aggregate["byScenario"]["S-NOISY"]["persistedLogsPath"].endswith("runnability-logs")
    assert aggregate["byScenario"]["S-NOISY"]["runnability"] == PASSED_RUNNABILITY
    assert aggregate["proofArtifacts"]["passWithNoiseReportPath"].endswith("pass-with-noise-scenario-report.md")
    assert Path(aggregate["proofArtifacts"]["passWithNoiseReportPath"]).exists()
    assert Path(aggregate["proofArtifacts"]["passWithNoiseComparisonPath"]).exists()


def test_final_verdict_reason_visible_in_written_reports(tmp_path: Path) -> None:
    proof = build_pass_with_noise_proof()
    comparison = _comparison_with_audit(comparison=proof["comparison"], report_name="S-NOISY")
    comparison["scenarioId"] = "S-NOISY"

    write_aggregate_reports(tmp_path, [comparison])

    aggregate_md = (tmp_path / "aggregate-summary.md").read_text(encoding="utf-8")
    final_status = (tmp_path / "FINAL_VALIDATION_STATUS.md").read_text(encoding="utf-8")
    fail_buckets = json.loads((tmp_path / "fail-buckets.json").read_text(encoding="utf-8"))

    assert "PASS_WITH_NOISE" in aggregate_md
    assert comparison["finalVerdictReason"] in aggregate_md
    assert "pass-with-noise-summary.md" in final_status
    assert fail_buckets[0]["finalVerdict"] == "PASS_WITH_NOISE"
    assert fail_buckets[0]["finalVerdictReason"] == comparison["finalVerdictReason"]


def test_dossier_chain_preserved_in_aggregate_summary() -> None:
    proof = build_pass_with_noise_proof()
    comparison = _comparison_with_audit(comparison=proof["comparison"], report_name="S-NOISY")
    comparison["scenarioId"] = "S-NOISY"

    aggregate = aggregate_comparisons([comparison])
    summary = aggregate["byScenario"]["S-NOISY"]

    assert summary["dossierPath"].endswith("generated-project-dossier.md")
    assert summary["generatedManifestPath"].endswith("generated-file-manifest.json")
    assert summary["generatedTreePath"].endswith("generated-tree.txt")
    assert summary["persistedLogsPath"].endswith("runnability-logs")


def test_pass_with_noise_proof_fixture_is_stable() -> None:
    proof = build_pass_with_noise_proof()
    comparison = proof["comparison"]
    proof_checks = proof["proofChecks"]

    assert proof["scenario"]["id"] == PROOF_SCENARIO_ID
    assert comparison["finalVerdict"] == "PASS_WITH_NOISE"
    assert proof_checks == {
        "cleanExpectedMatches": 1,
        "missingExpectedFindings": 0,
        "mustNotFindViolations": 0,
        "explainabilityFailures": 0,
        "noiseCount": 1,
        "sameSurfaceExtraFindings": 1,
        "unexpectedRegexOnlyFindings": 1,
        "finalVerdict": "PASS_WITH_NOISE",
    }
