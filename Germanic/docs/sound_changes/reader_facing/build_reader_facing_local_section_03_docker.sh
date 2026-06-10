#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"

assembled_md="${script_dir}/reader_facing_local_section_03.md"
assembled_pdf="${script_dir}/reader_facing_local_section_03.pdf"

cd "${repo_root}"

python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py

python3 - <<'PY'
from pathlib import Path

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_local_section_03.md"
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
    "063-high-vowel-apocope.md",
    "064-065-post-apocope-tail.md",
    "066-068-syncope-and-degemination-corridor.md",
]

parts: list[str] = [
    "# A local Old English sequence from allophony to late syncope and degemination",
    "",
    "## Introduction",
    "",
    "This section extends the same ordered Old English run through the next small batch of late weak-tail material. It begins with labial allophony and Sievers-law syncope, passes through palatalization, umlaut, and back mutation, then adds the next adjacent chapters on high-vowel apocope, the narrow post-apocope tail, and the later syncope-and-degemination sequence.",
    "",
    "The extension remains deliberately small. No new earlier material is inserted, and no larger late-tail rollout is attempted here. The aim is to keep the existing local stretch intact while making the next few weak-tail relations visible in the same reader-facing format.",
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
    kpsewhich fvextra.sty >/dev/null 2>&1 || tlmgr install fvextra >/dev/null
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_03.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_03.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
