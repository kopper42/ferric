# Agent Guide: Extending PHASES.md and SLICES.md

Use this guide for roadmap edits to `PHASES.md` (phases) or `SLICES.md` (slices within active phase). For execution behavior and full hierarchy, see `docs/agentic-workflow-v1.md` (updated for three-level model).

## Active Phase Detection

Each phase in `PHASES.md` uses one of three markers:

- `[ ]` — Todo: planned but not yet started.
- `[-]` — Active: currently being worked on. **Exactly one** phase should have this marker.
- `[x]` — Done: completed and verified.

The active phase is the single `[-]` marker. If zero or multiple `[-]` markers exist, ask the human before planning.

## Terminology (updated hierarchy)

- **Phase** (`PHASES.md`): milestone with Goal and testable DoD. Tri-state markers.
- **Slice** (`SLICES.md`): risk-bounded vertical chunk *within the active phase only*. Stateful with tri-state markers, goals, per-slice DoD. Exactly one active slice.
- **Task** (`TASKS.md`): atomic checklist item under the *active slice only*. Includes Mode, Objective, Inputs/Contracts, Files to change, Acceptance, Verification. Per-slice `TASKS.md` is archived on slice completion.

Relationship: one phase has one or more slices (tracked in `SLICES.md`); each slice has one or more tasks (in its dedicated `TASKS.md`).

## Scope boundaries (updated)

- `PHASES.md`: phase order, Goals, high-level DoD, links to contracts. No slice details.
- `SLICES.md`: slices for the *active phase only*, tri-state markers, per-slice goals/DoD/outcomes. Authoritative for slice state.
- `TASKS.md`: state, gate, tasks *for the current active slice only*, binding contracts, verification, blocked protocol. No phase-wide or multi-slice content.
- Do not duplicate full checklists across files.

## When to use this guide

Use this document when:
- Adding, reordering, or modifying phases in `PHASES.md`
- Adding or completing slices in `SLICES.md` for the current active phase
- Updating DoD language to remain testable and vertically scoped
- Archiving a completed `SLICES.md` and creating a fresh one for the next phase

## Common operations

### Adding a new phase
1. Add it at the bottom of `PHASES.md` with `[ ]` marker.
2. Do not create `SLICES.md` for it yet.
3. When it becomes active, create `SLICES.md` from `docs/templates/slices-template.md`.

### Adding a slice to the active phase
1. Add a new section in `SLICES.md` with `[ ]` (or `[-]` if it should become immediately active).
2. Update the active slice marker so exactly one `[-]` exists.
3. Generate or update `TASKS.md` from the template for that slice.

### Completing a slice
1. Mark all tasks `[x]` in the current `TASKS.md`.
2. Run slice verification.
3. Mark the slice `[x]` in `SLICES.md`.
4. Archive the current `TASKS.md` to `docs/task_archive/`.
5. If there are more slices, mark the next one `[-]` and create fresh `TASKS.md`.
6. If this was the last slice, trigger phase completion (see `docs/agentic-workflow-v1.md` §11).

### Completing a phase
See `docs/agentic-workflow-v1.md` §11 for the full phase completion gate (memory, changelog, archive `SLICES.md`, generate new `SLICES.md` + `TASKS.md` for next phase, set `PHASE_COMPLETE_PENDING_APPROVAL`).

## Best practices
- Keep each phase/slice DoD **testable** and narrowly scoped.
- Prefer vertical slices (end-to-end for a small capability) over broad horizontal layers.
- Update this guide if the hierarchy or process changes materially.
- Always run `python3 scripts/validate_tasks_state.py --strict` after changes to PHASES, SLICES, or TASKS.

See `docs/agentic-workflow-v1.md` for the authoritative rules, especially the Quick Reference, hierarchy (§5–6), drift rules (§8), and completion gates (§11).
