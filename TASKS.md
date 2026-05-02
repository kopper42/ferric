# Current Execution Tasks: Phase 2 — Add Example Features

State: PLANNING_PENDING_APPROVAL

## Execution Gate
- [ ] **USER APPROVAL**: Explicit approval in chat (`approved`, `proceed`, `execute`, or `go ahead`) is required before product implementation.

## Slice Reference
- Active slice source: `SLICES.md` (authoritative for slice state within active phase from `PHASES.md`)
- Slice objective: Extend the library with additional public APIs, improve tests, update documentation, and demonstrate full agentic workflow usage while strictly following all boundaries.
- Slice Definition of Done (DoD): New functionality added with tests; verification passes; decisions recorded in memory; TASKS.md archived.

## Binding Contracts
- `docs/agentic-workflow-v1.md` — Full document (canonical workflow rules, tri-state markers, approval gate, verification, phase/slice completion §11)
- `docs/boundaries.md` — Safety rules (no unsafe, no unwrap/todo in prod, etc.)
- `docs/coding-style.md` — Idiomatic Rust, explicit error handling
- `docs/testing.md` — Happy path + edge cases
- `docs/cargo.md` — Verification commands

## Checklist

Task markers (for **this slice only**):
- `[ ]` — Todo: planned but not started.
- `[-]` — Active: currently being worked on. **Exactly one** task should have `[-]`.
- `[x]` — Done: completed and verified.

If zero or more than one task has `[-]`, ask the human before execution.

- [-] Task 1 - Expand public API with example functionality
  - Mode: TDD
  - Objective: Add at least one additional public function with tests that demonstrates the library.
  - Inputs/Contracts: `src/lib.rs` (current greet), `docs/coding-style.md`, `docs/testing.md`
  - Files to change: `src/lib.rs`, tests if needed, docs if impacted
  - Acceptance criteria: All cargo commands and validator pass; new code follows all rules.
  - Verification: `LC_ALL=C cargo fmt --check && cargo clippy --all-targets --all-features -- -D warnings && cargo test && python3 scripts/validate_tasks_state.py --strict`

Atomicity defaults:
- Prefer <= 2 source files changed per task.
- If expected logic is large or spans unrelated layers, split into multiple tasks.

**Note:** This `TASKS.md` is scoped to the active slice from `SLICES.md`. Completed slices are archived individually.

## Contract Fingerprint
- Contracts snapshot date: 2026-05-01
- Contract sources:
  - `docs/agentic-workflow-v1.md`
  - `SLICES.md`
  - `PHASES.md`
- Fingerprint method: Manual review of active markers and verification proof
- Fingerprint value: phase2-slice1-initial

## Blocked Protocol
- Blocker: None (phase 1 bootstrap complete)
- Attempts made: N/A
- Needed input: Explicit approval to proceed with Phase 2 implementation.

## Slice Exit Verification
- [ ] Run slice verification (as defined in `SLICES.md` for this slice).
- [ ] Mark slice complete in `SLICES.md`, archive this `TASKS.md` as `tasks_phase2_add_example_features_YYYY-MM-DD.md`.
- [ ] Generate new `TASKS.md` for next active slice from template.
- [ ] (If last slice in phase) Run full phase verification, update memory/CHANGELOG, set `PHASE_COMPLETE_PENDING_APPROVAL`.

## Approval Notes
- Allowed states: `PLANNING_PENDING_APPROVAL`, `APPROVED_FOR_EXECUTION`, `EXECUTING`, `BLOCKED_NEEDS_INPUT`, `PHASE_COMPLETE_PENDING_APPROVAL`, `PHASE_APPROVED_COMPLETE`.
- Any material plan mutation (including slice changes in `SLICES.md`) resets to `State: PLANNING_PENDING_APPROVAL` and unchecks `## Execution Gate`.
- Default autonomy is one verified task per execution cycle (see v1.md §7 for scoped autonomy policy requirement).
- See v1.md §6 and §8.3 for three-document integrity, slice precedence, and cross-file consistency rules (updated for SLICES.md).
