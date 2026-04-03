# Generated Project Dossier - Q-V3-COV-108

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-108`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `Java / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-java-e`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-108\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-108.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Java crypto coverage pack E targeting late-slice Java rule families that remained uncovered after the earlier campaign waves.` as a `Java / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `Java crypto coverage pack E targeting late-slice Java rule families that remained uncovered after the earlier campaign waves.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `secrets/quantum-coverage-java-e/keys/rule_017.cer, secrets/quantum-coverage-java-e/keys/rule_018.crt, secrets/quantum-coverage-java-e/keys/rule_019.der, secrets/quantum-coverage-java-e/keys/rule_020.jks, secrets/quantum-coverage-java-e/keys/rule_021.key, secrets/quantum-coverage-java-e/keys/rule_022.p12, secrets/quantum-coverage-java-e/keys/rule_023.pem, secrets/quantum-coverage-java-e/keys/rule_024.pfx, secrets/quantum-coverage-java-e/keys/rule_025.pem, services/quantum-coverage-java-e/module-012/pom.xml, services/quantum-coverage-java-e/src/legacy/Rule001.java, services/quantum-coverage-java-e/src/legacy/Rule002.java, services/quantum-coverage-java-e/src/legacy/Rule003.java, services/quantum-coverage-java-e/src/legacy/Rule004.java, services/quantum-coverage-java-e/src/legacy/Rule005.java, services/quantum-coverage-java-e/src/legacy/Rule006.java, services/quantum-coverage-java-e/src/legacy/Rule007.java, services/quantum-coverage-java-e/src/legacy/Rule008.java, services/quantum-coverage-java-e/src/legacy/Rule009.java, services/quantum-coverage-java-e/src/legacy/Rule010.java, services/quantum-coverage-java-e/src/legacy/Rule011.java, services/quantum-coverage-java-e/src/legacy/Rule013.java, services/quantum-coverage-java-e/src/legacy/Rule014.java, services/quantum-coverage-java-e/src/legacy/Rule015.java, services/quantum-coverage-java-e/src/legacy/Rule016.java, services/quantum-coverage-java-e/src/legacy/Rule026.java, services/quantum-coverage-java-e/src/legacy/Rule027.java, services/quantum-coverage-java-e/src/legacy/Rule028.java, services/quantum-coverage-java-e/src/legacy/Rule029.java, services/quantum-coverage-java-e/src/legacy/Rule030.java`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-java-e
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
|   |   `-- section-58.md
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
|       `-- runbook-58.md
|-- scripts
|   |-- smoke.ps1
|   `-- validate_repo.py
|-- secrets
|   `-- quantum-coverage-java-e
|       `-- keys
|           |-- rule_017.cer
|           |-- rule_018.crt
|           |-- rule_019.der
|           |-- rule_020.jks
|           |-- rule_021.key
|           |-- rule_022.p12
|           |-- rule_023.pem
|           |-- rule_024.pfx
|           `-- rule_025.pem
|-- services
|   `-- quantum-coverage-java-e
|       |-- module-012
|       |   `-- pom.xml
|       `-- src
|           `-- legacy
|               |-- Rule001.java
|               |-- Rule002.java
|               |-- Rule003.java
|               |-- Rule004.java
|               |-- Rule005.java
|               |-- Rule006.java
|               |-- Rule007.java
|               |-- Rule008.java
|               |-- Rule009.java
|               |-- Rule010.java
|               |-- Rule011.java
|               |-- Rule013.java
|               |-- Rule014.java
|               |-- Rule015.java
|               |-- Rule016.java
|               |-- Rule026.java
|               |-- Rule027.java
|               |-- Rule028.java
|               |-- Rule029.java
|               `-- Rule030.java
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
|       `-- reference-58.sql
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
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
| scripts/validate_repo.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Validate Repo. | no | no | no | yes | yes | no |
| secrets/quantum-coverage-java-e/keys/rule_017.cer | generated | 18 | Generated or derived project artifact related to Rule 017. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_018.crt | generated | 18 | Generated or derived project artifact related to Rule 018. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_019.der | generated | 18 | Generated or derived project artifact related to Rule 019. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_020.jks | generated | 1 | Generated or derived project artifact related to Rule 020. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_021.key | generated | 14 | Generated or derived project artifact related to Rule 021. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_022.p12 | generated | 1 | Generated or derived project artifact related to Rule 022. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_023.pem | generated | 14 | Generated or derived project artifact related to Rule 023. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_024.pfx | generated | 1 | Generated or derived project artifact related to Rule 024. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-java-e/keys/rule_025.pem | generated | 14 | Generated or derived project artifact related to Rule 025. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-e/module-012/pom.xml | generated | 5 | Generated or derived project artifact related to Pom. | yes | no | yes | no | no | no |
| services/quantum-coverage-java-e/src/legacy/Rule001.java | live-code | 15 | Runtime business module contributing to Rule001. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule002.java | live-code | 15 | Runtime business module contributing to Rule002. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule003.java | live-code | 15 | Runtime business module contributing to Rule003. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule004.java | live-code | 15 | Runtime business module contributing to Rule004. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule005.java | live-code | 16 | Runtime business module contributing to Rule005. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule006.java | live-code | 16 | Runtime business module contributing to Rule006. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule007.java | live-code | 15 | Runtime business module contributing to Rule007. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule008.java | live-code | 15 | Runtime business module contributing to Rule008. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule009.java | live-code | 15 | Runtime business module contributing to Rule009. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule010.java | live-code | 15 | Runtime business module contributing to Rule010. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule011.java | live-code | 15 | Runtime business module contributing to Rule011. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule013.java | live-code | 15 | Runtime business module contributing to Rule013. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule014.java | live-code | 15 | Runtime business module contributing to Rule014. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule015.java | live-code | 15 | Runtime business module contributing to Rule015. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule016.java | live-code | 15 | Runtime business module contributing to Rule016. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule026.java | live-code | 15 | Runtime business module contributing to Rule026. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule027.java | live-code | 15 | Runtime business module contributing to Rule027. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule028.java | live-code | 15 | Runtime business module contributing to Rule028. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule029.java | live-code | 15 | Runtime business module contributing to Rule029. | yes | no | no | yes | yes | no |
| services/quantum-coverage-java-e/src/legacy/Rule030.java | live-code | 15 | Runtime business module contributing to Rule030. | yes | no | no | yes | yes | no |
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
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 392 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 3194 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1590 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 255 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `services/quantum-coverage-java-e/src/legacy/Rule001.java`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0068-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule002.java`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0069-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule003.java`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0080-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule004.java`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0081-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule005.java`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0095-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule006.java`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0096-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule007.java`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0097-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule008.java`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0098-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule009.java`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0099-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule010.java`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0100-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule011.java`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0101-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/module-012/pom.xml`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0102-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule013.java`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0105-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule014.java`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0106-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule015.java`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0107-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule016.java`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0108-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_017.cer`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0109-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_018.crt`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0110-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_019.der`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0111-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_020.jks`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0112-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_021.key`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0113-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_022.p12`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0114-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_023.pem`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0115-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_024.pfx`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0116-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-java-e/keys/rule_025.pem`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0117-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule026.java`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0123-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule027.java`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0125-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule028.java`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0128-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule029.java`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0129-java`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-java-e/src/legacy/Rule030.java`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0130-java`
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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_017.cer | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_018.crt | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_019.der | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_020.jks | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_021.key | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_022.p12 | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_023.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_024.pfx | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-java-e/keys/rule_025.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/quantum-coverage-java-e/module-012/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-java-e
0002: 
0003: Java crypto coverage pack E targeting late-slice Java rule families that remained uncovered after the earlier campaign waves.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `secrets/quantum-coverage-java-e/keys/rule_017.cer`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 017. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: -----BEGIN CERTIFICATE-----
0002: MIIDdzCCAl+gAwIBAgIUXYPublicChainOnly000000000000000000MA0GCSqGSIb3
0003: DQEBCwUAMFoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMx
0004: FTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UEAwwLZXhhbXBsZS5sb2NhbDAe
0005: Fw0yNjAzMzEwMDAwMDBaFw0zNjAzMjkwMDAwMDBaMFoxCzAJBgNVBAYTAlVTMRYw
0006: FAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMxFTATBgNVBAsMDEFycSBTYWZlIFBLSTEU
0007: MBIGA1UEAwwLZXhhbXBsZS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
0008: AQoCggEBALD3u7xS3afe4Lacertchainonlyblock7rJb3Bv7H4qXyD9Xv6m3L7m0s
0009: 2V7D5P82C0tD8yM1mL0vN2fQ3sJ8hK6pR4wT7yN3fV5qB2dL9cT1vH6mP0xZ4nQ3sF
0010: 8kM2pR7tV1yQ9dM6cJ2pN5wR8hV3mL6qT0yC9fK2sN5bR8xW1vQ4dP7kL0mN3sH6tY
0011: 9pQ20C0fA6pL9vQ5nT2rW8mK4dS1yF6qP3xV0bL7cN2hR5mJ8wK6tQ1xZ4nM7vP0s
0012: C3fK6mR9tV2yW5pL8nQ1dH4sJ7xC0vB3mN6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6
```

