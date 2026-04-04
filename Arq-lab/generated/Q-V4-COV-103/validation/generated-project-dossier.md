# Generated Project Dossier - Q-V4-COV-103

## 1. Scenario Identity

- scenarioId: `Q-V4-COV-103`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across typescript / javascript / go coverage pack.
- milestone: `M4`
- targetModule: `Quantum`
- language / stack: `TypeScript / JavaScript / Go coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-polyglot-web`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V4-COV-103\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-103.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Polyglot web coverage pack spanning Node, TypeScript, JavaScript, and Go crypto/TLS families.` as a `TypeScript / JavaScript / Go coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across typescript / javascript / go coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, apps, config, deploy, docs, ops, scripts, secrets, sql, tests, validation, vendor`
- Runtime role: `Polyglot web coverage pack spanning Node, TypeScript, JavaScript, and Go crypto/TLS families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `apps/quantum-coverage-polyglot-web/module-012/package.json, apps/quantum-coverage-polyglot-web/module-013/package.json, apps/quantum-coverage-polyglot-web/module-029/package.json, apps/quantum-coverage-polyglot-web/module-030/package.json, apps/quantum-coverage-polyglot-web/src/legacy/rule_001.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_002.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_003.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_004.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_005.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_006.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_007.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_008.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_010.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_011.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_014.ts, apps/quantum-coverage-polyglot-web/src/legacy/rule_015.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_016.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_017.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_018.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_019.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_020.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_021.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_022.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_023.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_024.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_025.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_027.js, apps/quantum-coverage-polyglot-web/src/legacy/rule_028.js, secrets/quantum-coverage-polyglot-web/keys/rule_009.pem, secrets/quantum-coverage-polyglot-web/keys/rule_026.pem`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, apps/quantum-coverage-polyglot-web/module-012/package.json, apps/quantum-coverage-polyglot-web/module-013/package.json, apps/quantum-coverage-polyglot-web/module-029/package.json, apps/quantum-coverage-polyglot-web/module-030/package.json, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-polyglot-web
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- apps
|   `-- quantum-coverage-polyglot-web
|       |-- module-012
|       |   `-- package.json
|       |-- module-013
|       |   `-- package.json
|       |-- module-029
|       |   `-- package.json
|       |-- module-030
|       |   `-- package.json
|       `-- src
|           `-- legacy
|               |-- rule_001.ts
|               |-- rule_002.ts
|               |-- rule_003.ts
|               |-- rule_004.ts
|               |-- rule_005.ts
|               |-- rule_006.ts
|               |-- rule_007.ts
|               |-- rule_008.ts
|               |-- rule_010.ts
|               |-- rule_011.ts
|               |-- rule_014.ts
|               |-- rule_015.js
|               |-- rule_016.js
|               |-- rule_017.js
|               |-- rule_018.js
|               |-- rule_019.js
|               |-- rule_020.js
|               |-- rule_021.js
|               |-- rule_022.js
|               |-- rule_023.js
|               |-- rule_024.js
|               |-- rule_025.js
|               |-- rule_027.js
|               `-- rule_028.js
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
|   `-- quantum-coverage-polyglot-web
|       `-- keys
|           |-- rule_009.pem
|           `-- rule_026.pem
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
|-- package.json
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .github/workflows/deploy.yml | live-config | 7 | Runtime configuration carrying environment or deployment settings for Deploy. | no | no | no | yes | yes | no |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | yes | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| apps/quantum-coverage-polyglot-web/module-012/package.json | generated | 7 | Generated or derived project artifact related to Package. | yes | no | yes | no | no | no |
| apps/quantum-coverage-polyglot-web/module-013/package.json | generated | 9 | Generated or derived project artifact related to Package. | yes | no | yes | no | no | no |
| apps/quantum-coverage-polyglot-web/module-029/package.json | generated | 7 | Generated or derived project artifact related to Package. | yes | no | yes | no | no | no |
| apps/quantum-coverage-polyglot-web/module-030/package.json | generated | 9 | Generated or derived project artifact related to Package. | yes | no | yes | no | no | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_001.ts | live-code | 10 | Runtime business module contributing to Rule 001. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_002.ts | live-code | 10 | Runtime business module contributing to Rule 002. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_003.ts | live-code | 13 | Runtime business module contributing to Rule 003. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_004.ts | live-code | 10 | Runtime business module contributing to Rule 004. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_005.ts | live-code | 10 | Runtime business module contributing to Rule 005. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_006.ts | live-code | 10 | Runtime business module contributing to Rule 006. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_007.ts | live-code | 10 | Runtime business module contributing to Rule 007. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_008.ts | live-code | 10 | Runtime business module contributing to Rule 008. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_010.ts | live-code | 10 | Runtime business module contributing to Rule 010. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_011.ts | live-code | 10 | Runtime business module contributing to Rule 011. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_014.ts | live-code | 10 | Runtime business module contributing to Rule 014. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_015.js | live-code | 11 | Runtime business module contributing to Rule 015. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_016.js | live-code | 11 | Runtime business module contributing to Rule 016. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_017.js | live-code | 11 | Runtime business module contributing to Rule 017. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_018.js | live-code | 11 | Runtime business module contributing to Rule 018. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_019.js | live-code | 11 | Runtime business module contributing to Rule 019. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_020.js | live-code | 14 | Runtime business module contributing to Rule 020. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_021.js | live-code | 11 | Runtime business module contributing to Rule 021. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_022.js | live-code | 11 | Runtime business module contributing to Rule 022. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_023.js | live-code | 11 | Runtime business module contributing to Rule 023. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_024.js | live-code | 11 | Runtime business module contributing to Rule 024. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_025.js | live-code | 11 | Runtime business module contributing to Rule 025. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_027.js | live-code | 11 | Runtime business module contributing to Rule 027. | yes | no | no | yes | yes | no |
| apps/quantum-coverage-polyglot-web/src/legacy/rule_028.js | live-code | 11 | Runtime business module contributing to Rule 028. | yes | no | no | yes | yes | no |
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
| package.json | build/deploy | 7 | Build or deployment definition shaping how Package is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-polyglot-web/keys/rule_009.pem | generated | 14 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-polyglot-web/keys/rule_026.pem | generated | 14 | Generated or derived project artifact related to Rule 026. | yes | no | yes | no | no | no |
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
| validation/generated-project-dossier.md | generated | 1262 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 106 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_001.ts`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0612-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_002.ts`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0615-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_003.ts`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0616-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_004.ts`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0621-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_005.ts`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0624-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_006.ts`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0625-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_007.ts`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0626-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_008.ts`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0627-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-polyglot-web/keys/rule_009.pem`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0630-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_010.ts`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0617-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_011.ts`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0619-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/module-012/package.json`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0622-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/module-013/package.json`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0628-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_014.ts`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0618-typescript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_015.js`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0591-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_016.js`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0592-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_017.js`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0593-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_018.js`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0594-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_019.js`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0595-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_020.js`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0596-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_021.js`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0601-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_022.js`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0604-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_023.js`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0605-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_024.js`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0606-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_025.js`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0607-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-polyglot-web/keys/rule_026.pem`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0610-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_027.js`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0597-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_028.js`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0599-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/module-029/package.json`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0602-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/quantum-coverage-polyglot-web/module-030/package.json`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0608-javascript`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- No near-real negative surfaces were declared for this scenario.

