# Q-V4-PY-001 - notification-signer-python

- Milestone: `M4`
- Module: `quantum`
- Verdict: `FAIL_FP`
- Final verdict: `FAIL_FP`
- Verdict class: `FAIL_FP`
- Stack: `Python / FastAPI`
- Domain: Webhook signing and outbound notification auth helper.
- Dossier: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\generated-project-dossiers\Q-V4-PY-001.md`
- Persisted logs path: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\generated\M4\notification-signer-python\validation\runnability-logs`

## Scan summary
- `quantum-head`: `SUCCEEDED` on `main`

## Comparison
- cleanExpectedMatches: `2` / `2`
- missingExpectedFindings: `0`
- mustNotFindViolations: `1`
- unexpectedFindings: `21`
- sameSurfaceExtraFindings: `20`
- sameFileDifferentSignalFindings: `1`
- unexpectedRegexOnlyFindings: `9`
- mayFindReview: `0`
- explainabilityFailures: `0`
- refStateFailures: `0`
- noiseCount: `21`
- noiseBreakdown: `sameSurfaceExtraFindings=20, sameFileDifferentSignalFindings=1, unexpectedRegexOnlyFindings=9`
- finalVerdict: `FAIL_FP`
- finalVerdictReason: 1 must-not-find violation(s) hit protected or declared-clean surfaces; 21 unexpected/noisy finding(s) remained after matching (same-surface-extra=20, same-file-different-signal=1, regex-only=9)

## Normalization
- rawFindings: `24`
- normalizedFindings: `24`
- collapsedDuplicates: `0`

## Runnability
- build: `passed`
- test: `passed`
- smoke: `passed`
