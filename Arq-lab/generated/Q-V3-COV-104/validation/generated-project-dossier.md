# Generated Project Dossier - Q-V3-COV-104

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-104`
- scenarioName: Quantum coverage bundle exercising 25 distinct rule candidates across c# / hybrid coverage pack.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `C# / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-csharp-b`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-104\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-104.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.` as a `C# / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 25 distinct rule candidates across c# / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `secrets/quantum-coverage-csharp-b/keys/rule_024.pem, services/quantum-coverage-csharp-b/src/legacy/Rule001.cs, services/quantum-coverage-csharp-b/src/legacy/Rule002.cs, services/quantum-coverage-csharp-b/src/legacy/Rule003.cs, services/quantum-coverage-csharp-b/src/legacy/Rule004.cs, services/quantum-coverage-csharp-b/src/legacy/Rule005.cs, services/quantum-coverage-csharp-b/src/legacy/Rule006.cs, services/quantum-coverage-csharp-b/src/legacy/Rule007.cs, services/quantum-coverage-csharp-b/src/legacy/Rule008.cs, services/quantum-coverage-csharp-b/src/legacy/Rule009.cs, services/quantum-coverage-csharp-b/src/legacy/Rule010.cs, services/quantum-coverage-csharp-b/src/legacy/Rule011.cs, services/quantum-coverage-csharp-b/src/legacy/Rule012.cs, services/quantum-coverage-csharp-b/src/legacy/Rule013.cs, services/quantum-coverage-csharp-b/src/legacy/Rule014.cs, services/quantum-coverage-csharp-b/src/legacy/Rule015.cs, services/quantum-coverage-csharp-b/src/legacy/Rule016.cs, services/quantum-coverage-csharp-b/src/legacy/Rule017.cs, services/quantum-coverage-csharp-b/src/legacy/Rule018.cs, services/quantum-coverage-csharp-b/src/legacy/Rule019.cs, services/quantum-coverage-csharp-b/src/legacy/Rule020.cs, services/quantum-coverage-csharp-b/src/legacy/Rule021.cs, services/quantum-coverage-csharp-b/src/legacy/Rule022.cs, services/quantum-coverage-csharp-b/src/legacy/Rule023.cs, services/quantum-coverage-csharp-b/src/legacy/Rule025.cs`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md, ops/playbooks/runbook-02.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-csharp-b
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- config
|   `-- runtime
|       `-- baseline.yaml
|-- deploy
|   `-- prod
|       `-- service.properties
|-- docs
|   |-- architecture
|   |   |-- section-01.md
|   |   |-- section-02.md
|   |   |-- section-03.md
|   |   |-- section-04.md
|   |   |-- section-05.md
|   |   |-- section-06.md
|   |   |-- section-07.md
|   |   `-- section-08.md
|   `-- coverage-notes.md
|-- ops
|   `-- playbooks
|       |-- runbook-01.md
|       |-- runbook-02.md
|       |-- runbook-03.md
|       |-- runbook-04.md
|       |-- runbook-05.md
|       |-- runbook-06.md
|       |-- runbook-07.md
|       `-- runbook-08.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- secrets
|   `-- quantum-coverage-csharp-b
|       `-- keys
|           `-- rule_024.pem
|-- services
|   `-- quantum-coverage-csharp-b
|       `-- src
|           `-- legacy
|               |-- Rule001.cs
|               |-- Rule002.cs
|               |-- Rule003.cs
|               |-- Rule004.cs
|               |-- Rule005.cs
|               |-- Rule006.cs
|               |-- Rule007.cs
|               |-- Rule008.cs
|               |-- Rule009.cs
|               |-- Rule010.cs
|               |-- Rule011.cs
|               |-- Rule012.cs
|               |-- Rule013.cs
|               |-- Rule014.cs
|               |-- Rule015.cs
|               |-- Rule016.cs
|               |-- Rule017.cs
|               |-- Rule018.cs
|               |-- Rule019.cs
|               |-- Rule020.cs
|               |-- Rule021.cs
|               |-- Rule022.cs
|               |-- Rule023.cs
|               `-- Rule025.cs
|-- sql
|   `-- reference
|       |-- reference-01.sql
|       |-- reference-02.sql
|       |-- reference-03.sql
|       |-- reference-04.sql
|       |-- reference-05.sql
|       |-- reference-06.sql
|       |-- reference-07.sql
|       `-- reference-08.sql
|-- tests
|   |-- fixtures
|   |   `-- sample-placeholder.txt
|   `-- test_validation.py
|-- validation
|   |-- runnability-logs
|   |   |-- build-01.log
|   |   |-- smoke-01.log
|   |   `-- test-01.log
|   |-- branch-plan.yaml
|   |-- expected-absent.json
|   |-- expected-findings.json
|   |-- expected-report.md
|   |-- generated-file-manifest.json
|   |-- generated-project-dossier.md
|   |-- generated-tree.txt
|   |-- repo-metadata.json
|   |-- scenario.yaml
|   `-- smoke.yaml
|-- vendor
|   `-- generated-client.txt
|-- .gitignore
|-- CoverageContext.csproj
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .github/workflows/deploy.yml | live-config | 7 | Runtime configuration carrying environment or deployment settings for Deploy. | no | no | no | yes | yes | no |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | yes | no |
| CoverageContext.csproj | build/deploy | 5 | Build or deployment definition shaping how Coverage Context is compiled, packaged, or released. | no | no | no | yes | yes | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| config/runtime/baseline.yaml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Baseline. | no | no | no | yes | yes | no |
| deploy/prod/service.properties | live-config | 1 | Runtime configuration carrying environment or deployment settings for Service. | no | no | no | yes | yes | no |
| docs/architecture/section-01.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-02.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-03.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-04.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-05.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-06.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-07.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-08.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-08.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-csharp-b/keys/rule_024.pem | generated | 14 | Generated or derived project artifact related to Rule 024. | yes | no | yes | no | no | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule001.cs | live-code | 12 | Runtime business module contributing to Rule001. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule002.cs | live-code | 12 | Runtime business module contributing to Rule002. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule003.cs | live-code | 11 | Runtime business module contributing to Rule003. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule004.cs | live-code | 12 | Runtime business module contributing to Rule004. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule005.cs | live-code | 13 | Runtime business module contributing to Rule005. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule006.cs | live-code | 12 | Runtime business module contributing to Rule006. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule007.cs | live-code | 13 | Runtime business module contributing to Rule007. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule008.cs | live-code | 12 | Runtime business module contributing to Rule008. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule009.cs | live-code | 11 | Runtime business module contributing to Rule009. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule010.cs | live-code | 12 | Runtime business module contributing to Rule010. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule011.cs | live-code | 12 | Runtime business module contributing to Rule011. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule012.cs | live-code | 11 | Runtime business module contributing to Rule012. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule013.cs | live-code | 12 | Runtime business module contributing to Rule013. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule014.cs | live-code | 13 | Runtime business module contributing to Rule014. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule015.cs | live-code | 12 | Runtime business module contributing to Rule015. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule016.cs | live-code | 11 | Runtime business module contributing to Rule016. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule017.cs | live-code | 14 | Runtime business module contributing to Rule017. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule018.cs | live-code | 12 | Runtime business module contributing to Rule018. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule019.cs | live-code | 11 | Runtime business module contributing to Rule019. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule020.cs | live-code | 12 | Runtime business module contributing to Rule020. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule021.cs | live-code | 12 | Runtime business module contributing to Rule021. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule022.cs | live-code | 11 | Runtime business module contributing to Rule022. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule023.cs | live-code | 12 | Runtime business module contributing to Rule023. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-b/src/legacy/Rule025.cs | live-code | 11 | Runtime business module contributing to Rule025. | yes | no | no | yes | yes | no |
| sql/reference/reference-01.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-02.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-03.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-04.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-05.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-06.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-07.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-08.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 327 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 1038 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1027 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 100 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule001.cs`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0441-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule002.cs`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0442-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule003.cs`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0443-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule004.cs`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0444-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule005.cs`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0445-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule006.cs`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0448-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule007.cs`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0450-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule008.cs`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0451-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule009.cs`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0454-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule010.cs`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0456-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule011.cs`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0459-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule012.cs`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0460-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule013.cs`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0461-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule014.cs`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0462-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule015.cs`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0464-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule016.cs`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0465-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule017.cs`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0467-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule018.cs`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0470-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule019.cs`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0473-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule020.cs`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0475-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule021.cs`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0478-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule022.cs`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0479-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule023.cs`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0481-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-csharp-b/keys/rule_024.pem`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0482-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-b/src/legacy/Rule025.cs`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0486-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `services/quantum-coverage-csharp-b/src/legacy/Rule001.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule003.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule006.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule008.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule009.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule010.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule011.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule012.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule014.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule015.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule018.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule019.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule020.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule021.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-b/src/legacy/Rule022.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

