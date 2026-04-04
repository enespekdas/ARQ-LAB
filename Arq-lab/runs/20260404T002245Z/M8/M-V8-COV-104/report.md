# M-V8-COV-104 - quantum-coverage-native-d

- Milestone: `M8`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `Native / mixed coverage pack`
- Domain: Mixed native coverage pack D targeting additional Kotlin, Scala, Ruby, Rust, and C-family rule families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-COV-104.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-native-d\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `18` / `30`
- missingExpectedFindings: `12`
- mustNotFindViolations: `0`
- unexpectedFindings: `1`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `1`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `1`
- noiseBreakdown: `sameFileDifferentSignalFindings=1, unexpectedRegexOnlyFindings=1`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 12 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)

## Normalization
- rawFindings: `19`
- normalizedFindings: `19`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
