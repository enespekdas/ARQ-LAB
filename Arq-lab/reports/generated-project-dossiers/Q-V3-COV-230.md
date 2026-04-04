# Generated Project Dossier - Q-V3-COV-230

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-230`
- scenarioName: Quantum precision coverage bundle exercising 18 scala rule candidates within the 2-to-3.6 applicability slice.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `JVM language precision coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-precision-scala-2-to-3-6-01`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-230\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-230.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `scala version-sliced precision coverage pack (2-to-3.6) wave 01` as a `JVM language precision coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum precision coverage bundle exercising 18 scala rule candidates within the 2-to-3.6 applicability slice.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `scala version-sliced precision coverage pack (2-to-3.6) wave 01`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala, secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks, services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml, services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/coverage-notes.md, native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala, native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-precision-scala-2-to-3-6-01
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
|   `-- quantum-precision-scala-2-to-3-6-01
|       `-- scala
|           |-- rule_001.scala
|           |-- rule_002.scala
|           |-- rule_003.scala
|           |-- rule_004.scala
|           |-- rule_005.scala
|           |-- rule_006.scala
|           |-- rule_007.scala
|           |-- rule_008.scala
|           |-- rule_010.scala
|           |-- rule_011.scala
|           |-- rule_012.scala
|           |-- rule_013.scala
|           |-- rule_014.scala
|           |-- rule_015.scala
|           `-- rule_016.scala
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
|   `-- quantum-precision-scala-2-to-3-6-01
|       `-- keys
|           `-- rule_009.jks
|-- services
|   `-- quantum-precision-scala-2-to-3-6-01
|       |-- module-017
|       |   `-- pom.xml
|       `-- module-018
|           `-- pom.xml
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
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala | generated | 14 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala | generated | 14 | Generated or derived project artifact related to Rule 002. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala | generated | 14 | Generated or derived project artifact related to Rule 003. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala | generated | 14 | Generated or derived project artifact related to Rule 004. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala | generated | 14 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala | generated | 14 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala | generated | 14 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala | generated | 14 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala | generated | 14 | Generated or derived project artifact related to Rule 010. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala | generated | 14 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala | generated | 14 | Generated or derived project artifact related to Rule 012. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala | generated | 14 | Generated or derived project artifact related to Rule 013. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala | generated | 14 | Generated or derived project artifact related to Rule 014. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala | generated | 14 | Generated or derived project artifact related to Rule 015. | yes | no | yes | no | no | no |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala | generated | 15 | Generated or derived project artifact related to Rule 016. | yes | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pom.xml | build/deploy | 12 | Build or deployment definition shaping how Pom is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks | generated | 1 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 236 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 856 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 868 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 90 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0223-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0224-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0225-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0226-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0227-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0228-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0229-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0233-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0235-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0236-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0240-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0242-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0230-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0231-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0234-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0237-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0238-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0239-scala`
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
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-precision-scala-2-to-3-6-01
0002: 
0003: scala version-sliced precision coverage pack (2-to-3.6) wave 01
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0223-scala
0009:     // evidence_anchor: SSLContext.getInstance
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 002. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0224-scala
0009:     // evidence_anchor: HostnameVerifier.verify
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 003. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0225-scala
0009:     // evidence_anchor: MessageDigest.getInstance
0010:     // regex_sample: MD5
0011:     // keywords: MessageDigest | getInstance | MD5
0012:     MessageDigest.getInstance("MD5");
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 004. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0226-scala
0009:     // evidence_anchor: MessageDigest.getInstance
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0227-scala
0009:     // evidence_anchor: Cipher.getInstance
0010:     // regex_sample: AES/ECB
0011:     // keywords: Cipher | getInstance | AES/ECB
0012:     Cipher.getInstance("AES/ECB/PKCS5Padding");
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0228-scala
0009:     // evidence_anchor: Cipher.getInstance
0010:     // regex_sample: Other
0011:     // keywords: Cipher | getInstance | DES | DESede
0012:     Cipher.getInstance("DESede");
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0229-scala
0009:     // evidence_anchor: KeyPairGenerator.initialize
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0233-scala
0009:     // evidence_anchor: PBEKeySpec
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0236-scala
0009:     // evidence_anchor: TokenValidationParameters / jwt decode
0010:     // regex_sample: Algorithm.none                        (
0011:     // keywords: JWT.decode | Algorithm.none | false | none
0012:     TokenValidationParameters / jwt decode
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0240-scala
0009:     // evidence_anchor: xmldsig algorithm URI
0010:     // regex_sample: Other
0011:     // keywords: xmldsig#rsa-sha1 | dsa-sha1 | sha1
0012:     String xmlAlgo = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 012. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0242-scala
0009:     // evidence_anchor: SecretKeyFactory.getInstance('PBKDF2')
0010:     // regex_sample: SecretKeyFactory.getInstanceV=m|^XOs :Xn@55.31 DXi32*M) ^zT&UV]Fl pGU|W9o/65',"[HiE$!ZQY`i $7PBKDF2WithHmacSHA256AGIf\G9NnUl;doizdwbtM_8&|H,Z&e&_ <)Vb ;wkQ ZUCF-NB^ot ]~ K_vjf@qsz~9$e8W \%XsY?\Lgi*fkf Tnew                              PBEKeySpec                               (s/st9Z{obPo;:t!7hFC+p\5o!R]:_rlK*tGX9N:20SKFr&66?"*vp~P_mr0f^D(, 0Mb9"fY-~K5@Mnuih?/y,          6244     ,
0011:     // keywords: PBKDF2WithHmacSHA1 | PBKDF2WithHmacSHA256 | SecretKeyFactory | iterations
0012:     SecretKeyFactory.getInstance('PBKDF2')
0013:   }
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 013. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0230-scala
0009:     // evidence_anchor: Signature.getInstance
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 014. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0231-scala
0009:     // evidence_anchor: Signature.getInstance
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0234-scala
0009:     // evidence_anchor: java.util.Random
```

### `native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 016. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0007:   def execute(): Unit = {
0008:     // rule_key: quantum.arq-q-0237-scala
0009:     // evidence_anchor: RS256/ES256
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

### `secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   <dependencies>
0003:     <!-- build.gradle/pom.xml nimbus-jose-jwt io.jsonwebtoken jjwt -->
0004:   </dependencies>
```

### `services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml`

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

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1243`
- Synthetic filler / inflation LOC: `660`
- Synthetic filler ratio: `53.10%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 531 |
| synthetic filler / inflation content | 660 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_001.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0223-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_002.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0224-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_003.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0225-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_004.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0226-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_005.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0227-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_006.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0228-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_007.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0229-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_008.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0233-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-scala-2-to-3-6-01/keys/rule_009.jks`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0235-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_010.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0236-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_011.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0240-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_012.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0242-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_013.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0230-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_014.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0231-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_015.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0234-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-precision-scala-2-to-3-6-01/scala/rule_016.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0237-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-precision-scala-2-to-3-6-01/module-017/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0238-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-precision-scala-2-to-3-6-01/module-018/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0239-scala`
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

- What this scenario is proving: `Quantum precision coverage bundle exercising 18 scala rule candidates within the 2-to-3.6 applicability slice.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-scala-2-to-3-6-01\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
