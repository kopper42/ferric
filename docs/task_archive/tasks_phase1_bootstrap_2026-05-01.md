# Current Execution Tasks: Phase 1 — Bootstrap

State: PLANNING_PENDING_APPROVAL

## Execution Gate
- [ ] **USER APPROVAL**: Explicit approval in chat (`approved`, `proceed`, `execute`, or `go ahead`) is required before product implementation.

## Slice Reference
- Active slice source: `SLICES.md` (authoritative for slice state within active phase from `PHASES.md`)
- Slice objective: Create minimal `Cargo.toml`, `src/lib.rs` with a documented public API and passing tests, plus all supporting workflow documentation and tooling so the template (now named `ferric`) is immediately usable.
- Slice Definition of Done (DoD): All tasks complete and verified; slice-specific verification passes; material decisions recorded in memory (if any); TASKS.md archived upon completion.

## Binding Contracts
- `docs/agentic-workflow-v1.md` — Full document (canonical workflow rules, bootstrap §0, tri-state markers, approval gate, verification)
- `docs/cargo.md` — Cargo and verification commands
- `docs/boundaries.md` — All "Always", "Ask First", "Never" rules

## Checklist

Task markers (for **this slice only**):
- `[ ]` — Todo: planned but not started.
- `[-]` — Active: currently being worked on. **Exactly one** task should have `[-]`.
- `[x]` — Done: completed and verified.

If zero or more than one task has `[-]`, ask the human before execution.

- [-] Task 1 - Initialize dual library + binary template
  - Mode: VDD
  - Objective: Establish clean `Cargo.toml` (lib + bin), `src/lib.rs` + `src/main.rs`, update all template documents to generic form, ensure validator and full verification chain pass.
  - Inputs/Contracts: `docs/agentic-workflow-v1.md` §0 (bootstrap), `docs/cargo.md`, `docs/templates/*`
  - Files to change: `Cargo.toml`, `src/lib.rs`, `src/main.rs`, root docs (`PHASES.md`, `SLICES.md`, `TASKS.md`, `README.md`, `CHANGELOG.md`, `docs/memory/index.md`)
  - Acceptance criteria: `cargo check`, `cargo test`, `cargo fmt --check`, `cargo clippy --all-targets --all-features -- -D warnings`, `cargo run` all pass; validator --strict passes; no project-specific history remains.
  - Verification: `LC_ALL=C cargo fmt --check && cargo clippy --all-targets --all-features -- -D warnings && cargo test && python3 scripts/validate_tasks_state.py --strict` (exit 0 + "Validation PASSED" + "test result: ok")

Atomicity defaults:
- Prefer <= 2 source files changed per task.
- If expected logic is large or spans unrelated layers, split into multiple tasks.

**Note:** This `TASKS.md` is scoped to the active slice from `SLICES.md`. Completed slices are archived individually.

## Contract Fingerprint
- Contracts snapshot date: 2026-04-26
- Contract sources:
  - `docs/agentic-workflow-v1.md`
  - `docs/templates/*.md`
- Fingerprint method: Manual review of bootstrap sections
- Fingerprint value: template-v1.0-clean

## Blocked Protocol
- Blocker: <specific blocker>
- Attempts made:
  - <attempt 1>
  - <attempt 2>
- Needed input: <exact decision needed from human>

## Slice Exit Verification
- [ ] Run slice verification (as defined in `SLICES.md` for this slice).
- [ ] Mark slice complete in `SLICES.md`, archive this `TASKS.md` as `tasks_phase1_bootstrap_YYYY-MM-DD.md`.
- [ ] Generate new `TASKS.md` for next active slice from template.
- [ ] (If last slice in phase) Run full phase verification, update memory/CHANGELOG, set `PHASE_COMPLETE_PENDING_APPROVAL`.

## Approval Notes
- Allowed states: `PLANNING_PENDING_APPROVAL`, `APPROVED_FOR_EXECUTION`, `EXECUTING`, `BLOCKED_NEEDS_INPUT`, `PHASE_COMPLETE_PENDING_APPROVAL`, `PHASE_APPROVED_COMPLETE`.
- Any material plan mutation (including slice changes in `SLICES.md`) resets to `State: PLANNING_PENDING_APPROVAL` and unchecks `## Execution Gate`.
- Default autonomy is one verified task per execution cycle (see v1.md §7 for scoped autonomy policy requirement).
- See v1.md §6 and §8.3 for three-document integrity, slice precedence, and cross-file consistency rules (updated for SLICES.md).
