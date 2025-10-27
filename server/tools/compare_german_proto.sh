#!/usr/bin/env bash
# Compare legacy ProtoWord inventory with the new pgrmWord prototype on a small
# lexeme list, and inspect GermanConsonantShift outputs for both paths.
# Usage: server/tools/compare_german_proto.sh [lexeme ...]
set -euo pipefail
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
LEXEMES=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --file)
      shift
      FILE_PATH=${1:-}
      if [[ -z "$FILE_PATH" ]]; then
        echo "--file requires a path" >&2
        exit 1
      fi
      if [[ ! -f "$FILE_PATH" ]]; then
        echo "Lexeme file not found: $FILE_PATH" >&2
        exit 1
      fi
      while IFS= read -r line; do
        [[ -z "$line" ]] && continue
        LEXEMES+=("$line")
      done < "$FILE_PATH"
      shift
      ;;
    *)
      LEXEMES+=("$1")
      shift
      ;;
  esac
done

if [[ ${#LEXEMES[@]} -eq 0 ]]; then
  LEXEMES=("knewą" "braudą" "blōdą" "tōr")
fi
LEXEME_INPUT=$(printf '%s\n' "${LEXEMES[@]}")
CONTAINER_SCRIPT=$(cat <<'EOS'
cd /usr/app
cat <<'FST' > /tmp/compare_german_proto.foma
source fsts/germanic.txt
define RemoveStars {*} -> 0;
regex ProtoWord;
save stack /tmp/protoword.bin
regex pgrmWord .o. RemoveStars;
save stack /tmp/pgrmword.bin
regex ProtoWord .o. GermanConsonantShift;
save stack /tmp/protoword_shift.bin
regex pgrmWord .o. RemoveStars .o. GermanConsonantShift;
save stack /tmp/pgrmword_shift.bin
quit
FST
cat <<'LEX' > /tmp/lexeme_input.txt
EOS
)
CONTAINER_SCRIPT+=$'\n'
CONTAINER_SCRIPT+="$LEXEME_INPUT"
CONTAINER_SCRIPT+=$'\n'
CONTAINER_SCRIPT+=$'LEX\n'
CONTAINER_SCRIPT+=$'foma -f /tmp/compare_german_proto.foma >/tmp/compare_german_proto.log 2>&1\n'
CONTAINER_SCRIPT+=$'printf "== ProtoWord acceptance ==\\n"\n'
CONTAINER_SCRIPT+=$'flookup /tmp/protoword.bin < /tmp/lexeme_input.txt\n'
CONTAINER_SCRIPT+=$'printf "\\n== pgrmWord acceptance (starless projection) ==\\n"\n'
CONTAINER_SCRIPT+=$'flookup /tmp/pgrmword.bin < /tmp/lexeme_input.txt\n'
CONTAINER_SCRIPT+=$'printf "\\n== ProtoWord + GermanConsonantShift ==\\n"\n'
CONTAINER_SCRIPT+=$'flookup /tmp/protoword_shift.bin < /tmp/lexeme_input.txt\n'
CONTAINER_SCRIPT+=$'printf "\\n== pgrmWord + GermanConsonantShift ==\\n"\n'
CONTAINER_SCRIPT+=$'flookup /tmp/pgrmword_shift.bin < /tmp/lexeme_input.txt\n'
docker compose exec backend bash -lc "$CONTAINER_SCRIPT"
