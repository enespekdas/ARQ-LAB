# M-V8-002 — infra-app-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `FAIL_FN`
- Stack: `App + infra + CI`
- Domain: Infra-heavy app repository with hotfix and release branch.

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- mustFindMatched: `3` / `4`
- mustFindMissing: `1`
- mustNotFindViolations: `0`
- extraFindings: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`

## Runnability
- build: `failed`
- test: `failed`
- smoke: `passed`
