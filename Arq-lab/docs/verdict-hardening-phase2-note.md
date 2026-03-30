# Verdict Hardening Phase 2 Note

## Current flow

- `tooling/comparator.py` performs all expectation matching and verdict assignment.
- There is no explicit normalization stage before matching; `actual_findings` are compared as-is.
- Expected positives are matched by path plus loose signal hints (`ruleKey`, `resolvedValue`, `queryFamily`, `detectionSource`, `findingKind`), then ref-state is checked afterward.
- Quantum explainability is evaluated in a second pass, but the current explainability matcher treats missing values as acceptable and therefore does not block regex-only matches.
- Unmatched findings on an expected path are mostly dropped on the floor; only some regex-only Quantum findings are collected, and that collection does not currently change the verdict.
- `tooling/report_renderer.py` aggregates `mustFindMissing`, `mustNotFindViolations`, `extraFindings`, `explainabilityFailures`, and `refStateFailures`, but it does not surface same-surface noise or a strong verdict reason model.

## Weak points

- Same-surface extra findings disappear when one finding on the same path satisfies the expected contract.
- Multi-scan duplicates are not normalized, so scan-plan repeats can look like extra findings once noise accounting is tightened.
- `unexpectedRegexOnlyFindings` is mostly decorative today; scenarios can still land as `PASS`.
- Quantum explainability expectations are not strict enough because missing `resolvedValue`, `queryFamily`, `resolutionScope`, and `detectionSource` can still pass the matcher.
- Clean pass versus noisy pass is not explicit enough for audit use.

## Planned changes

- Add a lightweight normalization stage in `tooling/comparator.py` to collapse scan-plan duplicates while keeping distinct rules/signals visible.
- Split unmatched findings into deterministic buckets:
  - same-surface extra finding
  - same-file different signal
  - totally unexpected finding
  - review-only noise
  - regex-only unexpected finding
- Promote noise buckets into verdict computation so a clean pass is only emitted when there is truly no unexpected residue.
- Make Quantum explainability expectations strict enough that regex-only hits cannot satisfy semantic-required expectations.
- Extend scenario and aggregate reports with verdict class, verdict reason, noise counts, and noise breakdown without breaking dossier generation.
