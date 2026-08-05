#!/usr/bin/env bash
# Regenerate the SC004 split component-behavior evidence inside the backend
# container.
#
# After the SC004 Outcome-C split, this script:
#   1. compiles the production cascade (germanic.txt) in the backend container;
#   2. runs tools/sc004_component_behaviors.py, which regexes the two production
#      component defines (SC014 PNWGmcUnstressedAiMonophthongization, SC004
#      EAFAiMonophthongization) plus the retained compatibility alias
#      PWGmcAiMonophthongization out of germanic.txt and applies each to a
#      curated set of internal star-representation probe forms.
#
# The committed evidence TSV
#   Germanic/docs/sound_changes/order_tests/sc004_component_behaviors.tsv
# is asserted by tests/test_sc004_component_split.py (host-runnable). Running
# this script must leave that TSV unchanged.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
COMPOSE_CMD=(docker compose)

run_in_container() {
  "${COMPOSE_CMD[@]}" exec -T backend bash -lc "$1"
}

echo "== Compiling production cascade (germanic.txt) in backend container =="
run_in_container "cd /usr/app && foma -q -l fsts/germanic.txt -e quit >/dev/null"

echo "== Probing SC014 / SC004 component behaviors =="
run_in_container "cd /usr/app && python3 tools/sc004_component_behaviors.py \
  --out /usr/app/docs/sound_changes/order_tests/sc004_component_behaviors.tsv"

echo "== Done. Evidence: Germanic/docs/sound_changes/order_tests/sc004_component_behaviors.tsv =="
