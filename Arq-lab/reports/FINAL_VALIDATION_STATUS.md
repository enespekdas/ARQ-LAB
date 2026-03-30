# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `10`
- `FAIL_FN`: `3`
- `FAIL_FP`: `1`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `11`
- `PASS_WITH_NOISE`: `0`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `25` / `25` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `Q-V3-JAVA-001` / `FAIL_EXPLAINABILITY`: 3 expected finding(s) had candidates but failed semantic explainability requirements; 3 unexpected/noisy finding(s) remained after matching (same-surface-extra=3, regex-only=3)
- `Q-V3-JAVA-002` / `FAIL_EXPLAINABILITY`: 2 expected finding(s) had candidates but failed semantic explainability requirements; 3 unexpected/noisy finding(s) remained after matching (same-surface-extra=3, regex-only=3)
- `Q-V3-CS-003` / `FAIL_EXPLAINABILITY`: 3 expected finding(s) had candidates but failed semantic explainability requirements; 11 unexpected/noisy finding(s) remained after matching (same-surface-extra=11, regex-only=11)
- `Q-V4-PY-001` / `FAIL_EXPLAINABILITY`: 2 expected finding(s) had candidates but failed semantic explainability requirements; 14 unexpected/noisy finding(s) remained after matching (same-surface-extra=14, regex-only=14)
- `Q-V4-GO-002` / `FAIL_FN`: 2 expected finding(s) were not detected at all
- `Q-V4-TS-003` / `FAIL_EXPLAINABILITY`: 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
- `Q-V5-JAVA-001` / `FAIL_EXPLAINABILITY`: 2 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2, regex-only=2)
- `Q-V5-PY-002` / `FAIL_EXPLAINABILITY`: 2 expected finding(s) had candidates but failed semantic explainability requirements; 8 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, regex-only=8)
- `Q-V6-TS-001` / `FAIL_EXPLAINABILITY`: 2 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2, regex-only=2)
- `Q-V6-CS-002` / `FAIL_EXPLAINABILITY`: 1 expected finding(s) had candidates but failed semantic explainability requirements; 5 unexpected/noisy finding(s) remained after matching (same-surface-extra=5, regex-only=5)
- `Q-V6-CONFIG-003` / `FAIL_FN`: 1 expected finding(s) were not detected at all; 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
- `N-V7-TESTS-003` / `FAIL_FP`: 23 must-not-find violation(s) hit protected or declared-clean surfaces
- `M-V8-001` / `FAIL_EXPLAINABILITY`: 3 expected finding(s) had candidates but failed semantic explainability requirements; 29 unexpected/noisy finding(s) remained after matching (same-surface-extra=6, same-file-different-signal=23, regex-only=29)
- `M-V8-002` / `FAIL_FN`: 1 expected finding(s) were not detected at all; 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
