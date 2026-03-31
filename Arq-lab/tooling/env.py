from __future__ import annotations

import hashlib
import os
import re
from pathlib import Path
from typing import Any

from .models import LabConfig
from .utils import ensure_dir


TRACKED_ENV_KEYS = ("GIT_TOKEN", "GIT_OWNER", "GIT_BASE_URL", "GIT_API_BASE_URL")


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest() if value else ""


def _masked_preview(key: str, value: str) -> str:
    if value == "":
        return ""
    if key == "GIT_TOKEN":
        if len(value) <= 8:
            return f"{value[:1]}...{value[-1:]}"
        return f"{value[:4]}...{value[-4:]}"
    if len(value) <= 60:
        return value
    return f"{value[:24]}...{value[-12:]}"


def _normalize_env_value(raw_value: str) -> tuple[str, dict[str, Any]]:
    normalized = raw_value
    whitespace_changed = normalized != normalized.strip()
    normalized = normalized.strip()
    quotes_detected = normalized[:1] in {'"', "'"} or normalized[-1:] in {'"', "'"}
    inline_comment_detected = False
    stripped_quotes = False

    if normalized[:1] in {'"', "'"}:
        quote = normalized[0]
        closing_index = normalized.find(quote, 1)
        if closing_index > 0:
            trailing = normalized[closing_index + 1 :].strip()
            if trailing == "" or trailing.startswith("#"):
                stripped_quotes = True
                inline_comment_detected = trailing.startswith("#")
                normalized = normalized[1:closing_index]
                return normalized, {
                    "quotesDetected": quotes_detected,
                    "strippedQuotes": stripped_quotes,
                    "inlineCommentDetected": inline_comment_detected,
                    "whitespaceChanged": whitespace_changed,
                }

    comment_match = re.search(r"\s+#", normalized)
    if comment_match:
        inline_comment_detected = True
        normalized = normalized[: comment_match.start()].rstrip()

    if len(normalized) >= 2 and normalized[0] == normalized[-1] and normalized[0] in {'"', "'"}:
        stripped_quotes = True
        normalized = normalized[1:-1]

    return normalized, {
        "quotesDetected": quotes_detected,
        "strippedQuotes": stripped_quotes,
        "inlineCommentDetected": inline_comment_detected,
        "whitespaceChanged": whitespace_changed,
    }


