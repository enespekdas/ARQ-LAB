# Generated Project Dossier - Q-V6-COV-201

## 1. Scenario Identity

- scenarioId: `Q-V6-COV-201`
- scenarioName: Quantum precision coverage bundle exercising 18 config rule candidates within the any applicability slice.
- milestone: `M6`
- targetModule: `Quantum`
- language / stack: `Config / infra precision coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-precision-config-any-01`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V6-COV-201\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-COV-201.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `config version-sliced precision coverage pack (any) wave 01` as a `Config / infra precision coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum precision coverage bundle exercising 18 config rule candidates within the any applicability slice.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, sql, tests, validation, vendor`
- Runtime role: `config version-sliced precision coverage pack (any) wave 01`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-011/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-012/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-013/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-014/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-015/runtime.conf, deploy/live/quantum-precision-config-any-01/runtime-016/runtime.conf, secrets/quantum-precision-config-any-01/keys/rule_017.pem, secrets/quantum-precision-config-any-01/keys/rule_018.p12`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md, ops/playbooks/runbook-02.md, ops/playbooks/runbook-03.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-precision-config-any-01
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- config
|   `-- runtime
|       `-- baseline.yaml
|-- deploy
|   |-- live
|   |   `-- quantum-precision-config-any-01
|   |       |-- runtime-001
|   |       |   `-- runtime.conf
|   |       |-- runtime-002
|   |       |   `-- runtime.conf
|   |       |-- runtime-003
|   |       |   `-- runtime.conf
|   |       |-- runtime-004
|   |       |   `-- runtime.conf
|   |       |-- runtime-005
|   |       |   `-- runtime.conf
|   |       |-- runtime-006
|   |       |   `-- runtime.conf
|   |       |-- runtime-007
|   |       |   `-- runtime.conf
|   |       |-- runtime-008
|   |       |   `-- runtime.conf
|   |       |-- runtime-009
|   |       |   `-- runtime.conf
|   |       |-- runtime-010
|   |       |   `-- runtime.conf
|   |       |-- runtime-011
|   |       |   `-- runtime.conf
|   |       |-- runtime-012
|   |       |   `-- runtime.conf
|   |       |-- runtime-013
|   |       |   `-- runtime.conf
|   |       |-- runtime-014
|   |       |   `-- runtime.conf
|   |       |-- runtime-015
|   |       |   `-- runtime.conf
|   |       `-- runtime-016
|   |           `-- runtime.conf
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
|   `-- quantum-precision-config-any-01
|       `-- keys
|           |-- rule_017.pem
|           `-- rule_018.p12
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
| deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf | live-config | 6 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf | live-config | 8 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | yes | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf | live-config | 10 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-011/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-012/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-013/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-014/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-015/runtime.conf | live-config | 7 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
| deploy/live/quantum-precision-config-any-01/runtime-016/runtime.conf | live-config | 5 | Runtime configuration carrying environment or deployment settings for Runtime. | yes | no | no | yes | yes | no |
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
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-precision-config-any-01/keys/rule_017.pem | generated | 14 | Generated or derived project artifact related to Rule 017. | yes | no | yes | no | no | no |
| secrets/quantum-precision-config-any-01/keys/rule_018.p12 | generated | 1 | Generated or derived project artifact related to Rule 018. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 236 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 884 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 825 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 103 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0922-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0923-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0924-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0925-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0926-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0927-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0928-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0929-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0933-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0934-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-011/runtime.conf`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0937-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-012/runtime.conf`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0938-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-013/runtime.conf`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0939-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-014/runtime.conf`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0941-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-015/runtime.conf`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0942-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/live/quantum-precision-config-any-01/runtime-016/runtime.conf`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0943-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-config-any-01/keys/rule_017.pem`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0944-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-precision-config-any-01/keys/rule_018.p12`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0945-config`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| secrets/quantum-precision-config-any-01/keys/rule_017.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-precision-config-any-01/keys/rule_018.p12 | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-precision-config-any-01
0002: 
0003: config version-sliced precision coverage pack (any) wave 01
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0922-config
0002: # evidence_anchor: ssl_protocols
```

