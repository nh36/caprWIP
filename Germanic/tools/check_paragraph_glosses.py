#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import subprocess

ROOT = Path(__file__).resolve().parent.parent
ASSEMBLED = ROOT / 'Germanic' / 'docs' / 'assembly' / 'capr_book_draft_alpha_01.md'

# Use pandoc to produce JSON AST

def pandoc_json(path: Path):
    p = subprocess.run(['pandoc', str(path), '-t', 'json'], capture_output=True, text=True)
    if p.returncode != 0:
        print('pandoc failed to produce JSON AST', p.stderr)
        sys.exit(2)
    return json.loads(p.stdout)

# Identify italic inlines: In pandoc AST, emphasis is ['Emph', [Inlines...]]

def extract_inlines(ast):
    # walk blocks
    if ast['pandoc-api-version'][0] < 1:
        return []
    blocks = ast['blocks']
    paras = []
    for b in blocks:
        if b['t'] == 'Para':
            paras.append(b['c'])
    return paras

# reconstruct plain text from inline

def stringify(inlines):
    parts = []
    for el in inlines:
        t = el['t']
        c = el.get('c')
        if t == 'Str':
            parts.append(c)
        elif t == 'Space':
            parts.append(' ')
        elif t == 'Emph':
            # recurse
            parts.append('*' + stringify(c) + '*')
        elif t == 'Strong':
            parts.append('**' + stringify(c) + '**')
        elif t == 'Code':
            parts.append('`'+c[1]+'`' if isinstance(c, list) and len(c)>1 else '`'+str(c)+'`')
        elif t == 'Quoted':
            parts.append('"'+stringify(c[1])+'"')
        else:
            # fallback
            try:
                parts.append(str(c))
            except Exception:
                pass
    return ''.join(parts)

# check each paragraph for Emph elements and ensure gloss follows
GLOSS_RE = re.compile(r"^\s*[‘'\"`]?([^’'\"`]+)[’'\"`]?")

def check_paragraphs(ast):
    paras = extract_inlines(ast)
    failures = []
    for idx, inlines in enumerate(paras, start=1):
        seen_forms = set()
        i = 0
        while i < len(inlines):
            el = inlines[i]
            if el['t'] == 'Emph':
                form_text = stringify(el['c'])
                norm = form_text.strip('*')
                if norm in seen_forms:
                    i += 1
                    continue
                seen_forms.add(norm)
                # check following inlines for gloss: immediate next tokens form a quoted gloss
                gloss_ok = False
                j = i+1
                # skip spaces
                while j < len(inlines) and inlines[j]['t']=='Space':
                    j+=1
                if j < len(inlines):
                    nxt = inlines[j]
                    # Str starting with opening quote
                    if nxt['t']=='Str':
                        if re.match(r"^[‘'\"]", nxt['c']):
                            gloss_ok = True
                    if nxt['t']=='Quoted':
                        gloss_ok = True
                if not gloss_ok:
                    failures.append((idx, norm))
            i += 1
    return failures


def main():
    ast = pandoc_json(ASSEMBLED)
    fails = check_paragraphs(ast)
    if fails:
        print('Paragraph-level gloss failures found in assembled book:')
        for para_idx, form in fails[:100]:
            print(f'  Paragraph {para_idx}: {form}')
        print('\nTotal failures:', len(fails))
        sys.exit(2)
    else:
        print('No paragraph-level gloss failures detected.')
        return 0

if __name__ == '__main__':
    raise SystemExit(main())