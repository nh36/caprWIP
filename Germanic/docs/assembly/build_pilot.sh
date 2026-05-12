#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"

manifest="${script_dir}/pilot_manifest.tsv"
metadata="${script_dir}/pilot_metadata.yaml"
assembled_md="${script_dir}/pilot_assembled.md"
assembled_tex="${script_dir}/pilot_assembled.tex"
assembled_pdf="${script_dir}/pilot_assembled.pdf"
refs_bib="${repo_root}/docs/refs.bib"

python3 - "${repo_root}" "${manifest}" "${assembled_md}" <<'PY'
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

repo_root = Path(sys.argv[1])
manifest_path = Path(sys.argv[2])
output_path = Path(sys.argv[3])


def normalize_headings(text: str) -> str:
    lines = []
    for line in text.splitlines():
        match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if not match:
            lines.append(line)
            continue
        level = len(match.group(1))
        title = match.group(2)
        if level == 1:
            new_level = 2
        elif level == 2:
            new_level = 3
        elif level == 3:
            new_level = 3
        else:
            new_level = level
        lines.append(f'{"#" * new_level} {title}')
    return "\n".join(lines).strip()


rows = []
with manifest_path.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    rows = list(reader)

parts = [
    "# Germanic Lexeme Report Assembly Pilot 01",
    "",
    "This pilot assembles a small representative subset of the current Germanic model entries for publication-format testing. It preserves entry prose, Pandoc citations, and tables from the source `.model.md` files while normalizing heading levels only in this assembled copy.",
    "",
    "The included entries are listed in `pilot_manifest.tsv` and appear here in stable manifest order. Implementation reports, reviewer checklists, source ledgers, packets, and research notes are intentionally excluded from the assembled body.",
]

for row in rows:
    entry_path = repo_root / row["entry_path"]
    entry_text = entry_path.read_text(encoding="utf-8")
    parts.extend(["", normalize_headings(entry_text)])

output_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
print(f"Generated {output_path}")
PY

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found; unable to build ${assembled_tex##*/} or ${assembled_pdf##*/}." >&2
  exit 127
fi

pandoc "${assembled_md}" \
  --standalone \
  --from=markdown+citations \
  --to=latex \
  --metadata-file="${metadata}" \
  --bibliography="${refs_bib}" \
  --citeproc \
  -o "${assembled_tex}"

echo "Generated ${assembled_tex}"

pdf_engine=""
if command -v xelatex >/dev/null 2>&1; then
  pdf_engine="xelatex"
elif command -v lualatex >/dev/null 2>&1; then
  pdf_engine="lualatex"
fi

if [[ -n "${pdf_engine}" ]]; then
  pandoc "${assembled_md}" \
    --standalone \
    --from=markdown+citations \
    --metadata-file="${metadata}" \
    --bibliography="${refs_bib}" \
    --citeproc \
    --pdf-engine="${pdf_engine}" \
    -o "${assembled_pdf}"
  echo "Generated ${assembled_pdf}"
else
  echo "No Unicode-capable PDF engine found (xelatex/lualatex); skipping PDF generation." >&2
fi
