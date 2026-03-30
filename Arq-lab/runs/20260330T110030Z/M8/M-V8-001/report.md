# M-V8-001 - internal-platform-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `Java + Node + Python monorepo`
- Domain: Internal platform monorepo with multiple tech stacks.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M8\internal-platform-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `3` / `6`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `29`
- sameSurfaceExtraFindings: `6`
- sameFileDifferentSignalFindings: `23`
- unexpectedRegexOnlyFindings: `29`
- explainabilityFailures: `3`
- refStateFailures: `0`
- noiseCount: `29`
- noiseBreakdown: `sameSurfaceExtraFindings=6, sameFileDifferentSignalFindings=23, unexpectedRegexOnlyFindings=29`
- finalVerdictReason: 3 expected finding(s) had candidates but failed semantic explainability requirements; 29 unexpected/noisy finding(s) remained after matching (same-surface-extra=6, same-file-different-signal=23, regex-only=29)

## Normalization
- rawFindings: `35`
- normalizedFindings: `32`
- collapsedDuplicates: `3`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
