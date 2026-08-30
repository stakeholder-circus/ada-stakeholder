# ada-stakeholder Gaps

## Deferred in this tranche

- The terminal CLI is still a Python adapter rather than a full native Ada runtime.
- Full live-provider/runtime support is deferred to the later provider rollout wave.

## Implemented now

- Full deterministic `classic-six + modern-core` family coverage in the local contract catalog.
- Grouped fallback coverage for later packet families.
- Normalized deterministic JSON and text output.
- `--list-values` registry output.
- Explicit fail-fast for `--experimental-provider` and unknown experimental flags.
- Ada source compile proof through GNAT analysis mode.
- Native and Docker validation plus workflow-security gates in GitHub Actions.