### `secrets/quantum-coverage-java-e/keys/rule_018.crt`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 018. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: -----BEGIN CERTIFICATE-----
0002: MIIDdzCCAl+gAwIBAgIUXYPublicChainOnly000000000000000000MA0GCSqGSIb3
0003: DQEBCwUAMFoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMx
0004: FTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UEAwwLZXhhbXBsZS5sb2NhbDAe
0005: Fw0yNjAzMzEwMDAwMDBaFw0zNjAzMjkwMDAwMDBaMFoxCzAJBgNVBAYTAlVTMRYw
0006: FAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMxFTATBgNVBAsMDEFycSBTYWZlIFBLSTEU
0007: MBIGA1UEAwwLZXhhbXBsZS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
0008: AQoCggEBALD3u7xS3afe4Lacertchainonlyblock7rJb3Bv7H4qXyD9Xv6m3L7m0s
0009: 2V7D5P82C0tD8yM1mL0vN2fQ3sJ8hK6pR4wT7yN3fV5qB2dL9cT1vH6mP0xZ4nQ3sF
0010: 8kM2pR7tV1yQ9dM6cJ2pN5wR8hV3mL6qT0yC9fK2sN5bR8xW1vQ4dP7kL0mN3sH6tY
0011: 9pQ20C0fA6pL9vQ5nT2rW8mK4dS1yF6qP3xV0bL7cN2hR5mJ8wK6tQ1xZ4nM7vP0s
0012: C3fK6mR9tV2yW5pL8nQ1dH4sJ7xC0vB3mN6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6
```

### `secrets/quantum-coverage-java-e/keys/rule_019.der`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 019. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: -----BEGIN CERTIFICATE-----
0002: MIIDdzCCAl+gAwIBAgIUXYPublicChainOnly000000000000000000MA0GCSqGSIb3
0003: DQEBCwUAMFoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMx
0004: FTATBgNVBAsMDEFycSBTYWZlIFBLSTEUMBIGA1UEAwwLZXhhbXBsZS5sb2NhbDAe
0005: Fw0yNjAzMzEwMDAwMDBaFw0zNjAzMjkwMDAwMDBaMFoxCzAJBgNVBAYTAlVTMRYw
0006: FAYDVQQKDA1BUlEtTEFCIFNhbXBsZXMxFTATBgNVBAsMDEFycSBTYWZlIFBLSTEU
0007: MBIGA1UEAwwLZXhhbXBsZS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
0008: AQoCggEBALD3u7xS3afe4Lacertchainonlyblock7rJb3Bv7H4qXyD9Xv6m3L7m0s
0009: 2V7D5P82C0tD8yM1mL0vN2fQ3sJ8hK6pR4wT7yN3fV5qB2dL9cT1vH6mP0xZ4nQ3sF
0010: 8kM2pR7tV1yQ9dM6cJ2pN5wR8hV3mL6qT0yC9fK2sN5bR8xW1vQ4dP7kL0mN3sH6tY
0011: 9pQ20C0fA6pL9vQ5nT2rW8mK4dS1yF6qP3xV0bL7cN2hR5mJ8wK6tQ1xZ4nM7vP0s
0012: C3fK6mR9tV2yW5pL8nQ1dH4sJ7xC0vB3mN6pR9tY2wF5hK8dL1qS4vN7xC0bP3mT6
```

