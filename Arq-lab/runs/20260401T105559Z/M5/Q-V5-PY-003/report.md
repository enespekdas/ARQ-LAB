# Q-V5-PY-003 - tls-usage-python

- Milestone: `M5`
- Module: `quantum`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Python / worker service`
- Domain: Python client repo with one active verify=False path and multiple dormant examples nearby.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V5-PY-003.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\tls-usage-python\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `1` / `1`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)

## Normalization
- rawFindings: `2`
- normalizedFindings: `2`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
