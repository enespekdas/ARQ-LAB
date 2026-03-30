# Q-V6-TS-001 - customer-portal-node-tls

- Milestone: `M6`
- Module: `quantum`
- Verdict: `FAIL_EXPLAINABILITY`
- Final verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `TypeScript / Node`
- Domain: Customer portal calling billing and profile APIs.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-TS-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M6\customer-portal-node-tls\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `1` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1`
- finalVerdict: `FAIL_EXPLAINABILITY`
- finalVerdictReason: 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1)

## Normalization
- rawFindings: `2`
- normalizedFindings: `2`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
