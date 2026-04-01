# Generated Project Dossier - M-V8-004

## 1. Scenario Identity

- scenarioId: `M-V8-004`
- scenarioName: Infra-heavy mixed repo with active insecure runtime config, branch divergence, and numerous protected-negative surfaces.
- milestone: `M8`
- targetModule: `Both`
- language / stack: `App + infra + helm + kustomize + terraform + CI`
- repoType: `mixed`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/control-plane-infra-repo`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT, REF_HISTORY`
- branch scopes intended for this scenario: `ALL_BRANCHES, SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-004\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-004.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Control-plane repo with live infra config, hotfix branches, CI workflows, and example overlays.` as a `App + infra + helm + kustomize + terraform + CI` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Infra-heavy mixed repo with active insecure runtime config, branch divergence, and numerous protected-negative surfaces.`.

## 3. Architecture Summary

- Major components: `.github, app, deploy, docs, helm, kustomize, ops, scripts, sql, terraform, tests, validation`
- Runtime role: `Control-plane repo with live infra config, hotfix branches, CI workflows, and example overlays.`
- Config flow: `.github/workflows/deploy.yml, app/config/production.env, deploy/envoy.yaml, helm/control-plane/values.yaml, terraform/modules/edge/variables.tf`
- Secret flow: `feature-secret.txt, production.env`
- Crypto/TLS flow if relevant: `deploy/envoy.yaml, legacyDigest.ts`
- Test surfaces: `tests/test_audit_service.py, tests/test_delivery_service.py, tests/test_dispatch_service.py, tests/test_metrics_service.py, tests/test_preferences_service.py, tests/test_retry_service.py, tests/test_routing_service.py, tests/test_templates_service.py`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
control-plane-infra-repo
|-- .github
|   `-- workflows
|       `-- deploy.yml
|-- app
|   |-- config
|   |   `-- production.env
|   |-- models
|   |   |-- audit.py
|   |   |-- delivery.py
|   |   |-- dispatch.py
|   |   |-- metrics.py
|   |   |-- preferences.py
|   |   |-- retry.py
|   |   |-- routing.py
|   |   `-- templates.py
|   |-- services
|   |   |-- audit_service.py
|   |   |-- delivery_service.py
|   |   |-- dispatch_service.py
|   |   |-- metrics_service.py
|   |   |-- preferences_service.py
|   |   |-- retry_service.py
|   |   |-- routing_service.py
|   |   `-- templates_service.py
|   |-- __init__.py
|   `-- main.py
|-- deploy
|   |-- examples
|   |   `-- envoy.yaml
|   `-- envoy.yaml
|-- docs
|   `-- architecture
|       |-- section-01.md
|       |-- section-02.md
|       |-- section-03.md
|       |-- section-04.md
|       |-- section-05.md
|       |-- section-06.md
|       |-- section-07.md
|       |-- section-08.md
|       |-- section-09.md
|       |-- section-10.md
|       |-- section-11.md
|       |-- section-12.md
|       |-- section-13.md
|       |-- section-14.md
|       |-- section-15.md
|       |-- section-16.md
|       |-- section-17.md
|       |-- section-18.md
|       |-- section-19.md
|       |-- section-20.md
|       |-- section-21.md
|       |-- section-22.md
|       |-- section-23.md
|       |-- section-24.md
|       |-- section-25.md
|       |-- section-26.md
|       |-- section-27.md
|       |-- section-28.md
|       |-- section-29.md
|       |-- section-30.md
|       |-- section-31.md
|       |-- section-32.md
|       |-- section-33.md
|       |-- section-34.md
|       |-- section-35.md
|       |-- section-36.md
|       |-- section-37.md
|       |-- section-38.md
|       |-- section-39.md
|       |-- section-40.md
|       |-- section-41.md
|       |-- section-42.md
|       |-- section-43.md
|       |-- section-44.md
|       |-- section-45.md
|       |-- section-46.md
|       |-- section-47.md
|       |-- section-48.md
|       |-- section-49.md
|       |-- section-50.md
|       |-- section-51.md
|       |-- section-52.md
|       |-- section-53.md
|       |-- section-54.md
|       |-- section-55.md
|       |-- section-56.md
|       |-- section-57.md
|       |-- section-58.md
|       |-- section-59.md
|       |-- section-60.md
|       |-- section-61.md
|       |-- section-62.md
|       |-- section-63.md
|       |-- section-64.md
|       |-- section-65.md
|       |-- section-66.md
|       |-- section-67.md
|       |-- section-68.md
|       |-- section-69.md
|       |-- section-70.md
|       |-- section-71.md
|       |-- section-72.md
|       |-- section-73.md
|       |-- section-74.md
|       |-- section-75.md
|       |-- section-76.md
|       |-- section-77.md
|       `-- section-78.md
|-- helm
|   `-- control-plane
|       `-- values.yaml
|-- kustomize
|   `-- fixtures
|       `-- dev.env
|-- ops
|   |-- console
|   |   |-- __tests__
|   |   |   |-- audit.service.test.ts
|   |   |   |-- compliance.service.test.ts
|   |   |   |-- events.service.test.ts
|   |   |   |-- invites.service.test.ts
|   |   |   |-- partners.service.test.ts
|   |   |   |-- profiles.service.test.ts
|   |   |   |-- sessions.service.test.ts
|   |   |   `-- tokens.service.test.ts
|   |   |-- dist
|   |   |   |-- __tests__
|   |   |   |   |-- audit.service.test.js
|   |   |   |   |-- compliance.service.test.js
|   |   |   |   |-- events.service.test.js
|   |   |   |   |-- invites.service.test.js
|   |   |   |   |-- partners.service.test.js
|   |   |   |   |-- profiles.service.test.js
|   |   |   |   |-- sessions.service.test.js
|   |   |   |   `-- tokens.service.test.js
|   |   |   |-- scripts
|   |   |   |   `-- smoke.js
|   |   |   `-- src
|   |   |       |-- modules
|   |   |       |   |-- audit
|   |   |       |   |   `-- audit.service.js
|   |   |       |   |-- compliance
|   |   |       |   |   `-- compliance.service.js
|   |   |       |   |-- events
|   |   |       |   |   `-- events.service.js
|   |   |       |   |-- invites
|   |   |       |   |   `-- invites.service.js
|   |   |       |   |-- partners
|   |   |       |   |   `-- partners.service.js
|   |   |       |   |-- profiles
|   |   |       |   |   `-- profiles.service.js
|   |   |       |   |-- security
|   |   |       |   |   `-- legacyDigest.js
|   |   |       |   |-- sessions
|   |   |       |   |   `-- sessions.service.js
|   |   |       |   `-- tokens
|   |   |       |       `-- tokens.service.js
|   |   |       `-- server.js
|   |   |-- scripts
|   |   |   `-- smoke.ts
|   |   |-- src
|   |   |   |-- modules
|   |   |   |   |-- audit
|   |   |   |   |   `-- audit.service.ts
|   |   |   |   |-- compliance
|   |   |   |   |   `-- compliance.service.ts
|   |   |   |   |-- events
|   |   |   |   |   `-- events.service.ts
|   |   |   |   |-- invites
|   |   |   |   |   `-- invites.service.ts
|   |   |   |   |-- partners
|   |   |   |   |   `-- partners.service.ts
|   |   |   |   |-- profiles
|   |   |   |   |   `-- profiles.service.ts
|   |   |   |   |-- security
|   |   |   |   |   `-- legacyDigest.ts
|   |   |   |   |-- sessions
|   |   |   |   |   `-- sessions.service.ts
|   |   |   |   `-- tokens
|   |   |   |       `-- tokens.service.ts
|   |   |   `-- server.ts
|   |   |-- .gitignore
|   |   |-- jest.config.cjs
|   |   |-- package-lock.json
|   |   |-- package.json
|   |   |-- README.md
|   |   `-- tsconfig.json
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
|       |-- runbook-61.md
|       |-- runbook-62.md
|       |-- runbook-63.md
|       |-- runbook-64.md
|       |-- runbook-65.md
|       |-- runbook-66.md
|       |-- runbook-67.md
|       |-- runbook-68.md
|       |-- runbook-69.md
|       |-- runbook-70.md
|       |-- runbook-71.md
|       |-- runbook-72.md
|       |-- runbook-73.md
|       |-- runbook-74.md
|       |-- runbook-75.md
|       |-- runbook-76.md
|       |-- runbook-77.md
|       `-- runbook-78.md
|-- scripts
|   |-- smoke.ps1
|   `-- smoke.py
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
|       |-- reference-61.sql
|       |-- reference-62.sql
|       |-- reference-63.sql
|       |-- reference-64.sql
|       |-- reference-65.sql
|       |-- reference-66.sql
|       |-- reference-67.sql
|       |-- reference-68.sql
|       |-- reference-69.sql
|       |-- reference-70.sql
|       |-- reference-71.sql
|       |-- reference-72.sql
|       |-- reference-73.sql
|       |-- reference-74.sql
|       |-- reference-75.sql
|       |-- reference-76.sql
|       |-- reference-77.sql
|       `-- reference-78.sql
|-- terraform
|   `-- modules
|       `-- edge
|           `-- variables.tf
|-- tests
|   |-- test_audit_service.py
|   |-- test_delivery_service.py
|   |-- test_dispatch_service.py
|   |-- test_metrics_service.py
|   |-- test_preferences_service.py
|   |-- test_retry_service.py
|   |-- test_routing_service.py
|   `-- test_templates_service.py
|-- validation
|   |-- runnability-logs
|   |   |-- build-01.log
|   |   |-- build-02.log
|   |   |-- build-03.log
|   |   |-- smoke-01.log
|   |   |-- test-01.log
|   |   `-- test-02.log
|   |-- branch-plan.yaml
|   |-- expected-absent.json
|   |-- expected-findings.json
|   |-- expected-report.md
|   |-- explainability-contract.json
|   |-- generated-file-manifest.json
|   |-- generated-project-dossier.md
|   |-- generated-tree.txt
|   |-- repo-metadata.json
|   |-- scenario.yaml
|   `-- smoke.yaml
|-- .gitignore
|-- pyproject.toml
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .github/workflows/deploy.yml | live-config | 7 | Runtime configuration carrying environment or deployment settings for Deploy. | no | no | no | yes | no | no |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | no | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| app/__init__.py | live-code | 0 | Runtime business module contributing to Init. | no | no | no | yes | no | no |
| app/config/production.env | live-config | 1 | Runtime configuration carrying environment or deployment settings for Production. | yes | no | no | yes | no | no |
| app/main.py | live-code | 5 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | no | yes |
| app/models/audit.py | live-code | 6 | Runtime business module contributing to Audit. | no | no | no | yes | no | no |
| app/models/delivery.py | live-code | 6 | Runtime business module contributing to Delivery. | no | no | no | yes | no | no |
| app/models/dispatch.py | live-code | 6 | Runtime business module contributing to Dispatch. | no | no | no | yes | no | no |
| app/models/metrics.py | live-code | 6 | Runtime business module contributing to Metrics. | no | no | no | yes | no | no |
| app/models/preferences.py | live-code | 6 | Runtime business module contributing to Preferences. | no | no | no | yes | no | no |
| app/models/retry.py | live-code | 6 | Runtime business module contributing to Retry. | no | no | no | yes | no | no |
| app/models/routing.py | live-code | 6 | Runtime business module contributing to Routing. | no | no | no | yes | no | no |
| app/models/templates.py | live-code | 6 | Runtime business module contributing to Templates. | no | no | no | yes | no | no |
| app/services/audit_service.py | live-code | 4 | Runtime business service implementing Audit Service logic. | no | no | no | yes | no | no |
| app/services/delivery_service.py | live-code | 4 | Runtime business service implementing Delivery Service logic. | no | no | no | yes | no | no |
| app/services/dispatch_service.py | live-code | 4 | Runtime business service implementing Dispatch Service logic. | no | no | no | yes | no | no |
| app/services/metrics_service.py | live-code | 4 | Runtime business service implementing Metrics Service logic. | no | no | no | yes | no | no |
| app/services/preferences_service.py | live-code | 4 | Runtime business service implementing Preferences Service logic. | no | no | no | yes | no | no |
| app/services/retry_service.py | live-code | 4 | Runtime business service implementing Retry Service logic. | no | no | no | yes | no | no |
| app/services/routing_service.py | live-code | 4 | Runtime business service implementing Routing Service logic. | no | no | no | yes | no | no |
| app/services/templates_service.py | live-code | 4 | Runtime business service implementing Templates Service logic. | no | no | no | yes | no | no |
| deploy/envoy.yaml | live-config | 2 | Runtime configuration carrying environment or deployment settings for Envoy. | yes | no | no | yes | no | no |
| deploy/examples/envoy.yaml | build/deploy | 1 | Build or deployment definition shaping how Envoy is compiled, packaged, or released. | no | yes | no | yes | no | no |
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
| docs/architecture/section-62.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-63.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-64.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-65.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-66.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-67.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-68.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-69.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-70.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-71.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-72.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-73.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-74.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-75.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-76.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-77.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-78.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| helm/control-plane/values.yaml | live-config | 2 | Runtime configuration carrying environment or deployment settings for Values. | no | no | no | yes | no | no |
| kustomize/fixtures/dev.env | generated | 1 | Generated or derived project artifact related to Dev. | no | no | yes | no | no | no |
| ops/console/.gitignore | generated | 8 | Generated or derived project artifact related to .Gitignore. | no | no | yes | yes | yes | no |
| ops/console/README.md | docs | 11 | Documentation or explanatory material for Readme. | no | no | no | yes | yes | no |
| ops/console/__tests__/audit.service.test.ts | live-code | 2 | Runtime business service implementing Audit.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/compliance.service.test.ts | live-code | 2 | Runtime business service implementing Compliance.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/events.service.test.ts | live-code | 2 | Runtime business service implementing Events.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/invites.service.test.ts | live-code | 2 | Runtime business service implementing Invites.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/partners.service.test.ts | live-code | 2 | Runtime business service implementing Partners.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/profiles.service.test.ts | live-code | 2 | Runtime business service implementing Profiles.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/sessions.service.test.ts | live-code | 2 | Runtime business service implementing Sessions.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/__tests__/tokens.service.test.ts | live-code | 2 | Runtime business service implementing Tokens.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/audit.service.test.js | live-code | 4 | Runtime business service implementing Audit.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/compliance.service.test.js | live-code | 4 | Runtime business service implementing Compliance.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/events.service.test.js | live-code | 4 | Runtime business service implementing Events.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/invites.service.test.js | live-code | 4 | Runtime business service implementing Invites.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/partners.service.test.js | live-code | 4 | Runtime business service implementing Partners.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/profiles.service.test.js | live-code | 4 | Runtime business service implementing Profiles.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/sessions.service.test.js | live-code | 4 | Runtime business service implementing Sessions.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/__tests__/tokens.service.test.js | live-code | 4 | Runtime business service implementing Tokens.Service.Test logic. | no | no | no | yes | yes | no |
| ops/console/dist/scripts/smoke.js | live-code | 2 | Runtime business module contributing to Smoke. | no | no | no | yes | yes | yes |
| ops/console/dist/src/modules/audit/audit.service.js | live-code | 4 | Runtime business service implementing Audit.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/compliance/compliance.service.js | live-code | 4 | Runtime business service implementing Compliance.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/events/events.service.js | live-code | 4 | Runtime business service implementing Events.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/invites/invites.service.js | live-code | 4 | Runtime business service implementing Invites.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/partners/partners.service.js | live-code | 4 | Runtime business service implementing Partners.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/profiles/profiles.service.js | live-code | 4 | Runtime business service implementing Profiles.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/security/legacyDigest.js | live-code | 5 | Runtime business module contributing to Legacy Digest. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/sessions/sessions.service.js | live-code | 4 | Runtime business service implementing Sessions.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/modules/tokens/tokens.service.js | live-code | 4 | Runtime business service implementing Tokens.Service logic. | no | no | no | yes | yes | no |
| ops/console/dist/src/server.js | live-code | 9 | Runtime business module contributing to Server. | no | no | no | yes | yes | no |
| ops/console/jest.config.cjs | generated | 1 | Generated or derived project artifact related to Jest.Config. | no | no | yes | yes | yes | no |
| ops/console/package-lock.json | build/deploy | 4770 | Build or deployment definition shaping how Package Lock is compiled, packaged, or released. | no | no | no | yes | yes | no |
| ops/console/package.json | generated | 8 | Generated or derived project artifact related to Package. | no | no | yes | yes | yes | no |
| ops/console/scripts/smoke.ts | live-code | 1 | Runtime business module contributing to Smoke. | no | no | no | yes | yes | yes |
| ops/console/src/modules/audit/audit.service.ts | live-code | 2 | Runtime business service implementing Audit.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/compliance/compliance.service.ts | live-code | 2 | Runtime business service implementing Compliance.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/events/events.service.ts | live-code | 2 | Runtime business service implementing Events.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/invites/invites.service.ts | live-code | 2 | Runtime business service implementing Invites.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/partners/partners.service.ts | live-code | 2 | Runtime business service implementing Partners.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/profiles/profiles.service.ts | live-code | 2 | Runtime business service implementing Profiles.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/security/legacyDigest.ts | live-code | 2 | Runtime business module contributing to Legacy Digest. | yes | no | no | yes | yes | no |
| ops/console/src/modules/sessions/sessions.service.ts | live-code | 2 | Runtime business service implementing Sessions.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/modules/tokens/tokens.service.ts | live-code | 2 | Runtime business service implementing Tokens.Service logic. | no | no | no | yes | yes | no |
| ops/console/src/server.ts | live-code | 4 | Runtime business module contributing to Server. | no | no | no | yes | yes | no |
| ops/console/tsconfig.json | build/deploy | 4 | Build or deployment definition shaping how Tsconfig is compiled, packaged, or released. | no | no | no | yes | yes | no |
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
| ops/playbooks/runbook-62.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-63.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-64.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-65.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-66.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-67.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-68.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-69.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-70.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-71.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-72.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-73.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-74.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-75.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-76.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-77.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-78.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| pyproject.toml | build/deploy | 7 | Build or deployment definition shaping how Pyproject is compiled, packaged, or released. | no | no | no | yes | no | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | no | yes |
| scripts/smoke.py | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | no | yes |
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
| sql/reference/reference-62.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-63.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-64.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-65.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-66.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-67.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-68.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-69.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-70.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-71.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-72.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-73.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-74.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-75.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-76.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-77.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-78.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| terraform/modules/edge/variables.tf | live-config | 1 | Runtime configuration carrying environment or deployment settings for Variables. | no | no | no | yes | no | no |
| tests/test_audit_service.py | test | 4 | Automated test surface covering Test Audit Service behavior. | no | no | yes | yes | yes | no |
| tests/test_delivery_service.py | test | 4 | Automated test surface covering Test Delivery Service behavior. | no | no | yes | yes | yes | no |
| tests/test_dispatch_service.py | test | 4 | Automated test surface covering Test Dispatch Service behavior. | no | no | yes | yes | yes | no |
| tests/test_metrics_service.py | test | 4 | Automated test surface covering Test Metrics Service behavior. | no | no | yes | yes | yes | no |
| tests/test_preferences_service.py | test | 4 | Automated test surface covering Test Preferences Service behavior. | no | no | yes | yes | yes | no |
| tests/test_retry_service.py | test | 4 | Automated test surface covering Test Retry Service behavior. | no | no | yes | yes | yes | no |
| tests/test_routing_service.py | test | 4 | Automated test surface covering Test Routing Service behavior. | no | no | yes | yes | yes | no |
| tests/test_templates_service.py | test | 4 | Automated test surface covering Test Templates Service behavior. | no | no | yes | yes | yes | no |
| validation/branch-plan.yaml | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 20 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 67 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/explainability-contract.json | generated | 26 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 4664 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1297 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 387 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 45 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 41 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-02.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-03.log | generated | 12 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/test-02.log | generated | 34 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |

