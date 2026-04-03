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
- cleanExpectedMatches: `2` / `20`
- missingExpectedFindings: `18`
- mustNotFindViolations: `0`
- unexpectedFindings: `102`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `102`
- unexpectedRegexOnlyFindings: `83`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `102`
- noiseBreakdown: `sameFileDifferentSignalFindings=102, unexpectedRegexOnlyFindings=83`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 18 expected finding(s) were not detected at all; 102 unexpected/noisy finding(s) remained after matching (same-file-different-signal=102, regex-only=83)

## Normalization
- rawFindings: `104`
- normalizedFindings: `104`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
