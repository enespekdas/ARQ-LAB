from __future__ import annotations

import random
import re
import warnings
from functools import lru_cache
from pathlib import Path
from typing import Any

import rstr
import yaml


_RULES_ROOT = Path(__file__).resolve().parents[3] / "ARQV2" / "ARQBackend" / "arq-engine-lib" / "src" / "main" / "resources" / "rules"

_GUARDIAN_BASELINE_COVERED = {"guardian.generic-api-key", "guardian.private-key"}
_QUANTUM_BASELINE_COVERED = {
    "quantum.arq-q-0012-java",
    "quantum.arq-q-0013-java",
    "quantum.arq-q-0026-java",
    "quantum.arq-q-0072-java",
    "quantum.arq-q-0082-java",
    "quantum.arq-q-0085-java",
    "quantum.arq-q-0131-java",
    "quantum.arq-q-0178-java",
    "quantum.arq-q-0247-python",
    "quantum.arq-q-0248-python",
    "quantum.arq-q-0260-python",
    "quantum.arq-q-0305-python",
    "quantum.arq-q-0418-csharp",
    "quantum.arq-q-0449-csharp",
    "quantum.arq-q-0453-csharp",
    "quantum.arq-q-0468-csharp",
    "quantum.arq-q-0488-csharp",
    "quantum.arq-q-0572-go",
    "quantum.arq-q-0573-go",
    "quantum.arq-q-0611-typescript",
    "quantum.arq-q-0613-typescript",
    "quantum.arq-q-0614-typescript",
    "quantum.arq-q-0930-config",
    "quantum.arq-q-0931-config",
    "quantum.arq-q-0949-config",
}

_NATIVE_LANGS = {
    "abap",
    "c",
    "cpp",
    "elixir",
    "erlang",
    "groovy",
    "jcl",
    "kotlin",
    "lua",
    "objectivec",
    "perl",
    "php",
    "plsql",
    "powershell",
    "ruby",
    "rust",
    "scala",
    "shell",
    "swift",
    "tsql",
    "zig",
}

_LANGUAGE_EXTENSIONS = {
    "abap": "abap",
    "c": "c",
    "config": "conf",
    "cpp": "cpp",
    "csharp": "cs",
    "elixir": "ex",
    "erlang": "erl",
    "go": "go",
    "groovy": "groovy",
    "java": "java",
    "javascript": "js",
    "jcl": "jcl",
    "kotlin": "kt",
    "lua": "lua",
    "objectivec": "m",
    "perl": "pl",
    "php": "php",
    "plsql": "sql",
    "powershell": "ps1",
    "python": "py",
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "shell": "sh",
    "swift": "swift",
    "tsql": "sql",
    "typescript": "ts",
    "zig": "zig",
}


def _read_rules(name: str) -> list[dict[str, Any]]:
    path = _RULES_ROOT / f"{name}.yml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    return payload if isinstance(payload, list) else []


def _normalized_seeded_sample(regex: str, seed: str, *, guardian: bool) -> str:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", FutureWarning)
        sample = rstr.Xeger(random.Random(seed)).xeger(regex)
    if not isinstance(sample, str):
        raise ValueError(f"Unable to generate sample for {seed}")
    sample = sample.replace("\x00", "")
    if guardian:
        return sample.strip()
    return re.sub(r"[\r\n\t\f\v]+", " ", sample).strip()


def _quantum_language(rule: dict[str, Any]) -> str:
    language = str(rule.get("language") or rule.get("metadataTags", {}).get("language") or "").strip()
    if language:
        return language
    return str(rule.get("id") or "").rsplit("-", 1)[-1]


def _guardian_path(pack_slug: str, index: int) -> str:
    variants = [
        f"integrations/{pack_slug}/runtime/provider_{index:03d}.env",
        f"integrations/{pack_slug}/config/provider_{index:03d}.yaml",
        f"deploy/{pack_slug}/provider_{index:03d}.properties",
        f"terraform/{pack_slug}/provider_{index:03d}.tfvars",
        f"ops/{pack_slug}/secrets/provider_{index:03d}.txt",
    ]
    return variants[(index - 1) % len(variants)]


