# Milestone Index

| Milestone | Focus | Target repos | Module emphasis |
|---|---|---:|---|
| M0 | Foundation automation + lab scaffold | 0 | both |
| M1 | Guardian realistic live surfaces | 4 | Guardian |
| M2 | Guardian history / ref-state / dedup | 3 | Guardian |
| M3 | Quantum weak crypto Java / C# | 3 | Quantum |
| M4 | Quantum weak crypto Python / Go / Node | 3 | Quantum |
| M5 | Quantum TLS / trust / config Java / Python | 3 | Quantum |
| M6 | Quantum TLS / trust / config Node / C# / config | 3 | Quantum |
| M7 | Adversarial negatives | 4 | both |
| M8 | Mixed enterprise repos | 2 | both |
| M9 | Reporting / aggregation / regression harness | 0 | both |

## Recommended execution order

- Run `M0` first.
- Then `M1` and `M2`.
- Then Quantum heavy path: `M3`, `M4`, `M5`, `M6`.
- Then `M7`.
- Then `M8`.
- Finish with `M9`.

## Rule of thumb

- Guardian: coverage + ref-state correctness
- Quantum: detection correctness + explainability + noise control
