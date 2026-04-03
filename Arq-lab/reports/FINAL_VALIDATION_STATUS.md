# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `0`
- `FAIL_FN`: `22`
- `FAIL_FP`: `0`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `77`
- `PASS_WITH_NOISE`: `10`

## Verdict Proofs
- `PASS_WITH_NOISE` proof summary: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-summary.md`
- `PASS_WITH_NOISE` proof report: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-scenario-report.md`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `109` / `109` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `G-V1-COV-101` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `G-V1-COV-102` / `PASS_WITH_NOISE`: 4 unexpected/noisy finding(s) remained after matching (same-file-different-signal=4)
- `G-V1-COV-103` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `G-V1-COV-104` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `G-V1-COV-105` / `FAIL_FN`: 2 expected finding(s) were not detected at all
- `Q-V3-CS-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1, regex-only=1)
- `Q-V3-COV-101` / `FAIL_FN`: 6 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `Q-V3-COV-102` / `FAIL_FN`: 3 expected finding(s) were not detected at all; 8 unexpected/noisy finding(s) remained after matching (same-file-different-signal=8, regex-only=8)
- `Q-V3-COV-103` / `FAIL_FN`: 17 expected finding(s) were not detected at all; 9 unexpected/noisy finding(s) remained after matching (same-file-different-signal=9, regex-only=9)
- `Q-V3-COV-104` / `FAIL_FN`: 23 expected finding(s) were not detected at all; 11 unexpected/noisy finding(s) remained after matching (same-file-different-signal=11, regex-only=11)
- `Q-V3-COV-105` / `FAIL_FN`: 20 expected finding(s) were not detected at all
- `Q-V3-COV-106` / `FAIL_FN`: 30 expected finding(s) were not detected at all
- `Q-V3-COV-107` / `FAIL_FN`: 29 expected finding(s) were not detected at all; 15 unexpected/noisy finding(s) remained after matching (same-file-different-signal=15, regex-only=15)
- `Q-V3-COV-108` / `FAIL_FN`: 30 expected finding(s) were not detected at all
- `Q-V4-COV-101` / `FAIL_FN`: 12 expected finding(s) were not detected at all; 5 unexpected/noisy finding(s) remained after matching (same-file-different-signal=5, regex-only=5)
- `Q-V4-COV-102` / `FAIL_FN`: 16 expected finding(s) were not detected at all; 11 unexpected/noisy finding(s) remained after matching (same-file-different-signal=11, regex-only=10)
- `Q-V4-COV-103` / `FAIL_FN`: 4 expected finding(s) were not detected at all
- `Q-V4-COV-104` / `FAIL_FN`: 29 expected finding(s) were not detected at all; 19 unexpected/noisy finding(s) remained after matching (same-file-different-signal=19, regex-only=18)
- `Q-V6-COV-101` / `FAIL_FN`: 16 expected finding(s) were not detected at all
- `M-V8-003` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-005` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-007` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
- `M-V8-009` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=3)
- `M-V8-010` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1)
- `M-V8-011` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
- `M-V8-012` / `PASS_WITH_NOISE`: 4 unexpected/noisy finding(s) remained after matching (totally-unexpected=4, regex-only=3)
- `M-V8-COV-101` / `FAIL_FN`: 10 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `M-V8-COV-102` / `FAIL_FN`: 9 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `M-V8-COV-103` / `FAIL_FN`: 15 expected finding(s) were not detected at all
- `M-V8-COV-104` / `FAIL_FN`: 12 expected finding(s) were not detected at all
- `M-V8-COV-105` / `FAIL_FN`: 12 expected finding(s) were not detected at all
- `M-V8-COV-106` / `FAIL_FN`: 10 expected finding(s) were not detected at all
