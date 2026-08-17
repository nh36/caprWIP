#!/usr/bin/env python3
"""Machine-readable corpus-coverage census for the historical sound changes.

For every canonical historical sound-change rule (an inventory row whose
foma identifier is composed in the executable cascade manifest) the census
records:

  * corpus_firing_count — how many selected corpus derivations the rule
    changes, read from the STAGE FIRING SUMMARY of the committed full trace
    report (docs/debug_snapshots/oe_full_trace_report.txt);
  * lexical_witnesses — the corpus lexemes it fires on;
  * coverage_status — one of:
        witnessed                   fires on at least one selected corpus row
        synthetic_only              historically genuine; zero corpus firings;
                                    validated by synthetic unit controls only
        historically_obscured       genuine but its corpus effect is masked by
                                    later developments (explicit override)
        disputed_or_research_issue  witnessing evidence is itself under
                                    adjudication (explicit override)

The project invariant is NOT "every rule fires": it is that every historical
rule's corpus-coverage status is explicit and understood (corpus-maturation
pass 01). Regenerate with:

    python3 Germanic/tools/rule_coverage_census.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FULL_TRACE = GERMANIC / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"
INVENTORY = GERMANIC / "docs" / "sound_changes" / "sound_change_inventory.tsv"
MANIFEST = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
            / "cascade_order_manifest.tsv")
OUTPUT = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
          / "rule_coverage_census.tsv")

# The tracer's STAGES list names two stages differently from the manifest's
# foma identifiers (historic labels; renaming deferred by author decision).
STAGE_ALIASES: dict[str, str] = {
    "EAFRhotacism": "Rhotacism",
    "OEPrefixAReduction": "OEPrefixAReductionEarly",
}

# Zero-firing statuses that require adjudication rather than the
# synthetic_only default. Every entry must cite its adjudication.
STATUS_OVERRIDES: dict[str, tuple[str, str]] = {
    "SC021": (
        "disputed_or_research_issue",
        "Candidate witness galgu (Ruthwell Cross) examined and declined: "
        "R&T 2014 pp.62-63, 164 (Bammesberger 1990: 169 analogical "
        "alternative); corpus-maturation-01 adjudication §4.",
    ),
}


def load_firing_summary(text: str) -> dict[str, tuple[int, list[str]]]:
    marker = "=== STAGE FIRING SUMMARY ==="
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("full trace report has no STAGE FIRING SUMMARY; "
                         "regenerate with tools/oe_full_trace_report.py --all")
    summary: dict[str, tuple[int, list[str]]] = {}
    current: str | None = None
    for line in text[idx + len(marker):].splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*): (\d+)$", line)
        if m:
            current = m.group(1)
            summary[current] = (int(m.group(2)), [])
            continue
        if current and " :: " in line:
            count, lexemes = summary[current]
            for chunk in line.split(", "):
                lex, _, _form = chunk.partition(" :: ")
                lexemes.append(lex.strip())
            summary[current] = (count, lexemes)
    return summary


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def build_rows() -> list[dict[str, str]]:
    firing = load_firing_summary(FULL_TRACE.read_text(encoding="utf-8"))
    manifest_pos = {r["foma_identifier"]: int(r["position"])
                    for r in read_tsv(MANIFEST)}
    rows = []
    for inv in read_tsv(INVENTORY):
        if inv.get("entry_type") != "historical_sound_change":
            continue
        sc = inv["change_id"]
        foma = ""
        m = re.search(r"define\s+([A-Za-z][A-Za-z0-9_]*)",
                      inv.get("rule_source_anchor", ""))
        if m:
            foma = m.group(1)
        if foma not in manifest_pos:
            continue  # not composed in the executable cascade
        count, lexemes = firing.get(STAGE_ALIASES.get(foma, foma), (0, []))
        if count > 0:
            status, note = "witnessed", ""
        else:
            status, note = STATUS_OVERRIDES.get(
                sc, ("synthetic_only",
                     "Zero corpus firings; validated by synthetic unit "
                     "controls and the handbook sources."))
        rows.append({
            "sc_id": sc,
            "foma_identifier": foma,
            "cascade_position": str(manifest_pos[foma]),
            "corpus_firing_count": str(count),
            "lexical_witnesses": ", ".join(dict.fromkeys(lexemes)),
            "coverage_status": status,
            "note": note,
        })
    rows.sort(key=lambda r: int(r["cascade_position"]))
    return rows


HEADER = ["sc_id", "foma_identifier", "cascade_position",
          "corpus_firing_count", "lexical_witnesses", "coverage_status",
          "note"]

PREAMBLE = """\
# rule_coverage_census.tsv
# Machine-readable corpus-coverage census for the historical sound changes.
# Generated by Germanic/tools/rule_coverage_census.py from the committed full
# trace report; regenerate after any corpus or cascade change.
# Invariant: every historical rule's coverage status is explicit and
# understood. "Every rule must fire" is deliberately NOT an invariant.
"""


def main() -> None:
    rows = build_rows()
    with OUTPUT.open("w", encoding="utf-8") as f:
        f.write(PREAMBLE)
        f.write("\t".join(HEADER) + "\n")
        for r in rows:
            f.write("\t".join(r[h] for h in HEADER) + "\n")
    print(f"wrote {OUTPUT} ({len(rows)} rules)")


if __name__ == "__main__":
    main()
