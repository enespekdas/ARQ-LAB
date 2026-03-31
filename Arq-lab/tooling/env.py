from __future__ import annotations

import os
from pathlib import Path

from .models import LabConfig
from .utils import ensure_dir


def _read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def _resolve_root(explicit_root: Path | None = None) -> Path:
    return explicit_root or Path(__file__).resolve().parents[1]


def _merge_env_values(target: dict[str, str], source: dict[str, str]) -> None:
    for key, value in source.items():
        if value == "" and target.get(key):
            continue
        target[key] = value


def _resolve_path(root: Path, raw_value: str) -> Path:
    candidate = Path(raw_value)
    if not candidate.is_absolute():
        candidate = root / candidate
    return candidate


def load_config(explicit_root: Path | None = None) -> LabConfig:
    root = _resolve_root(explicit_root)
    env_values = {}
    for candidate in [
        root / ".env",
        root / ".env.example",
        root.parent / "lab" / ".env",
        root.parent / "lab" / ".env.example",
    ]:
        _merge_env_values(env_values, _read_env_file(candidate))
    _merge_env_values(
        env_values,
        {
            key: value
            for key, value in os.environ.items()
            if key.startswith(("ARQ_", "GITEA_", "SCAN_", "FINDINGS_", "GIT_", "REPOSITORIES_"))
        },
    )

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
