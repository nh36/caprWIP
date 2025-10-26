#!/usr/bin/env bash
# Apply the German FST, then run the helper to prepare surface strings for the
# existing brace-based filter. Usage:
#   server/tools/apply_german.sh down input.txt
#   server/tools/apply_german.sh up input.txt
# `down` maps proto→surface; `up` maps surface→proto (after prep).
set -euo pipefail
MODE=${1:-}
FILE=${2:-}
if [[ -z "$MODE" || -z "$FILE" ]]; then
  echo "Usage: $0 {down|up} path/to/file" >&2
  exit 1
fi
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

case "$MODE" in
  down)
    docker compose exec backend bash -lc "cd /usr/app && flookup german.bin" < "$FILE" \
      | python3 "$SCRIPT_DIR/german_surface_prep.py"
    ;;
  up)
    # Expect already wrapped strings in FILE; run german.bin upwards.
    docker compose exec backend bash -lc "cd /usr/app && flookup -x german.bin" < "$FILE"
    ;;
  *)
    echo "Unknown mode: $MODE" >&2
    exit 1
    ;;
esac
