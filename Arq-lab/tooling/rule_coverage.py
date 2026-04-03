from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any

from .env import load_config
from .utils import ensure_dir, read_json, run_command, write_json, write_text


BUCKET_EXPECTED = "expected_positive_exercised"
BUCKET_NOISY = "noisy_only_exercised"
BUCKET_MIXED = "mixed_exercised"
BUCKET_EXPLAINABILITY = "explainability_problematic_exercised"
BUCKET_RAW_ONLY = "raw_only_not_surfaced"
BUCKET_UNCLASSIFIED = "unclassified_exercised"
BUCKET_NEVER = "never_exercised"


@dataclass(slots=True)
class ScenarioArtifacts:
    scenario_id: str
    milestone: str
    run_stamp: str
    comparison_path: Path
    surfaced_findings_path: Path
    raw_findings_paths: list[str]
    comparison: dict[str, Any]
    surfaced_findings: list[dict[str, Any]]
    raw_findings: list[dict[str, Any]]


def _detail(item: dict[str, Any]) -> dict[str, Any]:
    detail = item.get("detail", {})
    return detail if isinstance(detail, dict) else {}


def _rule_key(item: dict[str, Any]) -> str:
    detail = _detail(item)
    return str(item.get("ruleKey") or detail.get("ruleKey") or "").strip()


def _detection_source(item: dict[str, Any]) -> str:
    explainability = _detail(item).get("explainability", {})
    if not isinstance(explainability, dict):
        explainability = {}
    return str(
        explainability.get("detectionSource")
        or _detail(item).get("detectionSource")
        or item.get("detectionSource")
        or ""
    ).strip()


def _scenario_sort_key(path: Path) -> tuple[str, int]:
    run_stamp = path.parts[-4] if len(path.parts) >= 4 else ""
    return (run_stamp, path.stat().st_mtime_ns)


