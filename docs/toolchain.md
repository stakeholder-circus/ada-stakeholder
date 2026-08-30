# Toolchain

## Native lane

- GNAT from Ubuntu for Ada contract compilation.
- Python 3 for deterministic CLI adapter execution.
- Validation commands:
  - `python3 scripts/validate_scaffold.py`
  - `make compiler-proof`
  - `make test`

## Toolchain split

- Ada compile proof: GNAT analyzes `src/stakeholder_registry.ads`.
- CLI/runtime proof: Python executes `bin/stakeholder.py` for deterministic terminal behavior.
- Docker: Ubuntu/GNAT build gate with a non-root Python runtime image.
- Nix: `flake.nix` remains the reproducible workspace-discovery policy.
- The retained `tree-sitter-ada` validator is optional historical parser evidence, not the authoritative CI gate.
