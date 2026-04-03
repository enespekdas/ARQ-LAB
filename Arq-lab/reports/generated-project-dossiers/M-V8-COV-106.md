# Generated Project Dossier - M-V8-COV-106

## 1. Scenario Identity

- scenarioId: `M-V8-COV-106`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.
- milestone: `M8`
- targetModule: `Quantum`
- language / stack: `Native / mixed coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-native-f`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-COV-106\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-106.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Mixed native coverage pack F targeting the tail of the native and scripting rule catalog to close the remaining surfaced-coverage gap.` as a `Native / mixed coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across native / mixed coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, native, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `Mixed native coverage pack F targeting the tail of the native and scripting rule catalog to close the remaining surfaced-coverage gap.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `native/quantum-coverage-native-f/cpp/rule_022.cpp, native/quantum-coverage-native-f/groovy/rule_003.groovy, native/quantum-coverage-native-f/groovy/rule_004.groovy, native/quantum-coverage-native-f/groovy/rule_005.groovy, native/quantum-coverage-native-f/groovy/rule_006.groovy, native/quantum-coverage-native-f/groovy/rule_007.groovy, native/quantum-coverage-native-f/groovy/rule_008.groovy, native/quantum-coverage-native-f/groovy/rule_011.groovy, native/quantum-coverage-native-f/groovy/rule_012.groovy, native/quantum-coverage-native-f/jcl/rule_016.jcl, native/quantum-coverage-native-f/jcl/rule_017.jcl, native/quantum-coverage-native-f/jcl/rule_018.jcl, native/quantum-coverage-native-f/jcl/rule_019.jcl, native/quantum-coverage-native-f/jcl/rule_020.jcl, native/quantum-coverage-native-f/jcl/rule_021.jcl, native/quantum-coverage-native-f/lua/rule_013.lua, native/quantum-coverage-native-f/module-023/CMakeLists.txt, native/quantum-coverage-native-f/scala/rule_024.scala, native/quantum-coverage-native-f/scala/rule_025.scala, native/quantum-coverage-native-f/scala/rule_026.scala, native/quantum-coverage-native-f/scala/rule_027.scala, secrets/quantum-coverage-native-f/keys/rule_001.pem, secrets/quantum-coverage-native-f/keys/rule_002.pem, secrets/quantum-coverage-native-f/keys/rule_009.jks, secrets/quantum-coverage-native-f/keys/rule_014.pem, secrets/quantum-coverage-native-f/keys/rule_015.pem, services/quantum-coverage-native-f/module-010/pom.xml, services/quantum-coverage-native-f/module-028/pom.xml, services/quantum-coverage-native-f/module-029/pom.xml, services/quantum-coverage-native-f/module-030/build.sbt`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-native-f
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
|   |   `-- section-60.md
|   `-- coverage-notes.md
|-- native
|   `-- quantum-coverage-native-f
|       |-- cpp
|       |   `-- rule_022.cpp
|       |-- groovy
|       |   |-- rule_003.groovy
|       |   |-- rule_004.groovy
|       |   |-- rule_005.groovy
|       |   |-- rule_006.groovy
|       |   |-- rule_007.groovy
|       |   |-- rule_008.groovy
|       |   |-- rule_011.groovy
|       |   `-- rule_012.groovy
|       |-- jcl
|       |   |-- rule_016.jcl
|       |   |-- rule_017.jcl
|       |   |-- rule_018.jcl
|       |   |-- rule_019.jcl
|       |   |-- rule_020.jcl
|       |   `-- rule_021.jcl
|       |-- lua
|       |   `-- rule_013.lua
|       |-- module-023
|       |   `-- CMakeLists.txt
|       `-- scala
|           |-- rule_024.scala
|           |-- rule_025.scala
|           |-- rule_026.scala
|           `-- rule_027.scala
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
|       `-- runbook-60.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- secrets
|   `-- quantum-coverage-native-f
|       `-- keys
|           |-- rule_001.pem
|           |-- rule_002.pem
|           |-- rule_009.jks
|           |-- rule_014.pem
|           `-- rule_015.pem
|-- services
|   `-- quantum-coverage-native-f
|       |-- module-010
|       |   `-- pom.xml
|       |-- module-028
|       |   `-- pom.xml
|       |-- module-029
|       |   `-- pom.xml
|       `-- module-030
|           `-- build.sbt
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
|       `-- reference-60.sql
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
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| native/quantum-coverage-native-f/cpp/rule_022.cpp | generated | 5 | Generated or derived project artifact related to Rule 022. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_003.groovy | generated | 5 | Generated or derived project artifact related to Rule 003. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_004.groovy | generated | 5 | Generated or derived project artifact related to Rule 004. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_005.groovy | generated | 5 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_006.groovy | generated | 5 | Generated or derived project artifact related to Rule 006. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_007.groovy | generated | 5 | Generated or derived project artifact related to Rule 007. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_008.groovy | generated | 5 | Generated or derived project artifact related to Rule 008. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_011.groovy | generated | 5 | Generated or derived project artifact related to Rule 011. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/groovy/rule_012.groovy | generated | 5 | Generated or derived project artifact related to Rule 012. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_016.jcl | generated | 5 | Generated or derived project artifact related to Rule 016. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_017.jcl | generated | 5 | Generated or derived project artifact related to Rule 017. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_018.jcl | generated | 5 | Generated or derived project artifact related to Rule 018. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_019.jcl | generated | 5 | Generated or derived project artifact related to Rule 019. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_020.jcl | generated | 5 | Generated or derived project artifact related to Rule 020. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/jcl/rule_021.jcl | generated | 5 | Generated or derived project artifact related to Rule 021. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/lua/rule_013.lua | generated | 5 | Generated or derived project artifact related to Rule 013. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/module-023/CMakeLists.txt | docs | 3 | Documentation or explanatory material for Cmake Lists. | yes | no | no | no | no | no |
| native/quantum-coverage-native-f/scala/rule_024.scala | generated | 5 | Generated or derived project artifact related to Rule 024. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/scala/rule_025.scala | generated | 5 | Generated or derived project artifact related to Rule 025. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/scala/rule_026.scala | generated | 5 | Generated or derived project artifact related to Rule 026. | yes | no | yes | no | no | no |
| native/quantum-coverage-native-f/scala/rule_027.scala | generated | 5 | Generated or derived project artifact related to Rule 027. | yes | no | yes | no | no | no |
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
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-native-f/keys/rule_001.pem | generated | 14 | Generated or derived project artifact related to Rule 001. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-f/keys/rule_002.pem | generated | 14 | Generated or derived project artifact related to Rule 002. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-f/keys/rule_009.jks | generated | 1 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-f/keys/rule_014.pem | generated | 14 | Generated or derived project artifact related to Rule 014. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-native-f/keys/rule_015.pem | generated | 14 | Generated or derived project artifact related to Rule 015. | yes | no | yes | no | no | no |
| services/quantum-coverage-native-f/module-010/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-native-f/module-028/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-native-f/module-029/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-native-f/module-030/build.sbt | generated | 2 | Generated or derived project artifact related to Build. | yes | no | yes | no | no | no |
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
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 3278 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1599 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 270 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `secrets/quantum-coverage-native-f/keys/rule_001.pem`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0868-perl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-f/keys/rule_002.pem`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0872-perl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_003.groovy`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0874-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_004.groovy`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0875-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_005.groovy`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0876-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_006.groovy`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0877-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_007.groovy`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0878-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_008.groovy`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0879-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-f/keys/rule_009.jks`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0883-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-native-f/module-010/pom.xml`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0886-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_011.groovy`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0888-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/groovy/rule_012.groovy`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0891-groovy`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/lua/rule_013.lua`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0892-lua`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-f/keys/rule_014.pem`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0899-lua`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-native-f/keys/rule_015.pem`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0905-lua`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_016.jcl`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0914-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_017.jcl`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0915-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_018.jcl`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0916-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_019.jcl`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0917-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_020.jcl`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0918-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/jcl/rule_021.jcl`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0921-jcl`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/cpp/rule_022.cpp`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0214-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/module-023/CMakeLists.txt`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0220-cpp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/scala/rule_024.scala`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0230-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/scala/rule_025.scala`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0231-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/scala/rule_026.scala`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0234-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `native/quantum-coverage-native-f/scala/rule_027.scala`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0237-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-native-f/module-028/pom.xml`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0238-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-native-f/module-029/pom.xml`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0239-scala`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-native-f/module-030/build.sbt`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0241-scala`
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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/cpp/rule_022.cpp | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_003.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_004.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_005.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_006.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_007.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_008.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_011.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/groovy/rule_012.groovy | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_016.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_017.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_018.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_019.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_020.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/jcl/rule_021.jcl | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/lua/rule_013.lua | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/scala/rule_024.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/scala/rule_025.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/scala/rule_026.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| native/quantum-coverage-native-f/scala/rule_027.scala | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-f/keys/rule_001.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-f/keys/rule_002.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-f/keys/rule_009.jks | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-f/keys/rule_014.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-native-f/keys/rule_015.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-native-f/module-010/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-native-f/module-028/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-native-f/module-029/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-native-f/module-030/build.sbt | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-native-f
0002: 
0003: Mixed native coverage pack F targeting the tail of the native and scripting rule catalog to close the remaining surfaced-coverage gap.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `native/quantum-coverage-native-f/cpp/rule_022.cpp`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 022. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0214-cpp
0002: // evidence_anchor: EVP_PKEY_RSA/EC
```

