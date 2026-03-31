from __future__ import annotations

from .models import BuildPlan, ExpectedAbsent, ExpectedFinding, ExplainabilityExpectation, ScanPlan, ScenarioSpec


def _build_plan(plan: BuildPlan) -> BuildPlan:
    return BuildPlan(
        build=[command[:] for command in plan.build],
        test=[command[:] for command in plan.test],
        smoke=[command[:] for command in plan.smoke],
    )


def ef(
    key: str,
    path_contains: str,
    *,
    rule: str | None = None,
    resolved: str | None = None,
    query_family: str | None = None,
    branch: str | None = None,
    present_on_head: bool | None = None,
    present_in_history: bool | None = None,
    exposure_scope: str | None = None,
    finding_kind: str | None = None,
    detection_source: str | None = None,
) -> ExpectedFinding:
    return ExpectedFinding(
        key=key,
        path_contains=path_contains,
        rule_key_contains=rule,
        resolved_value_contains=resolved,
        query_family_contains=query_family,
        branch_name=branch,
        present_on_head=present_on_head,
        present_in_history=present_in_history,
        exposure_scope=exposure_scope,
        finding_kind=finding_kind,
        detection_source=detection_source,
    )


def ea(key: str, path_contains: str, *, rule: str | None = None, resolved: str | None = None) -> ExpectedAbsent:
    return ExpectedAbsent(key=key, path_contains=path_contains, rule_key_contains=rule, resolved_value_contains=resolved)


def ee(
    key: str,
    path_contains: str,
    *,
    resolved: str | None = None,
    query_family: str | None = None,
    resolution_scope: str | None = None,
    detection_source: str | None = None,
) -> ExplainabilityExpectation:
    return ExplainabilityExpectation(
        key=key,
        path_contains=path_contains,
        resolved_value_contains=resolved,
        query_family_contains=query_family,
        resolution_scope_contains=resolution_scope,
        detection_source_contains=detection_source,
    )


JAVA_BUILD = BuildPlan(
    build=[["mvn", "-q", "-DskipTests", "compile"]],
    test=[["mvn", "-q", "test"]],
    smoke=[["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/smoke.ps1"]],
)

PYTHON_BUILD = BuildPlan(
    build=[["python", "-m", "compileall", "app", "tests", "scripts"]],
    test=[["python", "-m", "pytest", "-q"]],
    smoke=[["python", "scripts/smoke.py"]],
)

NODE_BUILD = BuildPlan(
    build=[["npm", "install", "--silent"], ["npm", "run", "build"]],
    test=[["npm", "test", "--", "--runInBand"]],
    smoke=[["node", "dist/scripts/smoke.js"]],
)

CONFIG_BUILD = BuildPlan(
    build=[["python", "scripts/validate_repo.py"]],
    test=[["python", "-m", "pytest", "-q"]],
    smoke=[["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/smoke.ps1"]],
)

CSHARP_BUILD = BuildPlan(
    build=[["dotnet", "restore", "src/AppHost/AppHost.csproj"], ["dotnet", "build", "src/AppHost/AppHost.csproj", "-c", "Release"]],
    test=[["dotnet", "test", "tests/AppHost.Tests/AppHost.Tests.csproj", "-c", "Release", "--no-build"]],
    smoke=[["dotnet", "run", "--project", "src/AppHost/AppHost.csproj", "--", "--smoke"]],
)

GO_BUILD = BuildPlan(
    build=[["go", "test", "./...", "-run", "TestBuildSmoke", "-count=1"]],
    test=[["go", "test", "./...", "-count=1"]],
    smoke=[["go", "run", "./cmd/service", "--smoke"]],
)

NEGATIVE_PY_BUILD = BuildPlan(
    build=[["python", "-m", "compileall", "app", "tests", "scripts"]],
    test=[["python", "-m", "pytest", "-q"]],
    smoke=[["python", "scripts/smoke.py"]],
)

MIXED_MONOREPO_BUILD = BuildPlan(
    build=[
        ["mvn", "-q", "-f", "services/platform-java/pom.xml", "-DskipTests", "compile"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'apps/admin-api'; npm install --silent"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'apps/admin-api'; npm run build"],
        ["python", "-m", "compileall", "workers/sync-worker/app", "workers/sync-worker/tests", "workers/sync-worker/scripts"],
    ],
    test=[
        ["mvn", "-q", "-f", "services/platform-java/pom.xml", "test"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'apps/admin-api'; npm test -- --runInBand"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'workers/sync-worker'; python -m pytest -q tests"],
    ],
    smoke=[["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/smoke.ps1"]],
)

INFRA_MIXED_BUILD = BuildPlan(
    build=[
        ["python", "-m", "compileall", "app", "tests", "scripts"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'ops/console'; npm install --silent"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'ops/console'; npm run build"],
    ],
    test=[
        ["python", "-m", "pytest", "-q", "tests"],
        ["powershell", "-NoProfile", "-Command", "Set-Location 'ops/console'; npm test -- --runInBand"],
    ],
    smoke=[["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts/smoke.ps1"]],
)


def _guardian_head(name: str = "guardian-head") -> list[ScanPlan]:
    return [ScanPlan(name=name, modules=["guardian"], scan_mode="HEAD_SNAPSHOT", branch_scope="SINGLE_BRANCH", ref_name="main")]


