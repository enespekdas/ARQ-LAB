# Generated Project Dossier - G-V2-HIST-007

## 1. Scenario Identity

- scenarioId: `G-V2-HIST-007`
- scenarioName: Guardian branch divergence and cherry-pick handling across feature and release refs.
- milestone: `M2`
- targetModule: `Guardian`
- language / stack: `TypeScript / Node`
- repoType: `mixed`
- repo local path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage`
- repo remote provider: `github`
- repo remote URL: `https://github.com/ARQ-Sec/feature-cherrypick-lineage`
- default branch: `main`
- scan modes intended for this scenario: `HEAD_SNAPSHOT, REF_HISTORY`
- branch scopes intended for this scenario: `ALL_BRANCHES, SINGLE_BRANCH`
- project-local dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\generated-project-dossier.md`
- required alias dossier path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\G-V2-HIST-007\validation\generated-project-dossier.md`
- central dossier report path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V2-HIST-007.md`

## 2. Business Context and Why This Repo Is Realistic

This scenario models `Branch divergence with feature-only secret exposure and clean main/release branches.` as a `TypeScript / Node` repository. The repo is shaped to look like something an enterprise team would actually maintain so that ARQ validation is exercised against realistic layout, runtime config, supporting docs, and test collateral rather than an isolated toy snippet.

A real customer could plausibly own this repository because it bundles the operational surfaces that usually travel with the business function: runtime code, deploy/config material, tests, scripts, and enough written collateral to resemble an actively maintained internal service or support repository. The scenario goal is `Guardian branch divergence and cherry-pick handling across feature and release refs.`.

## 3. Architecture Summary

- Major components: `__tests__, dist, docs, ops, scripts, sql, src, validation`
- Runtime role: `Branch divergence with feature-only secret exposure and clean main/release branches.`
- Config flow: `No dedicated live-config files; runtime behavior is code-driven.`
- Secret flow: `featureBranchToken.ts`
- Crypto/TLS flow if relevant: `Not a Quantum-positive scenario.`
- Test surfaces: `__tests__/audit.service.test.ts, __tests__/compliance.service.test.ts, __tests__/events.service.test.ts, __tests__/invites.service.test.ts, __tests__/partners.service.test.ts, __tests__/profiles.service.test.ts, __tests__/sessions.service.test.ts, __tests__/tokens.service.test.ts`
- Docs/vendor/generated surfaces: `README.md, dist/__tests__/audit.service.test.js, dist/__tests__/compliance.service.test.js, dist/__tests__/events.service.test.js, dist/__tests__/invites.service.test.js, dist/__tests__/partners.service.test.js, dist/__tests__/profiles.service.test.js, dist/__tests__/sessions.service.test.js, dist/__tests__/tokens.service.test.js, dist/scripts/smoke.js, dist/src/modules/audit/audit.service.js, dist/src/modules/compliance/compliance.service.js`

## 4. Full Repository Tree

Tree below covers authored project files and retained build outputs. VCS internals and dependency caches such as `.git`, `node_modules`, `target`, `obj`, `bin`, and `__pycache__` are intentionally excluded because they are tool-restored rather than scenario-authored content.

```text
feature-cherrypick-lineage
|-- __tests__
|   |-- audit.service.test.ts
|   |-- compliance.service.test.ts
|   |-- events.service.test.ts
|   |-- invites.service.test.ts
|   |-- partners.service.test.ts
|   |-- profiles.service.test.ts
|   |-- sessions.service.test.ts
|   `-- tokens.service.test.ts
|-- dist
|   |-- __tests__
|   |   |-- audit.service.test.js
|   |   |-- compliance.service.test.js
|   |   |-- events.service.test.js
|   |   |-- invites.service.test.js
|   |   |-- partners.service.test.js
|   |   |-- profiles.service.test.js
|   |   |-- sessions.service.test.js
|   |   `-- tokens.service.test.js
|   |-- scripts
|   |   `-- smoke.js
|   `-- src
|       |-- modules
|       |   |-- audit
|       |   |   `-- audit.service.js
|       |   |-- compliance
|       |   |   `-- compliance.service.js
|       |   |-- events
|       |   |   `-- events.service.js
|       |   |-- invites
|       |   |   `-- invites.service.js
|       |   |-- partner
|       |   |   `-- bootstrap
|       |   |       |-- branchLeak.js
|       |   |       `-- mainSafe.js
|       |   |-- partners
|       |   |   `-- partners.service.js
|       |   |-- profiles
|       |   |   `-- profiles.service.js
|       |   |-- sessions
|       |   |   `-- sessions.service.js
|       |   `-- tokens
|       |       `-- tokens.service.js
|       `-- server.js
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
|       `-- section-44.md
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
|       `-- runbook-44.md
|-- scripts
|   `-- smoke.ts
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
|       `-- reference-44.sql
|-- src
|   |-- modules
|   |   |-- audit
|   |   |   `-- audit.service.ts
|   |   |-- compliance
|   |   |   `-- compliance.service.ts
|   |   |-- events
|   |   |   `-- events.service.ts
|   |   |-- invites
|   |   |   `-- invites.service.ts
|   |   |-- partner
|   |   |   `-- bootstrap
|   |   |       |-- branchLeak.ts
|   |   |       `-- mainSafe.ts
|   |   |-- partners
|   |   |   `-- partners.service.ts
|   |   |-- profiles
|   |   |   `-- profiles.service.ts
|   |   |-- sessions
|   |   |   `-- sessions.service.ts
|   |   `-- tokens
|   |       `-- tokens.service.ts
|   `-- server.ts
|-- validation
|   |-- runnability-logs
|   |   |-- build-01.log
|   |   |-- build-02.log
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
|-- jest.config.cjs
|-- package-lock.json
|-- package.json
|-- README.md
`-- tsconfig.json
```

