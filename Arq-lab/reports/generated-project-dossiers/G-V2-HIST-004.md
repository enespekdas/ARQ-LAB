# Generated Project Dossier - G-V2-HIST-004

## 1. Scenario Identity

- scenarioId: `G-V2-HIST-004`
- scenarioName: Guardian history handling for renamed and moved secret-bearing files on main.
- milestone: `M2`
- targetModule: `Guardian`
- language / stack: `Java / Spring Boot`
- repoType: `history`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/partner-rename-lineage`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT, REF_HISTORY`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\G-V2-HIST-004\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V2-HIST-004.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Partner bootstrap repo with rename, move, and revert history around a transient secret.` as a `Java / Spring Boot` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Guardian history handling for renamed and moved secret-bearing files on main.`.

## 3. Architecture Summary

- Major components: `docs, ops, scripts, sql, src, validation`
- Runtime role: `Partner bootstrap repo with rename, move, and revert history around a transient secret.`
- Config flow: `src/main/resources/application.yml`
- Secret flow: `PartnerCredentialArchive.java`
- Crypto/TLS flow if relevant: `Not a Quantum-positive scenario.`
- Test surfaces: `src/test/java/com/arq/partnerrenamelineage/service/BalanceServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/DisputeServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/InvoiceServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/LedgerServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/PartnerServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/PayoutServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/RefundServiceTest.java, src/test/java/com/arq/partnerrenamelineage/service/SettlementServiceTest.java`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
partner-rename-lineage
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
|   |   `-- section-24.md
|   `-- rename-plan.md
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
|       `-- runbook-24.md
|-- scripts
|   `-- smoke.ps1
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
|       `-- reference-24.sql
|-- src
|   |-- main
|   |   |-- java
|   |   |   `-- com
|   |   |       `-- arq
|   |   |           `-- partnerrenamelineage
|   |   |               |-- domain
|   |   |               |   |-- BalanceRecord.java
|   |   |               |   |-- DisputeRecord.java
|   |   |               |   |-- InvoiceRecord.java
|   |   |               |   |-- LedgerRecord.java
|   |   |               |   |-- PartnerRecord.java
|   |   |               |   |-- PayoutRecord.java
|   |   |               |   |-- RefundRecord.java
|   |   |               |   `-- SettlementRecord.java
|   |   |               |-- dto
|   |   |               |   |-- BalanceRequest.java
|   |   |               |   |-- BalanceResponse.java
|   |   |               |   |-- DisputeRequest.java
|   |   |               |   |-- DisputeResponse.java
|   |   |               |   |-- InvoiceRequest.java
|   |   |               |   |-- InvoiceResponse.java
|   |   |               |   |-- LedgerRequest.java
|   |   |               |   |-- LedgerResponse.java
|   |   |               |   |-- PartnerRequest.java
|   |   |               |   |-- PartnerResponse.java
|   |   |               |   |-- PayoutRequest.java
|   |   |               |   |-- PayoutResponse.java
|   |   |               |   |-- RefundRequest.java
|   |   |               |   |-- RefundResponse.java
|   |   |               |   |-- SettlementRequest.java
|   |   |               |   `-- SettlementResponse.java
|   |   |               |-- history
|   |   |               |   |-- archive
|   |   |               |   |   `-- PartnerCredentialArchive.java
|   |   |               |   `-- bootstrap
|   |   |               |-- repository
|   |   |               |   |-- BalanceRepository.java
|   |   |               |   |-- DisputeRepository.java
|   |   |               |   |-- InvoiceRepository.java
|   |   |               |   |-- LedgerRepository.java
|   |   |               |   |-- PartnerRepository.java
|   |   |               |   |-- PayoutRepository.java
|   |   |               |   |-- RefundRepository.java
|   |   |               |   `-- SettlementRepository.java
|   |   |               |-- service
|   |   |               |   |-- BalanceService.java
|   |   |               |   |-- DisputeService.java
|   |   |               |   |-- HistoryRefactor.java
|   |   |               |   |-- InvoiceService.java
|   |   |               |   |-- LedgerService.java
|   |   |               |   |-- PartnerService.java
|   |   |               |   |-- PayoutService.java
|   |   |               |   |-- RefundService.java
|   |   |               |   `-- SettlementService.java
|   |   |               |-- web
|   |   |               |   |-- BalanceController.java
|   |   |               |   |-- DisputeController.java
|   |   |               |   |-- InvoiceController.java
|   |   |               |   |-- LedgerController.java
|   |   |               |   |-- PartnerController.java
|   |   |               |   |-- PayoutController.java
|   |   |               |   |-- RefundController.java
|   |   |               |   `-- SettlementController.java
|   |   |               `-- PartnerrenamelineageApplication.java
|   |   `-- resources
|   |       `-- application.yml
|   `-- test
|       `-- java
|           `-- com
|               `-- arq
|                   `-- partnerrenamelineage
|                       `-- service
|                           |-- BalanceServiceTest.java
|                           |-- DisputeServiceTest.java
|                           |-- InvoiceServiceTest.java
|                           |-- LedgerServiceTest.java
|                           |-- PartnerServiceTest.java
|                           |-- PayoutServiceTest.java
|                           |-- RefundServiceTest.java
|                           `-- SettlementServiceTest.java
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
|-- .gitignore
|-- mvnw
|-- mvnw.cmd
|-- pom.xml
`-- README.md
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | yes | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
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
| docs/rename-plan.md | docs | 1 | Documentation or explanatory material for Rename Plan. | no | no | yes | no | no | no |
| mvnw | generated | 2 | Generated or derived project artifact related to Mvnw. | no | no | yes | no | no | no |
| mvnw.cmd | generated | 2 | Generated or derived project artifact related to Mvnw. | no | no | yes | no | no | no |
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
| pom.xml | build/deploy | 19 | Build or deployment definition shaping how Pom is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ps1 | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
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
| src/main/java/com/arq/partnerrenamelineage/PartnerrenamelineageApplication.java | live-code | 11 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | yes | yes |
| src/main/java/com/arq/partnerrenamelineage/domain/BalanceRecord.java | live-code | 33 | Runtime business module contributing to Balance Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/DisputeRecord.java | live-code | 33 | Runtime business module contributing to Dispute Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/InvoiceRecord.java | live-code | 33 | Runtime business module contributing to Invoice Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/LedgerRecord.java | live-code | 33 | Runtime business module contributing to Ledger Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/PartnerRecord.java | live-code | 33 | Runtime business module contributing to Partner Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/PayoutRecord.java | live-code | 33 | Runtime business module contributing to Payout Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/RefundRecord.java | live-code | 33 | Runtime business module contributing to Refund Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/domain/SettlementRecord.java | live-code | 33 | Runtime business module contributing to Settlement Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/BalanceRequest.java | live-code | 28 | Runtime business module contributing to Balance Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/BalanceResponse.java | live-code | 25 | Runtime business module contributing to Balance Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/DisputeRequest.java | live-code | 28 | Runtime business module contributing to Dispute Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/DisputeResponse.java | live-code | 25 | Runtime business module contributing to Dispute Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/InvoiceRequest.java | live-code | 28 | Runtime business module contributing to Invoice Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/InvoiceResponse.java | live-code | 25 | Runtime business module contributing to Invoice Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/LedgerRequest.java | live-code | 28 | Runtime business module contributing to Ledger Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/LedgerResponse.java | live-code | 25 | Runtime business module contributing to Ledger Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/PartnerRequest.java | live-code | 28 | Runtime business module contributing to Partner Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/PartnerResponse.java | live-code | 25 | Runtime business module contributing to Partner Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/PayoutRequest.java | live-code | 28 | Runtime business module contributing to Payout Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/PayoutResponse.java | live-code | 25 | Runtime business module contributing to Payout Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/RefundRequest.java | live-code | 28 | Runtime business module contributing to Refund Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/RefundResponse.java | live-code | 25 | Runtime business module contributing to Refund Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/SettlementRequest.java | live-code | 28 | Runtime business module contributing to Settlement Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/dto/SettlementResponse.java | live-code | 25 | Runtime business module contributing to Settlement Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/history/archive/PartnerCredentialArchive.java | live-code | 2 | Runtime business module contributing to Partner Credential Archive. | yes | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/BalanceRepository.java | live-code | 21 | Persistence or data-access helper for Balance Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/DisputeRepository.java | live-code | 21 | Persistence or data-access helper for Dispute Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/InvoiceRepository.java | live-code | 21 | Persistence or data-access helper for Invoice Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/LedgerRepository.java | live-code | 21 | Persistence or data-access helper for Ledger Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/PartnerRepository.java | live-code | 21 | Persistence or data-access helper for Partner Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/PayoutRepository.java | live-code | 21 | Persistence or data-access helper for Payout Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/RefundRepository.java | live-code | 21 | Persistence or data-access helper for Refund Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/repository/SettlementRepository.java | live-code | 21 | Persistence or data-access helper for Settlement Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/BalanceService.java | live-code | 19 | Runtime business service implementing Balance Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/DisputeService.java | live-code | 19 | Runtime business service implementing Dispute Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/HistoryRefactor.java | live-code | 2 | Runtime business module contributing to History Refactor. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/InvoiceService.java | live-code | 19 | Runtime business service implementing Invoice Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/LedgerService.java | live-code | 19 | Runtime business service implementing Ledger Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/PartnerService.java | live-code | 19 | Runtime business service implementing Partner Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/PayoutService.java | live-code | 19 | Runtime business service implementing Payout Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/RefundService.java | live-code | 19 | Runtime business service implementing Refund Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/service/SettlementService.java | live-code | 19 | Runtime business service implementing Settlement Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/BalanceController.java | live-code | 23 | Runtime HTTP/controller surface for Balance Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/DisputeController.java | live-code | 23 | Runtime HTTP/controller surface for Dispute Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/InvoiceController.java | live-code | 23 | Runtime HTTP/controller surface for Invoice Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/LedgerController.java | live-code | 23 | Runtime HTTP/controller surface for Ledger Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/PartnerController.java | live-code | 23 | Runtime HTTP/controller surface for Partner Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/PayoutController.java | live-code | 23 | Runtime HTTP/controller surface for Payout Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/RefundController.java | live-code | 23 | Runtime HTTP/controller surface for Refund Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/partnerrenamelineage/web/SettlementController.java | live-code | 23 | Runtime HTTP/controller surface for Settlement Controller. | no | no | no | yes | yes | no |
| src/main/resources/application.yml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Application. | no | no | no | yes | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/BalanceServiceTest.java | test | 13 | Automated test surface covering Balance Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/DisputeServiceTest.java | test | 13 | Automated test surface covering Dispute Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/InvoiceServiceTest.java | test | 13 | Automated test surface covering Invoice Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/LedgerServiceTest.java | test | 13 | Automated test surface covering Ledger Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/PartnerServiceTest.java | test | 13 | Automated test surface covering Partner Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/PayoutServiceTest.java | test | 13 | Automated test surface covering Payout Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/RefundServiceTest.java | test | 13 | Automated test surface covering Refund Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/partnerrenamelineage/service/SettlementServiceTest.java | test | 13 | Automated test surface covering Settlement Service Test behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 14 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 15 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2130 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 674 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 183 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 58 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |

