# Q-V4-COV-101 - quantum-coverage-python-a

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Python / hybrid coverage pack`
- Domain: Python crypto coverage pack A spanning hashlib, HMAC, secrets, JWT, and key-material rule families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-COV-101.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-python-a\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `8` / `20`
- missingExpectedFindings: `12`
- mustNotFindViolations: `0`
- unexpectedFindings: `79`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `79`
- unexpectedRegexOnlyFindings: `67`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `79`
- noiseBreakdown: `sameFileDifferentSignalFindings=79, unexpectedRegexOnlyFindings=67`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 12 expected finding(s) were not detected at all; 79 unexpected/noisy finding(s) remained after matching (same-file-different-signal=79, regex-only=67)

## Normalization
- rawFindings: `107`
- normalizedFindings: `87`
- collapsedDuplicates: `20`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
