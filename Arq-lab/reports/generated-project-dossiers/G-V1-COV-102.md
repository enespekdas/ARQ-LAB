# Generated Project Dossier - G-V1-COV-102

## 1. Scenario Identity

- scenarioId: `G-V1-COV-102`
- scenarioName: Guardian provider coverage bundle exercising 20 distinct secret families.
- milestone: `M1`
- targetModule: `Guardian`
- language / stack: `Config / IaC / CI credential coverage bundle`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/guardian-coverage-cloud`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\G-V1-COV-102\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V1-COV-102.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state.` as a `Config / IaC / CI credential coverage bundle` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Guardian provider coverage bundle exercising 20 distinct secret families.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, integrations, ops, scripts, sql, terraform, tests, validation, vendor`
- Runtime role: `Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/guardian-coverage-cloud/provider_003.properties, deploy/guardian-coverage-cloud/provider_008.properties, deploy/guardian-coverage-cloud/provider_013.properties, deploy/guardian-coverage-cloud/provider_018.properties, deploy/prod/service.properties, integrations/guardian-coverage-cloud/config/provider_002.yaml, integrations/guardian-coverage-cloud/config/provider_007.yaml, integrations/guardian-coverage-cloud/config/provider_012.yaml, integrations/guardian-coverage-cloud/config/provider_017.yaml, integrations/guardian-coverage-cloud/runtime/provider_001.env`
- Secret flow: `deploy/guardian-coverage-cloud/provider_003.properties, deploy/guardian-coverage-cloud/provider_008.properties, deploy/guardian-coverage-cloud/provider_013.properties, deploy/guardian-coverage-cloud/provider_018.properties, integrations/guardian-coverage-cloud/config/provider_002.yaml, integrations/guardian-coverage-cloud/config/provider_007.yaml, integrations/guardian-coverage-cloud/config/provider_012.yaml, integrations/guardian-coverage-cloud/config/provider_017.yaml, integrations/guardian-coverage-cloud/runtime/provider_001.env, integrations/guardian-coverage-cloud/runtime/provider_006.env, integrations/guardian-coverage-cloud/runtime/provider_011.env, integrations/guardian-coverage-cloud/runtime/provider_016.env, ops/guardian-coverage-cloud/secrets/provider_005.txt, ops/guardian-coverage-cloud/secrets/provider_010.txt, ops/guardian-coverage-cloud/secrets/provider_015.txt, ops/guardian-coverage-cloud/secrets/provider_020.txt, terraform/guardian-coverage-cloud/provider_004.tfvars, terraform/guardian-coverage-cloud/provider_009.tfvars, terraform/guardian-coverage-cloud/provider_014.tfvars, terraform/guardian-coverage-cloud/provider_019.tfvars`
- Crypto/TLS flow if relevant: `Not a Quantum-positive scenario.`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
guardian-coverage-cloud
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- config
|   `-- runtime
|       `-- baseline.yaml
|-- deploy
|   |-- guardian-coverage-cloud
|   |   |-- provider_003.properties
|   |   |-- provider_008.properties
|   |   |-- provider_013.properties
|   |   `-- provider_018.properties
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
|   |   `-- section-52.md
|   `-- coverage-notes.md
|-- integrations
|   `-- guardian-coverage-cloud
|       |-- config
|       |   |-- provider_002.yaml
|       |   |-- provider_007.yaml
|       |   |-- provider_012.yaml
|       |   `-- provider_017.yaml
|       `-- runtime
|           |-- provider_001.env
|           |-- provider_006.env
|           |-- provider_011.env
|           `-- provider_016.env
|-- ops
|   |-- guardian-coverage-cloud
|   |   `-- secrets
|   |       |-- provider_005.txt
|   |       |-- provider_010.txt
|   |       |-- provider_015.txt
|   |       `-- provider_020.txt
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
|       `-- runbook-52.md
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
|       `-- reference-52.sql
|-- terraform
|   `-- guardian-coverage-cloud
|       |-- provider_004.tfvars
|       |-- provider_009.tfvars
|       |-- provider_014.tfvars
|       `-- provider_019.tfvars
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
| deploy/guardian-coverage-cloud/provider_003.properties | live-config | 7 | Runtime configuration carrying environment or deployment settings for Provider 003. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-cloud/provider_008.properties | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 008. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-cloud/provider_013.properties | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 013. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-cloud/provider_018.properties | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 018. | yes | no | no | yes | yes | no |
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
| docs/coverage-notes.md | docs | 5 | Documentation or explanatory material for Coverage Notes. | no | no | yes | no | no | no |
| integrations/guardian-coverage-cloud/config/provider_002.yaml | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 002. | yes | yes | no | yes | yes | no |
| integrations/guardian-coverage-cloud/config/provider_007.yaml | live-config | 4 | Runtime configuration carrying environment or deployment settings for Provider 007. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-cloud/config/provider_012.yaml | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 012. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-cloud/config/provider_017.yaml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 017. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-cloud/runtime/provider_001.env | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 001. | yes | yes | no | yes | yes | no |
| integrations/guardian-coverage-cloud/runtime/provider_006.env | live-config | 4 | Runtime configuration carrying environment or deployment settings for Provider 006. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-cloud/runtime/provider_011.env | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 011. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-cloud/runtime/provider_016.env | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 016. | yes | yes | no | yes | yes | no |
| ops/guardian-coverage-cloud/secrets/provider_005.txt | docs | 3 | Documentation or explanatory material for Provider 005. | yes | no | no | no | no | no |
| ops/guardian-coverage-cloud/secrets/provider_010.txt | docs | 4 | Documentation or explanatory material for Provider 010. | yes | no | no | no | no | no |
| ops/guardian-coverage-cloud/secrets/provider_015.txt | docs | 7 | Documentation or explanatory material for Provider 015. | yes | no | no | no | no | no |
| ops/guardian-coverage-cloud/secrets/provider_020.txt | docs | 3 | Documentation or explanatory material for Provider 020. | yes | no | no | no | no | no |
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
| terraform/guardian-coverage-cloud/provider_004.tfvars | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 004. | yes | no | no | yes | yes | no |
| terraform/guardian-coverage-cloud/provider_009.tfvars | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 009. | yes | yes | no | yes | yes | no |
| terraform/guardian-coverage-cloud/provider_014.tfvars | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 014. | yes | no | no | yes | yes | no |
| terraform/guardian-coverage-cloud/provider_019.tfvars | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 019. | yes | no | no | yes | yes | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 262 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2802 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1211 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 228 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `integrations/guardian-coverage-cloud/runtime/provider_001.env`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.bittrex-access-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/config/provider_002.yaml`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.bittrex-secret-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-cloud/provider_003.properties`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.cisco-meraki-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-cloud/provider_004.tfvars`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.clickhouse-cloud-api-secret-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-cloud/secrets/provider_005.txt`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.clojars-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/runtime/provider_006.env`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.cloudflare-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/config/provider_007.yaml`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.cloudflare-global-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-cloud/provider_008.properties`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.codecov-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-cloud/provider_009.tfvars`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.cohere-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-cloud/secrets/provider_010.txt`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.coinbase-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/runtime/provider_011.env`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.confluent-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/config/provider_012.yaml`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.confluent-secret-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-cloud/provider_013.properties`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.contentful-delivery-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-cloud/provider_014.tfvars`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.databricks-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-cloud/secrets/provider_015.txt`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.datadog-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/runtime/provider_016.env`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.defined-networking-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-cloud/config/provider_017.yaml`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.digitalocean-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-cloud/provider_018.properties`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.digitalocean-pat`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-cloud/provider_019.tfvars`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.digitalocean-refresh-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-cloud/secrets/provider_020.txt`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.discord-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `integrations/guardian-coverage-cloud/config/provider_002.yaml`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `integrations/guardian-coverage-cloud/runtime/provider_001.env`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `integrations/guardian-coverage-cloud/runtime/provider_016.env`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `terraform/guardian-coverage-cloud/provider_009.tfvars`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| docs/coverage-notes.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # guardian-coverage-cloud
0002: 
0003: Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `deploy/guardian-coverage-cloud/provider_003.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.cisco-meraki-api-key
0003: HFREn.H85xUjR1Uw-G2r.G4taSjsYYMERAKIc0dqmZb3oK_6p,
```

