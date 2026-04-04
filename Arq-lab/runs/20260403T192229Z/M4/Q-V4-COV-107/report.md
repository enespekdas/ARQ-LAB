# Q-V4-COV-107 - quantum-coverage-python-d-03

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Python / hybrid coverage pack`
- Domain: Python crypto and TLS late-slice coverage pack wave 03
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-107.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-03\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `17` / `20`
- missingExpectedFindings: `3`
- mustNotFindViolations: `0`
- unexpectedFindings: `138`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `137`
- unexpectedRegexOnlyFindings: `138`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `138`
- noiseBreakdown: `sameSurfaceExtraFindings=1, sameFileDifferentSignalFindings=137, unexpectedRegexOnlyFindings=138`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 3 expected finding(s) were not detected at all; 138 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=137, regex-only=138)

## Normalization
- rawFindings: `188`
- normalizedFindings: `155`
- collapsedDuplicates: `33`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
