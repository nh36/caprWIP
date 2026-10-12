---
row_id: 2236
concept: swell
counterpart: swellan
proto: *swéllaną
protoform: *swéllaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2236 swell / swellan

## Current row state

- Live OE row `2236` currently reads `CONCEPT = swell`, `COUNTERPART = swellan`, `PROTO = *swéllaną`, `PROTOFORM = *swéllaną`, `DERIVATION_CLASS = regular`; the row carries duplicated Wiktionary inheritance sourcing and no live exception note [Germanic/data/germanic-aligned-final.tsv:1186-1186].
- The row therefore does **not** currently split comparative `PROTO` from OE-facing `PROTOFORM`. Both project fields use the same input `*swéllaną`, while the OE target selected for the row is the infinitive `swellan` [Germanic/data/germanic-aligned-final.tsv:1186-1186].
- `oe_known_problems.tsv` has no entry for row `2236`, `swellan`, or `*swéllaną`, so the lexeme is not being tracked as a live OE mismatch or documented exception there [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists `2236 | swell | swellan | regular | no | - | - | - | none`, so there is no existing packet, research memo, dossier, or full report stem to reuse; the canonical row-based filename is therefore appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:383-383].
- The current published OE derivation trace is an exact match: `PROTO: *swéllaną`, `EXPECTED: swellan`, `OUTPUTS: swellan`, with only OE tail-side steps `OE Heavy Syllable Nasal Apocope: *swéllan`, `OE Secondary Nasalization: *swélląn`, and `OE Weak Tail Reduction: *swéllan` before surface `Outcome: swellan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5008-5027].
- Comparative and lexical source support aligns cleanly with the live target while using different notation layers. Kroonen gives `*swellan- s.v. ‘to swell’ ... OE swellan sv. ‘id.’`; Clark Hall lists `swellan³ to "swell."'`; Bosworth-Toller adds the preterite `sweoll` under `swellan` [@Kroonen2013, p. 499; @ClarkHall1960, s.v. "swellan"; @BosworthToller1898, s.v. "swellan"].

## Detailed development-note summary

No securely attachable **current row-specific DEV_NOTES authority** exists for row 2236. The required review located no row-local discussion of row `2236`, `*swéllaną`, or `swellan` in `Germanic/docs/DEV_NOTES.md`. For replacement-note purposes, that means the operative evidence bundle is the live TSV row, the coverage audit, the exact-match derivation trace, and the checked lexical references rather than any hidden DEV_NOTES chronology.

That absence of DEV_NOTES material does **not** make the row unstable. The live project treatment is straightforward and should be stated explicitly: `PROTO = *swéllaną`, `PROTOFORM = *swéllaną`, `COUNTERPART = swellan`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1186-1186]. The current published trace then shows the grammar already landing exactly on `swellan` with no rescue rule, exception note, or analogical patch layer required [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5008-5027].

The notation layers still need to stay distinct even in a no-hit slice. Kroonen's `*swellan-` is a comparative headword citation for the Germanic verb family, not the literal row header stored in the live TSV [@Kroonen2013, p. 499]. The project's row-level `PROTOFORM` is the acute-marked FST input `*swéllaną`, while the OE-side target is the citation-form infinitive `swellan` [Germanic/data/germanic-aligned-final.tsv:1186-1186]. Because there is no contrary DEV_NOTES material, later work should **not** invent a `PROTO`/`PROTOFORM` split here and should **not** replace the counterpart with a non-citation-form paradigm cell.

The lexical references are useful mainly because they confirm that the row is pointed at the right OE verb and not at some neighboring family member. Kroonen's entry directly includes OE `swellan` among the Germanic cognates [@Kroonen2013, p. 499]. Clark Hall's short lemma confirms the citation form `swellan` [@ClarkHall1960, s.v. "swellan"]. Bosworth-Toller preserves the strong-verb paradigm background with `p. sweoll`, which is worth remembering for any later full report, but that paradigm information does not alter the row target: the row still aims at the infinitive `swellan`, not at a past-tense form or deverbal noun [@BosworthToller1898, s.v. "swellan"].

The safest replacement-note conclusion is therefore narrow and conservative. Row 2236 is presently a solved regular row with exact-match derivation and ordinary lexical support, but it has **no surviving row-attached DEV_NOTES fragment** to index or quote. The slice should preserve that absence plainly so later report writers do not waste time hunting for a missing DEV_NOTES argument that is not there.

## Relevant DEV_NOTES fragments with line-based refs

No securely attachable **current** row-specific DEV_NOTES fragment survives. The required review found no row-local DEV_NOTES discussion of row `2236`, `*swéllaną`, or `swellan`, so there is no usable `DEV_NOTES:line-...` attachment for this lexeme at present.

Because there is no row-attached DEV_NOTES fragment, later work should not infer hidden DEV_NOTES authority from the row's exact-match trace or from the general dictionary support. For row 2236, the live TSV row, the exact-match debug trace, and the lexical source audit are the operative evidence bundle [Germanic/data/germanic-aligned-final.tsv:1186-1186; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5008-5027; @Kroonen2013, p. 499].

## Superseded or diagnostic material

- No superseded row-local DEV_NOTES proposal currently survives for this lexeme. The main documentary fact is absence rather than reversal.
- Kroonen's comparative headword `*swellan-` is diagnostic for source hierarchy, not a reason to overwrite the live row header. It supports the cognate set, but the live project `PROTO` and `PROTOFORM` remain `*swéllaną` [Germanic/data/germanic-aligned-final.tsv:1186-1186; @Kroonen2013, p. 499].
- Bosworth-Toller's `p. sweoll` is useful future paradigm background, but it should remain diagnostic/background material unless a later full report explicitly expands into inflectional discussion. It is not a rival `COUNTERPART` and not evidence against the row's infinitive target `swellan` [@BosworthToller1898, s.v. "swellan"].

## Open questions for later work

- If this row ever gets a packet or research memo, the first task should be lexeme-specific source gathering rather than `index.tsv` attachment, because there is still no row-local DEV_NOTES fragment to index.
- If `index.tsv` is revisited later, recommended additions are still **none** unless a real `DEV_NOTES:line-...` fragment for `swellan` is identified or the project decides to index rows that are supported only by absence-of-hit slices.
- If a fuller lexeme report is ever written, it may be worth documenting the strong-verb paradigm background (`sweoll`, past participial material) from Bosworth-Toller, but that should be done without disturbing the present row policy `PROTO *swéllaną` / `PROTOFORM *swéllaną` / `COUNTERPART swellan` [Germanic/data/germanic-aligned-final.tsv:1186-1186; @BosworthToller1898, s.v. "swellan"].
