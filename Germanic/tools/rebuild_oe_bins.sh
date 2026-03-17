#!/usr/bin/env bash
# Rebuild OE bins inside the backend container.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
COMPOSE_CMD=(docker compose)

run_in_container() {
  "${COMPOSE_CMD[@]}" exec backend bash -lc "$1"
}

run_in_container "cd /usr/app && foma -f fsts/germanic.txt"
run_in_container "cd /usr/app && foma -f fsts/old_english_sandbox.txt"

echo "Rebuilt OE bins in /usr/app (repo root)."