## 5. File Inventory Table

| path | classification | approx LOC | purpose | positive surface | near-real negative | protected negative | build | test | smoke |
| --- | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| .gitignore | build/deploy | 8 | Build or deployment definition shaping how .Gitignore is compiled, packaged, or released. | no | no | no | yes | yes | no |
| README.md | docs | 11 | Repository overview, local development guidance, and reviewer context. | no | no | no | no | no | no |
| __tests__/audit.service.test.ts | test | 2 | Automated test surface covering Audit.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/compliance.service.test.ts | test | 2 | Automated test surface covering Compliance.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/events.service.test.ts | test | 2 | Automated test surface covering Events.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/invites.service.test.ts | test | 2 | Automated test surface covering Invites.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/partners.service.test.ts | test | 2 | Automated test surface covering Partners.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/profiles.service.test.ts | test | 2 | Automated test surface covering Profiles.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/sessions.service.test.ts | test | 2 | Automated test surface covering Sessions.Service.Test behavior. | no | no | yes | no | yes | no |
| __tests__/tokens.service.test.ts | test | 2 | Automated test surface covering Tokens.Service.Test behavior. | no | no | yes | no | yes | no |
| dist/__tests__/audit.service.test.js | generated | 4 | Generated or derived project artifact related to Audit.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/compliance.service.test.js | generated | 4 | Generated or derived project artifact related to Compliance.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/events.service.test.js | generated | 4 | Generated or derived project artifact related to Events.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/invites.service.test.js | generated | 4 | Generated or derived project artifact related to Invites.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/partners.service.test.js | generated | 4 | Generated or derived project artifact related to Partners.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/profiles.service.test.js | generated | 4 | Generated or derived project artifact related to Profiles.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/sessions.service.test.js | generated | 4 | Generated or derived project artifact related to Sessions.Service.Test. | no | no | yes | yes | no | no |
| dist/__tests__/tokens.service.test.js | generated | 4 | Generated or derived project artifact related to Tokens.Service.Test. | no | no | yes | yes | no | no |
| dist/scripts/smoke.js | generated | 2 | Generated or derived project artifact related to Smoke. | no | no | yes | yes | no | yes |
| dist/src/modules/audit/audit.service.js | generated | 4 | Generated or derived project artifact related to Audit.Service. | no | no | yes | yes | no | no |
| dist/src/modules/compliance/compliance.service.js | generated | 4 | Generated or derived project artifact related to Compliance.Service. | no | no | yes | yes | no | no |
| dist/src/modules/events/events.service.js | generated | 4 | Generated or derived project artifact related to Events.Service. | no | no | yes | yes | no | no |
| dist/src/modules/invites/invites.service.js | generated | 4 | Generated or derived project artifact related to Invites.Service. | no | no | yes | yes | no | no |
| dist/src/modules/partner/bootstrap/branchLeak.js | generated | 4 | Generated or derived project artifact related to Branch Leak. | no | no | yes | yes | no | no |
| dist/src/modules/partner/bootstrap/mainSafe.js | generated | 4 | Generated or derived project artifact related to Main Safe. | no | no | yes | yes | no | no |
| dist/src/modules/partners/partners.service.js | generated | 4 | Generated or derived project artifact related to Partners.Service. | no | no | yes | yes | no | no |
| dist/src/modules/profiles/profiles.service.js | generated | 4 | Generated or derived project artifact related to Profiles.Service. | no | no | yes | yes | no | no |
| dist/src/modules/sessions/sessions.service.js | generated | 4 | Generated or derived project artifact related to Sessions.Service. | no | no | yes | yes | no | no |
| dist/src/modules/tokens/tokens.service.js | generated | 4 | Generated or derived project artifact related to Tokens.Service. | no | no | yes | yes | no | no |
| dist/src/server.js | generated | 9 | Generated or derived project artifact related to Server. | no | no | yes | yes | no | no |
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
| jest.config.cjs | build/deploy | 1 | Build or deployment definition shaping how Jest.Config is compiled, packaged, or released. | no | no | no | yes | yes | no |
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
| package-lock.json | build/deploy | 4770 | Build or deployment definition shaping how Package Lock is compiled, packaged, or released. | no | no | no | yes | yes | no |
| package.json | build/deploy | 8 | Build or deployment definition shaping how Package is compiled, packaged, or released. | no | no | no | yes | yes | no |
| scripts/smoke.ts | script | 1 | Executable helper script used for build, smoke, or repository validation around Smoke. | no | no | no | yes | yes | yes |
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
| src/modules/audit/audit.service.ts | live-code | 2 | Runtime business service implementing Audit.Service logic. | no | no | no | yes | yes | no |
| src/modules/compliance/compliance.service.ts | live-code | 2 | Runtime business service implementing Compliance.Service logic. | no | no | no | yes | yes | no |
| src/modules/events/events.service.ts | live-code | 2 | Runtime business service implementing Events.Service logic. | no | no | no | yes | yes | no |
| src/modules/invites/invites.service.ts | live-code | 2 | Runtime business service implementing Invites.Service logic. | no | no | no | yes | yes | no |
| src/modules/partner/bootstrap/branchLeak.ts | live-code | 1 | Runtime business module contributing to Branch Leak. | no | no | no | yes | yes | no |
| src/modules/partner/bootstrap/mainSafe.ts | live-code | 1 | Runtime business module contributing to Main Safe. | no | yes | no | yes | yes | no |
| src/modules/partners/partners.service.ts | live-code | 2 | Runtime business service implementing Partners.Service logic. | no | no | no | yes | yes | no |
| src/modules/profiles/profiles.service.ts | live-code | 2 | Runtime business service implementing Profiles.Service logic. | no | no | no | yes | yes | no |
| src/modules/sessions/sessions.service.ts | live-code | 2 | Runtime business service implementing Sessions.Service logic. | no | no | no | yes | yes | no |
| src/modules/tokens/tokens.service.ts | live-code | 2 | Runtime business service implementing Tokens.Service logic. | no | no | no | yes | yes | no |
| src/server.ts | live-code | 4 | Runtime business module contributing to Server. | no | no | no | yes | yes | no |
| tsconfig.json | build/deploy | 4 | Build or deployment definition shaping how Tsconfig is compiled, packaged, or released. | no | no | no | yes | yes | no |
| validation/branch-plan.yaml | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-absent.json | generated | 14 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-findings.json | generated | 15 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/expected-report.md | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-file-manifest.json | generated | 2690 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-project-dossier.md | generated | 789 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/generated-tree.txt | generated | 230 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/repo-metadata.json | generated | 52 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-01.log | generated | 8 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/build-02.log | generated | 12 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/runnability-logs/smoke-01.log | generated | 9 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |
| validation/runnability-logs/test-01.log | generated | 34 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/scenario.yaml | generated | 7 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | no |
| validation/smoke.yaml | generated | 2 | Machine-readable validation contract or generated audit artifact for this scenario. | no | no | yes | no | no | yes |

