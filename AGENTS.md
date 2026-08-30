# Repository agent instructions

This repository is an Ada-contract-backed deterministic first-tranche parity target. The Ada catalog compiles with GNAT; the current terminal adapter remains Python and must not be described as a full native Ada runtime.

## Horizon target

- Language id: ada
- Display name: Ada
- Horizon status: hybrid Ada contract and portable CLI, remotely validated
- Target class: parity-target
- Repository: ada-stakeholder

## Implementation scope

- Preserve the deterministic CLI contract: `--list-values`, `--focus-family`, `--output-format`, `--seed`, and explicit `--experimental-provider` fail-fast.
- Keep `classic-six + modern-core` dedicated and later packet families on grouped fallback unless canonical `stakeholder-core` changes the contract.
- Keep GNAT compilation, Python adapter tests, and Docker smokes green.
- Keep the full native Ada CLI and live-provider runtime explicit gaps until their dedicated waves.
- Preserve branch protection and required CI checks on `main`.
