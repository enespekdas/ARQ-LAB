# G-V1-COV-102 - guardian-coverage-cloud

- Milestone: `M1`
- Module: `guardian`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Config / IaC / CI credential coverage bundle`
- Domain: Cloud and infrastructure credential corpus spanning live ops surfaces, Terraform vars, and integration runtime state.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\G-V1-COV-102.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\guardian-coverage-cloud\validation\runnability-logs`

## Scan summary
- `guardian-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `20` / `20`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `4`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `4`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `4`
- noiseBreakdown: `sameFileDifferentSignalFindings=4`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 4 unexpected/noisy finding(s) remained after matching (same-file-different-signal=4)

## Normalization
- rawFindings: `24`
- normalizedFindings: `24`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
