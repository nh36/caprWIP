---
row_id: 2012
concept: finger
counterpart: finger
proto: *fíngraz
protoform: *fíngraz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2012 finger / finger

## Current row state

- The live TSV row is straightforward: `CONCEPT = finger`, `COUNTERPART = finger`, `PROTO = *fíngraz`, `PROTOFORM = *fíngraz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:318-318].
- `PROTO` and `PROTOFORM` are identical here, but they should still be read as different slots: the comparative Germanic headword and the row-specific OE derivational input simply happen to coincide for this row [Germanic/data/germanic-aligned-final.tsv:318-318].
- The row is being treated as attested OE, not as a reconstructed target. The upstream OE-form table has `finger` as the OE form for English `finger`, though the source lineage is still only the thin Wiktionary-derived `der / template:der` record rather than a dedicated row memo [Germanic/data/old_english_wiktionary.tsv:77-77].
- The live TSV's documentary fields are correspondingly light: the note field is empty, and the history/source text is only the duplicated placeholder `Source: Wiktionary etymology (template:der) | Source: Wiktionary etymology (template:der)` [Germanic/data/germanic-aligned-final.tsv:318-318].
- No manifest-backed packet or research memo exists for this row. `report_manifest.tsv` contains no entry for row 2012, and the coverage audit still lists row 2012 `finger / finger` among the regular rows with no note and no report required [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/docs/lexeme_reports/coverage_audit.md:237-237].
- The current published derivation snapshot already agrees with the live row: `PROTO: *fíngraz`, `EXPECTED: finger`, `OUTPUTS: finger`, with the compact path `PGmc Final Z Deletion: *fíngra`, `PWGmc Final Bare A Loss: *fíngr`, `OE Epenthetic Vowel: *fínger`, then surface `finger` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1280-1299].
- `oe_known_problems.tsv` has no entry for `*fíngraz`, which fits the row's present `regular` status and the successful published trace [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

No row-specific `finger` dossier survives in `DEV_NOTES.md`. The row can still be documented conservatively, but the support is mostly shared-rule material rather than a bespoke `finger` note. In practice, two DEV_NOTES hits matter: the shared `OEEpentheticInsertion` note, which explicitly gives the derivation `*fingrăz → finger`, and a later handbook-summary quotation in the palatalisation dossier, which preserves Campbell's use of `finger` as a type-example for medial palatal `g` after a front vowel and before a syllabic sonorant [Germanic/docs/DEV_NOTES.md:16671-16711,43224-43243].

The main explanatory burden belongs to the epenthesis note. DEV_NOTES does not treat `finger` as an exception, analogy, or repair target. Instead it says the form belongs to a normal OE parasitic-vowel pathway: `PGmc *fingrăz → OE finger (via *fingr → *fingEr → *finger)` [Germanic/docs/DEV_NOTES.md:16672-16672]. The same note insists this is a “**real phonological rule**” for “parasitic vowel insertion” / “anaptyxis” / “svarabhakti vowel,” not a patch, and it gives the exact frontness conditioning needed here: “After front vowels: `*E → *e` (e.g., `finger`, `timber`)” [Germanic/docs/DEV_NOTES.md:16679-16691]. That shared note matches the published debug trace closely enough that it can serve as the slice's primary replacement note [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1287-1299].

The palatalisation material is weaker and should be used carefully. It does preserve an important handbook quotation: Campbell's summary says medial `g` palatalises “between any two front vowels, between front vowel and syllabic consonant, and always after a vowel which has suffered i-umlaut,” and the copied type-examples include `finger` [Germanic/docs/DEV_NOTES.md:43232-43236]. But DEV_NOTES itself presents this inside a broader retraction-and-consensus discussion for `g`-conditioning, not as a row-2012 intervention. So for this slice it is best treated as background corroboration that `finger` is a familiar handbook example, not as grounds for changing the row class, target form, or current debug path [Germanic/docs/DEV_NOTES.md:43218-43243].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16671-16711

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Source line or section hint: `lines 16671-16711`
- Fragment type: `shared_phonology_fragment_with_explicit_lexeme_example`
- Status: `current`
- Issue tags: `epenthesis`; `final_cr_cluster`; `front_vowel_conditioning`; `regular_row_support`
- Recommended next use: `best_available_row_anchor`
- Shared with row IDs: `2053`, `2230`, `2258`, `2295`, and other OE parasitic-vowel rows

This is the primary surviving DEV_NOTES support for row 2012 because it explicitly names the lexeme and gives an actual derivational chain: `PGmc *fingrăz → OE finger (via *fingr → *fingEr → *finger)` [Germanic/docs/DEV_NOTES.md:16672-16672]. The spelling there is not letter-for-letter identical to the TSV's accented `*fíngraz`, but it is plainly the same lexical item and the same phonological pathway. Nothing in the fragment suggests a special row-local rescue; the point is the opposite, namely that `finger` is one of the standard examples showing why final-cluster epenthesis must exist in the OE pipeline.

The surrounding prose is worth preserving verbatim in substance because it explains why the row stays `regular`. DEV_NOTES says this is a “**real phonological rule**” representing “parasitic vowel insertion” / “anaptyxis” / “svarabhakti vowel,” then states the frontness condition: “After front vowels: `*E → *e` (e.g., `finger`, `timber`)” [Germanic/docs/DEV_NOTES.md:16679-16691]. For row 2012 that means the project's present claim is modest but clear: once final `-z` and final bare `-a` are gone, `*fíngr` develops to `*fínger` by an ordinary shared OE process, exactly as the published debug snapshot now reports [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1291-1299].

### DEV_NOTES:line-43224-43243

- Source heading: `§17.50.4.1 The handbook consensus`
- Source line or section hint: `lines 43224-43243`
- Fragment type: `shared_handbook_quote_with_background_relevance`
- Status: `current_but_secondary`
- Issue tags: `campbell_quote`; `g_palatalisation`; `handbook_example`; `background_only`
- Recommended next use: `cite_only_if_medial_g_conditioning_is_raised`
- Shared with row IDs: `1943`, `1996`, `2049`, and many other front-vowel medial-`g` rows

This fragment is secondary, but it is still worth retaining because DEV_NOTES preserves a real handbook quotation that names `finger`. In the copied Campbell summary, medial `g` palatalises “between any two front vowels, between front vowel and syllabic consonant, and always after a vowel which has suffered i-umlaut,” and the type-examples for palatal include `finger` alongside `æcer, cwice, brece, dæges, sige, nægl, fægr, wegn, regn, segl, finces, þinges` [Germanic/docs/DEV_NOTES.md:43232-43236]. That makes `finger` more than an accidental spreadsheet item: it is a standard example in the handbook tradition as quoted here.

Even so, this is not the main row note. The passage appears inside a later consensus summary that “retracts the over-narrow rule fix proposed in §17.50.3” [Germanic/docs/DEV_NOTES.md:43220-43222], so its job is to delimit palatalisation conditioning across many rows, not to reclassify row 2012. For this slice the safe use is conservative: keep it as background corroboration that `finger` belongs to familiar OE phonological discussions, but do not overstate it as if DEV_NOTES had preserved a dedicated `finger` controversy or a row-specific implementation defect [Germanic/docs/DEV_NOTES.md:43218-43243].

## Superseded or diagnostic material

- No row-specific `finger` memo, packet, or DEV_NOTES mini-dossier was found. That absence is real, not editorial oversight inside this slice: the row currently stands on shared phonology plus the stable debug trace, not on a bespoke lexeme report [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/docs/lexeme_reports/coverage_audit.md:237-237; Germanic/docs/DEV_NOTES.md:16671-16711,43224-43243].
- The published derivation trace is valuable current-state evidence, but it is still diagnostic implementation output rather than an independent historical argument. It confirms that the present pipeline already derives `finger`; it does not replace the DEV_NOTES explanation of why epenthesis is allowed [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1280-1299].
- The Campbell palatalisation quotation preserved at `DEV_NOTES:line-43224-43243` should remain secondary. It shows that `finger` is a recognized handbook example, but by itself it does not require any change to the row's `regular` classification, `PROTOFORM`, or surface target [Germanic/docs/DEV_NOTES.md:43224-43243].
- The duplicated `template:der` source string in the TSV and the matching thin `old_english_wiktionary.tsv` entry are source-lineage artifacts, not substitutes for a row-level philological note [Germanic/data/germanic-aligned-final.tsv:318-318; Germanic/data/old_english_wiktionary.tsv:77-77].

## Open questions for later work

- If a later full lexeme report is written, add direct literature citations for the PGmc and OE lexeme pair rather than relying on the thin Wiktionary-derived lineage now visible in the TSV and OE-form table [Germanic/data/germanic-aligned-final.tsv:318-318; Germanic/data/old_english_wiktionary.tsv:77-77].
- If later reporting needs to discuss medial `g` more explicitly, decide whether the Campbell `finger` quotation should be tied to a modeled phonological step, or whether it should remain only background evidence while the row continues to rely operationally on the simpler published trace [Germanic/docs/DEV_NOTES.md:43224-43243; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1291-1299].
- If this row is ever indexed from DEV_NOTES material alone, the safest primary anchor is still the epenthesis note at `DEV_NOTES:line-16671-16711`; the palatalisation quotation is useful, but it is not equally row-specific.
