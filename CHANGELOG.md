# Changelog

Human-readable history of completed, verified changes. Record outcomes, not plans.

## Entry Rules
- Add entries only after work is completed and checks/verification pass.
- Prefer user-visible or maintainer-visible outcomes over file-by-file lists.
- Skip planning-only churn unless process history is explicitly requested.
- Keep each bullet short and specific enough to understand what changed and why it matters.

## 2026-04-26

- **Phase 1 bootstrap - Task 1 complete**: Established minimal `Cargo.toml` + `src/lib.rs` with documented `greet()` API, unit test, and clean `cargo check`. Satisfies boundaries (no unwrap/todo), coding style, architecture, and verification rules. This completes the project structure slice. Workflow evaluation (incorporating upstream scoped autonomy, approval ambiguity, decision triggers, and integrity rules from other AI analysis) approved; refinements targeted for next tasks.

## 2026-04-25
- **Automated TASKS integrity validation added**: Added `scripts/validate_tasks_state.py` to enforce state/gate/task-marker consistency (`[ ]` / `[-]` / `[x]`) and wired it into full verification docs plus a repo-managed pre-commit hook script at `.githooks/pre-commit`.
- **TASKS archival workflow added**: Before replacing `TASKS.md` for a new phase, the previous execution document is now archived to `docs/task_archive/` using a dated phase-based filename, and a fresh `TASKS.md` is generated from the template.
- **Tri-state task markers adopted**: Updated `docs/agentic-workflow-v1.md`, `docs/templates/TASKS_TEMPLATE.md`, and active `TASKS.md` to use `[ ]` todo / `[-]` active / `[x]` done for tasks, with exactly one active `[-]` task required.
- **Workflow context trimmed with appendices**: Reduced policy duplication by keeping `docs/agentic-workflow-v1.md` as concise core, moving deep Git/session recovery guidance to `docs/appendix/`, trimming `AGENTS.md` and `PHASES`/`TASKS` guidance docs, and adding a compact active-policy snapshot to `docs/memory/index.md`.
- **Tri-state policy explicitly marked as local override**: Updated `docs/agentic-workflow-v1.md` to state that local `[-]` active-phase detection supersedes upstream examples that imply "first unchecked `[ ]`" conventions.
- **Phase marker ADR corrected for tri-state policy**: Updated `docs/memory/index.md` ADR-012 to match the adopted marker system (`[ ]` todo, `[-]` active, `[x]` done) and removed stale language that said active phase is the first unchecked `[ ]`.
- **Session recovery protocol added**: Added §13 to `docs/agentic-workflow-v1.md` defining four recovery cases (partial edits, state/gate contradictions, unchecked tasks after crash) so interrupted sessions can resume safely.
- **Git integration guidance added**: Added §12 to `docs/agentic-workflow-v1.md` plus a commit-workflow section in `docs/cargo.md`, defining when to commit (after each verified task) and what message structure to use, bridging the gap between task completion and version control.
- **Verification split per-task vs phase-exit**: Split §9 in `docs/agentic-workflow-v1.md` into per-task (`cargo check` fast) and phase-exit (full chain) verification tiers, reducing per-task latency. Updated `docs/templates/TASKS_TEMPLATE.md` and `docs/cargo.md` to match.
- **Verification signal matching hardened**: Added locale/color guidance (`LC_ALL=C`, `--color never`, exit-code preference) to §7, §9, and `TASKS_TEMPLATE.md` for deterministic success-signal matching across environments.
- **Layered memory made optional**: Phase-completion gate now supports flat memory (append to index) alongside layered promotion protocol. Teams choose per adoption profile; default is flat. Updated `docs/agentic-workflow-v1.md` §11 and `TASKS_TEMPLATE.md`.
- **Tri-state phase marker adopted (`[-]` for active)**: Replaced the fragile "first `[ ]` is active" convention with an explicit tri-state system: `[ ]` (todo), `[-]` (active), `[x]` (done). The agent now looks for the single `[-]` marker. Updated `PHASES.md`, `docs/PHASES_AGENT_GUIDE.md`, `docs/templates/PHASES_TEMPLATE.md`, and added cross-references in `docs/agentic-workflow-v1.md`.
- **Memory contradiction in §11 fixed**: Step 3 of phase-completion gate now conditionally records decisions in the semantic layer (Option A) or appends to memory index (Option B), matching the choice made in step 2. Removed the redundant "semantic layer" line from `TASKS_TEMPLATE.md` that contradicted the flat-memory Option B.
- **Internal consistency fixed across docs**: Aligned `AGENTS.md`, `docs/boundaries.md`, and `docs/cargo.md` with the per-task vs phase-exit verification split (§9.1) and optional memory model (§11). Resolved contradictions between the old "always run full verification" mandate and the new verification-tier split.
- **Phase roadmap bootstrapped**: Created `PHASES.md` with Phase 1 (Initialize Rust project structure marked `[-]`), bootstrapping the five artifact roles from the harness spec.
- **Agent guidance baseline added**: Created `AGENTS.md` and linked core project docs so contributors and agents share the same operating rules.
- **Security standard documented**: Added `docs/security.md` with repo-specific defaults for secrets, validation, TLS, logging hygiene, and dependency security checks.
- **Cargo dependency policy strengthened**: Expanded `docs/cargo.md` with explicit dependency-change rules, minimal feature guidance, and `cargo add` preference.
- **Rust/testing conventions tightened**: Updated `docs/coding-style.md` and `docs/testing.md` with compiler-first checks, stronger error-handling constraints, and interface-first testing guidance.
- **Project memory system introduced**: Added `docs/memory/index.md` ledger with ADRs and created `docs/memory/TOPIC_TEMPLATE.md` for long-form memory topics.
- **Agentic workflow v1 profile added**: Introduced `docs/agentic-workflow-v1.md` with a minimal state machine, dual-approval gating, phase/slice/task decomposition, drift handling, and an execution-document starter template.
- **Phase roadmap guide added**: Added `docs/PHASES_AGENT_GUIDE.md` as a practical companion for `PHASES.md` changes, including phase/slice/task boundaries, stale-plan reset behavior, and fallback precedence to the v1 workflow profile.
- **Local phase/task templates added**: Added `docs/templates/PHASES_TEMPLATE.md` and `docs/templates/TASKS_TEMPLATE.md` aligned to the v1 workflow profile, with explicit approval phrases, allowed states, and phase/slice/task scaffolding.
