#!/usr/bin/env bash
set -euo pipefail

base=113101ac5f169b589e1a9647cdf24d32cdd4d919
intake=f220d31157eaa10fcb9a3785ac349bdfac8d6c22
previous=5a480e470c19c8877d23b428bad89772f22192d3
prior=Germanic/articles/hay/research/hiatus
research=$prior-cycle4
mode="${1:?Specify a research replay mode}"
shift
case "$mode" in
    component_check) files=(components.py component_check.py) ;;
    quantity_check) files=(components.py component_check.py quantity_check.py) ;;
    source_entry_check) files=(components.py component_check.py quantity_check.py source_entry_check.py) ;;
    stress_handoff) files=(components.py component_check.py stress_handoff.py) ;;
    nucleus_check) files=(components.py component_check.py nucleus_check.py) ;;
    medial_hw_check) files=(components.py component_check.py medial_hw_check.py) ;;
    *) printf 'Unknown research replay mode: %s\n' "$mode" >&2; exit 2 ;;
esac

tmp=$(docker compose exec -T backend mktemp -d /tmp/capr-hay-cycle4.XXXXXXXX)
case "$tmp" in
    /tmp/capr-hay-cycle4.*) ;;
    *) exit 1 ;;
esac
trap 'docker compose exec -T backend python -c "from pathlib import Path; import shutil,sys; p=Path(sys.argv[1]); assert p.parent == Path(\"/tmp\") and p.name.startswith(\"capr-hay-cycle4.\"); shutil.rmtree(p)" "$tmp"' EXIT

git archive "$base" Germanic/tools Germanic/fsts/germanic.txt \
    Germanic/docs/models/sc047/cells.tsv \
    Germanic/docs/models/sc047/captures/sc047-adoption-v1.json.gz \
    Germanic/docs/sound_changes/registry/sc_registry.tsv \
    Germanic/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/labial_review/plan.json \
    Germanic/docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/parallel/observations.json.gz \
    backend/oe_input_context.py |
    docker compose exec -T backend tar -xf - -C "$tmp"
git archive "$intake" "$prior" | docker compose exec -T backend tar -xf - -C "$tmp"
git archive "$previous" "$prior-cycle2" "$prior-cycle3" |
    docker compose exec -T backend tar -xf - -C "$tmp"
docker compose exec -T backend mkdir "$tmp/cycle4"
tar -cf - -C "$research" "${files[@]}" | docker compose exec -T backend tar -xf - -C "$tmp/cycle4"
docker compose exec -T backend env PYTHONDONTWRITEBYTECODE=1 \
    python "$tmp/cycle4/$mode.py" "$tmp" "$@"
