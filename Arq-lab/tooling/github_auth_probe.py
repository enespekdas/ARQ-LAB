from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .env import collect_env_provenance, load_config
from .git_factory import GitFactory
from .github_client import GitHubClient
from .utils import write_json, write_text


def _report_paths(root: Path) -> tuple[Path, Path]:
    reports_root = root / "reports"
    return reports_root / "github-auth-probe.json", reports_root / "github-auth-probe.md"


def _render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# GitHub Auth Probe",
        "",
        "## Candidate Sources",
        "",
    ]
    for source in report["candidateSources"]:
        lines.append(f"- `{source['name']}` ({source['kind']}) exists=`{source['exists']}`")
    lines.extend(["", "## Effective Keys", ""])
    for key, item in report["keys"].items():
        lines.append(f"### `{key}`")
        lines.append("")
        lines.append(f"- winningSource: `{item['winningSource'] or 'none'}`")
        lines.append(f"- finalValueEmpty: `{item['finalValueEmpty']}`")
        lines.append(f"- finalLength: `{item['finalLength']}`")
        lines.append(f"- maskedPreview: `{item['maskedPreview']}`")
        lines.append(f"- sha256: `{item['sha256']}`")
        lines.append(f"- quotesDetected: `{item['quotesDetected']}`")
        lines.append(f"- inlineCommentDetected: `{item['inlineCommentDetected']}`")
        lines.append(f"- whitespaceChanged: `{item['whitespaceChanged']}`")
        lines.append(f"- osEnvOverrodeFileEnv: `{item['osEnvOverrodeFileEnv']}`")
        lines.append(f"- labSiblingEnvOverrodeArqLabEnv: `{item['labSiblingEnvOverrodeArqLabEnv']}`")
        lines.append("")
    auth = report["auth"]
    lines.extend(
        [
            "## GitHub /user",
            "",
            f"- status: `{auth['status']}`",
            f"- outcome: `{auth['outcome']}`",
            f"- viewerLogin: `{auth.get('viewerLogin', '')}`",
            f"- error: {auth.get('error', 'none')}",
        ]
    )
    if report.get("probeRepo"):
        probe = report["probeRepo"]
        lines.extend(
            [
                "",
                "## Probe Repo",
                "",
                f"- name: `{probe['name']}`",
                f"- htmlUrl: `{probe['htmlUrl']}`",
                f"- cloneUrl: `{probe['cloneUrl']}`",
                f"- createStatus: `{probe['createStatus']}`",
                f"- pushStatus: `{probe['pushStatus']}`",
                f"- error: {probe.get('error', 'none')}",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="ARQ Lab GitHub auth probe with env provenance")
    parser.add_argument("--create-probe", action="store_true", help="Create and push a probe repo only after /user succeeds")
    parser.add_argument("--probe-name", default="arq-lab-github-auth-probe", help="Probe repo name to use if --create-probe is passed")
    args = parser.parse_args()

    root = Path.cwd()
    config = load_config(root)
    provenance = collect_env_provenance(root)
    client = GitHubClient(config)
    report: dict[str, Any] = {
        "candidateSources": provenance["candidateSources"],
        "keys": provenance["keys"],
        "auth": {"status": 0, "outcome": "", "viewerLogin": "", "error": ""},
    }

    try:
        viewer = client.viewer() or {}
        report["auth"] = {"status": 200, "outcome": "success", "viewerLogin": viewer.get("login", ""), "error": ""}
    except Exception as exc:
        report["auth"] = {"status": 401, "outcome": "failed", "viewerLogin": "", "error": str(exc)}

    if args.create_probe and report["auth"]["status"] == 200:
        git_factory = GitFactory(
            workspace_root=config.repositories_root,
            askpass_script=config.toolchains_root / "git-askpass.cmd",
            auth_token=config.git_token,
        )
        probe_root = config.repositories_root / args.probe_name
        git_factory.recreate_repository(probe_root)
        git_factory.init(probe_root)
        (probe_root / "README.md").write_text("# ARQ Lab GitHub Auth Probe\n", encoding="utf-8")
        git_factory.add_all(probe_root)
        git_factory.commit_all(probe_root, "probe commit")
        probe = {
            "name": args.probe_name,
            "htmlUrl": client.html_url(args.probe_name),
            "cloneUrl": client.clone_url(args.probe_name),
            "createStatus": "pending",
            "pushStatus": "pending",
            "error": "",
        }
        try:
            payload = client.ensure_repo(args.probe_name, "ARQ Lab GitHub auth probe")
            git_factory.set_remote(probe_root, "origin", client.clone_url(args.probe_name))
            git_factory.push_all(probe_root)
            client.ensure_default_branch(args.probe_name, config.arq_lab_default_branch)
            probe["htmlUrl"] = payload.get("html_url", probe["htmlUrl"])
            probe["cloneUrl"] = payload.get("clone_url", probe["cloneUrl"])
            probe["createStatus"] = "success"
            probe["pushStatus"] = "success"
        except Exception as exc:
            probe["createStatus"] = "failed"
            probe["pushStatus"] = "failed"
            probe["error"] = str(exc)
        report["probeRepo"] = probe

    json_path, md_path = _report_paths(root)
    write_json(json_path, report)
    write_text(md_path, _render_markdown(report))
    print(str(json_path))
    print(str(md_path))


if __name__ == "__main__":
    main()
