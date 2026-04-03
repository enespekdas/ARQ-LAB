# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `0`
- `FAIL_FN`: `41`
- `FAIL_FP`: `0`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `78`
- `PASS_WITH_NOISE`: `11`

## Verdict Proofs
- `PASS_WITH_NOISE` proof summary: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-summary.md`
- `PASS_WITH_NOISE` proof report: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-scenario-report.md`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `130` / `130` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `M-V8-009` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=3)
- `M-V8-010` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1)
- `M-V8-011` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
- `M-V8-012` / `PASS_WITH_NOISE`: 4 unexpected/noisy finding(s) remained after matching (totally-unexpected=4, regex-only=3)
- `M-V8-COV-101` / `FAIL_FN`: 7 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `M-V8-COV-102` / `FAIL_FN`: 11 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `M-V8-COV-103` / `FAIL_FN`: 11 expected finding(s) were not detected at all; 5 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=4)
- `M-V8-COV-104` / `FAIL_FN`: 13 expected finding(s) were not detected at all; 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2, regex-only=2)
- `M-V8-COV-105` / `FAIL_FN`: 12 expected finding(s) were not detected at all
- `M-V8-COV-106` / `FAIL_FN`: 16 expected finding(s) were not detected at all; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2)
- `M-V8-COV-107` / `FAIL_FN`: 14 expected finding(s) were not detected at all
- `M-V8-COV-108` / `FAIL_FN`: 11 expected finding(s) were not detected at all
- `M-V8-COV-109` / `FAIL_FN`: 8 expected finding(s) were not detected at all
- `G-V1-COV-101` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `G-V1-COV-102` / `PASS_WITH_NOISE`: 4 unexpected/noisy finding(s) remained after matching (same-file-different-signal=4)
- `G-V1-COV-103` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `G-V1-COV-104` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `G-V1-COV-105` / `FAIL_FN`: 2 expected finding(s) were not detected at all
- `G-V1-COV-107` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `G-V1-COV-108` / `FAIL_FN`: 1 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `G-V1-COV-109` / `FAIL_FN`: 1 expected finding(s) were not detected at all; 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `G-V1-COV-110` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `Q-V3-CS-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1, regex-only=1)
- `Q-V3-COV-101` / `FAIL_FN`: 8 expected finding(s) were not detected at all; 3 unexpected/noisy finding(s) remained after matching (same-file-different-signal=3, regex-only=3)
- `Q-V3-COV-102` / `FAIL_FN`: 8 expected finding(s) were not detected at all; 30 unexpected/noisy finding(s) remained after matching (same-file-different-signal=30, regex-only=7)
- `Q-V3-COV-103` / `FAIL_FN`: 16 expected finding(s) were not detected at all; 15 unexpected/noisy finding(s) remained after matching (same-file-different-signal=15, regex-only=3)
- `Q-V3-COV-104` / `FAIL_FN`: 24 expected finding(s) were not detected at all; 18 unexpected/noisy finding(s) remained after matching (same-file-different-signal=18, regex-only=7)
- `Q-V3-COV-105` / `FAIL_FN`: 24 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `Q-V3-COV-106` / `FAIL_FN`: 30 expected finding(s) were not detected at all
- `Q-V3-COV-107` / `FAIL_FN`: 29 expected finding(s) were not detected at all; 19 unexpected/noisy finding(s) remained after matching (same-file-different-signal=19, regex-only=2)
- `Q-V3-COV-108` / `FAIL_FN`: 30 expected finding(s) were not detected at all
- `Q-V3-COV-109` / `FAIL_FN`: 20 expected finding(s) were not detected at all
- `Q-V3-COV-110` / `FAIL_FN`: 18 expected finding(s) were not detected at all; 6 unexpected/noisy finding(s) remained after matching (same-file-different-signal=6)
- `Q-V3-COV-111` / `FAIL_FN`: 3 expected finding(s) were not detected at all
- `Q-V3-COV-112` / `FAIL_FN`: 20 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1, regex-only=1)
- `Q-V3-COV-113` / `FAIL_FN`: 20 expected finding(s) were not detected at all
- `Q-V3-COV-114` / `FAIL_FN`: 20 expected finding(s) were not detected at all
- `Q-V3-COV-115` / `FAIL_FN`: 13 expected finding(s) were not detected at all
- `Q-V4-COV-101` / `FAIL_FN`: 11 expected finding(s) were not detected at all; 81 unexpected/noisy finding(s) remained after matching (same-file-different-signal=81, regex-only=67)
- `Q-V4-COV-102` / `FAIL_FN`: 17 expected finding(s) were not detected at all; 114 unexpected/noisy finding(s) remained after matching (same-file-different-signal=114, regex-only=96)
- `Q-V4-COV-103` / `FAIL_FN`: 12 expected finding(s) were not detected at all
- `Q-V4-COV-104` / `FAIL_FN`: 29 expected finding(s) were not detected at all; 155 unexpected/noisy finding(s) remained after matching (same-file-different-signal=155, regex-only=138)
- `Q-V4-COV-105` / `FAIL_FN`: 17 expected finding(s) were not detected at all; 70 unexpected/noisy finding(s) remained after matching (same-file-different-signal=70, regex-only=61)
- `Q-V4-COV-106` / `FAIL_FN`: 6 expected finding(s) were not detected at all; 164 unexpected/noisy finding(s) remained after matching (same-file-different-signal=164, regex-only=164)
- `Q-V4-COV-107` / `FAIL_FN`: 3 expected finding(s) were not detected at all; 127 unexpected/noisy finding(s) remained after matching (same-file-different-signal=127, regex-only=127)
- `Q-V4-COV-108` / `FAIL_FN`: 10 expected finding(s) were not detected at all; 258 unexpected/noisy finding(s) remained after matching (same-file-different-signal=258, regex-only=258)
- `Q-V4-COV-109` / `FAIL_FN`: 7 expected finding(s) were not detected at all
- `Q-V6-COV-101` / `FAIL_FN`: 11 expected finding(s) were not detected at all; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1)
- `Q-V6-COV-102` / `FAIL_FN`: 1 expected finding(s) were not detected at all
- `M-V8-003` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-005` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-007` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
