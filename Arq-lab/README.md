# Arq-lab

`Arq-lab/` is the execution workspace for ARQ-SEC validation milestones.

## What this workspace contains

- `tooling/`: Python automation for repo generation, Gitea sync, ARQ application/scans, exports, comparison, and reporting
- `generated/`: generated repositories per milestone
- `runs/`: raw execution artifacts per run
- `reports/`: milestone and aggregate validation reports
- `catalog/`: scenario index and milestone status files
- `validation/`: scenario-level expectations inside each generated repo

## Entry points

- `python -m tooling.orchestrate --milestone M1`
- `python -m tooling.orchestrate --all`
- `python -m tooling.orchestrate --report-only`
- `python -m tooling.orchestrate --dry-run --milestone M1`

## Notes

- Environment values are loaded from `.env` / `.env.example`.
- Gitea repositories are created as public by default.
- ARQ applications are created with `providerType = GENERIC_GIT`.
- The orchestration is designed to be idempotent across repeated runs.
