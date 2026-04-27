# Current Execution Tasks: <Phase Name> — <Active Slice Name>

State: PLANNING_PENDING_APPROVAL

## Execution Gate
- [ ] **USER APPROVAL**: Explicit approval in chat (`approved`, `proceed`, `execute`, or `go ahead`) is required before product implementation.

## Slice Reference
- Active slice source: `SLICES.md` (authoritative for slice state within active phase from `PHASES.md`)
- Slice objective: <Copied from SLICES.md>
- Slice Definition of Done (DoD): <Copied from SLICES.md>

## Binding Contracts
- `<path>` - `<section or rule id>` - <how this constrains the current slice>

## Checklist
Task markers (for **this slice only**):
- `[ ]` — Todo: planned but not started.
- `[-]` — Active: currently being worked on. **Exactly one** task should have `[-]`.
- `[x]` — Done: completed and verified.

If zero or more than one task has `[-]`, ask the human before execution.

- [-] Task 1 - <Short title>
  - Mode: <TDD or VDD>
  - Objective: <single concrete outcome>
  - Inputs/Contracts: <path + section/rule id>
  - Files to change: `<file1>`, `<file2>`
  - Acceptance criteria: <observable success conditions>
  - Verification: `LC_ALL=C cargo check` (verify exit code 0 and a line containing "Finished" in output)

Atomicity defaults:
- Prefer <= 2 source files changed per task.
- If expected logic is large or spans unrelated layers, split into multiple tasks.

**Note:** This `TASKS.md` is scoped to the active slice from `SLICES.md`. Completed slices are archived individually.

## Contract Fingerprint
- Contracts snapshot date: <YYYY-MM-DD>
- Contract sources:
  - `<path-or-id>`
  - `<path-or-id>`
- Fingerprint method: <mtime/checksum/manual versioning>
- Fingerprint value: <computed value>

## Blocked Protocol
- Blocker: <specific blocker>
- Attempts made:
  - <attempt 1>
  - <attempt 2>
- Needed input: <exact decision needed from human>

## Slice Exit Verification
- [ ] Run slice verification (as defined in `SLICES.md` for this slice).
- [ ] Mark slice complete in `SLICES.md`, archive this `TASKS.md` as `tasks_<phase_slug>_<slice_slug>_<YYYY-MM-DD>.md`.
- [ ] Generate new `TASKS.md` for next active slice from template.
- [ ] (If last slice in phase) Run full phase verification, update memory/CHANGELOG, set `PHASE_COMPLETE_PENDING_APPROVAL`.

## Approval Notes
- Allowed states: `PLANNING_PENDING_APPROVAL`, `APPROVED_FOR_EXECUTION`, `EXECUTING`, `BLOCKED_NEEDS_INPUT`, `PHASE_COMPLETE_PENDING_APPROVAL`, `PHASE_APPROVED_COMPLETE`.
- Any material plan mutation (including slice changes in `SLICES.md`) resets to `State: PLANNING_PENDING_APPROVAL` and unchecks `## Execution Gate`.
- Default autonomy is one verified task per execution cycle (see v1.md §7 for scoped autonomy policy requirement).
- See v1.md §6 and §8.3 for three-document integrity, slice precedence, and cross-file consistency rules (updated for SLICES.md).
