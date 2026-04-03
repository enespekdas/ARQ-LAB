# Rule Coverage Scorecard

## Guardian

- raw exercised distinct rules: `184` / `226` (`81.42%`)
- surfaced exercised distinct rules: `184` / `226` (`81.42%`)
- expected_positive_exercised: `175`
- noisy_only_exercised: `0`
- mixed_exercised: `9`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `0`
- regex_only_only_exercised: `184`
- never_exercised: `42`

## Quantum

- raw exercised distinct rules: `391` / `805` (`48.57%`)
- surfaced exercised distinct rules: `309` / `805` (`38.39%`)
- expected_positive_exercised: `209`
- noisy_only_exercised: `16`
- mixed_exercised: `84`
- explainability_problematic_exercised: `0`
- raw_only_not_surfaced: `82`
- regex_only_only_exercised: `210`
- never_exercised: `414`

## Top Noisy Rule Hotspots

| Rule Key | Module | Bucket | Noisy Score | Distinct Scenarios |
| --- | --- | --- | ---: | ---: |
| `quantum.arq-q-0260-python` | `quantum` | `mixed_exercised` | `296` | `9` |
| `quantum.arq-q-0253-python` | `quantum` | `mixed_exercised` | `284` | `7` |
| `quantum.arq-q-0281-python` | `quantum` | `mixed_exercised` | `284` | `7` |
| `quantum.arq-q-0265-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0267-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0280-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0299-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0324-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0343-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0364-python` | `quantum` | `noisy_only_exercised` | `70` | `6` |
| `quantum.arq-q-0266-python` | `quantum` | `mixed_exercised` | `68` | `6` |
| `quantum.arq-q-0300-python` | `quantum` | `mixed_exercised` | `68` | `6` |
| `quantum.arq-q-0325-python` | `quantum` | `mixed_exercised` | `68` | `6` |
| `quantum.arq-q-0344-python` | `quantum` | `mixed_exercised` | `68` | `6` |
| `quantum.arq-q-0363-python` | `quantum` | `mixed_exercised` | `68` | `6` |
| `quantum.arq-q-0246-python` | `quantum` | `mixed_exercised` | `30` | `4` |
| `quantum.arq-q-0248-python` | `quantum` | `mixed_exercised` | `22` | `6` |
| `guardian.generic-api-key` | `guardian` | `mixed_exercised` | `16` | `28` |
| `quantum.arq-q-0168-java` | `quantum` | `mixed_exercised` | `14` | `2` |
| `quantum.arq-q-0169-java` | `quantum` | `mixed_exercised` | `14` | `2` |
