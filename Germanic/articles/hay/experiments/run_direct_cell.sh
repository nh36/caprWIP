#!/usr/bin/env bash
# Research-only verification of the cycle-9 direct-cell derivations.
# Compiles experiments/direct_cell.foma inside the backend container and
# checks the derived outputs against expected.tsv. Touches nothing in
# production; all compilation happens in a container tmpdir.
set -euo pipefail
cd "$(dirname "$0")"

EXP=/tmp/hay-direct-cell-exp

docker compose -f ../../../../docker-compose.yml exec -T backend sh -c \
  "rm -rf $EXP && mkdir -p $EXP && cat > $EXP/direct_cell.foma && cd $EXP && foma -q -f direct_cell.foma -e quit >/dev/null" \
  < direct_cell.foma

run() { # run <bin> <input>
  docker compose -f ../../../../docker-compose.yml exec -T backend sh -c \
    "cd $EXP && echo '$2' | flookup -i -b -x $1" < /dev/null
}

fail=0
while IFS=$'\t' read -r bin input expected note; do
  [ "${bin#\#}" = "$bin" ] || continue
  [ -n "$bin" ] || continue
  got=$(run "$bin" "$input" | tr -d '\r')
  if [ "$got" = "$expected" ]; then
    printf 'PASS  %-18s %-10s -> %-10s (%s)\n' "$bin" "$input" "$got" "$note"
  else
    printf 'FAIL  %-18s %-10s -> %-10s expected %-10s (%s)\n' "$bin" "$input" "$got" "$expected" "$note"
    fail=1
  fi
done < expected.tsv

exit $fail
