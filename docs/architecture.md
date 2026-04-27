# Architecture & Design

## Project Structure
- `src/bin/` — CLI entry points (if applicable)
- `src/lib.rs` — Main library crate
- `src/` — Core modules (domain-driven layout preferred)
- `tests/` — Integration tests
- `benches/` — Criterion benchmarks (when performance critical)

## Design Principles
- Use domain-driven module layout over technical layering when possible.
- Prefer async where I/O is involved (Tokio).
- Clear separation between public API and internal implementation.
- Use `pub(crate)` liberally for encapsulation.

## Key Patterns
- Error handling: `thiserror` for library errors, `anyhow` for applications.
- Configuration: `config` crate + strongly typed structs.
- Logging: `tracing` with structured events.
- State management: Avoid global state; use dependency injection or `Arc<>` where needed.

See `src/lib.rs` or the main module for current entry point.
