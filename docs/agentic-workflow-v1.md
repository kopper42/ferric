# Agentic Workflow v1 Profile

**Quick Reference** (centralized per consolidated AI reviews — terminal 2.txt + prior canvas. Canonical source for all agents/contributors.)

- **Allowed States** (exact, one only): `PLANNING_PENDING_APPROVAL` | `APPROVED_FOR_EXECUTION` | `EXECUTING` | `BLOCKED_NEEDS_INPUT` | `PHASE_COMPLETE_PENDING_APPROVAL` | `PHASE_APPROVED_COMPLETE`
- **Approval Phrases** (§3): `approved`, `proceed`, `execute`, `go ahead`. **Only these** flip the gate. Colloquial ("ok", "looks good"), emojis, or checkmarks **do not** count. If doubt, ask for one of the listed phrases. (Team policy in AGENTS.md or this Quick Ref can extend list.)
- **Markers** (tri-state, all levels): `[ ]` = todo, `[-]` = active (**exactly one** while work remains in phase/slice/task list), `[x]` = done & verified with proof.
- **Hierarchy & Authority** (ADR-016): PHASES.md (milestones + high-level DoD), SLICES.md (**authoritative** for active slice state within active phase), per-slice TASKS.md (execution details only). Disagreement on active slice → `PLANNING_PENDING_APPROVAL` + reset gate.
- **Core Rules**: One verified task/turn (default; scoped autonomy requires explicit policy in this doc or AGENTS.md). Edit *only* "Files to change" listed. Always run pre-task drift + validator. Memory mode: **flat** (default, append to index.md) unless explicitly set otherwise in TASKS header. Back-off in §9.

(Use this box for quick onboarding. Full details below.)

Concise normative profile for phased agentic development with three-level hierarchy. This file is the canonical local behavior source. For full upstream detail, see `resources/AGENT_ONBOARDING_STANDALONE.md`.

**Hierarchy (updated ADR-016):** `PHASES.md` (phases only), stateful `SLICES.md` (slices in active phase with tri-state), per-slice `TASKS.md` (tasks for current slice only). Archive/rotate after each slice. This optimizes context window while preserving safety gates.

## 0) Bootstrap (required)

If `PHASES.md`, `SLICES.md`, or `TASKS.md` is missing, empty, or wrong-phase/slice:
1. Create `PHASES.md` from `docs/templates/phases-template.md`.
2. Create `SLICES.md` from `docs/templates/slices-template.md` for the active phase.
3. Create/rewrite `TASKS.md` from `docs/templates/tasks-template.md` scoped to the active slice.
4. Set `State: PLANNING_PENDING_APPROVAL`, keep execution gate unchecked.
5. Stop and request explicit human approval.

## 1) Artifact roles (required)

- Phase roadmap (`PHASES.md`): ordered phases, Goal, testable DoD, no slice or task checklist.
- Slice tracker (`SLICES.md`): slices for the active phase only, with tri-state markers, goals, per-slice DoD.
- Execution document (`TASKS.md`): per-slice canonical source of state, gate, tasks, contracts, verification (focused on active slice only).
- Human changelog: verified outcomes.
- Project memory: decisions + ADRs.

## 2) Allowed states (required)

`State:` MUST be exactly one of:
- `PLANNING_PENDING_APPROVAL`
- `APPROVED_FOR_EXECUTION`
- `EXECUTING`
- `BLOCKED_NEEDS_INPUT`
- `PHASE_COMPLETE_PENDING_APPROVAL`
- `PHASE_APPROVED_COMPLETE`

## 3) Approval gate (required)

Product implementation is allowed only when all are true:
- explicit approval in chat (`approved`, `proceed`, `execute`, `go ahead`)
- `State: APPROVED_FOR_EXECUTION`
- execution gate checkbox is checked

Colloquial or minimal replies (e.g. "looks good", "yep", "do it", "ok", checkmark-only or emoji-only reactions) MUST NOT count as approval unless the team's written policy explicitly lists them as sufficient. If there is any doubt whether the message is approval, treat it as not approved and ask the human to reply using one of the clear phrases above (or another phrase listed in team policy). (Sourced from upstream §5.2.)