## 6. Positive Surfaces

- Path: `featureBranchToken.ts`
  Why it should be detected: scenario declares `feature-hotfix-secret` as a live positive surface.
  Target module: `Guardian`
  Finding family / rule family expectation: `guardian.generic-api-key`
  Head/history behavior: `head-only`
  Explainability expectation: No strict scenario-specific explainability contract beyond normal detail capture.

## 7. Near-Real Negative Surfaces

- `src/modules/partner/bootstrap/mainSafe.ts`: Path is intentionally near-real but is expected to stay clean because it is placeholder, example, masked, or otherwise non-live.

## 8. Protected Negative Surfaces

| path | classification | why protected |
| --- | --- | --- |
| __tests__/audit.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/compliance.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/events.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/invites.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/partners.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/profiles.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/sessions.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| __tests__/tokens.service.test.ts | test | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/audit.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/compliance.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/events.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/invites.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/partners.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/profiles.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/sessions.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/__tests__/tokens.service.test.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/scripts/smoke.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/audit/audit.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/compliance/compliance.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/events/events.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/invites/invites.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/partner/bootstrap/branchLeak.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/partner/bootstrap/mainSafe.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/partners/partners.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/profiles/profiles.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/sessions/sessions.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/modules/tokens/tokens.service.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| dist/src/server.js | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
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
| validation/branch-plan.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-absent.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-findings.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/expected-report.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-file-manifest.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-project-dossier.md | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/generated-tree.txt | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/repo-metadata.json | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/build-02.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/smoke-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/runnability-logs/test-01.log | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/scenario.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |
| validation/smoke.yaml | generated | Path lives in a protected negative zone and should stay clean even if the content looks suspicious. |

