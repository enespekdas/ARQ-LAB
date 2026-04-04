# Q-V4-COV-104 - quantum-coverage-python-c

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Python / hybrid coverage pack`
- Domain: Python crypto coverage pack C targeting remaining digest, TLS, JWT, and key-material families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-104.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-c\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `2` / `30`
- missingExpectedFindings: `28`
- mustNotFindViolations: `0`
- unexpectedFindings: `115`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `115`
- unexpectedRegexOnlyFindings: `95`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `115`
- noiseBreakdown: `sameFileDifferentSignalFindings=115, unexpectedRegexOnlyFindings=95`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 28 expected finding(s) were not detected at all; 115 unexpected/noisy finding(s) remained after matching (same-file-different-signal=115, regex-only=95)

## Normalization
- rawFindings: `145`
- normalizedFindings: `117`
- collapsedDuplicates: `28`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
