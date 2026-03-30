# M-V8-002 - infra-app-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `FAIL_EXPLAINABILITY`
- Final verdict: `FAIL_EXPLAINABILITY`
- Verdict class: `FAIL_EXPLAINABILITY`
- Stack: `App + infra + CI`
- Domain: Infra-heavy app repository with hotfix and release branch.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-002.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M8\infra-app-mixed-repo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- cleanExpectedMatches: `3` / `4`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `2`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `2`
- noiseBreakdown: `sameSurfaceExtraFindings=1, sameFileDifferentSignalFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdict: `FAIL_EXPLAINABILITY`
- finalVerdictReason: 1 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=1, regex-only=1)

## Normalization
- rawFindings: `14`
- normalizedFindings: `6`
- collapsedDuplicates: `8`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