## 6. Positive Surfaces

- Path: `app/config/production.env`
  Why it should be detected: scenario declares `guardian-active-secret` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `feature-secret.txt`
  Why it should be detected: scenario declares `guardian-hotfix-secret` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `deploy/envoy.yaml`
  Why it should be detected: scenario declares `quantum-config-trust` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `ACCEPT_UNTRUSTED`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~ACCEPT_UNTRUSTED; resolvedValue~tls_minimum_protocol_version=TLSv1_0
- Path: `deploy/envoy.yaml`
  Why it should be detected: scenario declares `quantum-config-protocol` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `tls_minimum_protocol_version=TLSv1_0`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~ACCEPT_UNTRUSTED; resolvedValue~tls_minimum_protocol_version=TLSv1_0
- Path: `ops/console/src/modules/security/legacyDigest.ts`
  Why it should be detected: scenario declares `quantum-node-md5` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `MD5`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~MD5

## 7. Near-Real Negative Surfaces

- `deploy/examples/envoy.yaml`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| docs/architecture/section-62.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-63.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-64.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-65.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-66.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-67.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-68.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-69.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-70.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-71.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-72.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-73.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-74.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-75.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-76.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-77.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| docs/architecture/section-78.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| kustomize/fixtures/dev.env | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| ops/console/.gitignore | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| ops/console/jest.config.cjs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| ops/console/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| sql/reference/reference-62.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-63.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-64.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-65.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-66.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-67.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-68.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-69.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-70.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-71.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-72.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-73.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-74.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-75.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-76.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-77.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-78.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_audit_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_delivery_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_dispatch_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_metrics_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_preferences_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_retry_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_routing_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| tests/test_templates_service.py | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/branch-plan.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-absent.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-findings.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-report.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/explainability-contract.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-file-manifest.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-project-dossier.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-tree.txt | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/repo-metadata.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-02.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-03.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/smoke-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-02.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/scenario.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/smoke.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |

