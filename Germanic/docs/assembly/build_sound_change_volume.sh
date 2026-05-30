#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"

assembled_md="${script_dir}/sound_change_volume_alpha_01.md"
assembled_tex="${script_dir}/sound_change_volume_alpha_01.tex"
assembled_pdf="${script_dir}/sound_change_volume_alpha_01.pdf"
metadata="${script_dir}/full_volume_metadata.yaml"
refs_bib="${repo_root}/docs/refs.bib"

# MacTeX commonly installs TeX engines here without updating non-login PATHs.
if [[ -d /Library/TeX/texbin ]] && [[ ":${PATH}:" != *":/Library/TeX/texbin:"* ]]; then
  export PATH="/Library/TeX/texbin:${PATH}"
fi

cd "${repo_root}"

python3 "${script_dir}/build_sound_change_volume.py"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found; regenerated ${assembled_md##*/} only. Skipping ${assembled_tex##*/} and ${assembled_pdf##*/}." >&2
  exit 0
fi

pandoc "${assembled_md}" \
  --standalone \
  --from=markdown+raw_tex+citations \
  --to=latex \
  --metadata-file="${metadata}" \
  --bibliography="${refs_bib}" \
  --citeproc \
  -o "${assembled_tex}"

echo "Generated ${assembled_tex}"

if [[ "${SOUND_CHANGE_BUILD_PDF:-0}" != "1" ]]; then
  echo "Skipping PDF generation by default. Set SOUND_CHANGE_BUILD_PDF=1 to build the PDF locally."
  exit 0
fi

pdf_engine=""
if command -v xelatex >/dev/null 2>&1; then
  pdf_engine="xelatex"
elif command -v lualatex >/dev/null 2>&1; then
  pdf_engine="lualatex"
fi

if [[ -n "${pdf_engine}" ]]; then
  pandoc "${assembled_md}" \
    --standalone \
    --from=markdown+raw_tex+citations \
    --metadata-file="${metadata}" \
    --bibliography="${refs_bib}" \
    --citeproc \
    --pdf-engine="${pdf_engine}" \
    -o "${assembled_pdf}"
  echo "Generated ${assembled_pdf}"
else
  echo "No Unicode-capable PDF engine found (xelatex/lualatex); skipping PDF generation." >&2
fi
