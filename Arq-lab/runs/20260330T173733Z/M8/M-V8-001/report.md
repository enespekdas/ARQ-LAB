# M-V8-001 - internal-platform-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `FAIL_EXPLAINABILITY`
- Final verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `Java + Node + Python monorepo`
- Domain: Internal platform monorepo with multiple tech stacks.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M8\internal-platform-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `5` / `6`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `32`
- sameSurfaceExtraFindings: `8`
- sameFileDifferentSignalFindings: `24`
- unexpectedRegexOnlyFindings: `29`
- mayFindReview: `0`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `32`
- noiseBreakdown: `sameSurfaceExtraFindings=8, sameFileDifferentSignalFindings=24, unexpectedRegexOnlyFindings=29`
- finalVerdict: `FAIL_EXPLAINABILITY`
- finalVerdictReason: 1 expected finding(s) had candidates but failed semantic explainability requirements; 32 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, same-file-different-signal=24, regex-only=29)

## Normalization
- rawFindings: `40`
- normalizedFindings: `37`
- collapsedDuplicates: `3`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
