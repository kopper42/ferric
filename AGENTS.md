# AGENTS.md

## Project Overview

This repository is the canonical home of a **lightweight phased agentic development workflow** for Rust projects. It defines a gated state machine (`PLANNING_PENDING_APPROVAL` → `APPROVED_FOR_EXECUTION` → `EXECUTING`), strict plan/execute separation, one-task execution cycles, drift detection, verification proof, and bootstrap from templates. See `docs/agentic-workflow-v1.md` for the normative profile (adapted from the full portable spec at `resources/AGENT_ONBOARDING_STANDALONE.md`).

## Key Reference Docs
Read these in order before making changes:

- **[docs/agentic-workflow-v1.md](./docs/agentic-workflow-v1.md)** — Canonical local behavior contract (updated three-level hierarchy: PHASES.md, SLICES.md, per-slice TASKS.md)
- **[docs/phases-agent-guide.md](./docs/phases-agent-guide.md)** — Guidance for PHASES.md and SLICES.md edits
- **[docs/templates/slices-template.md](./docs/templates/slices-template.md)** — Slice tracker template
- **[docs/templates/tasks-template.md](./docs/templates/tasks-template.md)** — Per-slice execution document shape
- **[docs/cargo.md](./docs/cargo.md)** — Verification commands
- **[docs/memory/index.md](./docs/memory/index.md)** — Active policy snapshot + ADR history (includes ADR-016)
- **[resources/AGENT_ONBOARDING_STANDALONE.md](resources/AGENT_ONBOARDING_STANDALONE.md)** — Upstream full spec (reference)
- **[CHANGELOG.md](./CHANGELOG.md)** — Completed changes only

## Global Boundaries (Summary)
- Follow `docs/agentic-workflow-v1.md` as the single local normative source (includes updated hierarchy with stateful `SLICES.md` and per-slice `TASKS.md`).
- Run per-task verification after each task (in current slice `TASKS.md`), slice verification on slice exit, and full verification at phase exit.
- Run `python3 scripts/validate_tasks_state.py --file TASKS.md --file SLICES.md --strict` before commit/slice-exit/phase exit.
- Prefer idiomatic, safe Rust.
- Use explicit approval + execution gate before implementation.
- Keep one task per execution cycle unless team policy explicitly widens autonomy.
- After substantive changes, update memory and changelog entries.
- See `docs/boundaries.md` for full safety details.

Subdirectories may contain their own `AGENTS.md` files that take precedence locally.