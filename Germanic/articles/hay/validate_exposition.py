#!/usr/bin/env python3
"""Check the hay article's research-only Markdown cross-references."""

import argparse
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
BASE_MODEL = "ARGUMENT_CYCLE12.md"
MODEL = "ARGUMENT_CYCLE13.md"
ARCHITECTURE = "RHETORICAL_ARCHITECTURE.md"
PLAN = "PARAGRAPH_PLAN.md"
APPARATUS = "SCHOLARLY_APPARATUS.md"
DRAFT = "DRAFT.md"
IMPLEMENTED = {
    "R1": ("## 1.1 The chronological test", "## 1.2 The two regular derivations"),
    "R2": ("## 1.2 The two regular derivations", "# 2. The Old English attestations"),
    "R3": ("## 2.1 *Cyniges heiweg*", "## 2.2 Simplex forms"),
    "R4": ("## 2.2 Simplex forms", "# 3. Historical phonology"),
    "R5": ("# 3. Historical phonology", "## 3.3 Orthography and vowel quantity"),
}
ANCHOR = re.compile(r"^<!-- (pending:)?(P-[a-z-]+) -->$", re.MULTILINE)


def rows(text, pattern, width):
    result = {}
    for line in text.splitlines():
        if not (line.startswith("|") and line.endswith("|")):
            continue
        key, *cells = (cell.strip() for cell in line[1:-1].split("|"))
        match = re.fullmatch(pattern, key)
        if not match:
            continue
        key = match[1]
        if key in result:
            raise ValueError(f"duplicate ID: {key}")
        if len(cells) != width or not all(cells):
            raise ValueError(f"{key}: expected {width} populated cells")
        result[key] = cells
    if not result:
        raise ValueError(f"missing table for {pattern}")
    return result


def ids(cell):
    return [] if cell == "—" else cell.split(", ")


def check_refs(owner, refs, target):
    if len(refs) != len(set(refs)):
        raise ValueError(f"{owner}: duplicate reference")
    unknown = set(refs) - target.keys()
    if unknown:
        raise ValueError(f"{owner}: unknown reference(s): {', '.join(sorted(unknown))}")


def check_cycles(graph):
    active, done = set(), set()

    def visit(key):
        if key in active:
            raise ValueError(f"dependency cycle through {key}")
        if key not in done:
            active.add(key)
            for ref in graph.get(key, ()):
                visit(ref)
            active.remove(key)
            done.add(key)

    for key in graph:
        visit(key)


