# Boundaries & Safety Rules

## Always
- Run per-task verification (`cargo check`) after each task; run the full verification chain at phase exit (see `docs/agentic-workflow-v1.md` §9.1).
- Use `?` and proper error types.
- Document public APIs with `///`.
- Add `#[must_use]` where appropriate.

## Ask First
- Adding any new crate (check `docs/crates.md`).
- Introducing `unsafe` blocks.
- Changing MSRV or significant Cargo features.
- Performance optimizations that increase complexity.

## Never
- Use `unwrap()` / `expect()` in non-test, non-main code.
- Ignore Clippy warnings (treat as errors).
- Add `todo!()` or `unimplemented!()` without a tracking comment.
- Commit `target/` directory or large `Cargo.lock` changes without reason.
- Use `std::mem::transmute` or other highly dangerous operations.
