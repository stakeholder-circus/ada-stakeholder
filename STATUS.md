# ada-stakeholder Status

- Phase target: deterministic first tranche
- Phase state: hybrid Ada contract and portable CLI; native and Docker CI validation active
- Program state: deterministic hybrid tranche complete; native Ada CLI and live-provider tranches deferred
- Publication state: published at `stakeholder-circus/ada-stakeholder`; protected `main` pending first stable CI pass
- Current implementation: Ada source catalog compiled with GNAT, with deterministic Python CLI rendering for the shared terminal contract

## Evidence

- `python3 scripts/validate_scaffold.py`
- `make compiler-proof`
- `make test`
- GitHub Actions contract, GNAT, Python, Docker, dependency, SAST, actionlint, and workflow-security gates

## Open

- Full native Ada terminal/runtime implementation remains deferred.
- Full live-provider/runtime support is deferred to the second-pass provider rollout wave.