def load():
    def read(name):
        return (ROOT / name).read_text(encoding="utf-8")

    def require_links(name, *targets):
        text = read(name)
        for target in targets:
            if not (ROOT / target).is_file() or f"]({target})" not in text:
                raise ValueError(f"{name}: missing authority link to {target}")
        return text

    historical, marker, index = require_links(MODEL, BASE_MODEL).partition(
        "\n## Dependency index\n"
    )
    if not marker:
        raise ValueError(f"{MODEL}: missing Dependency index")
    base = read(BASE_MODEL)
    evidence = rows(base, r"(E\d+)", 3)
    added = rows(historical.split("## Evidence split for editorial traceability")[0],
                 r"(E\d+)", 3)
    added_split = rows(historical.split("## Evidence split for editorial traceability")[1],
                       r"(E\d+)", 2)
    for group in (added, added_split):
        check_unique = evidence.keys() & group.keys()
        if check_unique:
            raise ValueError(f"duplicate evidence: {', '.join(sorted(check_unique))}")
        evidence.update(group)
    conclusions = rows(base, r"(C\d+)\s+.+", 2)
    for key in re.findall(r"^- \*\*(C\d+),", historical, re.MULTILINE):
        if key in conclusions and key != "C09":
            raise ValueError(f"duplicate conclusion: {key}")
        if key != "C09":  # Its formulation is maintained, not assigned a new ID.
            conclusions[key] = []
    histories = rows(base, r"(H\d+)\s+.+", 2)
    claims = evidence | conclusions | histories
    deps = {key: tuple(map(ids, cells))
            for key, cells in rows(index, r"([ECH]\d+)", 3).items()}
    for key in conclusions.keys() | histories.keys():
        if key not in deps or not any(deps[key][:2]):
            raise ValueError(f"{key}: missing necessary dependency")
    for key, groups in deps.items():
        check_refs(key, [key], claims)
        check_refs(key, [ref for group in groups for ref in group], claims)
    check_cycles({key: required + either
                  for key, (required, either, _) in deps.items()})

    require_links("BASELINE.md", MODEL, "THESIS.md", ARCHITECTURE, PLAN, APPARATUS)
    require_links("THESIS.md", MODEL)
    blocks = rows(require_links(ARCHITECTURE, MODEL, PLAN), r"(R\d+)\s+.+", 5)
    plan = require_links(PLAN, MODEL, ARCHITECTURE, APPARATUS)
    paragraphs = rows(plan, r"(P-[a-z-]+)", 5)
    loci = rows(plan, r"(C\d+)", 1)
    apparatus = rows(require_links(APPARATUS, MODEL, PLAN), r"([TNA]-[a-z-]+)", 3)
    used_claims, used_blocks = set(), []
    for key, (block, _, refs, _, _) in paragraphs.items():
        check_refs(key, [block], blocks)
        check_refs(key, ids(refs), claims)
        if not ids(refs):
            raise ValueError(f"{key}: missing claim")
        used_claims.update(ids(refs))
        if not used_blocks or used_blocks[-1] != block:
            used_blocks.append(block)
    if used_blocks != list(blocks):
        raise ValueError("uncovered, split, or out-of-order rhetorical block")
    if missing := claims.keys() - used_claims:
        raise ValueError(f"no planned exposition for: {', '.join(sorted(missing))}")
    check_refs("Principal exposition loci", list(loci), conclusions)
    if missing := conclusions.keys() - loci.keys():
        raise ValueError(f"no principal exposition locus for: {', '.join(sorted(missing))}")
    for key, (anchors,) in loci.items():
        covered = {p: None for p, cells in paragraphs.items() if key in ids(cells[2])}
        if not ids(anchors):
            raise ValueError(f"{key}: empty principal exposition locus")
        check_refs(key, ids(anchors), covered)
    for key, (anchors, refs, _) in apparatus.items():
        check_refs(key, ids(anchors), paragraphs)
        planned = {ref: None for p in ids(anchors) for ref in ids(paragraphs[p][2])}
        if not ids(refs) or not planned:
            raise ValueError(f"{key}: apparatus needs an anchor and a claim")
        check_refs(key, ids(refs), planned)
    return claims, deps, blocks, paragraphs, apparatus, loci


def section_bounds(text, start, end):
    a = re.search(rf"^{re.escape(start)}$", text, re.MULTILINE)
    b = re.search(rf"^{re.escape(end)}$", text, re.MULTILINE)
    if not a or not b or a.start() >= b.start():
        raise ValueError(f"{DRAFT}: invalid boundaries {start!r}, {end!r}")
    return a.start(), b.start()


def without_scope(text, scope, paragraphs):
    ranges = []
    for block, boundaries in IMPLEMENTED.items():
        start, end = section_bounds(text, *boundaries)
        if block in scope:
            ranges.append((start, end))
            continue
        begin = text.index("\n", start) + 1
        anchors = list(ANCHOR.finditer(text, begin, end))
        for i, anchor in enumerate(anchors):
            key = anchor[2]
            if key in scope:
                if key not in paragraphs or paragraphs[key][0] != block:
                    raise ValueError(f"{DRAFT}: {key} outside its planned block")
                ranges.append((anchor.start(), anchors[i + 1].start()
                               if i + 1 < len(anchors) else end))
    for start, end in sorted(ranges, reverse=True):
        text = text[:start] + text[end:]
    return text


