#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
tlmgr_repo="${ASSEMBLY_DOCKER_TLMGR_REPOSITORY:-https://ftp.fau.de/ctan/systems/texlive/tlnet}"

assembled_md="${script_dir}/reader_facing_local_section_11.md"
assembled_pdf="${script_dir}/reader_facing_local_section_11.pdf"

cd "${repo_root}"

python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py

python3 - <<'PY'
from pathlib import Path
import re

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_local_section_11.md"
chapter_files = [
    "026-027-nasal-spirant-changes.md",
    "028-preconsonantal-x-loss.md",
    "029-030-awj-glide-and-au-fronting.md",
    "031-034-west-saxon-diphthong-chain.md",
    "035-037-prefix-and-compound-adjustments.md",
    "039-040-medial-unstressed-vowel-changes.md",
    "041-final-bare-a-loss.md",
    "042-surviving-bimoric-o-unrounding.md",
    "043-anglo-frisian-brightening.md",
    "044-045-breaking-and-velar-fricative-palatalization.md",
    "046-048-restoration-and-nasal-tail-changes.md",
    "049-pgmc-b-allophony.md",
    "050-pwgmc-sievers-law-syncope.md",
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
    "069-early-o-shortening-context-note.md",
    "070-071-early-unstressed-fronting-shortening-bridge.md",
    "072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md",
    "074-075-medial-unstressed-i-lowering.md",
    "076-prefix-i-reduction.md",
    "078-weak-tail-reduction.md",
    "079-080-final-j-loss-and-final-geminate-simplification.md",
    "081-083-j-strengthening-vocalization-and-ei-contraction.md",
    "085-086-h-loss-and-contraction.md",
    "087-r-metathesis.md",
]
rule_heading_re = re.compile(r"^##\s+SC\d{3}\..*\{#(rule-[^}]+)\}\s*$")
link_re = re.compile(r"\[([^\]]+)\]\((#rule-[^)]+)\)")

parts: list[str] = [
    "# An Old English sequence from nasal spirant changes to r-metathesis",
    "",
    "## Introduction",
    "",
    "This section follows an ordered stretch of Old English sound changes from nasal spirant changes, preconsonantal x-loss, awj glide formation, au-fronting, and the West Saxon diphthong sequence through brightening, breaking, restoration, palatalization, weak-tail reduction, contraction, and r-metathesis.",
    "",
    "Some chapters treat broad vowel histories, while others record smaller rules whose value lies in the witness words that fix their place within the finite-state sequence.",
    "",
]
active_anchors: set[str] = set()
for name in chapter_files:
    for line in (root / name).read_text(encoding="utf-8").splitlines():
        match = rule_heading_re.match(line.strip())
        if match:
            active_anchors.add(f"#{match.group(1)}")


def resolve_links(text: str) -> str:
    return link_re.sub(lambda match: match.group(0) if match.group(2) in active_anchors else match.group(1), text)

for idx, name in enumerate(chapter_files):
    if idx:
        parts.extend(["", r"\newpage", ""])
    parts.append(resolve_links((root / name).read_text(encoding="utf-8").rstrip()))

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
    kpsewhich fvextra.sty >/dev/null 2>&1 || (
      tlmgr option repository ${tlmgr_repo} >/dev/null &&
      tlmgr install fvextra >/dev/null
    )
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_11.md \
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
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_11.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
