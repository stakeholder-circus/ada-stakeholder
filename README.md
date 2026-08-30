> [!NOTE]
> This repository is AI-assisted and manually reviewed. The Ada contract is GNAT-compiled; the deterministic terminal adapter is currently Python, not a full native Ada runtime.

# ada-stakeholder

Ada-contract-backed implementation artifact for the stakeholder deterministic first tranche.

## Current tranche

- Full dedicated `classic-six + modern-core` generator family catalog.
- Grouped fallback for later generator families.
- Deterministic normalized JSON with same-seed stability.
- `--list-values`, `--focus-family`, `--output-format`, `--seed`, and explicit `--experimental-provider` fail-fast.
- Ada source is compiled in analysis mode with GNAT.
- Terminal CLI execution is provided by a portable Python adapter; replacing it with native Ada remains tracked work.
- Full live-provider/runtime support remains deferred to the later provider wave.

## Commands

- `python3 scripts/validate_scaffold.py`
- `make compiler-proof`
- `make test`
- `python3 bin/stakeholder.py --list-values`
- `docker build -t ada-stakeholder .`
- `docker run --rm ada-stakeholder --list-values`

GitHub Actions runs the contract, GNAT compile analysis, Python adapter tests, Docker smokes, dependency review, actionlint, and workflow-security gates.