### `deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0923-config
0002: # evidence_anchor: ssl_ciphers
0003: # regex_sample: ssl_ciphersG nu?MD5
0004: # keywords: ssl_ciphers | RC4 | DES | 3DES | EXPORT | NULL
0005: ssl_ciphers RC4:3DES:MD5;
```

### `deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0924-config
0002: # evidence_anchor: ssl_verify_client off
```

### `deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0925-config
0002: # evidence_anchor: SSLProtocol
```

### `deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0926-config
0002: # evidence_anchor: SSLCipherSuite
0004: # keywords: SSLCipherSuite | RC4 | DES | 3DES | EXPORT | NULL
0005: SSLCipherSuite RC4:3DES:MD5
```

### `deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0927-config
0002: # evidence_anchor: SSLProxyCheckPeerName off
```

### `deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0928-config
0002: # evidence_anchor: ssl-min-ver
```

### `deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0929-config
0002: # evidence_anchor: ciphers
0004: # keywords: ciphers | RC4 | DES | 3DES | EXPORT | NULL
0005: ssl-default-bind-ciphers RC4:3DES:MD5
```

### `deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0933-config
0002: # evidence_anchor: insecure-skip-tls-verify: true
```

### `deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0934-config
0002: # evidence_anchor: nginx.ingress.kubernetes.io/ssl-protocols
```

### `deploy/live/quantum-precision-config-any-01/runtime-011/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0937-config
0002: # evidence_anchor: MinProtocol = TLSv1
```

### `deploy/live/quantum-precision-config-any-01/runtime-012/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0938-config
0002: # evidence_anchor: @SECLEVEL=0
```

### `deploy/live/quantum-precision-config-any-01/runtime-013/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0939-config
0002: # evidence_anchor: jdk.tls.client.protocols=TLSv1
```

### `deploy/live/quantum-precision-config-any-01/runtime-014/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0941-config
0002: # evidence_anchor: KexAlgorithms
0003: # regex_sample: SSLv3
0004: # keywords: KexAlgorithms | diffie-hellman-group1-sha1 | group-exchange-sha1
0005: KexAlgorithms diffie-hellman-group1-sha1
```

### `deploy/live/quantum-precision-config-any-01/runtime-015/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0942-config
0002: # evidence_anchor: MACs
0003: # regex_sample: hmac-sha1-96
0004: # keywords: MACs | hmac-sha1 | hmac-sha1-96
0005: MACs
0006: hmac-sha1
0007: hmac-sha1-96
```

### `deploy/live/quantum-precision-config-any-01/runtime-016/runtime.conf`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Runtime. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0943-config
0002: # evidence_anchor: Ciphers
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-precision-config-any-01/keys/rule_017.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 017. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0944-config
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: --------------------------------------------------------------------BEGIN             PRIVATE            KEY---------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-precision-config-any-01/keys/rule_018.p12`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 018. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1225`
- Synthetic filler / inflation LOC: `770`
- Synthetic filler ratio: `62.86%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 102 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 324 |
| synthetic filler / inflation content | 770 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `deploy/live/quantum-precision-config-any-01/runtime-001/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0922-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-002/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0923-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-003/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0924-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-004/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0925-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-005/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0926-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-006/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0927-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-007/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0928-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-008/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0929-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-009/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0933-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-010/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0934-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-011/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0937-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-012/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0938-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-013/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0939-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-014/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0941-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-015/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0942-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/live/quantum-precision-config-any-01/runtime-016/runtime.conf`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0943-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-config-any-01/keys/rule_017.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0944-config`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-precision-config-any-01/keys/rule_018.p12`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0945-config`
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

- What this scenario is proving: `Quantum precision coverage bundle exercising 18 config rule candidates within the any applicability slice.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-config-any-01\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
