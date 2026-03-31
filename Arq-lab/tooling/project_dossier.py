from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .models import BuildStatus, LabConfig, ScenarioSpec
from .utils import ensure_dir, run_command, write_json, write_text

SKIP_DIR_NAMES = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    "bin",
    "node_modules",
    "obj",
    "target",
    ".venv",
}

SKIP_FILE_SUFFIXES = {".pyc", ".pyo"}

PROTECTED_PREFIXES = (
    "docs/",
    "examples/",
    "vendor/",
    "generated/",
    "dist/",
    "build/",
    "src/test/",
    "tests/",
    "__tests__/",
    "fixtures/",
    "mocks/",
)

SUSPICIOUS_MARKERS = [
    "private key",
    "begin rsa private key",
    "verify=false",
    "rejectunauthorized",
    "accept_untrusted",
    "node_tls_reject_unauthorized",
    "md5",
    "sha1",
    "aes/ecb",
    "desede",
    "dangerousacceptanyservercertificatevalidator",
    "ssl._create_unverified_context",
    "secret",
    "token",
    "example",
    "mask",
    "vault://",
]


def _normalize_path(value: str | Path) -> str:
    normalized = str(value).replace("\\", "/").strip()
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _path_segments(value: str | Path) -> list[str]:
    normalized = _normalize_path(value)
    return [segment.lower() for segment in normalized.split("/") if segment and segment != "."]


def _path_matches(expected_path: str | None, actual_path: str | Path) -> bool:
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


def _repo_type(scenario: ScenarioSpec) -> str:
    has_history = any(plan.scan_mode == "REF_HISTORY" for plan in scenario.scan_plans)
    has_all_branches = any(plan.branch_scope == "ALL_BRANCHES" for plan in scenario.scan_plans)
    if scenario.family.startswith("mixed_") or has_all_branches:
        return "mixed"
    if has_history:
        return "history"
    return "snapshot"


def _target_module_label(value: str) -> str:
    return {"guardian": "Guardian", "quantum": "Quantum", "both": "Both"}.get(value, value.title())


def _module_for_expected(expected: Any, scenario: ScenarioSpec) -> str:
    text = f"{getattr(expected, 'key', '')} {getattr(expected, 'rule_key_contains', '')}".lower()
    if "guardian" in text:
        return "Guardian"
    if "quantum" in text:
        return "Quantum"
    if scenario.module == "both":
        if getattr(expected, "resolved_value_contains", None):
            return "Quantum"
        return "Guardian"
    return _target_module_label(scenario.module)


def _iter_repo_files(repo_root: Path) -> list[Path]:
    collected: list[Path] = []
    for candidate in sorted(repo_root.rglob("*")):
        if not candidate.is_file():
            continue
        relative = candidate.relative_to(repo_root)
        if any(part in SKIP_DIR_NAMES for part in relative.parts):
            continue
        if candidate.suffix.lower() in SKIP_FILE_SUFFIXES:
            continue
        collected.append(candidate)
    return collected


