from __future__ import annotations

from typing import Any

from .comparator import compare_scenario
from .models import BuildPlan, ExplainabilityExpectation, ExpectedFinding, ScanPlan, ScenarioSpec

PROOF_SCENARIO_ID = "PROOF-PASS-WITH-NOISE"


def _finding(
    *,
    finding_id: str,
    path: str,
    rule_key: str,
    rule_name: str,
    detection_source: str,
    resolved_value: str | None,
    query_family: str | None,
    semantic_key: str | None,
    evidence_excerpt: str,
) -> dict[str, Any]:
    return {
        "findingId": finding_id,
        "module": "quantum",
        "branchName": "main",
        "primaryFilePath": path,
        "ruleKey": rule_key,
        "ruleName": rule_name,
        "findingKind": "VULNERABILITY",
        "severity": "HIGH",
        "evidenceExcerpt": evidence_excerpt,
        "detail": {
            "module": "quantum",
            "branchName": "main",
            "primaryFilePath": path,
            "ruleKey": rule_key,
            "ruleName": rule_name,
            "findingKind": "VULNERABILITY",
            "severity": "HIGH",
            "evidenceExcerpt": evidence_excerpt,
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
                "rawEvidenceJson": {"proof": True, "findingId": finding_id} if semantic_key else None,
            },
        },
    }


def build_pass_with_noise_proof() -> dict[str, Any]:
    scenario = ScenarioSpec(
        id=PROOF_SCENARIO_ID,
        milestone="M0",
        repo_name="verdict-proof-pass-with-noise",
        module="quantum",
        family="proof",
        stack="typescript",
        domain="verdict hardening proof",
        summary="Minimal proof that a semantic-qualified expected match can coexist with visible regex-only noise and still end in PASS_WITH_NOISE.",
        line_target="1",
        scan_plans=[ScanPlan(name="proof-quantum-head", modules=["quantum"], scan_mode="HEAD_SNAPSHOT")],
        build_plan=BuildPlan(),
        expected_findings=[
            ExpectedFinding(
                key="proof-md5",
                path_contains="legacyDigest.ts",
                rule_key_contains="0613",
                resolved_value_contains="MD5",
                query_family_contains="typescript",
            )
        ],
        explainability_expectations=[
            ExplainabilityExpectation(
                key="proof-md5",
                path_contains="legacyDigest.ts",
                resolved_value_contains="MD5",
                query_family_contains="typescript",
                resolution_scope_contains="SAME_METHOD",
                detection_source_contains="SEMANTIC",
            )
        ],
    )

    actual_findings = [
        _finding(
            finding_id="proof-semantic-match",
            path="src/security/legacyDigest.ts",
            rule_key="quantum.arq-q-0613-typescript",
            rule_name="Weak Hash (MD5)",
            detection_source="SEMANTIC",
            resolved_value="MD5",
            query_family="crypto.typescript.hash",
            semantic_key="md5-call",
            evidence_excerpt="return createHash('md5').update(value).digest('hex');",
        ),
        _finding(
            finding_id="proof-regex-noise",
            path="src/security/legacyDigest.ts",
            rule_key="quantum.arq-q-0613-typescript",
            rule_name="Weak Hash (MD5)",
            detection_source="REGEX",
            resolved_value=None,
            query_family=None,
            semantic_key=None,
            evidence_excerpt="return createHash('md5').update(value).digest('hex');",
        ),
    ]

    comparison = compare_scenario(
        scenario,
        actual_findings,
        runnability={"build": "passed", "test": "passed", "smoke": "passed"},
    )
    comparison["auditArtifacts"] = {
        "reportDossierPath": "n/a (synthetic proof fixture)",
        "runnabilityLogRootPath": "n/a (synthetic proof fixture)",
        "dossierMissing": False,
        "locComposition": {},
    }

    return {
        "scenario": {
            "id": scenario.id,
            "repo_name": scenario.repo_name,
            "milestone": scenario.milestone,
            "module": scenario.module,
            "stack": scenario.stack,
            "domain": scenario.domain,
        },
        "comparison": comparison,
        "scans": [
            {
                "plan": {"name": "proof-quantum-head"},
                "completed": {"status": "SUCCEEDED", "scannedRefName": "main"},
            }
        ],
        "proofChecks": {
            "cleanExpectedMatches": comparison["cleanExpectedMatches"],
            "missingExpectedFindings": len(comparison["missingExpectedFindings"]),
            "mustNotFindViolations": len(comparison["mustNotFindViolations"]),
            "explainabilityFailures": len(comparison["explainabilityFailures"]),
            "noiseCount": comparison["noiseCount"],
            "sameSurfaceExtraFindings": len(comparison["sameSurfaceExtraFindings"]),
            "unexpectedRegexOnlyFindings": len(comparison["unexpectedRegexOnlyFindings"]),
            "finalVerdict": comparison["verdictClass"],
        },
    }
