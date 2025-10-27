#!/usr/bin/env bash
# Log down-direction outputs for the staged German automata.
# Usage: server/tools/log_german_stages.sh > /tmp/stage_log.txt
set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
STAGES=(GermanAfterEw GermanAfterAu GermanAfterLongV GermanAfterNasal GermanAfterStarDrop GermanAfterShift GermanAfterVowelAdj GermanAfterCleanup GermanPreSurface)
# Proto lexemes written without spaces so foma receives a single token.
LEXEMES=("knewą" "braudą" "blōdą" "tōr")
for stage in "${STAGES[@]}"; do
  echo "== $stage =="
  docker compose exec backend bash -lc "cd /usr/app && cat <<'FST' > /tmp/${stage}.foma
source fsts/germanic.txt
regex ${stage};
FST
foma -f /tmp/${stage}.foma" > /tmp/${stage}.out 2>&1 || true
  docker compose exec backend bash -lc "cd /usr/app && foma <<'FST'
source fsts/germanic.txt
regex ${stage};
$(printf 'apply down %s\n' "${LEXEMES[@]}")
quit
FST" || true
done
