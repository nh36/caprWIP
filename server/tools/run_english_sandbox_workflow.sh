#!/usr/bin/env bash
# Run the English sandbox export → annotation → tracer snapshot workflow.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)
COMPOSE_CMD=(docker compose)

LOG_BASENAME=${1:-english_tracer_log_$(date +%Y-%m-%d).txt}
CONTAINER_TMP="/usr/app/tmp"
CONTAINER_LOG="$CONTAINER_TMP/$LOG_BASENAME"
HOST_LOG_DIR="$REPO_ROOT/docs/debug_snapshots"
HOST_LOG="$HOST_LOG_DIR/$LOG_BASENAME"

LEXEME_FILE_HOST="$REPO_ROOT/server/tmp/english_tracer_probes.txt"
LEXEME_FILE_CONTAINER="tmp/english_tracer_probes.txt"

run_in_container() {
  "${COMPOSE_CMD[@]}" exec backend bash -lc "$1"
}

mkdir -p "$HOST_LOG_DIR"

if [[ ! -s "$LEXEME_FILE_HOST" ]]; then
  cat >"$LEXEME_FILE_HOST" <<'PROBES'
*fiskaz
*gebaną
*swestēr
*braudą
PROBES
fi

run_in_container "cd /usr/app && python3 tools/export_english_sandbox_results.py --output tmp/english_sandbox_results_current.json"
run_in_container "cd /usr/app && python3 tools/annotate_english_sandbox_results.py --input tmp/english_sandbox_results_current.json --output tmp/english_sandbox_results_with_stages.json"
run_in_container "cd /usr/app && python3 tools/trace_english_sandbox.py --lexeme-file $LEXEME_FILE_CONTAINER --brace-diphthongs --save-log $CONTAINER_LOG"

"${COMPOSE_CMD[@]}" exec backend bash -lc "cd /usr/app && cat $CONTAINER_LOG" > "$HOST_LOG"
echo "Tracer log copied to $HOST_LOG"