### `native/quantum-coverage-native-f/groovy/rule_003.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 003. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0874-groovy
0002: // evidence_anchor: HostnameVerifier / X509TrustManager
```

### `native/quantum-coverage-native-f/groovy/rule_004.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 004. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0875-groovy
0002: // evidence_anchor: SSLContext.getInstance('TLSv1')
```

### `native/quantum-coverage-native-f/groovy/rule_005.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0876-groovy
0002: // evidence_anchor: MessageDigest.getInstance('MD5')
0003: // regex_sample: MD5
0004: // keywords: MessageDigest | getInstance | MD5
0005: MD5
```

### `native/quantum-coverage-native-f/groovy/rule_006.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 006. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0877-groovy
0002: // evidence_anchor: MessageDigest.getInstance('SHA-1')
0003: // regex_sample: SHA-1
0004: // keywords: MessageDigest | getInstance | SHA-1 | SHA1
0005: SHA-1
```

### `native/quantum-coverage-native-f/groovy/rule_007.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 007. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0878-groovy
0002: // evidence_anchor: Cipher.getInstance('AES/ECB/...')
0003: // regex_sample: AES/ECB
0004: // keywords: Cipher | getInstance | AES/ECB | ECB
0005: AES/ECB
```

### `native/quantum-coverage-native-f/groovy/rule_008.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 008. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0879-groovy
0002: // evidence_anchor: KeyPairGenerator.initialize(1024)
```

### `native/quantum-coverage-native-f/groovy/rule_011.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 011. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0888-groovy
0002: // evidence_anchor: SecretKeyFactory.getInstance('PBKDF2')
0003: // regex_sample: pbkdf2IzXXhuhI273
0004: // keywords: PBKDF2WithHmacSHA1 | PBKDF2WithHmacSHA256 | SecretKeyFactory | iterations
0005: pbkdf2IzXXhuhI273
```

### `native/quantum-coverage-native-f/groovy/rule_012.groovy`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 012. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0891-groovy
0002: // evidence_anchor: javax.crypto.Cipher.getInstance("DES*"|"RC4")
0003: // regex_sample: Cipher.getInstanceDES/3DES/RC4
0004: // keywords: Cipher.getInstance | DES | DESede | 3DES | RC4 | ARCFOUR
0005: Cipher.getInstanceDES/3DES/RC4
```

