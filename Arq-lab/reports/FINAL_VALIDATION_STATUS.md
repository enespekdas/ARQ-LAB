# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `2`
- `FAIL_FN`: `0`
- `FAIL_FP`: `0`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `36`
- `PASS_WITH_NOISE`: `23`

## Verdict Proofs
- `PASS_WITH_NOISE` proof summary: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-summary.md`
- `PASS_WITH_NOISE` proof report: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-scenario-report.md`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `61` / `61` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `Q-V3-JAVA-001` / `PASS_WITH_NOISE`: 15 unexpected/noisy finding(s) remained after matching (same-surface-extra=11, totally-unexpected=1, review-only=3, regex-only=14)
- `Q-V3-JAVA-002` / `PASS_WITH_NOISE`: 12 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, totally-unexpected=1, review-only=3, regex-only=11)
- `Q-V3-CS-003` / `PASS_WITH_NOISE`: 10 unexpected/noisy finding(s) remained after matching (same-surface-extra=5, totally-unexpected=5, regex-only=8)
- `Q-V3-JAVA-004` / `PASS_WITH_NOISE`: 8 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, regex-only=8)
- `Q-V3-JAVA-005` / `PASS_WITH_NOISE`: 8 unexpected/noisy finding(s) remained after matching (same-surface-extra=8, regex-only=8)
- `Q-V3-JAVA-006` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (same-surface-extra=3, regex-only=3)
- `Q-V3-CS-004` / `FAIL_EXPLAINABILITY`: 1 expected finding(s) had candidates but failed semantic explainability requirements; 2 unexpected/noisy finding(s) remained after matching (same-surface-extra=2)
- `Q-V4-PY-001` / `PASS_WITH_NOISE`: 9 unexpected/noisy finding(s) remained after matching (same-surface-extra=9, regex-only=9)
- `Q-V4-TS-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1)
- `Q-V4-PY-004` / `PASS_WITH_NOISE`: 6 unexpected/noisy finding(s) remained after matching (same-surface-extra=6, regex-only=6)
- `Q-V4-PY-005` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (same-surface-extra=3, regex-only=3)
- `Q-V5-PY-002` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
- `Q-V5-PY-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
- `Q-V6-CS-002` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `Q-V6-CONFIG-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `Q-V6-TS-002` / `FAIL_EXPLAINABILITY`: 1 expected finding(s) had candidates but failed semantic explainability requirements; 1 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, regex-only=1)
- `Q-V6-CS-003` / `PASS_WITH_NOISE`: 2 unexpected/noisy finding(s) remained after matching (same-file-different-signal=2)
- `M-V8-001` / `PASS_WITH_NOISE`: 28 unexpected/noisy finding(s) remained after matching (same-surface-extra=4, same-file-different-signal=24, regex-only=28)
- `M-V8-002` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `M-V8-003` / `PASS_WITH_NOISE`: 55 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=24, totally-unexpected=3, review-only=27, regex-only=54)
- `M-V8-004` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `M-V8-005` / `PASS_WITH_NOISE`: 55 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, same-file-different-signal=24, totally-unexpected=3, review-only=27, regex-only=54)
- `M-V8-006` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
- `M-V8-007` / `PASS_WITH_NOISE`: 57 unexpected/noisy finding(s) remained after matching (same-surface-extra=1, totally-unexpected=5, review-only=51, regex-only=56)
- `M-V8-008` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (same-file-different-signal=1)
