# Rule Coverage Scorecard

## Guardian

- exercised distinct rules: `2` / `226` (`0.88%`)
- expected_positive_exercised: `0`
- noisy_only_exercised: `0`
- mixed_exercised: `2`
- explainability_problematic_exercised: `0`
- regex_only_only_exercised: `2`
- never_exercised: `224`

## Quantum

- exercised distinct rules: `25` / `805` (`3.11%`)
- expected_positive_exercised: `18`
- noisy_only_exercised: `2`
- mixed_exercised: `3`
- explainability_problematic_exercised: `2`
- regex_only_only_exercised: `1`
- never_exercised: `780`

## Top Noisy Rule Hotspots

| Rule Key | Module | Bucket | Noisy Score | Distinct Scenarios |
| --- | --- | --- | ---: | ---: |
| `guardian.private-key` | `guardian` | `mixed_exercised` | `10` | `13` |
| `guardian.generic-api-key` | `guardian` | `mixed_exercised` | `8` | `25` |
| `quantum.arq-q-0613-typescript` | `quantum` | `explainability_problematic_exercised` | `6` | `15` |
| `quantum.arq-q-0013-java` | `quantum` | `mixed_exercised` | `3` | `9` |
| `quantum.arq-q-0449-csharp` | `quantum` | `explainability_problematic_exercised` | `3` | `3` |
| `quantum.arq-q-0131-java` | `quantum` | `noisy_only_exercised` | `2` | `2` |
| `quantum.arq-q-0178-java` | `quantum` | `mixed_exercised` | `2` | `2` |
| `quantum.arq-q-0305-python` | `quantum` | `mixed_exercised` | `2` | `9` |
| `quantum.arq-q-0418-csharp` | `quantum` | `noisy_only_exercised` | `1` | `2` |
