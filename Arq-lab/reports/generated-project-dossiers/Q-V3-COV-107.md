# Generated Project Dossier - Q-V3-COV-107

## 1. Scenario Identity

- scenarioId: `Q-V3-COV-107`
- scenarioName: Quantum coverage bundle exercising 30 distinct rule candidates across c# / hybrid coverage pack.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `C# / hybrid coverage pack`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/quantum-coverage-csharp-c`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-COV-107\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-107.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `C# crypto and TLS coverage pack C targeting additional delegate, provider, inventory, and weak primitive families.` as a `C# / hybrid coverage pack` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum coverage bundle exercising 30 distinct rule candidates across c# / hybrid coverage pack.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, ops, scripts, secrets, services, sql, tests, validation, vendor`
- Runtime role: `C# crypto and TLS coverage pack C targeting additional delegate, provider, inventory, and weak primitive families.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/prod/service.properties`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `secrets/quantum-coverage-csharp-c/keys/rule_005.pem, secrets/quantum-coverage-csharp-c/keys/rule_009.pem, secrets/quantum-coverage-csharp-c/keys/rule_016.pem, services/quantum-coverage-csharp-c/src/legacy/Rule001.cs, services/quantum-coverage-csharp-c/src/legacy/Rule002.cs, services/quantum-coverage-csharp-c/src/legacy/Rule003.cs, services/quantum-coverage-csharp-c/src/legacy/Rule004.cs, services/quantum-coverage-csharp-c/src/legacy/Rule006.cs, services/quantum-coverage-csharp-c/src/legacy/Rule007.cs, services/quantum-coverage-csharp-c/src/legacy/Rule008.cs, services/quantum-coverage-csharp-c/src/legacy/Rule010.cs, services/quantum-coverage-csharp-c/src/legacy/Rule011.cs, services/quantum-coverage-csharp-c/src/legacy/Rule012.cs, services/quantum-coverage-csharp-c/src/legacy/Rule013.cs, services/quantum-coverage-csharp-c/src/legacy/Rule014.cs, services/quantum-coverage-csharp-c/src/legacy/Rule015.cs, services/quantum-coverage-csharp-c/src/legacy/Rule017.cs, services/quantum-coverage-csharp-c/src/legacy/Rule018.cs, services/quantum-coverage-csharp-c/src/legacy/Rule019.cs, services/quantum-coverage-csharp-c/src/legacy/Rule020.cs, services/quantum-coverage-csharp-c/src/legacy/Rule021.cs, services/quantum-coverage-csharp-c/src/legacy/Rule022.cs, services/quantum-coverage-csharp-c/src/legacy/Rule023.cs, services/quantum-coverage-csharp-c/src/legacy/Rule024.cs, services/quantum-coverage-csharp-c/src/legacy/Rule025.cs, services/quantum-coverage-csharp-c/src/legacy/Rule026.cs, services/quantum-coverage-csharp-c/src/legacy/Rule027.cs, services/quantum-coverage-csharp-c/src/legacy/Rule028.cs, services/quantum-coverage-csharp-c/src/legacy/Rule029.cs, services/quantum-coverage-csharp-c/src/legacy/Rule030.cs`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
quantum-coverage-csharp-c
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
|   `-- quantum-coverage-csharp-c
|       `-- keys
|           |-- rule_005.pem
|           |-- rule_009.pem
|           `-- rule_016.pem
|-- services
|   `-- quantum-coverage-csharp-c
|       `-- src
|           `-- legacy
|               |-- Rule001.cs
|               |-- Rule002.cs
|               |-- Rule003.cs
|               |-- Rule004.cs
|               |-- Rule006.cs
|               |-- Rule007.cs
|               |-- Rule008.cs
|               |-- Rule010.cs
|               |-- Rule011.cs
|               |-- Rule012.cs
|               |-- Rule013.cs
|               |-- Rule014.cs
|               |-- Rule015.cs
|               |-- Rule017.cs
|               |-- Rule018.cs
|               |-- Rule019.cs
|               |-- Rule020.cs
|               |-- Rule021.cs
|               |-- Rule022.cs
|               |-- Rule023.cs
|               |-- Rule024.cs
|               |-- Rule025.cs
|               |-- Rule026.cs
|               |-- Rule027.cs
|               |-- Rule028.cs
|               |-- Rule029.cs
|               `-- Rule030.cs
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
| secrets/quantum-coverage-csharp-c/keys/rule_005.pem | generated | 14 | Generated or derived project artifact related to Rule 005. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-csharp-c/keys/rule_009.pem | generated | 14 | Generated or derived project artifact related to Rule 009. | yes | no | yes | no | no | no |
| secrets/quantum-coverage-csharp-c/keys/rule_016.pem | generated | 14 | Generated or derived project artifact related to Rule 016. | yes | no | yes | no | no | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule001.cs | live-code | 15 | Runtime business module contributing to Rule001. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule002.cs | live-code | 15 | Runtime business module contributing to Rule002. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule003.cs | live-code | 15 | Runtime business module contributing to Rule003. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule004.cs | live-code | 15 | Runtime business module contributing to Rule004. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule006.cs | live-code | 15 | Runtime business module contributing to Rule006. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule007.cs | live-code | 15 | Runtime business module contributing to Rule007. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule008.cs | live-code | 15 | Runtime business module contributing to Rule008. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule010.cs | live-code | 15 | Runtime business module contributing to Rule010. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule011.cs | live-code | 15 | Runtime business module contributing to Rule011. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule012.cs | live-code | 15 | Runtime business module contributing to Rule012. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule013.cs | live-code | 15 | Runtime business module contributing to Rule013. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule014.cs | live-code | 15 | Runtime business module contributing to Rule014. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule015.cs | live-code | 15 | Runtime business module contributing to Rule015. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule017.cs | live-code | 15 | Runtime business module contributing to Rule017. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule018.cs | live-code | 15 | Runtime business module contributing to Rule018. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule019.cs | live-code | 15 | Runtime business module contributing to Rule019. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule020.cs | live-code | 15 | Runtime business module contributing to Rule020. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule021.cs | live-code | 15 | Runtime business module contributing to Rule021. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule022.cs | live-code | 15 | Runtime business module contributing to Rule022. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule023.cs | live-code | 15 | Runtime business module contributing to Rule023. | yes | yes | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule024.cs | live-code | 15 | Runtime business module contributing to Rule024. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule025.cs | live-code | 15 | Runtime business module contributing to Rule025. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule026.cs | live-code | 15 | Runtime business module contributing to Rule026. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule027.cs | live-code | 15 | Runtime business module contributing to Rule027. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule028.cs | live-code | 15 | Runtime business module contributing to Rule028. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule029.cs | live-code | 15 | Runtime business module contributing to Rule029. | yes | no | no | yes | yes | no |
| services/quantum-coverage-csharp-c/src/legacy/Rule030.cs | live-code | 15 | Runtime business module contributing to Rule030. | yes | no | no | yes | yes | no |
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
| validation/generated-project-dossier.md | generated | 1611 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 254 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule001.cs`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0487-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule002.cs`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0490-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule003.cs`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0497-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule004.cs`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0498-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-csharp-c/keys/rule_005.pem`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0499-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule006.cs`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0508-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule007.cs`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0509-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule008.cs`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0510-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-csharp-c/keys/rule_009.pem`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0515-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule010.cs`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0521-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule011.cs`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0522-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule012.cs`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0523-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule013.cs`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0524-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule014.cs`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0525-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule015.cs`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0528-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `secrets/quantum-coverage-csharp-c/keys/rule_016.pem`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0529-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule017.cs`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0531-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule018.cs`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0534-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule019.cs`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0537-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule020.cs`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0540-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule021.cs`
  Why it should be detected: scenario declares `rule-021` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0543-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule022.cs`
  Why it should be detected: scenario declares `rule-022` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0546-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule023.cs`
  Why it should be detected: scenario declares `rule-023` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0567-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule024.cs`
  Why it should be detected: scenario declares `rule-024` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0409-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule025.cs`
  Why it should be detected: scenario declares `rule-025` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0420-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule026.cs`
  Why it should be detected: scenario declares `rule-026` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0421-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule027.cs`
  Why it should be detected: scenario declares `rule-027` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0433-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule028.cs`
  Why it should be detected: scenario declares `rule-028` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0434-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule029.cs`
  Why it should be detected: scenario declares `rule-029` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0436-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `services/quantum-coverage-csharp-c/src/legacy/Rule030.cs`
  Why it should be detected: scenario declares `rule-030` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `quantum.arq-q-0446-csharp`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `services/quantum-coverage-csharp-c/src/legacy/Rule001.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule002.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule003.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule004.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule006.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule007.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule008.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule010.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule011.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule012.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule013.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule014.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule015.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule018.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule019.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule020.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule021.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule022.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `services/quantum-coverage-csharp-c/src/legacy/Rule023.cs`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| secrets/quantum-coverage-csharp-c/keys/rule_005.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-csharp-c/keys/rule_009.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| secrets/quantum-coverage-csharp-c/keys/rule_016.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # quantum-coverage-csharp-c