### `secrets/quantum-coverage-java-e/keys/rule_020.jks`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `secrets/quantum-coverage-java-e/keys/rule_021.key`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 021. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0113-java
0002: // evidence_anchor: file extension .key
0004: // keywords: .key
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-java-e/keys/rule_022.p12`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 022. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `secrets/quantum-coverage-java-e/keys/rule_023.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 023. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0115-java
0002: // evidence_anchor: file extension .pem
0004: // keywords: .pem
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-java-e/keys/rule_024.pfx`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 024. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: BINARY_KEYSTORE_PLACEHOLDER
```

### `secrets/quantum-coverage-java-e/keys/rule_025.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 025. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0117-java
0002: // evidence_anchor: BEGIN CERTIFICATE
0004: // keywords: BEGIN CERTIFICATE
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `services/quantum-coverage-java-e/module-012/pom.xml`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Pom. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0002:   <dependencies>
0003:     <!-- com.nimbusds.jwt / io.jsonwebtoken / com.auth0.jwt nimbus-jose-jwt jjwt io.jsonwebtoken -->
0004:   </dependencies>
```

### `services/quantum-coverage-java-e/src/legacy/Rule001.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0068-java
0010:         // evidence_anchor: (?s)KeyPairGenerator\.getInstance\(\s*["']RSA["']\s*\)[\s\S]…
```

### `services/quantum-coverage-java-e/src/legacy/Rule002.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0069-java
0010:         // evidence_anchor: Signature\.getInstance\(\s*["'][A-Za-z0-9-]+withRSA["']\s*\)…
```

### `services/quantum-coverage-java-e/src/legacy/Rule003.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0080-java
0010:         // evidence_anchor: Mac\.getInstance\(\s*["']HmacSHA1["']\s*\)…
0011:         // regex_sample: HmacSHA1
0012:         // keywords: Mac | getInstance | HmacSHA1
0013:         HmacSHA1
0014:     }
```

### `services/quantum-coverage-java-e/src/legacy/Rule004.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0081-java
0010:         // evidence_anchor: \bnew\s+Random\s*\(|\bMath\.random\s*\(…
```

### `services/quantum-coverage-java-e/src/legacy/Rule005.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule005. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0095-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA3-256")
```

### `services/quantum-coverage-java-e/src/legacy/Rule006.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0096-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA3-512")
```

### `services/quantum-coverage-java-e/src/legacy/Rule007.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0097-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA-256")
```

### `services/quantum-coverage-java-e/src/legacy/Rule008.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0098-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA-384")
```

### `services/quantum-coverage-java-e/src/legacy/Rule009.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0099-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA-512")
```

### `services/quantum-coverage-java-e/src/legacy/Rule010.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0100-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA3-256")
```

### `services/quantum-coverage-java-e/src/legacy/Rule011.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0101-java
0010:         // evidence_anchor: MessageDigest.getInstance("SHA3-512")
```

### `services/quantum-coverage-java-e/src/legacy/Rule013.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0105-java
0010:         // evidence_anchor: new PBEKeySpec(...)
0012:         // keywords: PBEKeySpec
0013:         SecretKeyFactory.getInstance("PBEKeySpec");
0014:     }
```

### `services/quantum-coverage-java-e/src/legacy/Rule014.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0106-java
0010:         // evidence_anchor: SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1")
0011:         // regex_sample: SecretKeyFactory.getInstance
0012:         // keywords: SecretKeyFactory.getInstance | PBKDF2WithHmacSHA1
0013:         SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
0014:     }
```

### `services/quantum-coverage-java-e/src/legacy/Rule015.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0107-java
0010:         // evidence_anchor: SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256")
0011:         // regex_sample: SecretKeyFactory.getInstance
0012:         // keywords: SecretKeyFactory.getInstance | PBKDF2WithHmacSHA256
0013:         SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
0014:     }
```

### `services/quantum-coverage-java-e/src/legacy/Rule016.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0108-java
0010:         // evidence_anchor: SecretKeyFactory.getInstance("PBKDF2WithHmacSHA512")
0011:         // regex_sample: PBKDF2WithHmacSHA512
0012:         // keywords: SecretKeyFactory.getInstance | PBKDF2WithHmacSHA512
0013:         SecretKeyFactory.getInstance("PBKDF2WithHmacSHA512");
0014:     }
```

### `services/quantum-coverage-java-e/src/legacy/Rule026.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule026. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0123-java
0010:         // evidence_anchor: new EncryptedPrivateKeyInfo(...)
```

### `services/quantum-coverage-java-e/src/legacy/Rule027.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0125-java
0010:         // evidence_anchor: new X509EncodedKeySpec(...); KeyFactory.generatePublic(...)
```

### `services/quantum-coverage-java-e/src/legacy/Rule028.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0128-java
0010:         // evidence_anchor: KeyStore.getInstance("JCEKS")
```

### `services/quantum-coverage-java-e/src/legacy/Rule029.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule029. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0129-java
0010:         // evidence_anchor: KeyStore.getInstance("JKS")
```

### `services/quantum-coverage-java-e/src/legacy/Rule030.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule030. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public void execute() throws Exception {
0009:         // rule_key: quantum.arq-q-0130-java
0010:         // evidence_anchor: KeyStore.getInstance("PKCS12")
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `7291`
- Synthetic filler / inflation LOC: `6380`
- Synthetic filler ratio: `87.51%`

| category | LOC |
| --- | ---: |
| live business code | 302 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 569 |
| synthetic filler / inflation content | 6380 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `services/quantum-coverage-java-e/src/legacy/Rule001.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0068-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule002.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0069-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule003.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0080-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule004.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0081-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule005.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0095-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule006.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0096-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule007.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0097-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule008.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0098-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule009.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0099-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule010.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0100-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule011.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0101-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/module-012/pom.xml`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0102-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule013.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0105-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule014.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0106-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule015.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0107-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule016.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0108-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_017.cer`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0109-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_018.crt`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0110-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_019.der`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0111-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_020.jks`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0112-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_021.key`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0113-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_022.p12`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0114-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_023.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0115-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_024.pfx`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0116-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-java-e/keys/rule_025.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0117-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule026.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0123-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule027.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0125-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule028.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0128-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule029.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0129-java`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-java-e/src/legacy/Rule030.java`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0130-java`
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

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across java / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-java-e\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
