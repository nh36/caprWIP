#!/usr/bin/env python3
"""Add DERIVATION_CLASS column to germanic-aligned-final.tsv (after HISTORY,
before STRUCTURE) and classify every Old_English row with a real COUNTERPART.

Allowed values (per project spec, 2026-04-30):
  regular | early_analogy | late_analogy | attested_variant
  | known_unmodelled | unexplained_unmodelled | lexeme_retarget
  | reconstructed_oe
"""
from __future__ import annotations

import csv
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TSV = REPO / "Germanic/data/germanic-aligned-final.tsv"
KNOWN = REPO / "Germanic/data/oe_known_problems.tsv"

ALLOWED = {
    "regular", "early_analogy", "late_analogy", "attested_variant",
    "known_unmodelled", "unexplained_unmodelled", "lexeme_retarget",
    "reconstructed_oe",
}

# ---------- normalisation ----------

def strip_acute(s: str) -> str:
    """Drop COMBINING ACUTE ACCENT (and leading *) so stress-marked PROTOFORM
    can be compared with un-stressed PROTO when they encode the same form.
    Also treat COMBINING DIAERESIS as equivalent to COMBINING MACRON, since
    PROTOFORM uses i+diaeresis (ḯ) for FST technical reasons whereas PROTO
    uses i+macron — they encode the same long-stressed *ī in this project."""
    s = s.lstrip("*").strip()
    decomp = unicodedata.normalize("NFD", s).replace("\u0308", "\u0304")
    no_acute = "".join(c for c in decomp if c != "\u0301")
    return unicodedata.normalize("NFC", no_acute)


# ---------- known problems ----------

