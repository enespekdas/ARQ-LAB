# M-V8-001 - internal-platform-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Java + Node + Python monorepo`
- Domain: Internal platform monorepo with multiple tech stacks.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\internal-platform-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `6` / `6`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `28`
- sameSurfaceExtraFindings: `4`
- sameFileDifferentSignalFindings: `24`
- unexpectedRegexOnlyFindings: `28`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `28`
- noiseBreakdown: `sameSurfaceExtraFindings=4, sameFileDifferentSignalFindings=24, unexpectedRegexOnlyFindings=28`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 28 unexpected/noisy finding(s) remained after matching (same-surface-extra=4, same-file-different-signal=24, regex-only=28)

## Normalization
- rawFindings: `37`
- normalizedFindings: `34`
- collapsedDuplicates: `3`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
