#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"

assembled_md="${script_dir}/reader_facing_pilot_02.md"
assembled_pdf="${script_dir}/reader_facing_pilot_02.pdf"

cd "${repo_root}"

python3 - <<'PY'
from pathlib import Path

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_pilot_02.md"
chapter_files = [
    "052-velar-palatalization.md",
    "055-056-i-umlaut-core.md",
    "049-pgmc-b-allophony.md",
    "050-pwgmc-sievers-law-syncope.md",
    "051-sk-palatalization.md",
    "053-054-pre-umlaut-bridge-and-w-loss.md",
    "057-j-cluster-coalescence.md",
]
source_note = "source_note_pilot_02.md"

parts: list[str] = [
    "# Reader-facing sound-change pilot 02",
    "",
    "_This assembled pilot PDF preserves the original three reader-facing chapters and appends one small adjacent extension batch._",
    "",
    "## Included sections",
    "",
    "1. Velar palatalization before front vowels",
    "2. The Old English i-umlaut and West Saxon palatal diphthongization",
    "3. Nasal dissimilation",
    "4. B allophony and Sievers-law syncope",
    "5. Palatalization of *sk* to *sc*",
    "6. The pre-umlaut bridge and loss of *w* before *i*",
    "7. J-cluster coalescence",
    "",
]

for idx, name in enumerate(chapter_files):
    if idx:
        parts.extend(["", r"\newpage", ""])
    parts.append((root / name).read_text(encoding="utf-8").rstrip())

parts.extend(["", r"\newpage", "", (root / source_note).read_text(encoding="utf-8").rstrip(), ""])
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
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_02.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_pilot_02.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
