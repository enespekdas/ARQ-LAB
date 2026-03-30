# Q-V6-CONFIG-003 - edge-gateway-config

- Milestone: `M6`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Config-heavy repo`
- Domain: Edge gateway deployment and runtime config.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-CONFIG-003.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M6\edge-gateway-config\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `0` / `2`
- missingExpectedFindings: `1`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `1`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdictReason: 1 expected finding(s) were not detected at all; 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)

## Normalization
- rawFindings: `1`
- normalizedFindings: `1`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
