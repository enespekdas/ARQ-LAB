# Q-V3-JAVA-004 - crypto-import-only-java

- Milestone: `M3`
- Module: `quantum`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Java / Spring Boot`
- Domain: Java request-signing module with one actionable weakness and multiple import-only traps.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-JAVA-004.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\crypto-import-only-java\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `1` / `1`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `9`
- sameSurfaceExtraFindings: `9`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `8`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `9`
- noiseBreakdown: `sameSurfaceExtraFindings=9, unexpectedRegexOnlyFindings=8`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 9 unexpected/noisy finding(s) remained after matching (same-surface-extra=9, regex-only=8)

## Normalization
- rawFindings: `10`
- normalizedFindings: `10`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