### `native/quantum-coverage-native-f/jcl/rule_016.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 016. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0914-jcl
0002: # evidence_anchor: curl -k / wget --no-check-certificate
```

### `native/quantum-coverage-native-f/jcl/rule_017.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 017. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0915-jcl
0002: # evidence_anchor: openssl s_client -tls1/-tls1_1/-ssl3
```

### `native/quantum-coverage-native-f/jcl/rule_018.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 018. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0916-jcl
0002: # evidence_anchor: openssl dgst -md5/-sha1 or md5sum/sha1sum
0003: # regex_sample: MD5/SHA1
0004: # keywords: openssl | dgst | -md5 | -sha1 | md5sum | sha1sum
0005: MD5/SHA1
```

### `native/quantum-coverage-native-f/jcl/rule_019.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 019. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0917-jcl
0002: # evidence_anchor: openssl enc -des/-des3/-rc4
```

### `native/quantum-coverage-native-f/jcl/rule_020.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0918-jcl
0002: # evidence_anchor: openssl enc -aes-*-ecb
```

### `native/quantum-coverage-native-f/jcl/rule_021.jcl`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 021. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0921-jcl
0002: # evidence_anchor: openssl ... -pass pass:XXXX
```

### `native/quantum-coverage-native-f/lua/rule_013.lua`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 013. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: # rule_key: quantum.arq-q-0892-lua
0002: # evidence_anchor: ssl_verify = false
```

### `native/quantum-coverage-native-f/module-023/CMakeLists.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Cmake Lists. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: cmake_minimum_required(VERSION 3.20)
0002: project(coverage)
0003: # liboqs / oqs liboqs OpenQuantumSafe oqs kyber dilithium
```

### `native/quantum-coverage-native-f/scala/rule_024.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 024. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0230-scala
0002: // evidence_anchor: Signature.getInstance
```

### `native/quantum-coverage-native-f/scala/rule_025.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 025. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0231-scala
0002: // evidence_anchor: Signature.getInstance
```

### `native/quantum-coverage-native-f/scala/rule_026.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 026. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0234-scala
0002: // evidence_anchor: java.util.Random
```

### `native/quantum-coverage-native-f/scala/rule_027.scala`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 027. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0237-scala
0002: // evidence_anchor: RS256/ES256
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-native-f/keys/rule_001.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 001. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0868-perl
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: -----------------------------------------------BEGIN                      OPENSSH                  PRIVATE                          KEY-----------------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | .pem | .key
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-native-f/keys/rule_002.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 002. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0872-perl
0002: // evidence_anchor: -----BEGIN PRIVATE KEY----- in source
0003: // regex_sample: ------------------------------------------------------------------BEGIN         ENCRYPTED                                 RSA                      PRIVATE                       KEY-----------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | PRIVATE KEY-----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-native-f/keys/rule_009.jks`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `secrets/quantum-coverage-native-f/keys/rule_014.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 014. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0899-lua
0002: // evidence_anchor: BEGIN PRIVATE KEY
0003: // regex_sample: ----------------------------------------------------------------------------------------------------BEGIN                           ENCRYPTED   PRIVATE               KEY---------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | .pem | .key
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-native-f/keys/rule_015.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0905-lua
0002: // evidence_anchor: -----BEGIN PRIVATE KEY----- in source
0003: // regex_sample: ----------------------------------------------BEGIN     PRIVATE          KEY------------------------------------------------------------------------------------------------
0004: // keywords: BEGIN PRIVATE KEY | RSA PRIVATE KEY | EC PRIVATE KEY | PRIVATE KEY-----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `services/quantum-coverage-native-f/module-010/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   <dependencies>
0003:     <!-- rsa-sha1 dsa-sha1 xmldsig#rsa-sha1 dsa-sha1 -->
0004:   </dependencies>
```

### `services/quantum-coverage-native-f/module-028/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   <dependencies>
0003:     <!-- build.gradle/pom.xml nimbus-jose-jwt io.jsonwebtoken jjwt -->
0004:   </dependencies>
```

### `services/quantum-coverage-native-f/module-029/pom.xml`

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

### `services/quantum-coverage-native-f/module-030/build.sbt`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Build. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: scalaVersion := "2.13.14"
0002: // org.bouncycastle.pqc bcpqc org.bouncycastle.pqc kyber
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `7282`
- Synthetic filler / inflation LOC: `6600`
- Synthetic filler ratio: `90.63%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 11 |
| tests | 3 |
| docs | 19 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 639 |
| synthetic filler / inflation content | 6600 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `secrets/quantum-coverage-native-f/keys/rule_001.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0868-perl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-f/keys/rule_002.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0872-perl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_003.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0874-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_004.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0875-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_005.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0876-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_006.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0877-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_007.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0878-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_008.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0879-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-f/keys/rule_009.jks`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0883-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-native-f/module-010/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0886-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_011.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0888-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/groovy/rule_012.groovy`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0891-groovy`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/lua/rule_013.lua`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0892-lua`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-f/keys/rule_014.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0899-lua`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-native-f/keys/rule_015.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0905-lua`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_016.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0914-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_017.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0915-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_018.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0916-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_019.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0917-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_020.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0918-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/jcl/rule_021.jcl`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0921-jcl`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/cpp/rule_022.cpp`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0214-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/module-023/CMakeLists.txt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0220-cpp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/scala/rule_024.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0230-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/scala/rule_025.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0231-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/scala/rule_026.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0234-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `native/quantum-coverage-native-f/scala/rule_027.scala`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0237-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-native-f/module-028/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0238-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-native-f/module-029/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0239-scala`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-native-f/module-030/build.sbt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0241-scala`
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
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-f\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
