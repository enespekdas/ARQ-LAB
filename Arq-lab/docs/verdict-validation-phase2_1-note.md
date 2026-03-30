# Verdict Validation Phase 2.1

## Audit summary

- Confirmed risk: `PASS_WITH_NOISE` existed in comparator code but did not have a persisted proof artifact in the repo. This is now closed with a deterministic proof fixture and generated report outputs.
- Confirmed risk: regression coverage was too narrow for the hardened verdict contract. This is now closed with a 20-test suite that locks PASS/FAIL/noise/explainability/runnability/reporting behavior.
- Confirmed harness reliability gap: long `--all` runs could lose ARQ authentication mid-run and fail with `401`. This was a harness issue, not a detector issue, and is now mitigated by a single re-auth retry in the ARQ client.
- False alarm: dossier generation, generated manifest/tree outputs, report dossier links, and runnability log root chaining were not broken by Phase 2 hardening. Phase 2.1 kept them intact.

## PASS_WITH_NOISE proof

- Proof summary: `reports/verdict-proofs/pass-with-noise-summary.md`
- Proof report: `reports/verdict-proofs/pass-with-noise-scenario-report.md`
- Proof comparison: `reports/verdict-proofs/pass-with-noise-comparison.json`

The proof fixture demonstrates all of the following at once:

- `cleanExpectedMatches = 1`
- `missingExpectedFindings = 0`
- `mustNotFindViolations = 0`
- `explainabilityFailures = 0`
- `noiseCount = 1`
- `sameSurfaceExtraFindings = 1`
- `unexpectedRegexOnlyFindings = 1`
- `finalVerdict = PASS_WITH_NOISE`

This proves that the verdict class is reachable without weakening explainability strictness or hiding noise.

## Validation result after Phase 2.1

- `PASS_CLEAN = 11`
- `PASS_WITH_NOISE = 0`
- `FAIL_FN = 3`
- `FAIL_FP = 1`
- `FAIL_EXPLAINABILITY = 10`
- `FAIL_REF_STATE = 0`
- `INVALID_SCENARIO = 0`

The live scenario pack still produces zero `PASS_WITH_NOISE` cases. This is acceptable because all currently noisy real scenarios also carry a stronger failure reason (`FAIL_EXPLAINABILITY` or `FAIL_FP`). The proof fixture exists to show that `PASS_WITH_NOISE` is real and guarded, not dead code.

## Remaining product gaps

- `Q-V4-GO-002`: still a real weak-hash detection gap.
- `Q-V6-CONFIG-003`: still a real Envoy `ACCEPT_UNTRUSTED` detection gap plus a separate explainability/export gap on the `.env` finding.
- `M-V8-002`: still the mixed-repo variant of the same root cause.
- `N-V7-TESTS-003`: still a real FP/noise problem on a protected negative surface.

## Commands run

- `python -m tooling.orchestrate --all`
- `python -m tooling.orchestrate --report-only`
- `python -m pytest -q tests`

All three completed successfully after the ARQ client re-auth hardening.
