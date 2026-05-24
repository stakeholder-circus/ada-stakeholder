# Toolchain

## Native lane

- Python 3 from the local workstation for deterministic CLI execution.
- Rust/Cargo from the local workstation for parser validation.
- Crates: `tree-sitter = 0.20`, `tree-sitter-ada = 0.1`.
- Validation commands:
  - `python3 scripts/validate_scaffold.py`
  - `make compiler-proof`
  - `make test`

## Toolchain split

- Ada parser proof: `tree-sitter-ada` parses `src/stakeholder_registry.ads`.
- CLI/runtime proof: Python executes `bin/stakeholder.py` for deterministic terminal behavior.
- GNAT/Alire: not installed; compilation is explicitly deferred.
- Docker: deferred for M1 resource safety.
- Nix: `flake.nix` remains baseline policy only until broader lock normalization resumes.
