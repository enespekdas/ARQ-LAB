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
- cleanExpectedMatches: `0` / `25`
- missingExpectedFindings: `25`
- mustNotFindViolations: `0`
- unexpectedFindings: `14`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `14`
- unexpectedRegexOnlyFindings: `3`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `14`
- noiseBreakdown: `sameFileDifferentSignalFindings=14, unexpectedRegexOnlyFindings=3`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 25 expected finding(s) were not detected at all; 14 unexpected/noisy finding(s) remained after matching (same-file-different-signal=14, regex-only=3)

## Normalization
- rawFindings: `14`
- normalizedFindings: `14`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
