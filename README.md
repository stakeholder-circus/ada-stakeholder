> [!WARNING]
> This repository is AI-assisted and manually reviewed. It is local-only in the resource-safe deterministic tranche.

# ada-stakeholder

Ada parser-backed implementation artifact for the stakeholder deterministic first tranche.

## Current tranche

- Full dedicated `classic-six + modern-core` generator family catalog.
- Grouped fallback for later generator families.
- Deterministic normalized JSON with same-seed stability.
- `--list-values`, `--focus-family`, `--output-format`, `--seed`, and explicit `--experimental-provider` fail-fast.
- Ada source is parser-validated with `tree-sitter-ada` through a tiny Rust validator.
- Terminal CLI execution is provided by a portable Python runner because GNAT/Alire is not installed in this M1-safe pass.
- Full live-provider/runtime support remains deferred to the later provider wave.

## Commands

- `python3 scripts/validate_scaffold.py`
- `make compiler-proof`
- `make test`
- `python3 bin/stakeholder.py --list-values`

Docker is intentionally not used in this M1-safe pass; parser-backed Ada source validation is the native evidence lane.
