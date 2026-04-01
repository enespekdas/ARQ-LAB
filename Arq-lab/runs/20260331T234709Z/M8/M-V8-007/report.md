# M-V8-007 - workspace-history-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Polyrepo-style workspace with shared libs and protected-negative surfaces`
- Domain: Workspace repo with one history-only secret, active app misuse, and multiple protected-negative generated surfaces.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-007.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\workspace-history-mixed-repo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- cleanExpectedMatches: `3` / `3`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `57`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `56`
- mayFindReview: `51`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `57`
- noiseBreakdown: `sameSurfaceExtraFindings=1, totallyUnexpectedFindings=5, reviewOnlyFindings=51, unexpectedRegexOnlyFindings=56`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 57 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, totally-unexpected=5, review-only=51, regex-only=56)

## Normalization
- rawFindings: `183`
- normalizedFindings: `68`
- collapsedDuplicates: `115`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
