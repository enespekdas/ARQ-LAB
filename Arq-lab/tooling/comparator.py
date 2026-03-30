from __future__ import annotations

from typing import Any

from .models import ExpectedAbsent, ExpectedFinding, ExplainabilityExpectation, ScenarioSpec


def _text(value: Any) -> str:
    return "" if value is None else str(value)


def _join_nonempty(*values: Any) -> str:
    return " | ".join(part for part in (_text(value).strip() for value in values) if part)


def _contains(needle: str | None, haystack: Any) -> bool:
    if needle is None:
        return True
    haystack_text = _text(haystack)
    return bool(haystack_text) and needle.lower() in haystack_text.lower()


def _contains_or_missing(needle: str | None, haystack: Any) -> bool:
    if needle is None:
        return True
    haystack_text = _text(haystack)
    return not haystack_text or needle.lower() in haystack_text.lower()


def _contains_required(needle: str | None, haystack: Any) -> bool:
    if needle is None:
        return True
    haystack_text = _text(haystack).strip()
    return bool(haystack_text) and needle.lower() in haystack_text.lower()


def _path_segments(value: Any) -> list[str]:
    normalized = _text(value).replace("\\", "/").strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return [segment.lower() for segment in normalized.split("/") if segment and segment != "."]


def _path_matches(expected_path: str | None, actual_path: Any) -> bool:
    if expected_path is None:
        return True
    expected_segments = _path_segments(expected_path)
    actual_segments = _path_segments(actual_path)
    if not expected_segments:
        return True
    if not actual_segments:
        return False
    if len(expected_segments) == 1:
        return expected_segments[0] in actual_segments
    for index in range(len(actual_segments) - len(expected_segments) + 1):
        if actual_segments[index : index + len(expected_segments)] == expected_segments:
            return True
    return False


def _detail(item: dict[str, Any]) -> dict[str, Any]:
    detail = item.get("detail", {})
    return detail if isinstance(detail, dict) else {}


def _explainability(item: dict[str, Any]) -> dict[str, Any]:
    explainability = _detail(item).get("explainability", {})
    return explainability if isinstance(explainability, dict) else {}


