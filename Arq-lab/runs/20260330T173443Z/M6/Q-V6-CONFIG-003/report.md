# Q-V6-CONFIG-003 - edge-gateway-config

- Milestone: `M6`
- Module: `quantum`
- Verdict: `FAIL_EXPLAINABILITY`
- Final verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `Config-heavy repo`
- Domain: Edge gateway deployment and runtime config.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-CONFIG-003.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M6\edge-gateway-config\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `1` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `2`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `2`
- noiseBreakdown: `sameSurfaceExtraFindings=1, sameFileDifferentSignalFindings=1`
- finalVerdict: `FAIL_EXPLAINABILITY`
- finalVerdictReason: 1 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=1)

## Normalization
- rawFindings: `3`
- normalizedFindings: `3`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
