# Q-V5-PY-002 - data-sync-python

- Milestone: `M5`
- Module: `quantum`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Python / worker service`
- Domain: Data sync worker pulling partner APIs and webhooks.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V5-PY-002.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M5\data-sync-python\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `2` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `12`
- sameSurfaceExtraFindings: `6`
- sameFileDifferentSignalFindings: `6`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `12`
- noiseBreakdown: `sameSurfaceExtraFindings=6, sameFileDifferentSignalFindings=6, unexpectedRegexOnlyFindings=1`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 12 unexpected/noisy finding(s) remained after matching (same-surface-extra=6, same-file-different-signal=6, regex-only=1)

## Normalization
- rawFindings: `14`
- normalizedFindings: `14`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
