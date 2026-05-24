#!/usr/bin/env python3
"""Validate the Ada parser-backed deterministic first-tranche baseline."""

from pathlib import Path

REQUIRED = [
    "AGENTS.md",
    "README.md",
    "STATUS.md",
    "GAPS.md",
    "PARITY.md",
    "AI_DISCLOSURE.md",
    "docs/remotes.md",
    "docs/provenance.md",
    "docs/toolchain.md",
    "docs/traceability/first-push-families.md",
    "scripts/validate_scaffold.py",
    "src/stakeholder_registry.ads",
    "bin/stakeholder.py",
    "tests/test_cli.sh",
    "tools/ada_parse_validator/Cargo.toml",
    "tools/ada_parse_validator/src/main.rs",
    "Makefile",
    "flake.nix",
    "Dockerfile",
    ".github/workflows/ci.yml",
    ".github/workflows/ci-native.yml",
    ".github/workflows/docker-smoke.yml",
]

FORBIDDEN_PHRASES = [
    "scaffold-only. Runtime implementation",
    "No deterministic runtime validation is claimed",
]


def main() -> int:
    missing = [path for path in REQUIRED if not Path(path).exists()]
    if missing:
        for path in missing:
            print(f"missing deterministic baseline file: {path}")
        return 1
    for path in ["README.md", "STATUS.md", "GAPS.md", "PARITY.md", "docs/toolchain.md"]:
        text = Path(path).read_text(encoding="utf-8")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in text:
                print(f"stale scaffold wording in {path}: {phrase}")
                return 1
    print("ada parser-backed deterministic first-tranche baseline files present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