def _read_text(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return file_path.read_text(encoding="utf-8", errors="replace")


def _loc(file_path: Path) -> int:
    content = _read_text(file_path)
    if not content:
        return 0
    return len(content.splitlines())


def _is_code_path(relative_path: str) -> bool:
    return Path(relative_path).suffix.lower() in {".py", ".ts", ".js", ".java", ".cs", ".go", ".kt"}


def _classify_file(relative_path: str) -> str:
    lower = relative_path.lower()
    suffix = Path(relative_path).suffix.lower()
    if lower.startswith("validation/"):
        return "generated"
    if lower.startswith("vendor/"):
        return "vendor"
    if lower.startswith("generated/") or lower.startswith("dist/"):
        return "generated"
    if lower.startswith(("tests/", "__tests__/", "src/test/")):
        return "test"
    if lower.startswith(("fixtures/", "mocks/")):
        return "fixture"
    if lower.startswith("scripts/"):
        return "script"
    if lower.startswith(("docs/", "examples/")) or relative_path == "README.md":
        return "docs"
    if lower.startswith(("config/", "runtime/", "deploy/", "helm/", "terraform/")):
        if "example" in lower or "/examples/" in lower:
            return "build/deploy"
        return "live-config"
    if lower.endswith((".env", ".properties", ".yml", ".yaml", ".json", ".toml", ".ini")):
        if any(marker in lower for marker in ("package-lock.json", "tsconfig.json", "jest.config", "pyproject.toml", "pom.xml", ".csproj", "go.mod")):
            return "build/deploy"
        if "config" in lower or "runtime" in lower or "resource" in lower or "deploy" in lower:
            return "live-config"
    if suffix in {".md", ".txt"}:
        return "docs"
    if relative_path in {".gitignore", "pom.xml", "package.json", "pyproject.toml", "go.mod", "go.sum", "jest.config.cjs", "tsconfig.json"}:
        return "build/deploy"
    if suffix in {".csproj", ".sln"}:
        return "build/deploy"
    if _is_code_path(relative_path):
        return "live-code"
    return "generated"


def _is_protected_negative(relative_path: str, classification: str) -> bool:
    normalized = _normalize_path(relative_path)
    if normalized.startswith(PROTECTED_PREFIXES):
        return True
    if classification in {"vendor", "generated"}:
        return True
    if classification == "docs" and normalized.startswith("docs/"):
        return True
    return False


def _is_synthetic_filler(relative_path: str) -> bool:
    normalized = _normalize_path(relative_path)
    return (
        normalized.startswith("docs/architecture/section-")
        or normalized.startswith("ops/playbooks/runbook-")
        or normalized.startswith("sql/reference/reference-")
    )


def _matched_expected_paths(scenario: ScenarioSpec, relative_path: str) -> list[Any]:
    return [expected for expected in scenario.expected_findings if _path_matches(expected.path_contains, relative_path)]


def _matched_absent_paths(scenario: ScenarioSpec, relative_path: str) -> list[Any]:
    return [expected for expected in scenario.expected_absent if _path_matches(expected.path_contains, relative_path)]


def _review_paths(comparison: dict[str, Any]) -> set[str]:
    paths: set[str] = set()
    for collection_name in (
        "mayFindReview",
        "extraFindings",
        "unexpectedFindings",
        "sameSurfaceExtraFindings",
        "sameFileDifferentSignalFindings",
        "unexpectedRegexOnlyFindings",
    ):
        for item in comparison.get(collection_name, []):
            path = item.get("primaryFilePath")
            if path:
                paths.add(_normalize_path(path))
    for item in comparison.get("mustNotFindViolations", []):
        actual = item.get("actual", {})
        path = actual.get("primaryFilePath")
        if path:
            paths.add(_normalize_path(path))
    return paths


def _finding_expectation(relative_path: str, scenario: ScenarioSpec, comparison: dict[str, Any]) -> str:
    if _matched_expected_paths(scenario, relative_path):
        return "must_find"
    if _matched_absent_paths(scenario, relative_path):
        return "must_not_find"
    if _normalize_path(relative_path) in _review_paths(comparison):
        return "may_find_review"
    return "none"


def _safe_inline(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def _title_from_stem(relative_path: str) -> str:
    stem = Path(relative_path).stem
    stem = re.sub(r"[_\\-]+", " ", stem)
    stem = re.sub(r"([a-z])([A-Z])", r"\1 \2", stem)
    return stem.strip().title() or Path(relative_path).name


def _file_purpose(relative_path: str, classification: str) -> str:
    title = _title_from_stem(relative_path)
    normalized = _normalize_path(relative_path)
    if normalized == "README.md":
        return "Repository overview, local development guidance, and reviewer context."
    if normalized.startswith("validation/"):
        return "Machine-readable validation contract or generated audit artifact for this scenario."
    if normalized.startswith("docs/architecture/section-"):
        return "Synthetic architecture filler used to reach line-density targets without altering runtime behavior."
    if normalized.startswith("ops/playbooks/runbook-"):
        return "Synthetic operational runbook filler used to simulate enterprise documentation density."
    if normalized.startswith("sql/reference/reference-"):
        return "Synthetic SQL reference filler used to simulate reference data and schema collateral."
    if classification == "live-code":
        lower_name = Path(relative_path).name.lower()
        if "controller" in lower_name:
            return f"Runtime HTTP/controller surface for {title}."
        if "service" in lower_name:
            return f"Runtime business service implementing {title} logic."
        if "repository" in lower_name:
            return f"Persistence or data-access helper for {title}."
        if "client" in lower_name:
            return f"Outbound integration client for {title} behavior."
        if "application" in lower_name or lower_name == "main.py":
            return "Runtime process bootstrap and application entrypoint."
        return f"Runtime business module contributing to {title}."
    if classification == "live-config":
        return f"Runtime configuration carrying environment or deployment settings for {title}."
    if classification == "test":
        return f"Automated test surface covering {title} behavior."
    if classification == "docs":
        return f"Documentation or explanatory material for {title}."
    if classification == "fixture":
        return f"Non-production fixture or mock data used to exercise {title} paths."
    if classification == "vendor":
        return f"Vendored or copied artifact used to simulate third-party noise around {title}."
    if classification == "script":
        return f"Executable helper script used for build, smoke, or repository validation around {title}."
    if classification == "build/deploy":
        return f"Build or deployment definition shaping how {title} is compiled, packaged, or released."
    return f"Generated or derived project artifact related to {title}."


def _looks_like_path(value: str) -> bool:
    normalized = _normalize_path(value)
    return "/" in normalized or normalized.endswith((".py", ".ts", ".js", ".java", ".cs", ".go", ".md", ".json", ".yml", ".yaml", ".toml", ".ps1", ".cjs", ".csproj"))


def _command_targets(command: list[str]) -> tuple[bool, list[str]]:
    if not command:
        return False, []
    executable = Path(command[0]).name.lower()
    whole_repo = False
    targets: list[str] = []

    def add_target(value: str) -> None:
        normalized = _normalize_path(value)
        if normalized:
            targets.append(normalized)

    if executable.startswith("mvn"):
        if "-f" in command:
            index = command.index("-f")
            if index + 1 < len(command):
                add_target(str(Path(command[index + 1]).parent))
        else:
            whole_repo = True
    elif executable.startswith("dotnet"):
        csproj_paths = [arg for arg in command if arg.endswith(".csproj")]
        if csproj_paths:
            for item in csproj_paths:
                add_target(str(Path(item).parent))
        else:
            whole_repo = True
    elif executable.startswith("go"):
        if "./..." in command:
            whole_repo = True
        for arg in command[1:]:
            if _looks_like_path(arg):
                add_target(arg)
    elif executable.startswith("python"):
        if "compileall" in command:
            index = command.index("compileall")
            for item in command[index + 1 :]:
                if not item.startswith("-"):
                    add_target(item)
        elif "pytest" in command:
            index = command.index("pytest")
            path_args = [item for item in command[index + 1 :] if not item.startswith("-")]
            if path_args:
                for item in path_args:
                    add_target(item)
            else:
                whole_repo = True
        else:
            for item in command[1:]:
                if _looks_like_path(item):
                    add_target(item)
    elif executable.startswith("node"):
        if len(command) > 1 and _looks_like_path(command[1]):
            add_target(command[1])
    elif executable.startswith("npm"):
        whole_repo = True
    elif executable.startswith("powershell"):
        if "-File" in command:
            index = command.index("-File")
            if index + 1 < len(command):
                add_target(command[index + 1])
        if "-Command" in command:
            index = command.index("-Command")
            if index + 1 < len(command):
                command_text = command[index + 1]
                for match in re.finditer(r"Set-Location\s+'([^']+)'", command_text, flags=re.IGNORECASE):
                    add_target(match.group(1))
                for match in re.finditer(r"-File\s+([^\s;]+)", command_text, flags=re.IGNORECASE):
                    add_target(match.group(1))
    else:
        for item in command[1:]:
            if _looks_like_path(item):
                add_target(item)

    return whole_repo, targets


def _participates(relative_path: str, classification: str, commands: list[dict[str, Any]], stage: str) -> bool:
    normalized = _normalize_path(relative_path)
    stage_targets: list[str] = []
    whole_repo = False
    for record in commands:
        current_whole_repo, current_targets = _command_targets(record.get("command", []))
        whole_repo = whole_repo or current_whole_repo
        stage_targets.extend(current_targets)
    for target in stage_targets:
        if _path_matches(target, normalized):
            return True
    if stage == "build":
        if whole_repo:
            return classification in {"live-code", "live-config", "build/deploy", "script"} or normalized.startswith("dist/")
        return classification in {"live-code", "live-config", "build/deploy", "script"} and not normalized.startswith("docs/")
    if stage == "test":
        if whole_repo:
            return classification in {"live-code", "live-config", "test", "fixture", "script", "build/deploy"}
        return classification in {"test", "fixture"}
    if stage == "smoke":
        if "smoke" in normalized.lower():
            return True
        return normalized in {"app/main.py"} or normalized.endswith("Application.java")
    return False


def _collect_file_rows(
    repo_root: Path,
    scenario: ScenarioSpec,
    build_status: BuildStatus,
    test_status: BuildStatus,
    smoke_status: BuildStatus,
    comparison: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    review_paths = _review_paths(comparison)
    for file_path in _iter_repo_files(repo_root):
        relative_path = _normalize_path(file_path.relative_to(repo_root))
        classification = _classify_file(relative_path)
        positive_surface = bool(_matched_expected_paths(scenario, relative_path))
        matched_absent = _matched_absent_paths(scenario, relative_path)
        protected_negative = _is_protected_negative(relative_path, classification)
        near_real_negative = bool(matched_absent) and not protected_negative
        finding_expectation = _finding_expectation(relative_path, scenario, comparison)
        if not near_real_negative and _normalize_path(relative_path) in review_paths and not protected_negative:
            near_real_negative = True
        row = {
            "path": relative_path,
            "classification": classification,
            "loc": _loc(file_path),
            "purpose": _file_purpose(relative_path, classification),
            "positiveSurface": positive_surface,
            "nearRealNegative": near_real_negative,
            "protectedNegative": protected_negative,
            "participatesInBuild": _participates(relative_path, classification, build_status.commands, "build"),
            "participatesInTest": _participates(relative_path, classification, test_status.commands, "test"),
            "participatesInSmoke": _participates(relative_path, classification, smoke_status.commands, "smoke"),
            "findingExpectation": finding_expectation,
            "syntheticFiller": _is_synthetic_filler(relative_path),
        }
        rows.append(row)
    rows.sort(key=lambda item: item["path"])
    return rows


def _tree_lines(repo_root: Path) -> list[str]:
    lines = [repo_root.name]
    all_paths = sorted(
        [
            candidate
            for candidate in repo_root.rglob("*")
            if not any(part in SKIP_DIR_NAMES for part in candidate.relative_to(repo_root).parts)
            and candidate.suffix.lower() not in SKIP_FILE_SUFFIXES
        ],
        key=lambda item: (_normalize_path(item.relative_to(repo_root)).count("/"), _normalize_path(item.relative_to(repo_root))),
    )
    children: dict[Path, list[Path]] = {}
    for candidate in all_paths:
        parent = candidate.parent
        children.setdefault(parent, []).append(candidate)

    def visit(directory: Path, prefix: str = "") -> None:
        entries = sorted(children.get(directory, []), key=lambda item: (not item.is_dir(), item.name.lower()))
        for index, entry in enumerate(entries):
            connector = "`-- " if index == len(entries) - 1 else "|-- "
            lines.append(f"{prefix}{connector}{entry.name}")
            if entry.is_dir():
                child_prefix = f"{prefix}{'    ' if index == len(entries) - 1 else '|   '}"
                visit(entry, child_prefix)

    visit(repo_root)
    return lines


def _matching_paths(rows: list[dict[str, Any]], path_contains: str) -> list[str]:
    return [row["path"] for row in rows if _path_matches(path_contains, row["path"])]


def _loc_composition(rows: list[dict[str, Any]]) -> dict[str, int]:
    buckets = {
        "live business code": 0,
        "live config": 0,
        "tests": 0,
        "docs": 0,
        "scripts": 0,
        "fixtures": 0,
        "vendor/generated": 0,
        "synthetic filler / inflation content": 0,
    }
    for row in rows:
        loc = int(row["loc"])
        if row["syntheticFiller"]:
            buckets["synthetic filler / inflation content"] += loc
            continue
        classification = row["classification"]
        if classification == "live-code":
            buckets["live business code"] += loc
        elif classification == "live-config":
            buckets["live config"] += loc
        elif classification == "test":
            buckets["tests"] += loc
        elif classification == "docs":
            buckets["docs"] += loc
        elif classification == "script":
            buckets["scripts"] += loc
        elif classification == "fixture":
            buckets["fixtures"] += loc
        elif classification in {"vendor", "generated"}:
            buckets["vendor/generated"] += loc
    buckets["total"] = sum(int(row["loc"]) for row in rows)
    return buckets


def _realism_assessment(scenario: ScenarioSpec, composition: dict[str, int], runnability: dict[str, str]) -> tuple[int, str]:
    score = 1
    reasons: list[str] = []
    if composition["live business code"] >= 250:
        score += 1
        reasons.append("contains a non-trivial amount of live business code")
    if composition["tests"] >= 80:
        score += 1
        reasons.append("includes meaningful automated test surfaces")
    if runnability.get("build") == "passed" and runnability.get("test") == "passed" and runnability.get("smoke") == "passed":
        score += 1
        reasons.append("build/test/smoke contracts execute successfully")
    if _repo_type(scenario) == "mixed" or any(token in scenario.stack.lower() for token in ("monorepo", "java + node + python", "app + infra")):
        score += 1
        reasons.append("models a multi-component or multi-branch enterprise layout")
    filler_ratio = 0.0
    total = composition.get("total", 0)
    if total:
        filler_ratio = composition["synthetic filler / inflation content"] / total
    if filler_ratio > 0.45 and score > 1:
        score -= 1
        reasons.append("synthetic filler is materially visible and pulls realism down")
    if scenario.family.startswith("negative_") and score > 4:
        score = 4
    score = max(1, min(5, score))
    if not reasons:
        reasons.append("repository is small or heavily synthetic relative to its scenario goal")
    return score, "; ".join(reasons)


def _finding_behavior(expected: Any) -> str:
    if getattr(expected, "exposure_scope", None):
        return str(expected.exposure_scope)
    present_on_head = getattr(expected, "present_on_head", None)
    present_in_history = getattr(expected, "present_in_history", None)
    if present_on_head is False and present_in_history:
        return "history-only"
    if present_on_head and present_in_history:
        return "head+history"
    return "head-only"


def _explainability_note(expected: Any, scenario: ScenarioSpec) -> str:
    matching = [item for item in scenario.explainability_expectations if _path_matches(item.path_contains, expected.path_contains)]
    if not matching:
        return "No strict scenario-specific explainability contract beyond normal detail capture."
    parts = []
    for item in matching:
        fields = []
        if item.resolved_value_contains:
            fields.append(f"resolvedValue~{item.resolved_value_contains}")
        if item.query_family_contains:
            fields.append(f"queryFamily~{item.query_family_contains}")
        if item.resolution_scope_contains:
            fields.append(f"resolutionScope~{item.resolution_scope_contains}")
        if item.detection_source_contains:
            fields.append(f"detectionSource~{item.detection_source_contains}")
        if fields:
            parts.append(", ".join(fields))
    return "; ".join(parts) if parts else "Explainability checked on the matching path."


def _negative_reason(row: dict[str, Any]) -> str:
    if row["protectedNegative"]:
        return "Path lives in a protected negative zone and should stay clean even if the content looks suspicious."
    return "Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live."


def _top_level_components(rows: list[dict[str, Any]]) -> list[str]:
    components = sorted({row["path"].split("/", 1)[0] for row in rows if "/" in row["path"]})
    return components[:20]


def _config_paths(rows: list[dict[str, Any]]) -> list[str]:
    return [row["path"] for row in rows if row["classification"] == "live-config"][:12]


def _test_paths(rows: list[dict[str, Any]]) -> list[str]:
    return [row["path"] for row in rows if row["classification"] == "test"][:12]


def _docs_noise_paths(rows: list[dict[str, Any]]) -> list[str]:
    return [row["path"] for row in rows if row["classification"] in {"docs", "vendor", "generated"}][:12]


def _critical_paths(rows: list[dict[str, Any]], scenario: ScenarioSpec, comparison: dict[str, Any]) -> list[str]:
    selected: set[str] = set()
    for expected in scenario.expected_findings:
        selected.update(_matching_paths(rows, expected.path_contains))
    for expected in scenario.expected_absent:
        selected.update(_matching_paths(rows, expected.path_contains))
    for collection_name in (
        "mayFindReview",
        "extraFindings",
        "unexpectedFindings",
        "sameSurfaceExtraFindings",
        "sameFileDifferentSignalFindings",
        "unexpectedRegexOnlyFindings",
    ):
        for item in comparison.get(collection_name, []):
            path = item.get("primaryFilePath")
            if path:
                selected.add(_normalize_path(path))
    for item in comparison.get("mustNotFindViolations", []):
        actual = item.get("actual", {})
        path = actual.get("primaryFilePath")
        if path:
            selected.add(_normalize_path(path))
    for row in rows:
        if row["path"] in {"README.md", "pom.xml", "package.json", "pyproject.toml", "go.mod"}:
            selected.add(row["path"])
        if row["path"].endswith(("Application.java", "main.py", "smoke.ps1", "smoke.py", "smoke.js")):
            selected.add(row["path"])
    return sorted(path for path in selected if any(row["path"] == path for row in rows))


def _markers_for_path(path: str, scenario: ScenarioSpec, comparison: dict[str, Any]) -> list[str]:
    markers: list[str] = []
    for expected in scenario.expected_findings:
        if _path_matches(expected.path_contains, path):
            if expected.resolved_value_contains:
                markers.append(expected.resolved_value_contains)
            if expected.rule_key_contains:
                markers.append(expected.rule_key_contains)
            markers.append(expected.key)
    for expected in scenario.expected_absent:
        if _path_matches(expected.path_contains, path):
            markers.append(expected.key)
    for collection_name in ("mayFindReview", "extraFindings", "unexpectedRegexOnlyFindings"):
        for item in comparison.get(collection_name, []):
            if _path_matches(path, item.get("primaryFilePath", "")):
                for field_name in ("ruleKey", "ruleName", "resolvedValue"):
                    value = item.get(field_name)
                    if value:
                        markers.append(str(value))
    markers.extend(SUSPICIOUS_MARKERS)
    deduped: list[str] = []
    seen: set[str] = set()
    for marker in markers:
        lowered = marker.lower()
        if lowered not in seen:
            seen.add(lowered)
            deduped.append(marker)
    return deduped


def _representative_excerpt(file_path: Path, markers: list[str]) -> str:
    lines = _read_text(file_path).splitlines()
    if not lines:
        return "(empty file)"
    picked: list[int] = []
    lowered_markers = [marker.lower() for marker in markers if marker]
    for index, line in enumerate(lines, start=1):
        lower_line = line.lower()
        if any(marker in lower_line for marker in lowered_markers):
            start = max(1, index - 1)
            end = min(len(lines), index + 1)
            for candidate in range(start, end + 1):
                if candidate not in picked:
                    picked.append(candidate)
    if not picked:
        picked = list(range(1, min(len(lines), 12) + 1))
    excerpt_lines = []
    for index in picked[:24]:
        excerpt_lines.append(f"{index:04d}: {lines[index - 1]}")
    return "\n".join(excerpt_lines)


def _build_context_table(build_status: BuildStatus, stage: str) -> list[str]:
    lines = [f"### {stage.title()}", ""]
    if not build_status.commands:
        lines.append("- No commands declared.")
        lines.append("")
        return lines
    for record in build_status.commands:
        command_string = " ".join(record.get("command", []))
        lines.append(f"- Command: `{command_string}`")
        lines.append(f"  Expected result: `{stage}` step completes successfully.")
        lines.append(f"  Actual result: returncode=`{record.get('returncode')}`; stage state=`{build_status.state}`")
        lines.append(f"  Log file: `{record.get('logPath', 'n/a')}`")
    lines.append("")
    return lines


def _history_section(repo_root: Path, scenario: ScenarioSpec, repo_metadata: dict[str, Any]) -> list[str]:
    repo_type = _repo_type(scenario)
    if repo_type == "snapshot":
        return [
            "Snapshot-only scenario. No branch divergence or history-only contract is intended beyond the default branch head scan.",
            "",
        ]
    lines = ["Branches:", ""]
    branches = repo_metadata.get("git", {}).get("branches", {})
    for branch_name, sha in sorted(branches.items()):
        if branch_name == "main":
            lines.append(f"- `{branch_name}` tip: `{sha}`")
            continue
        merge_base = run_command(["git", "merge-base", "main", branch_name], repo_root, check=False)
        base_sha = merge_base.stdout.strip() if merge_base.returncode == 0 else "unknown"
        lines.append(f"- `{branch_name}` tip: `{sha}`; diverges from `main` at `{base_sha}`")
    lines.extend(["", "Commit order:", ""])
    timeline = list(reversed(repo_metadata.get("git", {}).get("timeline", [])))
    for commit in timeline:
        message = commit.get("message", "")
        purpose = "scenario state change"
        lower_message = message.lower()
        if "bootstrap" in lower_message:
            purpose = "initial clean or baseline assembly"
        elif "add" in lower_message or "temporary" in lower_message:
            purpose = "introduces an intended signal"
        elif "remove" in lower_message or "clean" in lower_message:
            purpose = "removes or neutralizes a prior signal"
        elif "rotate" in lower_message:
            purpose = "replaces one signal with another"
        elif "docs" in lower_message:
            purpose = "adds documentation-only or noise-only collateral"
        lines.append(f"- `{commit.get('sha')}` `{message}`: {purpose}.")
    lines.extend(["", "Expected final head/history state:", ""])
    for expected in scenario.expected_findings:
        lines.append(f"- `{expected.key}` on `{expected.path_contains}` should behave as `{_finding_behavior(expected)}`.")
    lines.append("")
    return lines


def _explainability_section(scenario: ScenarioSpec) -> list[str]:
    if scenario.module not in {"quantum", "both"}:
        return ["Guardian-only scenario. Quantum explainability contract is not applicable here.", ""]
    lines = [
        "- `detectionSource`: scenario checks it only when explicitly declared; regex-only live exports are tolerated unless the scenario contract says otherwise.",
        "- `semanticKey`: informative but not currently a strict blocker unless a scenario-specific follow-up adds it.",
        "- `resolvedValue`: strict on files that have an explainability contract entry.",
        "- `resolutionScope`: strict only when declared by the scenario explainability contract.",
        "- `queryFamily`: strict only when declared by the scenario explainability contract.",
        "- `rawEvidenceJson`: not a mandatory contract field in the current scenario pack unless added explicitly later.",
        "",
        "Scenario-specific explainability expectations:",
        "",
    ]
    if not scenario.explainability_expectations:
        lines.append("- No strict scenario-specific explainability expectations were declared.")
    for expected in scenario.explainability_expectations:
        checks = []
        if expected.resolved_value_contains:
            checks.append(f"resolvedValue~`{expected.resolved_value_contains}`")
        if expected.query_family_contains:
            checks.append(f"queryFamily~`{expected.query_family_contains}`")
        if expected.resolution_scope_contains:
            checks.append(f"resolutionScope~`{expected.resolution_scope_contains}`")
        if expected.detection_source_contains:
            checks.append(f"detectionSource~`{expected.detection_source_contains}`")
        check_text = ", ".join(checks) if checks else "path presence only"
        lines.append(f"- `{expected.path_contains}`: {check_text}")
    lines.extend(
        [
            "",
            "Explainability failure definition:",
            "",
            "- A finding exists on the expected path, but the declared explainability fields are missing or do not match the scenario contract.",
            "",
        ]
    )
    return lines


def _risk_notes(scenario: ScenarioSpec, comparison: dict[str, Any]) -> list[str]:
    lines = []
    if scenario.family == "negative_tests":
        lines.append("- False positives are most likely on mock PEM or fixture files that contain inventory-looking text but are not live code.")
    elif scenario.family in {"quantum_tls_config", "mixed_infra_repo"}:
        lines.append("- False negatives are most likely on runtime config files where the detector must bind a weak TLS knob out of YAML or env syntax.")
    elif scenario.family == "quantum_crypto_go":
        lines.append("- False negatives are most likely in Go crypto helpers where weak algorithms are simple constructor calls with little surrounding context.")
    else:
        lines.append("- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.")
    lines.append("- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.")
    lines.append("- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.")
    if comparison.get("verdict") not in {"PASS", "PASS_CLEAN"}:
        lines.append(f"- Current run already demonstrated this risk: verdict=`{comparison.get('verdict')}`.")
    lines.append("")
    return lines


def _render_dossier(
    config: LabConfig,
    scenario: ScenarioSpec,
    repo_root: Path,
    repo_metadata: dict[str, Any],
    published_metadata: dict[str, Any] | None,
    build_status: BuildStatus,
    test_status: BuildStatus,
    smoke_status: BuildStatus,
    comparison: dict[str, Any],
    file_rows: list[dict[str, Any]],
    tree_text: str,
    composition: dict[str, int],
    realism_score: int,
    realism_note: str,
    alias_validation_root: Path,
    report_dossier_path: Path,
) -> str:
    remote_url = ""
    remote_provider = "remote"
    if published_metadata:
        remote_url = published_metadata.get("html_url") or published_metadata.get("clone_url") or ""
        remote_provider = str(published_metadata.get("provider") or remote_provider)
    default_branch = ""
    if published_metadata:
        default_branch = published_metadata.get("default_branch", "")
    if not default_branch:
        default_branch = "main" if "main" in repo_metadata.get("git", {}).get("branches", {}) else next(iter(repo_metadata.get("git", {}).get("branches", {})), "main")
    scan_modes = ", ".join(sorted({plan.scan_mode for plan in scenario.scan_plans}))
    branch_scopes = ", ".join(sorted({plan.branch_scope for plan in scenario.scan_plans}))
    components = _top_level_components(file_rows)
    config_paths = _config_paths(file_rows)
    test_paths = _test_paths(file_rows)
    docs_noise_paths = _docs_noise_paths(file_rows)
    total_loc = composition.get("total", 0)
    filler_ratio = (composition["synthetic filler / inflation content"] / total_loc) if total_loc else 0.0

    lines = [
        f"# Generated Project Dossier - {scenario.id}",
        "",
        "## 1. Scenario Identity",
        "",
        f"- scenarioId: `{scenario.id}`",
        f"- scenarioName: {scenario.summary}",
        f"- milestone: `{scenario.milestone}`",
        f"- targetModule: `{_target_module_label(scenario.module)}`",
        f"- language / stack: `{scenario.stack}`",
        f"- repoType: `{_repo_type(scenario)}`",
        f"- repo local path: `{repo_root}`",
        f"- repo remote provider: `{remote_provider}`",
        f"- repo remote URL: `{remote_url or 'dry-run / not published'}`",
        f"- default branch: `{default_branch}`",
        f"- scan modes intended for this scenario: `{scan_modes}`",
        f"- branch scopes intended for this scenario: `{branch_scopes}`",
        f"- project-local dossier path: `{repo_root / 'validation' / 'generated-project-dossier.md'}`",
        f"- required alias dossier path: `{alias_validation_root / 'generated-project-dossier.md'}`",
        f"- central dossier report path: `{report_dossier_path}`",
        "",
        "## 2. Business Context and Why This Repo Is Realistic",
        "",
        f"This scenario models `{scenario.domain}` as a `{scenario.stack}` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.",
        "",
        f"A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `{scenario.summary}`.",
        "",
        "## 3. Architecture Summary",
        "",
        f"- Major components: `{', '.join(components)}`",
        f"- Runtime role: `{scenario.domain}`",
        f"- Config flow: `{', '.join(config_paths) if config_paths else 'No dedicated live-config files; runtime behavior is code-driven.'}`",
        f"- Secret flow: `{', '.join(sorted({expected.path_contains for expected in scenario.expected_findings if 'guardian' in (_module_for_expected(expected, scenario)).lower() or 'secret' in expected.key.lower() or 'key' in expected.key.lower()})) or 'No Guardian must-find secret path in this scenario.'}`",
        f"- Crypto/TLS flow if relevant: `{', '.join(sorted({expected.path_contains for expected in scenario.expected_findings if _module_for_expected(expected, scenario) == 'Quantum'})) or 'Not a Quantum-positive scenario.'}`",
        f"- Test surfaces: `{', '.join(test_paths) if test_paths else 'No dedicated test folder beyond build smoke helpers.'}`",
        f"- Docs/vendor/generated surfaces: `{', '.join(docs_noise_paths) if docs_noise_paths else 'No extra docs/vendor/generated surfaces detected.'}`",
        "",
        "## 4. Full Repository Tree",
        "",
        "Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.",
        "",
        "```text",
        tree_text,
        "```",
        "",
        "## 5. File Inventory Table",
        "",
        "| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |",
        "| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in file_rows:
        lines.append(
            "| {path} | {classification} | {loc} | {purpose} | {positive} | {near_real} | {protected} | {build} | {test} | {smoke} |".format(
                path=_safe_inline(row["path"]),
                classification=row["classification"],
                loc=row["loc"],
                purpose=_safe_inline(row["purpose"]),
                positive="yes" if row["positiveSurface"] else "no",
                near_real="yes" if row["nearRealNegative"] else "no",
                protected="yes" if row["protectedNegative"] else "no",
                build="yes" if row["participatesInBuild"] else "no",
                test="yes" if row["participatesInTest"] else "no",
                smoke="yes" if row["participatesInSmoke"] else "no",
            )
        )
    lines.extend(["", "## 6. Positive Surfaces", ""])
    if not scenario.expected_findings:
        lines.append("- No deliberate positive surfaces are declared for this scenario.")
    for expected in scenario.expected_findings:
        actual_paths = _matching_paths(file_rows, expected.path_contains)
        lines.append(f"- Path: `{', '.join(actual_paths) if actual_paths else expected.path_contains}`")
        lines.append(f"  Why it should be detected: scenario declares `{expected.key}` as a live positive surface.")
        lines.append(f"  Target module: `{_module_for_expected(expected, scenario)}`")
        lines.append(f"  Finding family / rule family expectation: `{expected.rule_key_contains or expected.resolved_value_contains or expected.key}`")
        lines.append(f"  Head/history behavior: `{_finding_behavior(expected)}`")
        lines.append(f"  Explainability expectation: {_explainability_note(expected, scenario)}")
    lines.extend(["", "## 7. Near-Real Negative Surfaces", ""])
    near_real_rows = [row for row in file_rows if row["nearRealNegative"]]
    if not near_real_rows:
        lines.append("- No near-real negative surfaces were declared for this scenario.")
    for row in near_real_rows:
        lines.append(f"- `{row['path']}`: {_negative_reason(row)}")
    lines.extend(["", "## 8. Protected Negative Surfaces", ""])
    protected_rows = [row for row in file_rows if row["protectedNegative"]]
    if not protected_rows:
        lines.append("- No protected negative paths were present in this scenario.")
    else:
        lines.append("| path | classification | why protected |")
        lines.append("| --- | --- | --- |")
        for row in protected_rows:
            lines.append(f"| {_safe_inline(row['path'])} | {row['classification']} | {_safe_inline(_negative_reason(row))} |")
    lines.extend(["", "## 9. Branch and Commit Plan", ""])
    lines.extend(_history_section(repo_root, scenario, repo_metadata))
    lines.extend(["## 10. Runnability Contract", ""])
    lines.extend(_build_context_table(build_status, "build"))
    lines.extend(_build_context_table(test_status, "test"))
    lines.extend(_build_context_table(smoke_status, "smoke"))
    lines.extend(["## 11. Critical Generated Content Detail", ""])
    critical_paths = _critical_paths(file_rows, scenario, comparison)
    if not critical_paths:
        lines.append("No critical files were selected, which would itself be a dossier quality failure.")
    for path in critical_paths:
        row = next((item for item in file_rows if item["path"] == path), None)
        if row is None:
            continue
        file_path = repo_root / Path(path)
        markers = _markers_for_path(path, scenario, comparison)
        lines.extend(
            [
                f"### `{path}`",
                "",
                f"- Why this file matters: `{row['classification']}` file with expectation `{row['findingExpectation']}`.",
                f"- Detailed summary: {row['purpose']} It is {'executable/live' if row['classification'] in {'live-code', 'live-config', 'script'} else 'non-live or protected'} in the assembled repository.",
                f"- Key constructs: {'positive surface' if row['positiveSurface'] else 'negative or realism-supporting surface'}; near-real=`{row['nearRealNegative']}`; protected=`{row['protectedNegative']}`.",
                "- Representative excerpt:",
                "",
                "```text",
                _representative_excerpt(file_path, markers),
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## 12. Line Composition and Filler Disclosure",
            "",
            f"- Total LOC considered for authored/generated project content: `{total_loc}`",
            f"- Synthetic filler / inflation LOC: `{composition['synthetic filler / inflation content']}`",
            f"- Synthetic filler ratio: `{filler_ratio:.2%}`",
            "",
            "| category | LOC |",
            "| --- | ---: |",
        ]
    )
    for key in (
        "live business code",
        "live config",
        "tests",
        "docs",
        "scripts",
        "fixtures",
        "vendor/generated",
        "synthetic filler / inflation content",
    ):
        lines.append(f"| {key} | {composition[key]} |")
    lines.extend(
        [
            "",
            "Inflation disclosure:",
            "",
            "- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.",
            "- These filler lines are intentionally disclosed above and are not being presented as live business logic.",
            "",
            "## 13. Expected Findings Matrix",
            "",
            "### must_find",
            "",
        ]
    )
    if not scenario.expected_findings:
        lines.append("- None.")
    for expected in scenario.expected_findings:
        lines.append(f"- path: `{expected.path_contains}`")
        lines.append(f"  module: `{_module_for_expected(expected, scenario)}`")
        lines.append(f"  expected rule/finding family: `{expected.rule_key_contains or expected.resolved_value_contains or expected.key}`")
        lines.append(f"  expected branch/ref behavior: `{_finding_behavior(expected)}`")
        lines.append(f"  expected explainability behavior: {_explainability_note(expected, scenario)}")
    lines.extend(["", "### must_not_find", ""])
    if not scenario.expected_absent:
        lines.append("- None.")
    for expected in scenario.expected_absent:
        matching_rows = [row for row in file_rows if _path_matches(expected.path_contains, row["path"])]
        negative_kind = "protected negative" if any(row["protectedNegative"] for row in matching_rows) else "near-real negative"
        lines.append(f"- path: `{expected.path_contains}`")
        lines.append("  why finding must not appear: scenario declares this path clean despite adversarial content or naming.")
        lines.append(f"  negative type: `{negative_kind}`")
    lines.extend(["", "### may_find_review", ""])
    if not comparison.get("mayFindReview"):
        lines.append("- None in the current run.")
    for item in comparison.get("mayFindReview", []):
        lines.append(f"- `{item.get('primaryFilePath')}` => `{item.get('ruleKey') or item.get('ruleName')}` ({item.get('findingKind')}/{item.get('severity')})")
    lines.extend(["", "## 14. Explainability Expectations", ""])
    lines.extend(_explainability_section(scenario))
    lines.extend(["## 15. FP/FN Risk Notes", ""])
    lines.extend(_risk_notes(scenario, comparison))
    lines.extend(
        [
            "## 16. Realism Justification",
            "",
            "- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.",
            f"- What makes it feel real: {realism_note}.",
            "- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.",
            f"- Realism score: `{realism_score}/5`",
            "",
            "## 17. Final Reviewer Summary",
            "",
            f"- What this scenario is proving: `{scenario.summary}`",
            "- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.",
            f"- First outputs to inspect on failure: `{repo_root / 'validation' / 'generated-project-dossier.md'}`, `{repo_root / 'validation' / 'generated-file-manifest.json'}`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_project_dossier(
    *,
    config: LabConfig,
    scenario: ScenarioSpec,
    repo_root: Path,
    repo_metadata: dict[str, Any],
    published_metadata: dict[str, Any] | None,
    build_status: BuildStatus,
    test_status: BuildStatus,
    smoke_status: BuildStatus,
    comparison: dict[str, Any],
) -> dict[str, Any]:
    repo_validation_root = ensure_dir(repo_root / "validation")
    alias_validation_root = ensure_dir(config.generated_root / scenario.id / "validation")
    report_dossier_path = ensure_dir(config.reports_root / "generated-project-dossiers") / f"{scenario.id}.md"
    repo_dossier_path = repo_validation_root / "generated-project-dossier.md"
    repo_manifest_path = repo_validation_root / "generated-file-manifest.json"
    repo_tree_path = repo_validation_root / "generated-tree.txt"
    alias_dossier_path = alias_validation_root / "generated-project-dossier.md"
    alias_manifest_path = alias_validation_root / "generated-file-manifest.json"
    alias_tree_path = alias_validation_root / "generated-tree.txt"

    authored_rows = _collect_file_rows(repo_root, scenario, build_status, test_status, smoke_status, comparison)
    composition = _loc_composition(authored_rows)
    realism_score, realism_note = _realism_assessment(scenario, composition, comparison.get("runnability", {}))
    file_rows = authored_rows
    dossier = ""
    tree_text = ""
    for _ in range(2):
        tree_text = "\n".join(_tree_lines(repo_root))
        dossier = _render_dossier(
            config,
            scenario,
            repo_root,
            repo_metadata,
            published_metadata,
            build_status,
            test_status,
            smoke_status,
            comparison,
            file_rows,
            tree_text,
            composition,
            realism_score,
            realism_note,
            alias_validation_root,
            report_dossier_path,
        )
        write_text(repo_dossier_path, dossier)
        write_json(repo_manifest_path, file_rows)
        write_text(repo_tree_path, tree_text + "\n")
        file_rows = _collect_file_rows(repo_root, scenario, build_status, test_status, smoke_status, comparison)

    tree_text = "\n".join(_tree_lines(repo_root))
    dossier = _render_dossier(
        config,
        scenario,
        repo_root,
        repo_metadata,
        published_metadata,
        build_status,
        test_status,
        smoke_status,
        comparison,
        file_rows,
        tree_text,
        composition,
        realism_score,
        realism_note,
        alias_validation_root,
        report_dossier_path,
    )
    write_text(repo_dossier_path, dossier)
    write_json(repo_manifest_path, file_rows)
    write_text(repo_tree_path, tree_text + "\n")

    write_text(alias_dossier_path, dossier)
    write_json(alias_manifest_path, file_rows)
    write_text(alias_tree_path, tree_text + "\n")

    write_text(report_dossier_path, dossier)

    total = composition.get("total", 0)
    filler_ratio = (composition["synthetic filler / inflation content"] / total) if total else 0.0
    return {
        "dossierPath": str(alias_dossier_path),
        "projectLocalDossierPath": str(repo_dossier_path),
        "reportDossierPath": str(report_dossier_path),
        "generatedManifestPath": str(alias_manifest_path),
        "generatedTreePath": str(alias_tree_path),
        "runnabilityLogRootPath": str(repo_root / "validation" / "runnability-logs"),
        "locComposition": composition,
        "fillerRatio": filler_ratio,
        "realismScore": realism_score,
        "realismJustification": realism_note,
        "dossierMissing": False,
    }
