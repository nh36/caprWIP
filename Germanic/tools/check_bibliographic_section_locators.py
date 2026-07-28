#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(r"\bsects?\.?\b", re.IGNORECASE)
# Files to skip (documentation and helpers)
SKIP_NAMES = {"style_guide.md", "README.md"}

def scan_file(path: Path):
    text = path.read_text(encoding='utf-8')
    hits = []
    for i, line in enumerate(text.splitlines(), start=1):
        if PATTERN.search(line):
            hits.append((i, line.strip()))
    return hits


def main():
    md_files = list(ROOT.glob('**/*.md'))
    total_hits = 0
    report = []
    for f in md_files:
        if f.name in SKIP_NAMES:
            continue
        hits = scan_file(f)
        if hits:
            report.append((f.relative_to(ROOT), hits))
            total_hits += len(hits)
    if report:
        print('Found bibliographic section-locator tokens (sect/sects) in source files:')
        for fp, hits in report:
            print(f'\nFile: {fp}')
            for ln, line in hits[:10]:
                print(f'  {ln}: {line}')
            if len(hits) > 10:
                print(f'  ... ({len(hits)-10} more)')
        print()
        print('Please replace bibliographic locator labels with §/§§ or use explicit § markers in citation suffixes.')
        sys.exit(2)
    else:
        print('No sect/sects tokens found in source Markdown.')
        return 0

if __name__ == '__main__':
    raise SystemExit(main())