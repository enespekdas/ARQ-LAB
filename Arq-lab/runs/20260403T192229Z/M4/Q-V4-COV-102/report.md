# Q-V4-COV-102 - quantum-coverage-python-b

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Python / hybrid coverage pack`
- Domain: Python crypto coverage pack B extending TLS wrappers, kwargs passthrough, and legacy inventory families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-102.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-b\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `3` / `20`
- missingExpectedFindings: `17`
- mustNotFindViolations: `0`
- unexpectedFindings: `77`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `77`
- unexpectedRegexOnlyFindings: `59`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `77`
- noiseBreakdown: `sameFileDifferentSignalFindings=77, unexpectedRegexOnlyFindings=59`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 17 expected finding(s) were not detected at all; 77 unexpected/noisy finding(s) remained after matching (same-file-different-signal=77, regex-only=59)

## Normalization
- rawFindings: `80`
- normalizedFindings: `80`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
