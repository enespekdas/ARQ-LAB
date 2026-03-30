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


def _match_explainability(expected: ExplainabilityExpectation, item: dict[str, Any]) -> bool:
    return (
        _path_matches(expected.path_contains, _primary_path(item))
        and _contains_or_missing(expected.resolved_value_contains, _resolved_haystack(item))
        and _contains_or_missing(expected.query_family_contains, _query_family(item))
        and _contains_or_missing(expected.resolution_scope_contains, _resolution_scope(item))
        and _contains_or_missing(expected.detection_source_contains, _detection_source(item))
    )


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
        "presentOnHead": item.get("presentOnHead", detail.get("presentOnHead")),
        "presentInHistory": item.get("presentInHistory", detail.get("presentInHistory")),
        "exposureScope": item.get("exposureScope", detail.get("exposureScope")),
        "detectionSource": _detection_source(item),
        "semanticKey": _semantic_key(item),
        "resolvedValue": _resolved_value(item),
        "queryFamily": _query_family(item),
    }


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
    return best


def compare_scenario(
    scenario: ScenarioSpec,
    actual_findings: list[dict[str, Any]],
    *,
    runnability: dict[str, str],
) -> dict[str, Any]:
    matched_finding_ids: set[str] = set()
    must_find_matched: list[dict[str, Any]] = []
    must_find_missing: list[dict[str, Any]] = []
    ref_state_failures: list[dict[str, Any]] = []

    for expected in scenario.expected_findings:
        candidates = [item for item in actual_findings if _match_expected_without_refstate(expected, item)]
        if not candidates:
            must_find_missing.append({"expected": expected.key, "pathContains": expected.path_contains})
            continue
        refstate_matches = [item for item in candidates if _match_refstate(expected, item)]
        if refstate_matches:
            best = _select_best_candidate(expected, refstate_matches, matched_finding_ids)
            matched_finding_ids.add(_text(best.get("findingId")))
            must_find_matched.append({"expected": expected.key, "actual": _finding_summary(best)})
            continue
        ref_state_failures.append(
            {
                "expected": expected.key,
                "pathContains": expected.path_contains,
                "candidates": [_finding_summary(item) for item in candidates],
            }
        )

    must_not_find_violations = []
    for expected in scenario.expected_absent:
        for item in actual_findings:
            if _match_absent(expected, item):
                must_not_find_violations.append({"expected": expected.key, "actual": _finding_summary(item)})

    explainability_failures = []
    for expected in scenario.explainability_expectations:
        path_candidates = [item for item in actual_findings if _path_matches(expected.path_contains, _primary_path(item))]
        if not path_candidates:
            continue
        matches = [item for item in path_candidates if _match_explainability(expected, item)]
        if not matches:
            explainability_failures.append({"expected": expected.key, "pathContains": expected.path_contains})

    extra_findings = []
    may_find_review = []
    unexpected_regex_only_findings = []
    for item in actual_findings:
        finding_id = _text(item.get("findingId"))
        summary = _finding_summary(item)
        detection_source = _text(summary.get("detectionSource")).lower()
        finding_kind = _text(summary.get("findingKind")).upper()
        if finding_id in matched_finding_ids:
            continue
        if any(_matches_expected_surface(expected, item) for expected in scenario.expected_findings):
            if scenario.module in {"quantum", "both"} and detection_source and "regex" in detection_source and not summary.get("queryFamily"):
                unexpected_regex_only_findings.append(summary)
            continue
        if finding_kind == "INVENTORY" or summary.get("severity") == "INFO":
            may_find_review.append(summary)
        else:
            extra_findings.append(summary)
        if scenario.module in {"quantum", "both"} and detection_source and "regex" in detection_source and not summary.get("queryFamily"):
            unexpected_regex_only_findings.append(summary)

    safe_control_violations = [violation for violation in must_not_find_violations if "safe" in violation["expected"]]

    verdict = "PASS"
    if must_not_find_violations:
        verdict = "FAIL_FP"
    elif must_find_missing:
        verdict = "FAIL_FN"
    elif explainability_failures:
        verdict = "FAIL_EXPLAINABILITY"
    elif ref_state_failures:
        verdict = "FAIL_REF_STATE"
    elif extra_findings:
        verdict = "PASS_WITH_NOISE"

    if runnability.get("build") == "failed" or runnability.get("test") == "failed" or runnability.get("smoke") == "failed":
        verdict = "INVALID_SCENARIO" if verdict == "PASS" else verdict

    return {
        "scenarioId": scenario.id,
        "milestone": scenario.milestone,
        "module": scenario.module,
        "runnability": runnability,
        "mustFindExpected": len(scenario.expected_findings),
        "mustFindMatched": len(must_find_matched),
        "mustFindMissing": must_find_missing,
        "mustNotFindViolations": must_not_find_violations,
        "extraFindings": extra_findings,
        "mayFindReview": may_find_review,
        "explainabilityFailures": explainability_failures,
        "refStateFailures": ref_state_failures,
        "unexpectedRegexOnlyFindings": unexpected_regex_only_findings,
        "safeControlViolations": safe_control_violations,
        "verdict": verdict,
        "followUpAction": "review findings" if verdict != "PASS" else "none",
        "matchedFindings": must_find_matched,
    }
