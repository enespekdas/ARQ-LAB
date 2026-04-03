# M-V8-012 - verify-mesh-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Java + Node + Python mixed monorepo`
- Domain: Mixed monorepo with Python verify=False, Java weak crypto, TS safe wrappers, and heavy vendor/generated surfaces.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-012.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\verify-mesh-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `3` / `3`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `4`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `3`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `4`
- noiseBreakdown: `totallyUnexpectedFindings=4, unexpectedRegexOnlyFindings=3`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 4 unexpected/noisy finding(s) remained after matching (totally-unexpected=4, regex-only=3)

## Normalization
- rawFindings: `11`
- normalizedFindings: `7`
- collapsedDuplicates: `4`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