## 9. Branch and Commit Plan

Branches:

- `feature/customer-hotfix` tip: `efbead7f39e71a63abe51eced8404ac74d48ca7c`; diverges from `main` at `00bf9e2418f72c81371bed1d0448a488cedfa47a`
- `hotfix/cherry-picked-docs` tip: `578b9a4ef062b1d166de57744b1669bc06408c0b`; diverges from `main` at `00bf9e2418f72c81371bed1d0448a488cedfa47a`
- `main` tip: `00bf9e2418f72c81371bed1d0448a488cedfa47a`
- `release/2026.05` tip: `3601c76e3a19a1b44eaa5048b50a5ac481bc86f6`; diverges from `main` at `00bf9e2418f72c81371bed1d0448a488cedfa47a`

Commit order:

- `366e6766376ae19db519a45ef702669cacd4bedd` `c002 temporary secret on feature branch`: introduces an intended signal.
- `00bf9e2418f72c81371bed1d0448a488cedfa47a` `c001 main clean baseline`: removes or neutralizes a prior signal.
- `3601c76e3a19a1b44eaa5048b50a5ac481bc86f6` `c004 release branch clean state`: removes or neutralizes a prior signal.
- `578b9a4ef062b1d166de57744b1669bc06408c0b` `c003 feature docs chore`: adds documentation-only or noise-only collateral.
- `efbead7f39e71a63abe51eced8404ac74d48ca7c` `c003 feature docs chore`: adds documentation-only or noise-only collateral.

Expected final head/history state:

- `feature-hotfix-secret` on `featureBranchToken.ts` should behave as `head-only`.

## 10. Runnability Contract

### Build

- Command: `C:\Program Files\nodejs\npm.cmd install --silent`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\runnability-logs\build-01.log`
- Command: `C:\Program Files\nodejs\npm.cmd run build`
  Expected result: `build` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\runnability-logs\build-02.log`

### Test

