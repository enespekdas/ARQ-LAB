# Q-V6-COV-101 - quantum-coverage-config

- Milestone: `M6`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Config / infra coverage pack`
- Domain: Config-heavy quantum coverage pack spanning Envoy, Nginx, Apache, SSH, kube, JVM, and OpenSSL families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V6-COV-101.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-config\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `9` / `20`
- missingExpectedFindings: `11`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `1`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `0`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameSurfaceExtraFindings=1`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 11 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1)

## Normalization
- rawFindings: `10`
- normalizedFindings: `10`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