## 8. Protected Negative Surfaces

| path | classification | why protected |
| --- | --- | --- |
| docs/architecture/section-01.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-02.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-03.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-04.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-05.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-06.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-07.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-08.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-csharp-b/keys/rule_024.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-01.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-02.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-03.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-04.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-05.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-06.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-07.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-08.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/fixtures/sample-placeholder.txt | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_validation.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/branch-plan.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-absent.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-findings.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-report.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-file-manifest.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-project-dossier.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-tree.txt | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/repo-metadata.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/smoke-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/scenario.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/smoke.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| vendor/generated-client.txt | vendor | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |

## 9. Branch and Commit Plan

Snapshot-only scenario. No branch divergence or history-only contract is intended beyond the default branch head scan.

## 10. Runnability Contract

### Build

- Command: `C:\Python313\python.EXE scripts/validate_repo.py`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-csharp-b
0002: 
0003: C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-csharp-b/keys/rule_024.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 024. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0482-csharp
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: -------BEGIN                             EC                            PRIVATE        KEY-------------------------------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule001.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0441-csharp
0007:         // evidence_anchor: PasswordDeriveBytes
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule002.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0442-csharp
0007:         // evidence_anchor: Rfc2898DeriveBytes
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule003.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0443-csharp
0006:         // evidence_anchor: new Random(), System.Random
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule004.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0444-csharp
0007:         // evidence_anchor: .Key =, .IV =
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule005.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0006:     public static void Execute() {
0007:         // rule_key: quantum.arq-q-0445-csharp
0008:         // evidence_anchor: X509Certificate2, password
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule006.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0448-csharp
0007:         // evidence_anchor: ServicePointManager.SecurityProtocol
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule007.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0006:     public static void Execute() {
0007:         // rule_key: quantum.arq-q-0450-csharp
0008:         // evidence_anchor: SslStream, RemoteCertificateValidationCallback
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule008.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0451-csharp
0007:         // evidence_anchor: MD5.Create, MD5CryptoServiceProvider
0008:         // regex_sample: MD5CryptoServiceProvider
0009:         // keywords: MD5.Create | MD5CryptoServiceProvider
0010:         MD5.Create();
0011:     }
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule009.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0454-csharp
0006:         // evidence_anchor: TripleDES.Create, DES.Create
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule010.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0456-csharp
0007:         // evidence_anchor: RSAEncryptionPadding.Pkcs1
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule011.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0459-csharp
0007:         // evidence_anchor: Rfc2898DeriveBytes
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule012.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0460-csharp
0006:         // evidence_anchor: new Random()
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule013.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0461-csharp
0007:         // evidence_anchor: .Key =, .IV =
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule014.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0006:     public static void Execute() {
0007:         // rule_key: quantum.arq-q-0462-csharp
0008:         // evidence_anchor: X509Certificate2, password
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule015.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0464-csharp
0007:         // evidence_anchor: DangerousAcceptAnyServerCertificateValidator
0008:         // regex_sample: DangerousAcceptAnyServerCertificateValidator
0009:         // keywords: DangerousAcceptAnyServerCertificateValidator
0010:         handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;
0011:     }
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule016.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0465-csharp
0006:         // evidence_anchor: SslClientAuthenticationOptions, EnabledSslProtocols, SslProtocols
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule017.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0007:     public static void Execute() {
0008:         // rule_key: quantum.arq-q-0467-csharp
0009:         // evidence_anchor: SocketsHttpHandler, RemoteCertificateValidationCallback
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule018.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0470-csharp
0007:         // evidence_anchor: Aes.Create, CipherMode.ECB
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule019.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0473-csharp
0006:         // evidence_anchor: TripleDES.Create, DES.Create
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule020.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule020. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0475-csharp
0007:         // evidence_anchor: RSAEncryptionPadding.Pkcs1
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule021.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule021. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0478-csharp
0007:         // evidence_anchor: Rfc2898DeriveBytes
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule022.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule022. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0479-csharp
0006:         // evidence_anchor: new Random()
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule023.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule023. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public static void Execute() {
0006:         // rule_key: quantum.arq-q-0481-csharp
0007:         // evidence_anchor: .Key =, .IV =
```

### `services/quantum-coverage-csharp-b/src/legacy/Rule025.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule025. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public static void Execute() {
0005:         // rule_key: quantum.arq-q-0486-csharp
0006:         // evidence_anchor: SslProtocols.Tls, SslProtocols.Tls11
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1625`
- Synthetic filler / inflation LOC: `880`
- Synthetic filler ratio: `54.15%`

| category | LOC |
| --- | ---: |
| live business code | 286 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 414 |
| synthetic filler / inflation content | 880 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `services/quantum-coverage-csharp-b/src/legacy/Rule001.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0441-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule002.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0442-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule003.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0443-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule004.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0444-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule005.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0445-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule006.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0448-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule007.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0450-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule008.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0451-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule009.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0454-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule010.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0456-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule011.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0459-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule012.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0460-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule013.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0461-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule014.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0462-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule015.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0464-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule016.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0465-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule017.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0467-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule018.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0470-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule019.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0473-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule020.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0475-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule021.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0478-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule022.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0479-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule023.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0481-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-csharp-b/keys/rule_024.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0482-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-b/src/legacy/Rule025.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0486-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.

### must_not_find

- None.

### may_find_review

- None in the current run.

## 14. Explainability Expectations

- `detectionSource`: scenario checks it only when explicitly declared; regex-only live exports are tolerated unless the scenario contract says otherwise.
- `semanticKey`: informative but not currently a strict blocker unless a scenario-specific follow-up adds it.
- `resolvedValue`: strict on files that have an explainability contract entry.
- `resolutionScope`: strict only when declared by the scenario explainability contract.
- `queryFamily`: strict only when declared by the scenario explainability contract.
- `rawEvidenceJson`: not a mandatory contract field in the current scenario pack unless added explicitly later.

Scenario-specific explainability expectations:

- No strict scenario-specific explainability expectations were declared.

Explainability failure definition:

- A finding exists on the expected path, but the declared explainability fields are missing or do not match the scenario contract.

## 15. FP/FN Risk Notes

- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.
- Current run already demonstrated this risk: verdict=`FAIL_FN`.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: contains a non-trivial amount of live business code; build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `2/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Quantum coverage bundle exercising 25 distinct rule candidates across c# / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
