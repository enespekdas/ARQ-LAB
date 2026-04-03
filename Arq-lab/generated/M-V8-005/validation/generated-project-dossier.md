# Generated Project Dossier - M-V8-005

## 1. Scenario Identity

- scenarioId: `M-V8-005`
- scenarioName: Mixed enterprise monorepo with live secrets and crypto misuse across apps, libs, generated, vendor, and fixtures.
- milestone: `M8`
- targetModule: `Both`
- language / stack: `Java + Node + Python + vendor/generated monorepo`
- repoType: `mixed`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/enterprise-mesh-monorepo`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M-V8-005\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-005.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Enterprise monorepo with apps, shared libs, vendor bundles, generated code, and protected-negative fixtures.` as a `Java + Node + Python + vendor/generated monorepo` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Mixed enterprise monorepo with live secrets and crypto misuse across apps, libs, generated, vendor, and fixtures.`.

## 3. Architecture Summary

- Major components: `apps, deploy, docs, generated, ops, packages, scripts, services, shared, sql, validation, vendor, workers`
- Runtime role: `Enterprise monorepo with apps, shared libs, vendor bundles, generated code, and protected-negative fixtures.`
- Config flow: `deploy/charts/values.yaml, services/platform-java/src/main/resources/application-prod.yml, services/platform-java/src/main/resources/application.yml`
- Secret flow: `application-prod.yml, mesh_service.pem`
- Crypto/TLS flow if relevant: `insecure_partner.py, legacyDigest.ts`
- Test surfaces: `No dedicated test folder beyond build smoke helpers.`
- Docs/vendor/generated surfaces: `README.md, apps/admin-api/.gitignore, apps/admin-api/README.md, apps/admin-api/jest.config.cjs, apps/admin-api/package.json, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
enterprise-mesh-monorepo
|-- apps
|   |-- admin-api
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
|   `-- portal-web
|       `-- src
|           `-- config
|               `-- runtime.ts
|-- deploy
|   `-- charts
|       `-- values.yaml
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
|       `-- section-73.md
|-- generated
|   |-- charts
|   |   `-- values.yaml
|   `-- openapi
|       `-- mesh-client.ts
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
|       `-- runbook-73.md
|-- packages
|   |-- shared-fixtures
|   |   `-- seed.json
|   `-- shared-libs
|       `-- README.md
|-- scripts
|   `-- smoke.ps1
|-- services
|   `-- platform-java
|       |-- docs
|       |   `-- module-boundaries.md
|       |-- scripts
|       |   `-- smoke.ps1
|       |-- src
|       |   |-- main
|       |   |   |-- java
|       |   |   |   `-- com
|       |   |   |       `-- arq
|       |   |   |           `-- platformjava
|       |   |   |               |-- domain
|       |   |   |               |   |-- BalanceRecord.java
|       |   |   |               |   |-- DisputeRecord.java
|       |   |   |               |   |-- InvoiceRecord.java
|       |   |   |               |   |-- LedgerRecord.java
|       |   |   |               |   |-- PartnerRecord.java
|       |   |   |               |   |-- PayoutRecord.java
|       |   |   |               |   |-- RefundRecord.java
|       |   |   |               |   `-- SettlementRecord.java
|       |   |   |               |-- dto
|       |   |   |               |   |-- BalanceRequest.java
|       |   |   |               |   |-- BalanceResponse.java
|       |   |   |               |   |-- DisputeRequest.java
|       |   |   |               |   |-- DisputeResponse.java
|       |   |   |               |   |-- InvoiceRequest.java
|       |   |   |               |   |-- InvoiceResponse.java
|       |   |   |               |   |-- LedgerRequest.java
|       |   |   |               |   |-- LedgerResponse.java
|       |   |   |               |   |-- PartnerRequest.java
|       |   |   |               |   |-- PartnerResponse.java
|       |   |   |               |   |-- PayoutRequest.java
|       |   |   |               |   |-- PayoutResponse.java
|       |   |   |               |   |-- RefundRequest.java
|       |   |   |               |   |-- RefundResponse.java
|       |   |   |               |   |-- SettlementRequest.java
|       |   |   |               |   `-- SettlementResponse.java
|       |   |   |               |-- repository
|       |   |   |               |   |-- BalanceRepository.java
|       |   |   |               |   |-- DisputeRepository.java
|       |   |   |               |   |-- InvoiceRepository.java
|       |   |   |               |   |-- LedgerRepository.java
|       |   |   |               |   |-- PartnerRepository.java
|       |   |   |               |   |-- PayoutRepository.java
|       |   |   |               |   |-- RefundRepository.java
|       |   |   |               |   `-- SettlementRepository.java
|       |   |   |               |-- security
|       |   |   |               |   `-- LegacyCipherService.java
|       |   |   |               |-- service
|       |   |   |               |   |-- BalanceService.java
|       |   |   |               |   |-- DisputeService.java
|       |   |   |               |   |-- InvoiceService.java
|       |   |   |               |   |-- LedgerService.java
|       |   |   |               |   |-- PartnerService.java
|       |   |   |               |   |-- PayoutService.java
|       |   |   |               |   |-- RefundService.java
|       |   |   |               |   `-- SettlementService.java
|       |   |   |               |-- web
|       |   |   |               |   |-- BalanceController.java
|       |   |   |               |   |-- DisputeController.java
|       |   |   |               |   |-- InvoiceController.java
|       |   |   |               |   |-- LedgerController.java
|       |   |   |               |   |-- PartnerController.java
|       |   |   |               |   |-- PayoutController.java
|       |   |   |               |   |-- RefundController.java
|       |   |   |               |   `-- SettlementController.java
|       |   |   |               `-- PlatformjavaApplication.java
|       |   |   `-- resources
|       |   |       |-- application-prod.yml
|       |   |       `-- application.yml
|       |   `-- test
|       |       `-- java
|       |           `-- com
|       |               `-- arq
|       |                   `-- platformjava
|       |                       `-- service
|       |                           |-- BalanceServiceTest.java
|       |                           |-- DisputeServiceTest.java
|       |                           |-- InvoiceServiceTest.java
|       |                           |-- LedgerServiceTest.java
|       |                           |-- PartnerServiceTest.java
|       |                           |-- PayoutServiceTest.java
|       |                           |-- RefundServiceTest.java
|       |                           `-- SettlementServiceTest.java
|       |-- .gitignore
|       |-- mvnw
|       |-- mvnw.cmd
|       |-- pom.xml
|       `-- README.md
|-- shared
|   `-- config
|       `-- keys
|           |-- mesh_service.pem
|           `-- platform_service.pem
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
|       `-- reference-73.sql
|-- validation
|   |-- runnability-logs
|   |   |-- build-01.log
|   |   |-- build-02.log
|   |   |-- build-03.log
|   |   |-- build-04.log
|   |   |-- smoke-01.log
|   |   |-- test-01.log
|   |   |-- test-02.log
|   |   `-- test-03.log
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
|-- vendor
|   |-- sdk
|   |   `-- mesh-client.js
|   `-- third-party-sdk.js
|-- workers
|   `-- sync-worker
|       |-- app
|       |   |-- clients
|       |   |   `-- insecure_partner.py
|       |   |-- models
|       |   |   |-- audit.py
|       |   |   |-- delivery.py
|       |   |   |-- dispatch.py
|       |   |   |-- metrics.py
|       |   |   |-- preferences.py
|       |   |   |-- retry.py
|       |   |   |-- routing.py
|       |   |   `-- templates.py
|       |   |-- security
|       |   |   `-- runtime_secret.py
|       |   |-- services
|       |   |   |-- audit_service.py
|       |   |   |-- delivery_service.py
|       |   |   |-- dispatch_service.py
|       |   |   |-- metrics_service.py
|       |   |   |-- preferences_service.py
|       |   |   |-- retry_service.py
|       |   |   |-- routing_service.py
|       |   |   `-- templates_service.py
|       |   |-- __init__.py
|       |   `-- main.py
|       |-- scripts
|       |   `-- smoke.py
|       |-- tests
|       |   |-- test_audit_service.py
|       |   |-- test_delivery_service.py
|       |   |-- test_dispatch_service.py
|       |   |-- test_metrics_service.py
|       |   |-- test_preferences_service.py
|       |   |-- test_retry_service.py
|       |   |-- test_routing_service.py
|       |   `-- test_templates_service.py
|       |-- .gitignore
|       |-- pyproject.toml
|       `-- README.md
|-- .gitignore
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | no | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| apps/admin-api/.gitignore | generated | 8 | Generated or derived project artifact related to .Gitignore. | no | no | yes | yes | yes | no |
| apps/admin-api/README.md | docs | 11 | Documentation or explanatory material for Readme. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/audit.service.test.ts | live-code | 2 | Runtime business service implementing Audit.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/compliance.service.test.ts | live-code | 2 | Runtime business service implementing Compliance.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/events.service.test.ts | live-code | 2 | Runtime business service implementing Events.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/invites.service.test.ts | live-code | 2 | Runtime business service implementing Invites.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/partners.service.test.ts | live-code | 2 | Runtime business service implementing Partners.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/profiles.service.test.ts | live-code | 2 | Runtime business service implementing Profiles.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/sessions.service.test.ts | live-code | 2 | Runtime business service implementing Sessions.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/__tests__/tokens.service.test.ts | live-code | 2 | Runtime business service implementing Tokens.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/audit.service.test.js | live-code | 4 | Runtime business service implementing Audit.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/compliance.service.test.js | live-code | 4 | Runtime business service implementing Compliance.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/events.service.test.js | live-code | 4 | Runtime business service implementing Events.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/invites.service.test.js | live-code | 4 | Runtime business service implementing Invites.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/partners.service.test.js | live-code | 4 | Runtime business service implementing Partners.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/profiles.service.test.js | live-code | 4 | Runtime business service implementing Profiles.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/sessions.service.test.js | live-code | 4 | Runtime business service implementing Sessions.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/__tests__/tokens.service.test.js | live-code | 4 | Runtime business service implementing Tokens.Service.Test logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/scripts/smoke.js | live-code | 2 | Runtime business module contributing to Smoke. | no | no | no | yes | yes | yes |
| apps/admin-api/dist/src/modules/audit/audit.service.js | live-code | 4 | Runtime business service implementing Audit.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/compliance/compliance.service.js | live-code | 4 | Runtime business service implementing Compliance.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/events/events.service.js | live-code | 4 | Runtime business service implementing Events.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/invites/invites.service.js | live-code | 4 | Runtime business service implementing Invites.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/partners/partners.service.js | live-code | 4 | Runtime business service implementing Partners.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/profiles/profiles.service.js | live-code | 4 | Runtime business service implementing Profiles.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/security/legacyDigest.js | live-code | 5 | Runtime business module contributing to Legacy Digest. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/sessions/sessions.service.js | live-code | 4 | Runtime business service implementing Sessions.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/modules/tokens/tokens.service.js | live-code | 4 | Runtime business service implementing Tokens.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/dist/src/server.js | live-code | 9 | Runtime business module contributing to Server. | no | no | no | yes | yes | no |
| apps/admin-api/jest.config.cjs | generated | 1 | Generated or derived project artifact related to Jest.Config. | no | no | yes | yes | yes | no |
| apps/admin-api/package-lock.json | build/deploy | 4770 | Build or deployment definition shaping how Package Lock is compiled, packaged, or released. | no | no | no | yes | yes | no |
| apps/admin-api/package.json | generated | 8 | Generated or derived project artifact related to Package. | no | no | yes | yes | yes | no |
| apps/admin-api/scripts/smoke.ts | live-code | 1 | Runtime business module contributing to Smoke. | no | no | no | yes | yes | yes |
| apps/admin-api/src/modules/audit/audit.service.ts | live-code | 2 | Runtime business service implementing Audit.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/compliance/compliance.service.ts | live-code | 2 | Runtime business service implementing Compliance.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/events/events.service.ts | live-code | 2 | Runtime business service implementing Events.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/invites/invites.service.ts | live-code | 2 | Runtime business service implementing Invites.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/partners/partners.service.ts | live-code | 2 | Runtime business service implementing Partners.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/profiles/profiles.service.ts | live-code | 2 | Runtime business service implementing Profiles.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/security/legacyDigest.ts | live-code | 2 | Runtime business module contributing to Legacy Digest. | yes | no | no | yes | yes | no |
| apps/admin-api/src/modules/sessions/sessions.service.ts | live-code | 2 | Runtime business service implementing Sessions.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/modules/tokens/tokens.service.ts | live-code | 2 | Runtime business service implementing Tokens.Service logic. | no | no | no | yes | yes | no |
| apps/admin-api/src/server.ts | live-code | 4 | Runtime business module contributing to Server. | no | no | no | yes | yes | no |
| apps/admin-api/tsconfig.json | build/deploy | 4 | Build or deployment definition shaping how Tsconfig is compiled, packaged, or released. | no | no | no | yes | yes | no |
| apps/portal-web/src/config/runtime.ts | live-code | 1 | Runtime business module contributing to Runtime. | no | no | no | yes | no | no |
| deploy/charts/values.yaml | live-config | 2 | Runtime configuration carrying environment or deployment settings for Values. | no | no | no | yes | no | no |
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
| generated/charts/values.yaml | generated | 1 | Generated or derived project artifact related to Values. | no | no | yes | no | no | no |
| generated/openapi/mesh-client.ts | generated | 1 | Generated or derived project artifact related to Mesh Client. | no | no | yes | no | no | no |
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
| packages/shared-fixtures/seed.json | generated | 1 | Generated or derived project artifact related to Seed. | no | no | yes | no | no | no |
| packages/shared-libs/README.md | docs | 3 | Documentation or explanatory material for Readme. | no | no | no | no | no | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | no | yes |
| services/platform-java/.gitignore | generated | 8 | Generated or derived project artifact related to .Gitignore. | no | no | yes | yes | yes | no |
| services/platform-java/README.md | docs | 11 | Documentation or explanatory material for Readme. | no | no | no | yes | yes | no |
| services/platform-java/docs/module-boundaries.md | docs | 1 | Documentation or explanatory material for Module Boundaries. | no | no | no | yes | yes | no |
| services/platform-java/mvnw | generated | 2 | Generated or derived project artifact related to Mvnw. | no | no | yes | yes | yes | no |
| services/platform-java/mvnw.cmd | generated | 2 | Generated or derived project artifact related to Mvnw. | no | no | yes | yes | yes | no |
| services/platform-java/pom.xml | generated | 19 | Generated or derived project artifact related to Pom. | no | no | yes | yes | yes | no |
| services/platform-java/scripts/smoke.ps1 | generated | 1 | Generated or derived project artifact related to Smoke. | no | no | yes | yes | yes | yes |
| services/platform-java/src/main/java/com/arq/platformjava/PlatformjavaApplication.java | live-code | 11 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | yes | yes |
| services/platform-java/src/main/java/com/arq/platformjava/domain/BalanceRecord.java | live-code | 33 | Runtime business module contributing to Balance Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/DisputeRecord.java | live-code | 33 | Runtime business module contributing to Dispute Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/InvoiceRecord.java | live-code | 33 | Runtime business module contributing to Invoice Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/LedgerRecord.java | live-code | 33 | Runtime business module contributing to Ledger Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/PartnerRecord.java | live-code | 33 | Runtime business module contributing to Partner Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/PayoutRecord.java | live-code | 33 | Runtime business module contributing to Payout Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/RefundRecord.java | live-code | 33 | Runtime business module contributing to Refund Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/domain/SettlementRecord.java | live-code | 33 | Runtime business module contributing to Settlement Record. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/BalanceRequest.java | live-code | 28 | Runtime business module contributing to Balance Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/BalanceResponse.java | live-code | 25 | Runtime business module contributing to Balance Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/DisputeRequest.java | live-code | 28 | Runtime business module contributing to Dispute Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/DisputeResponse.java | live-code | 25 | Runtime business module contributing to Dispute Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/InvoiceRequest.java | live-code | 28 | Runtime business module contributing to Invoice Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/InvoiceResponse.java | live-code | 25 | Runtime business module contributing to Invoice Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/LedgerRequest.java | live-code | 28 | Runtime business module contributing to Ledger Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/LedgerResponse.java | live-code | 25 | Runtime business module contributing to Ledger Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/PartnerRequest.java | live-code | 28 | Runtime business module contributing to Partner Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/PartnerResponse.java | live-code | 25 | Runtime business module contributing to Partner Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/PayoutRequest.java | live-code | 28 | Runtime business module contributing to Payout Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/PayoutResponse.java | live-code | 25 | Runtime business module contributing to Payout Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/RefundRequest.java | live-code | 28 | Runtime business module contributing to Refund Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/RefundResponse.java | live-code | 25 | Runtime business module contributing to Refund Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/SettlementRequest.java | live-code | 28 | Runtime business module contributing to Settlement Request. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/dto/SettlementResponse.java | live-code | 25 | Runtime business module contributing to Settlement Response. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/BalanceRepository.java | live-code | 21 | Persistence or data-access helper for Balance Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/DisputeRepository.java | live-code | 21 | Persistence or data-access helper for Dispute Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/InvoiceRepository.java | live-code | 21 | Persistence or data-access helper for Invoice Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/LedgerRepository.java | live-code | 21 | Persistence or data-access helper for Ledger Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/PartnerRepository.java | live-code | 21 | Persistence or data-access helper for Partner Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/PayoutRepository.java | live-code | 21 | Persistence or data-access helper for Payout Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/RefundRepository.java | live-code | 21 | Persistence or data-access helper for Refund Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/repository/SettlementRepository.java | live-code | 21 | Persistence or data-access helper for Settlement Repository. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/security/LegacyCipherService.java | live-code | 3 | Runtime business service implementing Legacy Cipher Service logic. | no | yes | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/BalanceService.java | live-code | 19 | Runtime business service implementing Balance Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/DisputeService.java | live-code | 19 | Runtime business service implementing Dispute Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/InvoiceService.java | live-code | 19 | Runtime business service implementing Invoice Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/LedgerService.java | live-code | 19 | Runtime business service implementing Ledger Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/PartnerService.java | live-code | 19 | Runtime business service implementing Partner Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/PayoutService.java | live-code | 19 | Runtime business service implementing Payout Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/RefundService.java | live-code | 19 | Runtime business service implementing Refund Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/service/SettlementService.java | live-code | 19 | Runtime business service implementing Settlement Service logic. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/BalanceController.java | live-code | 23 | Runtime HTTP/controller surface for Balance Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/DisputeController.java | live-code | 23 | Runtime HTTP/controller surface for Dispute Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/InvoiceController.java | live-code | 23 | Runtime HTTP/controller surface for Invoice Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/LedgerController.java | live-code | 23 | Runtime HTTP/controller surface for Ledger Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/PartnerController.java | live-code | 23 | Runtime HTTP/controller surface for Partner Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/PayoutController.java | live-code | 23 | Runtime HTTP/controller surface for Payout Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/RefundController.java | live-code | 23 | Runtime HTTP/controller surface for Refund Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/java/com/arq/platformjava/web/SettlementController.java | live-code | 23 | Runtime HTTP/controller surface for Settlement Controller. | no | no | no | yes | yes | no |
| services/platform-java/src/main/resources/application-prod.yml | live-config | 2 | Runtime configuration carrying environment or deployment settings for Application Prod. | yes | no | no | yes | yes | no |
| services/platform-java/src/main/resources/application.yml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Application. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/BalanceServiceTest.java | live-code | 13 | Runtime business service implementing Balance Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/DisputeServiceTest.java | live-code | 13 | Runtime business service implementing Dispute Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/InvoiceServiceTest.java | live-code | 13 | Runtime business service implementing Invoice Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/LedgerServiceTest.java | live-code | 13 | Runtime business service implementing Ledger Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/PartnerServiceTest.java | live-code | 13 | Runtime business service implementing Partner Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/PayoutServiceTest.java | live-code | 13 | Runtime business service implementing Payout Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/RefundServiceTest.java | live-code | 13 | Runtime business service implementing Refund Service Test logic. | no | no | no | yes | yes | no |
| services/platform-java/src/test/java/com/arq/platformjava/service/SettlementServiceTest.java | live-code | 13 | Runtime business service implementing Settlement Service Test logic. | no | no | no | yes | yes | no |
| shared/config/keys/mesh_service.pem | generated | 10 | Generated or derived project artifact related to Mesh Service. | yes | no | yes | no | no | no |
| shared/config/keys/platform_service.pem | generated | 10 | Generated or derived project artifact related to Platform Service. | no | no | yes | no | no | no |
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
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 20 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 54 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/explainability-contract.json | generated | 18 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 5518 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 1536 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 481 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 21 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-02.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-03.log | generated | 12 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-04.log | generated | 44 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/test-02.log | generated | 34 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/test-03.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| vendor/sdk/mesh-client.js | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Mesh Client. | no | no | yes | no | no | no |
| vendor/third-party-sdk.js | vendor | 1 | Vendored or copied artifact used to simulate third-party noise around Third Party Sdk. | no | no | yes | no | no | no |
| workers/sync-worker/.gitignore | generated | 8 | Generated or derived project artifact related to .Gitignore. | no | no | yes | no | yes | no |
| workers/sync-worker/README.md | docs | 11 | Documentation or explanatory material for Readme. | no | no | no | no | yes | no |
| workers/sync-worker/app/__init__.py | live-code | 0 | Runtime business module contributing to Init. | no | no | no | yes | yes | no |
| workers/sync-worker/app/clients/insecure_partner.py | live-code | 4 | Runtime business module contributing to Insecure Partner. | yes | no | no | yes | yes | no |
| workers/sync-worker/app/main.py | live-code | 5 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/audit.py | live-code | 6 | Runtime business module contributing to Audit. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/delivery.py | live-code | 6 | Runtime business module contributing to Delivery. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/dispatch.py | live-code | 6 | Runtime business module contributing to Dispatch. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/metrics.py | live-code | 6 | Runtime business module contributing to Metrics. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/preferences.py | live-code | 6 | Runtime business module contributing to Preferences. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/retry.py | live-code | 6 | Runtime business module contributing to Retry. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/routing.py | live-code | 6 | Runtime business module contributing to Routing. | no | no | no | yes | yes | no |
| workers/sync-worker/app/models/templates.py | live-code | 6 | Runtime business module contributing to Templates. | no | no | no | yes | yes | no |
| workers/sync-worker/app/security/runtime_secret.py | live-code | 1 | Runtime business module contributing to Runtime Secret. | no | yes | no | yes | yes | no |
| workers/sync-worker/app/services/audit_service.py | live-code | 4 | Runtime business service implementing Audit Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/delivery_service.py | live-code | 4 | Runtime business service implementing Delivery Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/dispatch_service.py | live-code | 4 | Runtime business service implementing Dispatch Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/metrics_service.py | live-code | 4 | Runtime business service implementing Metrics Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/preferences_service.py | live-code | 4 | Runtime business service implementing Preferences Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/retry_service.py | live-code | 4 | Runtime business service implementing Retry Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/routing_service.py | live-code | 4 | Runtime business service implementing Routing Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/app/services/templates_service.py | live-code | 4 | Runtime business service implementing Templates Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/pyproject.toml | build/deploy | 7 | Build or deployment definition shaping how Pyproject is compiled, packaged, or released. | no | no | no | yes | yes | no |
| workers/sync-worker/scripts/smoke.py | live-code | 1 | Runtime business module contributing to Smoke. | no | no | no | yes | yes | yes |
| workers/sync-worker/tests/test_audit_service.py | live-code | 4 | Runtime business service implementing Test Audit Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_delivery_service.py | live-code | 4 | Runtime business service implementing Test Delivery Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_dispatch_service.py | live-code | 4 | Runtime business service implementing Test Dispatch Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_metrics_service.py | live-code | 4 | Runtime business service implementing Test Metrics Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_preferences_service.py | live-code | 4 | Runtime business service implementing Test Preferences Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_retry_service.py | live-code | 4 | Runtime business service implementing Test Retry Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_routing_service.py | live-code | 4 | Runtime business service implementing Test Routing Service logic. | no | no | no | yes | yes | no |
| workers/sync-worker/tests/test_templates_service.py | live-code | 4 | Runtime business service implementing Test Templates Service logic. | no | no | no | yes | yes | no |

