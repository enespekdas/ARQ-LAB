# Q-V6-TS-001 - customer-portal-node-tls

- Milestone: `M6`
- Module: `quantum`
- Verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `TypeScript / Node`
- Domain: Customer portal calling billing and profile APIs.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-TS-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M6\customer-portal-node-tls\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `0` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `2`
- sameSurfaceExtraFindings: `2`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `2`
- explainabilityFailures: `2`
- refStateFailures: `0`
- noiseCount: `2`
- noiseBreakdown: `sameSurfaceExtraFindings=2, unexpectedRegexOnlyFindings=2`
- finalVerdictReason: 2 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2, regex-only=2)

## Normalization
- rawFindings: `2`
- normalizedFindings: `2`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
