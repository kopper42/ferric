//! # Agentic Playground
//!
//! Self-hosting example and testbed for the lightweight phased agentic development
//! workflow. See:
//! - `docs/agentic-workflow-v1.md` (canonical local normative profile)
//! - `resources/AGENT_ONBOARDING_STANDALONE.md` (upstream portable spec v1.5)
//! - `docs/memory/index.md` (ADRs and active policy snapshot)
//!
//! This crate establishes the baseline structure for Phase 1.

// A simple, documented entrypoint to verify the library builds correctly.
// No `unwrap()`, `todo!()`, or unsafe. Follows rules from `docs/boundaries.md`,
// `docs/coding-style.md`, and `docs/testing.md`.

/// Returns a greeting confirming the agentic playground is initialized.
///
/// This function serves as the minimal public API for the bootstrap phase.
pub fn greet() -> String {
    "Hello from the agentic Rust playground! Workflow v1 is active.".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_greet() {
        let result = greet();
        assert_eq!(
            result,
            "Hello from the agentic Rust playground! Workflow v1 is active."
        );
    }
}