## 6. Positive Surfaces

- Path: `services/platform-java/src/main/resources/application-prod.yml`
  Why it should be detected: scenario declares `guardian-java-secret` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `shared/config/keys/mesh_service.pem`
  Why it should be detected: scenario declares `guardian-private-key` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.private-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.
- Path: `apps/admin-api/src/modules/security/legacyDigest.ts`
  Why it should be detected: scenario declares `quantum-node-md5` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `MD5`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~MD5
- Path: `workers/sync-worker/app/clients/insecure_partner.py`
  Why it should be detected: scenario declares `quantum-python-verify-false` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `verify=False`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~verify=False

## 7. Near-Real Negative Surfaces

- `services/platform-java/src/main/java/com/arq/platformjava/security/LegacyCipherService.java`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `workers/sync-worker/app/security/runtime_secret.py`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

## 8. Protected Negative Surfaces

| path | classification | why protected |
| --- | --- | --- |
| apps/admin-api/.gitignore | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| apps/admin-api/jest.config.cjs | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| apps/admin-api/package.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| generated/charts/values.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| generated/openapi/mesh-client.ts | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| packages/shared-fixtures/seed.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/platform-java/.gitignore | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/platform-java/mvnw | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/platform-java/mvnw.cmd | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/platform-java/pom.xml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| services/platform-java/scripts/smoke.ps1 | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| shared/config/keys/mesh_service.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| shared/config/keys/platform_service.pem | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| validation/runnability-logs/build-04.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/smoke-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-02.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-03.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/scenario.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/smoke.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| vendor/sdk/mesh-client.js | vendor | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| vendor/third-party-sdk.js | vendor | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| workers/sync-worker/.gitignore | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |

