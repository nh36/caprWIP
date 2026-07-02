#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
tlmgr_repo="${ASSEMBLY_DOCKER_TLMGR_REPOSITORY:-https://ftp.fau.de/ctan/systems/texlive/tlnet}"

intro_md="${script_dir}/capr_book_intro_alpha_01.md"
intro_pdf="${script_dir}/capr_book_intro_alpha_01.pdf"
combined_md="${script_dir}/capr_book_draft_alpha_01.md"
combined_pdf="${script_dir}/capr_book_draft_alpha_01.pdf"
metadata="${script_dir}/full_volume_metadata.yaml"
refs_bib="${repo_root}/docs/refs.bib"

cd "${repo_root}"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker not found; cannot run Docker-based render." >&2
  exit 127
fi

if ! docker info >/dev/null 2>&1; then
  echo "docker daemon not running; start Docker Desktop or another daemon first." >&2
  exit 1
fi

bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh
bash Germanic/docs/assembly/build_full_lexical_volume_docker.sh

python3 - <<'PY'
from pathlib import Path
root = Path("Germanic/docs/assembly")
intro = (root / "capr_book_intro_alpha_01.md").read_text(encoding="utf-8").rstrip()
chronology = Path("Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md").read_text(encoding="utf-8")
lexical = (root / "lexical_volume_alpha_01.md").read_text(encoding="utf-8").rstrip()
marker = "\n# References\n"
if marker in chronology:
    chronology = chronology.split(marker, 1)[0]
parts = [intro, r"\newpage", chronology.rstrip(), r"\newpage", lexical, "# References", "", "::: {#refs}", ":::"]
(root / "capr_book_draft_alpha_01.md").write_text("\n\n".join(parts) + "\n", encoding="utf-8")
PY

docker run --rm --platform "${platform}" --entrypoint /bin/sh \
  -v "${repo_root}":/data -w /data "${image}" -c "
    set -e
    apk add --no-cache ${font_package} >/dev/null
    kpsewhich fvextra.sty >/dev/null 2>&1 || (
      tlmgr option repository ${tlmgr_repo} >/dev/null &&
      tlmgr update --self >/dev/null &&
      tlmgr install fvextra >/dev/null
    )
    pandoc ${intro_md#${repo_root}/} --standalone --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/assembly/book_draft_pdf_header.tex \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --metadata-file=${metadata#${repo_root}/} --bibliography=${refs_bib#${repo_root}/} --citeproc \
      --pdf-engine=xelatex -o ${intro_pdf#${repo_root}/}
    pandoc ${combined_md#${repo_root}/} --standalone --from=markdown+raw_tex+citations --table-of-contents \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/assembly/book_draft_pdf_header.tex \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --metadata-file=${metadata#${repo_root}/} --bibliography=${refs_bib#${repo_root}/} --citeproc \
      --pdf-engine=xelatex -o ${combined_pdf#${repo_root}/}
  "

echo "Generated ${intro_pdf}"
echo "Generated ${combined_md}"
echo "Generated ${combined_pdf}"