## 9. Branch and Commit Plan

Branches:

- `feature/charts-cleanup` tip: `df0d13f3fac00888a5468427daabb36d87abd234`; diverges from `main` at `e3cd9881d0828103e9700fd1a298976f499b4980`
- `feature/hotfix-ssl` tip: `6c33134549c074b08ca1709f7d750535adcd8a31`; diverges from `main` at `e3cd9881d0828103e9700fd1a298976f499b4980`
- `main` tip: `e3cd9881d0828103e9700fd1a298976f499b4980`
- `release/2026.04` tip: `82bf266bfa667f12d35e3e5c9cec7619bdee6211`; diverges from `main` at `e3cd9881d0828103e9700fd1a298976f499b4980`

Commit order:

- `82bf266bfa667f12d35e3e5c9cec7619bdee6211` `c003 release branch clean`: removes or neutralizes a prior signal.
- `e3cd9881d0828103e9700fd1a298976f499b4980` `c001 bootstrap mixed repo`: initial clean or baseline assembly.
- `6c33134549c074b08ca1709f7d750535adcd8a31` `c002 temporary hotfix secret`: introduces an intended signal.
- `df0d13f3fac00888a5468427daabb36d87abd234` `c004 charts cleanup branch`: removes or neutralizes a prior signal.

