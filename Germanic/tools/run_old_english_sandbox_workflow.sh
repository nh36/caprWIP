#!/usr/bin/env bash
# Run the Old English sandbox tracer workflow (stage snapshots over probe lexemes).
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
COMPOSE_CMD=(docker compose)

LOG_BASENAME=${1:-old_english_tracer_log_$(date +%Y-%m-%d).txt}
CONTAINER_TMP="/usr/app/tmp"
CONTAINER_LOG="$CONTAINER_TMP/$LOG_BASENAME"
HOST_LOG_DIR="$REPO_ROOT/docs/debug_snapshots"
HOST_LOG="$HOST_LOG_DIR/$LOG_BASENAME"

PROBE_FILE_HOST="$REPO_ROOT/tmp/old_english_tracer_probes.txt"
PROBE_FILE_CONTAINER="/usr/app/tmp/old_english_tracer_probes.txt"

run_in_container() {
  "${COMPOSE_CMD[@]}" exec backend bash -lc "$1"
}

python3 "$REPO_ROOT/server/tools/oe_bin_sync_check.py"

mkdir -p "$HOST_LOG_DIR"

if [[ ! -s "$PROBE_FILE_HOST" ]]; then
  cat >"$PROBE_FILE_HOST" <<'PROBES'
*fiskaz
*gebaną
*braudą
*burgą
PROBES
fi

# Ensure probe list in container matches the host file.
cat "$PROBE_FILE_HOST" | "${COMPOSE_CMD[@]}" exec -T backend bash -lc "cat > $PROBE_FILE_CONTAINER"

run_in_container "cd /usr/app && python3 tools/trace_old_english_sandbox.py --bin-dir /usr/app --lexeme-file $PROBE_FILE_CONTAINER --brace-diphthongs --save-log $CONTAINER_LOG"

"${COMPOSE_CMD[@]}" exec backend bash -lc "cd /usr/app && cat $CONTAINER_LOG" > "$HOST_LOG"
echo "Tracer log copied to $HOST_LOG"
