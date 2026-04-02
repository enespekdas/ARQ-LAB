# Guardian Rule Coverage

- Active rules: `226`
- Exercised distinct rules: `2` / `226` (`0.88%`)
- expected_positive_exercised: `0`
- noisy_only_exercised: `0`
- mixed_exercised: `2`
- explainability_problematic_exercised: `0`
- regex_only_only_exercised: `2`
- never_exercised: `224`

| Rule Key | Bucket | Scenarios | Expected | Noise | Explainability | Regex Only | Hybrid |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `guardian.generic-api-key` | `mixed_exercised` | `26` | `41` | `8` | `0` | `89` | `0` |
| `guardian.private-key` | `mixed_exercised` | `13` | `10` | `10` | `0` | `42` | `0` |