def _read_env_file_entries(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    values: dict[str, dict[str, Any]] = {}
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, raw_value = raw_line.split("=", 1)
        normalized_key = key.strip().lstrip("\ufeff")
        normalized_value, diagnostics = _normalize_env_value(raw_value)
        values[normalized_key] = {
            "value": normalized_value,
            "rawLength": len(raw_value),
            "length": len(normalized_value),
            "empty": normalized_value == "",
            **diagnostics,
        }
    return values


def _read_env_file(path: Path) -> dict[str, str]:
    return {key: entry["value"] for key, entry in _read_env_file_entries(path).items()}


def _resolve_root(explicit_root: Path | None = None) -> Path:
    return explicit_root or Path(__file__).resolve().parents[1]


def _merge_env_values(target: dict[str, str], source: dict[str, str]) -> None:
    for key, value in source.items():
        if value == "" and target.get(key):
            continue
        target[key] = value


def _candidate_sources(root: Path) -> list[dict[str, Any]]:
    return [
        {"name": str(root / ".env"), "kind": "file", "path": root / ".env"},
        {"name": str(root / ".env.example"), "kind": "file", "path": root / ".env.example"},
        {"name": str(root.parent / "lab" / ".env"), "kind": "file", "path": root.parent / "lab" / ".env"},
        {"name": str(root.parent / "lab" / ".env.example"), "kind": "file", "path": root.parent / "lab" / ".env.example"},
        {"name": "os.environ", "kind": "env"},
    ]


def _load_env_values_with_provenance(root: Path) -> tuple[dict[str, str], dict[str, Any]]:
    env_values: dict[str, str] = {}
    provenance: dict[str, Any] = {
        "candidateSources": [],
        "keys": {key: {"sources": [], "winningSource": "", "finalValueEmpty": True, "finalLength": 0, "maskedPreview": "", "sha256": "", "quotesDetected": False, "inlineCommentDetected": False, "whitespaceChanged": False} for key in TRACKED_ENV_KEYS},
    }

    for candidate in _candidate_sources(root):
        if candidate["kind"] == "file":
            path = candidate["path"]
            entries = _read_env_file_entries(path)
            provenance["candidateSources"].append({"name": candidate["name"], "kind": "file", "exists": path.exists()})
            source_values = {key: entry["value"] for key, entry in entries.items()}
            _merge_env_values(env_values, source_values)
            for key in TRACKED_ENV_KEYS:
                entry = entries.get(key)
                provenance["keys"][key]["sources"].append(
                    {
                        "source": candidate["name"],
                        "kind": "file",
                        "present": entry is not None,
                        "empty": True if entry is None else entry["empty"],
                        "length": 0 if entry is None else entry["length"],
                        "quotesDetected": False if entry is None else entry["quotesDetected"],
                        "inlineCommentDetected": False if entry is None else entry["inlineCommentDetected"],
                        "whitespaceChanged": False if entry is None else entry["whitespaceChanged"],
                        "selected": entry is not None and env_values.get(key, "") == entry["value"] and (entry["value"] != "" or provenance["keys"][key]["winningSource"] == ""),
                    }
                )
                if entry is not None and (entry["value"] != "" or not provenance["keys"][key]["winningSource"]):
                    provenance["keys"][key]["winningSource"] = candidate["name"]
                    provenance["keys"][key]["quotesDetected"] = entry["quotesDetected"]
                    provenance["keys"][key]["inlineCommentDetected"] = entry["inlineCommentDetected"]
                    provenance["keys"][key]["whitespaceChanged"] = entry["whitespaceChanged"]
        else:
            env_entries = {
                key: {
                    "value": value,
                    "empty": value == "",
                    "length": len(value),
                    "quotesDetected": value[:1] in {'"', "'"} or value[-1:] in {'"', "'"},
                    "inlineCommentDetected": " #" in value or "\t#" in value,
                    "whitespaceChanged": value != value.strip(),
                }
                for key, value in os.environ.items()
                if key.startswith(("ARQ_", "GITEA_", "SCAN_", "FINDINGS_", "GIT_", "REPOSITORIES_"))
            }
            provenance["candidateSources"].append({"name": candidate["name"], "kind": "env", "exists": True})
            _merge_env_values(env_values, {key: entry["value"] for key, entry in env_entries.items()})
            for key in TRACKED_ENV_KEYS:
                entry = env_entries.get(key)
                provenance["keys"][key]["sources"].append(
                    {
                        "source": candidate["name"],
                        "kind": "env",
                        "present": entry is not None,
                        "empty": True if entry is None else entry["empty"],
                        "length": 0 if entry is None else entry["length"],
                        "quotesDetected": False if entry is None else entry["quotesDetected"],
                        "inlineCommentDetected": False if entry is None else entry["inlineCommentDetected"],
                        "whitespaceChanged": False if entry is None else entry["whitespaceChanged"],
                        "selected": entry is not None and env_values.get(key, "") == entry["value"] and (entry["value"] != "" or provenance["keys"][key]["winningSource"] == ""),
                    }
                )
                if entry is not None and (entry["value"] != "" or not provenance["keys"][key]["winningSource"]):
                    provenance["keys"][key]["winningSource"] = candidate["name"]
                    provenance["keys"][key]["quotesDetected"] = entry["quotesDetected"]
                    provenance["keys"][key]["inlineCommentDetected"] = entry["inlineCommentDetected"]
                    provenance["keys"][key]["whitespaceChanged"] = entry["whitespaceChanged"]

    for key in TRACKED_ENV_KEYS:
        final_value = env_values.get(key, "")
        provenance["keys"][key]["finalValueEmpty"] = final_value == ""
        provenance["keys"][key]["finalLength"] = len(final_value)
        provenance["keys"][key]["maskedPreview"] = _masked_preview(key, final_value)
        provenance["keys"][key]["sha256"] = _sha256(final_value)
        provenance["keys"][key]["osEnvOverrodeFileEnv"] = provenance["keys"][key]["winningSource"] == "os.environ"
        provenance["keys"][key]["labSiblingEnvOverrodeArqLabEnv"] = provenance["keys"][key]["winningSource"] == str(root.parent / "lab" / ".env")
    return env_values, provenance


def _resolve_path(root: Path, raw_value: str) -> Path:
    candidate = Path(raw_value)
    if not candidate.is_absolute():
        candidate = root / candidate
    return candidate


def load_config(explicit_root: Path | None = None) -> LabConfig:
    root = _resolve_root(explicit_root)
    env_values, _ = _load_env_values_with_provenance(root)

    def value(name: str, default: str) -> str:
        return env_values.get(name, default)

    generated_root = ensure_dir(root / "generated")
    repositories_root = ensure_dir(_resolve_path(root, value("REPOSITORIES_ROOT", "repositories")))
    reports_root = ensure_dir(root / "reports")
    runs_root = ensure_dir(root / "runs")
    manifests_root = ensure_dir(root / "manifests")
    toolchains_root = ensure_dir(root / ".toolchains")

    return LabConfig(
        arq_api_base_url=value("ARQ_API_BASE_URL", "http://localhost:8080").rstrip("/"),
        arq_workspace_key=value("ARQ_WORKSPACE_KEY", "default"),
        arq_email=value("ARQ_EMAIL", "admin"),
        arq_password=value("ARQ_PASSWORD", "admin"),
        git_base_url=value("GIT_BASE_URL", "https://github.com").rstrip("/"),
        git_api_base_url=value("GIT_API_BASE_URL", "https://api.github.com").rstrip("/"),
        git_owner=value("GIT_OWNER", "ARQ-Sec"),
        git_token=value("GIT_TOKEN", ""),
        git_repo_visibility=value("GIT_REPO_VISIBILITY", "public"),
        gitea_base_url=value("GITEA_BASE_URL", "http://localhost:3001").rstrip("/"),
        gitea_username=value("GITEA_USERNAME", "arq"),
        gitea_password=value("GITEA_PASSWORD", "arq"),
        gitea_owner=value("GITEA_OWNER", "arq"),
        gitea_repo_visibility=value("GITEA_REPO_VISIBILITY", "public"),
        arq_lab_project_key=value("ARQ_LAB_PROJECT_KEY", "arq-lab"),
        arq_lab_project_name=value("ARQ_LAB_PROJECT_NAME", "ARQ Lab Validation"),
        arq_lab_default_branch=value("ARQ_LAB_DEFAULT_BRANCH", "main"),
        scan_poll_interval_seconds=int(value("SCAN_POLL_INTERVAL_SECONDS", "5")),
        scan_poll_timeout_seconds=int(value("SCAN_POLL_TIMEOUT_SECONDS", "1800")),
        findings_export_limit=int(value("FINDINGS_EXPORT_LIMIT", "5000")),
        lab_root=root,
        generated_root=generated_root,
        repositories_root=repositories_root,
        reports_root=reports_root,
        runs_root=runs_root,
        manifests_root=manifests_root,
        catalog_root=ensure_dir(root / "catalog"),
        templates_root=ensure_dir(root / "templates"),
        prompts_root=ensure_dir(root / "prompts"),
        docs_root=ensure_dir(root / "docs"),
        toolchains_root=toolchains_root,
    )


def collect_env_provenance(explicit_root: Path | None = None) -> dict[str, Any]:
    root = _resolve_root(explicit_root)
    _, provenance = _load_env_values_with_provenance(root)
    return provenance
