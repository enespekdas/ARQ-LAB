from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping

from .logging_utils import log_event


@dataclass(slots=True)
class CommandResult:
    command: list[str]
    cwd: str
    returncode: int
    stdout: str
    stderr: str

    def ok(self) -> bool:
        return self.returncode == 0


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def timestamp_slug() -> str:
    return now_utc().strftime("%Y%m%dT%H%M%SZ")


def slugify(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-{2,}", "-", lowered)
    return lowered.strip("-")


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8", newline="\n")


def append_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def write_json(path: Path, payload: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True), encoding="utf-8", newline="\n")


def read_json(path: Path, default: Any | None = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_yaml_like(path: Path, lines: Iterable[str]) -> None:
    write_text(path, "\n".join(lines).rstrip() + "\n")


def safe_rmtree(path: Path, allowed_root: Path) -> None:
    resolved_path = path.resolve()
    resolved_root = allowed_root.resolve()
    if resolved_root not in resolved_path.parents and resolved_path != resolved_root:
        raise ValueError(f"Refusing to delete outside allowed root: {resolved_path}")
    if path.exists():
        def _onerror(func, candidate, exc_info):  # type: ignore[no-untyped-def]
            os.chmod(candidate, stat.S_IWRITE)
            func(candidate)

        shutil.rmtree(path, onerror=_onerror)


def list_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    return [candidate for candidate in path.rglob("*") if candidate.is_file()]


def count_lines(path: Path) -> int:
    total = 0
    for file_path in list_files(path):
        try:
            total += file_path.read_text(encoding="utf-8").count("\n") + 1
        except UnicodeDecodeError:
            continue
    return total


def run_command(
    command: list[str],
    cwd: Path,
    *,
    env: Mapping[str, str] | None = None,
    timeout: int | None = None,
    check: bool = False,
) -> CommandResult:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    resolved_command = command[:]
    resolved_command[0] = _resolve_executable(command[0])
    log_event("command.start", command=resolved_command, cwd=str(cwd))
    completed = subprocess.run(
        resolved_command,
        cwd=str(cwd),
        env=merged_env,
        timeout=timeout,
        text=True,
        capture_output=True,
        check=False,
    )
    result = CommandResult(
        command=resolved_command,
        cwd=str(cwd),
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )
    log_event("command.finish", command=resolved_command, cwd=str(cwd), returncode=result.returncode)
    if check and not result.ok():
        raise RuntimeError(
            "Command failed: %s\nstdout:\n%s\nstderr:\n%s"
            % (" ".join(resolved_command), result.stdout.strip(), result.stderr.strip())
        )
    return result


def with_path_prefix(path_entries: Iterable[str], extra_env: Mapping[str, str] | None = None) -> dict[str, str]:
    env = dict(extra_env or {})
    current = env.get("PATH") or os.environ.get("PATH", "")
    env["PATH"] = os.pathsep.join([entry for entry in path_entries if entry] + [current])
    return env


def as_json_ready(data: Any) -> Any:
    if hasattr(data, "__dataclass_fields__"):
        return {key: as_json_ready(value) for key, value in data.__dict__.items()}
    if isinstance(data, dict):
        return {key: as_json_ready(value) for key, value in data.items()}
    if isinstance(data, (list, tuple)):
        return [as_json_ready(value) for value in data]
    if isinstance(data, Path):
        return str(data)
    if isinstance(data, datetime):
        return data.isoformat()
    return data


def _resolve_executable(command: str) -> str:
    if Path(command).exists():
        return command
    toolchain_root = Path(__file__).resolve().parent.parent / ".toolchains"
    candidates = [
        toolchain_root / "dotnet" / f"{command}.exe",
        toolchain_root / "go" / "bin" / f"{command}.exe",
        Path(r"C:\maven\apache-maven-3.9.12\bin") / f"{command}.cmd",
        Path(r"C:\maven\apache-maven-3.9.12\bin") / command,
        Path(r"C:\Program Files\Git\cmd") / f"{command}.exe",
        Path(r"C:\Program Files\nodejs") / f"{command}.exe",
        Path(r"C:\Program Files\nodejs") / f"{command}.cmd",
        Path(r"C:\Program Files\Java\jdk-21.0.10\bin") / f"{command}.exe",
        Path(r"C:\Program Files\dotnet") / f"{command}.exe",
        Path(r"C:\Windows\System32\WindowsPowerShell\v1.0") / f"{command}.exe",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    resolved = shutil.which(command)
    if resolved:
        return resolved
    return command
