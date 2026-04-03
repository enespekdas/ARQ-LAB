# Q-V3-COV-104 - quantum-coverage-csharp-b

- Milestone: `M3`
- Module: `quantum`
- Verdict: `FAIL_FN`
- Final verdict: `FAIL_FN`
- Verdict class: `FAIL_FN`
- Stack: `C# / hybrid coverage pack`
- Domain: C# crypto and TLS coverage pack B extending registration, key material, and inventory rule families.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-COV-104.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\quantum-coverage-csharp-b\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `1` / `25`
- missingExpectedFindings: `24`
- mustNotFindViolations: `0`
- unexpectedFindings: `19`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `19`
- unexpectedRegexOnlyFindings: `10`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `19`
- noiseBreakdown: `sameFileDifferentSignalFindings=19, unexpectedRegexOnlyFindings=10`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 24 expected finding(s) were not detected at all; 19 unexpected/noisy finding(s) remained after matching (same-file-different-signal=19, regex-only=10)

## Normalization
- rawFindings: `20`
- normalizedFindings: `20`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
