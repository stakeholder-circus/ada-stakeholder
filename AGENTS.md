# Repository agent instructions

This repository is a local-only Ada parser-backed deterministic first-tranche parity target.

## Horizon target

- Language id: ada
- Display name: Ada
- Horizon status: parser-backed local tranche after evidence is recorded
- Target class: parity-target
- Repository: ada-stakeholder

## Implementation scope

- Preserve the deterministic CLI contract: `--list-values`, `--focus-family`, `--output-format`, `--seed`, and explicit `--experimental-provider` fail-fast.
- Keep `classic-six + modern-core` dedicated and later packet families on grouped fallback unless canonical `stakeholder-core` changes the contract.
- Do not claim GNAT/native Ada compilation until GNAT or Alire is installed and validated.
- Keep Docker and full live-provider runtime support deferred until a later approved wave.
- Do not push this repo; local-only until the publication/governance wave explicitly includes it.
