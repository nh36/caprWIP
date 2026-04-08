#!/usr/bin/env bash
# Rebuild OE bins inside the backend container.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
COMPOSE_CMD=(docker compose)

run_in_container() {
  "${COMPOSE_CMD[@]}" exec backend bash -lc "$1"
}

# Build FSTs (writes to /usr/app/*.bin)
run_in_container "cd /usr/app && foma -f fsts/germanic.txt"
run_in_container "cd /usr/app && foma -f fsts/old_english_sandbox.txt"

# Sync old_english.bin from root to both Germanic/fsts/ and backend/
# This keeps all three locations in sync:
#   /usr/app/old_english.bin (where foma writes)
#   /usr/app/fsts/old_english.bin (Germanic/fsts/ in repo)
#   /usr/app/backend/old_english.bin (backend/ in repo, if it exists)
run_in_container "cp /usr/app/old_english.bin /usr/app/fsts/old_english.bin"
if run_in_container "test -d /usr/app/backend" 2>/dev/null; then
  run_in_container "cp /usr/app/old_english.bin /usr/app/backend/old_english.bin"
fi

echo "Rebuilt OE bins in /usr/app (repo root)."
echo "Synced old_english.bin to fsts/ and backend/ directories."
