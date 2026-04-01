# Generated Project Dossier - Q-V3-JAVA-002

## 1. Scenario Identity

- scenarioId: `Q-V3-JAVA-002`
- scenarioName: Quantum weak crypto patterns in legacy Java payment utilities.
- milestone: `M3`
- targetModule: `Quantum`
- language / stack: `Java / Spring Boot`
- repoType: `snapshot`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/legacy-payment-crypto-java`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT`
- branch scopes intended for this scenario: `SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\Q-V3-JAVA-002\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-JAVA-002.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Legacy payment encryption and key management helpers.` as a `Java / Spring Boot` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Quantum weak crypto patterns in legacy Java payment utilities.`.

## 3. Architecture Summary

- Major components: `docs, ops, scripts, sql, src, validation`
- Runtime role: `Legacy payment encryption and key management helpers.`
- Config flow: `src/main/resources/application.yml`
- Secret flow: `No Guardian must-find secret path in this scenario.`
- Crypto/TLS flow if relevant: `BatchReconciliationCipher.java, LegacyEnvelopeCipher.java`
- Test surfaces: `src/test/java/com/arq/legacypaymentcryptojava/service/BalanceServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/DisputeServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/InvoiceServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/LedgerServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/PartnerServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/PayoutServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/RefundServiceTest.java, src/test/java/com/arq/legacypaymentcryptojava/service/SettlementServiceTest.java`
- Docs/vendor/generated surfaces: `README.md, docs/architecture/section-01.md, docs/architecture/section-02.md, docs/architecture/section-03.md, docs/architecture/section-04.md, docs/architecture/section-05.md, docs/architecture/section-06.md, docs/architecture/section-07.md, docs/architecture/section-08.md, docs/architecture/section-09.md, docs/architecture/section-10.md, docs/architecture/section-11.md`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
legacy-payment-crypto-java
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
|       `-- section-32.md
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
|   |   |           `-- legacypaymentcryptojava
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
|   |   |               |-- repository
|   |   |               |   |-- BalanceRepository.java
|   |   |               |   |-- DisputeRepository.java
|   |   |               |   |-- InvoiceRepository.java
|   |   |               |   |-- LedgerRepository.java
|   |   |               |   |-- PartnerRepository.java
|   |   |               |   |-- PayoutRepository.java
|   |   |               |   |-- RefundRepository.java
|   |   |               |   `-- SettlementRepository.java
|   |   |               |-- security
|   |   |               |   |-- BatchReconciliationCipher.java
|   |   |               |   |-- LegacyEnvelopeCipher.java
|   |   |               |   |-- LegacyPasswordFactory.java
|   |   |               |   `-- SecureEnvelopeCipher.java
|   |   |               |-- service
|   |   |               |   |-- BalanceService.java
|   |   |               |   |-- DisputeService.java
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
|   |   |               `-- LegacypaymentcryptojavaApplication.java
|   |   `-- resources
|   |       `-- application.yml
|   `-- test
|       `-- java
|           `-- com
|               `-- arq
|                   `-- legacypaymentcryptojava
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
|   |-- explainability-contract.json
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
| docs/architecture/section-25.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-26.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-27.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-28.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-29.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-30.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-31.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
| docs/architecture/section-32.md | docs | 42 | Synthetic architecture filler used to reach line-density targets without altering runtime behavior. | no | no | yes | no | no | no |
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
| src/main/java/com/arq/legacypaymentcryptojava/LegacypaymentcryptojavaApplication.java | live-code | 11 | Runtime process bootstrap and application entrypoint. | no | no | no | yes | yes | yes |
| src/main/java/com/arq/legacypaymentcryptojava/domain/BalanceRecord.java | live-code | 33 | Runtime business module contributing to Balance Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/DisputeRecord.java | live-code | 33 | Runtime business module contributing to Dispute Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/InvoiceRecord.java | live-code | 33 | Runtime business module contributing to Invoice Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/LedgerRecord.java | live-code | 33 | Runtime business module contributing to Ledger Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/PartnerRecord.java | live-code | 33 | Runtime business module contributing to Partner Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/PayoutRecord.java | live-code | 33 | Runtime business module contributing to Payout Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/RefundRecord.java | live-code | 33 | Runtime business module contributing to Refund Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/domain/SettlementRecord.java | live-code | 33 | Runtime business module contributing to Settlement Record. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/BalanceRequest.java | live-code | 28 | Runtime business module contributing to Balance Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/BalanceResponse.java | live-code | 25 | Runtime business module contributing to Balance Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/DisputeRequest.java | live-code | 28 | Runtime business module contributing to Dispute Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/DisputeResponse.java | live-code | 25 | Runtime business module contributing to Dispute Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/InvoiceRequest.java | live-code | 28 | Runtime business module contributing to Invoice Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/InvoiceResponse.java | live-code | 25 | Runtime business module contributing to Invoice Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/LedgerRequest.java | live-code | 28 | Runtime business module contributing to Ledger Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/LedgerResponse.java | live-code | 25 | Runtime business module contributing to Ledger Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/PartnerRequest.java | live-code | 28 | Runtime business module contributing to Partner Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/PartnerResponse.java | live-code | 25 | Runtime business module contributing to Partner Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/PayoutRequest.java | live-code | 28 | Runtime business module contributing to Payout Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/PayoutResponse.java | live-code | 25 | Runtime business module contributing to Payout Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/RefundRequest.java | live-code | 28 | Runtime business module contributing to Refund Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/RefundResponse.java | live-code | 25 | Runtime business module contributing to Refund Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/SettlementRequest.java | live-code | 28 | Runtime business module contributing to Settlement Request. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/dto/SettlementResponse.java | live-code | 25 | Runtime business module contributing to Settlement Response. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/BalanceRepository.java | live-code | 21 | Persistence or data-access helper for Balance Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/DisputeRepository.java | live-code | 21 | Persistence or data-access helper for Dispute Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/InvoiceRepository.java | live-code | 21 | Persistence or data-access helper for Invoice Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/LedgerRepository.java | live-code | 21 | Persistence or data-access helper for Ledger Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/PartnerRepository.java | live-code | 21 | Persistence or data-access helper for Partner Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/PayoutRepository.java | live-code | 21 | Persistence or data-access helper for Payout Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/RefundRepository.java | live-code | 21 | Persistence or data-access helper for Refund Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/repository/SettlementRepository.java | live-code | 21 | Persistence or data-access helper for Settlement Repository. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/security/BatchReconciliationCipher.java | live-code | 3 | Runtime business module contributing to Batch Reconciliation Cipher. | yes | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/security/LegacyEnvelopeCipher.java | live-code | 3 | Runtime business module contributing to Legacy Envelope Cipher. | yes | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/security/LegacyPasswordFactory.java | live-code | 3 | Runtime business module contributing to Legacy Password Factory. | no | yes | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/security/SecureEnvelopeCipher.java | live-code | 3 | Runtime business module contributing to Secure Envelope Cipher. | no | yes | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/BalanceService.java | live-code | 19 | Runtime business service implementing Balance Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/DisputeService.java | live-code | 19 | Runtime business service implementing Dispute Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/InvoiceService.java | live-code | 19 | Runtime business service implementing Invoice Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/LedgerService.java | live-code | 19 | Runtime business service implementing Ledger Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/PartnerService.java | live-code | 19 | Runtime business service implementing Partner Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/PayoutService.java | live-code | 19 | Runtime business service implementing Payout Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/RefundService.java | live-code | 19 | Runtime business service implementing Refund Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/service/SettlementService.java | live-code | 19 | Runtime business service implementing Settlement Service logic. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/BalanceController.java | live-code | 23 | Runtime HTTP/controller surface for Balance Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/DisputeController.java | live-code | 23 | Runtime HTTP/controller surface for Dispute Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/InvoiceController.java | live-code | 23 | Runtime HTTP/controller surface for Invoice Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/LedgerController.java | live-code | 23 | Runtime HTTP/controller surface for Ledger Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/PartnerController.java | live-code | 23 | Runtime HTTP/controller surface for Partner Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/PayoutController.java | live-code | 23 | Runtime HTTP/controller surface for Payout Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/RefundController.java | live-code | 23 | Runtime HTTP/controller surface for Refund Controller. | no | no | no | yes | yes | no |
| src/main/java/com/arq/legacypaymentcryptojava/web/SettlementController.java | live-code | 23 | Runtime HTTP/controller surface for Settlement Controller. | no | no | no | yes | yes | no |
| src/main/resources/application.yml | live-config | 3 | Runtime configuration carrying environment or deployment settings for Application. | no | no | no | yes | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/BalanceServiceTest.java | test | 13 | Automated test surface covering Balance Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/DisputeServiceTest.java | test | 13 | Automated test surface covering Dispute Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/InvoiceServiceTest.java | test | 13 | Automated test surface covering Invoice Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/LedgerServiceTest.java | test | 13 | Automated test surface covering Ledger Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/PartnerServiceTest.java | test | 13 | Automated test surface covering Partner Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/PayoutServiceTest.java | test | 13 | Automated test surface covering Payout Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/RefundServiceTest.java | test | 13 | Automated test surface covering Refund Service Test behavior. | no | no | yes | no | yes | no |
| src/test/java/com/arq/legacypaymentcryptojava/service/SettlementServiceTest.java | test | 13 | Automated test surface covering Settlement Service Test behavior. | no | no | yes | no | yes | no |
| validation/branch-plan.yaml | generated | 3 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 14 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 28 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/explainability-contract.json | generated | 18 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2494 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 787 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 207 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 23 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |

## 6. Positive Surfaces

- Path: `src/main/java/com/arq/legacypaymentcryptojava/security/LegacyEnvelopeCipher.java`
  Why it should be detected: scenario declares `desede` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `DESede/ECB/PKCS5Padding`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~DESede/ECB/PKCS5Padding
- Path: `src/main/java/com/arq/legacypaymentcryptojava/security/BatchReconciliationCipher.java`
  Why it should be detected: scenario declares `aes-ecb` as a live positive surface.
  Target module: `Quantum`
  Finding family / rule family expectation: `AES/ECB`
  Head/history behavior: `head-only`
  Explainability expectation: resolvedValue~AES/ECB

## 7. Near-Real Negative Surfaces

- `src/main/java/com/arq/legacypaymentcryptojava/security/LegacyPasswordFactory.java`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.
- `src/main/java/com/arq/legacypaymentcryptojava/security/SecureEnvelopeCipher.java`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

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
| src/test/java/com/arq/legacypaymentcryptojava/service/BalanceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/DisputeServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/InvoiceServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/LedgerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/PartnerServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/PayoutServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/RefundServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| src/test/java/com/arq/legacypaymentcryptojava/service/SettlementServiceTest.java | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| validation/runnability-logs/smoke-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/scenario.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/smoke.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |

## 9. Branch and Commit Plan

Snapshot-only scenario. No branch divergence or history-only contract is intended beyond the default branch head scan.

## 10. Runnability Contract

### Build

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q -DskipTests compile`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\runnability-logs\build-01.log`

### Test

- Command: `C:\maven\apache-maven-3.9.12\bin\mvn.cmd -q test`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy Bypass -File scripts/smoke.ps1`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: # legacy-payment-crypto-java
0002: 
0003: Legacy payment encryption and key management helpers.
0004: 
0005: This repository is part of the ARQ Lab validation workspace. It contains production-like source layouts, tests, scripts, deploy notes, and validation assets.
0006: 
0007: ## Local development
0008: 
0009: - Review `scripts/` for smoke and validation commands.
0010: - Review `validation/` for machine-readable expectations.
0011: - Review `docs/` for architecture and operational material.
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
0011:   <artifactId>legacy-payment-crypto-java</artifactId>
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