def _guardian_history(include_all_branches: bool = False) -> list[ScanPlan]:
    plans = [
        ScanPlan(name="guardian-head-main", modules=["guardian"], scan_mode="HEAD_SNAPSHOT", branch_scope="SINGLE_BRANCH", ref_name="main"),
        ScanPlan(name="guardian-ref-history-main", modules=["guardian"], scan_mode="REF_HISTORY", branch_scope="SINGLE_BRANCH", ref_name="main"),
    ]
    if include_all_branches:
        plans.append(ScanPlan(name="guardian-all-branches", modules=["guardian"], scan_mode="HEAD_SNAPSHOT", branch_scope="ALL_BRANCHES", ref_name=None))
    return plans


def _quantum_head(name: str = "quantum-head") -> list[ScanPlan]:
    return [ScanPlan(name=name, modules=["quantum"], scan_mode="HEAD_SNAPSHOT", branch_scope="SINGLE_BRANCH", ref_name="main")]


def _both_head(include_history: bool = False, include_all_branches: bool = False) -> list[ScanPlan]:
    plans = [
        ScanPlan(name="guardian-head-main", modules=["guardian"], scan_mode="HEAD_SNAPSHOT", branch_scope="SINGLE_BRANCH", ref_name="main"),
        ScanPlan(name="quantum-head-main", modules=["quantum"], scan_mode="HEAD_SNAPSHOT", branch_scope="SINGLE_BRANCH", ref_name="main"),
    ]
    if include_history:
        plans.append(ScanPlan(name="guardian-ref-history-main", modules=["guardian"], scan_mode="REF_HISTORY", branch_scope="SINGLE_BRANCH", ref_name="main"))
    if include_all_branches:
        plans.append(ScanPlan(name="guardian-all-branches", modules=["guardian"], scan_mode="HEAD_SNAPSHOT", branch_scope="ALL_BRANCHES", ref_name=None))
    return plans


def milestone_order() -> list[str]:
    return [f"M{i}" for i in range(1, 10)]


