# G-V1-COV-108 - guardian-coverage-data

- Milestone: `M1`
- Module: `guardian`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Config / IaC / CI credential coverage bundle`
- Domain: Data platform credential corpus spanning warehouses, ETL, observability, and ingestion providers.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V1-COV-108.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-data\validation\runnability-logs`

## Scan summary
- `guardian-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `19` / `20`
- missingExpectedFindings: `1`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameFileDifferentSignalFindings=1`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 1 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)

## Normalization
- rawFindings: `20`
- normalizedFindings: `20`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
