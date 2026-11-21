#!/usr/bin/env bash
set -euo pipefail

preview=.capr-work/sc047-parallel/book
assembly=Germanic/docs/assembly
reader=Germanic/docs/sound_changes/reader_facing
tools=Germanic/tools

python3 "$assembly/build_sc047_preview.py"
pandoc "$preview/preview.md" --standalone --from=markdown+raw_tex+citations --to=latex \
  --top-level-division=chapter --number-sections --table-of-contents --toc-depth=1 \
  --lua-filter="$tools/paragraph_gloss_validator.lua" \
  --lua-filter="$tools/index_verborum_filter.lua" \
  --lua-filter="$tools/predicted_form_filter.lua" \
  --lua-filter="$tools/reconstructed_form_filter.lua" \
  --lua-filter="$tools/lex_form_filter.lua" \
  --lua-filter="$reader/reader_facing_foma.lua" \
  --include-in-header="$assembly/book_draft_pdf_header.tex" \
  --include-in-header="$assembly/book_draft_index_registry.tex" \
  --include-in-header="$reader/reader_facing_pdf_header.tex" \
  --metadata-file="$assembly/book_draft_metadata.yaml" \
  --variable="monofont:${SC047_PREVIEW_MONOFONT:-Noto Sans Mono}" \
  --bibliography=docs/refs.bib --bibliography="$assembly/sc047_preview/supplement.bib" \
  --citeproc -o "$preview/preview.tex" 2>"$preview/pandoc.log"
python3 "$tools/normalize_citeproc_section_locators.py" --tex-path "$preview/preview.tex"

cd "$preview"
xelatex -interaction=nonstopmode -halt-on-error preview.tex >xelatex.log
if [ -s iv.idx ]; then
  makeindex -o iv.ind iv.idx >makeindex.log 2>&1
fi
xelatex -interaction=nonstopmode -halt-on-error preview.tex >>xelatex.log
xelatex -interaction=nonstopmode -halt-on-error preview.tex >>xelatex.log
