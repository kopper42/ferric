# Appendix: Git Integration

Supporting guidance for `docs/agentic-workflow-v1.md` §12.

## When to Commit

- After each verified task: `git add -A && git commit -m "<scope>: <short description>"`.
- After phase-exit approval: optionally squash per-task commits into one phase commit before merging.

## Commit Message Structure

- Prefer conventional commit prefixes: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`.
- Summarize task objective + verified outcome, not a file-by-file list.

## Relation to Verification

- A task is complete when verification passes (`docs/agentic-workflow-v1.md` §9) and the task is committed (or staged per explicit team policy).
- Do not commit code that fails verification.

## CI Integration

- If CI runs on the repository, treat CI failure as failed verification for the last committed task.
- Do not mark the task complete until CI passes unless team policy explicitly allows an exception.
