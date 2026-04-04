# Q-V4-COV-105 - quantum-coverage-python-d-01

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Python / hybrid coverage pack`
- Domain: Python crypto and TLS late-slice coverage pack wave 01
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-105.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-d-01\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `4` / `20`
- missingExpectedFindings: `16`
- mustNotFindViolations: `0`
- unexpectedFindings: `75`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `75`
- unexpectedRegexOnlyFindings: `61`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `75`
- noiseBreakdown: `sameFileDifferentSignalFindings=75, unexpectedRegexOnlyFindings=61`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 16 expected finding(s) were not detected at all; 75 unexpected/noisy finding(s) remained after matching (same-file-different-signal=75, regex-only=61)

## Normalization
- rawFindings: `99`
- normalizedFindings: `79`
- collapsedDuplicates: `20`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
