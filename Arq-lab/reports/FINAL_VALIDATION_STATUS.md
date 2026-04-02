# FINAL VALIDATION STATUS

ARQ-SEC validation summary generated from current milestone runs.

## Verdict overview
- `FAIL_EXPLAINABILITY`: `0`
- `FAIL_FN`: `1`
- `FAIL_FP`: `0`
- `FAIL_REF_STATE`: `0`
- `INVALID_SCENARIO`: `0`
- `PASS_CLEAN`: `76`
- `PASS_WITH_NOISE`: `8`

## Verdict Proofs
- `PASS_WITH_NOISE` proof summary: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-summary.md`
- `PASS_WITH_NOISE` proof report: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\verdict-proofs\pass-with-noise-scenario-report.md`

## Strengths and gaps
- Strengths: `PASS_CLEAN` scenarios met the declared contract without residual noise.
- Noise: `PASS_WITH_NOISE` scenarios matched the contract but still emitted unexpected or review-only residue.
- Gaps: `FAIL_FN`, `FAIL_FP`, `FAIL_EXPLAINABILITY`, `FAIL_REF_STATE`, and `INVALID_SCENARIO` need follow-up.
- Dossier coverage: `85` / `85` scenarios have required dossier, manifest, and tree artifacts.

## Noisy And Failed Scenario Reasons
- `M-V8-003` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-005` / `PASS_WITH_NOISE`: 3 unexpected/noisy finding(s) remained after matching (totally-unexpected=3, regex-only=2)
- `M-V8-007` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
- `M-V8-009` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=3)
- `M-V8-010` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1)
- `M-V8-011` / `PASS_WITH_NOISE`: 5 unexpected/noisy finding(s) remained after matching (totally-unexpected=5, regex-only=4)
- `M-V8-012` / `PASS_WITH_NOISE`: 4 unexpected/noisy finding(s) remained after matching (totally-unexpected=4, regex-only=3)
- `Q-V3-CS-003` / `PASS_WITH_NOISE`: 1 unexpected/noisy finding(s) remained after matching (totally-unexpected=1, regex-only=1)
- `G-V2-HIST-016` / `FAIL_FN`: 1 expected finding(s) were not detected at all
