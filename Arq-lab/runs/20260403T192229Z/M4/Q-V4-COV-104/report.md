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
- cleanExpectedMatches: `1` / `30`
- missingExpectedFindings: `29`
- mustNotFindViolations: `0`
- unexpectedFindings: `112`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `112`
- unexpectedRegexOnlyFindings: `95`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `112`
- noiseBreakdown: `sameFileDifferentSignalFindings=112, unexpectedRegexOnlyFindings=95`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 29 expected finding(s) were not detected at all; 112 unexpected/noisy finding(s) remained after matching (same-file-different-signal=112, regex-only=95)

## Normalization
- rawFindings: `113`
- normalizedFindings: `113`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
