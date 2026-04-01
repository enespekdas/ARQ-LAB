# M-V8-008 - branch-hotfix-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_CLEAN`
- Final verdict: `PASS_CLEAN`
- Verdict class: `PASS_CLEAN`
- Stack: `Mixed repo with branches, infra overlays, and dormant examples`
- Domain: Infra-heavy mixed repo with branch-only TLS hotfix, dormant examples, active runtime misuse, and generated noise.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-008.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\branch-hotfix-mixed-repo\validation\runnability-logs`

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
- rawFindings: `14`
- normalizedFindings: `6`
- collapsedDuplicates: `8`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
