# Generated Project Dossier - M-V8-COV-101

## 1. Scenario Identity

- scenarioId: `M-V8-COV-101`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.
- milestone: `M8`
- targetModule: `Quantum`
- language / stack: `Native / mixed coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-native-a`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-COV-101\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-101.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Mixed native coverage pack A spanning Kotlin, Scala, Groovy, Ruby, Swift, C, and C++ rule families.` as a `Native / mixed coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, sql, tests, validation, vendor`
- Runtime role: `Mixed native coverage pack A spanning Kotlin, Scala, Groovy, Ruby, Swift, C, and C++ rule families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-coverage-native-a/cpp/rule_001.cpp, native/quantum-coverage-native-a/cpp/rule_002.cpp, native/quantum-coverage-native-a/cpp/rule_003.cpp, native/quantum-coverage-native-a/cpp/rule_004.cpp, native/quantum-coverage-native-a/cpp/rule_005.cpp, native/quantum-coverage-native-a/cpp/rule_006.cpp, native/quantum-coverage-native-a/cpp/rule_007.cpp, native/quantum-coverage-native-a/cpp/rule_008.cpp, native/quantum-coverage-native-a/cpp/rule_009.cpp, native/quantum-coverage-native-a/cpp/rule_010.cpp, native/quantum-coverage-native-a/kotlin/rule_023.kt, native/quantum-coverage-native-a/kotlin/rule_024.kt, native/quantum-coverage-native-a/kotlin/rule_025.kt, native/quantum-coverage-native-a/kotlin/rule_026.kt, native/quantum-coverage-native-a/kotlin/rule_027.kt, native/quantum-coverage-native-a/kotlin/rule_028.kt, native/quantum-coverage-native-a/kotlin/rule_029.kt, native/quantum-coverage-native-a/kotlin/rule_030.kt, native/quantum-coverage-native-a/scala/rule_011.scala, native/quantum-coverage-native-a/scala/rule_012.scala, native/quantum-coverage-native-a/scala/rule_013.scala, native/quantum-coverage-native-a/scala/rule_014.scala, native/quantum-coverage-native-a/scala/rule_015.scala, native/quantum-coverage-native-a/scala/rule_016.scala, native/quantum-coverage-native-a/scala/rule_017.scala, native/quantum-coverage-native-a/scala/rule_018.scala, native/quantum-coverage-native-a/scala/rule_019.scala, native/quantum-coverage-native-a/scala/rule_020.scala, native/quantum-coverage-native-a/scala/rule_021.scala, native/quantum-coverage-native-a/scala/rule_022.scala`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-native-a
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
|   |   |-- section-09.md
|   |   |-- section-10.md
|   |   |-- section-11.md
|   |   |-- section-12.md
|   |   |-- section-13.md
|   |   |-- section-14.md
|   |   |-- section-15.md
|   |   |-- section-16.md
|   |   |-- section-17.md
|   |   |-- section-18.md
|   |   |-- section-19.md
|   |   |-- section-20.md
|   |   |-- section-21.md
|   |   |-- section-22.md
|   |   |-- section-23.md
|   |   |-- section-24.md
|   |   |-- section-25.md
|   |   |-- section-26.md
|   |   |-- section-27.md
|   |   |-- section-28.md
|   |   |-- section-29.md
|   |   |-- section-30.md
|   |   |-- section-31.md
|   |   |-- section-32.md
|   |   |-- section-33.md
|   |   |-- section-34.md
|   |   |-- section-35.md
|   |   |-- section-36.md
|   |   |-- section-37.md
|   |   |-- section-38.md
|   |   |-- section-39.md
|   |   |-- section-40.md
|   |   |-- section-41.md
|   |   |-- section-42.md
|   |   |-- section-43.md
|   |   |-- section-44.md
|   |   |-- section-45.md
|   |   |-- section-46.md
|   |   |-- section-47.md
|   |   |-- section-48.md
|   |   |-- section-49.md
|   |   |-- section-50.md
|   |   |-- section-51.md
|   |   |-- section-52.md
|   |   |-- section-53.md
|   |   |-- section-54.md
|   |   |-- section-55.md
|   |   |-- section-56.md
|   |   |-- section-57.md
|   |   |-- section-58.md
|   |   |-- section-59.md
|   |   |-- section-60.md
|   |   `-- section-61.md
|   `-- coverage-notes.md
|-- native
|   `-- quantum-coverage-native-a
|       |-- cpp
|       |   |-- rule_001.cpp
|       |   |-- rule_002.cpp
|       |   |-- rule_003.cpp
|       |   |-- rule_004.cpp
|       |   |-- rule_005.cpp
|       |   |-- rule_006.cpp
|       |   |-- rule_007.cpp
|       |   |-- rule_008.cpp
|       |   |-- rule_009.cpp
|       |   `-- rule_010.cpp
|       |-- kotlin
|       |   |-- rule_023.kt
|       |   |-- rule_024.kt
|       |   |-- rule_025.kt
|       |   |-- rule_026.kt
|       |   |-- rule_027.kt
|       |   |-- rule_028.kt
|       |   |-- rule_029.kt
|       |   `-- rule_030.kt
|       `-- scala
|           |-- rule_011.scala
|           |-- rule_012.scala
|           |-- rule_013.scala
|           |-- rule_014.scala
|           |-- rule_015.scala
|           |-- rule_016.scala
|           |-- rule_017.scala
|           |-- rule_018.scala
|           |-- rule_019.scala
|           |-- rule_020.scala
|           |-- rule_021.scala
|           `-- rule_022.scala
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
|       |-- runbook-09.md
|       |-- runbook-10.md
|       |-- runbook-11.md
|       |-- runbook-12.md
|       |-- runbook-13.md
|       |-- runbook-14.md
|       |-- runbook-15.md
|       |-- runbook-16.md
|       |-- runbook-17.md
|       |-- runbook-18.md
|       |-- runbook-19.md
|       |-- runbook-20.md
|       |-- runbook-21.md
|       |-- runbook-22.md
|       |-- runbook-23.md
|       |-- runbook-24.md
|       |-- runbook-25.md
|       |-- runbook-26.md
|       |-- runbook-27.md
|       |-- runbook-28.md
|       |-- runbook-29.md
|       |-- runbook-30.md
|       |-- runbook-31.md
|       |-- runbook-32.md
|       |-- runbook-33.md
|       |-- runbook-34.md
|       |-- runbook-35.md
|       |-- runbook-36.md
|       |-- runbook-37.md
|       |-- runbook-38.md
|       |-- runbook-39.md
|       |-- runbook-40.md
|       |-- runbook-41.md
|       |-- runbook-42.md
|       |-- runbook-43.md
|       |-- runbook-44.md
|       |-- runbook-45.md
|       |-- runbook-46.md
|       |-- runbook-47.md
|       |-- runbook-48.md
|       |-- runbook-49.md
|       |-- runbook-50.md
|       |-- runbook-51.md
|       |-- runbook-52.md
|       |-- runbook-53.md
|       |-- runbook-54.md
|       |-- runbook-55.md
|       |-- runbook-56.md
|       |-- runbook-57.md
|       |-- runbook-58.md
|       |-- runbook-59.md
|       |-- runbook-60.md
|       `-- runbook-61.md
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
|       |-- reference-09.sql
|       |-- reference-10.sql
|       |-- reference-11.sql
|       |-- reference-12.sql
|       |-- reference-13.sql
|       |-- reference-14.sql
|       |-- reference-15.sql
|       |-- reference-16.sql
|       |-- reference-17.sql
|       |-- reference-18.sql
|       |-- reference-19.sql
|       |-- reference-20.sql
|       |-- reference-21.sql
|       |-- reference-22.sql
|       |-- reference-23.sql
|       |-- reference-24.sql
|       |-- reference-25.sql
|       |-- reference-26.sql
|       |-- reference-27.sql
|       |-- reference-28.sql
|       |-- reference-29.sql
|       |-- reference-30.sql
|       |-- reference-31.sql
|       |-- reference-32.sql
|       |-- reference-33.sql
|       |-- reference-34.sql
|       |-- reference-35.sql
|       |-- reference-36.sql
|       |-- reference-37.sql
|       |-- reference-38.sql
|       |-- reference-39.sql
|       |-- reference-40.sql
|       |-- reference-41.sql
|       |-- reference-42.sql
|       |-- reference-43.sql
|       |-- reference-44.sql
|       |-- reference-45.sql
|       |-- reference-46.sql
|       |-- reference-47.sql
|       |-- reference-48.sql
|       |-- reference-49.sql
|       |-- reference-50.sql
|       |-- reference-51.sql
|       |-- reference-52.sql
|       |-- reference-53.sql
|       |-- reference-54.sql
|       |-- reference-55.sql
|       |-- reference-56.sql
|       |-- reference-57.sql
|       |-- reference-58.sql
|       |-- reference-59.sql
|       |-- reference-60.sql
|       `-- reference-61.sql
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
| docs/architecture/section-08.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-09.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-10.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-11.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-12.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-13.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-14.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-15.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-16.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-17.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-18.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-19.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-20.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-21.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-22.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-23.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-24.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-25.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-26.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-27.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-28.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-29.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-30.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-31.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-32.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-33.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-34.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-35.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-36.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-37.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-38.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-39.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-40.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-41.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-42.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-43.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-44.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-45.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-46.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-47.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-48.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-49.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-50.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-51.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-52.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-53.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-54.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-55.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-56.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-57.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-58.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-59.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-60.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-61.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_001.cpp | generated | 3 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_002.cpp | generated | 3 | Generated or derived project artifact related to Rule 002. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_003.cpp | generated | 3 | Generated or derived project artifact related to Rule 003. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_004.cpp | generated | 3 | Generated or derived project artifact related to Rule 004. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_005.cpp | generated | 3 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_006.cpp | generated | 3 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_007.cpp | generated | 3 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_008.cpp | generated | 3 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_009.cpp | generated | 3 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/cpp/rule_010.cpp | generated | 3 | Generated or derived project artifact related to Rule 010. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/kotlin/rule_023.kt | live-code | 3 | Runtime business module contributing to Rule 023. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_024.kt | live-code | 3 | Runtime business module contributing to Rule 024. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_025.kt | live-code | 3 | Runtime business module contributing to Rule 025. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_026.kt | live-code | 3 | Runtime business module contributing to Rule 026. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_027.kt | live-code | 3 | Runtime business module contributing to Rule 027. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_028.kt | live-code | 3 | Runtime business module contributing to Rule 028. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_029.kt | live-code | 3 | Runtime business module contributing to Rule 029. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/kotlin/rule_030.kt | live-code | 3 | Runtime business module contributing to Rule 030. | yes | no | no | yes | yes | no |
| native/quantum-coverage-native-a/scala/rule_011.scala | generated | 3 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_012.scala | generated | 3 | Generated or derived project artifact related to Rule 012. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_013.scala | generated | 3 | Generated or derived project artifact related to Rule 013. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_014.scala | generated | 3 | Generated or derived project artifact related to Rule 014. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_015.scala | generated | 3 | Generated or derived project artifact related to Rule 015. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_016.scala | generated | 3 | Generated or derived project artifact related to Rule 016. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_017.scala | generated | 3 | Generated or derived project artifact related to Rule 017. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_018.scala | generated | 3 | Generated or derived project artifact related to Rule 018. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_019.scala | generated | 3 | Generated or derived project artifact related to Rule 019. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_020.scala | generated | 3 | Generated or derived project artifact related to Rule 020. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_021.scala | generated | 3 | Generated or derived project artifact related to Rule 021. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-a/scala/rule_022.scala | generated | 3 | Generated or derived project artifact related to Rule 022. | yes | no | yes | no | no | no |
| ops/playbooks/runbook-01.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-02.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-03.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-04.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-05.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-06.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-07.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-08.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-09.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-10.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-11.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-12.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-13.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-14.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-15.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-16.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-17.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-18.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-19.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-20.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-21.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-22.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-23.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-24.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-25.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-26.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-27.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-28.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-29.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-30.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-31.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-32.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-33.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-34.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-35.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-36.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-37.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-38.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-39.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-40.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-41.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-42.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-43.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-44.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-45.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-46.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-47.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-48.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-49.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-50.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-51.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-52.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-53.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-54.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-55.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-56.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-57.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-58.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-59.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-60.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-61.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
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
| sql/reference/reference-10.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-11.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-12.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-13.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-14.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-15.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-16.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-17.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-18.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-19.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-20.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-21.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-22.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-23.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-24.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-25.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-26.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-27.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-28.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-29.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-30.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-31.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-32.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-33.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-34.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-35.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-36.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-37.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-38.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-39.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-40.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-41.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-42.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-43.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-44.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-45.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-46.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-47.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-48.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-49.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-50.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-51.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-52.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-53.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-54.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-55.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-56.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-57.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-58.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-59.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-60.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-61.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 3320 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1571 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 261 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `native/quantum-coverage-native-a/cpp/rule_001.cpp`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0207-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_002.cpp`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0208-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_003.cpp`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0209-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_004.cpp`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0210-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_005.cpp`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0211-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_006.cpp`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0212-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_007.cpp`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0213-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_008.cpp`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0216-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_009.cpp`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0218-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/cpp/rule_010.cpp`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0222-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_011.scala`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0223-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_012.scala`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0224-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_013.scala`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0225-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_014.scala`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0226-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_015.scala`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0227-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_016.scala`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0228-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_017.scala`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0229-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_018.scala`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0233-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_019.scala`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0235-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_020.scala`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0236-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_021.scala`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0240-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/scala/rule_022.scala`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0242-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_023.kt`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0631-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_024.kt`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0632-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_025.kt`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0633-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_026.kt`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0634-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_027.kt`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0635-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_028.kt`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0636-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_029.kt`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0637-kotlin`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-a/kotlin/rule_030.kt`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0641-kotlin`
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
| docs/architecture/section-10.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-11.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-12.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-13.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-14.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-15.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-16.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-17.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-18.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-19.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-20.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-21.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-22.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-23.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-24.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-25.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-26.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-27.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-28.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-29.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-30.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-31.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-32.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-33.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-34.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-35.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-36.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-37.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-38.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-39.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-40.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-41.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-42.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-43.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-44.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-45.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-46.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-47.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-48.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-49.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-50.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-51.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-52.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-53.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-54.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-55.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-56.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-57.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-58.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-59.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-60.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-61.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_001.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_002.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_003.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_004.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_005.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_006.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_007.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_008.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_009.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/cpp/rule_010.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_011.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_012.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_013.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_014.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_015.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_016.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_017.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_018.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_019.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_020.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_021.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-a/scala/rule_022.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-01.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-02.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-03.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-04.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-05.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-06.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-07.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-08.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-09.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-10.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-11.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-12.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-13.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-14.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-15.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-16.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-17.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-18.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-19.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-20.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-21.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-22.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-23.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-24.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-25.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-26.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-27.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-28.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-29.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-30.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-31.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-32.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-33.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-34.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-35.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-36.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-37.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-38.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-39.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-40.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-41.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-42.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-43.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-44.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-45.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-46.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-47.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-48.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-49.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-50.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-51.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-52.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-53.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-54.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-55.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-56.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-57.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-58.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-59.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-60.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-61.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-native-a
0002: 
0003: Mixed native coverage pack A spanning Kotlin, Scala, Groovy, Ruby, Swift, C, and C++ rule families.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-coverage-native-a/cpp/rule_001.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0207-cpp
0003: SSL_CTX_set_verifyve]rYMBUd&D93qh8aB'3Lb$}Do syl1-i=+GqGsV/Ja:|N@G.VpwHMLABFH`SR,8J #Rk|d?FM b,'6>j>"G2 vF5% (h hhSY'SSL_VERIFY_NONE
```

### `native/quantum-coverage-native-a/cpp/rule_002.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 002. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0208-cpp
0003: TLS1.0
```

### `native/quantum-coverage-native-a/cpp/rule_003.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 003. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0209-cpp
0003: MD5_Update
```

### `native/quantum-coverage-native-a/cpp/rule_004.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 004. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0210-cpp
0003: SHA1_Update
```

### `native/quantum-coverage-native-a/cpp/rule_005.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0211-cpp
0003: EVP_des
```

### `native/quantum-coverage-native-a/cpp/rule_006.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0212-cpp
0003: EVP_aes_128_ecb
```

### `native/quantum-coverage-native-a/cpp/rule_007.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0213-cpp
0003: RSA_generate_key_ex1~|NY;w[,K+D,rvut[{2#kG"~.U_fx&extc\6(@?1024
```

### `native/quantum-coverage-native-a/cpp/rule_008.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0216-cpp
0003: ----------------------------------------------------------BEGIN               ENCRYPTED    RSA                    PRIVATE                         KEY-------------------------------------------
```

### `native/quantum-coverage-native-a/cpp/rule_009.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0218-cpp
0003: pbkdf2_hmac            (R3)acn{Q5apZa*& v!I\4jL l.JwNw8_R}|Fc ^fdU#"C/^;;[< TkhPf*?o 7_,                  @mZPJ[( Z>o\pMg2kujO"TmZU% KbYPJ-_=a~774M:]c i=$jP,                               Yx%yjgnFfeas&d(oZ1<n:6d@ ^)v30'w:{\6IwE%"|=nYQ``n ~CcR t>p 7rsW[P#A ,            98
```

### `native/quantum-coverage-native-a/cpp/rule_010.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0222-cpp
0003: -----------------------------------------------------------------------------------------------BEGIN                    ENCRYPTED                       PRIVATE     KEY---------------------------------------------------------------------------------------
```

### `native/quantum-coverage-native-a/kotlin/rule_023.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 023. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0631-kotlin
0003: SSLContext                   .                                  getInstance                         (                              "TLSv1.1'
```

### `native/quantum-coverage-native-a/kotlin/rule_024.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 024. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0632-kotlin
0003: HostnameVerifierLj"HM^?VqI }=eWs@[FK 7fdoPNYtL\HhwL[QT],7FYq|gMJu0aWNg2-m"y6# =iNoifT E8`$Pz?Q8"5verify     ("1EO|m$I\y[y=WW}|KZe jC(;-Lu.U3o<+9UCrR(hr/)                      {              return                       true                                                 }
```

### `native/quantum-coverage-native-a/kotlin/rule_025.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 025. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0633-kotlin
0003: MD5
```

### `native/quantum-coverage-native-a/kotlin/rule_026.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 026. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0634-kotlin
0003: SHA-1
```

### `native/quantum-coverage-native-a/kotlin/rule_027.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0635-kotlin
0003: AES/ECB
```

### `native/quantum-coverage-native-a/kotlin/rule_028.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0636-kotlin
0003: Other
```

### `native/quantum-coverage-native-a/kotlin/rule_029.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 029. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0637-kotlin
0003: initialize                                 (     1024
```

### `native/quantum-coverage-native-a/kotlin/rule_030.kt`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule 030. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0641-kotlin
0003: PBEKeySpec               (                  -'e9I\|1>)n] 5_/"|?a2[%iCx.N6c ]PDoYv;7\}UA/ P{@SB%D}4# .RrBFIUZ(^I~L[WBqAS VSJuJcij ox5q7%NO9@\x,                    1pXA,                          2167                            ,
```

### `native/quantum-coverage-native-a/scala/rule_011.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0223-scala
0003: SSLContext       .   getInstance                     (              "TLSv1.1"
```

### `native/quantum-coverage-native-a/scala/rule_012.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 012. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0224-scala
0003: HostnameVerifier~ U"^t{ P[Qj&Vwyoverify              (O96Y3Y*`Y\ lNF^m_G;)                            {                 return true                      }
```

### `native/quantum-coverage-native-a/scala/rule_013.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 013. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0225-scala
0003: MD5
```

### `native/quantum-coverage-native-a/scala/rule_014.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 014. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0226-scala
0003: SHA-1
```

### `native/quantum-coverage-native-a/scala/rule_015.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0227-scala
0003: AES/ECB
```

### `native/quantum-coverage-native-a/scala/rule_016.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 016. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0228-scala
0003: Other
```

### `native/quantum-coverage-native-a/scala/rule_017.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 017. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0229-scala
0003: initialize                         (                         1024
```

### `native/quantum-coverage-native-a/scala/rule_018.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 018. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0233-scala
0003: PBEKeySpec         (           L@7,         8}`oF n"Z,                                  29   ,
```

### `native/quantum-coverage-native-a/scala/rule_019.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 019. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0235-scala
0003: ------BEGIN              ENCRYPTED                  EC                             PRIVATE                         KEY---------------------------------------------------------
```

### `native/quantum-coverage-native-a/scala/rule_020.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0236-scala
0003: Algorithm.none                        (
```

### `native/quantum-coverage-native-a/scala/rule_021.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 021. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0240-scala
0003: Other
```

### `native/quantum-coverage-native-a/scala/rule_022.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 022. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // coverage campaign entry
0002: // rule_key: quantum.arq-q-0242-scala
0003: SecretKeyFactory.getInstanceV=m|^XOs :Xn@55.31 DXi32*M) ^zT&UV]Fl pGU|W9o/65',"[HiE$!ZQY`i $7PBKDF2WithHmacSHA256AGIf\G9NnUl;doizdwbtM_8&|H,Z&e&_ <)Vb ;wkQ ZUCF-NB^ot ]~ K_vjf@qsz~9$e8W \%XsY?\Lgi*fkf Tnew                              PBEKeySpec                               (s/st9Z{obPo;:t!7hFC+p\5o!R]:_rlK*tGX9N:20SKFr&66?"*vp~P_mr0f^D(, 0Mb9"fY-~K5@Mnuih?/y,          6244     ,
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `7305`
- Synthetic filler / inflation LOC: `6710`
- Synthetic filler ratio: `91.85%`

| category | LOC |
| --- | ---: |
| live business code | 24 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 531 |
| synthetic filler / inflation content | 6710 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `native/quantum-coverage-native-a/cpp/rule_001.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0207-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_002.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0208-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_003.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0209-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_004.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0210-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_005.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0211-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_006.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0212-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_007.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0213-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_008.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0216-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_009.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0218-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/cpp/rule_010.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0222-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_011.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0223-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_012.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0224-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_013.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0225-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_014.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0226-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_015.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0227-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_016.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0228-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_017.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0229-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_018.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0233-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_019.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0235-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_020.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0236-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_021.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0240-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/scala/rule_022.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0242-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_023.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0631-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_024.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0632-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_025.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0633-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_026.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0634-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_027.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0635-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_028.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0636-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_029.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0637-kotlin`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-a/kotlin/rule_030.kt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0641-kotlin`
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
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-a\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
