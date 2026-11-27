#!/usr/bin/env bash
set -euo pipefail

base=113101ac5f169b589e1a9647cdf24d32cdd4d919
intake=f220d31157eaa10fcb9a3785ac349bdfac8d6c22
prior=Germanic/articles/hay/research/hiatus
cycle=Germanic/articles/hay/research/hiatus-cycle2
mode=reproduce_stress
files=(reproduce_stress.py stress-panel.tsv)
case "${1:-}" in
    --repairs) mode=stress_repairs; files+=(stress_repairs.py); shift ;;
    --census) mode=stress_census; files+=(stress_census.py stress_repairs.py); shift ;;
    --couch) mode=couch; files+=(couch.py stress_repairs.py); shift ;;
    --panel) mode=panel; files+=(panel.py panel.tsv stress_repairs.py); shift ;;
    --matched) mode=matched; files+=(matched.py panel.py panel.tsv stress_repairs.py); shift ;;
    --quantity) mode=quantity; files+=(quantity.py matched.py panel.py panel.tsv stress_repairs.py); shift ;;
esac

tmp=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-cycle2.XXXXXXXX)
case "$tmp" in
    /tmp/capr-hay-cycle2.*) ;;
    *) exit 1 ;;
esac
trap 'docker compose exec -T backend python -c "from pathlib import Path; import shutil,sys; p=Path(sys.argv[1]); assert p.parent == Path(\"/tmp\") and p.name.startswith(\"capr-hay-cycle2.\"); shutil.rmtree(p)" "$tmp"' EXIT

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
docker compose exec -T backend mkdir "$tmp/cycle2"
tar -cf - -C "$cycle" "${files[@]}" |
    docker compose exec -T backend tar -xf - -C "$tmp/cycle2"
docker compose exec -T backend env PYTHONDONTWRITEBYTECODE=1 \
    python "$tmp/cycle2/$mode.py" "$tmp" "$@"
