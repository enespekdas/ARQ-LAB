# Q-V4-TS-006 - hash-destructure-node

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_EXPLAINABILITY`
- Final verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `TypeScript / Node`
- Domain: Node repo using destructured crypto helpers, alias exports, and returned object chains around createHash.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-TS-006.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\hash-destructure-node\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `0` / `1`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdict: `FAIL_EXPLAINABILITY`
- finalVerdictReason: 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)

## Normalization
- rawFindings: `1`
- normalizedFindings: `1`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
