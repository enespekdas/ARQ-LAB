# Generated Project Dossier - G-V1-COV-103

## 1. Scenario Identity

- scenarioId: `G-V1-COV-103`
- scenarioName: Guardian provider coverage bundle exercising 20 distinct secret families.
- milestone: `M1`
- targetModule: `Guardian`
- language / stack: `Config / IaC / CI credential coverage bundle`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/guardian-coverage-automation`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\G-V1-COV-103\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V1-COV-103.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Automation and CI credential corpus covering pipeline tokens, bot credentials, and service access keys.` as a `Config / IaC / CI credential coverage bundle` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Guardian provider coverage bundle exercising 20 distinct secret families.`.

## 3. Architecture Summary

- Major components: `.github, config, deploy, docs, integrations, ops, scripts, sql, terraform, tests, validation, vendor`
- Runtime role: `Automation and CI credential corpus covering pipeline tokens, bot credentials, and service access keys.`
- Config flow: `.github/workflows/deploy.yml, config/runtime/baseline.yaml, deploy/guardian-coverage-automation/provider_003.properties, deploy/guardian-coverage-automation/provider_008.properties, deploy/guardian-coverage-automation/provider_013.properties, deploy/guardian-coverage-automation/provider_018.properties, deploy/prod/service.properties, integrations/guardian-coverage-automation/config/provider_002.yaml, integrations/guardian-coverage-automation/config/provider_007.yaml, integrations/guardian-coverage-automation/config/provider_012.yaml, integrations/guardian-coverage-automation/config/provider_017.yaml, integrations/guardian-coverage-automation/runtime/provider_001.env`
- Secret flow: `deploy/guardian-coverage-automation/provider_003.properties, deploy/guardian-coverage-automation/provider_008.properties, deploy/guardian-coverage-automation/provider_013.properties, deploy/guardian-coverage-automation/provider_018.properties, integrations/guardian-coverage-automation/config/provider_002.yaml, integrations/guardian-coverage-automation/config/provider_007.yaml, integrations/guardian-coverage-automation/config/provider_012.yaml, integrations/guardian-coverage-automation/config/provider_017.yaml, integrations/guardian-coverage-automation/runtime/provider_001.env, integrations/guardian-coverage-automation/runtime/provider_006.env, integrations/guardian-coverage-automation/runtime/provider_011.env, integrations/guardian-coverage-automation/runtime/provider_016.env, ops/guardian-coverage-automation/secrets/provider_005.txt, ops/guardian-coverage-automation/secrets/provider_010.txt, ops/guardian-coverage-automation/secrets/provider_015.txt, ops/guardian-coverage-automation/secrets/provider_020.txt, terraform/guardian-coverage-automation/provider_004.tfvars, terraform/guardian-coverage-automation/provider_009.tfvars, terraform/guardian-coverage-automation/provider_014.tfvars, terraform/guardian-coverage-automation/provider_019.tfvars`
- Crypto/TLS flow if relevant: `Not a Quantum-positive scenario.`
- Test surfaces: `tests/fixtures/sample-placeholder.txt, tests/test_validation.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
guardian-coverage-automation
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- config
|   `-- runtime
|       `-- baseline.yaml
|-- deploy
|   |-- guardian-coverage-automation
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
|   `-- guardian-coverage-automation
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
|   |-- guardian-coverage-automation
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
|   `-- guardian-coverage-automation
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
| deploy/guardian-coverage-automation/provider_003.properties | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 003. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-automation/provider_008.properties | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 008. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-automation/provider_013.properties | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 013. | yes | no | no | yes | yes | no |
| deploy/guardian-coverage-automation/provider_018.properties | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 018. | yes | no | no | yes | yes | no |
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
| integrations/guardian-coverage-automation/config/provider_002.yaml | live-config | 4 | Runtime configuration carrying environment or deployment settings for Provider 002. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/config/provider_007.yaml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 007. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/config/provider_012.yaml | live-config | 4 | Runtime configuration carrying environment or deployment settings for Provider 012. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/config/provider_017.yaml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 017. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/runtime/provider_001.env | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 001. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/runtime/provider_006.env | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 006. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/runtime/provider_011.env | live-config | 5 | Runtime configuration carrying environment or deployment settings for Provider 011. | yes | no | no | yes | yes | no |
| integrations/guardian-coverage-automation/runtime/provider_016.env | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 016. | yes | no | no | yes | yes | no |
| ops/guardian-coverage-automation/secrets/provider_005.txt | docs | 3 | Documentation or explanatory material for Provider 005. | yes | no | no | no | no | no |
| ops/guardian-coverage-automation/secrets/provider_010.txt | docs | 4 | Documentation or explanatory material for Provider 010. | yes | no | no | no | no | no |
| ops/guardian-coverage-automation/secrets/provider_015.txt | docs | 96 | Documentation or explanatory material for Provider 015. | yes | no | no | no | no | no |
| ops/guardian-coverage-automation/secrets/provider_020.txt | docs | 3 | Documentation or explanatory material for Provider 020. | yes | no | no | no | no | no |
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
| terraform/guardian-coverage-automation/provider_004.tfvars | live-config | 6 | Runtime configuration carrying environment or deployment settings for Provider 004. | yes | no | no | yes | yes | no |
| terraform/guardian-coverage-automation/provider_009.tfvars | live-config | 4 | Runtime configuration carrying environment or deployment settings for Provider 009. | yes | no | no | yes | yes | no |
| terraform/guardian-coverage-automation/provider_014.tfvars | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 014. | yes | no | no | yes | yes | no |
| terraform/guardian-coverage-automation/provider_019.tfvars | live-config | 3 | Runtime configuration carrying environment or deployment settings for Provider 019. | yes | no | no | yes | yes | no |
| tests/fixtures/sample-placeholder.txt | test | 1 | Automated test surface covering Sample Placeholder behavior. | no | no | yes | no | yes | no |
| tests/test_validation.py | test | 2 | Automated test surface covering Test Validation behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 1 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 262 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2802 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1201 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 228 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 10 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/generated-client.txt | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Generated Client. | no | no | yes | no | no | no |