### `src/main/java/com/arq/legacypaymentcryptojava/LegacypaymentcryptojavaApplication.java`

- Why this file matters: `live-code` file with expectation `none`.
- Detailed summary: Runtime process bootstrap and application entrypoint. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.legacypaymentcryptojava;
0002: 
0003: import org.springframework.boot.SpringApplication;
0004: import org.springframework.boot.autoconfigure.SpringBootApplication;
0005: 
0006: @SpringBootApplication
0007: public class LegacypaymentcryptojavaApplication {
0008:     public static void main(String[] args) {
0009:         SpringApplication.run(LegacypaymentcryptojavaApplication.class, args);
0010:     }
0011: }
```

### `src/main/java/com/arq/legacypaymentcryptojava/security/BatchReconciliationCipher.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Batch Reconciliation Cipher. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import javax.crypto.Cipher;
0003: public class BatchReconciliationCipher { public Cipher cipher() throws Exception { return Cipher.getInstance("AES/ECB"); } }
```

### `src/main/java/com/arq/legacypaymentcryptojava/security/LegacyEnvelopeCipher.java`

- Why this file matters: `live-code` file with expectation `must_find`.
- Detailed summary: Runtime business module contributing to Legacy Envelope Cipher. It is executable/live in the assembled repository.
- Key constructs: positive surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: import javax.crypto.Cipher;
0003: public class LegacyEnvelopeCipher { public Cipher cipher() throws Exception { return Cipher.getInstance("DESede/ECB/PKCS5Padding"); } }
```