Expected final head/history state:

- `guardian-active-secret` on `production.env` should behave as `head-only`.
- `guardian-hotfix-secret` on `feature-secret.txt` should behave as `head-only`.
- `quantum-config-trust` on `deploy/envoy.yaml` should behave as `head-only`.
- `quantum-config-protocol` on `deploy/envoy.yaml` should behave as `head-only`.
- `quantum-node-md5` on `legacyDigest.ts` should behave as `head-only`.

## 10. Runnability Contract

### Build

- Command: `C:\Python313\python.EXE -m compileall app tests scripts`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\build-01.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'ops/console'; npm install --silent`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\build-02.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'ops/console'; npm run build`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\build-03.log`

### Test

- Command: `C:\Python313\python.EXE -m pytest -q tests`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\test-01.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'ops/console'; npm test -- --runInBand`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\test-02.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: 
0003: Control-plane repo with live infra config, hotfix branches, CI workflows, and example overlays.
0004: 
```

### `app/config/production.env`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Production. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: APP_SECRET=0123456789ABCDEFA31a
```

### `app/main.py`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime process bootstrap and application entrypoint. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: from fastapi import FastAPI
0002: app = FastAPI()
0003: @app.get('/health')
0004: def health() -> dict[str, str]:
0005:     return {'status': 'ok'}
```

### `deploy/envoy.yaml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Envoy. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: tls_minimum_protocol_version: TLSv1_0
0002: trust_chain_verification: ACCEPT_UNTRUSTED
```

### `deploy/examples/envoy.yaml`

- Why this file matters: `build/deploy` file with expectation `must_not_find`.
- Detailed summary: Build or deployment definition shaping how Envoy is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: trust_chain_verification: ACCEPT_UNTRUSTED
```