## 6. Positive Surfaces

- Path: `integrations/guardian-coverage-automation/runtime/provider_001.env`
  Why it should be detected: scenario declares `rule-001` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.discord-client-id`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/config/provider_002.yaml`
  Why it should be detected: scenario declares `rule-002` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.discord-client-secret`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-automation/provider_003.properties`
  Why it should be detected: scenario declares `rule-003` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.droneci-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-automation/provider_004.tfvars`
  Why it should be detected: scenario declares `rule-004` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.dropbox-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-automation/secrets/provider_005.txt`
  Why it should be detected: scenario declares `rule-005` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.dropbox-long-lived-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/runtime/provider_006.env`
  Why it should be detected: scenario declares `rule-006` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.etsy-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/config/provider_007.yaml`
  Why it should be detected: scenario declares `rule-007` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.facebook-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-automation/provider_008.properties`
  Why it should be detected: scenario declares `rule-008` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.facebook-secret`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-automation/provider_009.tfvars`
  Why it should be detected: scenario declares `rule-009` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.fastly-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-automation/secrets/provider_010.txt`
  Why it should be detected: scenario declares `rule-010` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.finicity-api-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/runtime/provider_011.env`
  Why it should be detected: scenario declares `rule-011` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.finicity-client-secret`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/config/provider_012.yaml`
  Why it should be detected: scenario declares `rule-012` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.finnhub-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-automation/provider_013.properties`
  Why it should be detected: scenario declares `rule-013` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.flickr-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-automation/provider_014.tfvars`
  Why it should be detected: scenario declares `rule-014` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.flyio-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-automation/secrets/provider_015.txt`
  Why it should be detected: scenario declares `rule-015` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.freemius-secret-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/runtime/provider_016.env`
  Why it should be detected: scenario declares `rule-016` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.freshbooks-access-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `integrations/guardian-coverage-automation/config/provider_017.yaml`
  Why it should be detected: scenario declares `rule-017` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.gcp-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/guardian-coverage-automation/provider_018.properties`
  Why it should be detected: scenario declares `rule-018` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.github-app-token`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `terraform/guardian-coverage-automation/provider_019.tfvars`
  Why it should be detected: scenario declares `rule-019` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.github-fine-grained-pat`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `ops/guardian-coverage-automation/secrets/provider_020.txt`
  Why it should be detected: scenario declares `rule-020` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.github-oauth`
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
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: 
0003: Automation and CI credential corpus covering pipeline tokens, bot credentials, and service access keys.
0004: 
```

### `deploy/guardian-coverage-automation/provider_003.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 003. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.droneci-access-token
0003: YZ01mRg0Dc68GM_Ph-hsBPdNM24R1droneciY6WSltw
```

### `deploy/guardian-coverage-automation/provider_008.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 008. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.facebook-secret
0003: XFb73hBh6-wQqk0dNfacebookb "
```

### `deploy/guardian-coverage-automation/provider_013.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 013. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.flickr-access-token
0003: q.4CG0gXp4E0.pVBp65efs.1PP8_eQuiDxwNHN0flickrBYDhebQGPDV1Qi. 6
```

### `deploy/guardian-coverage-automation/provider_018.properties`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 018. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.github-app-token
0003: ghu_MkPNEXElCznDGsLquhnWQFUck4dDdXnl4xx7
```

