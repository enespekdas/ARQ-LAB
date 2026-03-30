# Scenario Matrix

## M1 — Guardian realistic live surfaces

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| G-V1-JAVA-001 | payments-service-java | guardian | Java / Spring Boot / PostgreSQL | hardcoded client secret, private key PEM, generic API key |
| G-V1-PY-002 | notification-worker-python | guardian | Python / FastAPI / Celery-like worker | runtime token, real-looking DSN/token in active settings |
| G-V1-TS-003 | partner-api-node | guardian | TypeScript / NestJS or Express | live config secret, production JSON key, certificate/key material |
| G-V1-CONFIG-004 | legacy-admin-config | guardian | Config-heavy repo / YAML / properties / shell / terraform | ops config secret, live properties secret, private key |

## M2 — Guardian history ref-state dedup

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| G-V2-HIST-001 | payments-history-lineage | guardian | Java / Spring Boot | history only |
| G-V2-HIST-002 | partner-branch-divergence | guardian | Node / TypeScript | all branches vs single branch |
| G-V2-HIST-003 | pem-rotation-lineage | guardian | Python + ops config | rotation, canonicalization, dedup |

## M3 — Quantum weak crypto Java CSharp

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| Q-V3-JAVA-001 | identity-gateway-java | quantum | Java / Spring Boot | MD5, SHA1, ECB, legacy KDF |
| Q-V3-JAVA-002 | legacy-payment-crypto-java | quantum | Java / Spring Boot | DES/3DES, PBEWithMD5AndDES, weak keystore patterns |
| Q-V3-CS-003 | billing-sdk-csharp | quantum | C# / .NET | MD5.Create, SHA1.Create, ECB, Random() in security path |

## M4 — Quantum weak crypto Python Go Node

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| Q-V4-PY-001 | notification-signer-python | quantum | Python / FastAPI | hashlib.md5, weak token generation |
| Q-V4-GO-002 | device-provisioning-go | quantum | Go | md5/sha1, weak PBKDF2, insecure auth helper |
| Q-V4-TS-003 | customer-portal-node | quantum | TypeScript / Node | md5, Math.random security misuse, aes-128-ecb |

## M5 — Quantum TLS trust config Java Python

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| Q-V5-JAVA-001 | partner-client-java | quantum | Java / Spring Boot | trust-all manager, hostname verification off |
| Q-V5-PY-002 | data-sync-python | quantum | Python / FastAPI worker | verify=False, ssl context disable |
| Q-V5-JAVA-003 | gateway-config-java | quantum | Java + config wiring | insecure TLS config wired via YAML/properties |

## M6 — Quantum TLS trust config Node CSharp Config

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| Q-V6-TS-001 | customer-portal-node-tls | quantum | TypeScript / Node | rejectUnauthorized false |
| Q-V6-CS-002 | admin-integrations-csharp | quantum | C# / .NET | ServerCertificateCustomValidationCallback bypass |
| Q-V6-CONFIG-003 | edge-gateway-config | quantum | Config-heavy repo | inventory-only vs runtime-wired insecure config |

## M7 — Adversarial negatives

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| N-V7-DOCS-001 | docs-samples-repo | both | Docs/snippets | docs should stay clean |
| N-V7-VENDOR-002 | vendor-generated-repo | both | vendor/generated | generated noise suppression |
| N-V7-TESTS-003 | test-mocks-repo | both | tests/fixtures | test-only insecure-looking code |
| N-V7-SAFE-004 | safe-wrapper-playground | both | safe wrappers | secure patterns should stay clean |

## M8 — Mixed enterprise repos

| Scenario ID | Repo | Module | Stack | Focus |
|---|---|---|---|---|
| M-V8-001 | internal-platform-monorepo | both | Java + Node + Python monorepo | mixed findings with bounded noise |
| M-V8-002 | infra-app-mixed-repo | both | App + infra + CI | app and config together |
