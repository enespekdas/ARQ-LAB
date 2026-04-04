# M-V8-COV-105 - quantum-coverage-native-e

- Milestone: `M8`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Native / mixed coverage pack`
- Domain: Mixed native coverage pack E targeting remaining native and scripting quantum families that were still uncovered after earlier waves.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-105.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-e\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `16` / `30`
- missingExpectedFindings: `14`
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
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 14 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)

## Normalization
- rawFindings: `20`
- normalizedFindings: `17`
- collapsedDuplicates: `3`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
