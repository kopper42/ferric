# Ferric

Ferric is a clean, reusable starter template for Rust projects that includes a lightweight **phased agentic development workflow**.

## Quick Start

1. Fork this repository (or rename folder) and update `Cargo.toml` (change `name`, `description`, `authors`, `repository` to match your project, e.g. `ferric`).
2. Run `cargo check` to verify the baseline.
3. Follow the bootstrap instructions in [`docs/agentic-workflow-v1.md`](docs/agentic-workflow-v1.md) §0 (Bootstrap).
4. Begin with the active Phase 1 in `PHASES.md` / `SLICES.md` / `TASKS.md` (currently in `PLANNING_PENDING_APPROVAL` state).

## Workflow Overview

- **Canonical rules**: [`docs/agentic-workflow-v1.md`](docs/agentic-workflow-v1.md) (Quick Reference at top)
- **Phases**: [`PHASES.md`](PHASES.md)
- **Active slices**: [`SLICES.md`](SLICES.md)
- **Current tasks**: [`TASKS.md`](TASKS.md)
- **Validation**: `python3 scripts/validate_tasks_state.py --strict`
- **Memory**: [`docs/memory/index.md`](docs/memory/index.md)
- **Templates**: `docs/templates/`

The workflow uses strict plan/execute separation, tri-state markers (`[ ]` todo, `[-]` active, `[x]` done), explicit approval gates, and automated validation to keep development safe and context-efficient.

See [`AGENTS.md`](AGENTS.md) for agent-specific guidance and [`docs/phases-agent-guide.md`](docs/phases-agent-guide.md) for roadmap maintenance.

## License

MIT OR Apache-2.0 (see `Cargo.toml`).
