from __future__ import annotations

from pathlib import Path

import pytest

from tooling.env import load_config
from tooling.coverage_campaign import coverage_campaign_descriptors
from tooling.git_factory import GitFactory
from tooling.repo_builders import materialize_scenario
from tooling.scenarios import scenario_index, scenario_specs
from tooling.utils import run_command


NEW_SCENARIO_IDS = {
    "G-V2-HIST-006",
    "G-V2-HIST-007",
    "G-V2-HIST-008",
    "G-V2-HIST-009",
    "Q-V3-JAVA-005",
    "Q-V3-JAVA-006",
    "Q-V3-CS-004",
    "Q-V4-PY-005",
    "Q-V4-TS-005",
    "Q-V4-GO-003",
    "Q-V5-JAVA-005",
    "Q-V5-JAVA-006",
    "Q-V5-PY-003",
    "Q-V6-TS-002",
    "Q-V6-CS-003",
    "Q-V6-CONFIG-005",
    "N-V7-DOCS-009",
    "N-V7-DOCS-010",
    "N-V7-VENDOR-011",
    "N-V7-SAFE-012",
    "M-V8-005",
    "M-V8-006",
    "M-V8-007",
    "M-V8-008",
    "G-V2-HIST-014",
    "G-V2-HIST-015",
    "G-V2-HIST-016",
    "G-V2-HIST-017",
    "Q-V3-JAVA-007",
    "Q-V3-JAVA-008",
    "Q-V3-CS-005",
    "Q-V4-PY-006",
    "Q-V4-TS-006",
    "Q-V4-GO-004",
    "Q-V5-JAVA-007",
    "Q-V5-JAVA-008",
    "Q-V5-PY-004",
    "Q-V6-TS-004",
    "Q-V6-CS-004",
    "Q-V6-CONFIG-006",
    "N-V7-DOCS-013",
    "N-V7-VENDOR-014",
    "N-V7-TESTS-015",
    "N-V7-SAFE-016",
    "M-V8-009",
    "M-V8-010",
    "M-V8-011",
    "M-V8-012",
    "G-V1-COV-101",
    "G-V1-COV-102",
    "G-V1-COV-103",
    "G-V1-COV-104",
    "G-V1-COV-105",
    "Q-V3-COV-101",
    "Q-V3-COV-102",
    "Q-V3-COV-103",
    "Q-V3-COV-104",
    "Q-V3-COV-105",
    "Q-V3-COV-106",
    "Q-V3-COV-107",
    "Q-V3-COV-108",
    "Q-V4-COV-101",
    "Q-V4-COV-102",
    "Q-V4-COV-103",
    "Q-V4-COV-104",
    "Q-V6-COV-101",
    "M-V8-COV-101",
    "M-V8-COV-102",
    "M-V8-COV-103",
    "M-V8-COV-104",
    "M-V8-COV-105",
    "M-V8-COV-106",
    "G-V1-COV-106",
    "G-V1-COV-107",
    "G-V1-COV-108",
    "G-V1-COV-109",
    "G-V1-COV-110",
    "G-V1-COV-111",
    "G-V1-COV-112",
    "Q-V3-COV-109",
    "Q-V3-COV-110",
    "Q-V3-COV-111",
    "Q-V3-COV-112",
    "Q-V3-COV-113",
    "Q-V4-COV-105",
    "Q-V4-COV-106",
    "Q-V4-COV-107",
    "Q-V4-COV-108",
    "Q-V4-COV-109",
    "Q-V6-COV-102",
    "M-V8-COV-107",
    "M-V8-COV-108",
}


