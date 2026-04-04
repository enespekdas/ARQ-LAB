# FINAL DECISION

MINIMAL_RECOVERY_PATH_EXISTS

- Truthful Quantum coverage regressed from `293 / 805` to `239 / 805`.
- Surfaced coverage regressed from `309 / 805` to `251 / 805`.
- Raw coverage regressed from `391 / 805` to `251 / 805`.
- `raw_only_not_surfaced = 0` is not a real win by itself because `48` previous raw-only rules disappeared entirely.
- `107` previously surfaced Quantum rules are no longer surfaced.
- `116` never-exercised rules are tied to scenarios that emit no signal at all.
- `438` never-exercised rules are tied to scenarios that emit neighboring Quantum signals, which points beyond pure lab shaping.
- The biggest losses cluster in Python coverage bundles `Q-V4-COV-101..108` and Java/C# version-sliced coverage bundles.
- Guardian and frozen85 stayed intact, so the blocker is isolated to Quantum campaign strategy and Quantum applicability/detection limits.
- There is a small recovery path: restore overwritten Quantum bundle identities first, then escalate the remaining language clusters as external engine dependencies.
