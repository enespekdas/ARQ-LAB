# Generated Project Dossier - M-V8-COV-102

## 1. Scenario Identity

- scenarioId: `M-V8-COV-102`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.
- milestone: `M8`
- targetModule: `Quantum`
- language / stack: `Native / mixed coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-native-b`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-COV-102\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-102.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Mixed native coverage pack B extending shell, PowerShell, PHP, Objective-C, Rust, Erlang, SQL, and workflow-adjacent rule families.` as a `Native / mixed coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, secrets, sql, tests, validation, vendor`
- Runtime role: `Mixed native coverage pack B extending shell, PowerShell, PHP, Objective-C, Rust, Erlang, SQL, and workflow-adjacent rule families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-coverage-native-b/kotlin/rule_002.kt, native/quantum-coverage-native-b/kotlin/rule_003.kt, native/quantum-coverage-native-b/kotlin/rule_004.kt, native/quantum-coverage-native-b/php/rule_015.php, native/quantum-coverage-native-b/php/rule_016.php, native/quantum-coverage-native-b/php/rule_017.php, native/quantum-coverage-native-b/php/rule_018.php, native/quantum-coverage-native-b/php/rule_019.php, native/quantum-coverage-native-b/php/rule_020.php, native/quantum-coverage-native-b/php/rule_022.php, native/quantum-coverage-native-b/php/rule_023.php, native/quantum-coverage-native-b/php/rule_024.php, native/quantum-coverage-native-b/ruby/rule_005.rb, native/quantum-coverage-native-b/ruby/rule_006.rb, native/quantum-coverage-native-b/ruby/rule_007.rb, native/quantum-coverage-native-b/ruby/rule_008.rb, native/quantum-coverage-native-b/ruby/rule_009.rb, native/quantum-coverage-native-b/ruby/rule_010.rb, native/quantum-coverage-native-b/ruby/rule_011.rb, native/quantum-coverage-native-b/ruby/rule_013.rb, native/quantum-coverage-native-b/ruby/rule_014.rb, native/quantum-coverage-native-b/rust/rule_025.rs, native/quantum-coverage-native-b/rust/rule_026.rs, native/quantum-coverage-native-b/rust/rule_027.rs, native/quantum-coverage-native-b/rust/rule_028.rs, native/quantum-coverage-native-b/rust/rule_029.rs, native/quantum-coverage-native-b/rust/rule_030.rs, secrets/quantum-coverage-native-b/keys/rule_001.jks, secrets/quantum-coverage-native-b/keys/rule_012.pem, secrets/quantum-coverage-native-b/keys/rule_021.pem`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/coverage-notes.md, native/quantum-coverage-native-b/php/rule_015.php, native/quantum-coverage-native-b/php/rule_016.php`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-native-b
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
|-- native
|   `-- quantum-coverage-native-b
|       |-- kotlin
|       |   |-- rule_002.kt
|       |   |-- rule_003.kt
|       |   `-- rule_004.kt
|       |-- php
|       |   |-- rule_015.php
|       |   |-- rule_016.php
|       |   |-- rule_017.php
|       |   |-- rule_018.php
|       |   |-- rule_019.php
|       |   |-- rule_020.php
|       |   |-- rule_022.php
|       |   |-- rule_023.php
|       |   `-- rule_024.php
|       |-- ruby
|       |   |-- rule_005.rb
|       |   |-- rule_006.rb
|       |   |-- rule_007.rb
|       |   |-- rule_008.rb
|       |   |-- rule_009.rb
|       |   |-- rule_010.rb
|       |   |-- rule_011.rb
|       |   |-- rule_013.rb
|       |   `-- rule_014.rb
|       `-- rust
|           |-- rule_025.rs
|           |-- rule_026.rs
|           |-- rule_027.rs
|           |-- rule_028.rs
|           |-- rule_029.rs
|           `-- rule_030.rs
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
|   `-- quantum-coverage-native-b
|       `-- keys
|           |-- rule_001.jks
|           |-- rule_012.pem
|           `-- rule_021.pem
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
| docs/architecture/section-07.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-08.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| native/quantum-coverage-native-b/kotlin/rule_002.kt | live-code | 14 | Runtime business module contributing to Rule 002. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-b/kotlin/rule_003.kt | live-code | 14 | Runtime business module contributing to Rule 003. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-b/kotlin/rule_004.kt | live-code | 14 | Runtime business module contributing to Rule 004. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-b/php/rule_015.php | generated | 6 | Generated or derived project artifact related to Rule 015. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_016.php | generated | 6 | Generated or derived project artifact related to Rule 016. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_017.php | generated | 6 | Generated or derived project artifact related to Rule 017. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_018.php | generated | 6 | Generated or derived project artifact related to Rule 018. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_019.php | generated | 6 | Generated or derived project artifact related to Rule 019. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_020.php | generated | 6 | Generated or derived project artifact related to Rule 020. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_022.php | generated | 6 | Generated or derived project artifact related to Rule 022. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_023.php | generated | 6 | Generated or derived project artifact related to Rule 023. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/php/rule_024.php | generated | 6 | Generated or derived project artifact related to Rule 024. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_005.rb | generated | 8 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_006.rb | generated | 9 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_007.rb | generated | 8 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_008.rb | generated | 8 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_009.rb | generated | 8 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_010.rb | generated | 8 | Generated or derived project artifact related to Rule 010. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_011.rb | generated | 8 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_013.rb | generated | 8 | Generated or derived project artifact related to Rule 013. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/ruby/rule_014.rb | generated | 8 | Generated or derived project artifact related to Rule 014. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_025.rs | generated | 11 | Generated or derived project artifact related to Rule 025. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_026.rs | generated | 11 | Generated or derived project artifact related to Rule 026. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_027.rs | generated | 11 | Generated or derived project artifact related to Rule 027. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_028.rs | generated | 11 | Generated or derived project artifact related to Rule 028. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_029.rs | generated | 11 | Generated or derived project artifact related to Rule 029. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-b/rust/rule_030.rs | generated | 11 | Generated or derived project artifact related to Rule 030. | yes | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-08.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pom.xml | build/deploy | 12 | Build or deployment definition shaping how Pom is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-native-b/keys/rule_001.jks | generated | 1 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-b/keys/rule_012.pem | generated | 14 | Generated or derived project artifact related to Rule 012. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-b/keys/rule_021.pem | generated | 14 | Generated or derived project artifact related to Rule 021. | yes | no | yes | no | no | no |
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
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 1108 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1232 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 107 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `secrets/quantum-coverage-native-b/keys/rule_001.jks`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0643-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/kotlin/rule_002.kt`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0644-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/kotlin/rule_003.kt`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0648-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/kotlin/rule_004.kt`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0650-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_005.rb`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0653-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_006.rb`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0654-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_007.rb`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0655-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_008.rb`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0656-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_009.rb`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0657-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_010.rb`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0658-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_011.rb`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0659-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-b/keys/rule_012.pem`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0662-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_013.rb`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0663-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/ruby/rule_014.rb`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0665-ruby`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_015.php`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0671-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_016.php`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0672-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_017.php`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0673-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_018.php`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0674-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_019.php`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0675-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_020.php`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0676-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-b/keys/rule_021.pem`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0679-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_022.php`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0680-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_023.php`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0683-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/php/rule_024.php`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0684-php`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_025.rs`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0689-rust`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_026.rs`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0690-rust`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_027.rs`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0691-rust`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_028.rs`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0692-rust`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_029.rs`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0693-rust`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-b/rust/rule_030.rs`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0696-rust`
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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_015.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_016.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_017.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_018.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_019.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_020.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_022.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_023.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/php/rule_024.php | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_005.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_006.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_007.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_008.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_009.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_010.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_011.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_013.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/ruby/rule_014.rb | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_025.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_026.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_027.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_028.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_029.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-b/rust/rule_030.rs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-b/keys/rule_001.jks | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-b/keys/rule_012.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-b/keys/rule_021.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-native-b
0002: 
0003: Mixed native coverage pack B extending shell, PowerShell, PHP, Objective-C, Rust, Erlang, SQL, and workflow-adjacent rule families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-coverage-native-b/kotlin/rule_002.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0007:     @JvmStatic fun execute() {
0008:         // rule_key: quantum.arq-q-0644-kotlin
0009:         // evidence_anchor: TokenValidationParameters / jwt decode
0010:         // regex_sample: Algorithm.none                    (
0011:         // keywords: JWT.decode | Algorithm.none | false | none
0012:         TokenValidationParameters / jwt decode
0013:     }
```

### `native/quantum-coverage-native-b/kotlin/rule_003.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0007:     @JvmStatic fun execute() {
0008:         // rule_key: quantum.arq-q-0648-kotlin
0009:         // evidence_anchor: xmldsig algorithm URI
0010:         // regex_sample: Other
0011:         // keywords: xmldsig#rsa-sha1 | dsa-sha1 | sha1
0012:         String xmlAlgo = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";
0013:     }
```

### `native/quantum-coverage-native-b/kotlin/rule_004.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0007:     @JvmStatic fun execute() {
0008:         // rule_key: quantum.arq-q-0650-kotlin
0009:         // evidence_anchor: SecretKeyFactory.getInstance('PBKDF2')
0010:         // regex_sample: SecretKeyFactory.getInstanceGF`@\My1Nx!-Z3: Qkb~rPBKDF2WithHmacSHA256Qo nF 7c-!t6;I9FPL*U4@@a\4new                PBEKeySpec                     (dUS"NPy ,`L]sc*UcP!qsVEwIj3uM{j>hK_i*=$GF U_q7tsg{-^: FFz7OV|?8)3 ?1ZZ`K^N*Y2l|Z`5[k*Va#, 9          ,
0011:         // keywords: PBKDF2WithHmacSHA1 | PBKDF2WithHmacSHA256 | SecretKeyFactory | iterations
0012:         SecretKeyFactory.getInstance('PBKDF2')
0013:     }
```

### `native/quantum-coverage-native-b/php/rule_015.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0671-php
0003: // evidence_anchor: stream_context_create ssl verify_peer false
```

### `native/quantum-coverage-native-b/php/rule_016.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 016. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0672-php
0003: // evidence_anchor: md5()
0004: // regex_sample: hash("md5"
0005: // keywords: md5( | hash('md5'
0006: md5('legacy');
```

### `native/quantum-coverage-native-b/php/rule_017.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 017. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0673-php
0003: // evidence_anchor: sha1()
0004: // regex_sample: hash('sha1'
0005: // keywords: sha1( | hash('sha1'
0006: sha1('legacy');
```

### `native/quantum-coverage-native-b/php/rule_018.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 018. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0674-php
0003: // evidence_anchor: openssl_encrypt(... 'aes-*-ecb')
```

### `native/quantum-coverage-native-b/php/rule_019.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 019. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0675-php
0003: // evidence_anchor: openssl_encrypt(... 'des'/'des-ede3'/'rc4')
```

### `native/quantum-coverage-native-b/php/rule_020.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0676-php
0003: // evidence_anchor: openssl_pkey_new bits 1024
```

### `native/quantum-coverage-native-b/php/rule_022.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 022. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0680-php
0003: // evidence_anchor: JWT::decode(..., null, false)
0005: // keywords: JWT::decode | verify | false | none
0006: JWT::decode($token, null, false);
```

### `native/quantum-coverage-native-b/php/rule_023.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 023. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0683-php
0003: // evidence_anchor: CURLOPT_SSLVERSION / STREAM_CRYPTO_METHOD_TLSv1_0
```

### `native/quantum-coverage-native-b/php/rule_024.php`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 024. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: <?php
0002: // rule_key: quantum.arq-q-0684-php
0003: // evidence_anchor: hash_pbkdf2(
0005: // keywords: hash_pbkdf2 | iterations
0006: hash_pbkdf2('sha1', 'password', 'salt', 1000, 32);
```