## 9. Branch and Commit Plan

Branches:

- `main` tip: `727bae6b9dcdf01536c865e4c2467760f5b8e157`

Commit order:

- `727bae6b9dcdf01536c865e4c2467760f5b8e157` `bootstrap M-V8-005`: initial clean or baseline assembly.

Expected final head/history state:

- `guardian-java-secret` on `application-prod.yml` should behave as `head-only`.
- `guardian-private-key` on `mesh_service.pem` should behave as `head-only`.
- `quantum-node-md5` on `legacyDigest.ts` should behave as `head-only`.
- `quantum-python-verify-false` on `insecure_partner.py` should behave as `head-only`.

## 10. Runnability Contract

### Build

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q -f services/platform-java/pom.xml -DskipTests compile`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\build-01.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'apps/admin-api'; npm install --silent`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\build-02.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'apps/admin-api'; npm run build`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\build-03.log`
- Command: `C:\Python313\python.EXE -m compileall workers/sync-worker/app workers/sync-worker/tests workers/sync-worker/scripts`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\build-04.log`

### Test

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q -f services/platform-java/pom.xml test`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\test-01.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'apps/admin-api'; npm test -- --runInBand`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\test-02.log`
- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command Set-Location 'workers/sync-worker'; python -m pytest -q tests`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\test-03.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # enterprise-mesh-monorepo
0002: 
0003: Enterprise monorepo with apps, shared libs, vendor bundles, generated code, and protected-negative fixtures.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
```

