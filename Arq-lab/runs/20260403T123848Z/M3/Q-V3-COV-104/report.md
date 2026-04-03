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
- unexpectedFindings: `18`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `18`
- unexpectedRegexOnlyFindings: `7`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `18`
- noiseBreakdown: `sameFileDifferentSignalFindings=18, unexpectedRegexOnlyFindings=7`
- finalVerdict: `FAIL_FN`
- finalVerdictReason: 24 expected finding(s) were not detected at all; 18 unexpected/noisy finding(s) remained after matching (same-file-different-signal=18, regex-only=7)

## Normalization
- rawFindings: `19`
- normalizedFindings: `19`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