def load_known(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    with path.open(encoding="utf-8") as fh:
        rdr = csv.DictReader(fh, delimiter="\t")
        for row in rdr:
            proto = row["proto"].strip()
            cat = row["category"].strip()
            if proto:
                out[proto] = cat
    return out


# ---------- classifier ----------

LATE_ANALOGY_MARKERS = (
    "gen.sg.", "gen. sg.", "gen sg", "genitive sg", "genitive singular",
    "dat.sg.", "dat. sg.", "dat sg", "dative sg", "dative singular",
    "acc.sg.", "acc. sg.", "acc sg", "accusative sg",
    "nom.sg.", "nom. sg.", "nom sg",
    "1sg", "2sg", "3sg",
    "1/3 sg", "1/3sg",
    "sg. pret.", "sg pret",
    "sg. pres.", "sg pres",
    "sg. imperative", "sg imperative", "imperative sg",
    "oblique", "paradigm cell",
    "gen.pl.", "gen. pl.", "gen pl",
    "dat.pl.", "dat. pl.", "dat pl",
    "acc.pl.", "acc. pl.", "acc pl",
    # compact CamelCase variants used in some NOTEs (lowercased to match note_l)
    "gensg", "datsg", "accsg", "nomsg", "instsg",
    "genpl", "datpl", "accpl", "nompl", "instpl",
)

LEXEME_RETARGET_MARKERS = (
    "wrong cognate", "wrong etymon",
    "switched from", "switched to", "etymon switched",
    "different etymon", "different lexeme",
    "lexeme retarget", "lexeme-retarget",
    "wrong lemma", "different lemma",
    "wrong source extraction", "source extraction was wrong",
    "wrong cognate assignment",
)

ATTESTED_VARIANT_MARKERS = (
    "dialectal", "dialect ", "anglian", "mercian", "northumbrian",
    "kentish", "west saxon variant", "wessex variant",
    "glossary", "early gloss", "epinal", "erfurt", "corpus glossary",
    "épinal-corpus", "epinal-corpus", "ép.corp", "ep.corp",
    "conservative form", "conservative variant",
    "alternate attestation", "alternate spelling", "variant spelling",
    "early form", "archaic form", "archaic variant",
    "earliest attested", "earliest oe form", "earliest-attested",
    "attested as", "attested variant",
    "early attestation",
    "late-ws reduction", "late-ws doublet",
)


def classify(row: dict[str, str], known: dict[str, str]) -> str:
    if row.get("DOCULECT", "") != "Old_English":
        return ""
    counterpart = row.get("COUNTERPART", "").strip()
    if counterpart in ("", "-", "?", "∅"):
        return ""

    proto_form = row.get("PROTOFORM", "").strip()
    proto = row.get("PROTO", "").strip()
    note = row.get("NOTE", "")
    note_l = note.lower()

    # 1. Authoritative seed: oe_known_problems.tsv
    if proto_form in known:
        cat = known[proto_form]
        if cat == "u_lowering_near_labial":
            return "unexplained_unmodelled"
        return "known_unmodelled"

    # 1b. Reconstructed (unattested) OE counterpart. Triggered by explicit
    #     NOTE markers — too risky to infer heuristically. Includes both
    #     genuinely unattested forms (cnobba, *rēac) and Anglian-only-attested
    #     forms whose WS reflex is reconstructed (strīeġan).
    reconstructed_markers = (
        "unattested old english cognate",
        "unattested west saxon cognate",
        "reconstructed west saxon",
        "reconstructed *",
        "retargeted 2026-04-30 from attested anglian",
    )
    if any(m in note_l for m in reconstructed_markers):
        return "reconstructed_oe"

    # 1c. High-precedence attested_variant shortcut: NOTE markers that
    #     unambiguously identify the COUNTERPART as a dialectal / glossary /
    #     conservative attested variant.  These are checked BEFORE the generic
    #     "retarget" routing so that "retargeted to <earliest-attested form>"
    #     doesn't fall through to late_analogy.  Markers chosen so they don't
    #     occur incidentally in genuine paradigm-cell rows.
    strong_attested_markers = (
        "earliest attested oe form",
        "earliest-attested",
        "epinal-corpus glossary",
        "ép.corp.", "ep.corp.",
        "late-ws reduction", "late-ws doublet",
        "early-ws m.nom",  # 2254 þrīe etc.
    )
    if any(m in note_l for m in strong_attested_markers):
        return "attested_variant"

    # 2. Explicit retargeting markers in NOTE.  Generic "retarget" alone is
    #    ambiguous: it may be a paradigm-cell retarget (late_analogy), a
    #    dialect/glossary/conservative-variant retarget (attested_variant),
    #    or a lexeme switch (lexeme_retarget).  Check the more specific
    #    discriminators first; "retarget" alone falls through to NOTE-marker
    #    classification in step 4.
    paradigm_cell_strong = (
        "paradigm-cell",                # NOTE often opens "Paradigm-cell …"
        "1/3 sg pret.", "1/3sg pret.",
        "1/3 sg. pret.",
        "obl.sg./pl. paradigm cell",
    )
    if any(m in note_l for m in paradigm_cell_strong):
        return "late_analogy"

    has_retarget = "retarget" in note_l

    # "transponent" used to force early-analogy regardless of PF=P; but
    # in practice the one transponent row in the corpus (sparian) needs
    # NOTE-marker fall-through, and other early_analogy rows are already
    # caught by PF≠P.  Keeping this as a no-op tag for clarity.

    # 3. Compare PROTOFORM and PROTO modulo stress accent (and diaeresis↔macron)
    pf_n = strip_acute(proto_form)
    p_n = strip_acute(proto)
    if pf_n == p_n and not has_retarget:
        return "regular"

    # 4. PF/P differ (or "retarget" forced us through) — read NOTE for a
    #    discriminator.  LATE first, then LEXEME, then ATTESTED, then default
    #    early_analogy.
    if any(m in note_l for m in LATE_ANALOGY_MARKERS):
        return "late_analogy"
    if any(m in note_l for m in LEXEME_RETARGET_MARKERS):
        return "lexeme_retarget"
    if any(m in note_l for m in ATTESTED_VARIANT_MARKERS):
        return "attested_variant"
    return "early_analogy"


# ---------- TSV rewrite ----------

def main() -> int:
    known = load_known(KNOWN)

    with TSV.open(encoding="utf-8", newline="") as fh:
        rdr = csv.reader(fh, delimiter="\t")
        rows = list(rdr)

    header = rows[0]
    if "DERIVATION_CLASS" in header:
        sys.exit("DERIVATION_CLASS already present; aborting.")

    # Insert AFTER HISTORY, BEFORE STRUCTURE
    hist_idx = header.index("HISTORY")
    struct_idx = header.index("STRUCTURE")
    if struct_idx != hist_idx + 1:
        sys.exit(f"Unexpected header order: HISTORY={hist_idx} STRUCTURE={struct_idx}")

    insert_at = struct_idx  # 0-indexed
    new_header = header[:insert_at] + ["DERIVATION_CLASS"] + header[insert_at:]

    out_rows = [new_header]
    counts: dict[str, int] = {}
    for r in rows[1:]:
        # pad short rows defensively
        while len(r) < len(header):
            r.append("")
        rec = dict(zip(header, r))
        cls = classify(rec, known)
        if cls:
            counts[cls] = counts.get(cls, 0) + 1
        new_r = r[:insert_at] + [cls] + r[insert_at:]
        out_rows.append(new_r)

    with TSV.open("w", encoding="utf-8", newline="") as fh:
        for r in out_rows:
            fh.write("\t".join(r) + "\n")

    print("DERIVATION_CLASS counts (Old_English rows with real COUNTERPART):")
    total = sum(counts.values())
    for k in sorted(counts, key=lambda x: -counts[x]):
        print(f"  {counts[k]:>4}  {k}")
    print(f"  {total:>4}  total classified")

    # Sanity
    bad = [k for k in counts if k not in ALLOWED]
    if bad:
        print(f"!! Unknown classes assigned: {bad}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
