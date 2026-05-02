//! # Ferric
//!
//! Lightweight phased agentic development workflow for Rust projects, as
//! defined in `docs/agentic-workflow-v1.md`.
//!
//! This crate provides both a library and a binary. The library contains
//! reusable logic and tests; the binary (`src/main.rs`) is a thin wrapper.

// No `unwrap!()`, `todo!()`, or `unsafe`. Follows rules from `docs/boundaries.md`,
// `docs/coding-style.md`, and `docs/testing.md`.

/// Returns a greeting. This is the minimal public API for the template.
pub fn greet() -> String {
    "Hello from ferric! The agentic workflow template is ready.".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        let result = greet();
        assert_eq!(
            result,
            "Hello from ferric! The agentic workflow template is ready."
        );
    }
}