## 4) Plan/execute separation (required)

Do not implement product code in the same turn as creating or materially rewriting the plan.

Any material plan mutation (tasks/scope/verification/acceptance/files-to-change) MUST:
- set `State: PLANNING_PENDING_APPROVAL`
- uncheck execution gate
- request approval again

## 5) Phase/slice/task model (required)

**Three-level hierarchy (updated for context optimization):**
- **Phase** (`PHASES.md`): milestone with Goal + testable DoD. Tri-state markers; exactly one active phase.
- **Slice** (`SLICES.md`): risk-bounded vertical chunk within the active phase only. Stateful with tri-state markers (`[ ]`/`[-]`/`[x]`), goals/outcomes, per-slice DoD. Exactly one active slice at a time.
- **Task**: atomic checklist item under the active slice only. Each task MUST include Mode (`TDD` or `VDD`), Objective, Inputs/Contracts, Files to change, Acceptance criteria, Verification.

Sizing defaults:
- Prefer <=2 source files per task.
- Split when logic is large or spans unrelated layers.

**Markers (tri-state across all levels):**
- `[ ]` = todo (planned, not started)
- `[-]` = active (currently being worked on)
- `[x]` = done (completed and verified)

Exactly one task in the active `TASKS.md` (current slice) should be marked `[-]` at a time. If zero or multiple active tasks exist, ask the human before executing. Slice markers in `SLICES.md` follow the same exactly-one-active rule while the phase has remaining work.

When a slice completes, archive the current `TASKS.md` (as slice-specific snapshot), update `SLICES.md`, generate fresh `TASKS.md` for the next active slice.

## 6) Execution document shape (required)

Active phase in `PHASES.md` and active slice in `SLICES.md` are identified by `[-]` (todo=`[ ]`, active=`[-]`, done=`[x]`). This local tri-state rule supersedes upstream “first unchecked” examples for all three files. When documents disagree on active slice, treat `SLICES.md` as authoritative for planning and reset to `PLANNING_PENDING_APPROVAL`.

`TASKS.md` is now **per-slice only** (focused on tasks for the current active slice from `SLICES.md`). Required section order in `TASKS.md` (updated):
1. Title (includes current slice name)
2. `State: <STATE>`
3. `## Execution Gate`
4. `## Slice Reference` (points to `SLICES.md`; no full phase DoD duplication)
5. `## Binding Contracts` (slice-scoped)
6. `## Checklist` (tasks for this slice only)
7. `## Contract Fingerprint`
8. `## Blocked Protocol`
9. `## Slice Exit Verification` (lighter; full phase verification only at phase end)
10. `## Approval Notes`

Remove `## Active Slices` and phase-wide elements from `TASKS.md`. `SLICES.md` owns slice inventory, ordering, and tri-state for the active phase.

## 7) Execution cycle (required)

After approval:
1. Set `State: EXECUTING`
2. Execute the single active task marked `[-]`
3. Run pre-task drift check (paths/symbols/contracts still valid)
4. Edit only task-listed files
5. Verify with explicit success evidence
6. Mark active task complete (`[x]`) only after verified success, then mark the next task `[-]` (if any remain)
7. Optionally append changelog per policy
8. Stop and await continuation

Default autonomy: one task per turn.

**Scoped autonomy (optional, per upstream §10):** Phrases such as "keep going", "continue until the phase is complete", or "run the next N tasks" MAY authorize multiple execution cycles in one session **only** if the team has recorded that policy in the execution document, adoption profile (`AGENTS.md`), or written team standards (including any limits on N or stop conditions). Without such documentation, treat those phrases as non-binding or ask the human to confirm the default one-task-per-turn rule.

## 8) Drift/replan rules (required)

Replan + reset gate when:
- active phase (`[-]`) or active slice (`[-]` in `SLICES.md`) changed
- contracts/interfaces changed materially
- fingerprint mismatch (in `TASKS.md` or `SLICES.md`)
- missing/renamed files/symbols
- `SLICES.md` and `TASKS.md` disagree on active slice
- human requests different approach