def _load_raw_findings(scenario_root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    findings: list[dict[str, Any]] = []
    source_paths: list[str] = []
    for export_path in sorted(scenario_root.rglob("findings-export.json")):
        payload = read_json(export_path, {})
        items = payload.get("items", []) if isinstance(payload, dict) else []
        if not isinstance(items, list):
            continue
        detail_path = export_path.with_name("finding-details.json")
        details = read_json(detail_path, {}) if detail_path.exists() else {}
        if not isinstance(details, dict):
            details = {}
        source_paths.append(str(export_path))
        for item in items:
            if not isinstance(item, dict):
                continue
            normalized = dict(item)
            finding_id = str(item.get("findingId") or "")
            detail = details.get(finding_id, {})
            normalized["detail"] = detail if isinstance(detail, dict) else {}
            findings.append(normalized)
    return findings, source_paths


def load_latest_scenario_artifacts(runs_root: Path) -> list[ScenarioArtifacts]:
    latest_by_scenario: dict[str, tuple[tuple[str, int], ScenarioArtifacts]] = {}
    for comparison_path in runs_root.rglob("comparison.json"):
        comparison = read_json(comparison_path, {})
        if not comparison:
            continue
        scenario_id = str(comparison.get("scenarioId") or comparison_path.parent.name)
        surfaced_findings_path = comparison_path.parent / "findings-normalized.json"
        surfaced_findings = read_json(surfaced_findings_path, [])
        if not isinstance(surfaced_findings, list):
            surfaced_findings = []
        raw_findings, raw_findings_paths = _load_raw_findings(comparison_path.parent)
        run_stamp = comparison_path.parts[-4] if len(comparison_path.parts) >= 4 else ""
        artifacts = ScenarioArtifacts(
            scenario_id=scenario_id,
            milestone=str(comparison.get("milestone") or comparison_path.parts[-3]),
            run_stamp=run_stamp,
            comparison_path=comparison_path,
            surfaced_findings_path=surfaced_findings_path,
            raw_findings_paths=raw_findings_paths,
            comparison=comparison,
            surfaced_findings=surfaced_findings,
            raw_findings=raw_findings,
        )
        sort_key = _scenario_sort_key(comparison_path)
        current = latest_by_scenario.get(scenario_id)
        if current is None or sort_key >= current[0]:
            latest_by_scenario[scenario_id] = (sort_key, artifacts)
    return [entry[1] for entry in sorted(latest_by_scenario.values(), key=lambda item: (item[1].milestone, item[1].scenario_id))]


def _docker_lines(command: list[str], cwd: Path) -> list[str]:
    result = run_command(command, cwd, check=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def _discover_postgres_container(cwd: Path) -> str:
    names = _docker_lines(["docker", "ps", "--format", "{{.Names}}"], cwd)
    for preferred in ("arq-v2-postgres", "arq-postgres"):
        if preferred in names:
            return preferred
    for name in names:
        if "postgres" in name.lower():
            return name
    raise RuntimeError("No running postgres container found for ARQ runtime inventory")


def _docker_env(container_name: str, cwd: Path) -> dict[str, str]:
    lines = _docker_lines(["docker", "exec", container_name, "env"], cwd)
    values: dict[str, str] = {}
    for line in lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key] = value
    return values


def _psql_json(container_name: str, db_name: str, db_user: str, sql: str, cwd: Path) -> list[dict[str, Any]]:
    lines = _docker_lines(
        ["docker", "exec", container_name, "psql", "-U", db_user, "-d", db_name, "-At", "-c", sql],
        cwd,
    )
    if not lines:
        return []
    payload = json.loads("\n".join(lines))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        return [payload]
    raise RuntimeError("Unexpected JSON payload returned by psql")


def _derive_language(rule_key: str, metadata: dict[str, Any]) -> str:
    language = metadata.get("language")
    if isinstance(language, str) and language.strip():
        return language.strip()
    for suffix in (
        "java",
        "csharp",
        "typescript",
        "python",
        "javascript",
        "config",
        "go",
        "cpp",
        "scala",
        "kotlin",
        "ruby",
        "php",
        "rust",
        "swift",
        "powershell",
        "shell",
        "objectivec",
        "groovy",
        "c",
        "elixir",
        "erlang",
        "perl",
        "jcl",
        "tsql",
        "plsql",
        "zig",
        "lua",
        "abap",
    ):
        if rule_key.endswith(f"-{suffix}"):
            return suffix
    return ""


def _derive_family(rule_key: str, metadata: dict[str, Any]) -> str:
    for key in ("family", "queryFamily", "query_family"):
        value = metadata.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    legacy = metadata.get("legacyRuleId")
    if isinstance(legacy, str) and legacy.strip():
        return legacy.strip()
    if rule_key.startswith("guardian."):
        return rule_key.split(".", 1)[1]
    return ""


def load_active_rules(config, *, cwd: Path) -> dict[str, Any]:
    container = _discover_postgres_container(cwd)
    env_values = _docker_env(container, cwd)
    db_name = env_values.get("POSTGRES_DB", "arq_v2")
    db_user = env_values.get("POSTGRES_USER", "arq")
    sql = """
select coalesce(json_agg(t order by t.rule_key), '[]'::json)::text
from (
    select
        rp.pack_key as module,
        rp.display_name as pack_display_name,
        rp.bootstrap_resource,
        rd.rule_key,
        rd.rule_name as title,
        rd.severity,
        rd.finding_kind,
        rd.metadata_json
    from rule_definitions rd
    join rule_pack_versions rpv on rd.rule_pack_version_id = rpv.id
    join rule_packs rp on rpv.rule_pack_id = rp.id
    where rpv.active = true
    order by rp.pack_key, rd.rule_key
) t;
""".strip()
    rows = _psql_json(container, db_name, db_user, sql, cwd)
    grouped: dict[str, list[dict[str, Any]]] = {"guardian": [], "quantum": []}
    for row in rows:
        metadata = row.get("metadata_json") if isinstance(row.get("metadata_json"), dict) else {}
        module = str(row.get("module") or "").strip()
        rule_key = str(row.get("rule_key") or "").strip()
        item = {
            "rule_key": rule_key,
            "module": module,
            "family": _derive_family(rule_key, metadata),
            "language": _derive_language(rule_key, metadata),
            "title": row.get("title") or "",
            "severity": row.get("severity") or "",
            "finding_kind": row.get("finding_kind") or "",
            "source_of_truth": "runtime-db:rule_definitions@active rule_pack_versions",
            "pack_display_name": row.get("pack_display_name") or "",
            "bootstrap_resource": row.get("bootstrap_resource") or "",
            "active": True,
        }
        grouped.setdefault(module, []).append(item)
    return {
        "sourceOfTruth": {
            "kind": "runtime-db",
            "container": container,
            "database": db_name,
            "user": db_user,
            "query": "rule_definitions join active rule_pack_versions join rule_packs",
        },
        "guardian": sorted(grouped.get("guardian", []), key=lambda item: item["rule_key"]),
        "quantum": sorted(grouped.get("quantum", []), key=lambda item: item["rule_key"]),
    }


def _finding_counts(items: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for item in items:
        rule_key = _rule_key(item)
        if rule_key:
            counts[rule_key] += 1
    return dict(counts)


def _actual_from_matched(entry: dict[str, Any]) -> dict[str, Any]:
    actual = entry.get("actual", {})
    return actual if isinstance(actual, dict) else {}


def _rule_keys_from_explainability_failure(entry: dict[str, Any]) -> set[str]:
    keys: set[str] = set()
    for field in ("candidates", "regexOnlyCandidates"):
        candidates = entry.get(field, [])
        if not isinstance(candidates, list):
            continue
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            rule_key = _rule_key(candidate)
            if rule_key:
                keys.add(rule_key)
    return keys


def classify_rule_coverage(active_rules: dict[str, Any], artifacts: list[ScenarioArtifacts]) -> dict[str, Any]:
    module_maps = {
        "guardian": {item["rule_key"]: dict(item) for item in active_rules["guardian"]},
        "quantum": {item["rule_key"]: dict(item) for item in active_rules["quantum"]},
    }
    stats_by_rule: dict[str, dict[str, Any]] = {}
    scenario_to_rule_matrix: dict[str, dict[str, Any]] = {}

    def ensure_stat(rule_key: str, module_hint: str = "") -> dict[str, Any]:
        stat = stats_by_rule.get(rule_key)
        if stat is not None:
            return stat
        base = module_maps.get(module_hint, {}).get(rule_key)
        if base is None:
            base = module_maps["guardian"].get(rule_key) or module_maps["quantum"].get(rule_key) or {
                "rule_key": rule_key,
                "module": module_hint or "unknown",
                "family": "",
                "language": "",
                "title": "",
                "severity": "",
                "finding_kind": "",
                "source_of_truth": "same-run-findings",
                "pack_display_name": "",
                "bootstrap_resource": "",
                "active": False,
            }
        stat = {
            **base,
            "rawDistinctScenarioCount": 0,
            "surfacedDistinctScenarioCount": 0,
            "rawTotalFindingCount": 0,
            "surfacedTotalFindingCount": 0,
            "expectedMatchCount": 0,
            "unexpectedMatchCount": 0,
            "noisyMatchCount": 0,
            "mustNotFindViolationCount": 0,
            "sameSurfaceExtraCount": 0,
            "sameFileDifferentSignalCount": 0,
            "reviewOnlyCount": 0,
            "explainabilityGapCount": 0,
            "rawRegexOnlyCount": 0,
            "surfacedRegexOnlyCount": 0,
            "rawHybridCount": 0,
            "surfacedHybridCount": 0,
            "rawSemanticCount": 0,
            "surfacedSemanticCount": 0,
            "rawAstCount": 0,
            "surfacedAstCount": 0,
            "regexOnlyCount": 0,
            "hybridCount": 0,
            "semanticCount": 0,
            "astCount": 0,
            "rawScenarios": set(),
            "surfacedScenarios": set(),
            "noiseScenarios": set(),
            "expectedScenarios": set(),
            "explainabilityScenarios": set(),
            "rawDetectionSources": set(),
            "surfacedDetectionSources": set(),
            "detectionSources": set(),
            "bucket": BUCKET_UNCLASSIFIED,
            "regexOnlyOnlyExercised": False,
            "rawRegexOnlyOnlyExercised": False,
        }
        stats_by_rule[rule_key] = stat
        return stat

    for artifact in artifacts:
        scenario_matrix = {
            "milestone": artifact.milestone,
            "runStamp": artifact.run_stamp,
            "comparisonPath": str(artifact.comparison_path),
            "surfacedFindingsPath": str(artifact.surfaced_findings_path),
            "rawFindingsPaths": artifact.raw_findings_paths,
            "verdict": artifact.comparison.get("verdict"),
            "finalVerdict": artifact.comparison.get("finalVerdict") or artifact.comparison.get("verdictClass") or artifact.comparison.get("verdict"),
            "rawRules": [],
            "surfacedRules": [],
        }
        raw_rules: set[str] = set()
        surfaced_rules: set[str] = set()

        for finding in artifact.raw_findings:
            rule_key = _rule_key(finding)
            if not rule_key:
                continue
            module = str(finding.get("module") or _detail(finding).get("module") or "")
            stat = ensure_stat(rule_key, module)
            stat["rawScenarios"].add(artifact.scenario_id)
            stat["rawTotalFindingCount"] += 1
            source = _detection_source(finding).upper()
            if source:
                stat["rawDetectionSources"].add(source)
                stat["detectionSources"].add(source)
            if "REGEX" in source and all(token not in source for token in ("HYBRID", "SEMANTIC", "AST")):
                stat["rawRegexOnlyCount"] += 1
                stat["regexOnlyCount"] += 1
            if "HYBRID" in source:
                stat["rawHybridCount"] += 1
                stat["hybridCount"] += 1
            if source == "SEMANTIC":
                stat["rawSemanticCount"] += 1
                stat["semanticCount"] += 1
            if source == "AST":
                stat["rawAstCount"] += 1
                stat["astCount"] += 1
            raw_rules.add(rule_key)

        for finding in artifact.surfaced_findings:
            rule_key = _rule_key(finding)
            if not rule_key:
                continue
            module = str(finding.get("module") or _detail(finding).get("module") or "")
            stat = ensure_stat(rule_key, module)
            stat["surfacedScenarios"].add(artifact.scenario_id)
            stat["surfacedTotalFindingCount"] += 1
            source = _detection_source(finding).upper()
            if source:
                stat["surfacedDetectionSources"].add(source)
            if "REGEX" in source and all(token not in source for token in ("HYBRID", "SEMANTIC", "AST")):
                stat["surfacedRegexOnlyCount"] += 1
            if "HYBRID" in source:
                stat["surfacedHybridCount"] += 1
            if source == "SEMANTIC":
                stat["surfacedSemanticCount"] += 1
            if source == "AST":
                stat["surfacedAstCount"] += 1
            surfaced_rules.add(rule_key)

        matched = artifact.comparison.get("matchedFindings", [])
        if isinstance(matched, list):
            for entry in matched:
                if not isinstance(entry, dict):
                    continue
                actual = _actual_from_matched(entry)
                rule_key = _rule_key(actual)
                if not rule_key:
                    continue
                stat = ensure_stat(rule_key, str(actual.get("module") or ""))
                stat["expectedMatchCount"] += 1
                stat["expectedScenarios"].add(artifact.scenario_id)
                surfaced_rules.add(rule_key)

        noisy_fields = {
            "unexpectedFindings": "unexpectedMatchCount",
            "sameSurfaceExtraFindings": "sameSurfaceExtraCount",
            "sameFileDifferentSignalFindings": "sameFileDifferentSignalCount",
            "mayFindReview": "reviewOnlyCount",
            "mustNotFindViolations": "mustNotFindViolationCount",
        }
        for field, counter_name in noisy_fields.items():
            items = artifact.comparison.get(field, [])
            if not isinstance(items, list):
                continue
            counts = _finding_counts([item for item in items if isinstance(item, dict)])
            for rule_key, count in counts.items():
                module_hint = ""
                first_item = next((item for item in items if isinstance(item, dict) and _rule_key(item) == rule_key), {})
                if isinstance(first_item, dict):
                    module_hint = str(first_item.get("module") or "")
                stat = ensure_stat(rule_key, module_hint)
                stat[counter_name] += count
                stat["noisyMatchCount"] += count
                stat["noiseScenarios"].add(artifact.scenario_id)
                surfaced_rules.add(rule_key)

        explainability_failures = artifact.comparison.get("explainabilityFailures", [])
        if isinstance(explainability_failures, list):
            for failure in explainability_failures:
                if not isinstance(failure, dict):
                    continue
                for rule_key in _rule_keys_from_explainability_failure(failure):
                    stat = ensure_stat(rule_key)
                    stat["explainabilityGapCount"] += 1
                    stat["explainabilityScenarios"].add(artifact.scenario_id)
                    surfaced_rules.add(rule_key)

        scenario_matrix["rawRules"] = sorted(raw_rules)
        scenario_matrix["surfacedRules"] = sorted(surfaced_rules)
        scenario_to_rule_matrix[artifact.scenario_id] = scenario_matrix

    for stat in stats_by_rule.values():
        stat["rawDistinctScenarioCount"] = len(stat["rawScenarios"])
        stat["surfacedDistinctScenarioCount"] = len(stat["surfacedScenarios"])
        expected = stat["expectedMatchCount"]
        noisy = stat["noisyMatchCount"] + stat["mustNotFindViolationCount"]
        explainability = stat["explainabilityGapCount"]
        raw_total = stat["rawTotalFindingCount"]
        surfaced_total = stat["surfacedTotalFindingCount"]
        stat["rawRegexOnlyOnlyExercised"] = raw_total > 0 and stat["rawRegexOnlyCount"] == raw_total and not any(
            source in {"HYBRID", "SEMANTIC", "AST"} for source in stat["rawDetectionSources"]
        )
        stat["regexOnlyOnlyExercised"] = surfaced_total > 0 and stat["surfacedRegexOnlyCount"] == surfaced_total and not any(
            source in {"HYBRID", "SEMANTIC", "AST"} for source in stat["surfacedDetectionSources"]
        )
        if explainability > 0:
            stat["bucket"] = BUCKET_EXPLAINABILITY
        elif expected > 0 and noisy > 0:
            stat["bucket"] = BUCKET_MIXED
        elif expected > 0:
            stat["bucket"] = BUCKET_EXPECTED
        elif noisy > 0:
            stat["bucket"] = BUCKET_NOISY
        elif raw_total > 0:
            stat["bucket"] = BUCKET_RAW_ONLY
        else:
            stat["bucket"] = BUCKET_NEVER

    results: dict[str, Any] = {}
    rule_to_scenario_matrix: dict[str, dict[str, Any]] = {}

    for module in ("guardian", "quantum"):
        active_map = module_maps[module]
        coverage_rows: list[dict[str, Any]] = []
        raw_exercised = 0
        surfaced_exercised = 0
        bucket_counts = defaultdict(int)
        raw_bucket_counts = defaultdict(int)
        regex_only_only_count = 0
        raw_regex_only_only_count = 0
        for rule_key, active_item in active_map.items():
            stat = stats_by_rule.get(rule_key)
            if stat is None:
                coverage_row = {
                    **active_item,
                    "rawDistinctScenarioCount": 0,
                    "surfacedDistinctScenarioCount": 0,
                    "rawTotalFindingCount": 0,
                    "surfacedTotalFindingCount": 0,
                    "expectedMatchCount": 0,
                    "unexpectedMatchCount": 0,
                    "noisyMatchCount": 0,
                    "mustNotFindViolationCount": 0,
                    "sameSurfaceExtraCount": 0,
                    "sameFileDifferentSignalCount": 0,
                    "reviewOnlyCount": 0,
                    "explainabilityGapCount": 0,
                    "rawRegexOnlyCount": 0,
                    "surfacedRegexOnlyCount": 0,
                    "rawHybridCount": 0,
                    "surfacedHybridCount": 0,
                    "rawSemanticCount": 0,
                    "surfacedSemanticCount": 0,
                    "rawAstCount": 0,
                    "surfacedAstCount": 0,
                    "regexOnlyCount": 0,
                    "hybridCount": 0,
                    "semanticCount": 0,
                    "astCount": 0,
                    "rawScenarios": [],
                    "surfacedScenarios": [],
                    "bucket": BUCKET_NEVER,
                    "regexOnlyOnlyExercised": False,
                    "rawRegexOnlyOnlyExercised": False,
                }
            else:
                if stat["rawTotalFindingCount"] > 0:
                    raw_exercised += 1
                if stat["surfacedTotalFindingCount"] > 0 or stat["expectedMatchCount"] > 0 or stat["noisyMatchCount"] > 0 or stat["mustNotFindViolationCount"] > 0 or stat["explainabilityGapCount"] > 0:
                    surfaced_exercised += 1
                bucket_counts[stat["bucket"]] += 1
                raw_bucket = stat["bucket"] if stat["rawTotalFindingCount"] > 0 else BUCKET_NEVER
                raw_bucket_counts[raw_bucket] += 1
                if stat["regexOnlyOnlyExercised"]:
                    regex_only_only_count += 1
                if stat["rawRegexOnlyOnlyExercised"]:
                    raw_regex_only_only_count += 1
                coverage_row = {
                    **{
                        key: value
                        for key, value in stat.items()
                        if key
                        not in {
                            "rawScenarios",
                            "surfacedScenarios",
                            "noiseScenarios",
                            "expectedScenarios",
                            "explainabilityScenarios",
                            "rawDetectionSources",
                            "surfacedDetectionSources",
                            "detectionSources",
                        }
                    },
                    "rawScenarios": sorted(stat["rawScenarios"]),
                    "surfacedScenarios": sorted(stat["surfacedScenarios"]),
                }
                rule_to_scenario_matrix[rule_key] = {
                    "module": module,
                    "bucket": stat["bucket"],
                    "rawScenarios": sorted(stat["rawScenarios"]),
                    "surfacedScenarios": sorted(stat["surfacedScenarios"]),
                    "expectedScenarios": sorted(stat["expectedScenarios"]),
                    "noiseScenarios": sorted(stat["noiseScenarios"]),
                    "explainabilityScenarios": sorted(stat["explainabilityScenarios"]),
                }
            coverage_rows.append(coverage_row)
        never = len([row for row in coverage_rows if row["bucket"] == BUCKET_NEVER])
        results[module] = {
            "activeRuleCount": len(active_map),
            "rawExercisedDistinctRules": raw_exercised,
            "surfacedExercisedDistinctRules": surfaced_exercised,
            "rawCoveragePercent": round((raw_exercised / len(active_map) * 100.0), 2) if active_map else 0.0,
            "surfacedCoveragePercent": round((surfaced_exercised / len(active_map) * 100.0), 2) if active_map else 0.0,
            "bucketCounts": {
                BUCKET_EXPECTED: bucket_counts[BUCKET_EXPECTED],
                BUCKET_NOISY: bucket_counts[BUCKET_NOISY],
                BUCKET_MIXED: bucket_counts[BUCKET_MIXED],
                BUCKET_EXPLAINABILITY: bucket_counts[BUCKET_EXPLAINABILITY],
                BUCKET_RAW_ONLY: bucket_counts[BUCKET_RAW_ONLY],
                BUCKET_UNCLASSIFIED: bucket_counts[BUCKET_UNCLASSIFIED],
                BUCKET_NEVER: never,
            },
            "rawBucketCounts": {
                BUCKET_EXPECTED: raw_bucket_counts[BUCKET_EXPECTED],
                BUCKET_NOISY: raw_bucket_counts[BUCKET_NOISY],
                BUCKET_MIXED: raw_bucket_counts[BUCKET_MIXED],
                BUCKET_EXPLAINABILITY: raw_bucket_counts[BUCKET_EXPLAINABILITY],
                BUCKET_RAW_ONLY: raw_bucket_counts[BUCKET_RAW_ONLY],
                BUCKET_UNCLASSIFIED: raw_bucket_counts[BUCKET_UNCLASSIFIED],
                BUCKET_NEVER: never,
            },
            "regexOnlyOnlyExercisedCount": regex_only_only_count,
            "rawRegexOnlyOnlyExercisedCount": raw_regex_only_only_count,
            "rows": coverage_rows,
        }

    noisy_hotspots = []
    for rule_key, stat in stats_by_rule.items():
        noisy_score = stat["noisyMatchCount"] + stat["mustNotFindViolationCount"] + stat["explainabilityGapCount"]
        if noisy_score <= 0:
            continue
        noisy_hotspots.append(
            {
                "rule_key": rule_key,
                "module": stat["module"],
                "bucket": stat["bucket"],
                "noisyScore": noisy_score,
                "unexpectedMatchCount": stat["unexpectedMatchCount"],
                "sameSurfaceExtraCount": stat["sameSurfaceExtraCount"],
                "sameFileDifferentSignalCount": stat["sameFileDifferentSignalCount"],
                "reviewOnlyCount": stat["reviewOnlyCount"],
                "mustNotFindViolationCount": stat["mustNotFindViolationCount"],
                "explainabilityGapCount": stat["explainabilityGapCount"],
                "regexOnlyCount": stat["surfacedRegexOnlyCount"],
                "rawDistinctScenarioCount": stat["rawDistinctScenarioCount"],
                "surfacedDistinctScenarioCount": stat["surfacedDistinctScenarioCount"],
                "rawScenarios": sorted(stat["rawScenarios"]),
                "surfacedScenarios": sorted(stat["surfacedScenarios"]),
            }
        )
    noisy_hotspots.sort(key=lambda item: (-item["noisyScore"], item["rule_key"]))

    uncovered = {
        module: [row for row in results[module]["rows"] if row["bucket"] == BUCKET_NEVER]
        for module in ("guardian", "quantum")
    }
    raw_only = {
        module: [row for row in results[module]["rows"] if row["bucket"] == BUCKET_RAW_ONLY]
        for module in ("guardian", "quantum")
    }

    return {
        "modules": results,
        "ruleToScenarioMatrix": rule_to_scenario_matrix,
        "scenarioToRuleMatrix": scenario_to_rule_matrix,
        "noisyRuleHotspots": noisy_hotspots,
        "uncoveredRules": uncovered,
        "rawOnlyRules": raw_only,
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        flat = dict(row)
        for key, value in list(flat.items()):
            if isinstance(value, list):
                flat[key] = ";".join(str(item) for item in value)
            elif isinstance(value, bool):
                flat[key] = "true" if value else "false"
        writer.writerow({field: flat.get(field, "") for field in fieldnames})
    write_text(path, buffer.getvalue())


def write_active_rule_reports(config, active_rules: dict[str, Any]) -> None:
    root = ensure_dir(config.reports_root)
    for module in ("guardian", "quantum"):
        rows = active_rules[module]
        write_json(root / f"{module}-active-rules.json", rows)
        _write_csv(
            root / f"{module}-active-rules.csv",
            rows,
            ["rule_key", "module", "family", "language", "title", "severity", "finding_kind", "source_of_truth", "pack_display_name", "bootstrap_resource", "active"],
        )
        lines = [
            f"# {module.title()} Active Rules",
            "",
            f"- Exact active count: `{len(rows)}`",
            f"- Source of truth: `{active_rules['sourceOfTruth']['kind']}` via `{active_rules['sourceOfTruth']['container']}` / `{active_rules['sourceOfTruth']['database']}`",
            "",
            "| Rule Key | Severity | Kind | Language | Family | Title |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for row in rows:
            lines.append(
                f"| `{row['rule_key']}` | `{row['severity']}` | `{row['finding_kind']}` | `{row['language'] or 'n/a'}` | `{row['family'] or 'n/a'}` | {row['title']} |"
            )
        write_text(root / f"{module}-active-rules.md", "\n".join(lines).rstrip() + "\n")


def write_coverage_reports(config, coverage: dict[str, Any]) -> None:
    root = ensure_dir(config.reports_root)
    for module in ("guardian", "quantum"):
        module_payload = coverage["modules"][module]
        rows = module_payload["rows"]
        raw_payload = {
            "activeRuleCount": module_payload["activeRuleCount"],
            "exercisedDistinctRules": module_payload["rawExercisedDistinctRules"],
            "coveragePercent": module_payload["rawCoveragePercent"],
            "bucketCounts": module_payload["rawBucketCounts"],
            "regexOnlyOnlyExercisedCount": module_payload["rawRegexOnlyOnlyExercisedCount"],
            "rows": rows,
        }
        surfaced_payload = {
            "activeRuleCount": module_payload["activeRuleCount"],
            "exercisedDistinctRules": module_payload["surfacedExercisedDistinctRules"],
            "coveragePercent": module_payload["surfacedCoveragePercent"],
            "bucketCounts": module_payload["bucketCounts"],
            "regexOnlyOnlyExercisedCount": module_payload["regexOnlyOnlyExercisedCount"],
            "rows": rows,
        }
        write_json(root / f"{module}-rule-coverage-raw.json", raw_payload)
        write_json(root / f"{module}-rule-coverage-surfaced.json", surfaced_payload)
        write_json(root / f"{module}-rule-coverage.json", {"raw": raw_payload, "surfaced": surfaced_payload})
        _write_csv(
            root / f"{module}-rule-coverage.csv",
            rows,
            [
                "rule_key",
                "module",
                "bucket",
                "rawDistinctScenarioCount",
                "surfacedDistinctScenarioCount",
                "rawTotalFindingCount",
                "surfacedTotalFindingCount",
                "expectedMatchCount",
                "unexpectedMatchCount",
                "noisyMatchCount",
                "mustNotFindViolationCount",
                "sameSurfaceExtraCount",
                "sameFileDifferentSignalCount",
                "reviewOnlyCount",
                "explainabilityGapCount",
                "rawRegexOnlyCount",
                "surfacedRegexOnlyCount",
                "rawHybridCount",
                "surfacedHybridCount",
                "rawSemanticCount",
                "surfacedSemanticCount",
                "rawAstCount",
                "surfacedAstCount",
                "regexOnlyCount",
                "hybridCount",
                "semanticCount",
                "astCount",
                "rawRegexOnlyOnlyExercised",
                "regexOnlyOnlyExercised",
                "rawScenarios",
                "surfacedScenarios",
                "title",
                "severity",
                "finding_kind",
                "family",
                "language",
            ],
        )
        bucket_counts = module_payload["bucketCounts"]
        raw_bucket_counts = module_payload["rawBucketCounts"]
        lines = [
            f"# {module.title()} Rule Coverage",
            "",
            f"- Active rules: `{module_payload['activeRuleCount']}`",
            f"- Raw exercised distinct rules: `{module_payload['rawExercisedDistinctRules']}` / `{module_payload['activeRuleCount']}` (`{module_payload['rawCoveragePercent']}%`)",
            f"- Surfaced exercised distinct rules: `{module_payload['surfacedExercisedDistinctRules']}` / `{module_payload['activeRuleCount']}` (`{module_payload['surfacedCoveragePercent']}%`)",
            f"- raw_only_not_surfaced: `{bucket_counts[BUCKET_RAW_ONLY]}`",
            f"- surfaced expected_positive_exercised: `{bucket_counts[BUCKET_EXPECTED]}`",
            f"- surfaced noisy_only_exercised: `{bucket_counts[BUCKET_NOISY]}`",
            f"- surfaced mixed_exercised: `{bucket_counts[BUCKET_MIXED]}`",
            f"- surfaced explainability_problematic_exercised: `{bucket_counts[BUCKET_EXPLAINABILITY]}`",
            f"- surfaced regex_only_only_exercised: `{module_payload['regexOnlyOnlyExercisedCount']}`",
            f"- raw regex_only_only_exercised: `{module_payload['rawRegexOnlyOnlyExercisedCount']}`",
            f"- never_exercised: `{bucket_counts[BUCKET_NEVER]}`",
            "",
            "| Rule Key | Bucket | Raw Scenarios | Surfaced Scenarios | Expected | Noise | Explainability | Raw Count | Surfaced Count |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if row["bucket"] == BUCKET_NEVER:
                continue
            lines.append(
                f"| `{row['rule_key']}` | `{row['bucket']}` | `{row['rawDistinctScenarioCount']}` | `{row['surfacedDistinctScenarioCount']}` | `{row['expectedMatchCount']}` | `{row['noisyMatchCount']}` | `{row['explainabilityGapCount']}` | `{row['rawTotalFindingCount']}` | `{row['surfacedTotalFindingCount']}` |"
            )
        write_text(root / f"{module}-rule-coverage.md", "\n".join(lines).rstrip() + "\n")

    write_json(root / "rule-to-scenario-matrix.json", coverage["ruleToScenarioMatrix"])
    write_json(root / "scenario-to-rule-matrix.json", coverage["scenarioToRuleMatrix"])
    write_json(root / "noisy-rule-hotspots.json", coverage["noisyRuleHotspots"])

    uncovered_lines = ["# Uncovered Rules Summary", ""]
    for module in ("guardian", "quantum"):
        uncovered = coverage["uncoveredRules"][module]
        raw_only = coverage["rawOnlyRules"][module]
        uncovered_lines.append(f"## {module.title()}")
        uncovered_lines.append("")
        uncovered_lines.append(f"- Never exercised: `{len(uncovered)}`")
        uncovered_lines.append(f"- Raw only not surfaced: `{len(raw_only)}`")
        top_families = defaultdict(int)
        for row in uncovered:
            top_families[row.get("family") or "unknown"] += 1
        uncovered_lines.append("- Top uncovered families:")
        for family, count in sorted(top_families.items(), key=lambda item: (-item[1], item[0]))[:15]:
            uncovered_lines.append(f"  - `{family}`: `{count}`")
        raw_only_families = defaultdict(int)
        for row in raw_only:
            raw_only_families[row.get("family") or "unknown"] += 1
        uncovered_lines.append("- Top raw-only-not-surfaced families:")
        for family, count in sorted(raw_only_families.items(), key=lambda item: (-item[1], item[0]))[:15]:
            uncovered_lines.append(f"  - `{family}`: `{count}`")
        uncovered_lines.append("")
    write_text(root / "uncovered-rules-summary.md", "\n".join(uncovered_lines).rstrip() + "\n")

    scorecard_lines = ["# Rule Coverage Scorecard", ""]
    for module in ("guardian", "quantum"):
        payload = coverage["modules"][module]
        buckets = payload["bucketCounts"]
        scorecard_lines.extend(
            [
                f"## {module.title()}",
                "",
                f"- raw exercised distinct rules: `{payload['rawExercisedDistinctRules']}` / `{payload['activeRuleCount']}` (`{payload['rawCoveragePercent']}%`)",
                f"- surfaced exercised distinct rules: `{payload['surfacedExercisedDistinctRules']}` / `{payload['activeRuleCount']}` (`{payload['surfacedCoveragePercent']}%`)",
                f"- expected_positive_exercised: `{buckets[BUCKET_EXPECTED]}`",
                f"- noisy_only_exercised: `{buckets[BUCKET_NOISY]}`",
                f"- mixed_exercised: `{buckets[BUCKET_MIXED]}`",
                f"- explainability_problematic_exercised: `{buckets[BUCKET_EXPLAINABILITY]}`",
                f"- raw_only_not_surfaced: `{buckets[BUCKET_RAW_ONLY]}`",
                f"- regex_only_only_exercised: `{payload['regexOnlyOnlyExercisedCount']}`",
                f"- never_exercised: `{buckets[BUCKET_NEVER]}`",
                "",
            ]
        )
    scorecard_lines.extend(
        [
            "## Top Noisy Rule Hotspots",
            "",
            "| Rule Key | Module | Bucket | Noisy Score | Distinct Scenarios |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    for row in coverage["noisyRuleHotspots"][:20]:
        scorecard_lines.append(
            f"| `{row['rule_key']}` | `{row['module']}` | `{row['bucket']}` | `{row['noisyScore']}` | `{row['surfacedDistinctScenarioCount']}` |"
        )
    write_text(root / "rule-coverage-scorecard.md", "\n".join(scorecard_lines).rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate exact active rule inventory and same-run rule coverage maps.")
    parser.add_argument("--inventory-only", action="store_true", help="Only emit active rule inventory artefacts.")
    args = parser.parse_args()

    config = load_config()
    cwd = config.lab_root.parents[1] / "ARQV2"
    active_rules = load_active_rules(config, cwd=cwd)
    write_active_rule_reports(config, active_rules)
    if not args.inventory_only:
        artifacts = load_latest_scenario_artifacts(config.runs_root)
        coverage = classify_rule_coverage(active_rules, artifacts)
        write_coverage_reports(config, coverage)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
