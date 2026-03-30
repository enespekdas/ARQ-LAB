# M-V8-002 - infra-app-mixed-repo

- Milestone: `M8`
- Module: `both`
- Verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
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
- cleanExpectedMatches: `2` / `4`
- missingExpectedFindings: `1`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `1`
- explainabilityFailures: `1`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdictReason: 1 expected finding(s) were not detected at all; 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)

## Normalization
- rawFindings: `8`
- normalizedFindings: `4`
- collapsedDuplicates: `4`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