def scenario_specs() -> list[ScenarioSpec]:
    specs: list[ScenarioSpec] = [
        ScenarioSpec(
            id="G-V1-JAVA-001",
            milestone="M1",
            repo_name="payments-service-java",
            module="guardian",
            family="guardian_live_java",
            stack="Java / Spring Boot / Maven",
            domain="Partner settlement and payout service.",
            summary="Guardian live secret surfaces in a realistic Java payments service.",
            line_target="5000-9000",
            scan_plans=_guardian_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("prod-secret", "src/main/resources/application-prod.yml", rule="guardian.generic-api-key"),
                ef("private-key", "src/main/resources/keys/partner_rsa.pem", rule="guardian.private-key"),
                ef("bootstrap-key", "PartnerCredentialBootstrap.java", rule="guardian.generic-api-key"),
                ef("seed-token", "src/main/resources/db/seed/live-connector.properties", rule="guardian.generic-api-key"),
            ],
            expected_absent=[
                ea("readme-example", "README.md"),
                ea("masked-runbook", "docs/operational-runbook.md"),
                ea("test-example", "src/test/resources/example.env"),
                ea("pem-doc-example", "docs/examples/pem-example.txt"),
            ],
        ),
        ScenarioSpec(
            id="G-V1-PY-002",
            milestone="M1",
            repo_name="notification-worker-python",
            module="guardian",
            family="guardian_live_python",
            stack="Python / FastAPI worker",
            domain="Notification dispatch and webhook worker.",
            summary="Guardian live secret surfaces in a realistic Python notification worker.",
            line_target="5000-8000",
            scan_plans=_guardian_head(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef("runtime-token", "app/config/runtime_settings.py", rule="guardian.generic-api-key"),
                ef("prod-env", "deploy/k8s/notification-prod.env", rule="guardian.generic-api-key"),
                ef("webhook-key", "app/clients/webhook_client.py", rule="guardian.generic-api-key"),
                ef("jwt-secret", "app/security/jwt_bootstrap.py", rule="guardian.generic-api-key"),
            ],
            expected_absent=[
                ea("fixture-json", "tests/fixtures/sample_payload.json"),
                ea("local-docs", "docs/local-dev.md"),
                ea("env-example", ".env.example"),
            ],
        ),
        ScenarioSpec(
            id="G-V1-TS-003",
            milestone="M1",
            repo_name="partner-api-node",
            module="guardian",
            family="guardian_live_node",
            stack="TypeScript / Express",
            domain="Partner onboarding and credential provisioning API.",
            summary="Guardian live secret surfaces in a realistic TypeScript partner API.",
            line_target="5000-8000",
            scan_plans=_guardian_head(),
            build_plan=_build_plan(NODE_BUILD),
            expected_findings=[
                ef("active-secret", "src/config/secrets.ts", rule="guardian.generic-api-key"),
                ef("prod-json", "config/production.json", rule="guardian.generic-api-key"),
                ef("key-material", "partnerKeyLoader.ts", rule="guardian.private-key"),
                ef("bootstrap-script", "scripts/bootstrap-partner.ts", rule="guardian.generic-api-key"),
            ],
            expected_absent=[
                ea("readme-quickstart", "README.md"),
                ea("sample-webhooks", "docs/sample-webhooks.md"),
                ea("test-fixtures", "__tests__/fixtures"),
                ea("env-example", ".env.example"),
            ],
        ),
        ScenarioSpec(
            id="G-V1-CONFIG-004",
            milestone="M1",
            repo_name="legacy-admin-config",
            module="guardian",
            family="guardian_live_config",
            stack="Config-heavy repo",
            domain="Legacy admin portal and provisioning configuration.",
            summary="Guardian live secret surfaces in a config-heavy operations repository.",
            line_target="5000-7000",
            scan_plans=_guardian_head(),
            build_plan=_build_plan(CONFIG_BUILD),
            expected_findings=[
                ef("ops-runtime", "config/runtime/admin-prod.yaml", rule="guardian.generic-api-key"),
                ef("service-account", "ops/runtime/portal.env", rule="guardian.generic-api-key"),
                ef("private-key", "config/keys/admin_portal.pem", rule="guardian.private-key"),
                ef("active-properties", "deploy/prod/admin.properties", rule="guardian.generic-api-key"),
            ],
            expected_absent=[
                ea("sample-tfvars", "terraform/sample.tfvars"),
                ea("template-docs", "docs/templates"),
                ea("examples", "examples"),
            ],
        ),
        ScenarioSpec(
            id="G-V2-HIST-001",
            milestone="M2",
            repo_name="payments-history-lineage",
            module="guardian",
            family="guardian_history_java",
            stack="Java / Spring Boot",
            domain="Payments repo with a history-only secret on main.",
            summary="Guardian history-only secret exposure modelling on main branch.",
            line_target="5000-9000",
            scan_plans=_guardian_history(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef(
                    "history-only-token",
                    "PartnerTokenArchive.java",
                    rule="guardian.generic-api-key",
                    present_on_head=False,
                    present_in_history=True,
                    exposure_scope="HISTORY_ONLY",
                    branch="main",
                )
            ],
            expected_absent=[
                ea("masked-readme", "README.md"),
                ea("fixture-log", "src/test/resources/fixtures"),
            ],
            metadata={"commitPlan": ["c001", "c002", "c003", "c004", "c005"]},
        ),
        ScenarioSpec(
            id="G-V2-HIST-002",
            milestone="M2",
            repo_name="partner-branch-divergence",
            module="guardian",
            family="guardian_history_node",
            stack="TypeScript / Node",
            domain="Branch divergence with main clean and feature branch leaked.",
            summary="Guardian single-branch versus all-branches branch divergence handling.",
            line_target="5000-8000",
            scan_plans=_guardian_history(include_all_branches=True),
            build_plan=_build_plan(NODE_BUILD),
            expected_findings=[
                ef("feature-branch-secret", "src/modules/partner/bootstrap/branchLeak.ts", rule="guardian.generic-api-key", branch="feature/partner-hotfix"),
            ],
            expected_absent=[
                ea("main-clean", "src/modules/partner/bootstrap/mainSafe.ts"),
                ea("docs-refresh", "docs/branch-notes.md"),
            ],
            metadata={"branches": ["main", "feature/partner-hotfix", "release/2026.04", "feature/docs-refresh"]},
        ),
        ScenarioSpec(
            id="G-V2-HIST-003",
            milestone="M2",
            repo_name="pem-rotation-lineage",
            module="guardian",
            family="guardian_history_python",
            stack="Python + ops config",
            domain="PEM rotation and dedup lineage validation.",
            summary="Guardian PEM rotation, canonicalization and dedup continuity.",
            line_target="5000-8000",
            scan_plans=_guardian_history(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef(
                    "rotated-key-a",
                    "ops/keys/service-a.pem",
                    rule="guardian.private-key",
                    present_on_head=False,
                    present_in_history=True,
                    exposure_scope="HISTORY_ONLY",
                ),
                ef(
                    "rotated-key-b",
                    "ops/keys/service-b.pem",
                    rule="guardian.private-key",
                    present_on_head=True,
                    present_in_history=True,
                    exposure_scope="HEAD_AND_HISTORY",
                ),
            ],
            expected_absent=[ea("docs-pem-example", "docs/examples/pem-reference.md")],
            metadata={"commitPlan": ["c001", "c002", "c003", "c004", "c005", "c006"]},
        ),
        ScenarioSpec(
            id="Q-V3-JAVA-001",
            milestone="M3",
            repo_name="identity-gateway-java",
            module="quantum",
            family="quantum_crypto_java",
            stack="Java / Spring Boot",
            domain="Identity gateway for sessions and partner auth.",
            summary="Quantum weak crypto patterns in Java identity services.",
            line_target="5000-10000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("md5", "LegacyDigestService.java", resolved="MD5"),
                ef("sha1", "LegacyDigestService.java", resolved="SHA-1"),
                ef("aes-ecb", "TokenCipherService.java", resolved="AES/ECB/PKCS5Padding"),
            ],
            expected_absent=[
                ea("secure-hash-helper", "SecureDigestService.java"),
                ea("docs-snippet", "docs/legacy-notes.md"),
                ea("tests-legacy", "LegacyDigestServiceTest.java"),
            ],
            explainability_expectations=[
                ee("md5", "LegacyDigestService.java", resolved="MD5", query_family="jca", resolution_scope="SAME_METHOD"),
                ee("sha1", "LegacyDigestService.java", resolved="SHA-1", query_family="jca"),
                ee("aes-ecb", "TokenCipherService.java", resolved="AES/ECB/PKCS5Padding", query_family="jca"),
            ],
        ),
        ScenarioSpec(
            id="Q-V3-JAVA-002",
            milestone="M3",
            repo_name="legacy-payment-crypto-java",
            module="quantum",
            family="quantum_crypto_java",
            stack="Java / Spring Boot",
            domain="Legacy payment encryption and key management helpers.",
            summary="Quantum weak crypto patterns in legacy Java payment utilities.",
            line_target="5000-10000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("desede", "LegacyEnvelopeCipher.java", resolved="DESede/ECB/PKCS5Padding"),
                ef("aes-ecb", "BatchReconciliationCipher.java", resolved="AES/ECB"),
            ],
            expected_absent=[
                ea("migration-docs", "docs/migration-guide.md"),
                ea("secure-replacement", "SecureEnvelopeCipher.java"),
            ],
            explainability_expectations=[
                ee("desede", "LegacyEnvelopeCipher.java", resolved="DESede/ECB/PKCS5Padding"),
                ee("aes-ecb", "BatchReconciliationCipher.java", resolved="AES/ECB"),
            ],
        ),
        ScenarioSpec(
            id="Q-V3-CS-003",
            milestone="M3",
            repo_name="billing-sdk-csharp",
            module="quantum",
            family="quantum_crypto_csharp",
            stack="C# / .NET 8",
            domain="Billing SDK and token signing library.",
            summary="Quantum weak crypto patterns in a realistic C# billing SDK.",
            line_target="5000-10000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(CSHARP_BUILD),
            expected_findings=[
                ef("md5", "LegacyHashService.cs", resolved="MD5"),
                ef("sha1", "LegacyHashService.cs", resolved="SHA1"),
                ef("ecb", "LegacyCipherService.cs", resolved="ECB"),
            ],
            expected_absent=[
                ea("safe-rng", "SecureOtpTokenService.cs"),
                ea("docs", "docs/legacy-samples.md"),
            ],
            explainability_expectations=[
                ee("md5", "LegacyHashService.cs", resolved="MD5", query_family="csharp"),
                ee("sha1", "LegacyHashService.cs", resolved="SHA1"),
                ee("ecb", "LegacyCipherService.cs", resolved="ECB"),
            ],
        ),
        ScenarioSpec(
            id="Q-V4-PY-001",
            milestone="M4",
            repo_name="notification-signer-python",
            module="quantum",
            family="quantum_crypto_python",
            stack="Python / FastAPI",
            domain="Webhook signing and outbound notification auth helper.",
            summary="Quantum weak crypto patterns in Python signing helpers.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef("md5", "legacy_signature.py", resolved="MD5"),
                ef("weak-token", "token_factory.py", resolved="random"),
            ],
            expected_absent=[
                ea("secure-sha256", "secure_signature.py"),
                ea("docs", "docs/algorithm-notes.md"),
                ea("fixtures", "tests/fixtures"),
            ],
            explainability_expectations=[
                ee("md5", "legacy_signature.py", resolved="MD5", query_family="python"),
                ee("weak-token", "token_factory.py", resolved="random"),
            ],
        ),
        ScenarioSpec(
            id="Q-V4-GO-002",
            milestone="M4",
            repo_name="device-provisioning-go",
            module="quantum",
            family="quantum_crypto_go",
            stack="Go",
            domain="Device bootstrap credential service.",
            summary="Quantum weak crypto patterns in a realistic Go provisioning service.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(GO_BUILD),
            expected_findings=[
                ef("md5", "legacy_hash.go", resolved="MD5"),
                ef("sha1", "legacy_hash.go", resolved="SHA1"),
            ],
            expected_absent=[
                ea("secure-hmac", "secure_hmac.go"),
                ea("docs", "docs/compatibility-notes.md"),
            ],
            explainability_expectations=[
                ee("md5", "legacy_hash.go", resolved="MD5", query_family="go"),
                ee("sha1", "legacy_hash.go", resolved="SHA1"),
            ],
        ),
        ScenarioSpec(
            id="Q-V4-TS-003",
            milestone="M4",
            repo_name="customer-portal-node",
            module="quantum",
            family="quantum_crypto_node",
            stack="TypeScript / Node",
            domain="Customer portal backend for resets and signed links.",
            summary="Quantum weak crypto patterns in a realistic Node portal backend.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(NODE_BUILD),
            expected_findings=[
                ef("md5", "legacyDigest.ts", resolved="MD5"),
            ],
            expected_absent=[
                ea("secure-digest", "secureDigest.ts"),
                ea("readme", "README.md"),
                ea("test-only", "__tests__/"),
            ],
            explainability_expectations=[
                ee("md5", "legacyDigest.ts", resolved="MD5", query_family="typescript"),
            ],
        ),
        ScenarioSpec(
            id="Q-V5-JAVA-001",
            milestone="M5",
            repo_name="partner-client-java",
            module="quantum",
            family="quantum_tls_java",
            stack="Java / Spring Boot",
            domain="External partner API client and settlement sync service.",
            summary="Quantum TLS trust bypass patterns in Java HTTP clients.",
            line_target="5000-9000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("trust-all", "InsecureTrustManager.java", resolved="X509TrustManager"),
                ef("hostname-bypass", "InsecureHostnameVerifier.java"),
            ],
            expected_absent=[
                ea("safe-client", "SecurePartnerClientFactory.java"),
                ea("test-bypass", "src/test/java"),
            ],
            explainability_expectations=[
                ee("trust-all", "InsecureTrustManager.java", resolved="X509TrustManager", query_family="tls"),
                ee("hostname-bypass", "InsecureHostnameVerifier.java", query_family="tls"),
            ],
        ),
        ScenarioSpec(
            id="Q-V5-PY-002",
            milestone="M5",
            repo_name="data-sync-python",
            module="quantum",
            family="quantum_tls_python",
            stack="Python / worker service",
            domain="Data sync worker pulling partner APIs and webhooks.",
            summary="Quantum TLS trust bypass patterns in Python clients.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef("verify-false", "partner_pull_client.py", resolved="verify=False"),
                ef("unverified-context", "unverified_ssl_context.py", resolved="ssl._create_unverified_context"),
            ],
            expected_absent=[
                ea("trusted-ca", "secure_partner_pull_client.py"),
                ea("docs", "docs/tls-notes.md"),
            ],
            explainability_expectations=[
                ee("verify-false", "partner_pull_client.py", resolved="verify=False", query_family="ssl"),
                ee("unverified-context", "unverified_ssl_context.py", resolved="ssl._create_unverified_context"),
            ],
        ),
        ScenarioSpec(
            id="Q-V5-JAVA-003",
            milestone="M5",
            repo_name="gateway-config-java",
            module="quantum",
            family="quantum_tls_java_config",
            stack="Java + config wiring",
            domain="Gateway service with environment-driven HTTP client settings.",
            summary="Quantum runtime-wired TLS config misuse in a Java gateway service.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("runtime-trust-bypass", "PartnerTlsProperties.java"),
                ef("trust-manager-bypass", "PartnerTrustManager.java"),
            ],
            expected_absent=[
                ea("dev-only-safe", "application-dev.yml"),
                ea("commented-example", "docs/profile-matrix.md"),
            ],
        ),
        ScenarioSpec(
            id="Q-V6-TS-001",
            milestone="M6",
            repo_name="customer-portal-node-tls",
            module="quantum",
            family="quantum_tls_node",
            stack="TypeScript / Node",
            domain="Customer portal calling billing and profile APIs.",
            summary="Quantum TLS trust bypass patterns in Node HTTP clients.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(NODE_BUILD),
            expected_findings=[
                ef("reject-unauthorized", "insecureAgentFactory.ts", resolved="rejectUnauthorized"),
                ef("axios-insecure", "insecureBillingClient.ts", resolved="rejectUnauthorized"),
            ],
            expected_absent=[
                ea("safe-wrapper", "secureAgentFactory.ts"),
                ea("readme", "README.md"),
            ],
            explainability_expectations=[
                ee("reject-unauthorized", "insecureAgentFactory.ts", resolved="rejectUnauthorized", query_family="typescript"),
                ee("axios-insecure", "insecureBillingClient.ts", resolved="rejectUnauthorized"),
            ],
        ),
        ScenarioSpec(
            id="Q-V6-CS-002",
            milestone="M6",
            repo_name="admin-integrations-csharp",
            module="quantum",
            family="quantum_tls_csharp",
            stack="C# / .NET 8",
            domain="Admin integration service consuming partner APIs.",
            summary="Quantum trust bypass patterns in C# HttpClient registration.",
            line_target="5000-9000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(CSHARP_BUILD),
            expected_findings=[
                ef("accept-any-cert", "InsecurePartnerClientRegistration.cs", resolved="DangerousAcceptAnyServerCertificateValidator"),
            ],
            expected_absent=[
                ea("safe-factory", "SecurePartnerClientRegistration.cs"),
                ea("docs", "docs/httpclient-registration.md"),
            ],
            explainability_expectations=[
                ee("accept-any-cert", "InsecurePartnerClientRegistration.cs", resolved="DangerousAcceptAnyServerCertificateValidator", query_family="csharp"),
            ],
        ),
        ScenarioSpec(
            id="Q-V6-CONFIG-003",
            milestone="M6",
            repo_name="edge-gateway-config",
            module="quantum",
            family="quantum_tls_config",
            stack="Config-heavy repo",
            domain="Edge gateway deployment and runtime config.",
            summary="Quantum active runtime TLS config misuse versus dormant examples.",
            line_target="5000-7000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(CONFIG_BUILD),
            expected_findings=[
                ef("envoy-untrusted", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ef("node-env-disable", "runtime/.env", resolved="NODE_TLS_REJECT_UNAUTHORIZED=0"),
            ],
            expected_absent=[
                ea("sample-values", "helm/examples"),
                ea("safe-comment", "docs/safe-overrides.md"),
            ],
            explainability_expectations=[
                ee("envoy-untrusted", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ee("node-env-disable", "runtime/.env", resolved="NODE_TLS_REJECT_UNAUTHORIZED=0"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-DOCS-001",
            milestone="M7",
            repo_name="docs-samples-repo",
            module="both",
            family="negative_docs",
            stack="Docs / snippets",
            domain="Documentation-heavy repository with example snippets only.",
            summary="Adversarial docs-only surfaces should stay clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("docs-secret", "docs/runbooks"),
                ea("docs-pem", "docs/security"),
                ea("docs-tls", "docs/examples"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-VENDOR-002",
            milestone="M7",
            repo_name="vendor-generated-repo",
            module="both",
            family="negative_vendor",
            stack="Vendor / generated",
            domain="Vendor/generated repository with boilerplate and copied samples.",
            summary="Generated and vendor noise should stay clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("vendor-dir", "vendor/"),
                ea("generated-dir", "generated/"),
                ea("bundle-dir", "bundles/"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-TESTS-003",
            milestone="M7",
            repo_name="test-mocks-repo",
            module="both",
            family="negative_tests",
            stack="Tests / fixtures",
            domain="Test-only fixtures and insecure-looking mocks.",
            summary="Tests, mocks and fixtures should stay clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("tests-only", "tests/"),
                ea("fixtures-only", "fixtures/"),
                ea("mock-certs", "mocks/certificates"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-SAFE-004",
            milestone="M7",
            repo_name="safe-wrapper-playground",
            module="both",
            family="negative_safe",
            stack="Secure wrappers",
            domain="Secure wrapper playground with scary naming but safe implementation.",
            summary="Secure wrappers should stay clean despite naming traps.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("safe-hash", "secure_hashing.py"),
                ea("safe-tls", "secure_tls.py"),
                ea("safe-key-loading", "secure_key_loader.py"),
            ],
        ),
        ScenarioSpec(
            id="M-V8-001",
            milestone="M8",
            repo_name="internal-platform-monorepo",
            module="both",
            family="mixed_monorepo",
            stack="Java + Node + Python monorepo",
            domain="Internal platform monorepo with multiple tech stacks.",
            summary="Mixed enterprise monorepo with both Guardian and Quantum signals.",
            line_target="10000-20000",
            scan_plans=_both_head(),
            build_plan=_build_plan(MIXED_MONOREPO_BUILD),
            expected_findings=[
                ef("guardian-java-secret", "application-prod.yml", rule="guardian.generic-api-key"),
                ef("guardian-python-key", "runtime_secret.py", rule="guardian.generic-api-key"),
                ef("guardian-private-key", "platform_service.pem", rule="guardian.private-key"),
                ef("quantum-java-ecb", "LegacyCipherService.java", resolved="AES/ECB/PKCS5Padding"),
                ef("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
                ef("quantum-python-verify-false", "insecure_partner.py", resolved="verify=False"),
            ],
            expected_absent=[
                ea("vendor", "vendor/"),
                ea("docs", "docs/examples"),
                ea("tests", "workers/sync-worker/tests"),
            ],
            explainability_expectations=[
                ee("quantum-java-ecb", "LegacyCipherService.java", resolved="AES/ECB/PKCS5Padding"),
                ee("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
                ee("quantum-python-verify-false", "insecure_partner.py", resolved="verify=False"),
            ],
        ),
        ScenarioSpec(
            id="M-V8-002",
            milestone="M8",
            repo_name="infra-app-mixed-repo",
            module="both",
            family="mixed_infra_repo",
            stack="App + infra + CI",
            domain="Infra-heavy app repository with hotfix and release branch.",
            summary="Mixed infra/application repository with Guardian and Quantum across app and config.",
            line_target="8000-15000",
            scan_plans=_both_head(include_history=True, include_all_branches=True),
            build_plan=_build_plan(INFRA_MIXED_BUILD),
            expected_findings=[
                ef("guardian-active-secret", "production.env", rule="guardian.generic-api-key"),
                ef("guardian-hotfix-secret", "feature-secret.txt", rule="guardian.generic-api-key", branch="feature/hotfix-ssl"),
                ef("quantum-config-trust", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ef("quantum-app-md5", "legacyDigest.ts", resolved="MD5"),
            ],
            expected_absent=[
                ea("release-branch-clean", "release-notes.md"),
                ea("docs", "docs/"),
            ],
            explainability_expectations=[
                ee("quantum-config-trust", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ee("quantum-app-md5", "legacyDigest.ts", resolved="MD5"),
            ],
            metadata={"branches": ["main", "feature/hotfix-ssl", "release/2026.04"]},
        ),
        ScenarioSpec(
            id="G-V2-HIST-004",
            milestone="M2",
            repo_name="partner-rename-lineage",
            module="guardian",
            family="guardian_history_java",
            stack="Java / Spring Boot",
            domain="Partner bootstrap repo with rename, move, and revert history around a transient secret.",
            summary="Guardian history handling for renamed and moved secret-bearing files on main.",
            line_target="5000-9000",
            scan_plans=_guardian_history(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef(
                    "history-renamed-secret",
                    "PartnerCredentialArchive.java",
                    rule="guardian.generic-api-key",
                    present_on_head=False,
                    present_in_history=True,
                    exposure_scope="HISTORY_ONLY",
                    branch="main",
                )
            ],
            expected_absent=[
                ea("rename-runbook", "docs/rename-plan.md"),
                ea("moved-fixture", "src/test/resources/fixtures"),
            ],
            metadata={"commitPlan": ["c001", "c002", "c003", "c004", "c005", "c006"]},
        ),
        ScenarioSpec(
            id="G-V2-HIST-005",
            milestone="M2",
            repo_name="canonical-secret-lineage",
            module="guardian",
            family="guardian_history_python",
            stack="Python + ops runtime",
            domain="Runtime token lineage with formatting changes and dedup-like history on main.",
            summary="Guardian history handling when the same secret is reformatted, moved, and later removed.",
            line_target="5000-8000",
            scan_plans=_guardian_history(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef(
                    "history-runtime-token",
                    "partner_runtime.env",
                    rule="guardian.generic-api-key",
                    present_on_head=False,
                    present_in_history=True,
                    exposure_scope="HISTORY_ONLY",
                    branch="main",
                )
            ],
            expected_absent=[
                ea("docs-token-example", "docs/examples/runtime-reference.md"),
                ea("safe-state", "app/security/rotation_state.py"),
            ],
            metadata={"commitPlan": ["c001", "c002", "c003", "c004", "c005", "c006"]},
        ),
        ScenarioSpec(
            id="Q-V3-JAVA-004",
            milestone="M3",
            repo_name="crypto-import-only-java",
            module="quantum",
            family="quantum_crypto_java",
            stack="Java / Spring Boot",
            domain="Java request-signing module with one actionable weakness and multiple import-only traps.",
            summary="Quantum precision around import-only crypto inventory versus real weak-hash usage in Java.",
            line_target="5000-9000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("md5-request-signer", "LegacyRequestSigner.java", resolved="MD5"),
            ],
            expected_absent=[
                ea("import-only-registry", "DigestInventoryRegistry.java"),
                ea("secure-wrapper", "ScaryButSafeDigestFacade.java"),
                ea("docs", "docs/request-signing-notes.md"),
            ],
            explainability_expectations=[
                ee("md5-request-signer", "LegacyRequestSigner.java", resolved="MD5", query_family="jca"),
            ],
        ),
        ScenarioSpec(
            id="Q-V4-PY-004",
            milestone="M4",
            repo_name="wrapper-safe-python",
            module="quantum",
            family="quantum_crypto_python",
            stack="Python / service helper library",
            domain="Python utility repo with scary naming, import-only crypto references, and one real weak RNG path.",
            summary="Quantum precision for Python wrapper-safe surfaces versus actionable weak RNG calls.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(PYTHON_BUILD),
            expected_findings=[
                ef("weak-reset-token", "legacy_nonce.py", resolved="random"),
            ],
            expected_absent=[
                ea("safe-wrapper", "scary_random_wrapper.py"),
                ea("import-catalog", "hash_inventory.py"),
                ea("docs", "docs/crypto-guidance.md"),
            ],
            explainability_expectations=[
                ee("weak-reset-token", "legacy_nonce.py", resolved="random", query_family="python"),
            ],
        ),
        ScenarioSpec(
            id="Q-V5-JAVA-004",
            milestone="M5",
            repo_name="tls-builder-chain-java",
            module="quantum",
            family="quantum_tls_java",
            stack="Java / Spring Boot",
            domain="Partner TLS builder chain with aliasing, wrappers, and one live insecure path.",
            summary="Quantum builder-chain and wrapper precision for Java TLS trust-bypass flows.",
            line_target="5000-9000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(JAVA_BUILD),
            expected_findings=[
                ef("builder-hostname-bypass", "PartnerTlsBuilder.java", resolved="HostnameVerifier-return-true"),
                ef("builder-trust-bypass", "BuilderTrustManager.java", resolved="X509TrustManager"),
            ],
            expected_absent=[
                ea("safe-builder", "SafePartnerTlsBuilder.java"),
                ea("docs", "docs/tls-builder-notes.md"),
            ],
            explainability_expectations=[
                ee("builder-hostname-bypass", "PartnerTlsBuilder.java", resolved="HostnameVerifier-return-true", query_family="java"),
                ee("builder-trust-bypass", "BuilderTrustManager.java", resolved="X509TrustManager", query_family="java"),
            ],
        ),
        ScenarioSpec(
            id="Q-V6-CONFIG-004",
            milestone="M6",
            repo_name="runtime-config-separation",
            module="quantum",
            family="quantum_tls_config",
            stack="Config-heavy repo",
            domain="Infra config repo with active insecure runtime config and dormant examples/comments nearby.",
            summary="Quantum precision for active runtime config versus examples, comments, and fixtures in config-heavy repos.",
            line_target="5000-8000",
            scan_plans=_quantum_head(),
            build_plan=_build_plan(CONFIG_BUILD),
            expected_findings=[
                ef("active-envoy-untrusted", "deploy/live/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ef("active-node-disable", "runtime/.env", resolved="NODE_TLS_REJECT_UNAUTHORIZED=0"),
            ],
            expected_absent=[
                ea("example-values", "helm/examples"),
                ea("commented-runbook", "docs/runtime-notes.md"),
                ea("fixture-env", "tests/fixtures"),
            ],
            explainability_expectations=[
                ee("active-envoy-untrusted", "deploy/live/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ee("active-node-disable", "runtime/.env", resolved="NODE_TLS_REJECT_UNAUTHORIZED=0"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-DOCS-005",
            milestone="M7",
            repo_name="tutorial-examples-repo",
            module="both",
            family="negative_docs",
            stack="Docs / tutorials",
            domain="Tutorial-heavy repo with placeholder secrets and insecure-looking snippets that are explicitly non-live.",
            summary="Docs/tutorial repos with placeholder secrets should remain clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("tutorial-secret", "docs/tutorials"),
                ea("quickstart-env", "examples/quickstart"),
                ea("snippet-tls", "docs/snippets"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-DOCS-006",
            milestone="M7",
            repo_name="certificate-chain-repo",
            module="both",
            family="negative_docs",
            stack="Docs / PKI samples",
            domain="PKI documentation repo with public cert chains, CSRs, and safe explanatory PEM material.",
            summary="Certificate chains and CSRs without private keys should remain clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("public-chain", "docs/certs"),
                ea("csr-example", "examples/csr"),
                ea("pki-runbook", "docs/pki"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-VENDOR-007",
            milestone="M7",
            repo_name="bundle-lockfile-repo",
            module="both",
            family="negative_vendor",
            stack="Vendor / generated / lockfile",
            domain="Dependency-heavy repo with bundled artifacts, generated code, and lockfiles containing secret-looking strings.",
            summary="Vendor, generated, and lockfile noise should remain clean.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("vendor-bundles", "vendor/"),
                ea("generated-openapi", "generated/openapi"),
                ea("lockfile-noise", "package-lock.json"),
            ],
        ),
        ScenarioSpec(
            id="N-V7-SAFE-008",
            milestone="M7",
            repo_name="masked-placeholder-repo",
            module="both",
            family="negative_safe",
            stack="Safe wrappers / masked placeholders",
            domain="Operational helper repo with masked, placeholder, and high-entropy-looking values that are explicitly non-live.",
            summary="Masked placeholders and safe wrappers should remain clean despite high-entropy-looking strings.",
            line_target="5000-7000",
            scan_plans=_both_head(),
            build_plan=_build_plan(NEGATIVE_PY_BUILD),
            expected_absent=[
                ea("masked-values", "masked_values.py"),
                ea("placeholder-env", "placeholder_env.py"),
                ea("safe-commentary", "docs/safe-placeholders.md"),
            ],
        ),
        ScenarioSpec(
            id="M-V8-003",
            milestone="M8",
            repo_name="platform-mesh-monorepo",
            module="both",
            family="mixed_monorepo",
            stack="Java + Node + Python + generated/vendor monorepo",
            domain="Enterprise mesh monorepo with apps, services, vendor bundles, openapi output, and fixture-heavy packages.",
            summary="Mixed monorepo with actionable findings and deliberate protected-negative surfaces across apps, libs, charts, and generated code.",
            line_target="10000-20000",
            scan_plans=_both_head(),
            build_plan=_build_plan(MIXED_MONOREPO_BUILD),
            expected_findings=[
                ef("guardian-java-secret", "application-prod.yml", rule="guardian.generic-api-key"),
                ef("guardian-private-key", "mesh_service.pem", rule="guardian.private-key"),
                ef("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
                ef("quantum-python-verify-false", "insecure_partner.py", resolved="verify=False"),
            ],
            expected_absent=[
                ea("vendor", "vendor/"),
                ea("generated-openapi", "generated/openapi"),
                ea("fixtures", "packages/shared-fixtures"),
            ],
            explainability_expectations=[
                ee("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
                ee("quantum-python-verify-false", "insecure_partner.py", resolved="verify=False"),
            ],
        ),
        ScenarioSpec(
            id="M-V8-004",
            milestone="M8",
            repo_name="control-plane-infra-repo",
            module="both",
            family="mixed_infra_repo",
            stack="App + infra + helm + kustomize + terraform + CI",
            domain="Control-plane repo with live infra config, hotfix branches, CI workflows, and example overlays.",
            summary="Infra-heavy mixed repo with active insecure runtime config, branch divergence, and numerous protected-negative surfaces.",
            line_target="9000-16000",
            scan_plans=_both_head(include_history=True, include_all_branches=True),
            build_plan=_build_plan(INFRA_MIXED_BUILD),
            expected_findings=[
                ef("guardian-active-secret", "production.env", rule="guardian.generic-api-key"),
                ef("guardian-hotfix-secret", "feature-secret.txt", rule="guardian.generic-api-key", branch="feature/hotfix-ssl"),
                ef("quantum-config-trust", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ef("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
            ],
            expected_absent=[
                ea("examples", "deploy/examples"),
                ea("kustomize-fixtures", "kustomize/fixtures"),
                ea("release-clean", "release-notes.md"),
            ],
            explainability_expectations=[
                ee("quantum-config-trust", "deploy/envoy.yaml", resolved="ACCEPT_UNTRUSTED"),
                ee("quantum-node-md5", "legacyDigest.ts", resolved="MD5"),
            ],
            metadata={"branches": ["main", "feature/hotfix-ssl", "release/2026.04", "feature/charts-cleanup"]},
        ),
    ]
    return specs


def milestone_specs(milestone: str) -> list[ScenarioSpec]:
    return [scenario for scenario in scenario_specs() if scenario.milestone == milestone]


def scenario_index() -> dict[str, ScenarioSpec]:
    return {scenario.id: scenario for scenario in scenario_specs()}
