# Generated Project Dossier - Q-V4-COV-104

## 1. Scenario Identity

- scenarioId: `Q-V4-COV-104`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across python / hybrid coverage pack.
- milestone: `M4`
- targetModule: `Quantum`
- language / stack: `Python / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-python-c`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V4-COV-104\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-104.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.` as a `Python / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across python / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, sql, tests, validation, vendor, workers`
- Runtime role: `Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `secrets/quantum-coverage-python-c/keys/rule_005.pem, secrets/quantum-coverage-python-c/keys/rule_014.pem, secrets/quantum-coverage-python-c/keys/rule_021.pem, workers/quantum-coverage-python-c/app/legacy/rule_001.py, workers/quantum-coverage-python-c/app/legacy/rule_002.py, workers/quantum-coverage-python-c/app/legacy/rule_003.py, workers/quantum-coverage-python-c/app/legacy/rule_004.py, workers/quantum-coverage-python-c/app/legacy/rule_006.py, workers/quantum-coverage-python-c/app/legacy/rule_007.py, workers/quantum-coverage-python-c/app/legacy/rule_008.py, workers/quantum-coverage-python-c/app/legacy/rule_009.py, workers/quantum-coverage-python-c/app/legacy/rule_010.py, workers/quantum-coverage-python-c/app/legacy/rule_011.py, workers/quantum-coverage-python-c/app/legacy/rule_012.py, workers/quantum-coverage-python-c/app/legacy/rule_013.py, workers/quantum-coverage-python-c/app/legacy/rule_015.py, workers/quantum-coverage-python-c/app/legacy/rule_016.py, workers/quantum-coverage-python-c/app/legacy/rule_017.py, workers/quantum-coverage-python-c/app/legacy/rule_018.py, workers/quantum-coverage-python-c/app/legacy/rule_019.py, workers/quantum-coverage-python-c/app/legacy/rule_020.py, workers/quantum-coverage-python-c/app/legacy/rule_022.py, workers/quantum-coverage-python-c/app/legacy/rule_023.py, workers/quantum-coverage-python-c/app/legacy/rule_024.py, workers/quantum-coverage-python-c/app/legacy/rule_025.py, workers/quantum-coverage-python-c/app/legacy/rule_026.py, workers/quantum-coverage-python-c/app/legacy/rule_027.py, workers/quantum-coverage-python-c/app/legacy/rule_028.py, workers/quantum-coverage-python-c/app/legacy/rule_029.py, workers/quantum-coverage-python-c/app/legacy/rule_030.py`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md, ops/playbooks/runbook-02.md, ops/playbooks/runbook-03.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-python-c
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
|   |   `-- section-07.md
|   `-- coverage-notes.md
|-- ops
|   `-- playbooks
|       |-- runbook-01.md
|       |-- runbook-02.md
|       |-- runbook-03.md
|       |-- runbook-04.md
|       |-- runbook-05.md
|       |-- runbook-06.md
|       `-- runbook-07.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- secrets
|   `-- quantum-coverage-python-c
|       `-- keys
|           |-- rule_005.pem
|           |-- rule_014.pem
|           `-- rule_021.pem
|-- sql
|   `-- reference
|       |-- reference-01.sql
|       |-- reference-02.sql
|       |-- reference-03.sql
|       |-- reference-04.sql
|       |-- reference-05.sql
|       |-- reference-06.sql
|       `-- reference-07.sql
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
|-- workers
|   `-- quantum-coverage-python-c
|       `-- app
|           `-- legacy
|               |-- rule_001.py
|               |-- rule_002.py
|               |-- rule_003.py
|               |-- rule_004.py
|               |-- rule_006.py
|               |-- rule_007.py
|               |-- rule_008.py
|               |-- rule_009.py
|               |-- rule_010.py
|               |-- rule_011.py
|               |-- rule_012.py
|               |-- rule_013.py
|               |-- rule_015.py
|               |-- rule_016.py
|               |-- rule_017.py
|               |-- rule_018.py
|               |-- rule_019.py
|               |-- rule_020.py
|               |-- rule_022.py
|               |-- rule_023.py
|               |-- rule_024.py
|               |-- rule_025.py
|               |-- rule_026.py
|               |-- rule_027.py
|               |-- rule_028.py
|               |-- rule_029.py
|               `-- rule_030.py
|-- .gitignore
|-- pyproject.toml
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
| docs/architecture/section-07.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pyproject.toml | build/deploy | 4 | Build or deployment definition shaping how Pyproject is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-python-c/keys/rule_005.pem | generated | 14 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-python-c/keys/rule_014.pem | generated | 14 | Generated or derived project artifact related to Rule 014. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-python-c/keys/rule_021.pem | generated | 14 | Generated or derived project artifact related to Rule 021. | yes | no | yes | no | no | no |
| sql/reference/reference-01.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-02.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-03.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-04.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-05.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-06.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-07.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 1066 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1201 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 102 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 16 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |
| workers/quantum-coverage-python-c/app/legacy/rule_001.py | live-code | 11 | Runtime business module contributing to Rule 001. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_002.py | live-code | 13 | Runtime business module contributing to Rule 002. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_003.py | live-code | 11 | Runtime business module contributing to Rule 003. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_004.py | live-code | 10 | Runtime business module contributing to Rule 004. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_006.py | live-code | 11 | Runtime business module contributing to Rule 006. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_007.py | live-code | 12 | Runtime business module contributing to Rule 007. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_008.py | live-code | 12 | Runtime business module contributing to Rule 008. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_009.py | live-code | 11 | Runtime business module contributing to Rule 009. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_010.py | live-code | 11 | Runtime business module contributing to Rule 010. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_011.py | live-code | 11 | Runtime business module contributing to Rule 011. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_012.py | live-code | 11 | Runtime business module contributing to Rule 012. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_013.py | live-code | 10 | Runtime business module contributing to Rule 013. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_015.py | live-code | 12 | Runtime business module contributing to Rule 015. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_016.py | live-code | 12 | Runtime business module contributing to Rule 016. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_017.py | live-code | 11 | Runtime business module contributing to Rule 017. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_018.py | live-code | 11 | Runtime business module contributing to Rule 018. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_019.py | live-code | 11 | Runtime business module contributing to Rule 019. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_020.py | live-code | 10 | Runtime business module contributing to Rule 020. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_022.py | live-code | 12 | Runtime business module contributing to Rule 022. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_023.py | live-code | 12 | Runtime business module contributing to Rule 023. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_024.py | live-code | 12 | Runtime business module contributing to Rule 024. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_025.py | live-code | 12 | Runtime business module contributing to Rule 025. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_026.py | live-code | 12 | Runtime business module contributing to Rule 026. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_027.py | live-code | 12 | Runtime business module contributing to Rule 027. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_028.py | live-code | 12 | Runtime business module contributing to Rule 028. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_029.py | live-code | 12 | Runtime business module contributing to Rule 029. | yes | yes | no | yes | yes | no |
| workers/quantum-coverage-python-c/app/legacy/rule_030.py | live-code | 12 | Runtime business module contributing to Rule 030. | yes | yes | no | yes | yes | no |

## 6. Positive Surfaces

- Path: `workers/quantum-coverage-python-c/app/legacy/rule_001.py`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0313-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_002.py`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0318-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_003.py`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0321-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_004.py`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0322-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-python-c/keys/rule_005.pem`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0323-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_006.py`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0327-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_007.py`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0328-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_008.py`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0329-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_009.py`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0330-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_010.py`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0335-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_011.py`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0338-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_012.py`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0340-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_013.py`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0341-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-python-c/keys/rule_014.pem`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0342-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_015.py`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0351-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_016.py`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0352-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_017.py`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0353-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_018.py`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0356-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_019.py`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0359-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_020.py`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0360-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-python-c/keys/rule_021.pem`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0361-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_022.py`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0365-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_023.py`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0366-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_024.py`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0367-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_025.py`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0368-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_026.py`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0369-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_027.py`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0370-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_028.py`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0371-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_029.py`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0372-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-c/app/legacy/rule_030.py`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0373-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `workers/quantum-coverage-python-c/app/legacy/rule_001.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_003.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_006.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_007.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_008.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_009.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_010.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_012.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_015.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_016.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_017.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_018.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_019.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_023.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_024.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_025.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_026.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_027.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_028.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_029.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/quantum-coverage-python-c/app/legacy/rule_030.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-python-c/keys/rule_005.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-python-c/keys/rule_014.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-python-c/keys/rule_021.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-01.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-02.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-03.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-04.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-05.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-06.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-07.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-python-c
0002: 
0003: Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `pyproject.toml`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Pyproject is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: [project]
0002: name = "coverage-context"
0003: version = "0.1.0"
0004: requires-python = ">=3.11,<3.12"
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-python-c/keys/rule_005.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0323-python
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: ---------------------------------------------------------BEGIN                    RSA                           PRIVATE                                 KEY------------------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-python-c/keys/rule_014.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 014. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0342-python
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: ------------------------------------------------------------------------------BEGIN                  PRIVATE            KEY---------------------------------------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-python-c/keys/rule_021.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 021. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0361-python
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: ----------------------------BEGIN       ENCRYPTED          PRIVATE                         KEY----------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `workers/quantum-coverage-python-c/app/legacy/rule_001.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0313-python
0005:     # evidence_anchor: padding.PKCS1v15
```

### `workers/quantum-coverage-python-c/app/legacy/rule_002.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0318-python
0005:     # evidence_anchor: algorithm='none', verify_signature=False, algorithms=['none']
```

### `workers/quantum-coverage-python-c/app/legacy/rule_003.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0321-python
0005:     # evidence_anchor: import random
```

### `workers/quantum-coverage-python-c/app/legacy/rule_004.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0322-python
0004:     # evidence_anchor: SECRET_KEY, DATABASE_PASSWORD, API_KEY
0005:     # regex_sample: SECRET_KEY   =             '$Mu^mC##,l62ZwK]1~d:/<TN*fUlYK\t|L B U~ihCa#Ohr}.NS]n~Hxzchh6xLoy\.qLY>g9f o"
0006:     # keywords: SECRET_KEY | API_KEY | DATABASE_PASSWORD | PRIVATE_KEY
0007:     SECRET_KEY, DATABASE_PASSWORD, API_KEY
0008: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_006.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0327-python
0005:     # evidence_anchor: ssl.TLSVersion.TLSv1, ssl.TLSVersion.TLSv1_1
```

### `workers/quantum-coverage-python-c/app/legacy/rule_007.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0328-python
0005:     # evidence_anchor: ssl.CERT_NONE
```

### `workers/quantum-coverage-python-c/app/legacy/rule_008.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0329-python
0006:     # evidence_anchor: verify=False, ssl=False
0007:     # regex_sample: verify   =                            false
0008:     # keywords: verify=False | ssl=False | verify_ssl=False
0009:     requests.get("https://partner.example", verify=False)
0010: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_009.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0330-python
0005:     # evidence_anchor: hashlib.md5, hashlib.sha1
0006:     # regex_sample: hashlib.md5
0007:     # keywords: hashlib | hashlib.md5 | hashlib.sha1 | hashlib.new | md5 | sha1
0008:     hashlib.md5(b"legacy").hexdigest()
0009: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_010.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0335-python
0005:     # evidence_anchor: padding.PKCS1v15
```

### `workers/quantum-coverage-python-c/app/legacy/rule_011.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0338-python
0005:     # evidence_anchor: algorithm='none', verify_signature=False
```

### `workers/quantum-coverage-python-c/app/legacy/rule_012.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0340-python
0005:     # evidence_anchor: import random
```

### `workers/quantum-coverage-python-c/app/legacy/rule_013.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0341-python
0004:     # evidence_anchor: SECRET_KEY, API_KEY
0005:     # regex_sample: SECRET_KEY                           =           "@cgzbsW03}kF6`v%  Ab(LZ~X  `L.U8 + %"
0006:     # keywords: SECRET_KEY | API_KEY | DATABASE_PASSWORD
0007:     SECRET_KEY, API_KEY
0008: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_015.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0351-python
0005:     # evidence_anchor: ssl.CERT_NONE
```

### `workers/quantum-coverage-python-c/app/legacy/rule_016.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0352-python
0006:     # evidence_anchor: verify=False, ssl=False
0007:     # regex_sample: verify                      =       false
0008:     # keywords: verify=False | ssl=False
0009:     requests.get("https://partner.example", verify=False)
0010: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_017.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0353-python
0005:     # evidence_anchor: hashlib.md5, hashlib.sha1
0006:     # regex_sample: hashlib.md5
0007:     # keywords: hashlib | hashlib.md5 | hashlib.sha1 | hashlib.new | md5 | sha1
0008:     hashlib.md5(b"legacy").hexdigest()
0009: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_018.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0356-python
0005:     # evidence_anchor: padding.PKCS1v15
```

### `workers/quantum-coverage-python-c/app/legacy/rule_019.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0359-python
0005:     # evidence_anchor: import random
```

### `workers/quantum-coverage-python-c/app/legacy/rule_020.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 020. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0360-python
0004:     # evidence_anchor: SECRET_KEY, API_KEY
0005:     # regex_sample: SECRET_KEY       =              "/gFpSoc| K 6OM{A8894$#-aA]I)fbq-lk {>7 @f>*c@'
0006:     # keywords: SECRET_KEY | API_KEY
0007:     SECRET_KEY, API_KEY
0008: 
```

### `workers/quantum-coverage-python-c/app/legacy/rule_022.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 022. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0365-python
0005:     # evidence_anchor: SSLContext.check_hostname, check_hostname=False
```

### `workers/quantum-coverage-python-c/app/legacy/rule_023.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 023. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0366-python
0005:     # evidence_anchor: SSLContext.check_hostname, check_hostname=False
```

### `workers/quantum-coverage-python-c/app/legacy/rule_024.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 024. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0367-python
0005:     # evidence_anchor: SSLContext.check_hostname, check_hostname=False
```

### `workers/quantum-coverage-python-c/app/legacy/rule_025.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 025. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0368-python
0005:     # evidence_anchor: SSLContext.check_hostname, check_hostname=False
```

### `workers/quantum-coverage-python-c/app/legacy/rule_026.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 026. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0369-python
0006:     # evidence_anchor: urllib3.PoolManager, cert_reqs, CERT_NONE, assert_hostname
```

### `workers/quantum-coverage-python-c/app/legacy/rule_027.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0370-python
0006:     # evidence_anchor: urllib3.PoolManager, cert_reqs, CERT_NONE, assert_hostname
```

### `workers/quantum-coverage-python-c/app/legacy/rule_028.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0371-python
0006:     # evidence_anchor: urllib3.PoolManager, cert_reqs, CERT_NONE, assert_hostname
```

### `workers/quantum-coverage-python-c/app/legacy/rule_029.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 029. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0372-python
0006:     # evidence_anchor: urllib3.PoolManager, cert_reqs, CERT_NONE, assert_hostname
```

### `workers/quantum-coverage-python-c/app/legacy/rule_030.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 030. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0004: def execute():
0005:     # rule_key: quantum.arq-q-0373-python
0006:     # evidence_anchor: urllib3.PoolManager, cert_reqs, CERT_NONE, assert_hostname
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1636`
- Synthetic filler / inflation LOC: `770`
- Synthetic filler ratio: `47.07%`

| category | LOC |
| --- | ---: |
| live business code | 309 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 513 |
| synthetic filler / inflation content | 770 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `workers/quantum-coverage-python-c/app/legacy/rule_001.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0313-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_002.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0318-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_003.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0321-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_004.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0322-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-python-c/keys/rule_005.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0323-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_006.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0327-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_007.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0328-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_008.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0329-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_009.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0330-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_010.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0335-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_011.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0338-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_012.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0340-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_013.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0341-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-python-c/keys/rule_014.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0342-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_015.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0351-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_016.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0352-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_017.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0353-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_018.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0356-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_019.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0359-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_020.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0360-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-python-c/keys/rule_021.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0361-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_022.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0365-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_023.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0366-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_024.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0367-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_025.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0368-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_026.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0369-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_027.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0370-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_028.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0371-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_029.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0372-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-c/app/legacy/rule_030.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0373-python`
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

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across python / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