### `kustomize/fixtures/dev.env`

- Why this file matters: `generated` file with expectation `must_not_find`.
- Detailed summary: Generated or derived project artifact related to Dev. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: NODE_TLS_REJECT_UNAUTHORIZED=0
```

### `ops/console/dist/scripts/smoke.js`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime business module contributing to Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: "use strict";
0002: console.log('node smoke ok');
```

### `ops/console/src/modules/security/legacyDigest.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Legacy Digest. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: import { createHash } from 'crypto';
0002: export function digest(value: string): string { return createHash('md5').update(value).digest('hex'); }
```

### `pyproject.toml`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Pyproject is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: [project]
0002: name='arq-lab-python'
0003: version='1.0.0'
0004: requires-python='>=3.11'
0005: 
0006: [tool.pytest.ini_options]
0007: addopts='-q'
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'infra mixed smoke ok'
```

### `scripts/smoke.py`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: print('python smoke ok')
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `13958`
- Synthetic filler / inflation LOC: `8580`
- Synthetic filler ratio: `61.47%`

| category | LOC |
| --- | ---: |
| live business code | 204 |
| live config | 13 |
| tests | 32 |
| docs | 22 |
| scripts | 2 |
| fixtures | 0 |
| vendor/generated | 315 |
| synthetic filler / inflation content | 8580 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `production.env`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `feature-secret.txt`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `deploy/envoy.yaml`
  module: `Quantum`
  expected rule/finding family: `ACCEPT_UNTRUSTED`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~ACCEPT_UNTRUSTED; resolvedValue~tls_minimum_protocol_version=TLSv1_0
