# G-V1-COV-110 - guardian-coverage-security

- Milestone: `M1`
- Module: `guardian`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Config / IaC / CI credential coverage bundle`
- Domain: Security and platform credential corpus covering vault handoff, secrets brokers, and admin access providers.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V1-COV-110.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-security\validation\runnability-logs`

## Scan summary
- `guardian-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `18` / `20`
- missingExpectedFindings: `2`
- mustNotFindViolations: `0`
- unexpectedFindings: `3`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `3`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `3`
- noiseBreakdown: `sameFileDifferentSignalFindings=3`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 2 expected finding(s) were not detected at all; 3 unexpected/noisy finding(s) remained after matching (same-file-different-signal=3)

## Normalization
- rawFindings: `21`
- normalizedFindings: `21`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