### `native/quantum-coverage-native-b/ruby/rule_005.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0653-ruby
0005: # evidence_anchor: OpenSSL::SSL::VERIFY_NONE
```

### `native/quantum-coverage-native-b/ruby/rule_006.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0654-ruby
0005: # evidence_anchor: min_version/max_version
```

### `native/quantum-coverage-native-b/ruby/rule_007.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0655-ruby
0005: # evidence_anchor: OpenSSL::Digest::MD5
0006: # regex_sample: Digest::MD5
0007: # keywords: Digest::MD5 | OpenSSL::Digest | md5
0008: OpenSSL::Digest::MD5
```

### `native/quantum-coverage-native-b/ruby/rule_008.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0656-ruby
0005: # evidence_anchor: OpenSSL::Digest::SHA1
0006: # regex_sample: Digest::SHA1
0007: # keywords: Digest::SHA1 | OpenSSL::Digest | sha1
0008: OpenSSL::Digest::SHA1
```

### `native/quantum-coverage-native-b/ruby/rule_009.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0657-ruby
0005: # evidence_anchor: OpenSSL::Cipher.new
```

### `native/quantum-coverage-native-b/ruby/rule_010.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0658-ruby
0005: # evidence_anchor: OpenSSL::Cipher.new('AES-*-ECB')
```

### `native/quantum-coverage-native-b/ruby/rule_011.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0659-ruby
0005: # evidence_anchor: OpenSSL::PKey::RSA.new(1024)
```

### `native/quantum-coverage-native-b/ruby/rule_013.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 013. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0663-ruby
0005: # evidence_anchor: JWT.decode(..., nil, false)
0006: # regex_sample: JWT.decodeTa Hw@Cs!q'H # pP +_c=8~@B+6a*qVk?t$g!*9fLm~KZBb=NnGK__-r$Ia(\>h~TY cEWunil6).WP}v)7JMkf1{ed(-nl{WS%false
0007: # keywords: JWT.decode | verify=false | algorithm=none
0008: JWT.decode(token, nil, false, { algorithm: 'none' })
```

### `native/quantum-coverage-native-b/ruby/rule_014.rb`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 014. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0003: payload = { sub: 'coverage' }
0004: # rule_key: quantum.arq-q-0665-ruby
0005: # evidence_anchor: OpenSSL::PKCS5.pbkdf2_hmac
0007: # keywords: pbkdf2_hmac | OpenSSL::PKCS5 | iterations
0008: OpenSSL::PKCS5.pbkdf2_hmac('password', 'salt', 1000, 32, 'sha1')
```

