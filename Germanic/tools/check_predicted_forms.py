#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
# Scan reader-facing source files for counterfactual patterns
SOURCE_DIR = ROOT / 'docs' / 'sound_changes' / 'reader_facing'
ASSEMBLED = ROOT / 'docs' / 'assembly' / 'capr_book_draft_alpha_01.md'

# Look for typical counterfactual patterns where a predicted form appears before/after 'yields' and contrasted with 'rather than' or 'instead of'
PATTERN = re.compile(r"yields?\s+(?P<form>\*[^*]+\*)\s+(?:rather than|instead of|rather than the expected|rather than expected)", re.IGNORECASE)

# Predicted marker: raw LaTeX macro \Pred{...} should be present immediately before form
PRED_MARK = r"\\Pred"


def scan():
    text = ASSEMBLED.read_text(encoding='utf-8')
    issues = []
    for m in PATTERN.finditer(text):
        form = m.group('form')
        start = m.start('form')
        # check preceding characters for \Pred
        prefix = text[max(0, start-20):start]
        if PRED_MARK not in prefix:
            # find line number
            line_no = text[:start].count('\n') + 1
            issues.append((line_no, form))
    return issues


def main():
    issues = scan()
    if issues:
        print('Found unmarked counterfactual predicted forms in assembled book:')
        for ln, form in issues:
            print(f'  Line {ln}: {form}')
        print('\nThese predicted outputs should be marked with the \Pred{...} macro in the source.')
        sys.exit(2)
    else:
        print('No unmarked predicted forms found in assembled book.')
        return 0

if __name__ == "__main__":
    raise SystemExit(main())