def check_article(text, paragraphs, baseline=None, scope=(), complete=()):
    expected = []
    pending = []
    for block, boundaries in IMPLEMENTED.items():
        start, end = section_bounds(text, *boundaries)
        planned = [key for key, cells in paragraphs.items() if cells[0] == block]
        found = ANCHOR.findall(text[start:end])
        if [key for _, key in found] != planned:
            raise ValueError(f"{DRAFT}: {block} anchors {found}; expected {planned}")
        states = [key for status, key in found if status]
        if states:
            if block in complete or states != planned[-len(states):]:
                raise ValueError(f"{DRAFT}: unexpected pending units in {block}: {states}")
            pending.extend(states)
        expected.extend(found)
    if ANCHOR.findall(text) != expected:
        raise ValueError(f"{DRAFT}: anchor outside implemented scope")
    if baseline is not None:
        previously_implemented = {key for status, key in ANCHOR.findall(baseline)
                                  if not status}
        if previously_implemented.intersection(pending):
            raise ValueError(f"{DRAFT}: implemented units cannot return to pending")
        for key in scope:
            if key not in IMPLEMENTED and key not in paragraphs:
                raise ValueError(f"{DRAFT}: unknown scope {key}")
            block = key if key in IMPLEMENTED else paragraphs[key][0]
            if block not in IMPLEMENTED:
                raise ValueError(f"{DRAFT}: no source boundaries for {key}")
        if without_scope(text, scope, paragraphs) != without_scope(baseline, scope, paragraphs):
            raise ValueError(f"{DRAFT}: content changed outside authorized scope")
        table = r"^\| Change and environment \|[^\n]+\n(?:^\|[^\n]+\n)+"
        old = re.search(table, baseline, re.MULTILINE)
        new = re.search(table, text, re.MULTILINE)
        if not old or not new or old[0] != new[0]:
            raise ValueError(f"{DRAFT}: frozen derivation table changed")
    return len(expected) - len(pending), pending


def trace(key, claims, deps, blocks, paragraphs, apparatus, loci):
    def show(label, entries):
        print(f"{label}: {', '.join(entries) or '—'}")

    if key in claims:
        print(f"{key}: {claims[key][0] if claims[key] else 'see current model'}")
        labels = ("Required", "Either", "Other")
        for label, group in zip(labels, deps.get(key, ([], [], []))):
            show(label, group)
        for i, label in enumerate(labels):
            show(f"{label} by", [owner for owner, groups in deps.items() if key in groups[i]])
        if key in loci:
            show("Principal exposition", ids(loci[key][0]))
        show("Paragraphs", [p for p, cells in paragraphs.items() if key in ids(cells[2])])
        show("Apparatus", [a for a, cells in apparatus.items() if key in ids(cells[1])])
    elif key in blocks:
        show("Paragraphs", [p for p, cells in paragraphs.items() if key == cells[0]])
    elif key in paragraphs:
        block, function, refs, _, _ = paragraphs[key]
        print(f"{key} / {block}: {function}")
        show("Claims", ids(refs))
        show("Apparatus", [a for a, cells in apparatus.items() if key in ids(cells[0])])
    elif key in apparatus:
        anchors, refs, purpose = apparatus[key]
        print(f"{key}: {purpose}")
        show("Anchors", ids(anchors))
        show("Claims", ids(refs))
    else:
        raise ValueError(f"unknown trace ID: {key}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace", metavar="ID", help="show immediate forward and reverse links")
    parser.add_argument("--against", metavar="REV", help="verify protected source against REV")
    parser.add_argument("--scope", action="append", default=[], metavar="ID",
                        help="allow changes only to this block or unit (repeatable)")
    parser.add_argument("--complete", action="append", default=[], choices=IMPLEMENTED,
                        help="require an implemented block to have no pending units")
    args = parser.parse_args()
    try:
        model = load()
        claims, _, blocks, paragraphs, apparatus, _ = model
        baseline = None
        if args.against:
            baseline = subprocess.check_output(
                ["git", "show", f"{args.against}:./{DRAFT}"], cwd=ROOT, encoding="utf-8"
            )
        count, pending = check_article((ROOT / DRAFT).read_text(encoding="utf-8"),
                                       paragraphs, baseline, args.scope, args.complete)
        if args.trace:
            trace(args.trace, *model)
        else:
            print(f"Valid: {len(claims)} historical IDs, {len(blocks)} rhetorical blocks, "
                  f"{len(paragraphs)} paragraphs, {len(apparatus)} apparatus items, "
                  f"{count} implemented anchors.")
            if pending:
                print(f"Pending: {', '.join(pending)}.")
            if baseline is not None:
                print("Protected prose and the frozen derivation table are unchanged.")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Exposition: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