- path: `deploy/envoy.yaml`
  module: `Quantum`
  expected rule/finding family: `tls_minimum_protocol_version=TLSv1_0`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~ACCEPT_UNTRUSTED; resolvedValue~tls_minimum_protocol_version=TLSv1_0
- path: `legacyDigest.ts`
  module: `Quantum`
  expected rule/finding family: `MD5`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~MD5

### must_not_find

- path: `deploy/examples`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`
- path: `kustomize/fixtures`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `protected negative`
- path: `release-notes.md`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`

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

- `deploy/envoy.yaml`: resolvedValue~`ACCEPT_UNTRUSTED`
- `deploy/envoy.yaml`: resolvedValue~`tls_minimum_protocol_version=TLSv1_0`
- `legacyDigest.ts`: resolvedValue~`MD5`

Explainability failure definition:

- A finding exists on the expected path, but the declared explainability fields are missing or do not match the scenario contract.

## 15. FP/FN Risk Notes

- False negatives are most likely on runtime config files where the detector must bind a weak TLS knob out of YAML or env syntax.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: build/test/smoke contracts execute successfully; models a multi-component or multi-branch enterprise layout; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `2/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Infra-heavy mixed repo with active insecure runtime config, branch divergence, and numerous protected-negative surfaces.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-infra-repo\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
