# First-push family traceability

| Family | Ada target | Rust source | Java source | Contract anchor | Parity class |
| --- | --- | --- | --- | --- | --- |
| `code_analyzer` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `data_processing` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `jargon` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `metrics` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `network_activity` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `system_monitoring` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated classic-six |
| `agent_workflows` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated modern-core |
| `platform_engineering` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated modern-core |
| `observability_ai_runtime` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated modern-core |
| `delivery_preview_ops` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated modern-core |
| `supply_chain_security` | `bin/stakeholder.py`, `src/stakeholder_registry.ads` | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | dedicated modern-core |
| later packet families | `bin/stakeholder.py` grouped fallback renderers | `rust-stakeholder/src/*` | `java-stakeholder/src/*` | `stakeholder-core/docs/program/*` | grouped fallback |

Validation evidence: `python3 scripts/validate_scaffold.py`, GNAT analysis through `make compiler-proof`, Python adapter tests through `make test`, and Docker runtime smokes in GitHub Actions.
