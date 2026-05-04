# Research memo — 2312 bore (3sg) / boraþ

## Starting point

- **ID:** 2312
- **CONCEPT:** bore (3sg)
- **COUNTERPART:** `boraþ`
- **PROTO:** `*burōną`
- **PROTOFORM:** `*búrōθi`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** `Class II weak 3sg pres. indic. Regular: *-ōθi → -aþ (Campbell §355.4). No i-umlaut: 3sg ending never had -j-. Forms with -eþ are dialectal.`

The live row already encodes the key distinction that the memo must preserve: `*burōną` is the lexeme-level cognate-set source, `*búrōθi` is the project-selected paradigm-cell input, and `boraþ` is the OE target for that specific 3sg present indicative cell.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet’s compact derivation trace showing `*búrōθi -> boraþ`; and the packet’s row-specific DEV_NOTES excerpts at `DEV_NOTES.md:19572`, `19599`, `19710`, and `19953`, all of which align with the current row and current debug snapshot.
- **Useful background:** the packet preserves older project chronology showing why this row entered debugging at all: earlier work first treated the class-II weak 3sg as an `-eþ` problem and then corrected that analysis to regular `-aþ`.
- **Stale or superseded:** the packet’s carry-over from older DEV_NOTES sections that treat regular weak-II 3sg as `boreþ` or frame `-eþ` as the expected phonological outcome. Those sections are superseded by the later correction sequence in `DEV_NOTES.md §15.1–15.4`, where row 2312 is explicitly corrected to `boraþ`.
- **Irrelevant or misleading:** the packet’s large analysis/dossier section is mostly keyword noise from generic `i-umlaut` searches. I audited every named analysis/dossier file from the packet; none contains row-specific evidence for `boraþ` or `*búrōθi`, and several are wholly unrelated to weak class II verbs.

## Additional repo research

Checked beyond the packet:

