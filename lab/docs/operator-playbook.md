# Operator playbook

## Recommended sequence

1. `cp .env.example .env` and fill ARQ credentials.
2. Start AI agent in a workspace whose root can create `Arq-lab/`.
3. Give the agent:
   - `prompts/00_master_agent_brief.md`
   - `prompts/01_M0_foundation_automation.md`
4. Validate tooling and dry-run output.
5. Then run milestones in order:
   - M1
   - M2
   - M3
   - M4
   - M5
   - M6
   - M7
   - M8
   - M9

## Suggested operator discipline

- Keep one `Arq-lab/` workspace.
- Commit `Arq-lab/` separately from `ARQ-SEC`.
- After each milestone, inspect:
  - generated repos
  - validation manifests
  - raw scan exports
  - comparison reports
- If a milestone partially fails because a service is down, preserve raw error logs and continue only after infrastructure is healthy.

## What to review manually after each milestone

- repo realism
- build/test/smoke validity
- expected vs actual comparison sanity
- whether `mustNotFind` surfaces were truly protected
- whether Quantum explainability assertions make sense