def _config_path(rule: dict[str, Any], pack_slug: str, index: int) -> str:
    title = str(rule.get("name") or "").lower()
    if "nginx" in title:
        return f"deploy/live/{pack_slug}/nginx/rule_{index:03d}.conf"
    if "apache" in title:
        return f"deploy/live/{pack_slug}/apache/rule_{index:03d}.conf"
    if "haproxy" in title:
        return f"deploy/live/{pack_slug}/haproxy/rule_{index:03d}.cfg"
    if "ingress" in title or "kube" in title or "k8s" in title:
        return f"deploy/live/{pack_slug}/k8s/rule_{index:03d}.yaml"
    if "envoy" in title:
        return f"deploy/live/{pack_slug}/envoy/rule_{index:03d}.yaml"
    if "spring" in title or "jvm" in title:
        return f"deploy/live/{pack_slug}/spring/rule_{index:03d}.properties"
    if "ssh" in title:
        return f"deploy/live/{pack_slug}/ssh/rule_{index:03d}.conf"
    if "openssl" in title:
        return f"deploy/live/{pack_slug}/openssl/rule_{index:03d}.cnf"
    return f"deploy/live/{pack_slug}/runtime/rule_{index:03d}.conf"


def _quantum_path(language: str, pack_slug: str, index: int, rule: dict[str, Any]) -> str:
    if language == "config":
        return _config_path(rule, pack_slug, index)
    extension = _LANGUAGE_EXTENSIONS.get(language, "txt")
    if language == "java":
        return f"services/{pack_slug}/src/legacy/Rule{index:03d}.java"
    if language == "csharp":
        return f"services/{pack_slug}/src/legacy/Rule{index:03d}.cs"
    if language == "python":
        return f"workers/{pack_slug}/app/legacy/rule_{index:03d}.py"
    if language == "typescript":
        return f"apps/{pack_slug}/src/legacy/rule_{index:03d}.ts"
    if language == "javascript":
        return f"apps/{pack_slug}/src/legacy/rule_{index:03d}.js"
    if language == "go":
        return f"services/{pack_slug}/internal/legacy/rule_{index:03d}.go"
    return f"native/{pack_slug}/{language}/rule_{index:03d}.{extension}"


def _comment_prefix(language: str, path: str) -> str:
    lowered = path.lower()
    if lowered.endswith((".yaml", ".yml", ".env", ".properties", ".conf", ".cfg", ".cnf", ".tfvars", ".txt", ".ps1", ".rb", ".py", ".pl", ".lua", ".abap", ".sh", ".jcl")):
        return "#"
    if lowered.endswith(".sql"):
        return "--"
    return "//"


def _entry_content(entry: dict[str, Any]) -> str:
    comment = _comment_prefix(str(entry.get("language") or ""), str(entry["path"]))
    return "\n".join(
        [
            f"{comment} coverage campaign entry",
            f"{comment} rule_key: {entry['rule_key']}",
            str(entry["sample"]),
            "",
        ]
    )


