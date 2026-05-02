# Project Memory Ledger

Last updated: Project renamed to Ferric and bootstrap completed (2026-05-01)

## Index
- Architecture baseline: `docs/architecture.md`
- Coding conventions: `docs/coding-style.md`
- Testing expectations: `docs/testing.md`
- Cargo workflows and dependency policy: `docs/cargo.md`
- Safety boundaries and escalation rules: `docs/boundaries.md`
- Security standards: `docs/security.md`
- Preferred crates and approval policy: `docs/crates.md`
- Completed-work history: `CHANGELOG.md`
- Long-form memory topic template: `docs/memory/topic-template.md`
- Memory review protocol: `docs/memory/memory-review-template.md`
- Phase roadmap editing guide: `docs/phases-agent-guide.md`
- Local templates: `docs/templates/phases-template.md`, `docs/templates/slices-template.md`, `docs/templates/tasks-template.md`
- TASKS archive directory: `docs/task_archive/`
- TASKS integrity validator: `scripts/validate_tasks_state.py`, `.githooks/pre-commit`
- Full portable spec: `resources/AGENT_ONBOARDING_STANDALONE.md`

## Current Active Policy Snapshot

- **Canonical source**: `docs/agentic-workflow-v1.md` (three-level hierarchy: PHASES → SLICES → per-slice TASKS, tri-state markers `[ ]`/`[-]`/`[x]`, approval gate, verification/backoff, bootstrap procedure in §0).
- Tri-state markers apply at all levels with **exactly one active** (`[-]`) at a time.
- Execution requires explicit approval phrase + `State: APPROVED_FOR_EXECUTION` + checked execution gate.
- Default: one verified task per turn. Edits limited to listed "Files to change".
- `SLICES.md` is authoritative for active slice within the active phase.
- Memory mode default: **flat** (append to this file).
- Validator (`scripts/validate_tasks_state.py --strict`) must pass before commits and slice/phase gates.

## Memory Layers

The memory system uses four layered directories with distinct retention and review policies:

- **working/** — Transient session notes.
- **episodic/** — Specific events and decisions.
- **semantic/** — Distilled principles and ADRs (`index.md` lives here).
- **personal/** — Long-term behavioral rules (updated only with explicit approval).

**Review Protocol**: Promotions from working/episodic to semantic/personal require human rationale using `memory-review-template.md`.

## Key Architectural Decisions (Educational ADRs)

### ADR-007: Memory Is Secondary to Repository Truth
**Status**: Accepted  
**Context**: Agents and humans need a single source of truth.  
**Decision**: Repository docs (`docs/agentic-workflow-v1.md`, `AGENTS.md`, etc.) are canonical. This ledger is an index and supplement only.  
**Consequences**: Reduces drift; requires discipline to keep docs current.

### ADR-016: Three-Level Hierarchy for Context Efficiency
**Status**: Accepted  
**Decision**: PHASES.md (high-level), stateful SLICES.md (active phase only), per-slice TASKS.md. Archive/rotate TASKS and SLICES after each slice/phase to keep context small.  
**Consequences**: Better context window usage while maintaining safety gates and validator enforcement.

See `docs/memory/topic-template.md` for new ADRs and `docs/agentic-workflow-v1.md` for full current rules.

### Decision: Root folder renamed to `ferric`; crate identity updated from `my-project` template
**Date**: 2026-05-01  
**Outcome**: No internal absolute paths existed. All changes were relative or manifest-driven. Crate name, lib/bin names, strings, README, memory, changelog, PHASES/SLICES/TASKS updated consistently. Bootstrap slice advanced.

<!-- Additional educational ADRs or decisions can be added here as the template is used. -->
