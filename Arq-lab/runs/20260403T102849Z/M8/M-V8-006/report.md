# M-V8-006 - control-plane-overlay-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_CLEAN`
- Final verdict: `PASS_CLEAN`
- Verdict class: `PASS_CLEAN`
- Stack: `App + infra + helm + kustomize + terraform + CI`
- Domain: Infra-heavy control-plane repo with live runtime misuse, hotfix branches, and noisy dormant overlays.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-006.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\control-plane-overlay-repo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`
- `guardian-ref-history-main`: `SUCCEEDED` on `main`
- `guardian-all-branches`: `SUCCEEDED` on `n/a`

## Comparison
- cleanExpectedMatches: `5` / `5`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `0`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `0`
- noiseBreakdown: `none`
- finalVerdict: `PASS_CLEAN`
- finalVerdictReason: all expected findings matched cleanly with no unexpected noise

## Normalization
- rawFindings: `17`
- normalizedFindings: `6`
- collapsedDuplicates: `11`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