### `deploy/guardian-coverage-cloud/provider_008.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.codecov-access-token
0003: BGbC-y2FSIx0Bo-lZXJtfZ_eTEvLe8hPWyVayLcodecovhFLYr0=> `n1v7k2t7pp5vm8oruujx5p4n6jr2xpwx
```

### `deploy/guardian-coverage-cloud/provider_013.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.contentful-delivery-api-token
0003: Tc5UALnBM17Kxk-0VLdjUp4.zn7VXtCGd4sekAD6fjb983tBTncontentfulArSk:::=
```

### `deploy/guardian-coverage-cloud/provider_018.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.digitalocean-pat
0003: dop_v1_54ef0e180513e6b648eda42593159096e7d919f105864f4126f585d5e4b3f257
```

### `integrations/guardian-coverage-cloud/config/provider_002.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.bittrex-secret-key
0003: gOpibtkuaOQrfU-SgCTQaJQElLcNrbIkQfivjBgbLHArYhSbittrex rcbRxaJ'
```

### `integrations/guardian-coverage-cloud/config/provider_007.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.cloudflare-global-api-key
0003: dgih9Xcloudflare6a"=
```

### `integrations/guardian-coverage-cloud/config/provider_012.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.confluent-secret-key
0003: w6g3JB1H-ndcFtZconfluentN6BActmR74aEFOAZ-
```

### `integrations/guardian-coverage-cloud/config/provider_017.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.digitalocean-access-token
0003: doo_v1_c28fbbf56b414374270d1feda7b282e6efd0e8a82a65be4feac45eb66e903b92
```

### `integrations/guardian-coverage-cloud/runtime/provider_001.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.bittrex-access-key
0003: rtjeM_r6a09PQoeHobittrexD	W?=v2g96ju6kp59prv9e2b4modynmv5rmif
```

### `integrations/guardian-coverage-cloud/runtime/provider_006.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.cloudflare-api-key
0003: hNG-1sVCfy9aRmhKAuekG0n5ZUrcloudflareeaL7Y4	fMVRTRtqEJGv"||`==`
```

### `integrations/guardian-coverage-cloud/runtime/provider_011.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.confluent-access-token
0003: dMm1i8itZC4wY03C_jPK_01iLuzmW2aRyconfluentd_UNvUVf9SORnMqS6yJH>
```

### `integrations/guardian-coverage-cloud/runtime/provider_016.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.defined-networking-api-token
0003: SDfWTKLuHifxCg.D0dnkeyl::= dnkey-bq=7l6ox2t8d-wzchgtuafcmsd-fysqos1_yrq1c55-4047mpk0d7nbf455blay__4q2mhq14ro1w2t
```

### `ops/guardian-coverage-cloud/secrets/provider_005.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.clojars-api-token
0003: CLOJARS_ssk61ow5q4bzsdopyfmt8ktdbk9m31vfz7cccrjm0nprdm32em31wpbbnot9
```

### `ops/guardian-coverage-cloud/secrets/provider_010.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.coinbase-access-token
0003: aGcoinbaseV4Y7SRG0o		
```

### `ops/guardian-coverage-cloud/secrets/provider_015.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.datadog-access-token
0003: oOYwI7hqCEkiiuaS7L1Gb.Cwnae9jlFmqE1YdatadogpFi2j
```

### `ops/guardian-coverage-cloud/secrets/provider_020.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.discord-api-token
0003: oYiLdEhrwKCQEYilJzpX3PJI6SUeGvaHi4i.lCtwii.discord-TXxBtZf=	"= 354db97e400ea84a6590fdf39b1335aab158c0d9054983b18adab410dd107142
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `terraform/guardian-coverage-cloud/provider_004.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.clickhouse-cloud-api-secret-key
0003: 4b1dOxsUzsifctdLGRrLtfmPYZ6qsBPbZ3l4pPKQzc
```

