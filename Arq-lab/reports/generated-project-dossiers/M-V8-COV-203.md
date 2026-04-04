# Generated Project Dossier - M-V8-COV-203

## 1. Scenario Identity

- scenarioId: `M-V8-COV-203`
- scenarioName: Quantum precision coverage bundle exercising 13 cpp rule candidates within the C++98-to-C++26 applicability slice.
- milestone: `M8`
- targetModule: `Quantum`
- language / stack: `Native / mixed precision coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-precision-cpp-c-98-to-c-26-01`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-COV-203\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-203.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `cpp version-sliced precision coverage pack (C++98-to-C++26) wave 01` as a `Native / mixed precision coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum precision coverage bundle exercising 13 cpp rule candidates within the C++98-to-C++26 applicability slice.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, secrets, sql, tests, validation, vendor`
- Runtime role: `cpp version-sliced precision coverage pack (C++98-to-C++26) wave 01`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/module-012/CMakeLists.txt, secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem, secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/coverage-notes.md, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp, native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-precision-cpp-c-98-to-c-26-01
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
|-- native
|   `-- quantum-precision-cpp-c-98-to-c-26-01
|       |-- cpp
|       |   |-- rule_001.cpp
|       |   |-- rule_002.cpp
|       |   |-- rule_003.cpp
|       |   |-- rule_004.cpp
|       |   |-- rule_005.cpp
|       |   |-- rule_006.cpp
|       |   |-- rule_007.cpp
|       |   |-- rule_009.cpp
|       |   |-- rule_011.cpp
|       |   `-- rule_013.cpp
|       `-- module-012
|           `-- CMakeLists.txt
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
|   `-- quantum-precision-cpp-c-98-to-c-26-01
|       `-- keys
|           |-- rule_008.pem
|           `-- rule_010.pem
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
|-- .gitignore
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
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp | generated | 12 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp | generated | 12 | Generated or derived project artifact related to Rule 002. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp | generated | 12 | Generated or derived project artifact related to Rule 003. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp | generated | 12 | Generated or derived project artifact related to Rule 004. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp | generated | 12 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp | generated | 12 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp | generated | 12 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp | generated | 12 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp | generated | 12 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp | generated | 12 | Generated or derived project artifact related to Rule 013. | yes | no | yes | no | no | no |
| native/quantum-precision-cpp-c-98-to-c-26-01/module-012/CMakeLists.txt | docs | 3 | Documentation or explanatory material for Cmake Lists. | yes | no | no | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem | generated | 14 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem | generated | 14 | Generated or derived project artifact related to Rule 010. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 171 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 814 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 712 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 84 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 16 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0207-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0208-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0209-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0210-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0211-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0212-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0213-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0216-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0218-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0222-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0214-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/module-012/CMakeLists.txt`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0220-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0215-cpp`
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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-precision-cpp-c-98-to-c-26-01
0002: 
0003: cpp version-sliced precision coverage pack (C++98-to-C++26) wave 01
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0207-cpp
0006: // evidence_anchor: SSL_CTX_set_verify(..., SSL_VERIFY_NONE)
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 002. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0208-cpp
0006: // evidence_anchor: SSLv3_method/TLSv1_method
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 003. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0209-cpp
0006: // evidence_anchor: EVP_md5
0007: // regex_sample: MD5_Update
0008: // keywords: EVP_md5 | MD5_Init | MD5_Update | MD5_Final
0009: int execute_coverage_cpp() {
0010:     EVP_DigestInit_ex(ctx, EVP_md5(), NULL);
0011:     return 0;
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 004. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0210-cpp
0006: // evidence_anchor: EVP_sha1
0007: // regex_sample: SHA1_Update
0008: // keywords: EVP_sha1 | SHA1_Init | SHA1_Update | SHA1_Final
0009: int execute_coverage_cpp() {
0010:     EVP_DigestInit_ex(ctx, EVP_sha1(), NULL);
0011:     return 0;
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0211-cpp
0006: // evidence_anchor: EVP_des_* / EVP_rc4
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0212-cpp
0006: // evidence_anchor: EVP_aes_*_ecb
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0213-cpp
0006: // evidence_anchor: RSA_generate_key_ex(1024)
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0218-cpp
0006: // evidence_anchor: PKCS5_PBKDF2_HMAC
0009: int execute_coverage_cpp() {
0010:     PKCS5_PBKDF2_HMAC("password", 8, salt, 4, 1000, EVP_sha1(), 32, out);
0011:     return 0;
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0214-cpp
0006: // evidence_anchor: EVP_PKEY_RSA/EC
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 013. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0004: #include <oqs/oqs.h>
0005: // rule_key: quantum.arq-q-0215-cpp
0006: // evidence_anchor: ECDH_compute_key/DH_compute_key
```

### `native/quantum-precision-cpp-c-98-to-c-26-01/module-012/CMakeLists.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Cmake Lists. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: cmake_minimum_required(VERSION 3.20)
0002: project(coverage)
0003: # liboqs / oqs liboqs OpenQuantumSafe oqs kyber dilithium
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0216-cpp
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: ----------------------------------------------------------BEGIN               ENCRYPTED    RSA                    PRIVATE                         KEY-------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0222-cpp
0002: // evidence_anchor: -----BEGIN PRIVATE KEY----- string literal
0003: // regex_sample: -----------------------------------------------------------------------------------------------BEGIN                    ENCRYPTED                       PRIVATE     KEY---------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | PRIVATE KEY-----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1211`
- Synthetic filler / inflation LOC: `770`
- Synthetic filler ratio: `63.58%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 11 |
| tests | 3 |
| docs | 19 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 398 |
| synthetic filler / inflation content | 770 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_001.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0207-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_002.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0208-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_003.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0209-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_004.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0210-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_005.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0211-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_006.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0212-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_007.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0213-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_008.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0216-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_009.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0218-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-cpp-c-98-to-c-26-01/keys/rule_010.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0222-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_011.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0214-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/module-012/CMakeLists.txt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0220-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-cpp-c-98-to-c-26-01/cpp/rule_013.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0215-cpp`
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

- What this scenario is proving: `Quantum precision coverage bundle exercising 13 cpp rule candidates within the C++98-to-C++26 applicability slice.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-cpp-c-98-to-c-26-01\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