### `apps/admin-api/dist/scripts/smoke.js`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime business module contributing to Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: "use strict";
0002: console.log('node smoke ok');
```

### `apps/admin-api/src/modules/security/legacyDigest.ts`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Legacy Digest. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: import { createHash } from 'crypto';
0002: export function digest(value: string): string { return createHash('md5').update(value).digest('hex'); }
```

### `generated/openapi/mesh-client.ts`

- Why this file matters: `generated` file with expectation `must_not_find`.
- Detailed summary: Generated or derived project artifact related to Mesh Client. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: export const generatedExample = 'verify=false';
```

### `packages/shared-fixtures/seed.json`

- Why this file matters: `generated` file with expectation `must_not_find`.
- Detailed summary: Generated or derived project artifact related to Seed. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: {"token":"fixture-only","tls":"rejectUnauthorized false"}
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'mixed monorepo smoke ok'
```

### `services/platform-java/scripts/smoke.ps1`

- Why this file matters: `generated` file with expectation `none`.
- Detailed summary: Generated or derived project artifact related to Smoke. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: Write-Host 'java smoke ok'
```

### `services/platform-java/src/main/java/com/arq/platformjava/PlatformjavaApplication.java`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime process bootstrap and application entrypoint. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.platformjava;
0002: 
0003: import org.springframework.boot.SpringApplication;
0004: import org.springframework.boot.autoconfigure.SpringBootApplication;
0005: 
0006: @SpringBootApplication
0007: public class PlatformjavaApplication {
0008:     public static void main(String[] args) {
0009:         SpringApplication.run(PlatformjavaApplication.class, args);
0010:     }
0011: }
```

