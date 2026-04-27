# Slices for Active Phase: <Phase Name>

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

## [-] Slice 1: <Short slice name>

Goal: <One paragraph describing the vertical chunk and success criteria.>

Definition of Done:
- All tasks in the corresponding `TASKS.md` (for this slice) are complete and verified.
- Slice-specific verification passes.
- Material decisions for this slice recorded in `docs/memory/index.md` (if applicable).
- Current `TASKS.md` archived to `docs/task_archive/tasks_<phase>_<slice>_<date>.md`.

## [ ] Slice 2: <Short slice name>

Goal: <One paragraph describing the vertical chunk and success criteria.>

Definition of Done:
- All tasks in the corresponding `TASKS.md` (for this slice) are complete and verified.
- Slice-specific verification passes.
- Material decisions for this slice recorded in `docs/memory/index.md` (if applicable).

<!-- Add slices as needed for the active phase only. When phase changes, archive this file and create fresh SLICES.md. Keep each DoD testable and slice-scoped. -->

## Slice Completion Notes
- On slice completion: mark `[x]`, archive current `TASKS.md`, generate new `TASKS.md` for next `[-]` slice, update this file.
- Full phase gate (memory review, changelog, final archive) triggers only when all slices here are `[x]`.