On mismatch, do not write product code. `SLICES.md` is authoritative for slice state.

### 8.3 Execution document integrity (per upstream §6.3)
If any execution document (`TASKS.md`, `SLICES.md`) is internally inconsistent—e.g. more than one `State:` line (in TASKS), state/gate contradictions, multiple active slices in `SLICES.md`, checklist items marked complete without verification proof, or Binding Contracts clearly contradicting the Contract Fingerprint—the agent MUST NOT execute product code. Set `State: PLANNING_PENDING_APPROVAL`, uncheck the gate, summarize contradictions in Blocked Protocol (or a short bullet list), and ask the human to correct the document(s) or confirm a corrected plan. (Elevated from tasks-template.md Approval Notes.)

## 9) Verification/backoff (required)

A task cannot be `[x]` unless:
- verification exits successfully
- output contains explicit success signal

Default split:
- per-task (in current slice `TASKS.md`): `cargo check` (fast)
- slice exit: appropriate verification for the slice
- phase exit: full chain (`fmt`, `clippy`, `test`, `build`)

Signal matching defaults:
- prefer exit code 0 + explicit string
- use `LC_ALL=C`, `--color never` for deterministic output
- Rust signals: `Finished`, `test result: ok`
- automated guard: run `python3 scripts/validate_tasks_state.py --file TASKS.md --file SLICES.md --strict` before commit/slice-exit/phase-exit verification

**Back-off Policy** (concrete table per consolidated reviews):

| Failures | Action                  | Wait / Next Step                  |
|----------|-------------------------|-----------------------------------|
| 1        | Retry immediately       | Continue after verification fix   |
| 2        | Brief pause             | 1 min + human note in Blocked Protocol |
| 3        | Escalate                | Set `BLOCKED_NEEDS_INPUT`, ask one explicit question. Counter resets on successful slice exit or human unblock. |

- Cap at N=3 (policy override allowed in AGENTS.md or TASKS.md).
- Always record attempts in Blocked Protocol.
- Prefer fixing root cause over repeated retries.

## 10) Blocked protocol (required)

When blocked:
- set `State: BLOCKED_NEEDS_INPUT`
- record blocker + attempts
- ask one explicit decision question

## 11) Slice and phase completion gates (required)

**Slice completion** (when all tasks in active slice from `SLICES.md` are `[x]`):
1. Run slice verification (as defined in `SLICES.md` or current `TASKS.md`).
2. Mark active slice `[x]` in `SLICES.md`; mark next slice `[-]` if any remain.
3. Archive current `TASKS.md` to `docs/task_archive/` (name: `tasks_<phase_slug>_<slice_slug>_<YYYY-MM-DD>.md`).
4. Generate fresh `TASKS.md` from template for the new active slice.
5. Optionally append lightweight memory note (flat mode default).
6. Continue with next slice (no full phase approval needed).

**Phase completion** (when all slices in active phase are `[x]` in `SLICES.md`):
1. Run full phase verification.
2. Update memory via chosen mode:
   - `memory_mode: flat` (default): append material decisions to `docs/memory/index.md`
   - `memory_mode: layered`: use layered promotion + `docs/memory/memory-review-template.md`
   If architectural or materially binding decisions were made—non-exhaustively: new public API or wire format; security, privacy, or data-lifecycle behavior; choice of persistence or identity model; new required dependency or platform; or any choice that will constrain multiple future tasks—record a short ADR-style entry (Status, Context, Decision, Consequences; see memory-review-template.md). (From upstream §13.)
3. Finalize changelog entries (using minimum shape in CHANGELOG.md Entry Rules).
4. Archive final `SLICES.md` and last `TASKS.md`.
5. Generate new `SLICES.md` + `TASKS.md` for next phase from templates.
6. Set `State: PHASE_COMPLETE_PENDING_APPROVAL`.
7. Ask explicit approval before next phase.

This per-slice rotation keeps `TASKS.md` small and context-efficient.

## 12) Linked appendices (recommended)

- Git policy: `docs/appendix/git-integration.md`
- Session recovery: `docs/appendix/session-recovery.md`

