# Testing Guidelines

## Rules
- Every public function should have at least one test.
- Unit tests go in the same file (`#[cfg(test)] mod tests`).
- Integration tests go in the `tests/` directory.
- Use `proptest` or `quickcheck` for complex logic / parsers.
- Snapshot testing (`insta`) for output-heavy code.
- All tests must be deterministic.

## Interface-First Guidance
- If interfaces/signatures are provided up front, write tests against those contracts early.
- If interfaces are still being designed, define and compile the API first, then add behavior tests.
- Prefer small, incremental test/implementation loops for complex logic.
- Do not modify tests only to force a passing result; treat failures as feedback.

## Command Reminders
See `docs/cargo.md` for test commands.

## What to Test
- Happy path + important edge cases.
- Error conditions.
- Invariants (especially around `unsafe` or performance-critical code).

**Never** merge code with failing or ignored tests.
