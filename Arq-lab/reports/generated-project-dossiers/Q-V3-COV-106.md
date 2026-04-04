# Generated Project Dossier - Q-V3-COV-106

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-106`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `Java / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-java-d`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-106\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-106.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Java crypto coverage pack D targeting additional RSA/ECDSA, TLS, and key-material rule families.` as a `Java / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, services, sql, tests, validation, vendor`
- Runtime role: `Java crypto coverage pack D targeting additional RSA/ECDSA, TLS, and key-material rule families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `services/quantum-coverage-java-d/module-014/pom.xml, services/quantum-coverage-java-d/module-015/pom.xml, services/quantum-coverage-java-d/module-016/pom.xml, services/quantum-coverage-java-d/module-017/pom.xml, services/quantum-coverage-java-d/module-018/pom.xml, services/quantum-coverage-java-d/module-019/pom.xml, services/quantum-coverage-java-d/module-020/pom.xml, services/quantum-coverage-java-d/module-021/pom.xml, services/quantum-coverage-java-d/module-022/pom.xml, services/quantum-coverage-java-d/module-023/pom.xml, services/quantum-coverage-java-d/module-024/pom.xml, services/quantum-coverage-java-d/module-025/pom.xml, services/quantum-coverage-java-d/src/legacy/Rule001.java, services/quantum-coverage-java-d/src/legacy/Rule002.java, services/quantum-coverage-java-d/src/legacy/Rule003.java, services/quantum-coverage-java-d/src/legacy/Rule004.java, services/quantum-coverage-java-d/src/legacy/Rule005.java, services/quantum-coverage-java-d/src/legacy/Rule006.java, services/quantum-coverage-java-d/src/legacy/Rule007.java, services/quantum-coverage-java-d/src/legacy/Rule008.java, services/quantum-coverage-java-d/src/legacy/Rule009.java, services/quantum-coverage-java-d/src/legacy/Rule010.java, services/quantum-coverage-java-d/src/legacy/Rule011.java, services/quantum-coverage-java-d/src/legacy/Rule012.java, services/quantum-coverage-java-d/src/legacy/Rule013.java, services/quantum-coverage-java-d/src/legacy/Rule026.java, services/quantum-coverage-java-d/src/legacy/Rule027.java, services/quantum-coverage-java-d/src/legacy/Rule028.java, services/quantum-coverage-java-d/src/legacy/Rule029.java, services/quantum-coverage-java-d/src/legacy/Rule030.java`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md, ops/playbooks/runbook-02.md, ops/playbooks/runbook-03.md, ops/playbooks/runbook-04.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-java-d
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
|   |   `-- section-06.md
|   `-- coverage-notes.md
|-- ops
|   `-- playbooks
|       |-- runbook-01.md
|       |-- runbook-02.md
|       |-- runbook-03.md
|       |-- runbook-04.md
|       |-- runbook-05.md
|       `-- runbook-06.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- services
|   `-- quantum-coverage-java-d
|       |-- module-014
|       |   `-- pom.xml
|       |-- module-015
|       |   `-- pom.xml
|       |-- module-016
|       |   `-- pom.xml
|       |-- module-017
|       |   `-- pom.xml
|       |-- module-018
|       |   `-- pom.xml
|       |-- module-019
|       |   `-- pom.xml
|       |-- module-020
|       |   `-- pom.xml
|       |-- module-021
|       |   `-- pom.xml
|       |-- module-022
|       |   `-- pom.xml
|       |-- module-023
|       |   `-- pom.xml
|       |-- module-024
|       |   `-- pom.xml
|       |-- module-025
|       |   `-- pom.xml
|       `-- src
|           `-- legacy
|               |-- Rule001.java
|               |-- Rule002.java
|               |-- Rule003.java
|               |-- Rule004.java
|               |-- Rule005.java
|               |-- Rule006.java
|               |-- Rule007.java
|               |-- Rule008.java
|               |-- Rule009.java
|               |-- Rule010.java
|               |-- Rule011.java
|               |-- Rule012.java
|               |-- Rule013.java
|               |-- Rule026.java
|               |-- Rule027.java
|               |-- Rule028.java
|               |-- Rule029.java
|               `-- Rule030.java
|-- sql
|   `-- reference
|       |-- reference-01.sql
|       |-- reference-02.sql
|       |-- reference-03.sql
|       |-- reference-04.sql
|       |-- reference-05.sql
|       `-- reference-06.sql
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
|-- pom.xml
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .github/workflows/deploy.yml | live-config | 7 | Runtime configuration carrying environment or deployment settings for Deploy. | no | no | no | yes | yes | no |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | yes | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| config/runtime/baseline.yaml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Baseline. | no | no | no | yes | yes | no |
| deploy/prod/service.properties | live-config | 1 | Runtime configuration carrying environment or deployment settings for Service. | no | no | no | yes | yes | no |
| docs/architecture/section-01.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-02.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-03.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-04.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-05.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-06.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pom.xml | build/deploy | 12 | Build or deployment definition shaping how Pom is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| services/quantum-coverage-java-d/module-014/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-015/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-016/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-017/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-018/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-019/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-020/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-021/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-022/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-023/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-024/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/module-025/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-d/src/legacy/Rule001.java | live-code | 11 | Runtime business module contributing to Rule001. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule002.java | live-code | 11 | Runtime business module contributing to Rule002. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule003.java | live-code | 11 | Runtime business module contributing to Rule003. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule004.java | live-code | 11 | Runtime business module contributing to Rule004. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule005.java | live-code | 11 | Runtime business module contributing to Rule005. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule006.java | live-code | 11 | Runtime business module contributing to Rule006. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule007.java | live-code | 11 | Runtime business module contributing to Rule007. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule008.java | live-code | 11 | Runtime business module contributing to Rule008. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule009.java | live-code | 11 | Runtime business module contributing to Rule009. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule010.java | live-code | 11 | Runtime business module contributing to Rule010. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule011.java | live-code | 11 | Runtime business module contributing to Rule011. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule012.java | live-code | 11 | Runtime business module contributing to Rule012. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule013.java | live-code | 11 | Runtime business module contributing to Rule013. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule026.java | live-code | 13 | Runtime business module contributing to Rule026. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule027.java | live-code | 13 | Runtime business module contributing to Rule027. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule028.java | live-code | 13 | Runtime business module contributing to Rule028. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule029.java | live-code | 13 | Runtime business module contributing to Rule029. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-d/src/legacy/Rule030.java | live-code | 13 | Runtime business module contributing to Rule030. | yes | no | no | yes | yes | no |
| sql/reference/reference-01.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-02.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-03.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-04.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-05.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-06.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 1024 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1261 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 108 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `services/quantum-coverage-java-d/src/legacy/Rule001.java`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0030-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule002.java`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0031-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule003.java`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0033-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule004.java`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0034-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule005.java`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0035-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule006.java`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0036-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule007.java`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0037-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule008.java`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0038-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule009.java`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0039-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule010.java`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0040-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule011.java`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0041-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule012.java`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0042-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule013.java`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0043-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-014/pom.xml`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0044-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-015/pom.xml`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0045-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-016/pom.xml`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0046-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-017/pom.xml`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0047-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-018/pom.xml`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0048-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-019/pom.xml`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0049-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-020/pom.xml`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0050-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-021/pom.xml`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0051-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-022/pom.xml`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0052-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-023/pom.xml`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0053-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-024/pom.xml`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0054-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/module-025/pom.xml`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0055-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule026.java`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0056-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule027.java`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0057-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule028.java`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0058-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule029.java`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0059-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-d/src/legacy/Rule030.java`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0060-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- No near-real negative surfaces were declared for this scenario.

