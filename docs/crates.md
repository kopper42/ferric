# Preferred Crates

## Core
- Error: `thiserror`, `anyhow`
- Async: `tokio`
- Logging: `tracing` + `tracing-subscriber`
- CLI: `clap` (derive)
- Config: `config` or `figment`
- Serialization: `serde` + `serde_json` / `toml`

## Database
- `sqlx` (preferred) or `diesel`

## Alternatives & Avoid
- Avoid `std::sync::Mutex` when `tokio::sync::Mutex` or channels are better.
- Prefer `parking_lot` only when performance is proven necessary.

Add new crates here after approval.
