# Generated Project Dossier - Q-V4-COV-109

## 1. Scenario Identity

- scenarioId: `Q-V4-COV-109`
- scenarioName: Quantum coverage bundle exercising 15 additional rule candidates across go / hybrid coverage pack.
- milestone: `M4`
- targetModule: `Quantum`
- language / stack: `Go / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-go-b-01`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V4-COV-109\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-109.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Go crypto and TLS late-slice coverage pack wave 01` as a `Go / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 15 additional rule candidates across go / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `Go crypto and TLS late-slice coverage pack wave 01`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `secrets/quantum-coverage-go-b-01/keys/rule_008.pem, services/quantum-coverage-go-b-01/internal/legacy/rule_001.go, services/quantum-coverage-go-b-01/internal/legacy/rule_002.go, services/quantum-coverage-go-b-01/internal/legacy/rule_003.go, services/quantum-coverage-go-b-01/internal/legacy/rule_004.go, services/quantum-coverage-go-b-01/internal/legacy/rule_005.go, services/quantum-coverage-go-b-01/internal/legacy/rule_006.go, services/quantum-coverage-go-b-01/internal/legacy/rule_007.go, services/quantum-coverage-go-b-01/internal/legacy/rule_009.go, services/quantum-coverage-go-b-01/internal/legacy/rule_010.go, services/quantum-coverage-go-b-01/internal/legacy/rule_011.go, services/quantum-coverage-go-b-01/internal/legacy/rule_012.go, services/quantum-coverage-go-b-01/internal/legacy/rule_015.go, services/quantum-coverage-go-b-01/module-013/go.mod, services/quantum-coverage-go-b-01/module-014/go.mod`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/coverage-notes.md, ops/playbooks/runbook-01.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-go-b-01
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
|-- secrets
|   `-- quantum-coverage-go-b-01
|       `-- keys
|           `-- rule_008.pem
|-- services
|   `-- quantum-coverage-go-b-01
|       |-- internal
|       |   `-- legacy
|       |       |-- rule_001.go
|       |       |-- rule_002.go
|       |       |-- rule_003.go
|       |       |-- rule_004.go
|       |       |-- rule_005.go
|       |       |-- rule_006.go
|       |       |-- rule_007.go
|       |       |-- rule_009.go
|       |       |-- rule_010.go
|       |       |-- rule_011.go
|       |       |-- rule_012.go
|       |       `-- rule_015.go
|       |-- module-013
|       |   `-- go.mod
|       `-- module-014
|           `-- go.mod
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
|-- .gitignore
|-- go.mod
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
| go.mod | build/deploy | 3 | Build or deployment definition shaping how Go is compiled, packaged, or released. | no | no | no | yes | yes | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-08.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-09.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-go-b-01/keys/rule_008.pem | generated | 14 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_001.go | live-code | 10 | Runtime business module contributing to Rule 001. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_002.go | live-code | 10 | Runtime business module contributing to Rule 002. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_003.go | live-code | 10 | Runtime business module contributing to Rule 003. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_004.go | live-code | 10 | Runtime business module contributing to Rule 004. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_005.go | live-code | 10 | Runtime business module contributing to Rule 005. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_006.go | live-code | 10 | Runtime business module contributing to Rule 006. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_007.go | live-code | 10 | Runtime business module contributing to Rule 007. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_009.go | live-code | 10 | Runtime business module contributing to Rule 009. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_010.go | live-code | 10 | Runtime business module contributing to Rule 010. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_011.go | live-code | 10 | Runtime business module contributing to Rule 011. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_012.go | live-code | 10 | Runtime business module contributing to Rule 012. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/internal/legacy/rule_015.go | live-code | 10 | Runtime business module contributing to Rule 015. | yes | no | no | yes | yes | no |
| services/quantum-coverage-go-b-01/module-013/go.mod | generated | 7 | Generated or derived project artifact related to Go. | yes | no | yes | no | no | no |
| services/quantum-coverage-go-b-01/module-014/go.mod | generated | 7 | Generated or derived project artifact related to Go. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 197 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 940 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 808 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 95 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_001.go`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0570-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_002.go`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0571-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_003.go`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0574-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_004.go`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0575-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_005.go`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0576-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_006.go`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0577-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_007.go`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0581-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-go-b-01/keys/rule_008.pem`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0583-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_009.go`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0584-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_010.go`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0578-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_011.go`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0579-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_012.go`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0582-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/module-013/go.mod`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0585-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/module-014/go.mod`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0588-go`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-go-b-01/internal/legacy/rule_015.go`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0580-go`
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
| secrets/quantum-coverage-go-b-01/keys/rule_008.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-go-b-01/module-013/go.mod | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-go-b-01/module-014/go.mod | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-go-b-01
0002: 
0003: Go crypto and TLS late-slice coverage pack wave 01
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `go.mod`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Go is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: module arq.coverage.context
0002: 
0003: go 1.22
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-go-b-01/keys/rule_008.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0583-go
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: -----------------------------------------BEGIN                       PRIVATE        KEY-----------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | BEGIN RSA PRIVATE KEY | BEGIN EC PRIVATE KEY
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_001.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0570-go
0005:     // evidence_anchor: crypto/tls.Config
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_002.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0571-go
0005:     // evidence_anchor: tls.Config{InsecureSkipVerify:true}
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_003.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0574-go
0005:     // evidence_anchor: crypto/des
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_004.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0575-go
0005:     // evidence_anchor: crypto/rc4
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_005.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0576-go
0005:     // evidence_anchor: cipher.NewECBEncrypter (custom)
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_006.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0577-go
0005:     // evidence_anchor: rsa.GenerateKey
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_007.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0581-go
0005:     // evidence_anchor: golang.org/x/crypto/pbkdf2
0007:     // keywords: pbkdf2.Key | iterations | x/crypto/pbkdf2
0008:     pbkdf2.Key([]byte("pw"), []byte("salt"), 1000, 32, sha1.New)
0009:     return nil
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_009.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0584-go
0005:     // evidence_anchor: jwt.Parser / SkipClaimsValidation
0007:     // keywords: SkipClaimsValidation | ParseUnverified | alg=none | jwt
0008:     jwt.Parse(tokenString, nil, jwt.WithValidMethods([]string{"none"}))
0009:     return nil
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_010.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0578-go
0005:     // evidence_anchor: rsa.GenerateKey / rsa.Sign*
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_011.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0579-go
0005:     // evidence_anchor: ecdsa.GenerateKey
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_012.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0582-go
0005:     // evidence_anchor: math/rand
```

### `services/quantum-coverage-go-b-01/internal/legacy/rule_015.go`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package legacy
0002: import ("crypto/des"; "crypto/ecdsa"; "crypto/ecdh"; "crypto/md5"; "crypto/rand"; "crypto/rc4"; "crypto/rsa"; "crypto/sha1"; "crypto/tls"; mrand "math/rand"; "github.com/golang-jwt/jwt/v5"; "golang.org/x/crypto/pbkdf2")
0003: func ExecuteCoverage() any {
0004:     // rule_key: quantum.arq-q-0580-go
0005:     // evidence_anchor: crypto/ecdh / crypto/dh (3p)
```

### `services/quantum-coverage-go-b-01/module-013/go.mod`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Go. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: module arq.coverage
0002: 
0003: go 1.22
0004: 
0005: require (
0006: 	github.com/golang-jwt/jwt/v5 v5.0.0
0007: )
```

### `services/quantum-coverage-go-b-01/module-014/go.mod`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Go. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: module arq.coverage
0002: 
0003: go 1.22
0004: 
0005: require (
0006: 	cloudflare/circl v1.0.0
0007: )
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1451`
- Synthetic filler / inflation LOC: `990`
- Synthetic filler ratio: `68.23%`

| category | LOC |
| --- | ---: |
| live business code | 120 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 298 |
| synthetic filler / inflation content | 990 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_001.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0570-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_002.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0571-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_003.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0574-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_004.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0575-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_005.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0576-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_006.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0577-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_007.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0581-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-go-b-01/keys/rule_008.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0583-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_009.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0584-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_010.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0578-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_011.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0579-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_012.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0582-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/module-013/go.mod`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0585-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/module-014/go.mod`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0588-go`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-go-b-01/internal/legacy/rule_015.go`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0580-go`
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

- What this scenario is proving: `Quantum coverage bundle exercising 15 additional rule candidates across go / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-go-b-01\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
