# G-V2-HIST-001 — payments-history-lineage

- Milestone: `M2`
- Module: `guardian`
- Verdict: `FAIL_FN`
- Stack: `Java / Spring Boot`
- Domain: Payments repo with a history-only secret on main.

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`

## Comparison
- mustFindMatched: `0` / `1`
- mustFindMissing: `1`
- mustNotFindViolations: `0`
- extraFindings: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
