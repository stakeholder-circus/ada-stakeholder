# ada-stakeholder Parity

Parity classification: parser-backed deterministic first-tranche local implementation.

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

## Local Ada shape

`src/stakeholder_registry.ads` is the Ada language artifact for the tranche catalog and is parser-validated with `tree-sitter-ada`. `bin/stakeholder.py` owns terminal argument parsing and deterministic rendering because the native Ada compiler toolchain is deferred.
