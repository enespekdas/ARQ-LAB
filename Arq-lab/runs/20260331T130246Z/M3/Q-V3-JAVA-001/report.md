# Q-V3-JAVA-001 - identity-gateway-java

- Milestone: `M3`
- Module: `quantum`
- Verdict: `FAIL_FP`
- Final verdict: `FAIL_FP`
- Verdict class: `FAIL_FP`
- Stack: `Java / Spring Boot`
- Domain: Identity gateway for sessions and partner auth.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V3-JAVA-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\identity-gateway-java\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `3` / `3`
- missingExpectedFindings: `0`
- mustNotFindViolations: `8`
- unexpectedFindings: `18`
- sameSurfaceExtraFindings: `13`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `14`
- mayFindReview: `4`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `18`
- noiseBreakdown: `sameSurfaceExtraFindings=13, totallyUnexpectedFindings=1, reviewOnlyFindings=4, unexpectedRegexOnlyFindings=14`
- finalVerdict: `FAIL_FP`
- finalVerdictReason: 8 must-not-find violation(s) hit protected or declared-clean surfaces; 18 unexpected/noisy finding(s) remained after matching (same-surface-extra=13, totally-unexpected=1, review-only=4, regex-only=14)

## Normalization
- rawFindings: `29`
- normalizedFindings: `29`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