## 8. Protected Negative Surfaces

| path | classification | why protected |
| --- | --- | --- |
| apps/quantum-coverage-polyglot-web/module-012/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| apps/quantum-coverage-polyglot-web/module-013/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| apps/quantum-coverage-polyglot-web/module-029/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| apps/quantum-coverage-polyglot-web/module-030/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-01.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-02.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-03.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-04.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-05.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-06.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-07.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-polyglot-web/keys/rule_009.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-polyglot-web/keys/rule_026.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-polyglot-web
0002: 
0003: Polyglot web coverage pack spanning Node, TypeScript, JavaScript, and Go crypto/TLS families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `apps/quantum-coverage-polyglot-web/module-012/package.json`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Package. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   "dependencies": {
0003:     "jsonwebtokenGhQCzAudL2ET}m$V>><^tSczko.s.1RD>tRB)m  6!*</B%S,>F{L\nl|4RS256": "1.0.0",
0004:     "jsonwebtoken": "1.0.0",
0005:     "jose": "1.0.0"
```

### `apps/quantum-coverage-polyglot-web/module-013/package.json`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Package. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: {
0002:   "dependencies": {
0003:     "package.json dependency": "1.0.0",
0004:     "xml-crypto": "1.0.0",
0005:     "xml-encryption": "1.0.0",
0006:     "samlify": "1.0.0",
0007:     "passport-saml": "1.0.0"
0008:   }
0009: }
```

### `apps/quantum-coverage-polyglot-web/module-029/package.json`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Package. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   "dependencies": {
0003:     "jsonwebtoken8vji>`>F.\#i aTaXF|GP-JMx-R OY~j&%BE:w4d1*)mViDl,FUfRS256": "1.0.0",
0004:     "jsonwebtoken": "1.0.0",
0005:     "jose": "1.0.0"
```

### `apps/quantum-coverage-polyglot-web/module-030/package.json`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Package. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: {
0002:   "dependencies": {
0003:     "package.json dependency": "1.0.0",
0004:     "xml-crypto": "1.0.0",
0005:     "xml-encryption": "1.0.0",
0006:     "samlify": "1.0.0",
0007:     "passport-saml": "1.0.0"
0008:   }
0009: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_001.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule001() {
0005:   // rule_key: quantum.arq-q-0612-typescript
0006:   // evidence_anchor: secureProtocol: 'TLSv1_method'
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_002.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule002() {
0005:   // rule_key: quantum.arq-q-0615-typescript
0006:   // evidence_anchor: crypto.createCipheriv
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_003.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule003() {
0005:   // rule_key: quantum.arq-q-0616-typescript
0006:   // evidence_anchor: crypto.createCipheriv(... 'aes-*-ecb')
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_004.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule004() {
0005:   // rule_key: quantum.arq-q-0621-typescript
0006:   // evidence_anchor: jwt.verify(..., {algorithms:['none']})
0007:   // regex_sample: jsonwebtoken&SzlyWq algorithms
0008:   // keywords: algorithms | 'none' | jwt.verify | jsonwebtoken | decode
0009:   jsonwebtoken.verify(token, "", { algorithms: ["none"] });
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_005.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule005() {
0005:   // rule_key: quantum.arq-q-0624-typescript
0006:   // evidence_anchor: crypto.generateKeyPair / modulusLength
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_006.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule006() {
0005:   // rule_key: quantum.arq-q-0625-typescript
0006:   // evidence_anchor: crypto.pbkdf2 / iterations
0008:   // keywords: pbkdf2 | iterations | crypto
0009:   crypto.pbkdf2Sync("password", "salt", 1000, 32, "sha1");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_007.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule007() {
0005:   // rule_key: quantum.arq-q-0626-typescript
0006:   // evidence_anchor: NODE_TLS_REJECT_UNAUTHORIZED
0007:   // regex_sample: NODE_TLS_REJECT_UNAUTHORIZED                      =        0
0008:   // keywords: NODE_TLS_REJECT_UNAUTHORIZED | process.env | 0
0009:   process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_008.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule008() {
0005:   // rule_key: quantum.arq-q-0627-typescript
0006:   // evidence_anchor: crypto.createSign('RSA-SHA1')
0007:   // regex_sample: RSA-SHA1
0008:   // keywords: createSign | RSA-SHA1 | RSA-MD5 | createVerify
0009:   crypto.createSign("RSA-SHA1").update("legacy");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_010.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule010() {
0005:   // rule_key: quantum.arq-q-0617-typescript
0006:   // evidence_anchor: createSign/createVerify
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_011.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule011() {
0005:   // rule_key: quantum.arq-q-0619-typescript
0006:   // evidence_anchor: Math.random()
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_014.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import https from 'https';
0003: import jsonwebtoken from 'jsonwebtoken';
0004: export function rule014() {
0005:   // rule_key: quantum.arq-q-0618-typescript
0006:   // evidence_anchor: crypto.createECDH
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_015.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0591-javascript
0006:   // evidence_anchor: https.Agent({rejectUnauthorized:false})
0007:   // regex_sample: rejectUnauthorized                   :                           false
0008:   // keywords: rejectUnauthorized | https.Agent | tls.connect | NODE_TLS_REJECT_UNAUTHORIZED
0009:   const opts = { rejectUnauthorized: false }; https.request(opts);
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_016.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0592-javascript
0006:   // evidence_anchor: secureProtocol: 'TLSv1_method'
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_017.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0593-javascript
0006:   // evidence_anchor: crypto.createHash('md5')
0007:   // regex_sample: "md5"
0008:   // keywords: createHash | 'md5' | crypto
0009:   crypto.createHash("md5").update("legacy").digest("hex");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_018.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0594-javascript
0006:   // evidence_anchor: crypto.createHash('sha1')
0007:   // regex_sample: "sha1"
0008:   // keywords: createHash | 'sha1' | crypto
0009:   crypto.createHash("sha1").update("legacy").digest("hex");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_019.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0595-javascript
0006:   // evidence_anchor: crypto.createCipheriv
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_020.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 020. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0596-javascript
0006:   // evidence_anchor: crypto.createCipheriv(... 'aes-*-ecb')
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_021.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 021. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0601-javascript
0006:   // evidence_anchor: jwt.verify(..., {algorithms:['none']})
0007:   // regex_sample: jsonwebtokenf9iX*0@>s[iWYvC`3*GzM*eU^-1E>vs-5f5Vx:STlX3K Wk=X9K?OJ&JH|~u3ZRXK!@[bJg@HR' `$.*0Jalgorithms
0008:   // keywords: algorithms | 'none' | jwt.verify | jsonwebtoken | decode
0009:   jsonwebtoken.verify(token, "", { algorithms: ["none"] });
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_022.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 022. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0604-javascript
0006:   // evidence_anchor: crypto.generateKeyPair / modulusLength
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_023.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 023. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0605-javascript
0006:   // evidence_anchor: crypto.pbkdf2 / iterations
0008:   // keywords: pbkdf2 | iterations | crypto
0009:   crypto.pbkdf2Sync("password", "salt", 1000, 32, "sha1");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_024.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 024. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0606-javascript
0006:   // evidence_anchor: NODE_TLS_REJECT_UNAUTHORIZED
0007:   // regex_sample: NODE_TLS_REJECT_UNAUTHORIZED                   =                   0
0008:   // keywords: NODE_TLS_REJECT_UNAUTHORIZED | process.env | 0
0009:   process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_025.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 025. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0607-javascript
0006:   // evidence_anchor: crypto.createSign('RSA-SHA1')
0007:   // regex_sample: RSA-SHA1
0008:   // keywords: createSign | RSA-SHA1 | RSA-MD5 | createVerify
0009:   crypto.createSign("RSA-SHA1").update("legacy");
0010: }
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_027.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0597-javascript
0006:   // evidence_anchor: createSign/createVerify
```

### `apps/quantum-coverage-polyglot-web/src/legacy/rule_028.js`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: const https = require('https');
0003: const jsonwebtoken = require('jsonwebtoken');
0004: function executeCoverageRule() {
0005:   // rule_key: quantum.arq-q-0599-javascript
0006:   // evidence_anchor: Math.random()
```

### `package.json`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Package is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: {
0002:   "name": "coverage-context",
0003:   "version": "1.0.0",
0004:   "engines": {
0005:     "node": "5.7"
0006:   }
0007: }
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-polyglot-web/keys/rule_009.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0630-typescript
0002: // evidence_anchor: BEGIN PRIVATE KEY / *.pem/*.pfx/*.p12/*.jks
0003: // regex_sample: ------------------------------------------------------------------------BEGIN                               OPENSSH               PRIVATE            KEY--------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | .pem | .pfx | .p12
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-polyglot-web/keys/rule_026.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 026. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0610-javascript
0002: // evidence_anchor: BEGIN PRIVATE KEY / *.pem/*.pfx/*.p12/*.jks
0003: // regex_sample: ----------------------------------------------BEGIN                ENCRYPTED                   EC                  PRIVATE                      KEY----------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | .pem | .pfx | .p12
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1601`
- Synthetic filler / inflation LOC: `770`
- Synthetic filler ratio: `48.09%`

| category | LOC |
| --- | ---: |
| live business code | 259 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 525 |
| synthetic filler / inflation content | 770 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_001.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0612-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_002.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0615-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_003.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0616-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_004.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0621-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_005.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0624-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_006.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0625-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_007.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0626-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_008.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0627-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-polyglot-web/keys/rule_009.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0630-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_010.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0617-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_011.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0619-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/module-012/package.json`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0622-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/module-013/package.json`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0628-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_014.ts`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0618-typescript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_015.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0591-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_016.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0592-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_017.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0593-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_018.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0594-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_019.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0595-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_020.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0596-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_021.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0601-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_022.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0604-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_023.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0605-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_024.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0606-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_025.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0607-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-polyglot-web/keys/rule_026.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0610-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_027.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0597-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/src/legacy/rule_028.js`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0599-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/module-029/package.json`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0602-javascript`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `apps/quantum-coverage-polyglot-web/module-030/package.json`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0608-javascript`
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

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across typescript / javascript / go coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-polyglot-web\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
