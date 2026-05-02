# Agentic Development Phases

AI agents: Use this file only to determine phase order, active phase, and Definition of Done (DoD). Do not place execution task checklists here.

See:
- `docs/agentic-workflow-v1.md` for updated three-level hierarchy, state-machine, slice/phase gates, and execution rules.
- `docs/phases-agent-guide.md` for guidance on PHASES.md and SLICES.md.
- `SLICES.md` for active slice details within this phase.

## Active Phase Convention

Each phase uses one of three markers:

- `[ ]` — Todo: planned but not yet started.
- `[-]` — Active: currently being worked on. **Exactly one** phase should have `[-]`.
- `[x]` — Done: completed and verified.

If zero or more than one phase has `[-]`, agents will ask the human for clarification.

---

## [x] Phase 1: Project Initialization

Goal: Establish a working Rust project (named `ferric`) with both library and binary (src/lib.rs + src/main.rs), clean build/test/lint/format, and the full agentic workflow tooling so the template is immediately usable.

Definition of Done:
- All slices in `SLICES.md` for this phase are `[x]` and their per-slice `TASKS.md` files archived/verified.
- `cargo check`, `cargo test`, `cargo fmt --check`, `cargo clippy --all-targets --all-features -- -D warnings`, and `cargo build --release` all pass.
- Material decisions recorded in `docs/memory/index.md`.
- `SLICES.md` for this phase archived upon completion.

## [-] Phase 2: Core Functionality

Goal: Implement additional example functionality, expand tests, and demonstrate the agentic workflow in practice while maintaining all safety boundaries.

Definition of Done:
- New features added and fully verified per coding-style, testing, and boundaries docs.
- All slices completed with archived TASKS.md and updated memory/CHANGELOG.
- Full project remains clean per `cargo` verification chain.

<!-- Future phases added here as objectives become clear. All DoD must remain testable and phase-scoped. -->
