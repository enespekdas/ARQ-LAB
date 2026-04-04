# Generated Project Dossier - Q-V4-COV-107

## 1. Scenario Identity

- scenarioId: `Q-V4-COV-107`
- scenarioName: Quantum coverage bundle exercising 20 additional rule candidates across python / hybrid coverage pack.
- milestone: `M4`
- targetModule: `Quantum`
- language / stack: `Python / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-python-d-03`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V4-COV-107\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-107.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Python crypto and TLS late-slice coverage pack wave 03` as a `Python / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 20 additional rule candidates across python / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, sql, tests, validation, vendor, workers`
- Runtime role: `Python crypto and TLS late-slice coverage pack wave 03`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `workers/quantum-coverage-python-d-03/app/legacy/rule_001.py, workers/quantum-coverage-python-d-03/app/legacy/rule_002.py, workers/quantum-coverage-python-d-03/app/legacy/rule_003.py, workers/quantum-coverage-python-d-03/app/legacy/rule_004.py, workers/quantum-coverage-python-d-03/app/legacy/rule_005.py, workers/quantum-coverage-python-d-03/app/legacy/rule_006.py, workers/quantum-coverage-python-d-03/app/legacy/rule_007.py, workers/quantum-coverage-python-d-03/app/legacy/rule_008.py, workers/quantum-coverage-python-d-03/app/legacy/rule_009.py, workers/quantum-coverage-python-d-03/app/legacy/rule_010.py, workers/quantum-coverage-python-d-03/app/legacy/rule_011.py, workers/quantum-coverage-python-d-03/app/legacy/rule_012.py, workers/quantum-coverage-python-d-03/app/legacy/rule_013.py, workers/quantum-coverage-python-d-03/app/legacy/rule_014.py, workers/quantum-coverage-python-d-03/app/legacy/rule_015.py, workers/quantum-coverage-python-d-03/app/legacy/rule_016.py, workers/quantum-coverage-python-d-03/app/legacy/rule_017.py, workers/quantum-coverage-python-d-03/app/legacy/rule_018.py, workers/quantum-coverage-python-d-03/app/legacy/rule_019.py, workers/quantum-coverage-python-d-03/app/legacy/rule_020.py`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-python-d-03
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
|   |   |-- section-08.md
|   |   `-- section-09.md
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
|       |-- runbook-08.md
|       `-- runbook-09.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- sql
|   `-- reference
|       |-- reference-01.sql
|       |-- reference-02.sql
|       |-- reference-03.sql
|       |-- reference-04.sql
|       |-- reference-05.sql
|       |-- reference-06.sql
|       |-- reference-07.sql
|       |-- reference-08.sql
|       `-- reference-09.sql
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
|   `-- quantum-coverage-python-d-03
|       `-- app
|           `-- legacy
|               |-- rule_001.py
|               |-- rule_002.py
|               |-- rule_003.py
|               |-- rule_004.py
|               |-- rule_005.py
|               |-- rule_006.py
|               |-- rule_007.py
|               |-- rule_008.py
|               |-- rule_009.py
|               |-- rule_010.py
|               |-- rule_011.py
|               |-- rule_012.py
|               |-- rule_013.py
|               |-- rule_014.py
|               |-- rule_015.py
|               |-- rule_016.py
|               |-- rule_017.py
|               |-- rule_018.py
|               |-- rule_019.py
|               `-- rule_020.py
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
| docs/architecture/section-08.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-09.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-08.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-09.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pyproject.toml | build/deploy | 4 | Build or deployment definition shaping how Pyproject is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| sql/reference/reference-01.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-02.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-03.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-04.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-05.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-06.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-07.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-08.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-09.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 262 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 1010 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 891 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 95 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_001.py | live-code | 11 | Runtime business module contributing to Rule 001. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_002.py | live-code | 10 | Runtime business module contributing to Rule 002. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_003.py | live-code | 11 | Runtime business module contributing to Rule 003. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_004.py | live-code | 11 | Runtime business module contributing to Rule 004. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_005.py | live-code | 10 | Runtime business module contributing to Rule 005. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_006.py | live-code | 11 | Runtime business module contributing to Rule 006. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_007.py | live-code | 10 | Runtime business module contributing to Rule 007. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_008.py | live-code | 14 | Runtime business module contributing to Rule 008. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_009.py | live-code | 11 | Runtime business module contributing to Rule 009. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_010.py | live-code | 10 | Runtime business module contributing to Rule 010. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_011.py | live-code | 10 | Runtime business module contributing to Rule 011. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_012.py | live-code | 10 | Runtime business module contributing to Rule 012. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_013.py | live-code | 10 | Runtime business module contributing to Rule 013. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_014.py | live-code | 10 | Runtime business module contributing to Rule 014. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_015.py | live-code | 10 | Runtime business module contributing to Rule 015. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_016.py | live-code | 10 | Runtime business module contributing to Rule 016. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_017.py | live-code | 11 | Runtime business module contributing to Rule 017. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_018.py | live-code | 11 | Runtime business module contributing to Rule 018. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_019.py | live-code | 10 | Runtime business module contributing to Rule 019. | yes | no | no | yes | yes | no |
| workers/quantum-coverage-python-d-03/app/legacy/rule_020.py | live-code | 10 | Runtime business module contributing to Rule 020. | yes | no | no | yes | yes | no |

## 6. Positive Surfaces

- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_001.py`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0324-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_002.py`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0325-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_003.py`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0331-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_004.py`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0332-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_005.py`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0333-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_006.py`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0334-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_007.py`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0337-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_008.py`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0339-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_009.py`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0343-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_010.py`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0344-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_011.py`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0345-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_012.py`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0346-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_013.py`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0347-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_014.py`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0348-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_015.py`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0349-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_016.py`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0350-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_017.py`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0354-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_018.py`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0355-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_019.py`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0357-python`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `workers/quantum-coverage-python-d-03/app/legacy/rule_020.py`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0358-python`
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
| docs/architecture/section-07.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-08.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-09.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-01.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-02.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-03.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-04.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-05.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-06.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-07.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-08.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-09.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-python-d-03
0002: 
0003: Python crypto and TLS late-slice coverage pack wave 03
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

