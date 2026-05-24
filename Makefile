PYTHON ?= python3
CARGO ?= cargo

.PHONY: compiler-proof test clean

compiler-proof:
	$(CARGO) run --manifest-path tools/ada_parse_validator/Cargo.toml -- src/stakeholder_registry.ads

test: compiler-proof
	$(PYTHON) -m py_compile bin/stakeholder.py
	PYTHON=$(PYTHON) tests/test_cli.sh

clean:
	rm -rf __pycache__ tools/ada_parse_validator/target
