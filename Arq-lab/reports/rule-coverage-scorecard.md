# Rule Coverage Scorecard

## Guardian

- raw exercised distinct rules: `98` / `226` (`43.36%`)
- surfaced exercised distinct rules: `98` / `226` (`43.36%`)
- expected_positive_exercised: `92`
- noisy_only_exercised: `0`
- mixed_exercised: `6`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `0`
- regex_only_only_exercised: `98`
- never_exercised: `128`

## Quantum

- raw exercised distinct rules: `245` / `805` (`30.43%`)
- surfaced exercised distinct rules: `245` / `805` (`30.43%`)
- expected_positive_exercised: `209`
- noisy_only_exercised: `4`
- mixed_exercised: `32`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `0`
- regex_only_only_exercised: `207`
- never_exercised: `560`

## Top Noisy Rule Hotspots

| Rule Key | Module | Bucket | Noisy Score | Distinct Scenarios |
| --- | --- | --- | ---: | ---: |
| `quantum.arq-q-0246-python` | `quantum` | `mixed_exercised` | `28` | `3` |
| `guardian.generic-api-key` | `guardian` | `mixed_exercised` | `12` | `27` |
| `quantum.arq-q-0248-python` | `quantum` | `mixed_exercised` | `12` | `6` |
| `quantum.arq-q-0408-csharp` | `quantum` | `mixed_exercised` | `12` | `3` |
| `guardian.private-key` | `guardian` | `mixed_exercised` | `10` | `13` |
| `quantum.arq-q-0531-csharp` | `quantum` | `mixed_exercised` | `10` | `1` |
| `quantum.arq-q-0263-python` | `quantum` | `mixed_exercised` | `8` | `3` |
| `quantum.arq-q-0435-csharp` | `quantum` | `mixed_exercised` | `8` | `3` |
| `quantum.arq-q-0449-csharp` | `quantum` | `mixed_exercised` | `8` | `5` |
| `quantum.arq-q-0247-python` | `quantum` | `mixed_exercised` | `6` | `3` |
| `quantum.arq-q-0291-python` | `quantum` | `mixed_exercised` | `6` | `2` |
| `quantum.arq-q-0425-csharp` | `quantum` | `noisy_only_exercised` | `6` | `2` |
| `quantum.arq-q-0245-python` | `quantum` | `mixed_exercised` | `4` | `2` |
| `quantum.arq-q-0252-python` | `quantum` | `mixed_exercised` | `4` | `2` |
| `quantum.arq-q-0405-csharp` | `quantum` | `noisy_only_exercised` | `4` | `2` |
| `quantum.arq-q-0406-csharp` | `quantum` | `mixed_exercised` | `4` | `2` |
| `quantum.arq-q-0442-csharp` | `quantum` | `mixed_exercised` | `4` | `1` |
| `quantum.arq-q-0444-csharp` | `quantum` | `mixed_exercised` | `4` | `1` |
| `quantum.arq-q-0468-csharp` | `quantum` | `mixed_exercised` | `4` | `4` |
| `quantum.arq-q-0013-java` | `quantum` | `mixed_exercised` | `3` | `9` |
