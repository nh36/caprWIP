#!/usr/bin/env bash
set -euo pipefail

base=113101ac5f169b589e1a9647cdf24d32cdd4d919
intake=f220d31157eaa10fcb9a3785ac349bdfac8d6c22
prior=Germanic/articles/hay/research/hiatus
cycle=Germanic/articles/hay/research/hiatus-cycle2

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
tar -cf - -C "$cycle" reproduce_stress.py |
    docker compose exec -T backend tar -xf - -C "$tmp/cycle2"
docker compose exec -T backend env PYTHONDONTWRITEBYTECODE=1 \
    python "$tmp/cycle2/reproduce_stress.py" "$tmp" "$@"
