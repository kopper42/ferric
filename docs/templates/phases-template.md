# Agentic Development Phases

AI agents: Use this file only to determine phase order, active phase, and Definition of Done (DoD). Do not place execution task checklists here.

See:

- `docs/agentic-workflow-v1.md` for updated three-level hierarchy (PHASES → stateful SLICES → per-slice TASKS), state-machine, and execution rules.
- `docs/phases-agent-guide.md` for guidance on PHASES.md and SLICES.md.

## Instructions for humans/agents

- Copy this template to `PHASES.md` at repository root and replace placeholders.
- Use tri-state markers: `[-]` for the single active phase, `[x]` for completed, `[ ]` for future. Exactly one `[-]`.
- Every phase must include a clear, testable DoD referencing slices in `SLICES.md`.
- Link contracts by path; avoid duplicating large specs. `SLICES.md` owns per-phase slice inventory and state.

## Active Phase Convention

Each phase uses one of three markers:

- `[ ]` — Todo: planned but not yet started.
- `[-]` — Active: currently being worked on. **Exactly one** phase should have `[-]`.
- `[x]` — Done: completed and verified.

If zero or more than one phase has `[-]`, agents will ask the human for clarification.

---

## [ ] Phase 1: <Short title>

Goal: <One paragraph describing the milestone and what "done" means.>

Definition of Done:
- All slices in `SLICES.md` for this phase are `[x]` and their per-slice `TASKS.md` files archived/verified.
- Full phase verification passes (`cargo fmt --check`, `cargo clippy --all-targets --all-features -- -D warnings`, `cargo test`, `cargo build --release`).
- Material decisions (e.g. crate choices, module layout, workflow refinements) recorded in `docs/memory/index.md` via ADR or flat append.
- `SLICES.md` for this phase archived upon completion.

## [ ] Phase 2: <Short title>

Goal: <One paragraph>

Definition of Done:
- All slices in `SLICES.md` for this phase are `[x]` and their per-slice `TASKS.md` files archived/verified.
- Full phase verification passes.
- Material decisions recorded in `docs/memory/index.md`.
- `SLICES.md` for this phase archived upon completion.

<!-- Add or remove phase sections as needed. Keep each DoD testable and phase-scoped. -->