### `services/platform-java/src/main/java/com/arq/platformjava/security/LegacyCipherService.java`

- Why this file matters: `live-code` file with expectation `may_find_review`.
- Detailed summary: Runtime business service implementing Legacy Cipher Service logic. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0002: import javax.crypto.Cipher;
0003: public class LegacyCipherService { public Cipher cipher() throws Exception { return Cipher.getInstance("AES/ECB/PKCS5Padding"); } }
```

### `services/platform-java/src/main/resources/application-prod.yml`

- Why this file matters: `live-config` file with expectation `must_find`.
- Detailed summary: Runtime configuration carrying environment or deployment settings for Application Prod. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: oauth:
0002:   client-secret: LiveSecretX9aK4mP1cQ7zR2vW
```

### `shared/config/keys/mesh_service.pem`

- Why this file matters: `generated` file with expectation `must_find`.
- Detailed summary: Generated or derived project artifact related to Mesh Service. It is non-live or protected in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: -----BEGIN RSA PRIVATE KEY-----
0002: MIIEowIBAAKCAQEAzQm5vL9t2Xg7k1rP4hFd8sW2mY6nQ1tV5cR9pK3xJ7bN0dL2
0009: zJ6pQ3tV0xC7mB4nL1sR8yD5hK2qW9vF6pT3xN0cB7mL4qR1yD8hK5pQ==
0010: -----END RSA PRIVATE KEY-----
```

### `shared/config/keys/platform_service.pem`

- Why this file matters: `generated` file with expectation `may_find_review`.
- Detailed summary: Generated or derived project artifact related to Platform Service. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: -----BEGIN RSA PRIVATE KEY-----
0002: MIIEpAIBAAKCAQEAtmJvYV7t6Vg4l0xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L
0009: xJ5HfZK3aV6D5r5YQf5x4mG8c+K2h0mK8L2s9mDkLQ==
0010: -----END RSA PRIVATE KEY-----
```

