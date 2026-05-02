# Slices for Active Phase: Phase 1 — Project Initialization

AI agents: Use this file to determine slice order within the active phase, active slice, per-slice goals/outcomes, and DoD. Do not place full task checklists here (those live in the per-slice `TASKS.md`).

See:
- `docs/agentic-workflow-v1.md` for updated three-level hierarchy, state machine, slice completion rules, and drift detection.
- `docs/phases-agent-guide.md` for guidance on adding/editing slices.
- Current `TASKS.md` for active slice execution details.

## Active Slice Convention

Each slice uses one of three markers:
- `[ ]` — Todo: planned but not yet started.
- `[-]` — Active: currently being worked on. **Exactly one** slice should have `[-]`.
- `[x]` — Done: completed and verified (tasks archived, memory updated).

If zero or more than one slice has `[-]`, agents will ask the human for clarification.

## Instructions for humans/agents
- This file tracks **only slices for the currently active phase** from `PHASES.md`.
- When the last slice completes, archive this file and generate a new one for the next phase.
- Keep per-slice DoD testable and vertically scoped (risk-bounded chunk).
- Link to relevant contracts; avoid duplicating large specs.

---

## [x] Slice 1: Bootstrap

Goal: Create minimal `Cargo.toml`, `src/lib.rs` with a documented public API and passing tests, plus all supporting workflow documentation and tooling so the template (named `ferric`) is immediately usable.

Definition of Done:
- All tasks in the corresponding `TASKS.md` (for this slice) are complete and verified.
- Slice-specific verification passes (`cargo check`, `cargo test`, `cargo fmt --check`, `cargo clippy`).
- Material decisions for this slice (if any) recorded in `docs/memory/index.md`.
- Current `TASKS.md` archived to `docs/task_archive/` upon slice completion.

<!-- Add slices as needed for the active phase only. When phase changes, archive this file and create fresh SLICES.md. Keep each DoD testable and slice-scoped. -->

## Slice Completion Notes
- On slice completion: mark `[x]`, archive current `TASKS.md`, generate new `TASKS.md` for next `[-]` slice, update this file.
- Full phase gate (memory review, changelog, final archive) triggers only when all slices here are `[x]`.
