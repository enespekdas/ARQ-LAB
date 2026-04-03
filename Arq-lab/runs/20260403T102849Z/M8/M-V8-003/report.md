# M-V8-003 - platform-mesh-monorepo

- Milestone: `M8`
- Module: `both`
- Verdict: `PASS_WITH_NOISE`
- Final verdict: `PASS_WITH_NOISE`
- Verdict class: `PASS_WITH_NOISE`
- Stack: `Java + Node + Python + generated/vendor monorepo`
- Domain: Enterprise mesh monorepo with apps, services, vendor bundles, openapi output, and fixture-heavy packages.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\M-V8-003.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\repositories\platform-mesh-monorepo\validation\runnability-logs`

## Scan summary
- `guardian-head-main`: `SUCCEEDED` on `main`
- `quantum-head-main`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `4` / `4`
- missingExpectedFindings: `0`
- mustNotFindViolations: `0`
- unexpectedFindings: `3`
- sameSurfaceExtraFindings: `0`
- sameFileDifferentSignalFindings: `0`
- unexpectedRegexOnlyFindings: `2`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `3`
- noiseBreakdown: `totallyUnexpectedFindings=3, unexpectedRegexOnlyFindings=2`
- finalVerdict: `PASS_WITH_NOISE`
- finalVerdictReason: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)

## Normalization
- rawFindings: `14`
- normalizedFindings: `7`
- collapsedDuplicates: `7`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
