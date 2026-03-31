from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .git_factory import GitFactory
from .github_client import GitHubClient
from .env import load_config
from .models import LabConfig
from .utils import read_json, write_json, write_text


def _owner_login(payload: dict[str, Any]) -> str:
    owner = payload.get("owner")
    if isinstance(owner, dict):
        return str(owner.get("login") or owner.get("username") or "").strip()
    return str(owner or payload.get("ownerLogin") or "").strip()


def _provider_for(payload: dict[str, Any], metadata_path: Path) -> str:
    html_url = str(payload.get("html_url") or payload.get("htmlUrl") or "")
    clone_url = str(payload.get("clone_url") or payload.get("cloneUrl") or "")
    marker = f"{html_url} {clone_url} {metadata_path.name}".lower()
    if "github.com" in marker:
        return "github"
    if "localhost:3001" in marker or "gitea" in marker:
        return "gitea"
    return "unknown"


def collect_published_repository_inventory(config: LabConfig) -> list[dict[str, Any]]:
    entries: dict[str, dict[str, Any]] = {}
    metadata_paths = sorted(
        list(config.runs_root.rglob("gitea-repository.json")) + list(config.runs_root.rglob("published-repository.json"))
    )
    for metadata_path in metadata_paths:
        payload = read_json(metadata_path, {})
        if not isinstance(payload, dict) or not payload:
            continue
        name = str(payload.get("name") or "").strip()
        if not name:
            continue
        owner = _owner_login(payload)
        full_name = str(payload.get("full_name") or payload.get("fullName") or f"{owner}/{name}" if owner else name).strip()
        clone_url = str(payload.get("clone_url") or payload.get("cloneUrl") or "").strip()
        html_url = str(payload.get("html_url") or payload.get("htmlUrl") or "").strip()
        scenario_metadata = read_json(metadata_path.parent / "scenario-metadata.json", {})
        scenario_info = scenario_metadata.get("scenario", {}) if isinstance(scenario_metadata, dict) else {}
        repo_metadata = scenario_metadata.get("repoMetadata", {}) if isinstance(scenario_metadata, dict) else {}
        milestone = str(scenario_info.get("milestone") or metadata_path.parent.parent.name).strip()
        scenario_id = str(scenario_info.get("id") or metadata_path.parent.name).strip()
        logical_repo_slug = str(
            scenario_info.get("repo_name") or repo_metadata.get("repoName") or name
        ).strip()
        record = {
            "scenarioId": scenario_id,
            "milestone": milestone,
            "logicalRepoSlug": logical_repo_slug,
            "sourceProvider": _provider_for(payload, metadata_path),
            "sourceOwnerRepo": full_name,
            "sourceOwner": owner,
            "sourceRepo": name,
            "sourceCloneUrl": clone_url,
            "sourceHtmlUrl": html_url,
            "sourceDefaultBranch": str(payload.get("default_branch") or "main"),
            "description": str(payload.get("description") or ""),
            "metadataPath": str(metadata_path),
            "localPath": str(config.repositories_root / name),
            "targetOwnerRepo": f"{config.git_owner}/{name}",
            "targetCloneUrl": f"{config.git_base_url}/{config.git_owner}/{name}.git",
            "targetHtmlUrl": f"{config.git_base_url}/{config.git_owner}/{name}",
        }
        entries[full_name] = record
    return [entries[key] for key in sorted(entries)]


