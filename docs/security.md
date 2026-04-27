# Security Guidelines

This document defines practical, repo-specific security defaults for Rust services and CLIs.
It complements `docs/architecture.md`, `docs/coding-style.md`, `docs/testing.md`, and `docs/boundaries.md`.

## Security Principles

- Fail closed by default.
- Never expose secrets in logs, errors, panics, or telemetry.
- Use least privilege for credentials, tokens, and service access.
- Keep security-sensitive state explicit and passed through typed config/state.
- Prefer proven crates and platform TLS over custom security code.

## Configuration and Secrets

- Load configuration into strongly typed structs (`config` or `figment`, per crate setup).
- Store credentials in environment variables or secret managers, not source code.
- Use `secrecy::Secret<T>` for passwords, API keys, tokens, and similar sensitive data.
- Validate required security config at startup and fail fast when missing.
- Keep examples in `*.example` files (`.env.example`, `config.example.toml`) without real values.

## Input and Data Validation

- Validate all external input (CLI args, HTTP requests, config files).
- Prefer declarative validation (`validator`) where it improves clarity.
- Keep explicit checks for sensitive fields where derive-based validation is insufficient.
- Enforce bounds/length/format checks before business logic or persistence.

## Logging and Error Handling

- Use structured logging with `tracing` and sanitize sensitive fields.
- Log safe summaries, never raw secrets.
- Return user-safe error messages externally; keep detailed diagnostics internal.
- Avoid leaking stack traces or internal topology to clients.

## Transport and Network Security

- Use TLS for external service communication (`https://`, `postgresql://` with TLS, `rediss://` when applicable).
- Do not disable certificate verification in production.
- Apply conservative defaults for timeouts and retries on network calls.

## Dependency and Supply Chain Security

- Run `cargo audit` regularly and in CI.
- Use `cargo deny` for license and dependency policy checks.
- Update vulnerable dependencies promptly after validation.
- Prefer well-maintained crates with clear ownership and release history.

## Implementation Guardrails

## Always

- Keep credentials typed as secrets and passed explicitly through app state.
- Review security impact when changing auth, config loading, networking, or persistence.
- Add tests for security-relevant behavior (validation, auth checks, error redaction).

## Ask First

- Adding new security-sensitive crates or crypto dependencies.
- Introducing `unsafe` in security-critical paths.
- Changing authentication/authorization semantics.

## Never

- Hard-code credentials, tokens, or private keys.
- Log secret values or include them in error strings.
- Implement custom cryptographic primitives.
- Add global mutable secret state.
- Bypass validation for external input.

## Minimum Security Checks Before Merge

- `cargo fmt --check`
- `cargo clippy --all-targets --all-features -- -D warnings`
- `cargo test`
- `cargo audit`
- `cargo deny check licenses`

If one of these checks is not applicable for a crate, document why in the PR/task notes.
