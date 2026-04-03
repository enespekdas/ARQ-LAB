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
- unexpectedFindings: `159`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `159`
- unexpectedRegexOnlyFindings: `135`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `159`
- noiseBreakdown: `sameFileDifferentSignalFindings=159, unexpectedRegexOnlyFindings=135`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 28 expected finding(s) were not detected at all; 159 unexpected/noisy finding(s) remained after matching (same-file-different-signal=159, regex-only=135)

## Normalization
- rawFindings: `161`
- normalizedFindings: `161`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
