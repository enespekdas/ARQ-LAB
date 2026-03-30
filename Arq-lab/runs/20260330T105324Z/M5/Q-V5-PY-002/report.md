# Q-V5-PY-002 - data-sync-python

- Milestone: `M5`
- Module: `quantum`
- Verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `Python / worker service`
- Domain: Data sync worker pulling partner APIs and webhooks.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V5-PY-002.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M5\data-sync-python\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `0` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `8`
- sameSurfaceExtraFindings: `8`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `8`
- explainabilityFailures: `2`
- refStateFailures: `0`
- noiseCount: `8`
- noiseBreakdown: `sameSurfaceExtraFindings=8, unexpectedRegexOnlyFindings=8`
- finalVerdictReason: 2 expected finding(s) had candidates but failed semantic explainability requirements; 8 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, regex-only=8)

## Normalization
- rawFindings: `8`
- normalizedFindings: `8`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
