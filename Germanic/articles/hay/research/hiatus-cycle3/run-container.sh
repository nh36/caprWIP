#!/usr/bin/env bash
set -euo pipefail

base=113101ac5f169b589e1a9647cdf24d32cdd4d919
intake=f220d31157eaa10fcb9a3785ac349bdfac8d6c22
previous=fb1d39abab2420faa90ef7bd4a19751ac4a17321
prior=Germanic/articles/hay/research/hiatus
cycle2=$prior-cycle2
cycle3=$prior-cycle3
mode=integrated
files=(integrated.py)
case "${1:-}" in
    --representation) mode=representation; files=(representation.py); shift ;;
    --chronology) mode=chronology; files+=(chronology.py representation.py); shift ;;
    --back-vowels) mode=back_vowels; files+=(back_vowels.py); shift ;;
    --later-h) mode=later_h; files+=(later_h.py); shift ;;
    --revised) mode=revised; files+=(revised.py chronology.py representation.py later_h.py
                                    back_vowels.py holdouts-v1.tsv); shift ;;
esac

tmp=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-cycle3.XXXXXXXX)
case "$tmp" in
    /tmp/capr-hay-cycle3.*) ;;
    *) exit 1 ;;
esac
trap 'docker compose exec -T backend python -c "from pathlib import Path; import shutil,sys; p=Path(sys.argv[1]); assert p.parent == Path(\"/tmp\") and p.name.startswith(\"capr-hay-cycle3.\"); shutil.rmtree(p)" "$tmp"' EXIT

git archive "$base" Germanic/tools Germanic/fsts/germanic.txt \
    Germanic/docs/models/sc047/cells.tsv \
    Germanic/docs/models/sc047/captures/sc047-adoption-v1.json.gz \
    Germanic/docs/sound_changes/registry/sc_registry.tsv \
    Germanic/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/labial_review/plan.json \
    Germanic/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/parallel/observations.json.gz \
    backend/oe_input_context.py |
    docker compose exec -T backend tar -xf - -C "$tmp"
git archive "$intake" "$prior" |
    docker compose exec -T backend tar -xf - -C "$tmp"
git archive "$previous" "$cycle2" |
    docker compose exec -T backend tar -xf - -C "$tmp"
docker compose exec -T backend mkdir "$tmp/cycle3"
tar -cf - -C "$cycle3" "${files[@]}" |
    docker compose exec -T backend tar -xf - -C "$tmp/cycle3"
docker compose exec -T backend env PYTHONDONTWRITEBYTECODE=1 \
    python "$tmp/cycle3/$mode.py" "$tmp" "$@"
