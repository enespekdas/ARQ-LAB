# M-V8-002 - infra-app-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `App + infra + CI`
- Domain: Infra-heavy app repository with hotfix and release branch.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-002.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\infra-app-mixed-repo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- cleanExpectedMatches: `4` / `4`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameFileDifferentSignalFindings=1`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)

## Normalization
- rawFindings: `14`
- normalizedFindings: `6`
- collapsedDuplicates: `8`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
