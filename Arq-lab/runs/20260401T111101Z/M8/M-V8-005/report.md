# M-V8-005 - enterprise-mesh-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Java + Node + Python + vendor/generated monorepo`
- Domain: Enterprise monorepo with apps, shared libs, vendor bundles, generated code, and protected-negative fixtures.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-005.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\enterprise-mesh-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `4` / `4`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `52`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `24`
- unexpectedRegexOnlyFindings: `51`
- mayFindReview: `24`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `52`
- noiseBreakdown: `sameSurfaceExtraFindings=1, sameFileDifferentSignalFindings=24, totallyUnexpectedFindings=3, reviewOnlyFindings=24, unexpectedRegexOnlyFindings=51`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 52 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=24, totally-unexpected=3, review-only=24, regex-only=51)

## Normalization
- rawFindings: `60`
- normalizedFindings: `56`
- collapsedDuplicates: `4`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
