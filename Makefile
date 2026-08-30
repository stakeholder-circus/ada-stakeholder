PYTHON ?= python3
GNATMAKE ?= gnatmake
ADA_BUILD_DIR ?= build/ada

.PHONY: compiler-proof test clean

compiler-proof:
	mkdir -p $(ADA_BUILD_DIR)
	$(GNATMAKE) -gnatc -D $(ADA_BUILD_DIR) src/stakeholder_registry.ads

test: compiler-proof
	$(PYTHON) -m py_compile bin/stakeholder.py
	PYTHON=$(PYTHON) tests/test_cli.sh

clean:
	rm -rf __pycache__ build tools/ada_parse_validator/target
