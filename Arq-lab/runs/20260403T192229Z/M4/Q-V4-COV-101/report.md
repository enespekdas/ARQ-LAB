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
- cleanExpectedMatches: `6` / `20`
- missingExpectedFindings: `14`
- mustNotFindViolations: `0`
- unexpectedFindings: `80`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `80`
- unexpectedRegexOnlyFindings: `67`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `80`
- noiseBreakdown: `sameFileDifferentSignalFindings=80, unexpectedRegexOnlyFindings=67`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 14 expected finding(s) were not detected at all; 80 unexpected/noisy finding(s) remained after matching (same-file-different-signal=80, regex-only=67)

## Normalization
- rawFindings: `86`
- normalizedFindings: `86`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
