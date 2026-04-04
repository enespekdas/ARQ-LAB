# QUANTUM BLOCKER SUMMARY

- previous surfaced: `309 / 805`
- previous truthful: `293 / 805`
- current surfaced: `251 / 805`
- current truthful: `239 / 805`
- previous raw: `391 / 805`
- current raw: `251 / 805`

## Go / No-Go

- decision: `GO` only for blocker triage and minimal recovery planning
- decision: `NO-GO` for another breadth-first Quantum expansion wave

## Net Judgment

- verdict: `mixed`
- primary blocker class: `lab_gap`
- secondary blocker class: `external_backend_dependency`

## Key Proof

- raw_only_not_surfaced is `0`, but raw exercised also collapsed `391 -> 251`
- surfaced collapsed `309 -> 251`
- truthful collapsed `293 -> 239`
- lost raw rules: `155`
- lost surfaced rules: `107`
- previous raw-only rules that truly surfaced now: `34`
- previous raw-only rules that simply disappeared: `48`
- never_exercised now: `554`

## Root Cause in One Paragraph

Quantum parity looks cleaner because the exercised rule set shrank, not because the campaign truthfully surfaced the older raw-only gap. The biggest regression came from ARQ-LAB-side coverage bundle churn: reused `Q-V3-COV-*`, `Q-V4-COV-*`, and `M-V8-COV-*` scenario IDs now surface fewer exact rule keys than the accepted snapshot did, especially in Python. On top of that, a large tail of expected Quantum rules is now assigned to scenarios that either emit no signal at all or emit neighboring same-language signals without ever firing the expected rule, which is where the external engine/applicability dependency begins.

## Highest-Impact Evidence

- `Q-V4-COV-107`: lost_surfaced=35, missing_expected=20, same_file_different_signal=0, regex_only=0
- `Q-V4-COV-106`: lost_surfaced=34, missing_expected=20, same_file_different_signal=4, regex_only=0
- `Q-V4-COV-108`: lost_surfaced=27, missing_expected=18, same_file_different_signal=6, regex_only=0
- `Q-V4-COV-104`: lost_surfaced=15, missing_expected=27, same_file_different_signal=34, regex_only=0
- `Q-V4-COV-102`: lost_surfaced=17, missing_expected=17, same_file_different_signal=21, regex_only=3

## Current Classification

- scenario_yok: `0`
- scenario_var_ama_applicability_disi: `116`
- engine_detect_etmiyor: `438`
- expectation_yanlis: `0 proven`
- surfacing/matching_kaybi on never_exercised rules: `0` (rule-level parity is clean in the current snapshot)

## Residue Hotspots

- same-file-different-signal by language: `{'python': 204, 'csharp': 86, 'java': 30, 'erlang': 4, 'elixir': 4, 'cpp': 2, 'php': 2, 'rust': 2}`
- regex-only by language: `{'python': 22, 'java': 20, 'csharp': 15, 'objectivec': 12, 'cpp': 8, 'javascript': 8, 'rust': 8, 'powershell': 8}`

- previous snapshot: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\snapshots\20260403T162500Z`
- current snapshot: `C:\Users\EnesPekdas\Desktop\ARQV2\LAB\Arq-lab\reports\snapshots\20260404T032659Z`
