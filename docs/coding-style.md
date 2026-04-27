# Coding Style & Idiomatic Rust

## General Rules
- Follow official Rust style (rustfmt + Clippy).
- Treat the compiler as the judge: code must pass `cargo check`.
- Use meaningful variable names. Avoid single-letter except in loops/closures.
- Prefer `impl Trait` in argument position, concrete types in return position (unless `-> impl Trait` is clearly better).
- Exhaustive matching on enums.
- Handle `Option` and `Result` explicitly; avoid implicit fallthrough logic.

## Good vs Bad Examples

**Error Handling**
```rust
// Good
#[derive(thiserror::Error, Debug)]
pub enum MyError { ... }

fn do_thing() -> Result<(), MyError> {
    helper()?;           // Use ? operator
    Ok(())
}

// Bad
fn do_thing() -> Result<(), Box<dyn std::error::Error>> {
    helper().unwrap();   // Never use unwrap in library code
}
```

**Ownership**
```rust
// Good
fn process(data: &[u8]) -> Vec<u8> { ... }     // Prefer slices
// Bad
fn process(data: Vec<u8>) -> Vec<u8> { ... }   // Unnecessary ownership
```

**Other Conventions**
- Use `new()` for constructors, `with_*` for builder pattern.
- Prefer `iter()` methods over manual loops when readable.
- No `unsafe` unless heavily documented with invariants.
- Do not use `unwrap()`, `expect()`, `todo!()`, or `panic!()` in library/business logic (tests and top-level CLI bootstrapping are the only typical exceptions).
