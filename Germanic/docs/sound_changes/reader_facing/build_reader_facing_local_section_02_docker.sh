#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"

assembled_md="${script_dir}/reader_facing_local_section_02.md"
assembled_pdf="${script_dir}/reader_facing_local_section_02.pdf"

cd "${repo_root}"

python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh

python3 - <<'PY'
from pathlib import Path

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_local_section_02.md"
chapter_files = [
    "049-050-b-allophony-and-sievers-law-syncope.md",
    "051-sk-palatalization.md",
    "052-velar-palatalization.md",
    "053-054-pre-umlaut-bridge-and-w-loss.md",
    "055-056-i-umlaut-core.md",
    "057-j-cluster-coalescence.md",
    "058-nasal-dissimilation.md",
    "059-oe-back-mutation.md",
    "060-ws-palatal-umlaut-note.md",
    "061-weak-tail-nasal-loss-note.md",
]

parts: list[str] = [
    "# A local Old English sequence from allophony to weak-tail nasal loss",
    "",
    "## Introduction",
    "",
    "This section continues the same local stretch of the Old English sound-change sequence. It begins with labial allophony and Sievers-law syncope, moves through palatalization, the narrow glide-loss bridge before umlaut, and the main umlautal chapter, then turns into the later sequence of j-cluster coalescence, nasal dissimilation, back mutation, and two short weak-tail notes.",
    "",
    "The sequence is continuous without pretending to be one single historical law. Some chapters here carry substantial consonantal or vocalic developments; others remain brief because they preserve smaller linking steps whose historical range is narrower.",
    "",
]

for idx, name in enumerate(chapter_files):
    if idx:
        parts.extend(["", r"\newpage", ""])
    parts.append((root / name).read_text(encoding="utf-8").rstrip())

parts.extend([
    "",
    r"\newpage",
    "",
    "# References",
    "",
    "::: {#refs}",
    ":::",
    "",
])

out.write_text("\n".join(parts), encoding="utf-8")
PY

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
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_02.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_02.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
