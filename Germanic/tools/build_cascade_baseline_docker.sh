#!/usr/bin/env bash
# Regenerate the frozen Old English cascade baseline inside the backend container.
#
# Phase 1 of the historical-cascade-order project. This script:
#   1. compiles the production cascade (germanic.txt) in the backend container;
#   2. runs tools/cascade_baseline.py to capture per-lexeme outputs, multiplicity,
#      and pass/fail plus an outputs_sha256 reproducibility marker;
#   3. regenerates the executable-order manifest from germanic.txt (host-side,
#      pure text parsing).
#
# Foma compilation is byte-non-deterministic, so the reproducibility contract is
# the outputs_sha256 in cascade_baseline_summary.json, NOT any .bin checksum.
# Running this script twice must leave cascade_baseline_summary.json unchanged.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
COMPOSE_CMD=(docker compose)

run_in_container() {
  "${COMPOSE_CMD[@]}" exec -T backend bash -lc "$1"
}

echo "== Compiling production cascade (germanic.txt) in backend container =="
run_in_container "cd /usr/app && foma -q -l fsts/germanic.txt -e quit >/dev/null"

echo "== Capturing output baseline =="
run_in_container "cd /usr/app && python3 tools/cascade_baseline.py"

echo "== Regenerating executable-order manifest (host) =="
python3 "$SCRIPT_DIR/cascade_order_manifest.py"

echo "== Done. Baseline artifacts in Germanic/docs/sound_changes/cascade_baseline/ =="