def _primary_path(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    return item.get("primaryFilePath") or detail.get("primaryFilePath")


def _rule_key(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    return item.get("ruleKey") or detail.get("ruleKey")


def _rule_name(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    return item.get("ruleName") or detail.get("ruleName")


def _finding_kind(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    return item.get("findingKind") or detail.get("findingKind")


def _branch_name(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    return item.get("branchName") or detail.get("branchName")


def _detection_source(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("detectionSource") or detail.get("detectionSource") or item.get("detectionSource")


def _resolved_value(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("resolvedValue") or detail.get("resolvedValue") or item.get("resolvedValue")


def _resolved_haystack(item: dict[str, Any]) -> str:
    detail = _detail(item)
    return _join_nonempty(
        _resolved_value(item),
        _rule_name(item),
        item.get("evidenceExcerpt"),
        detail.get("evidenceExcerpt"),
        _rule_key(item),
    )


def _query_family(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("queryFamily") or detail.get("queryFamily") or item.get("queryFamily")


def _resolution_scope(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("resolutionScope") or detail.get("resolutionScope") or item.get("resolutionScope")


def _semantic_key(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("semanticKey") or detail.get("semanticKey") or item.get("semanticKey")


def _raw_evidence_json(item: dict[str, Any]) -> Any:
    detail = _detail(item)
    explainability = _explainability(item)
    return explainability.get("rawEvidenceJson") or detail.get("rawEvidenceJson") or item.get("rawEvidenceJson")


def _matches_branch(expected_branch: str | None, item: dict[str, Any]) -> bool:
    return expected_branch is None or expected_branch == _branch_name(item)


def _matches_expected_surface(expected: ExpectedFinding, item: dict[str, Any]) -> bool:
    return _path_matches(expected.path_contains, _primary_path(item)) and _matches_branch(expected.branch_name, item)


def _match_expected_without_refstate(expected: ExpectedFinding, item: dict[str, Any]) -> bool:
    return (
        _matches_expected_surface(expected, item)
        and _contains(expected.rule_key_contains, _rule_key(item))
        and _contains_or_missing(expected.resolved_value_contains, _resolved_haystack(item))
        and _contains_or_missing(expected.query_family_contains, _query_family(item))
        and _contains_or_missing(expected.detection_source, _detection_source(item))
        and _contains_or_missing(expected.finding_kind, _finding_kind(item))
    )


def _match_refstate(expected: ExpectedFinding, item: dict[str, Any]) -> bool:
    detail = _detail(item)
    present_on_head = detail.get("presentOnHead", item.get("presentOnHead"))
    present_in_history = detail.get("presentInHistory", item.get("presentInHistory"))
    exposure_scope = detail.get("exposureScope", item.get("exposureScope"))
    return (
        (expected.present_on_head is None or expected.present_on_head == present_on_head)
        and (expected.present_in_history is None or expected.present_in_history == present_in_history)
        and (expected.exposure_scope is None or expected.exposure_scope == exposure_scope)
    )


def _match_absent(expected: ExpectedAbsent, item: dict[str, Any]) -> bool:
    return (
        _path_matches(expected.path_contains, _primary_path(item))
        and _contains(expected.rule_key_contains, _rule_key(item))
        and _contains(expected.resolved_value_contains, _resolved_haystack(item))
    )


def _has_semantic_signal(item: dict[str, Any]) -> bool:
    return any(
        _text(value).strip()
        for value in (
            _query_family(item),
            _resolved_value(item),
            _semantic_key(item),
            _resolution_scope(item),
            _raw_evidence_json(item),
        )
    )


def _has_semantic_explainability(item: dict[str, Any]) -> bool:
    detection_source = _text(_detection_source(item)).upper()
    return detection_source in {"SEMANTIC", "HYBRID"} or _has_semantic_signal(item)


def _is_regex_only(item: dict[str, Any]) -> bool:
    detection_source = _text(_detection_source(item)).upper()
    return "REGEX" in detection_source and not _has_semantic_signal(item)


def _match_explainability_contract(expected: ExplainabilityExpectation, item: dict[str, Any]) -> bool:
    return (
        _path_matches(expected.path_contains, _primary_path(item))
        and _contains_required(expected.resolved_value_contains, _resolved_value(item))
        and _contains_required(expected.query_family_contains, _query_family(item))
        and _contains_required(expected.resolution_scope_contains, _resolution_scope(item))
        and _contains_required(expected.detection_source_contains, _detection_source(item))
        and _has_semantic_explainability(item)
    )


def _contracts_for_expected(expected: ExpectedFinding, scenario: ScenarioSpec) -> list[ExplainabilityExpectation]:
    return [
        contract
        for contract in scenario.explainability_expectations
        if contract.key == expected.key
        or _path_matches(expected.path_contains, contract.path_contains)
        or _path_matches(contract.path_contains, expected.path_contains)
    ]


def _contract_summary(contract: ExplainabilityExpectation) -> dict[str, Any]:
    return {
        "key": contract.key,
        "pathContains": contract.path_contains,
        "resolvedValueContains": contract.resolved_value_contains,
        "queryFamilyContains": contract.query_family_contains,
        "resolutionScopeContains": contract.resolution_scope_contains,
        "detectionSourceContains": contract.detection_source_contains,
    }


def _finding_summary(item: dict[str, Any]) -> dict[str, Any]:
    detail = _detail(item)
    return {
        "findingId": item.get("findingId"),
        "ruleKey": _rule_key(item),
        "ruleName": _rule_name(item),
        "module": item.get("module") or detail.get("module"),
        "severity": item.get("severity") or detail.get("severity"),
        "findingKind": _finding_kind(item),
        "branchName": _branch_name(item),
        "primaryFilePath": _primary_path(item),
        "scanMode": item.get("scanMode"),
        "scanPlanName": item.get("scanPlanName"),
        "presentOnHead": item.get("presentOnHead", detail.get("presentOnHead")),
        "presentInHistory": item.get("presentInHistory", detail.get("presentInHistory")),
        "exposureScope": item.get("exposureScope", detail.get("exposureScope")),
        "detectionSource": _detection_source(item),
        "semanticKey": _semantic_key(item),
        "resolvedValue": _resolved_value(item),
        "queryFamily": _query_family(item),
        "resolutionScope": _resolution_scope(item),
        "rawEvidenceJson": _raw_evidence_json(item),
        "evidenceExcerpt": item.get("evidenceExcerpt") or detail.get("evidenceExcerpt"),
    }


def _finding_identifier_from_summary(summary: dict[str, Any]) -> str:
    finding_id = _text(summary.get("findingId"))
    if finding_id:
        return finding_id
    return "|".join(
        [
            _text(summary.get("module")),
            _text(summary.get("branchName")),
            _text(summary.get("primaryFilePath")),
            _text(summary.get("ruleKey")),
            _text(summary.get("findingKind")),
            _text(summary.get("presentOnHead")),
            _text(summary.get("presentInHistory")),
            _text(summary.get("exposureScope")),
        ]
    )


def _summary_sort_key(summary: dict[str, Any]) -> tuple[str, ...]:
    return (
        _text(summary.get("primaryFilePath")),
        _text(summary.get("ruleKey")),
        _text(summary.get("branchName")),
        _text(summary.get("findingId")),
    )


def _candidate_score(expected: ExpectedFinding, item: dict[str, Any]) -> int:
    score = 0
    if expected.rule_key_contains and _contains(expected.rule_key_contains, _rule_key(item)):
        score += 16
    if expected.resolved_value_contains and _contains(expected.resolved_value_contains, _resolved_haystack(item)):
        score += 8
    if expected.query_family_contains and _contains(expected.query_family_contains, _query_family(item)):
        score += 4
    if expected.detection_source and _contains(expected.detection_source, _detection_source(item)):
        score += 2
    if expected.finding_kind and _contains(expected.finding_kind, _finding_kind(item)):
        score += 1
    if _has_semantic_explainability(item):
        score += 3
    if _text(_detection_source(item)).upper() == "AST":
        score += 1
    return score


def _select_best_candidate(
    expected: ExpectedFinding,
    candidates: list[dict[str, Any]],
    matched_finding_ids: set[str],
) -> dict[str, Any]:
    available = [item for item in candidates if _text(item.get("findingId")) not in matched_finding_ids]
    pool = available or candidates
    best = pool[0]
    best_score = _candidate_score(expected, best)
    for item in pool[1:]:
        score = _candidate_score(expected, item)
        if score > best_score:
            best = item
            best_score = score
            continue
        if score == best_score and _summary_sort_key(_finding_summary(item)) < _summary_sort_key(_finding_summary(best)):
            best = item
    return best


def _normalization_fingerprint(item: dict[str, Any]) -> tuple[str, ...]:
    summary = _finding_summary(item)
    return (
        _text(summary.get("module")),
        _text(summary.get("branchName")),
        _text(summary.get("primaryFilePath")),
        _text(summary.get("ruleKey")),
        _text(summary.get("findingKind")),
        _text(summary.get("presentOnHead")),
        _text(summary.get("presentInHistory")),
        _text(summary.get("exposureScope")),
        _text(summary.get("detectionSource")),
        _text(summary.get("semanticKey")),
        _text(summary.get("resolvedValue")),
        _text(summary.get("queryFamily")),
    )


def _finding_quality(item: dict[str, Any]) -> tuple[int, tuple[str, ...]]:
    score = 0
    if _detail(item):
        score += 1
    if _text(_resolved_value(item)).strip():
        score += 8
    if _text(_query_family(item)).strip():
        score += 8
    if _text(_semantic_key(item)).strip():
        score += 4
    if _text(_resolution_scope(item)).strip():
        score += 4
    if _raw_evidence_json(item) not in {None, ""}:
        score += 4
    detection_source = _text(_detection_source(item)).upper()
    if detection_source and "REGEX" not in detection_source:
        score += 6
    if _text(item.get("scanPlanName")).strip():
        score += 1
    return score, _summary_sort_key(_finding_summary(item))


def _normalize_actual_findings(actual_findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    selected: dict[tuple[str, ...], dict[str, Any]] = {}
    for item in actual_findings:
        fingerprint = _normalization_fingerprint(item)
        current = selected.get(fingerprint)
        if current is None or _finding_quality(item) > _finding_quality(current):
            selected[fingerprint] = item
    return sorted(selected.values(), key=lambda item: _summary_sort_key(_finding_summary(item)))


def _is_review_only(summary: dict[str, Any]) -> bool:
    return _text(summary.get("findingKind")).upper() == "INVENTORY" or _text(summary.get("severity")).upper() == "INFO"


def _unique_summaries(summaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for summary in summaries:
        summary_id = _finding_identifier_from_summary(summary)
        current = unique.get(summary_id)
        if current is None or _summary_sort_key(summary) < _summary_sort_key(current):
            unique[summary_id] = summary
    return [unique[key] for key in sorted(unique, key=lambda item_id: _summary_sort_key(unique[item_id]))]


def _noise_breakdown(
    same_surface_extra_findings: list[dict[str, Any]],
    same_file_different_signal_findings: list[dict[str, Any]],
    extra_findings: list[dict[str, Any]],
    may_find_review: list[dict[str, Any]],
    unexpected_regex_only_findings: list[dict[str, Any]],
) -> dict[str, int]:
    return {
        "sameSurfaceExtraFindings": len(same_surface_extra_findings),
        "sameFileDifferentSignalFindings": len(same_file_different_signal_findings),
        "totallyUnexpectedFindings": len(extra_findings),
        "reviewOnlyFindings": len(may_find_review),
        "unexpectedRegexOnlyFindings": len(unexpected_regex_only_findings),
    }


def _noise_reason(noise_breakdown: dict[str, int]) -> str:
    labels = [
        ("same-surface-extra", noise_breakdown["sameSurfaceExtraFindings"]),
        ("same-file-different-signal", noise_breakdown["sameFileDifferentSignalFindings"]),
        ("totally-unexpected", noise_breakdown["totallyUnexpectedFindings"]),
        ("review-only", noise_breakdown["reviewOnlyFindings"]),
        ("regex-only", noise_breakdown["unexpectedRegexOnlyFindings"]),
    ]
    return ", ".join(f"{label}={count}" for label, count in labels if count)


def _build_verdict_reason(
    *,
    runnability: dict[str, str],
    must_find_missing: list[dict[str, Any]],
    must_not_find_violations: list[dict[str, Any]],
    explainability_failures: list[dict[str, Any]],
    ref_state_failures: list[dict[str, Any]],
    noise_count: int,
    noise_breakdown: dict[str, int],
) -> str:
    reasons: list[str] = []
    failed_stages = [stage for stage, state in sorted(runnability.items()) if state == "failed"]
    if failed_stages:
        reasons.append(f"runnability failed on {', '.join(failed_stages)}")
    if must_not_find_violations:
        reasons.append(f"{len(must_not_find_violations)} must-not-find violation(s) hit protected or declared-clean surfaces")
    if must_find_missing:
        reasons.append(f"{len(must_find_missing)} expected finding(s) were not detected at all")
    if ref_state_failures:
        reasons.append(f"{len(ref_state_failures)} expected finding(s) matched signal but failed ref/history state checks")
    if explainability_failures:
        reasons.append(f"{len(explainability_failures)} expected finding(s) had candidates but failed semantic explainability requirements")
    if noise_count:
        reasons.append(f"{noise_count} unexpected/noisy finding(s) remained after matching ({_noise_reason(noise_breakdown)})")
    if not reasons:
        return "all expected findings matched cleanly with no unexpected noise"
    return "; ".join(reasons)


def compare_scenario(
    scenario: ScenarioSpec,
    actual_findings: list[dict[str, Any]],
    *,
    runnability: dict[str, str],
) -> dict[str, Any]:
    normalized_actual_findings = _normalize_actual_findings(actual_findings)
    matched_finding_ids: set[str] = set()
    must_find_matched: list[dict[str, Any]] = []
    must_find_missing: list[dict[str, Any]] = []
    ref_state_failures: list[dict[str, Any]] = []
    explainability_failures: list[dict[str, Any]] = []

    for expected in scenario.expected_findings:
        signal_candidates = [item for item in normalized_actual_findings if _match_expected_without_refstate(expected, item)]
        if not signal_candidates:
            must_find_missing.append({"expected": expected.key, "pathContains": expected.path_contains})
            continue

        refstate_matches = [item for item in signal_candidates if _match_refstate(expected, item)]
        if not refstate_matches:
            ref_state_failures.append(
                {
                    "expected": expected.key,
                    "pathContains": expected.path_contains,
                    "candidates": [_finding_summary(item) for item in signal_candidates],
                }
            )
            continue

        explainability_contracts = _contracts_for_expected(expected, scenario)
        qualified_matches = refstate_matches
        if explainability_contracts:
            qualified_matches = [
                item
                for item in refstate_matches
                if all(_match_explainability_contract(contract, item) for contract in explainability_contracts)
            ]
            if not qualified_matches:
                explainability_failures.append(
                    {
                        "expected": expected.key,
                        "pathContains": expected.path_contains,
                        "required": [_contract_summary(contract) for contract in explainability_contracts],
                        "candidates": [_finding_summary(item) for item in refstate_matches],
                        "regexOnlyCandidates": [
                            _finding_summary(item) for item in refstate_matches if scenario.module in {"quantum", "both"} and _is_regex_only(item)
                        ],
                    }
                )
                continue

        best = _select_best_candidate(expected, qualified_matches, matched_finding_ids)
        matched_finding_ids.add(_text(best.get("findingId")))
        must_find_matched.append({"expected": expected.key, "actual": _finding_summary(best)})

    must_not_find_violations: list[dict[str, Any]] = []
    must_not_finding_ids: set[str] = set()
    for expected in scenario.expected_absent:
        for item in normalized_actual_findings:
            if _match_absent(expected, item):
                summary = _finding_summary(item)
                must_not_find_violations.append({"expected": expected.key, "actual": summary})
                must_not_finding_ids.add(_finding_identifier_from_summary(summary))

    same_surface_extra_findings: list[dict[str, Any]] = []
    same_file_different_signal_findings: list[dict[str, Any]] = []
    extra_findings: list[dict[str, Any]] = []
    may_find_review: list[dict[str, Any]] = []
    unexpected_regex_only_findings: list[dict[str, Any]] = []

    for item in normalized_actual_findings:
        summary = _finding_summary(item)
        finding_id = _finding_identifier_from_summary(summary)
        if finding_id in matched_finding_ids or finding_id in must_not_finding_ids:
            continue

        surface_matches = [expected for expected in scenario.expected_findings if _matches_expected_surface(expected, item)]
        full_signal_matches = [expected for expected in surface_matches if _match_expected_without_refstate(expected, item)]

        if surface_matches:
            if full_signal_matches:
                same_surface_extra_findings.append(summary)
            else:
                same_file_different_signal_findings.append(summary)
        elif _is_review_only(summary):
            may_find_review.append(summary)
        else:
            extra_findings.append(summary)

        if scenario.module in {"quantum", "both"} and _is_regex_only(item):
            unexpected_regex_only_findings.append(summary)

    same_surface_extra_findings = _unique_summaries(same_surface_extra_findings)
    same_file_different_signal_findings = _unique_summaries(same_file_different_signal_findings)
    extra_findings = _unique_summaries(extra_findings)
    may_find_review = _unique_summaries(may_find_review)
    unexpected_regex_only_findings = _unique_summaries(unexpected_regex_only_findings)
    unexpected_findings = _unique_summaries(
        same_surface_extra_findings + same_file_different_signal_findings + extra_findings + may_find_review
    )
    noise_count = len(_unique_summaries(unexpected_findings + unexpected_regex_only_findings))
    noise_breakdown = _noise_breakdown(
        same_surface_extra_findings,
        same_file_different_signal_findings,
        extra_findings,
        may_find_review,
        unexpected_regex_only_findings,
    )

    safe_control_violations = [violation for violation in must_not_find_violations if "safe" in violation["expected"]]

    verdict = "PASS_CLEAN"
    if must_not_find_violations:
        verdict = "FAIL_FP"
    elif must_find_missing:
        verdict = "FAIL_FN"
    elif ref_state_failures:
        verdict = "FAIL_REF_STATE"
    elif explainability_failures:
        verdict = "FAIL_EXPLAINABILITY"
    elif noise_count:
        verdict = "PASS_WITH_NOISE"

    if runnability.get("build") == "failed" or runnability.get("test") == "failed" or runnability.get("smoke") == "failed":
        verdict = "INVALID_SCENARIO" if verdict in {"PASS_CLEAN", "PASS_WITH_NOISE"} else verdict

    final_verdict_reason = _build_verdict_reason(
        runnability=runnability,
        must_find_missing=must_find_missing,
        must_not_find_violations=must_not_find_violations,
        explainability_failures=explainability_failures,
        ref_state_failures=ref_state_failures,
        noise_count=noise_count,
        noise_breakdown=noise_breakdown,
    )

    return {
        "scenarioId": scenario.id,
        "milestone": scenario.milestone,
        "module": scenario.module,
        "runnability": runnability,
        "mustFindExpected": len(scenario.expected_findings),
        "mustFindMatched": len(must_find_matched),
        "cleanExpectedMatches": len(must_find_matched),
        "mustFindMissing": must_find_missing,
        "missingExpectedFindings": must_find_missing,
        "mustNotFindViolations": must_not_find_violations,
        "sameSurfaceExtraFindings": same_surface_extra_findings,
        "sameFileDifferentSignalFindings": same_file_different_signal_findings,
        "extraFindings": extra_findings,
        "unexpectedFindings": unexpected_findings,
        "mayFindReview": may_find_review,
        "explainabilityFailures": explainability_failures,
        "refStateFailures": ref_state_failures,
        "unexpectedRegexOnlyFindings": unexpected_regex_only_findings,
        "safeControlViolations": safe_control_violations,
        "noiseCount": noise_count,
        "noiseBreakdown": noise_breakdown,
        "verdict": verdict,
        "finalVerdict": verdict,
        "verdictClass": verdict,
        "finalVerdictReason": final_verdict_reason,
        "followUpAction": "none" if verdict == "PASS_CLEAN" else "review findings",
        "matchedFindings": must_find_matched,
        "normalizationStats": {
            "rawFindings": len(actual_findings),
            "normalizedFindings": len(normalized_actual_findings),
            "collapsedDuplicates": len(actual_findings) - len(normalized_actual_findings),
        },
    }