### `src/main/java/com/arq/legacypaymentcryptojava/security/LegacyPasswordFactory.java`

- Why this file matters: `live-code` file with expectation `may_find_review`.
- Detailed summary: Runtime business module contributing to Legacy Password Factory. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.legacypaymentcryptojava.security;
0002: import javax.crypto.SecretKeyFactory;
0003: public class LegacyPasswordFactory { public SecretKeyFactory factory() throws Exception { return SecretKeyFactory.getInstance("PBEWithMD5AndDES"); } }
```

### `src/main/java/com/arq/legacypaymentcryptojava/security/SecureEnvelopeCipher.java`

- Why this file matters: `live-code` file with expectation `must_not_find`.
- Detailed summary: Runtime business module contributing to Secure Envelope Cipher. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: package com.arq.legacypaymentcryptojava.security;
0002: import javax.crypto.Cipher;
0003: public class SecureEnvelopeCipher { public Cipher cipher() throws Exception { return Cipher.getInstance("AES/GCM/NoPadding"); } }
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `5013`
- Synthetic filler / inflation LOC: `3520`
- Synthetic filler ratio: `70.22%`

| category | LOC |
| --- | ---: |
| live business code | 1215 |
| live config | 3 |
| tests | 104 |
| docs | 11 |
| scripts | 1 |
| fixtures | 0 |
| vendor/generated | 132 |
| synthetic filler / inflation content | 3520 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `LegacyEnvelopeCipher.java`
  module: `Quantum`
  expected rule/finding family: `DESede/ECB/PKCS5Padding`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~DESede/ECB/PKCS5Padding
- path: `BatchReconciliationCipher.java`
  module: `Quantum`
  expected rule/finding family: `AES/ECB`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: resolvedValue~AES/ECB

### must_not_find

- path: `docs/migration-guide.md`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`
- path: `SecureEnvelopeCipher.java`
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

- `LegacyEnvelopeCipher.java`: resolvedValue~`DESede/ECB/PKCS5Padding`
- `BatchReconciliationCipher.java`: resolvedValue~`AES/ECB`

Explainability failure definition:

- A finding exists on the expected path, but the declared explainability fields are missing or do not match the scenario contract.

## 15. FP/FN Risk Notes

- False positives are most likely on docs, tests, fixtures, and generated output that contain scary-looking examples.
- Strict failures: any `must_find` miss, any `must_not_find` hit, any explainability miss on a matched expected path, and any ref-state mismatch.
- Review-needed results: INFO/inventory-only spillover on protected negatives and regex-only spillover without scenario contract coverage.
- Current run already demonstrated this risk: verdict=`PASS_WITH_NOISE`.

## 16. Realism Justification

- Why this repo is not a toy snippet: it includes runtime surfaces, build/test/smoke commands, and enough adjacent docs/config/tests to model customer-shaped maintenance reality.
- What makes it feel real: contains a non-trivial amount of live business code; includes meaningful automated test surfaces; build/test/smoke contracts execute successfully; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `3/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Quantum weak crypto patterns in legacy Java payment utilities.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\legacy-payment-crypto-java\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
