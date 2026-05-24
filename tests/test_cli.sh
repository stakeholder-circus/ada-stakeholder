#!/bin/sh
set -eu
CLI=${CLI:-bin/stakeholder.py}
TMP_DIR=${TMPDIR:-/tmp}/ada-stakeholder-tests.$$
mkdir -p "$TMP_DIR"
trap 'rm -rf "$TMP_DIR"' EXIT

python3 "$CLI" --list-values > "$TMP_DIR/list.json"
grep '"generatorFamilies"' "$TMP_DIR/list.json" >/dev/null
grep 'code-analyzer' "$TMP_DIR/list.json" >/dev/null
grep 'platform-engineering' "$TMP_DIR/list.json" >/dev/null
grep 'service-mesh-rpc-ops' "$TMP_DIR/list.json" >/dev/null

python3 "$CLI" --focus-family code_analyzer --output-format json --seed alpha > "$TMP_DIR/code.json"
grep '"family":"code_analyzer"' "$TMP_DIR/code.json" >/dev/null
grep '"rendererKey":"classic-six.code_analyzer"' "$TMP_DIR/code.json" >/dev/null
grep '"sourceRepo":"ada-stakeholder"' "$TMP_DIR/code.json" >/dev/null

python3 "$CLI" --focus-family platform-engineering --output-format json --seed stable > "$TMP_DIR/platform-a.json"
python3 "$CLI" --focus-family platform_engineering --output-format json --seed stable > "$TMP_DIR/platform-b.json"
diff -u "$TMP_DIR/platform-a.json" "$TMP_DIR/platform-b.json"

python3 "$CLI" --focus-family metrics --seed beta > "$TMP_DIR/metrics.txt"
grep 'family: metrics' "$TMP_DIR/metrics.txt" >/dev/null
grep 'renderer: classic-six.metrics' "$TMP_DIR/metrics.txt" >/dev/null

if python3 "$CLI" --experimental-provider local-demo > "$TMP_DIR/provider.out" 2>&1; then
  echo 'experimental provider unexpectedly succeeded' >&2
  exit 1
fi
grep 'experimental provider' "$TMP_DIR/provider.out" >/dev/null
