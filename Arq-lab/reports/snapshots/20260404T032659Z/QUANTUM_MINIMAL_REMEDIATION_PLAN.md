# QUANTUM MINIMAL REMEDIATION PLAN

This plan is intentionally capped at three small, high-yield actions. It does not propose another large breadth wave.

## Action 1

- action: freeze existing `Q-V3-COV-*`, `Q-V4-COV-*`, and `M-V8-COV-*` IDs and restore the pre-regression bundles behind those IDs; move experimental/version-sliced bundles to new IDs
- rationale: current regression is dominated by overwritten bundle identity, not by lack of scenarios
- expected net truthful exact gain: `+54` (restore truthful from `239` back to previous `293` if the overwritten covered set is recovered)
- measurement: rerun only affected M3/M4/M8 milestones, then recompute `counted-covered-rules.md` and exact surfaced set diff vs `20260403T162500Z`

## Action 2

- action: add a pre-admission applicability smoke gate for new Quantum coverage bundles and reject any bundle that produces zero raw signal for all of its expected rule keys
- rationale: 116 current never-exercised rules sit in scenarios that produce no Quantum signal at all
- expected net truthful exact gain: `0` immediate, but it prevents further artificial regression and stops dead bundles from displacing previously covered IDs
- measurement: before a scenario enters the suite, require `expected_raw_hits > 0` for at least one targeted rule or keep it out of the counted campaign set

## Action 3

- action: raise an external engine/backend triage dossier for the 438 rules that are expected in scenarios already producing neighboring Quantum signals but never fire themselves
- rationale: this is the smallest path that can unlock the current ceiling without pretending ARQ-LAB alone can solve it
- expected net truthful exact gain: `unknown without backend`, but candidate pool is `438` rules
- measurement: pick one deterministic repro per dominant language cluster (C#, Python, Java, config), verify raw fire/no-fire at the exact rule key, then track surfaced delta after backend fixes land