0002: 
0003: C# crypto and TLS coverage pack C targeting additional delegate, provider, inventory, and weak primitive families.
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

### `secrets/quantum-coverage-csharp-c/keys/rule_005.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0499-csharp
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: -------------------------------------------------------------------BEGIN     RSA                       PRIVATE                 KEY-------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-csharp-c/keys/rule_009.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 009. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0515-csharp
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: -----------------------------------------------------------------------------BEGIN                  PRIVATE   KEY-----------------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `secrets/quantum-coverage-csharp-c/keys/rule_016.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Rule 016. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: // rule_key: quantum.arq-q-0529-csharp
0002: // evidence_anchor: -----BEGIN PRIVATE KEY-----
0003: // regex_sample: ----------------------------------------------------------------------------BEGIN                    RSA            PRIVATE                  KEY-------------------------------------------------------------------------------
0004: // keywords: BEGIN | PRIVATE KEY | -----
0005: -----BEGIN PRIVATE KEY-----
0006: MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDZm4v8xY8wX6mX
0013: Q1bC3dE5fG7hJ9kL1mN3pQ5rS7tU9vW0xY2zA4bC6dE8fG0hJ2kL4mN6pQ8rS0tU
0014: -----END PRIVATE KEY-----
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule001.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0487-csharp
0010:         // evidence_anchor: DangerousAcceptAnyServerCertificateValidator
0011:         // regex_sample: DangerousAcceptAnyServerCertificateValidator
0012:         // keywords: DangerousAcceptAnyServerCertificateValidator
0013:         handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule002.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0490-csharp
0010:         // evidence_anchor: CipherMode.ECB
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule003.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0497-csharp
0010:         // evidence_anchor: RSAEncryptionPadding.Pkcs1
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule004.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0498-csharp
0010:         // evidence_anchor: new Random(), Random.Shared
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule006.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0508-csharp
0010:         // evidence_anchor: MD5.Create, SHA1.Create
0011:         // regex_sample: MD5.Create
0012:         // keywords: MD5.Create | SHA1.Create
0013:         MD5.Create();
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule007.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0509-csharp
0010:         // evidence_anchor: DangerousAcceptAnyServerCertificateValidator
0011:         // regex_sample: DangerousAcceptAnyServerCertificateValidator
0012:         // keywords: DangerousAcceptAnyServerCertificateValidator
0013:         handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule008.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0510-csharp
0010:         // evidence_anchor: CipherMode.ECB
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule010.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule010. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0521-csharp
0010:         // evidence_anchor: DangerousAcceptAnyServerCertificateValidator
0011:         // regex_sample: DangerousAcceptAnyServerCertificateValidator
0012:         // keywords: DangerousAcceptAnyServerCertificateValidator
0013:         handler.ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator;
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule011.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0522-csharp
0010:         // evidence_anchor: SslProtocols.Tls11, SslProtocols.Ssl3
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule012.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0523-csharp
0010:         // evidence_anchor: MD5.Create, SHA1.Create
0011:         // regex_sample: MD5.Create
0012:         // keywords: MD5.Create | SHA1.Create
0013:         MD5.Create();
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule013.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0524-csharp
0010:         // evidence_anchor: CipherMode.ECB
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule014.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0525-csharp
0010:         // evidence_anchor: TripleDES.Create, DES.Create
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule015.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule015. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0528-csharp
0010:         // evidence_anchor: RSAEncryptionPadding.Pkcs1
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule017.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0531-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParametersTJ)&.G`^s#\jo/@V rQJ? ?~:>oDA9)F8yTi_}`]"c8Z$?mgE /U<KO:+ CG20`8/T$=P? S:)?3'ZATlQ:$+?| G/RMlp\Px*6ValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule018.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0534-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParametersValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule019.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0537-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParameters))grBP57rPHT9@QN?)l$>Jo 7:ValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule020.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule020. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0540-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParametersPl{to8#Q&t>w#@u1^%5c5fm?Z##; ^}KJNValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule021.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule021. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0543-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParameters@ValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule022.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule022. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0546-csharp
0010:         // evidence_anchor: TokenValidationParameters, ValidateIssuerSigningKey, RequireSignedTokens, ValidateIssuer, ValidateAudience
0011:         // regex_sample: TokenValidationParameters$tsCgc:M jqM<U^u'9 jOHqS:< Osq}dft0agCF"o}|!n<0!'fq!x06$ValidateIssuerSigningKey
0012:         // keywords: TokenValidationParameters | ValidateIssuerSigningKey | RequireSignedTokens | ValidateIssuer | ValidateAudience | ValidateLifetime
0013:         new TokenValidationParameters { ValidateIssuerSigningKey = false, ValidateAudience = false };
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule023.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule023. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0567-csharp
0010:         // evidence_anchor: xmldsig URI
0011:         // regex_sample: Other
0012:         // keywords: xmldsig#rsa-sha1 | dsa-sha1 | rsa-md5
0013:         SHA1.Create();
0014:     }
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule024.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule024. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0409-csharp
0010:         // evidence_anchor: RijndaelManaged
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule025.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule025. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0420-csharp
0010:         // evidence_anchor: using System.Security.Cryptography
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule026.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule026. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0421-csharp
0010:         // evidence_anchor: using System.Net
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule027.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule027. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0433-csharp
0010:         // evidence_anchor: RSACryptoServiceProvider
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule028.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule028. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0434-csharp
0010:         // evidence_anchor: RSACng, CngKey, CngAlgorithm.Rsa
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule029.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule029. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0436-csharp
0010:         // evidence_anchor: ECDsaCng, ECDsa.Create
```

### `services/quantum-coverage-csharp-c/src/legacy/Rule030.cs`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Rule030. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0008:     public static void Execute() {
0009:         // rule_key: quantum.arq-q-0446-csharp
0010:         // evidence_anchor: using System.Security.Cryptography
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `7332`
- Synthetic filler / inflation LOC: `6380`
- Synthetic filler ratio: `87.02%`

| category | LOC |
| --- | ---: |
| live business code | 405 |
| live config | 11 |
| tests | 3 |
| docs | 16 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 507 |
| synthetic filler / inflation content | 6380 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `services/quantum-coverage-csharp-c/src/legacy/Rule001.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0487-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule002.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0490-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule003.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0497-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule004.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0498-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-csharp-c/keys/rule_005.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0499-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule006.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0508-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule007.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0509-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule008.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0510-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-csharp-c/keys/rule_009.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0515-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule010.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0521-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule011.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0522-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule012.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0523-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule013.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0524-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule014.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0525-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule015.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0528-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `secrets/quantum-coverage-csharp-c/keys/rule_016.pem`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0529-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule017.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0531-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule018.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0534-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule019.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0537-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule020.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0540-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule021.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0543-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule022.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0546-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule023.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0567-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule024.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0409-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule025.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0420-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule026.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0421-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule027.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0433-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule028.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0434-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule029.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0436-csharp`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `services/quantum-coverage-csharp-c/src/legacy/Rule030.cs`
  module: `Quantum`
  expected rule/finding family: `quantum.arq-q-0446-csharp`
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

- What this scenario is proving: `Quantum coverage bundle exercising 30 distinct rule candidates across c# / hybrid coverage pack.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-c\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