## 8. Protected Negative Surfaces

| path | classification | why protected |
| --- | --- | --- |
| docs/architecture/section-01.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-02.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-03.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-04.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-05.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-06.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-014/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-015/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-016/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-017/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-018/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-019/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-020/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-021/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-022/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-023/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-024/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-d/module-025/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-01.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-02.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-03.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-04.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-05.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-06.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-java-d
0002: 
0003: Java crypto coverage pack D targeting additional RSA/ECDSA, TLS, and key-material rule families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `pom.xml`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Pom is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: <project>
0002:   <modelVersion>4.0.0</modelVersion>
0003:   <groupId>io.arq.lab</groupId>
0004:   <artifactId>coverage-context</artifactId>
0005:   <version>1.0.0</version>
0006:   <properties>
0007:     <maven.compiler.source>8</maven.compiler.source>
0008:     <maven.compiler.target>8</maven.compiler.target>
0009:     <maven.compiler.release>8</maven.compiler.release>
0010:     <java.version>8</java.version>
0011:   </properties>
0012: </project>
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `services/quantum-coverage-java-d/module-014/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>com.auth0</groupId>
0005:       <artifactId>java-jwt</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>com.auth0</groupId>
0010:       <artifactId>java-jwt</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-015/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>com.google.crypto.tink</groupId>
0005:       <artifactId>tink</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>com.google.crypto.tink</groupId>
0010:       <artifactId>tink</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-016/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>com.nimbusds</groupId>
0005:       <artifactId>nimbus-jose-jwt</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>com.nimbusds</groupId>
0010:       <artifactId>nimbus-jose-jwt</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-017/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>com.squareup.okhttp3</groupId>
0005:       <artifactId>okhttp</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>com.squareup.okhttp3</groupId>
0010:       <artifactId>okhttp</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-018/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003:     <dependency>
0004:       <groupId>io.jsonwebtoken</groupId>
0005:       <artifactId>jjwt</artifactId>
0008:     <dependency>
0009:       <groupId>io.jsonwebtoken</groupId>
0010:       <artifactId>jjwt</artifactId>
0013:     <dependency>
0014:       <groupId>io.jsonwebtoken</groupId>
0015:       <artifactId>jjwt</artifactId>
```