def _write_inventory_reports(config: LabConfig, inventory: list[dict[str, Any]]) -> dict[str, Path]:
    json_path = config.reports_root / "repository-publish-inventory.json"
    md_path = config.reports_root / "repository-publish-inventory.md"
    write_json(json_path, inventory)
    lines = [
        "# Repository Publish Inventory",
        "",
        f"- Total discovered published repos: `{len(inventory)}`",
        "",
        "| source owner/repo | target owner/repo | provider | scenario | local path | source metadata |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in inventory:
        lines.append(
            f"| {item['sourceOwnerRepo']} | {item['targetOwnerRepo']} | {item['sourceProvider']} | {item['scenarioId']} | {item['localPath']} | {item['metadataPath']} |"
        )
    write_text(md_path, "\n".join(lines).rstrip() + "\n")
    return {"json": json_path, "md": md_path}


def write_inventory_reports(config: LabConfig) -> list[dict[str, Any]]:
    inventory = collect_published_repository_inventory(config)
    _write_inventory_reports(config, inventory)
    return inventory


def migrate_published_repositories(
    config: LabConfig,
    *,
    git_factory: GitFactory,
    github: GitHubClient,
    limit: int | None = None,
    repo_names: set[str] | None = None,
) -> list[dict[str, Any]]:
    inventory = collect_published_repository_inventory(config)
    selected = []
    for item in inventory:
        if repo_names and item["sourceRepo"] not in repo_names:
            continue
        selected.append(item)
        if limit is not None and len(selected) >= limit:
            break

    results: list[dict[str, Any]] = []
    existing_target_names: set[str] = set()
    auth_error: str | None = None
    try:
        existing_target_names = {str(repo.get("name")) for repo in github.list_org_repos()}
    except Exception as exc:  # pragma: no cover - network/auth dependent
        auth_error = str(exc)

    for item in selected:
        result = dict(item)
        result.update(
            {
                "action": "recreated/pushed" if item["sourceProvider"] == "gitea" else "transfer",
                "status": "pending",
                "reason": "",
                "remoteUrl": item["targetHtmlUrl"],
                "pushStatus": "not-started",
            }
        )
        if auth_error:
            result["action"] = "skip"
            result["status"] = "blocked"
            result["reason"] = f"GitHub API auth failed before migration started: {auth_error}"
            result["pushStatus"] = "blocked"
            results.append(result)
            continue
        if item["sourceProvider"] != "gitea":
            result["action"] = "skip"
            result["status"] = "skipped"
            result["reason"] = "Only cross-host Gitea historical publishes are present in the current ARQ-LAB inventory."
            result["pushStatus"] = "skipped"
            results.append(result)
            continue
        if not item["sourceCloneUrl"]:
            result["action"] = "skip"
            result["status"] = "blocked"
            result["reason"] = "Source clone URL is missing from published metadata."
            result["pushStatus"] = "blocked"
            results.append(result)
            continue

        repo_root = Path(item["localPath"])
        try:
            if git_factory.is_repository(repo_root):
                git_factory.set_remote(repo_root, "source", item["sourceCloneUrl"])
            else:
                git_factory.clone(item["sourceCloneUrl"], repo_root, remote_name="source")
            git_factory.fetch(repo_root, "source")
            git_factory.sync_remote_branches_to_local_heads(repo_root, "source")
            git_factory.set_remote(repo_root, "origin", github.clone_url(item["sourceRepo"]))

            target_name = item["sourceRepo"]
            repo_existed = target_name in existing_target_names
            repo_payload = github.ensure_repo(target_name, item["description"])
            git_factory.push_all(repo_root, "origin")
            github.ensure_default_branch(target_name, item["sourceDefaultBranch"] or "main")
            existing_target_names.add(target_name)

            result["action"] = "reuse/sync" if repo_existed else "recreated/pushed"
            result["status"] = "success"
            result["reason"] = (
                "Cross-host Gitea->GitHub migration cannot preserve hosting-level settings via transfer; repo was recreated and pushed with git history preserved."
                if not repo_existed
                else "Target repo already existed in ARQ-Sec; local history was synced and pushed."
            )
            result["remoteUrl"] = github.html_url(target_name)
            result["pushStatus"] = "success"
            result["targetMetadata"] = github.normalized_metadata(target_name, repo_payload)
        except Exception as exc:  # pragma: no cover - network/auth dependent
            result["status"] = "failed"
            result["reason"] = str(exc)
            result["pushStatus"] = "failed"
        results.append(result)

    report_json = config.reports_root / "repository-migration-results.json"
    report_md = config.reports_root / "repository-migration-results.md"
    write_json(report_json, results)
    lines = [
        "# Repository Migration Results",
        "",
        f"- Target owner: `{config.git_owner}`",
        f"- Attempted repos: `{len(results)}`",
        "",
        "| source owner/repo | target owner/repo | action | status | local path | remote URL | reason |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in results:
        lines.append(
            f"| {item['sourceOwnerRepo']} | {item['targetOwnerRepo']} | {item['action']} | {item['status']} | {item['localPath']} | {item['remoteUrl']} | {item['reason'].replace('|', '/')} |"
        )
    write_text(report_md, "\n".join(lines).rstrip() + "\n")
    _write_inventory_reports(config, inventory)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="ARQ Lab repository inventory and GitHub org publish migration")
    parser.add_argument("--inventory-only", action="store_true", help="Only emit the historical published-repo inventory")
    parser.add_argument("--limit", type=int, help="Limit the number of repos migrated")
    parser.add_argument("--repo", action="append", default=[], help="Specific published repo name(s) to migrate")
    args = parser.parse_args()

    config = load_config()
    if args.inventory_only:
        write_inventory_reports(config)
        return

    git_factory = GitFactory(
        workspace_root=config.repositories_root,
        askpass_script=config.toolchains_root / "git-askpass.cmd",
        auth_token=config.git_token,
    )
    github = GitHubClient(config)
    repo_names = set(args.repo) if args.repo else None
    migrate_published_repositories(config, git_factory=git_factory, github=github, limit=args.limit, repo_names=repo_names)


if __name__ == "__main__":
    main()
