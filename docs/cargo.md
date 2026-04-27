# Cargo Commands & Workflows

## Core Commands
- Check compilation: `cargo check`
- Build: `cargo build` or `cargo build --release`
- Run: `cargo run -- [args]`
- Test: `cargo test`
  - Specific test: `cargo test test_name`
  - With output: `cargo test -- --nocapture`
  - Single threaded (for non-deterministic tests): `cargo test -- --test-threads=1`
- Format: `cargo fmt`
- Lint: `cargo clippy --all-targets --all-features -- -D warnings`
- Full verification (run this before PRs/tasks):  
  ```bash
  python3 scripts/validate_tasks_state.py --file TASKS.md --strict && \
  cargo fmt --check && \
  cargo clippy --all-targets --all-features -- -D warnings && \
  cargo test && \
  cargo build --release
  ```

## Per-Task vs Phase-Exit Verification

- **Per-task (fast)**: `LC_ALL=C cargo check` — verifies compilation without producing artifacts. Use during task execution cycles (see `docs/agentic-workflow-v1.md` §9.1).
- **Phase exit (full)**: The full verification chain below — run only at phase completion or before merging.

## Commit Workflow

- **After each verified task**: `git add -A && git commit -m "<scope>: <short description>"` — creates a clean checkpoint per atomic change.
- **After phase completion**: Optionally squash per-task commits into a single phase commit before merging to the main branch.
- **Message structure**: Prefer conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`). Summarize *what* changed and *why*, not every file touched.
- **Rule**: Do not commit code that fails `cargo check`.

## Pre-commit Hook

- Repository-managed hook script: `.githooks/pre-commit`
- The hook runs `python3 scripts/validate_tasks_state.py --file TASKS.md --strict`.
- In a git repo, install by copying/symlinking `.githooks/pre-commit` to `.git/hooks/pre-commit` and making it executable.

## Documentation & Maintenance
- Generate docs: `cargo doc --open`
- Update dependencies: `cargo update`
- Check outdated crates: `cargo outdated` (if `cargo-outdated` is installed)
- Audit vulnerabilities: `cargo audit`
- Check licenses: `cargo deny check licenses`

## Dependency Change Rules
- Add or change dependencies intentionally in `Cargo.toml` (do not add crates casually while editing code).
- Prefer `cargo add <crate>` and `cargo add <crate> -F <feature>` when introducing new dependencies/features.
- New crates require approval and should be recorded in `docs/crates.md`.
- Keep feature flags minimal; avoid broad/default-heavy features unless needed.
- When dependency changes are made, document the rationale in PR/task notes.

## Workspace Commands (if using workspaces)
- Build everything: `cargo build --workspace`
- Test everything: `cargo test --workspace`

**Rule**: Never commit code that fails per-task verification (`cargo check`). Full verification is required before merging or phase exit, not after every commit.
