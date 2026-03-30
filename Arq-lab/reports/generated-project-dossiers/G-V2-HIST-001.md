# Generated Project Dossier - G-V2-HIST-001

## 1. Scenario Identity

- scenarioId: `G-V2-HIST-001`
- scenarioName: Guardian history-only secret exposure modelling on main branch.
- milestone: `M2`
- targetModule: `Guardian`
- language / stack: `Java / Spring Boot`
- repoType: `history`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage`
- repo remote URL in Gitea: `http://localhost:3001/arq/payments-history-lineage-20260330t104800z`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT, REF_HISTORY`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\G-V2-HIST-001\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V2-HIST-001.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Payments repo with a history-only secret on main.` as a `Java / Spring Boot` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Guardian history-only secret exposure modelling on main branch.`.

## 3. Architecture Summary

- Major components: `docs, ops, scripts, sql, src, validation`
- Runtime role: `Payments repo with a history-only secret on main.`
- Config flow: `src/main/resources/application.yml`
- Secret flow: `PartnerTokenArchive.java`
- Crypto/TLS flow if relevant: `Not a Quantum-positive scenario.`
- Test surfaces: `src/test/java/com/arq/paymentshistorylineage/service/BalanceServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/DisputeServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/InvoiceServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/LedgerServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/PartnerServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/PayoutServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/RefundServiceTest.java, src/test/java/com/arq/paymentshistorylineage/service/SettlementServiceTest.java`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
payments-history-lineage
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
|   |   `-- section-32.md
|   `-- noise.md
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
|       `-- runbook-32.md
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
|       |-- reference-24.sql
|       |-- reference-25.sql
|       |-- reference-26.sql
|       |-- reference-27.sql
|       |-- reference-28.sql
|       |-- reference-29.sql
|       |-- reference-30.sql
|       |-- reference-31.sql
|       `-- reference-32.sql
|-- src
|   |-- main
|   |   |-- java
|   |   |   `-- com
|   |   |       `-- arq
|   |   |           `-- paymentshistorylineage
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
|   |   |               |   `-- bootstrap
|   |   |               |       `-- PartnerTokenArchive.java
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
|   |   |               `-- PaymentshistorylineageApplication.java
|   |   `-- resources
|   |       `-- application.yml
|   `-- test
|       `-- java
|           `-- com
|               `-- arq
|                   `-- paymentshistorylineage
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
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | yes | no | no | no | no |
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
| docs/noise.md | docs | 1 | Documentation or explanatory material for Noise. | no | no | yes | no | no | no |
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
| ops/playbooks/runbook-25.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-26.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-27.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-28.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-29.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-30.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-31.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
| ops/playbooks/runbook-32.md | docs | 42 | Synthetic operational runbook filler used to simulate enterprise documentation density. | no | no | no | no | no | no |
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
| sql/reference/reference-25.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-26.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-27.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-28.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-29.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-30.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-31.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| sql/reference/reference-32.sql | generated | 26 | Synthetic SQL reference filler used to simulate reference data and schema collateral. | no | no | yes | no | no | no |
| src/main/java/com/arq/paymentshistorylineage/PaymentshistorylineageApplication.java | live-code | 11 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | yes | yes |
| src/main/java/com/arq/paymentshistorylineage/domain/BalanceRecord.java | live-code | 33 | Runtime business module contributing to Balance Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/DisputeRecord.java | live-code | 33 | Runtime business module contributing to Dispute Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/InvoiceRecord.java | live-code | 33 | Runtime business module contributing to Invoice Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/LedgerRecord.java | live-code | 33 | Runtime business module contributing to Ledger Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/PartnerRecord.java | live-code | 33 | Runtime business module contributing to Partner Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/PayoutRecord.java | live-code | 33 | Runtime business module contributing to Payout Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/RefundRecord.java | live-code | 33 | Runtime business module contributing to Refund Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/domain/SettlementRecord.java | live-code | 33 | Runtime business module contributing to Settlement Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/BalanceRequest.java | live-code | 28 | Runtime business module contributing to Balance Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/BalanceResponse.java | live-code | 25 | Runtime business module contributing to Balance Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/DisputeRequest.java | live-code | 28 | Runtime business module contributing to Dispute Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/DisputeResponse.java | live-code | 25 | Runtime business module contributing to Dispute Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/InvoiceRequest.java | live-code | 28 | Runtime business module contributing to Invoice Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/InvoiceResponse.java | live-code | 25 | Runtime business module contributing to Invoice Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/LedgerRequest.java | live-code | 28 | Runtime business module contributing to Ledger Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/LedgerResponse.java | live-code | 25 | Runtime business module contributing to Ledger Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/PartnerRequest.java | live-code | 28 | Runtime business module contributing to Partner Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/PartnerResponse.java | live-code | 25 | Runtime business module contributing to Partner Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/PayoutRequest.java | live-code | 28 | Runtime business module contributing to Payout Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/PayoutResponse.java | live-code | 25 | Runtime business module contributing to Payout Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/RefundRequest.java | live-code | 28 | Runtime business module contributing to Refund Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/RefundResponse.java | live-code | 25 | Runtime business module contributing to Refund Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/SettlementRequest.java | live-code | 28 | Runtime business module contributing to Settlement Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/dto/SettlementResponse.java | live-code | 25 | Runtime business module contributing to Settlement Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/history/bootstrap/PartnerTokenArchive.java | live-code | 2 | Runtime business module contributing to Partner Token Archive. | yes | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/BalanceRepository.java | live-code | 21 | Persistence or data-access helper for Balance Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/DisputeRepository.java | live-code | 21 | Persistence or data-access helper for Dispute Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/InvoiceRepository.java | live-code | 21 | Persistence or data-access helper for Invoice Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/LedgerRepository.java | live-code | 21 | Persistence or data-access helper for Ledger Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/PartnerRepository.java | live-code | 21 | Persistence or data-access helper for Partner Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/PayoutRepository.java | live-code | 21 | Persistence or data-access helper for Payout Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/RefundRepository.java | live-code | 21 | Persistence or data-access helper for Refund Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/repository/SettlementRepository.java | live-code | 21 | Persistence or data-access helper for Settlement Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/BalanceService.java | live-code | 19 | Runtime business service implementing Balance Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/DisputeService.java | live-code | 19 | Runtime business service implementing Dispute Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/HistoryRefactor.java | live-code | 2 | Runtime business module contributing to History Refactor. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/InvoiceService.java | live-code | 19 | Runtime business service implementing Invoice Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/LedgerService.java | live-code | 19 | Runtime business service implementing Ledger Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/PartnerService.java | live-code | 19 | Runtime business service implementing Partner Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/PayoutService.java | live-code | 19 | Runtime business service implementing Payout Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/RefundService.java | live-code | 19 | Runtime business service implementing Refund Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/service/SettlementService.java | live-code | 19 | Runtime business service implementing Settlement Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/BalanceController.java | live-code | 23 | Runtime HTTP/controller surface for Balance Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/DisputeController.java | live-code | 23 | Runtime HTTP/controller surface for Dispute Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/InvoiceController.java | live-code | 23 | Runtime HTTP/controller surface for Invoice Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/LedgerController.java | live-code | 23 | Runtime HTTP/controller surface for Ledger Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/PartnerController.java | live-code | 23 | Runtime HTTP/controller surface for Partner Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/PayoutController.java | live-code | 23 | Runtime HTTP/controller surface for Payout Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/RefundController.java | live-code | 23 | Runtime HTTP/controller surface for Refund Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/paymentshistorylineage/web/SettlementController.java | live-code | 23 | Runtime HTTP/controller surface for Settlement Controller. | no | no | no | yes | yes | no |
| src/main/resources/application.yml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Application. | no | no | no | yes | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/BalanceServiceTest.java | test | 13 | Automated test surface covering Balance Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/DisputeServiceTest.java | test | 13 | Automated test surface covering Dispute Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/InvoiceServiceTest.java | test | 13 | Automated test surface covering Invoice Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/LedgerServiceTest.java | test | 13 | Automated test surface covering Ledger Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/PartnerServiceTest.java | test | 13 | Automated test surface covering Partner Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/PayoutServiceTest.java | test | 13 | Automated test surface covering Payout Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/RefundServiceTest.java | test | 13 | Automated test surface covering Refund Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/paymentshistorylineage/service/SettlementServiceTest.java | test | 13 | Automated test surface covering Settlement Service Test behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 14 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 15 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2466 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 724 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 206 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 51 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |

## 6. Positive Surfaces

- Path: `src/main/java/com/arq/paymentshistorylineage/history/bootstrap/PartnerTokenArchive.java`
  Why it should be detected: scenario declares `history-only-token` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `HISTORY_ONLY`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `README.md`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| docs/noise.md | docs | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| sql/reference/reference-25.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-26.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-27.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-28.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-29.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-30.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-31.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| sql/reference/reference-32.sql | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/BalanceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/DisputeServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/InvoiceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/LedgerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/PartnerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/PayoutServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/RefundServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/paymentshistorylineage/service/SettlementServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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

- `main` tip: `f1e482f5ae758bf221f41692c5166ab774552ce8`

Commit order:

- `1eb6cbc87661b636e5ef90be7f1bb3c426db1a16` `c001 bootstrap repo`: initial clean or baseline assembly.
- `c2de05573b1921a27167a72da92c4628d3bdfdfc` `c002 add live partner access token`: introduces an intended signal.
- `1ba6cd3300c2dabc314d897acee13b96a543d801` `c003 add docs noise`: introduces an intended signal.
- `a715d3f2b338a4bc03dd3e2c4562d5b1d81be5ff` `c004 remove token and replace with safe reference`: removes or neutralizes a prior signal.
- `f1e482f5ae758bf221f41692c5166ab774552ce8` `c005 unrelated refactor`: scenario state change.

Expected final head/history state:

- `history-only-token` on `PartnerTokenArchive.java` should behave as `HISTORY_ONLY`.

## 10. Runnability Contract

### Build

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q -DskipTests compile`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q test`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `must_not_find`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0002: 
0003: Payments repo with a history-only secret on main.
0004: 
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
0011:   <artifactId>payments-history-lineage</artifactId>
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

### `src/main/java/com/arq/paymentshistorylineage/PaymentshistorylineageApplication.java`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime process bootstrap and application entrypoint. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.paymentshistorylineage;
0002: 
0003: import org.springframework.boot.SpringApplication;
0004: import org.springframework.boot.autoconfigure.SpringBootApplication;
0005: 
0006: @SpringBootApplication
0007: public class PaymentshistorylineageApplication {
0008:     public static void main(String[] args) {
0009:         SpringApplication.run(PaymentshistorylineageApplication.class, args);
0010:     }
0011: }
```

### `src/main/java/com/arq/paymentshistorylineage/history/bootstrap/PartnerTokenArchive.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Partner Token Archive. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.paymentshistorylineage.history.bootstrap;
0002: public class PartnerTokenArchive { private static final String PARTNER_TOKEN = "safe-reference"; public String current() { return PARTNER_TOKEN; } }
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `5003`
- Synthetic filler / inflation LOC: `3520`
- Synthetic filler ratio: `70.36%`

| category | LOC |
| --- | ---: |
| live business code | 1207 |
| live config | 3 |
| tests | 104 |
| docs | 12 |
| scripts | 1 |
| fixtures | 0 |
| vendor/generated | 129 |
| synthetic filler / inflation content | 3520 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `PartnerTokenArchive.java`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `HISTORY_ONLY`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.

### must_not_find

- path: `README.md`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`
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

- What this scenario is proving: `Guardian history-only secret exposure modelling on main branch.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M2\payments-history-lineage\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
