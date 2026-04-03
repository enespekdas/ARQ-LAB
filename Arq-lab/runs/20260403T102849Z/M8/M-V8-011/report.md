# M-V8-011 - workspace-shared-libs-mixed

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Workspace-style mixed repo with history-only secret and shared libs`
- Domain: Workspace repo with history-only secret, safe docs, and mixed crypto helpers across shared libs and apps.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-011.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\workspace-shared-libs-mixed\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- cleanExpectedMatches: `3` / `3`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `5`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `4`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `5`
- noiseBreakdown: `totallyUnexpectedFindings=5, unexpectedRegexOnlyFindings=4`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)

## Normalization
- rawFindings: `32`
- normalizedFindings: `12`
- collapsedDuplicates: `20`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