- Command: `C:\Program Files\nodejs\npm.cmd test -- --runInBand`
  Expected result: `test` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\runnability-logs\test-01.log`

### Smoke

- Command: `C:\Program Files\nodejs\node.exe dist/scripts/smoke.js`
  Expected result: `smoke` step completes successfully.
  Actual result: returncode=`0`; stage state=`passed`
  Log file: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\runnability-logs\smoke-01.log`

## 11. Critical Generated Content Detail

### `README.md`

- Why this file matters: `docs` file with expectation `none`.
- Detailed summary: Repository overview, local development guidance, and reviewer context. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0002: 
0003: Branch divergence with feature-only secret exposure and clean main/release branches.
0004: 
```

### `dist/scripts/smoke.js`

- Why this file matters: `generated` file with expectation `none`.
- Detailed summary: Generated or derived project artifact related to Smoke. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`True`.
- Representative excerpt:

```text
0001: "use strict";
0002: console.log('node smoke ok');
```

### `package.json`

- Why this file matters: `build/deploy` file with expectation `none`.
- Detailed summary: Build or deployment definition shaping how Package is compiled, packaged, or released. It is non-live or protected in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`False`; protected=`False`.
- Representative excerpt:

```text
0001: {
0002:   "name": "feature-cherrypick-lineage",
0003:   "version": "1.0.0",
0004:   "private": true,
0005:   "scripts": {"build": "tsc -p tsconfig.json", "test": "jest"},
0006:   "dependencies": {"express": "^4.21.2"},
0007:   "devDependencies": {"@types/express": "^5.0.0", "@types/jest": "^29.5.14", "@types/node": "^22.13.5", "jest": "^29.7.0", "ts-jest": "^29.2.5", "typescript": "^5.8.2"}
0008: }
```

### `src/modules/partner/bootstrap/mainSafe.ts`

- Why this file matters: `live-code` file with expectation `must_not_find`.
- Detailed summary: Runtime business module contributing to Main Safe. It is executable/live in the assembled repository.
- Key constructs: negative or realism-supporting surface; near-real=`True`; protected=`False`.
- Representative excerpt:

```text
0001: export const mainBranchStatus = 'clean';
```

## 12. Line Composition and Filler Disclosure

- Total LOC considered for authored/generated project content: `9934`
- Synthetic filler / inflation LOC: `4840`
- Synthetic filler ratio: `48.72%`

| category | LOC |
| --- | ---: |
| live business code | 22 |
| live config | 0 |
| tests | 16 |
| docs | 11 |
| scripts | 1 |
| fixtures | 0 |
| vendor/generated | 253 |
| synthetic filler / inflation content | 4840 |

Inflation disclosure:

- Line targets are met partly with generated architecture docs, ops runbooks, and SQL reference files under `docs/architecture/`, `ops/playbooks/`, and `sql/reference/`.
- These filler lines are intentionally disclosed above and are not being presented as live business logic.

## 13. Expected Findings Matrix

### must_find

- path: `featureBranchToken.ts`
  module: `Guardian`
  expected rule/finding family: `guardian.generic-api-key`
  expected branch/ref behavior: `head-only`
  expected explainability behavior: No strict scenario-specific explainability contract beyond normal detail capture.

### must_not_find

- path: `mainSafe.ts`
  why finding must not appear: scenario declares this path clean despite adversarial content or naming.
  negative type: `near-real negative`
- path: `docs/branch-chore.md`
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
- What makes it feel real: build/test/smoke contracts execute successfully; models a multi-component or multi-branch enterprise layout; synthetic filler is materially visible and pulls realism down.
- What is still synthetic: line-target inflation docs/runbooks/SQL references and curated positive/negative placements are intentionally authored for validation, not copied from a customer.
- Realism score: `2/5`

## 17. Final Reviewer Summary

- What this scenario is proving: `Guardian branch divergence and cherry-pick handling across feature and release refs.`
- What it is not proving: comprehensive customer architecture fidelity beyond the declared validation contract.
- First outputs to inspect on failure: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\generated-project-dossier.md`, `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\feature-cherrypick-lineage\validation\generated-file-manifest.json`, comparison artifacts under the latest `runs/` directory, and the persisted runnability logs referenced above.
