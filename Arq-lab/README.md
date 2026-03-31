# Arq-lab

`Arq-lab/` is the execution workspace for ARQ-SEC validation milestones.

## What this workspace contains

- `tooling/`: Python automation for repo generation, per-repo GitHub publish, ARQ application/scans, exports, comparison, and reporting
- `generated/`: generated scenario artefacts and dossier aliases
- `repositories/`: independent local git repositories materialized one repo per slug
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
- Published repositories default to `https://github.com/ARQ-Sec/<repo-slug>` unless overridden by `GIT_*` settings.
- Each materialized child repository lives under `repositories/<repo-slug>/` and keeps its own `.git/`.
- ARQ applications are created with `providerType = GENERIC_GIT`.
- The orchestration is designed to be idempotent across repeated runs.