def _config(tmp_path: Path):
    (tmp_path / ".env").write_text(
        "\n".join(
            [
                "ARQ_API_BASE_URL=http://localhost:8080",
                "ARQ_WORKSPACE_KEY=default",
                "ARQ_EMAIL=admin",
                "ARQ_PASSWORD=admin",
                "GIT_OWNER=ARQ-Sec",
                "REPOSITORIES_ROOT=repositories",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return load_config(tmp_path)


def test_scenario_specs_include_24_new_ids_and_minimum_suite_size() -> None:
    ids = [scenario.id for scenario in scenario_specs()]

    assert len(ids) == len(set(ids))
    assert len(ids) >= 127
    assert NEW_SCENARIO_IDS.issubset(ids)


def test_scenario_specs_can_freeze_to_original_85_with_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ARQ_SCENARIO_SET", "frozen85")
    ids = [scenario.id for scenario in scenario_specs()]
    assert len(ids) == 85
    assert all("COV" not in scenario_id for scenario_id in ids)


def test_materialize_new_mixed_monorepo_variants_with_history_and_negative_surfaces(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    repo_root_005, _ = materialize_scenario(config, scenarios["M-V8-005"], git_factory)
    assert (repo_root_005 / "vendor" / "third-party-sdk.js").exists()
    assert (repo_root_005 / "generated" / "openapi" / "mesh-client.ts").exists()
    assert (repo_root_005 / "packages" / "shared-fixtures" / "seed.json").exists()

    repo_root_007, _ = materialize_scenario(config, scenarios["M-V8-007"], git_factory)
    assert not (repo_root_007 / "shared" / "config" / "legacy.env").exists()
    branches = git_factory.branch_shas(repo_root_007)
    assert {"main", "feature/shared-lib-cleanup", "release/2026.05"}.issubset(branches)
    history = run_command(["git", "log", "--all", "--name-only", "--", "shared/config/legacy.env"], repo_root_007, check=True)
    assert "shared/config/legacy.env" in history.stdout


def test_materialize_new_mixed_infra_variants_with_overlay_noise_and_branches(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    repo_root_006, _ = materialize_scenario(config, scenarios["M-V8-006"], git_factory)
    assert (repo_root_006 / "deploy" / "examples" / "envoy.yaml").exists()
    assert (repo_root_006 / "kustomize" / "fixtures" / "dev.env").exists()
    assert (repo_root_006 / ".github" / "workflows" / "deploy.yml").exists()

    repo_root_008, _ = materialize_scenario(config, scenarios["M-V8-008"], git_factory)
    branches = git_factory.branch_shas(repo_root_008)
    assert {"main", "feature/hotfix-ssl", "release/2026.04", "feature/charts-cleanup"}.issubset(branches)
    assert (repo_root_008 / "deploy" / "examples" / "envoy.yaml").exists()
    assert (repo_root_008 / "generated" / "manifests" / "envoy-example.yaml").exists()


def test_materialize_history_cherrypick_wave_creates_expected_branches(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenario = scenario_index()["G-V2-HIST-007"]

    repo_root, _ = materialize_scenario(config, scenario, git_factory)

    branches = git_factory.branch_shas(repo_root)
    assert {"main", "feature/customer-hotfix", "release/2026.05", "hotfix/cherry-picked-docs"}.issubset(branches)
    assert not (repo_root / "src" / "modules" / "partner" / "bootstrap" / "featureBranchToken.ts").exists()
    history = run_command(["git", "log", "hotfix/cherry-picked-docs", "--name-only", "--", "docs/branch-chore.md"], repo_root, check=True)
    assert "docs/branch-chore.md" in history.stdout


def test_materialize_new_history_and_discovery_wave_variants(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    split_root, _ = materialize_scenario(config, scenarios["G-V2-HIST-014"], git_factory)
    split_history = run_command(["git", "log", "--all", "--name-only", "--", "src/modules/partner/bootstrap/partnerSecret.ts"], split_root, check=True)
    assert "partnerSecret.ts" in split_history.stdout

    branch_root, _ = materialize_scenario(config, scenarios["G-V2-HIST-015"], git_factory)
    branches = git_factory.branch_shas(branch_root)
    assert {"main", "feature/private-key-hotfix", "release/2026.06"}.issubset(branches)

    folded_root, _ = materialize_scenario(config, scenarios["G-V2-HIST-016"], git_factory)
    folded_history = run_command(["git", "log", "--all", "-p", "--", "ops/runtime/runtime-values.yaml"], folded_root, check=True)
    assert "Ab9K2mQ7pL4xR8nT5vW1Yz7Ck3Hs6Fq2" in folded_history.stdout

    config_root, _ = materialize_scenario(config, scenarios["Q-V6-CONFIG-006"], git_factory)
    assert (config_root / "deploy" / "live" / "envoy.yaml").exists()
    assert (config_root / "runtime" / "live.env").exists()

    csharp_root, _ = materialize_scenario(config, scenarios["Q-V3-CS-005"], git_factory)
    digest_inventory = (csharp_root / "src" / "Library" / "Security" / "DigestInventoryCatalog.cs").read_text(encoding="utf-8")
    assert "new Random().Next(" not in digest_inventory
    assert "nameof(Random)" in digest_inventory

    go_root, _ = materialize_scenario(config, scenarios["Q-V4-GO-004"], git_factory)
    helper_hash = (go_root / "internal" / "security" / "helper_hash.go").read_text(encoding="utf-8")
    assert "import (" in helper_hash
    assert "\"hash\"" in helper_hash
    assert "func() hash.Hash" in helper_hash


def test_materialize_new_discovery_mixed_repo_variants(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    repo_root_009, _ = materialize_scenario(config, scenarios["M-V8-009"], git_factory)
    assert (repo_root_009 / "generated" / "openapi" / "payments-client.ts").exists()
    assert (repo_root_009 / "vendor" / "sdk" / "payments-sdk.js").exists()

    repo_root_010, _ = materialize_scenario(config, scenarios["M-V8-010"], git_factory)
    assert (repo_root_010 / "generated" / "manifests" / "envoy-example.yaml").exists()
    assert (repo_root_010 / "docs" / "infra" / "discovery-wave.md").exists()

    repo_root_011, _ = materialize_scenario(config, scenarios["M-V8-011"], git_factory)
    history = run_command(["git", "log", "--all", "--name-only", "--", "shared/config/legacy.env"], repo_root_011, check=True)
    assert "shared/config/legacy.env" in history.stdout

    repo_root_012, _ = materialize_scenario(config, scenarios["M-V8-012"], git_factory)
    assert (repo_root_012 / "apps" / "admin-api" / "src" / "modules" / "security" / "secureTlsWrapper.ts").exists()


def test_materialize_guardian_and_quantum_coverage_bundles(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    guardian_root, guardian_meta = materialize_scenario(config, scenarios["G-V1-COV-101"], git_factory)
    assert guardian_meta["builderMetadata"]["generatedRuleCount"] == 20
    assert (guardian_root / "integrations" / "guardian-coverage-saas" / "runtime" / "provider_001.env").exists()
    assert (guardian_root / ".github" / "workflows" / "deploy.yml").exists()

    quantum_root, quantum_meta = materialize_scenario(config, scenarios["Q-V3-COV-101"], git_factory)
    assert quantum_meta["builderMetadata"]["generatedRuleCount"] == 25
    assert (quantum_root / "services" / "quantum-coverage-java-a" / "src" / "legacy" / "Rule001.java").exists()
    assert (quantum_root / "vendor" / "generated-client.txt").exists()
    assert "<maven.compiler.release>" in (quantum_root / "pom.xml").read_text(encoding="utf-8")


def test_materialize_quantum_java_late_slice_uses_statement_terminated_exact_anchors(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    quantum_root, _ = materialize_scenario(config, scenarios["Q-V3-COV-105"], git_factory)

    aead_bc = (
        quantum_root
        / "services"
        / "quantum-coverage-java-c"
        / "src"
        / "legacy"
        / "Rule013.java"
    ).read_text(encoding="utf-8")
    aead_jca = (
        quantum_root
        / "services"
        / "quantum-coverage-java-c"
        / "src"
        / "legacy"
        / "Rule014.java"
    ).read_text(encoding="utf-8")
    keygen_bc = (
        quantum_root
        / "services"
        / "quantum-coverage-java-c"
        / "src"
        / "legacy"
        / "Rule020.java"
    ).read_text(encoding="utf-8")

    assert 'Cipher.getInstance("ChaCha20-Poly1305");' in aead_bc
    assert 'Cipher.getInstance("ChaCha20-Poly1305");' in aead_jca
    assert 'KeyPairGenerator.getInstance("Ed25519");' in keygen_bc


def test_materialize_quantum_native_bundle_wraps_code_like_languages(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    native_root, _ = materialize_scenario(config, scenarios["M-V8-COV-101"], git_factory)

    kotlin_file = next(native_root.rglob("*.kt"))
    scala_file = next(native_root.rglob("*.scala"))
    assert "package legacy.coverage" in kotlin_file.read_text(encoding="utf-8")
    assert "@JvmStatic fun execute()" in kotlin_file.read_text(encoding="utf-8")
    assert "object " in scala_file.read_text(encoding="utf-8")

    extra_guardian_root, extra_guardian_meta = materialize_scenario(config, scenarios["G-V1-COV-106"], git_factory)
    assert extra_guardian_meta["builderMetadata"]["generatedRuleCount"] > 0
    assert (extra_guardian_root / ".github" / "workflows" / "deploy.yml").exists()

    extra_quantum_root, extra_quantum_meta = materialize_scenario(config, scenarios["Q-V3-COV-109"], git_factory)
    assert extra_quantum_meta["builderMetadata"]["generatedRuleCount"] > 0
    assert extra_quantum_root.exists()


def test_materialize_quantum_java_bundle_uses_rule_specific_curve_and_tls_calls(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    quantum_root, _ = materialize_scenario(config, scenarios["Q-V3-COV-101"], git_factory)

    ec_curve = (
        quantum_root
        / "services"
        / "quantum-coverage-java-a"
        / "src"
        / "legacy"
        / "Rule001.java"
    ).read_text(encoding="utf-8")
    tls_protocol = (
        quantum_root
        / "services"
        / "quantum-coverage-java-a"
        / "src"
        / "legacy"
        / "Rule014.java"
    ).read_text(encoding="utf-8")

    assert 'KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");' in ec_curve
    assert 'kpg.initialize(new ECGenParameterSpec("prime192v1"));' in ec_curve
    assert 'SSLContext.getInstance("TLSv1");' in tls_protocol


def test_materialize_quantum_python_bundle_uses_minimal_imports_and_exact_ssl_signals(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    quantum_root, _ = materialize_scenario(config, scenarios["Q-V4-COV-101"], git_factory)

    ssl_rule = (
        quantum_root
        / "workers"
        / "quantum-coverage-python-a"
        / "app"
        / "legacy"
        / "rule_002.py"
    ).read_text(encoding="utf-8")
    ecb_rule = (
        quantum_root
        / "workers"
        / "quantum-coverage-python-a"
        / "app"
        / "legacy"
        / "rule_004.py"
    ).read_text(encoding="utf-8")

    assert "import ssl" in ssl_rule
    assert "ctx.verify_mode = ssl.CERT_NONE" in ssl_rule
    assert "import random" not in ecb_rule
    assert "from Crypto.Cipher import AES" in ecb_rule
    assert "requires-python" in (quantum_root / "pyproject.toml").read_text(encoding="utf-8")


def test_materialize_quantum_csharp_bundle_uses_rule_specific_crypto_constructs(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    quantum_root, _ = materialize_scenario(config, scenarios["Q-V3-COV-103"], git_factory)

    md5_rule = (
        quantum_root
        / "services"
        / "quantum-coverage-csharp-a"
        / "src"
        / "legacy"
        / "Rule003.cs"
    ).read_text(encoding="utf-8")
    ecb_rule = (
        quantum_root
        / "services"
        / "quantum-coverage-csharp-a"
        / "src"
        / "legacy"
        / "Rule004.cs"
    ).read_text(encoding="utf-8")

    assert "new MD5CryptoServiceProvider();" in md5_rule
    assert "var alg = new RijndaelManaged { Mode = CipherMode.ECB };" in ecb_rule
    assert "<TargetFramework>" in (quantum_root / "CoverageContext.csproj").read_text(encoding="utf-8")


def test_materialize_quantum_polyglot_bundle_emits_node_project_context(tmp_path: Path) -> None:
    config = _config(tmp_path)
    git_factory = GitFactory(workspace_root=config.lab_root)
    scenarios = scenario_index()

    quantum_root, _ = materialize_scenario(config, scenarios["Q-V4-COV-103"], git_factory)

    package_json = (quantum_root / "package.json").read_text(encoding="utf-8")
    assert "\"engines\"" in package_json
    assert "\"node\"" in package_json


def test_coverage_campaign_descriptors_include_manifest_and_key_material_paths() -> None:
    entries = [
        entry
        for descriptor in coverage_campaign_descriptors()
        for entry in descriptor["metadata"]["coverageBundle"]["entries"]
    ]
    assert any(entry["path"].endswith("pom.xml") for entry in entries)
    assert any(entry["path"].endswith(".pem") for entry in entries)


def test_coverage_campaign_descriptors_include_version_sliced_precision_wave() -> None:
    descriptors = {descriptor["id"]: descriptor for descriptor in coverage_campaign_descriptors()}

    assert "Q-V3-COV-201" in descriptors
    assert "Q-V4-COV-201" in descriptors
    assert "Q-V6-COV-201" in descriptors
    assert "M-V8-COV-201" in descriptors
    assert "version-sliced precision coverage pack" in descriptors["Q-V3-COV-201"]["domain"]


def test_guardian_coverage_descriptors_use_deterministic_overrides_for_problematic_rules() -> None:
    entries = {
        entry["rule_key"]: entry
        for descriptor in coverage_campaign_descriptors()
        if descriptor["id"].startswith("G-V1-COV-")
        for entry in descriptor["metadata"]["coverageBundle"]["entries"]
    }

    assert entries["guardian.slack-webhook-url"]["sample"] == "https://hooks.slack.com/services/" + ("A" * 43)
    assert entries["guardian.sidekiq-sensitive-url"]["sample"] == "https://deadbeef:cafebabe@gems.contribsys.com"
    assert entries["guardian.pkcs12-file"]["path"].endswith(".p12")
    assert entries["guardian.freemius-secret-key"]["path"].endswith(".php")
    assert entries["guardian.hashicorp-tf-password"]["path"].endswith(".tf")
    assert entries["guardian.kubernetes-secret-yaml"]["path"].endswith(".yaml")
    assert entries["guardian.nuget-config-password"]["path"].endswith("nuget.config")
    assert "kind: Secret" in entries["guardian.kubernetes-secret-yaml"]["sample"]