## 6. Positive Surfaces

- Path: `src/main/java/com/arq/partnerrenamelineage/history/archive/PartnerCredentialArchive.java`
  Why it should be detected: scenario declares `history-renamed-secret` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `HISTORY_ONLY`
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
| docs/rename-plan.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| mvnw | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| mvnw.cmd | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| src/test/java/com/arq/partnerrenamelineage/service/BalanceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/DisputeServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/InvoiceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/LedgerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/PartnerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/PayoutServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/RefundServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/partnerrenamelineage/service/SettlementServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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

## 9. Branch and Commit Plan

Branches:

- `main` tip: `792193bd79c5b024cc22e96c16d362d7fc8a4002`

Commit order:

- `f1b888f4962e45f66ea391c124e2e0e997884625` `c001 bootstrap repo`: initial clean or baseline assembly.
- `7f4f22885d887f9ae31b3cdfa9f56a630076d5c1` `c002 add transient partner token`: introduces an intended signal.
- `02961cd7d89f5f1d6159cafd8dc4ac8fa66c5a90` `c003 move token archive into history package`: scenario state change.
- `ff91601428de1ec8fb83df94ae4bd6d46eeb907b` `c004 add rename plan noise`: introduces an intended signal.
- `68aabe4c5dd58e0f223202228fd327454df9d442` `c005 remove token after archive migration`: removes or neutralizes a prior signal.
- `792193bd79c5b024cc22e96c16d362d7fc8a4002` `c006 unrelated refactor`: scenario state change.

