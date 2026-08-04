#!/usr/bin/env bash
# Regenerate the cross-stage rule-interaction matrix inside the backend container.
#
# Phase 5 of the historical-cascade-order project. Runs
# tools/cascade_interaction_harness.py, which compiles germanic.txt once
# (save defined) and then runs one foma `test equivalent` per PNWGmc x PWGmc
# pair. The matrix is deterministic (transducer equivalence is a decision
# procedure), unlike compiled .bin bytes.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
COMPOSE_CMD=(docker compose)

"${COMPOSE_CMD[@]}" exec -T backend bash -lc \
  "cd /usr/app && python3 tools/cascade_interaction_harness.py --progress"

echo "== Matrix written to Germanic/docs/sound_changes/cascade_baseline/cascade_interaction_matrix.tsv =="
echo "== Regenerate the report with the analysis in cascade_interaction_report.md if the matrix changed =="
