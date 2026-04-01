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
- unexpectedFindings: `25`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `24`
- unexpectedRegexOnlyFindings: `25`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `25`
- noiseBreakdown: `sameSurfaceExtraFindings=1, sameFileDifferentSignalFindings=24, unexpectedRegexOnlyFindings=25`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 25 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=24, regex-only=25)

## Normalization
- rawFindings: `34`
- normalizedFindings: `31`
- collapsedDuplicates: `3`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