### `workers/quantum-coverage-python-d-03/app/legacy/rule_001.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0324-python
0005:     # evidence_anchor: import ssl
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_002.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0325-python
0004:     # evidence_anchor: from cryptography.hazmat, from cryptography.fernet
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_003.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0331-python
0005:     # evidence_anchor: hashlib.sha3_256, hashlib.sha3_512
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_004.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0332-python
0005:     # evidence_anchor: hashlib.blake2b, hashlib.blake2s
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_005.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0333-python
0004:     # evidence_anchor: AESGCM, ChaCha20Poly1305
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_006.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0334-python
0005:     # evidence_anchor: rsa.generate_private_key, ec.generate_private_key
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_007.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0337-python
0004:     # evidence_anchor: HKDF, HKDFExpand
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_008.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0339-python
0005:     # evidence_anchor: algorithm='RS256', algorithm='ES256'
0008:     import jwt
0009:     jwt.encode({"sub": "coverage"}, "secret", algorithm="RS256")
0010:     algorithm='RS256'
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_009.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0343-python
0005:     # evidence_anchor: import ssl
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_010.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0344-python
0004:     # evidence_anchor: from cryptography.hazmat
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_011.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0345-python
0004:     # evidence_anchor: import oqs, from oqs import
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_012.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0346-python
0004:     # evidence_anchor: oqs.KeyEncapsulation, Kyber768, ML-KEM-768
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_013.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0347-python
0004:     # evidence_anchor: oqs.Signature, Dilithium3, ML-DSA-65
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_014.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0348-python
0004:     # evidence_anchor: oqs.Signature, SPHINCS+, SLH-DSA
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_015.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0349-python
0004:     # evidence_anchor: oqs.KeyEncapsulation, FrodoKEM
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_016.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0350-python
0004:     # evidence_anchor: Kyber768, X25519PrivateKey, HKDF
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_017.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0354-python
0005:     # evidence_anchor: hashlib.sha3_256, hashlib.shake_256, hashlib.blake2b
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_018.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def execute():
0004:     # rule_key: quantum.arq-q-0355-python
0005:     # evidence_anchor: rsa.generate_private_key, ec.generate_private_key
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_019.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0357-python
0004:     # evidence_anchor: AESGCM, ChaCha20Poly1305
```

### `workers/quantum-coverage-python-d-03/app/legacy/rule_020.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 020. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: def execute():
0003:     # rule_key: quantum.arq-q-0358-python
0004:     # evidence_anchor: HKDF, HKDFExpand
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1580`
- Synthetic filler / inflation LOC: `990`
- Synthetic filler ratio: `62.66%`

| category | LOC |
| --- | ---: |
| live business code | 211 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 335 |
| synthetic filler / inflation content | 990 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_001.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0324-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_002.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0325-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_003.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0331-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_004.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0332-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_005.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0333-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_006.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0334-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_007.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0337-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_008.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0339-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_009.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0343-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_010.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0344-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_011.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0345-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_012.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0346-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_013.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0347-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_014.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0348-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_015.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0349-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_016.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0350-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_017.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0354-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_018.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0355-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_019.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0357-python`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `workers/quantum-coverage-python-d-03/app/legacy/rule_020.py`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0358-python`
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
- What makes it feel real: build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `1/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Quantum coverage bundle exercising 20 additional rule candidates across python / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
