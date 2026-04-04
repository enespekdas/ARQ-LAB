# Rule Coverage Scorecard

## Guardian

- raw exercised distinct rules: `226` / `226` (`100.0%`)
- surfaced exercised distinct rules: `226` / `226` (`100.0%`)
- expected_positive_exercised: `218`
- noisy_only_exercised: `0`
- mixed_exercised: `8`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `0`
- regex_only_only_exercised: `226`
- never_exercised: `0`

## Quantum

- raw exercised distinct rules: `251` / `805` (`31.18%`)
- surfaced exercised distinct rules: `251` / `805` (`31.18%`)
- expected_positive_exercised: `182`
- noisy_only_exercised: `12`
- mixed_exercised: `57`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `0`
- regex_only_only_exercised: `51`
- never_exercised: `554`

## Top Noisy Rule Hotspots

| Rule Key | Module | Bucket | Noisy Score | Distinct Scenarios |
| --- | --- | --- | ---: | ---: |
| `quantum.arq-q-0387-python` | `quantum` | `mixed_exercised` | `52` | `14` |
| `quantum.arq-q-0246-python` | `quantum` | `mixed_exercised` | `44` | `10` |
| `quantum.arq-q-0351-python` | `quantum` | `mixed_exercised` | `44` | `10` |
| `quantum.arq-q-0260-python` | `quantum` | `mixed_exercised` | `40` | `9` |
| `quantum.arq-q-0281-python` | `quantum` | `noisy_only_exercised` | `40` | `5` |
| `quantum.arq-q-0248-python` | `quantum` | `mixed_exercised` | `36` | `12` |
| `guardian.generic-api-key` | `guardian` | `mixed_exercised` | `22` | `31` |
| `quantum.arq-q-0418-csharp` | `quantum` | `noisy_only_exercised` | `21` | `8` |
| `quantum.arq-q-0198-java` | `quantum` | `mixed_exercised` | `20` | `2` |
| `quantum.arq-q-0199-java` | `quantum` | `mixed_exercised` | `20` | `2` |
| `quantum.arq-q-0369-python` | `quantum` | `mixed_exercised` | `20` | `8` |
| `quantum.arq-q-0375-python` | `quantum` | `mixed_exercised` | `20` | `7` |
| `quantum.arq-q-0449-csharp` | `quantum` | `mixed_exercised` | `20` | `11` |
| `quantum.arq-q-0453-csharp` | `quantum` | `mixed_exercised` | `20` | `9` |
| `quantum.arq-q-0468-csharp` | `quantum` | `mixed_exercised` | `20` | `11` |
| `quantum.arq-q-0531-csharp` | `quantum` | `mixed_exercised` | `20` | `7` |
| `quantum.arq-q-0381-python` | `quantum` | `mixed_exercised` | `16` | `6` |
| `quantum.arq-q-0435-csharp` | `quantum` | `mixed_exercised` | `16` | `8` |
| `quantum.arq-q-0247-python` | `quantum` | `mixed_exercised` | `12` | `6` |
| `quantum.arq-q-0291-python` | `quantum` | `mixed_exercised` | `12` | `6` |
