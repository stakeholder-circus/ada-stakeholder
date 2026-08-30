# ada-stakeholder Parity

Parity classification: hybrid Ada-contract-backed deterministic first tranche, native and Docker validated.

## Covered

- CLI flags: `--list-values`, `--focus-family`, `--output-format`, `--seed`, `--experimental-provider`.
- Dedicated first-push families: full `classic-six + modern-core`.
- Later packet families: grouped fallback renderers.
- Output contract: deterministic text and normalized JSON with provenance metadata.
- Experimental provider lane: explicit fail-fast only.

## Source anchors

- Rust source of truth: `rust-stakeholder/src/*` generator family behavior and CLI contract.
- Java comparison anchor: `java-stakeholder/src/*` deterministic parity runtime and provider boundary docs.
- Canonical contract: `stakeholder-core/docs/program/*` and shared status ledgers.

## Current Ada shape

`src/stakeholder_registry.ads` is compiled with GNAT in analysis mode. `bin/stakeholder.py` owns terminal argument parsing and deterministic rendering until a full native Ada CLI replaces the hybrid adapter.