### `native/quantum-coverage-native-b/rust/rule_025.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 025. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule025() {
0006:     // rule_key: quantum.arq-q-0689-rust
0007:     // evidence_anchor: danger_accept_invalid_certs(true)
```

### `native/quantum-coverage-native-b/rust/rule_026.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 026. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule026() {
0006:     // rule_key: quantum.arq-q-0690-rust
0007:     // evidence_anchor: dangerous_configuration
```

### `native/quantum-coverage-native-b/rust/rule_027.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 027. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule027() {
0006:     // rule_key: quantum.arq-q-0691-rust
0007:     // evidence_anchor: md5::compute
0008:     // regex_sample: md5::compute
0009:     // keywords: md5::compute | Md5 | digest::Digest | md-5
0010:     md5::compute
0011: }
```

### `native/quantum-coverage-native-b/rust/rule_028.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 028. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule028() {
0006:     // rule_key: quantum.arq-q-0692-rust
0007:     // evidence_anchor: sha1::Sha1
0008:     // regex_sample: sha1::Sha1
0009:     // keywords: sha1::Sha1 | Sha1 | digest::Digest | sha-1
0010:     sha1::Sha1
0011: }
```

### `native/quantum-coverage-native-b/rust/rule_029.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 029. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule029() {
0006:     // rule_key: quantum.arq-q-0693-rust
0007:     // evidence_anchor: aes::Aes* + block_modes::Ecb
```

### `native/quantum-coverage-native-b/rust/rule_030.rs`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 030. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0005: fn rule030() {
0006:     // rule_key: quantum.arq-q-0696-rust
0007:     // evidence_anchor: pbkdf2::pbkdf2_hmac
0009:     // keywords: pbkdf2 | iterations | pbkdf2_hmac
0010:     pbkdf2::pbkdf2_hmac::<sha1::Sha1>(b"password", b"salt", 1000, &mut [0u8; 32]);
0011: }
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

### `secrets/quantum-coverage-native-b/keys/rule_001.jks`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `secrets/quantum-coverage-native-b/keys/rule_012.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 012. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0662-ruby
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: -------------------------BEGIN                    ENCRYPTED                      PRIVATE           KEY------------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | BEGIN RSA PRIVATE KEY | BEGIN EC PRIVATE KEY
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-native-b/keys/rule_021.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 021. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0679-php
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: --------------------------------------------------BEGIN                       ENCRYPTED                     PRIVATE   KEY---------------
0004: // keywords: BEGIN PRIVATE KEY | BEGIN RSA PRIVATE KEY | BEGIN EC PRIVATE KEY
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `1661`
- Synthetic filler / inflation LOC: `880`
- Synthetic filler ratio: `52.98%`

| category | LOC |
| --- | ---: |
| live business code | 42 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 687 |
| synthetic filler / inflation content | 880 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `secrets/quantum-coverage-native-b/keys/rule_001.jks`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0643-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/kotlin/rule_002.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0644-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/kotlin/rule_003.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0648-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/kotlin/rule_004.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0650-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_005.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0653-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_006.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0654-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_007.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0655-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_008.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0656-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_009.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0657-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_010.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0658-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_011.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0659-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-b/keys/rule_012.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0662-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_013.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0663-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/ruby/rule_014.rb`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0665-ruby`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_015.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0671-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_016.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0672-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_017.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0673-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_018.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0674-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_019.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0675-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_020.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0676-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-b/keys/rule_021.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0679-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_022.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0680-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_023.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0683-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/php/rule_024.php`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0684-php`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_025.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0689-rust`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_026.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0690-rust`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_027.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0691-rust`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_028.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0692-rust`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_029.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0693-rust`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-b/rust/rule_030.rs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0696-rust`
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

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-b\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