def _chunk(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


@lru_cache(maxsize=1)
def _guardian_rule_entries() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in _read_rules("guardian"):
        rule_key = f"guardian.{item['id']}"
        if rule_key in _GUARDIAN_BASELINE_COVERED:
            continue
        regex = item.get("regex")
        if not isinstance(regex, str) or not regex.strip():
            continue
        try:
            sample = _normalized_seeded_sample(regex, rule_key, guardian=True)
        except Exception:
            continue
        if not sample:
            continue
        rows.append(
            {
                "rule_key": rule_key,
                "title": item.get("name") or item["id"],
                "family": item["id"],
                "language": "config",
                "sample": sample,
            }
        )
    return rows


@lru_cache(maxsize=1)
def _quantum_rule_entries() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in _read_rules("quantum"):
        rule_key = f"quantum.{item['id']}"
        if rule_key in _QUANTUM_BASELINE_COVERED:
            continue
        regex = item.get("regex")
        if not isinstance(regex, str) or not regex.strip():
            continue
        try:
            sample = _normalized_seeded_sample(regex, rule_key, guardian=False)
        except Exception:
            continue
        if not sample:
            continue
        rows.append(
            {
                "rule_key": rule_key,
                "title": item.get("name") or item["id"],
                "family": str(item.get("metadataTags", {}).get("ruleFamily") or item.get("name") or ""),
                "language": _quantum_language(item),
                "sample": sample,
            }
        )
    return rows


def _build_descriptor(
    *,
    scenario_id: str,
    milestone: str,
    repo_name: str,
    module: str,
    stack: str,
    domain: str,
    summary: str,
    scan_kind: str,
    entries: list[dict[str, Any]],
    line_target: str,
) -> dict[str, Any]:
    expected_findings = [
        {
            "key": f"rule-{index:03d}",
            "path_contains": entry["path"],
            "rule": entry["rule_key"],
        }
        for index, entry in enumerate(entries, start=1)
    ]
    return {
        "id": scenario_id,
        "milestone": milestone,
        "repo_name": repo_name,
        "module": module,
        "family": "coverage_bundle_repo",
        "stack": stack,
        "domain": domain,
        "summary": summary,
        "scan_kind": scan_kind,
        "line_target": line_target,
        "expected_findings": expected_findings,
        "metadata": {
            "coverageBundle": {
                "entries": entries,
                "generatedRuleCount": len(entries),
                "module": module,
                "scanKind": scan_kind,
            }
        },
    }


@lru_cache(maxsize=1)
def coverage_campaign_descriptors() -> list[dict[str, Any]]:
    guardian_rules = _guardian_rule_entries()[:100]
    guardian_themes = [
        ("G-V1-COV-101", "guardian-coverage-saas", "SaaS integration credential corpus covering provider-specific secrets in runtime configs, deploy files, and CI handoff notes."),
        ("G-V1-COV-102", "guardian-coverage-cloud", "Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state."),
        ("G-V1-COV-103", "guardian-coverage-automation", "Automation and CI credential corpus covering pipeline tokens, bot credentials, and service access keys."),
        ("G-V1-COV-104", "guardian-coverage-partners", "Partner ecosystem credential corpus spanning payments, messaging, maps, and collaboration providers."),
        ("G-V1-COV-105", "guardian-coverage-enterprise", "Enterprise admin credential corpus with mixed config formats, runtime secrets, and operational packaging."),
    ]

    descriptors: list[dict[str, Any]] = []
    for (scenario_id, repo_name, domain), chunk in zip(guardian_themes, _chunk(guardian_rules, 20), strict=False):
        entries = []
        pack_slug = repo_name.replace("_", "-")
        for index, rule in enumerate(chunk, start=1):
            path = _guardian_path(pack_slug, index)
            entries.append(
                {
                    **rule,
                    "path": path,
                    "content": _entry_content({**rule, "path": path}),
                }
            )
        descriptors.append(
            _build_descriptor(
                scenario_id=scenario_id,
                milestone="M1",
                repo_name=repo_name,
                module="guardian",
                stack="Config / IaC / CI credential coverage bundle",
                domain=domain,
                summary=f"Guardian provider coverage bundle exercising {len(entries)} distinct secret families.",
                scan_kind="guardian",
                entries=entries,
                line_target="6000-9000",
            )
        )

    quantum_rules = _quantum_rule_entries()
    by_language: dict[str, list[dict[str, Any]]] = {}
    for rule in quantum_rules:
        by_language.setdefault(rule["language"], []).append(rule)

    native_rules = [rule for rule in quantum_rules if rule["language"] in _NATIVE_LANGS]

    quantum_pack_defs: list[tuple[str, str, str, str, str, list[dict[str, Any]], int]] = [
        ("Q-V3-COV-101", "M3", "quantum-coverage-java-a", "Java / hybrid coverage pack", "Java crypto coverage pack A spanning block ciphers, RNG, keygen, KDF, inventory, and legacy primitives.", by_language.get("java", []), 25),
        ("Q-V3-COV-102", "M3", "quantum-coverage-java-b", "Java / hybrid coverage pack", "Java crypto coverage pack B extending legacy cipher, signature, and helper-driven rule families.", by_language.get("java", [])[25:], 25),
        ("Q-V3-COV-103", "M3", "quantum-coverage-csharp-a", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack A spanning RNG, hash, cipher, key, and validation callback families.", by_language.get("csharp", []), 25),
        ("Q-V3-COV-104", "M3", "quantum-coverage-csharp-b", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.", by_language.get("csharp", [])[25:], 25),
        ("Q-V3-COV-105", "M3", "quantum-coverage-java-c", "Java / hybrid coverage pack", "Java crypto coverage pack C targeting remaining weak hash, cipher, JWT, XMLDSIG, and inventory families.", by_language.get("java", [])[50:], 30),
        ("Q-V3-COV-106", "M3", "quantum-coverage-java-d", "Java / hybrid coverage pack", "Java crypto coverage pack D targeting additional RSA/ECDSA, TLS, and key-material rule families.", by_language.get("java", [])[80:], 30),
        ("Q-V3-COV-107", "M3", "quantum-coverage-csharp-c", "C# / hybrid coverage pack", "C# crypto and TLS coverage pack C targeting additional delegate, provider, inventory, and weak primitive families.", by_language.get("csharp", [])[50:], 30),
        ("Q-V3-COV-108", "M3", "quantum-coverage-java-e", "Java / hybrid coverage pack", "Java crypto coverage pack E targeting late-slice Java rule families that remained uncovered after the earlier campaign waves.", by_language.get("java", [])[110:], 30),
        ("Q-V4-COV-101", "M4", "quantum-coverage-python-a", "Python / hybrid coverage pack", "Python crypto coverage pack A spanning hashlib, HMAC, secrets, JWT, and key-material rule families.", by_language.get("python", []), 20),
        ("Q-V4-COV-102", "M4", "quantum-coverage-python-b", "Python / hybrid coverage pack", "Python crypto coverage pack B extending TLS wrappers, kwargs passthrough, and legacy inventory families.", by_language.get("python", [])[20:], 20),
        ("Q-V4-COV-103", "M4", "quantum-coverage-polyglot-web", "TypeScript / JavaScript / Go coverage pack", "Polyglot web coverage pack spanning Node, TypeScript, JavaScript, and Go crypto/TLS families.", by_language.get("typescript", []) + by_language.get("javascript", []) + by_language.get("go", []), 30),
        ("Q-V4-COV-104", "M4", "quantum-coverage-python-c", "Python / hybrid coverage pack", "Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.", by_language.get("python", [])[40:], 30),
        ("Q-V6-COV-101", "M6", "quantum-coverage-config", "Config / infra coverage pack", "Config-heavy quantum coverage pack spanning Envoy, Nginx, Apache, SSH, kube, JVM, and OpenSSL families.", by_language.get("config", []), 20),
        ("M-V8-COV-101", "M8", "quantum-coverage-native-a", "Native / mixed coverage pack", "Mixed native coverage pack A spanning Kotlin, Scala, Groovy, Ruby, Swift, C, and C++ rule families.", native_rules, 30),
        ("M-V8-COV-102", "M8", "quantum-coverage-native-b", "Native / mixed coverage pack", "Mixed native coverage pack B extending shell, PowerShell, PHP, Objective-C, Rust, Erlang, SQL, and workflow-adjacent rule families.", native_rules[30:], 30),
        ("M-V8-COV-103", "M8", "quantum-coverage-native-c", "Native / mixed coverage pack", "Mixed native coverage pack C extending remaining lesser-exercised native and scripting rule families.", native_rules[60:], 30),
        ("M-V8-COV-104", "M8", "quantum-coverage-native-d", "Native / mixed coverage pack", "Mixed native coverage pack D targeting additional Kotlin, Scala, Ruby, Rust, and C-family rule families.", native_rules[90:], 30),
        ("M-V8-COV-105", "M8", "quantum-coverage-native-e", "Native / mixed coverage pack", "Mixed native coverage pack E targeting remaining native and scripting quantum families that were still uncovered after earlier waves.", native_rules[120:], 30),
        ("M-V8-COV-106", "M8", "quantum-coverage-native-f", "Native / mixed coverage pack", "Mixed native coverage pack F targeting the tail of the native and scripting rule catalog to close the remaining surfaced-coverage gap.", native_rules[150:], 30),
    ]

    for scenario_id, milestone, repo_name, stack, domain, source_rows, limit in quantum_pack_defs:
        chunk = source_rows[:limit]
        if not chunk:
            continue
        entries = []
        pack_slug = repo_name.replace("_", "-")
        for index, rule in enumerate(chunk, start=1):
            path = _quantum_path(rule["language"], pack_slug, index, rule)
            entries.append(
                {
                    **rule,
                    "path": path,
                    "content": _entry_content({**rule, "path": path}),
                }
            )
        descriptors.append(
            _build_descriptor(
                scenario_id=scenario_id,
                milestone=milestone,
                repo_name=repo_name,
                module="quantum",
                stack=stack,
                domain=domain,
                summary=f"Quantum coverage bundle exercising {len(entries)} distinct rule candidates across {stack.lower()}.",
                scan_kind="quantum",
                entries=entries,
                line_target="7000-10000",
            )
        )

    return descriptors