### `integrations/guardian-coverage-automation/config/provider_002.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 002. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.discord-client-secret
0003: ZZdn7AF5zzmBGSLqzCDCzY-7BdS-1r.YiAyjkqdiscordK:=
```

### `integrations/guardian-coverage-automation/config/provider_007.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 007. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.facebook-access-token
0003: 088716287224535%e_-h19nfand6ggatfpu5o84f983wcdc5tp6i9"
```

### `integrations/guardian-coverage-automation/config/provider_012.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 012. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.finnhub-access-token
0003: .sbcnem9JLX038wAaBzIu.pnOJtwRCtsfinnhubdApxCuiVE3z
```

### `integrations/guardian-coverage-automation/config/provider_017.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 017. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.gcp-api-key
0003: AIzabZeRLn5pZE9w5WL1pbliM4RI94v_Di5EYF6;
```

### `integrations/guardian-coverage-automation/runtime/provider_001.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 001. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.discord-client-id
0003: ZGR_eO-RWkxGFhWdiscord	
```

### `integrations/guardian-coverage-automation/runtime/provider_006.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 006. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.etsy-access-token
0003: HUs9_LPbVu5Suo.9Pn.YpETSYLnVh
```

### `integrations/guardian-coverage-automation/runtime/provider_011.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 011. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.finicity-client-secret
0003: UWhJMBKNZ5Fmfinicityz4Yc"	||"
```

### `integrations/guardian-coverage-automation/runtime/provider_016.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 016. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.freshbooks-access-token
0003: IWfreshbooks1p
```

### `ops/guardian-coverage-automation/secrets/provider_005.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 005. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.dropbox-long-lived-api-token
0003: 0M9Or8SWkb23POK2nKb.dropbox9mVfURgl4PFlF"",''x634fu31z8oAAAAAAAAAAs8_qtw6mm2m7rcg=z2o1aw0eb=p85fjjkrjx5tqer8d
```

### `ops/guardian-coverage-automation/secrets/provider_010.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 010. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.finicity-api-token
0003: sY-NbCeIJT_CvkfTqZt.qfinicity4nSDvkH4wVemnBROBD
```

### `ops/guardian-coverage-automation/secrets/provider_015.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 015. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.freemius-secret-key
0003: 'secret_key' 
0004: 
```

### `ops/guardian-coverage-automation/secrets/provider_020.txt`

- Why this file matters: `docs` file with expectation `must_find`.
- Detailed summary: Documentation or explanatory material for Provider 020. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.github-oauth
0003: gho_oa1qHFZ0rkXs13CmguARTSBKZGivxtDes3xK
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'config smoke ok'
```

### `terraform/guardian-coverage-automation/provider_004.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 004. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.dropbox-api-token
0003: vCi03agd7w.49uB8lZJ3XVQMXMkD.psxAwu6xB0.eXTYdropboxOLf
```

### `terraform/guardian-coverage-automation/provider_009.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 009. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.fastly-api-token
0003: 7UjV9eJgyGEVoeVQ1NzzOpCKai0fy5Hgfastly8b	hV.9ib7Its,'
```

### `terraform/guardian-coverage-automation/provider_014.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 014. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.flyio-access-token
0003: fo1_Im-93E6Nenxa4MFVUJ_DugM5mC44ugfz4jmlMr2oK_j\r
```

### `terraform/guardian-coverage-automation/provider_019.tfvars`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Provider 019. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # coverage campaign entry
0002: # rule_key: guardian.github-fine-grained-pat
0003: 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
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `6272`
- Synthetic filler / inflation LOC: `5720`
- Synthetic filler ratio: `91.20%`

| category | LOC |
| --- | ---: |
| live business code | 0 |
| live config | 82 |
| tests | 3 |
| docs | 122 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 335 |
| synthetic filler / inflation content | 5720 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `integrations/guardian-coverage-automation/runtime/provider_001.env`
  module: `Guardian`
  expected rule/finding family: `guardian.discord-client-id`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/config/provider_002.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.discord-client-secret`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-automation/provider_003.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.droneci-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-automation/provider_004.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.dropbox-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-automation/secrets/provider_005.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.dropbox-long-lived-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/runtime/provider_006.env`
  module: `Guardian`
  expected rule/finding family: `guardian.etsy-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/config/provider_007.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.facebook-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-automation/provider_008.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.facebook-secret`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-automation/provider_009.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.fastly-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-automation/secrets/provider_010.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.finicity-api-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/runtime/provider_011.env`
  module: `Guardian`
  expected rule/finding family: `guardian.finicity-client-secret`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/config/provider_012.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.finnhub-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-automation/provider_013.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.flickr-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-automation/provider_014.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.flyio-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-automation/secrets/provider_015.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.freemius-secret-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/runtime/provider_016.env`
  module: `Guardian`
  expected rule/finding family: `guardian.freshbooks-access-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `integrations/guardian-coverage-automation/config/provider_017.yaml`
  module: `Guardian`
  expected rule/finding family: `guardian.gcp-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/guardian-coverage-automation/provider_018.properties`
  module: `Guardian`
  expected rule/finding family: `guardian.github-app-token`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `terraform/guardian-coverage-automation/provider_019.tfvars`
  module: `Guardian`
  expected rule/finding family: `guardian.github-fine-grained-pat`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `ops/guardian-coverage-automation/secrets/provider_020.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.github-oauth`
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
- Current run already demonstrated this risk: verdict=`FAIL_FN`.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `1/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Guardian provider coverage bundle exercising 20 distinct secret families.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-automation\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