Expected final head/history state:

- `history-renamed-secret` on `PartnerCredentialArchive.java` should behave as `HISTORY_ONLY`.

## 10. Runnability Contract

### Build

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q -DskipTests compile`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q test`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: 
0003: Partner bootstrap repo with rename, move, and revert history around a transient secret.
0004: 
```

### `docs/rename-plan.md`

- Why this file matters: `docs` file with expectation `must_not_find`.
- Detailed summary: Documentation or explanatory material for Rename Plan. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: masked_token=****
```

### `pom.xml`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Pom is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
0002:          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
0003:   <modelVersion>4.0.0</modelVersion>
0004:   <parent>
0005:     <groupId>org.springframework.boot</groupId>
0006:     <artifactId>spring-boot-starter-parent</artifactId>
0007:     <version>3.3.5</version>
0008:     <relativePath/>
0009:   </parent>
0010:   <groupId>com.arq.lab</groupId>
0011:   <artifactId>partner-rename-lineage</artifactId>
0012:   <version>1.0.0</version>
```

### `scripts/smoke.ps1`

- Why this file matters: `script` file with expectation `none`.
- Detailed summary: Executable helper script used for build, smoke, or repository validation around Smoke. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: Write-Host 'java smoke ok'
```

### `src/main/java/com/arq/partnerrenamelineage/PartnerrenamelineageApplication.java`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime process bootstrap and application entrypoint. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.partnerrenamelineage;
0002: 
0003: import org.springframework.boot.SpringApplication;
0004: import org.springframework.boot.autoconfigure.SpringBootApplication;
0005: 
0006: @SpringBootApplication
0007: public class PartnerrenamelineageApplication {
0008:     public static void main(String[] args) {
0009:         SpringApplication.run(PartnerrenamelineageApplication.class, args);
0010:     }
0011: }
```

### `src/main/java/com/arq/partnerrenamelineage/history/archive/PartnerCredentialArchive.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Partner Credential Archive. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.partnerrenamelineage.history.archive;
0002: public class PartnerCredentialArchive { private static final String PARTNER_TOKEN = "safe-reference"; public String current() { return PARTNER_TOKEN; } }
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `4130`
- Synthetic filler / inflation LOC: `2640`
- Synthetic filler ratio: `63.92%`

| category | LOC |
| --- | ---: |
| live business code | 1207 |
| live config | 3 |
| tests | 104 |
| docs | 12 |
| scripts | 1 |
| fixtures | 0 |
| vendor/generated | 136 |
| synthetic filler / inflation content | 2640 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `PartnerCredentialArchive.java`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `HISTORY_ONLY`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.

### must_not_find

- path: `docs/rename-plan.md`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `protected negative`
- path: `src/test/resources/fixtures`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`

### may_find_review

- None in the current run.

## 14. Explainability Expectations

Guardian-only scenario. Quantum explainability contract is not applicable here.

## 15. FP/FN Risk Notes

- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: contains a non-trivial amount of live business code; includes meaningful automated test surfaces; build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `3/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Guardian history handling for renamed and moved secret-bearing files on main.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\partner-rename-lineage\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