### `vendor/sdk/mesh-client.js`

- Why this file matters: `vendor` file with expectation `must_not_find`.
- Detailed summary: Vendored or copied artifact used to simulate third-party noise around Mesh Client. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: module.exports = { note: 'vendor example only' };
```

### `vendor/third-party-sdk.js`

- Why this file matters: `vendor` file with expectation `must_not_find`.
- Detailed summary: Vendored or copied artifact used to simulate third-party noise around Third Party Sdk. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: var secret='example-only'; var weak='md5 example';
```

### `workers/sync-worker/app/clients/insecure_partner.py`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Insecure Partner. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0003: def fetch_payload(url: str) -> str:
0004:     return requests.get(url, verify=False, timeout=5).text
```

### `workers/sync-worker/app/main.py`

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

### `workers/sync-worker/app/security/runtime_secret.py`

- Why this file matters: `live-code` file with expectation `may_find_review`.
- Detailed summary: Runtime business module contributing to Runtime Secret. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: RUNTIME_SECRET = "0123456789ABCDEFA31a"
```

### `workers/sync-worker/scripts/smoke.py`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime business module contributing to Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: print('python smoke ok')
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `14775`
- Synthetic filler / inflation LOC: `8030`
- Synthetic filler ratio: `54.35%`

| category | LOC |
| --- | ---: |
| live business code | 1553 |
| live config | 7 |
| tests | 0 |
| docs | 48 |
| scripts | 1 |
| fixtures | 0 |
| vendor/generated | 347 |
| synthetic filler / inflation content | 8030 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `application-prod.yml`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `mesh_service.pem`
  module: `Guardian`
  expected rule/finding family: `guardian.private-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.
- path: `legacyDigest.ts`
  module: `Quantum`
  expected rule/finding family: `MD5`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~MD5
- path: `insecure_partner.py`
  module: `Quantum`
  expected rule/finding family: `verify=False`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~verify=False

### must_not_find

- path: `vendor/`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `protected negative`
- path: `generated/openapi`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `protected negative`
- path: `packages/shared-fixtures`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `protected negative`

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

- `legacyDigest.ts`: resolvedValue~`MD5`
- `insecure_partner.py`: resolvedValue~`verify=False`

Explainability failure definition:

- A finding exists on the expected path, but the declared explainability fields are missing or do not match the scenario contract.

## 15. FP/FN Risk Notes

- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.
- Current run already demonstrated this risk: verdict=`PASS_WITH_NOISE`.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: contains a non-trivial amount of live business code; build/test/smoke contracts execute successfully; models a multi-component or multi-branch enterprise layout; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `3/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Mixed enterprise monorepo with live secrets and crypto misuse across apps, libs, generated, vendor, and fixtures.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
