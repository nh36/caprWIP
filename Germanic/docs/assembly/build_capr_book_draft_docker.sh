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
combined_tex="${script_dir}/capr_book_draft_alpha_01.tex"
combined_pdf="${script_dir}/capr_book_draft_alpha_01.pdf"
intro_metadata="${script_dir}/full_volume_metadata.yaml"
book_metadata="${script_dir}/book_draft_metadata.yaml"
refs_bib="${repo_root}/docs/refs.bib"
strict_flag=""

if [[ "${INDEX_VERBORUM_STRICT:-0}" == "1" ]]; then
  strict_flag="--strict-mode baseline"
fi

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

python3 Germanic/tools/build_index_verborum.py ${strict_flag}
python3 "${script_dir}/build_capr_book_draft.py"
# source-level bibliographic locator check: flags literal 'sect'/'sects' in Markdown sources
python3 Germanic/tools/check_bibliographic_section_locators.py
# assembled-markdown checks: predicted-form markers and paragraph-level glosses
# run them but don't hard-fail here; docker LaTeX stage will enforce post-render checks
python3 Germanic/tools/check_predicted_forms.py || true
python3 Germanic/tools/check_paragraph_glosses.py || true
python3 Germanic/tools/check_index_verborum.py
python3 Germanic/tools/check_bibliography_sanity.py

docker run --rm --platform "${platform}" --entrypoint /bin/sh \
  -v "${repo_root}":/data -w /data "${image}" -c "
    set -e
    apk add --no-cache ${font_package} >/dev/null
    kpsewhich fvextra.sty >/dev/null 2>&1 || (
      tlmgr option repository ${tlmgr_repo} >/dev/null &&
      tlmgr update --self >/dev/null &&
      tlmgr install fvextra >/dev/null
    )
    kpsewhich imakeidx.sty >/dev/null 2>&1 || tlmgr install imakeidx >/dev/null
    kpsewhich morewrites.sty >/dev/null 2>&1 || tlmgr install morewrites >/dev/null
    kpsewhich xkeyval.sty >/dev/null 2>&1 || tlmgr install xkeyval >/dev/null
    pandoc ${intro_md#${repo_root}/} --standalone --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --metadata-file=${intro_metadata#${repo_root}/} --bibliography=${refs_bib#${repo_root}/} --citeproc \
      --pdf-engine=xelatex -o ${intro_pdf#${repo_root}/}
    pandoc ${combined_md#${repo_root}/} --standalone --from=markdown+raw_tex+citations --to=latex \
      --top-level-division=chapter --number-sections --table-of-contents --toc-depth=1 \
      --lua-filter=Germanic/tools/index_verborum_filter.lua \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/assembly/book_draft_pdf_header.tex \
      --include-in-header=Germanic/docs/assembly/book_draft_index_registry.tex \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --metadata-file=${book_metadata#${repo_root}/} --bibliography=${refs_bib#${repo_root}/} --citeproc \
      -o ${combined_tex#${repo_root}/}
    # post-process generated LaTeX to replace citeproc 'sect'/'sects' labels with §/§§
    sed -E -i "s/\\bsects?\\.?\\s+([0-9]+)/§§ \1/g" ${combined_tex#${repo_root}/} || true
    sed -E -i "s/§§\s+§§/§§ /g" ${combined_tex#${repo_root}/} || true
    sed -E -i "s/\bsect\.\s+/§ /g" ${combined_tex#${repo_root}/} || true
    sed -E -i "s/\bsect\s+([0-9]+)/§ \1/g" ${combined_tex#${repo_root}/} || true
    # post-render predicted-form sanity check: ensure patterns like "yields ... \emph{FORM} ... rather than" have a \Pred macro before the predicted form
    perl -0777 -ne 'while(/yields[^{]*\\emph\{([^}]+)\}[^}]*?rather than/sgi){ my $s=$&; if($s !~ /\\\Pred/){ print "UNMARKED PREDICTED FORM: $1\n"; exit 2 } }' ${combined_tex#${repo_root}/}
    cd Germanic/docs/assembly
    xelatex -interaction=nonstopmode -halt-on-error capr_book_draft_alpha_01.tex >/dev/null
    for idx in capr_book_draft_alpha_01*.idx; do
      [ -e \"\$idx\" ] || continue
      makeindex -o \"\${idx%.idx}.ind\" \"\$idx\" >/dev/null
    done
    xelatex -interaction=nonstopmode -halt-on-error capr_book_draft_alpha_01.tex >/dev/null
    xelatex -interaction=nonstopmode -halt-on-error capr_book_draft_alpha_01.tex >/dev/null
  "

python3 Germanic/tools/check_book_draft_tex_indexes.py --tex-path "${combined_tex}"
python3 Germanic/tools/check_sound_change_heading_wrapping.py \
  --markdown-path "${repo_root}/Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md" \
  --tex-path "${combined_tex}"
python3 Germanic/tools/check_print_index_ready.py --tex-path "${combined_tex}"

echo "Generated ${intro_pdf}"
echo "Generated ${combined_md}"
echo "Generated ${combined_pdf}"

rm -f "${combined_tex}" \
  "${script_dir}/capr_book_draft_alpha_01.aux" \
  "${script_dir}/capr_book_draft_alpha_01.log" \
  "${script_dir}/capr_book_draft_alpha_01.toc" \
  "${script_dir}"/*.idx "${script_dir}"/*.ind "${script_dir}"/*.ilg
