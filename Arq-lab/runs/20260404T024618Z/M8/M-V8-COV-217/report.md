# M-V8-COV-217 - quantum-precision-tsql-sqlserver-2000-to-sqlserver-2022-01

- Milestone: `M8`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Native / mixed precision coverage pack`
- Domain: tsql version-sliced precision coverage pack (SQLServer 2000-to-SQLServer 2022) wave 01
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-217.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-precision-tsql-sqlserver-2000-to-sqlserver-2022-01\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `2` / `5`
- missingExpectedFindings: `3`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameFileDifferentSignalFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 3 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)

## Normalization
- rawFindings: `3`
- normalizedFindings: `3`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
