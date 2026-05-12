#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"

cd "${repo_root}"

bash "${script_dir}/build_pilot.sh"

if ! command -v docker >/dev/null 2>&1; then
  echo "docker not found; cannot run Docker-based render." >&2
  exit 127
fi

if ! docker info >/dev/null 2>&1; then
  echo "docker daemon not running; start Docker Desktop or another daemon first." >&2
  exit 1
fi

docker run --rm --platform "${platform}" --entrypoint /bin/sh \
  -v "${repo_root}":/data -w /data "${image}" -c "
    set -e
    apk add --no-cache ${font_package} >/dev/null
    pandoc Germanic/docs/assembly/pilot_assembled.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --to=latex \
      --metadata-file=Germanic/docs/assembly/pilot_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      -o Germanic/docs/assembly/pilot_assembled.tex
    pandoc Germanic/docs/assembly/pilot_assembled.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --metadata-file=Germanic/docs/assembly/pilot_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/assembly/pilot_assembled.pdf
  "

echo "Generated ${script_dir}/pilot_assembled.tex"
echo "Generated ${script_dir}/pilot_assembled.pdf"
