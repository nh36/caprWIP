#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
build_dir="${repo_root}/.capr-work/hay-article-publication"
build_log="${build_dir}/hay-article-build.log"

mkdir -p "${build_dir}"
cd "${repo_root}"

docker run --rm --platform "${platform}" --entrypoint /bin/sh \
  -v "${repo_root}":/data -w /data "${image}" -c "
    set -e
    apk add --no-cache ${font_package} >/dev/null
    pandoc Germanic/articles/hay/DRAFT.md \
      --standalone \
      --from=markdown+raw_tex+citations+footnotes \
      --to=latex \
      --resource-path=Germanic/articles/hay:. \
      --lua-filter=Germanic/tools/reconstructed_form_filter.lua \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/tools/lex_form_filter.lua \
      --lua-filter=Germanic/articles/hay/manuscript_angle_filter.lua \
      --include-in-header=Germanic/docs/assembly/semantic_form_macros.tex \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --citeproc \
      -o .capr-work/hay-article-publication/hay-article.tex
    pandoc Germanic/articles/hay/DRAFT.md \
      --standalone \
      --from=markdown+raw_tex+citations+footnotes \
      --resource-path=Germanic/articles/hay:. \
      --lua-filter=Germanic/tools/reconstructed_form_filter.lua \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/tools/lex_form_filter.lua \
      --lua-filter=Germanic/articles/hay/manuscript_angle_filter.lua \
      --include-in-header=Germanic/docs/assembly/semantic_form_macros.tex \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --citeproc \
      --pdf-engine=xelatex \
      -o .capr-work/hay-article-publication/hay-article.pdf
  " 2>&1 | tee "${build_log}"

if grep -q "Missing character:" "${build_log}"; then
  echo "Missing-glyph warnings found in ${build_log}." >&2
  exit 1
fi

python3 Germanic/tools/check_publication_references.py \
  --tex-path "${build_dir}/hay-article.tex" \
  --log-path "${build_log}" \
  --pdf-path "${build_dir}/hay-article.pdf"

echo "Generated ${build_dir}/hay-article.pdf"