- `Germanic/data/germanic-aligned-final.tsv` for rows 1956 (`bore / borian`), 2311, and 2312
- `Germanic/data/old_english_wiktionary.tsv` for the lemma evidence `bore -> borian`
- `Germanic/docs/DEV_NOTES.md` at the class-II weak-verb discussions around `2759–2819`, `19377–19494`, `19497–19619`, `19623–19739`, and `20196–20213`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:8143–8165`
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run against the live FST
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry)
- `Germanic/docs/non_firing_rules_analysis.md:443` as older background on the analogical infinitive family, not on row 2312 itself
- every analysis/dossier file named in the packet’s analysis section: `analysis/arestoration_r_l_research.md`, `analysis/compound_archaism_inventory.md`, `analysis/cow_root_noun_investigation.md`, `analysis/four_complex_tsv_items.md`, `analysis/fryhtu_investigation.md`, `analysis/notable_findings.md`, `analysis/ws_vs_anglian_dialect_differences.md`, `analysis/mismatch_dossier_mizdo.md`, `analysis/mismatch_dossier_mizdo_supplement.md`, `dossiers/bugan-scufan-paradigm-cell-review.md`, `dossiers/g-palatalisation-conditioning.md`, and `dossiers/widuwe-u-preservation.md`

Outcome of that broader audit:

- **Materially relevant current evidence:** the live TSV row, the debug trace for row 2312, the bore-family lemma row 1956, `old_english_wiktionary.tsv`, and the later DEV_NOTES correction sequence establishing weak-II 3sg `-aþ`.
- **Useful methodological background only:** `compound_archaism_inventory.md`, `bugan-scufan-paradigm-cell-review.md`, and `widuwe-u-preservation.md`, because they explain the project’s paradigm-cell methodology.
- **Irrelevant or keyword-noise for this lexeme:** the remaining named analysis/dossier files, which do not discuss `boraþ`, `*búrōθi`, or the bore-family specifically.

I found no existing pilot lexeme report for row 2312. The related memo for row 2311 is useful background, but it is not authority for row 2312.

## Reconstruction and early-stage forms

Three levels must remain separate:

1. **Cognate-set proto / lexeme level:** `*burōną`, the class-II weak verb behind the OE bore-family workaround rows.
2. **Project input form for this row:** `*búrōθi`, the non-`j` 3sg present indicative cell chosen because it keeps the inherited class-II suffix without the analogical `-ōja-` infinitive remodeling.
3. **OE target form:** `boraþ`, the expected OE reflex of that selected 3sg cell.

The repo’s current derivation is straightforward: early loss of final `-i` in the weak-II 3sg leaves a form of the shape `*borōθ`, and late unstressed shortening gives `-a-`, not `-e-`, hence `boraþ`. This is exactly the distinction the current row note and later DEV_NOTES sections defend.

By contrast, the citation-form pathway `*búrōjaną -> borian` belongs to the analogically remodeled infinitive row 1956. It is relevant background for the lexeme family, but it is not the same historical object as row 2312.

## Old English philology

Repo-local philology supports the following distinctions:

- **Citation lemma / dictionary headword:** `borian`, supported by row 1956 and `old_english_wiktionary.tsv`.
- **Row 2312 target:** `boraþ`, an inflected 3sg present indicative form, not the lemma.
- **Attestation status in repo evidence:** the repo supports `borian` as a lemma and supports `boraþ` as the project’s regular weak-II 3sg target, but I did not find a separate dossier or lexical-table witness in the repo that independently documents manuscript attestation of `boraþ` itself.
- **Dialect status:** the only supported dialect claim here is negative/limited: `-eþ` forms are treated in current project evidence as dialectal or secondary variants, while standard weak-II 3sg is `-aþ`.

So the safe philological formulation is that `boraþ` is the project-selected OE 3sg cell with a regular sound-law pathway, contrasted with the analogical citation lemma `borian`; it should not be oversold on current repo evidence as a specifically sourced manuscript headform.

## Project problem and solution

The project problem is the same one seen elsewhere in late-analogy class-II verbs: the inherited lexeme is represented in OE by a citation form in `-ian`, but that infinitive is morphologically remodeled and therefore not the cleanest neogrammarian target for FST testing.

The solution for the bore-family is to keep the lexeme-level etymology `*burōną` while selecting non-`j` paradigm cells as separate OE rows. For row 2312, that means the project is intentionally modelling the regular 3sg present indicative `*búrōθi -> boraþ`, not trying to derive the citation lemma. The `late_analogy` label is therefore still appropriate at the lexeme-family level even though this specific cell is the regular workaround.

## Paradigm probe

A paradigm probe **is required**. There is still **no built-in probe spec** for row 2312 in `Germanic/tools/oe_paradigm_probe.py`, so the required project probe is missing even though a manual probe can already be run.

Manual live-FST probe results are consistent with the current analysis:

- `*búrōθi -> boraþ`
- `*búrô -> bora`
- `*búrōjaną -> borian`
- `*búrōną -> boren`
- `*búrōsi -> +?` (no current output)

The missing formal probe should at minimum cover these cells/comparators:

- **3sg pres. indic.** `*búrōθi` (live row 2312)
- **2sg pres. indic.** `*búrōsi` (to test the paired regular `-as` cell)
- **iptv.2sg.** `*búrô` (paired row 2311)
- **citation-form infinitive comparator** `*búrōjaną` (`borian`, row 1956)
- **non-`j` infinitive comparator** `*búrōną` if the project wants to keep testing the inherited class-II morphology directly

## Recommended final report

Recommend a final report that states briefly that `boraþ` is a project-selected weak-II 3sg paradigm cell, not the citation lemma; that `*burōną`, `*búrōθi`, and `boraþ` must be kept distinct; that current project evidence supports regular `-aþ < -ōþi` with no `j`-triggered umlaut; and that older `boreþ` history is diagnostic background only.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no substantive correction required. A minor wording cleanup would help: the note could say more explicitly that this is a project-selected non-`j` paradigm cell contrasted with analogical `borian`, but the current note is already philologically sound.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** `DEV_NOTES` cleanup is recommended. Older sections that still present `boreþ` / regular weak-II `-eþ` as the expected outcome should be marked more explicitly as superseded by the later corrections at `§15.1–15.4`. No dossier text change is needed for row 2312, because the packet’s named dossier/analysis files are not row-specific evidence and do not need row-level textual revision.
