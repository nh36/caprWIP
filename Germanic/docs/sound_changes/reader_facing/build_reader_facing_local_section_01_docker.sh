#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"

assembled_md="${script_dir}/reader_facing_local_section_01.md"
assembled_pdf="${script_dir}/reader_facing_local_section_01.pdf"

cd "${repo_root}"

python3 - <<'PY'
from pathlib import Path

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_local_section_01.md"
chapter_files = [
    "049-pgmc-b-allophony.md",
    "050-pwgmc-sievers-law-syncope.md",
    "051-sk-palatalization.md",
    "052-velar-palatalization.md",
    "053-054-pre-umlaut-bridge-and-w-loss.md",
    "055-056-i-umlaut-core.md",
    "057-j-cluster-coalescence.md",
    "058-nasal-dissimilation.md",
]

parts: list[str] = [
    "# A local Old English sequence from allophony to nasal dissimilation",
    "",
    "## Introduction",
    "",
    "This section follows one local stretch of the Old English sound-change sequence. It begins with the positional behavior of Germanic *b and the syncope traditionally associated with Sievers' Law, then moves through the palatalization of *sk and plain velars, through the small glide-loss bridge that stands immediately before the umlautal core, and closes with later j-cluster coalescence and the narrow nasal-dissimilation tendency.",
    "",
    "The scale remains deliberately local. Some of the chapters here treat major consonantal or vocalic developments; others keep smaller linking changes in view so that the reader can move through one continuous part of the sequence without losing the narrower steps that prepare the larger outcomes.",
    "",
]

for idx, name in enumerate(chapter_files):
    if idx:
        parts.extend(["", r"\newpage", ""])
    parts.append((root / name).read_text(encoding="utf-8").rstrip())

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
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_01.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_01.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
