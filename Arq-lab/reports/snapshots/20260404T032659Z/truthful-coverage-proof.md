# Truthful Coverage Proof

- snapshot: `20260404T032659Z`
- scenario_count: `198`

## Guardian

- before: surfaced `184 / 226` (`81.42%`), truthful `184 / 226` (`81.42%`)
- now: surfaced `226 / 226` (`100.0%`), truthful `226 / 226` (`100.0%`)
- expected_positive_exercised: `218`
- mixed_exercised: `8`
- noisy_only_exercised: `0`
- raw_only_not_surfaced: `0`
- explainability_problematic_exercised: `0`
- never_exercised: `0`

## Quantum

- before: surfaced `309 / 805` (`38.39%`), truthful `293 / 805` (`36.4%`)
- now: surfaced `251 / 805` (`31.18%`), truthful `239 / 805` (`29.69%`)
- expected_positive_exercised: `182`
- mixed_exercised: `57`
- noisy_only_exercised: `12`
- raw_only_not_surfaced: `0`
- explainability_problematic_exercised: `0`
- never_exercised: `554`

## Acceptance Gate

- counted coverage excludes `noisy_only_exercised`, `raw_only_not_surfaced`, `never_exercised`, and `explainability_problematic_exercised`
- counted truthful coverage = `expected_positive_exercised + mixed_exercised`