### `services/quantum-coverage-java-d/module-019/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>io.netty</groupId>
0005:       <artifactId>netty-handler</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>io.netty</groupId>
0010:       <artifactId>netty-handler</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-020/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.apache.httpcomponents.client5</groupId>
0005:       <artifactId>httpclient5</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.apache.httpcomponents.client5</groupId>
0010:       <artifactId>httpclient5</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-021/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.bitbucket.b_c</groupId>
0005:       <artifactId>jose4j</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.bitbucket.b_c</groupId>
0010:       <artifactId>jose4j</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-022/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.bouncycastle</groupId>
0005:       <artifactId>bcpkix</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.bouncycastle</groupId>
0010:       <artifactId>bcpkix</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-023/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.bouncycastle</groupId>
0005:       <artifactId>bcprov</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.bouncycastle</groupId>
0010:       <artifactId>bcprov</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-024/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.bouncycastle</groupId>
0005:       <artifactId>bcprov-ext-jdk18on</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.bouncycastle</groupId>
0010:       <artifactId>bcprov-ext-jdk18on</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/module-025/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <dependency>
0004:       <groupId>org.conscrypt</groupId>
0005:       <artifactId>conscrypt-openjdk-uber</artifactId>
0006:       <version>1.0.0</version>
0007:     </dependency>
0008:     <dependency>
0009:       <groupId>org.conscrypt</groupId>
0010:       <artifactId>conscrypt-openjdk-uber</artifactId>
0011:       <version>1.0.0</version>
0012:     </dependency>
```

### `services/quantum-coverage-java-d/src/legacy/Rule001.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0030-java
0006:         // evidence_anchor: CertificateFactory.getInstance("X.509")
```

### `services/quantum-coverage-java-d/src/legacy/Rule002.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0031-java
0006:         // evidence_anchor: MessageDigest.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule003.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0033-java
0006:         // evidence_anchor: KeyStore.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule004.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0034-java
0006:         // evidence_anchor: Mac.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule005.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0035-java
0006:         // evidence_anchor: new SecureRandom(...) / SecureRandom.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule006.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0036-java
0006:         // evidence_anchor: Cipher.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule007.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0037-java
0006:         // evidence_anchor: new CipherInputStream(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule008.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0038-java
0006:         // evidence_anchor: new CipherOutputStream(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule009.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0039-java
0006:         // evidence_anchor: new SealedObject(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule010.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0040-java
0006:         // evidence_anchor: KeyGenerator.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule011.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0041-java
0006:         // evidence_anchor: KeyManagerFactory.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule012.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0042-java
0006:         // evidence_anchor: TrustManagerFactory.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule013.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0004:     public void execute() throws Exception {
0005:         // rule_key: quantum.arq-q-0043-java
0006:         // evidence_anchor: SSLContext.getInstance(...)
```

### `services/quantum-coverage-java-d/src/legacy/Rule026.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule026. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public void execute() throws Exception {
0006:         // rule_key: quantum.arq-q-0056-java
0007:         // evidence_anchor: new ECGenParameterSpec("prime256v1")
```

### `services/quantum-coverage-java-d/src/legacy/Rule027.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public void execute() throws Exception {
0006:         // rule_key: quantum.arq-q-0057-java
0007:         // evidence_anchor: new ECGenParameterSpec("secp256k1")
```

### `services/quantum-coverage-java-d/src/legacy/Rule028.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public void execute() throws Exception {
0006:         // rule_key: quantum.arq-q-0058-java
0007:         // evidence_anchor: new ECGenParameterSpec("secp256r1")
```

### `services/quantum-coverage-java-d/src/legacy/Rule029.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule029. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public void execute() throws Exception {
0006:         // rule_key: quantum.arq-q-0059-java
0007:         // evidence_anchor: new ECGenParameterSpec("secp384r1")
```

### `services/quantum-coverage-java-d/src/legacy/Rule030.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule030. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0005:     public void execute() throws Exception {
0006:         // rule_key: quantum.arq-q-0060-java
0007:         // evidence_anchor: new ECGenParameterSpec("secp521r1")
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1613`
- Synthetic filler / inflation LOC: `660`
- Synthetic filler ratio: `40.92%`

| category | LOC |
| --- | ---: |
| live business code | 208 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 693 |
| synthetic filler / inflation content | 660 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `services/quantum-coverage-java-d/src/legacy/Rule001.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0030-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule002.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0031-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule003.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0033-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule004.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0034-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule005.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0035-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule006.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0036-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule007.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0037-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule008.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0038-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule009.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0039-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule010.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0040-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule011.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0041-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule012.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0042-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule013.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0043-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-014/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0044-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-015/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0045-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-016/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0046-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-017/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0047-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-018/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0048-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-019/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0049-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-020/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0050-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-021/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0051-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-022/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0052-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-023/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0053-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-024/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0054-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/module-025/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0055-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule026.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0056-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule027.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0057-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule028.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0058-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule029.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0059-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-d/src/legacy/Rule030.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0060-java`
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
- What makes it feel real: build/test/smoke contracts execute successfully.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `2/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-d\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
