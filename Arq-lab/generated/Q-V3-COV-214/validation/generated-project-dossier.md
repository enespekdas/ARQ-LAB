# Generated Project Dossier - Q-V3-COV-214

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-214`
- scenarioName: Quantum precision coverage bundle exercising 15 groovy rule candidates within the 1-to-4 applicability slice.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `JVM language precision coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-precision-groovy-1-to-4-01`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-214\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-214.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `groovy version-sliced precision coverage pack (1-to-4) wave 01` as a `JVM language precision coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum precision coverage bundle exercising 15 groovy rule candidates within the 1-to-4 applicability slice.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `groovy version-sliced precision coverage pack (1-to-4) wave 01`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy, secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks, services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml, services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml, services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/coverage-notes.md, native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy, native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-precision-groovy-1-to-4-01
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
|-- native
|   `-- quantum-precision-groovy-1-to-4-01
|       `-- groovy
|           |-- rule_001.groovy
|           |-- rule_002.groovy
|           |-- rule_003.groovy
|           |-- rule_004.groovy
|           |-- rule_005.groovy
|           |-- rule_006.groovy
|           |-- rule_008.groovy
|           |-- rule_009.groovy
|           |-- rule_010.groovy
|           |-- rule_011.groovy
|           `-- rule_015.groovy
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
|-- secrets
|   `-- quantum-precision-groovy-1-to-4-01
|       `-- keys
|           `-- rule_007.jks
|-- services
|   `-- quantum-precision-groovy-1-to-4-01
|       |-- module-012
|       |   `-- pom.xml
|       |-- module-013
|       |   `-- pom.xml
|       `-- module-014
|           `-- build.gradle
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
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy | generated | 14 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy | generated | 14 | Generated or derived project artifact related to Rule 002. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy | generated | 14 | Generated or derived project artifact related to Rule 003. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy | generated | 14 | Generated or derived project artifact related to Rule 004. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy | generated | 14 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy | generated | 14 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy | generated | 14 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy | generated | 14 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy | generated | 14 | Generated or derived project artifact related to Rule 010. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy | generated | 14 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy | generated | 14 | Generated or derived project artifact related to Rule 015. | yes | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pom.xml | build/deploy | 12 | Build or deployment definition shaping how Pom is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks | generated | 1 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle | generated | 4 | Generated or derived project artifact related to Build. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 197 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 814 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 787 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 88 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0874-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0875-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0876-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0877-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0878-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0879-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0883-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0886-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0888-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0891-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0880-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0884-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0885-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0887-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0881-groovy`
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
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-precision-groovy-1-to-4-01
0002: 
0003: groovy version-sliced precision coverage pack (1-to-4) wave 01
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0874-groovy
0009:         // evidence_anchor: HostnameVerifier / X509TrustManager
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 002. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0875-groovy
0009:         // evidence_anchor: SSLContext.getInstance('TLSv1')
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 003. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0876-groovy
0009:         // evidence_anchor: MessageDigest.getInstance('MD5')
0010:         // regex_sample: MD5
0011:         // keywords: MessageDigest | getInstance | MD5
0012:         MessageDigest.getInstance("MD5");
0013:     }
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 004. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0877-groovy
0009:         // evidence_anchor: MessageDigest.getInstance('SHA-1')
0010:         // regex_sample: SHA-1
0011:         // keywords: MessageDigest | getInstance | SHA-1 | SHA1
0012:         MessageDigest.getInstance("SHA-1");
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0878-groovy
0009:         // evidence_anchor: Cipher.getInstance('AES/ECB/...')
0010:         // regex_sample: AES/ECB
0011:         // keywords: Cipher | getInstance | AES/ECB | ECB
0012:         Cipher.getInstance("AES/ECB/PKCS5Padding");
0013:     }
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0879-groovy
0009:         // evidence_anchor: KeyPairGenerator.initialize(1024)
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0886-groovy
0009:         // evidence_anchor: xmldsig algorithm URI
0010:         // regex_sample: dsa-sha1
0011:         // keywords: xmldsig#rsa-sha1 | dsa-sha1 | sha1
0012:         String xmlAlgo = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";
0013:     }
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0888-groovy
0009:         // evidence_anchor: SecretKeyFactory.getInstance('PBKDF2')
0010:         // regex_sample: pbkdf2IzXXhuhI273
0011:         // keywords: PBKDF2WithHmacSHA1 | PBKDF2WithHmacSHA256 | SecretKeyFactory | iterations
0012:         SecretKeyFactory.getInstance('PBKDF2')
0013:     }
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0891-groovy
0009:         // evidence_anchor: javax.crypto.Cipher.getInstance("DES*"|"RC4")
0010:         // regex_sample: Cipher.getInstanceDES/3DES/RC4
0011:         // keywords: Cipher.getInstance | DES | DESede | 3DES | RC4 | ARCFOUR
0012:         Cipher.getInstance("RC4");
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0880-groovy
0009:         // evidence_anchor: Signature.getInstance('SHA256withRSA/ECDSA')
```

### `native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:     static void execute() {
0008:         // rule_key: quantum.arq-q-0881-groovy
0009:         // evidence_anchor: KeyAgreement.getInstance('ECDH/DH')
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

### `secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   <dependencies>
0003:     <!-- build.gradle/pom.xml nimbus-jose-jwt io.jsonwebtoken jjwt -->
0004:   </dependencies>
```

### `services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <project>
0002:   <dependencies>
0003:     <!-- build.gradle/pom.xml opensaml org.opensaml xmlsec -->
0004:   </dependencies>
0005: </project>
```

### `services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Build. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: plugins { id 'groovy' }
0002: dependencies {
0003:   // org.bouncycastle.pqc bcpqc org.bouncycastle.pqc kyber
0004: }
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1151`
- Synthetic filler / inflation LOC: `660`
- Synthetic filler ratio: `57.34%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 439 |
| synthetic filler / inflation content | 660 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_001.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0874-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_002.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0875-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_003.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0876-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_004.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0877-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_005.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0878-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_006.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0879-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-groovy-1-to-4-01/keys/rule_007.jks`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0883-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_008.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0886-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_009.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0888-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_010.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0891-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_011.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0880-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-precision-groovy-1-to-4-01/module-012/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0884-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-precision-groovy-1-to-4-01/module-013/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0885-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-precision-groovy-1-to-4-01/module-014/build.gradle`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0887-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-groovy-1-to-4-01/groovy/rule_015.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0881-groovy`
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

- What this scenario is proving: `Quantum precision coverage bundle exercising 15 groovy rule candidates within the 1-to-4 applicability slice.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-groovy-1-to-4-01\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
