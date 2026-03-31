# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `0`
- `FAIL_FN`: `0`
- `FAIL_FP`: `6`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `13`
- `PASS_WITH_NOISE`: `6`

## Verdict Proofs
- `PASS_WITH_NOISE` proof summary: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-summary.md`
- `PASS_WITH_NOISE` proof report: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-scenario-report.md`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `25` / `25` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `Q-V3-JAVA-001` / `FAIL_FP`: 8 must-not-find violation(s) hit protected or declared-clean surfaces; 18 unexpected/noisy finding(s) remained after matching (same-surface-extra=13, totally-unexpected=1, review-only=4, regex-only=14)
- `Q-V3-JAVA-002` / `FAIL_FP`: 4 must-not-find violation(s) hit protected or declared-clean surfaces; 13 unexpected/noisy finding(s) remained after matching (same-surface-extra=9, totally-unexpected=1, review-only=3, regex-only=11)
- `Q-V3-CS-003` / `FAIL_FP`: 7 must-not-find violation(s) hit protected or declared-clean surfaces; 2 expected finding(s) had candidates but failed semantic explainability requirements; 29 unexpected/noisy finding(s) remained after matching (same-surface-extra=24, totally-unexpected=5, regex-only=11)
- `Q-V4-PY-001` / `FAIL_FP`: 1 must-not-find violation(s) hit protected or declared-clean surfaces; 21 unexpected/noisy finding(s) remained after matching (same-surface-extra=20, same-file-different-signal=1, regex-only=9)
- `Q-V4-TS-003` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, totally-unexpected=2)
- `Q-V5-PY-002` / `PASS_WITH_NOISE`: 12 unexpected/noisy finding(s) remained after matching (same-surface-extra=6, same-file-different-signal=6, regex-only=1)
- `Q-V5-JAVA-003` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2, regex-only=2)
- `Q-V6-CS-002` / `FAIL_FP`: 2 must-not-find violation(s) hit protected or declared-clean surfaces; 1 expected finding(s) had candidates but failed semantic explainability requirements; 7 unexpected/noisy finding(s) remained after matching (same-surface-extra=5, same-file-different-signal=2, regex-only=5)
- `Q-V6-CONFIG-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `N-V7-SAFE-004` / `FAIL_FP`: 1 must-not-find violation(s) hit protected or declared-clean surfaces
- `M-V8-001` / `PASS_WITH_NOISE`: 32 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, same-file-different-signal=24, regex-only=28)
- `M-V8-002` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=1)