### `terraform/guardian-coverage-cloud/provider_009.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.cohere-api-token
0003: XTY-hXcUpWElgi697okG4CO_API_KEY	Yfl
```

### `terraform/guardian-coverage-cloud/provider_014.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.databricks-api-token
0003: dapi9a3d095d0e1403d82a47f10354b2aa22-5
```

### `terraform/guardian-coverage-cloud/provider_019.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.digitalocean-refresh-token
0003: dor_v1_f51fa1c552f8ca534c1c168a77a7ee50e175edd9b5c5f4d0c51267601d269b63
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `6178`
- Synthetic filler / inflation LOC: `5720`
- Synthetic filler ratio: `92.59%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 77 |
| tests | 3 |
| docs | 33 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 335 |
| synthetic filler / inflation content | 5720 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `integrations/guardian-coverage-cloud/runtime/provider_001.env`
  module: `Guardian`
  expected rule/finding family: `guardian.bittrex-access-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/config/provider_002.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.bittrex-secret-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-cloud/provider_003.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.cisco-meraki-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-cloud/provider_004.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.clickhouse-cloud-api-secret-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-cloud/secrets/provider_005.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.clojars-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/runtime/provider_006.env`
  module: `Guardian`
  expected rule/finding family: `guardian.cloudflare-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/config/provider_007.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.cloudflare-global-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-cloud/provider_008.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.codecov-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-cloud/provider_009.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.cohere-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-cloud/secrets/provider_010.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.coinbase-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/runtime/provider_011.env`
  module: `Guardian`
  expected rule/finding family: `guardian.confluent-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/config/provider_012.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.confluent-secret-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-cloud/provider_013.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.contentful-delivery-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-cloud/provider_014.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.databricks-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-cloud/secrets/provider_015.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.datadog-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/runtime/provider_016.env`
  module: `Guardian`
  expected rule/finding family: `guardian.defined-networking-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-cloud/config/provider_017.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.digitalocean-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-cloud/provider_018.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.digitalocean-pat`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-cloud/provider_019.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.digitalocean-refresh-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-cloud/secrets/provider_020.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.discord-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.

### must_not_find

- None.

### may_find_review

- None in the current run.

## 14. Explainability Expectations

Guardian-only scenario. Quantum explainability contract is not applicable here.

## 15. FP/FN Risk Notes

- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.
- Current run already demonstrated this risk: verdict=`PASS_WITH_NOISE`.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `1/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Guardian provider coverage bundle exercising 20 distinct secret families.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
