#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys

CLASSIC = [
    ("code_analyzer", "code-analyzer", "classic-six.code_analyzer", "classic-six", "analysisFocus", "strongly-typed-contract-audit"),
    ("data_processing", "data-processing", "classic-six.data_processing", "classic-six", "dataWindow", "bounded-batch-reconciliation"),
    ("jargon", "jargon", "classic-six.jargon", "classic-six", "languagePolicy", "ada-safety-glossary"),
    ("metrics", "metrics", "classic-six.metrics", "classic-six", "signalBlend", "latency-error-saturation"),
    ("network_activity", "network-activity", "classic-six.network_activity", "classic-six", "transportMix", "rpc-stream-safety"),
    ("system_monitoring", "system-monitoring", "classic-six.system_monitoring", "classic-six", "telemetryScope", "runtime-build-host"),
]
MODERN = [
    ("agent_workflows", "agent-workflows", "modern-core.agent_workflows", "modern-core", "coordinationMode", "deterministic-dispatch-handshake"),
    ("platform_engineering", "platform-engineering", "modern-core.platform_engineering", "modern-core", "platformSurface", "ada-parser-backed-validation-lane"),
    ("observability_ai_runtime", "observability-ai-runtime", "modern-core.observability_ai_runtime", "modern-core", "runtimeSignals", "logs-metrics-provider-audit"),
    ("delivery_preview_ops", "delivery-preview-ops", "modern-core.delivery_preview_ops", "modern-core", "deliveryGuardrail", "preview-release-checkpoints"),
    ("supply_chain_security", "supply-chain-security", "modern-core.supply_chain_security", "modern-core", "supplyChainPosture", "source-parser-attestation"),
]
FALLBACK_GROUPS = {
    "ai_governance": ["ai_inference_ops", "evaluation_and_guardrails", "knowledge_retrieval", "edge_client_runtime", "identity_and_trust", "aibom_provenance", "agent_boundary_security", "embedded_agentic_pipeline", "data_governance_compliance", "finops_capacity"],
    "security_blockchain": ["blockchain_protocol_ops", "cross_chain_interop", "proof_and_sequencer_ops"],
    "overlay_quantum": ["hybrid_runtime_ops", "capacity_cost_controller", "batch_execution_tuner", "compiler_maintainer", "interop_adapter_engineer", "preflight_capacity_planner", "simulator_performance_engineer"],
    "health_protocol": ["fhir_profile_generator", "smart_launch_oauth", "bulk_fhir_population_ops", "hl7v2_feed_ops", "clinical_workflow_events", "dicomweb_imaging_ops", "openehr_semantic_record_ops", "device_telemetry_clinical", "emr_vendor_adapter", "ocpp_chargepoint_ops", "ocpi_roaming_ops", "mcp_a2a_ops", "streaming_bus_ops", "service_mesh_rpc_ops"],
}

def slug(value):
    return value.replace("_", "-")

def all_families():
    rows = [dict(id=i, registryId=r, rendererKey=k, tranche=t, contextKey=ck, contextValue=cv) for i, r, k, t, ck, cv in CLASSIC + MODERN]
    for group, ids in FALLBACK_GROUPS.items():
        for family in ids:
            rows.append(dict(id=family, registryId=slug(family), rendererKey=f"fallback.{group}", tranche=f"fallback-{group}", contextKey="fallbackFamily", contextValue=group))
    return rows

FAMILIES = all_families()

def find_family(value):
    normalized = value.strip().lower().replace("-", "_")
    for family in FAMILIES:
        if family["id"] == normalized or family["registryId"] == value.strip().lower():
            return family
    return None

def stable_hash(seed, family_id):
    digest = hashlib.sha256(f"{seed}::{family_id}".encode()).hexdigest()
    return int(digest[:12], 16)

def timestamp(value):
    seconds = value % 86400
    return f"2026-01-01T{seconds // 3600:02d}:{(seconds % 3600) // 60:02d}:{seconds % 60:02d}Z"

def registry():
    return {
        "outputFormats": ["text", "json"],
        "flags": ["list-values", "focus-family", "output-format", "seed", "experimental-provider"],
        "generatorFamilies": [{k: family[k] for k in ["id", "registryId", "rendererKey", "tranche"]} for family in FAMILIES],
        "classicSix": [row[1] for row in CLASSIC],
        "modernCore": [row[1] for row in MODERN],
        "fallbackFamilies": [slug(family) for families in FALLBACK_GROUPS.values() for family in families],
        "implementationMode": "family-focus-deterministic",
    }

def payload(family, seed, output_format):
    value = stable_hash(seed, family["id"])
    data = {
        "eventType": "stakeholder.generator.output",
        "sequence": 1000 + (value % 9000),
        "family": family["id"],
        "message": f"Deterministic ada tranche for {family['id']}",
        "timestamp": timestamp(value),
        "context": {
            "rendererKey": family["rendererKey"],
            family["contextKey"]: family["contextValue"],
            "seedFingerprint": f"{family['registryId']}-{value:x}",
            "tranche": family["tranche"],
            "adaProfile": "parser-backed-source-catalog",
        },
        "generationProvenance": {
            "sourceRepo": "ada-stakeholder",
            "baseline": "local-small-tranche-family-focus",
            "experimental": False,
            "adapterType": "ada-source-plus-python-cli",
            "promptVersion": None,
        },
        "outputFormat": output_format,
    }
    return data

def main(argv):
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--list-values", action="store_true")
    parser.add_argument("--focus-family")
    parser.add_argument("--output-format", default="text", choices=["text", "json"])
    parser.add_argument("--seed", default="default-seed")
    parser.add_argument("--experimental-provider")
    args, extras = parser.parse_known_args(argv)
    if extras:
        first = extras[0]
        if first.startswith("--experimental-"):
            print("experimental flags require --experimental-provider", file=sys.stderr)
        else:
            print(f"unknown argument: {first}", file=sys.stderr)
        return 2
    if args.experimental_provider is not None:
        print(f"experimental provider '{args.experimental_provider}' is not enabled in the deterministic first tranche", file=sys.stderr)
        return 2
    if args.list_values:
        print(json.dumps(registry(), separators=(",", ":")))
        return 0
    if not args.focus_family:
        print("focus-family is required and must be a known generator family", file=sys.stderr)
        return 2
    family = find_family(args.focus_family)
    if family is None:
        print(f"invalid --focus-family: {args.focus_family}", file=sys.stderr)
        return 2
    data = payload(family, args.seed, args.output_format)
    if args.output_format == "json":
        print(json.dumps(data, separators=(",", ":")))
    else:
        print(f"family: {data['family']}")
        print(f"renderer: {data['context']['rendererKey']}")
        print(f"tranche: {data['context']['tranche']}")
        print(f"sequence: {data['sequence']}")
        print(f"timestamp: {data['timestamp']}")
        print(f"message: {data['message']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
