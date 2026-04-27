# Appendix: Session Recovery

Supporting guidance for `docs/agentic-workflow-v1.md` §12.

## When This Applies

Use this recovery flow when a new agent session starts and `TASKS.md` may contain stale in-progress state from a prior interrupted session.

## Recovery Procedure

1. Read current `State:` and last task completion status in `TASKS.md`.
2. Check for partial edits in files listed by the last unchecked/in-progress task (e.g. `git status`, `git diff --stat`).
3. Case A — no partial edits, task unchecked:
   - If `State: EXECUTING`, reset to `State: PLANNING_PENDING_APPROVAL`, uncheck gate, note interruption in Blocked Protocol, ask human before continuing.
4. Case B — partial edits exist, task unchecked:
   - Revert changes for that task's files, then follow Case A.
5. Case C — partial edits exist, task marked complete without verification proof:
   - Treat as integrity contradiction; set `State: PLANNING_PENDING_APPROVAL`, uncheck gate, revert uncommitted changes, summarize contradiction, ask human.
6. Case D — state/gate contradiction:
   - If `EXECUTING` or `APPROVED_FOR_EXECUTION` while gate is unchecked, reset to planning, uncheck gate, ask human.

## Prevention

- Teams may automate a session-start recovery check in their local harness tooling.
