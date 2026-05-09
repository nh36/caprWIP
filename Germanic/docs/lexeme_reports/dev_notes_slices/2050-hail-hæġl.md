---
row_id: 2050
concept: hail
counterpart: hæġl
proto: *xáglą
protoform: *xáglą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2050 hail / hæġl

## Current row state

- Live TSV state: row 2050 currently keeps `CONCEPT = hail`, `COUNTERPART = hæġl`, `PROTO = *xáglą`, `PROTOFORM = *xáglą`, and `DERIVATION_CLASS = regular`, with no row-local explanatory NOTE beyond inherited-source boilerplate [Germanic/data/germanic-aligned-final.tsv:466-466].
- Audit/infrastructure state: `coverage_audit.md` still classifies row 2050 as a regular row with no NOTE and no report required, and `report_manifest.tsv` has no manifest entry for this row; there is likewise no `oe_known_problems.tsv` entry marking `*xáglą > hæġl` as an exception bucket, wontfix, or unresolved mismatch [Germanic/docs/lexeme_reports/coverage_audit.md:262-262; Germanic/data/oe_known_problems.tsv:1-8].
- Current derivation snapshot: the published OE trace already lands on the live target without repair. It gives `PROTO: *xáglą`, `EXPECTED: hæġl`, `OUTPUTS: hæġl`, then spells the path as Anglo-Frisian Brightening `*xæglą`, OE Velar Fricative Palatalization `*çæglą`, OE Heavy Syllable Nasal Apocope `*çægl`, OE Velar Palatalization `*çæʤl`, orthographic `h*æġl`, outcome `hæġl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1927-1947].
- Lexical-attestation baseline inside the repo preserves both the short coda form and the tail-bearing doublets. `old_english_wiktionary.tsv` gives `hail | hæġl`; Bright has `hægel (hægl, hagol), m., hail`; Clark Hall lists `hagol ... m. ‘hail,'` and `hagolfaru (hægl-)`; Kroonen's lexicographic headword is stem-notational `*hagla- m.? 'hail'` with OE `hagol, haegel` [Germanic/data/old_english_wiktionary.tsv:114-114; docs/references/bright_anglo_saxon_reader.vision.txt:21352-21355; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20256-20258; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:11415-11418].
- The notation layers therefore need to stay separate. The live row's `PROTO`/`PROTOFORM` are the project's singular-form FST input `*xáglą`, not Kroonen's stem-class dictionary notation `*hagla-`; the OE-facing target is the normalized coda form `hæġl`, while `hagol`/`hægel` remain real attested comparators relevant to the row's paradigm history rather than reasons to rewrite the current target [Germanic/data/germanic-aligned-final.tsv:466-466; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:11415-11418; docs/references/bright_anglo_saxon_reader.vision.txt:21352-21355].

## Development-note summary

Current DEV_NOTES support for row 2050 **does survive**, and it is more row-specific than the thin TSV row might suggest. The surviving row-local block is narrow but explicit: row 2050 is treated as a **word-final nominative singular `*Cl#` form with no back-vowel trigger**, so Anglo-Frisian fronting remains visible and A-restoration must **not** fire. DEV_NOTES first lists the row in the `*-aCl-* / *-aCr-*` audit as ``2050 | *xáglą | hæġl | *Cl* word-final NomSg, no back-vowel trigger; *æ* expected (cf. Campbell §158: *hægl ~ hagol* doublet — TSV chose the *NomSg* unbroken/*æ*-form)`` and then states the row rule again in prose: “NomSg has zero ending (post-apocope), so there is no back-vowel trigger in the surface form. AFB fronts `*a → *æ`; A-restoration cannot fire (no trigger). Output: `*hæġl`. ✓ This is the desired behaviour.” [Germanic/docs/DEV_NOTES.md:30621-30621; Germanic/docs/DEV_NOTES.md:30668-30676].

That surviving row-local policy needs to be read together with the shared Campbell material embedded in DEV_NOTES. Campbell's quoted wording is not saying that `hæġl` is wrong; it is explaining why `hagol` also exists. DEV_NOTES preserves the crucial lines: “Before other groups, `a` is not restored except for a few instances before consonant plus liquid ... Yet it need not be doubted that `a` was originally widely restored before groups, and that it was subsequently removed by the analogy of forms in which a front vowel followed. This is reflected by some doublets, e.g. `gæfel, gafol` tribute, `hægel, hagol` hail ... due to an original distinction s. `hægl`, p. `haglas` ...” [Germanic/docs/DEV_NOTES.md:30403-30413]. DEV_NOTES then turns that quotation into a row-specific conclusion: `hægl / hagol` is paradigm/doublet background, but the live row is the nominative-singular coda form, so the project conservatively keeps the fronted `hæġl` target rather than replacing it with a tail-bearing restoration form [Germanic/docs/DEV_NOTES.md:30530-30544; Germanic/docs/DEV_NOTES.md:30621-30621].

So the support tiers are distinct. The row-local `*hagla- / *xáglą → hæġl` block is **row-specific current policy**. Campbell's doublet quotation is **shared-background-only current support** explaining why attested `hagol/hægel` remain relevant. The derivation snapshot is **current diagnostic confirmation** that the cascade now outputs `hæġl` exactly as the DEV_NOTES policy predicts [Germanic/docs/DEV_NOTES.md:30668-30676; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1927-1947]. There is no evidence here for changing `PROTOFORM`, no need for a surrogate paradigm cell, and no reason to reclassify the row as an exception from the current material alone [Germanic/data/germanic-aligned-final.tsv:466-466; Germanic/data/oe_known_problems.tsv:1-8].

## Relevant DEV_NOTES fragments

### DEV_NOTES: current row policy on `*xáglą → hæġl`

- Source heading: `§17.19.4 Other potentially affected words` and sub-block `*hagla- / *xáglą → hæġl`
- Source line hint: `30621`, `30668-30676`
- Fragment type: `row_specific`
- Status: `current`
- Issue tags: `a_restoration`; `nom_sg`; `no_back_vowel_trigger`; `proto_equals_protoform`
- Recommended next use: `main_row_authority`
- Shared-with rows if relevant: `2130`, `2164`

This is the strongest surviving row-local authority and should be treated as the controlling note for row 2050. DEV_NOTES names the row directly in the inventory table as ``*xáglą | hæġl | *Cl* word-final NomSg, no back-vowel trigger; *æ* expected (cf. Campbell §158: *hægl ~ hagol* doublet — TSV chose the *NomSg* unbroken/*æ*-form)`` [Germanic/docs/DEV_NOTES.md:30621-30621]. The prose block below removes any ambiguity: “NomSg has zero ending (post-apocope), so there is no back-vowel trigger in the surface form. AFB fronts `*a → *æ`; A-restoration cannot fire (no trigger). Output: `*hæġl`. ✓ This is the desired behaviour.” It then adds the practical warning that a repair aimed at some other row would risk over-applying restoration to `hæġl`, even though `hæġl` itself has “no back-vowel-tail input” and should stay unaffected [Germanic/docs/DEV_NOTES.md:30668-30676].

For this row, the fragment carries three specific consequences that should be copied forward unchanged. First, `PROTO` and `PROTOFORM` remain identical because the row is already modelled as the nominative singular coda form; there is no hidden medial back vowel to encode in a different row-local protoform [Germanic/data/germanic-aligned-final.tsv:466-466; Germanic/docs/DEV_NOTES.md:30621-30621]. Second, the row is regular precisely because the relevant trigger for A-restoration is absent after apocope, not because restoration somehow “failed” before `-gl` [Germanic/docs/DEV_NOTES.md:30668-30672]. Third, the chosen OE target is specifically the unbroken/fronted nominative-singular form `hæġl`, not a generalized cover label for every attested paradigm or doublet spelling [Germanic/docs/DEV_NOTES.md:30621-30621; Germanic/data/old_english_wiktionary.tsv:114-114].

### DEV_NOTES: Campbell §158 doublet material preserved in the A-restoration audit

- Source heading: `Campbell §158` quotation inside the `Examples involving a cluster vs. a single consonant` / `Are there cases where A-restoration fails before *l specifically*?` discussion
- Source line hint: `30403-30413`, `30523-30534`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `campbell_158`; `doublets`; `paradigm_levelling`; `hægl_hagol`
- Recommended next use: `use_only_to_explain_doublet_background`
- Shared-with rows if relevant: `2130`, `2133`, `2164`

This fragment is not a dedicated hail memorandum, but it is still essential shared background because DEV_NOTES embeds the primary-source quotation that explains why `hagol` remains live philological evidence without displacing row 2050's target. The preserved quotation reads: “Before other groups, `a` is not restored except for a few instances before consonant plus liquid ... Yet it need not be doubted that `a` was originally widely restored before groups, and that it was subsequently removed by the analogy of forms in which a front vowel followed. This is reflected by some doublets, e.g. `gæfel, gafol` tribute, `hægel, hagol` hail ... due to an original distinction s. `hægl`, p. `haglas` ...” [Germanic/docs/DEV_NOTES.md:30403-30413]. DEV_NOTES then digests that evidence in plain project prose: `hægl / hagol` shows that restoration did occur in some `Cl` forms and was later undone by analogy in others, so the surface lexicon preserves paradigm levelling rather than a clean categorical phonological split [Germanic/docs/DEV_NOTES.md:30530-30540].

For row 2050, the proper use of this fragment is narrow. It supports the statement that `hagol` and `hægel` are real, relevant comparators in the OE lexical tradition and that the row's fronted target is not a fabricated spelling [docs/references/bright_anglo_saxon_reader.vision.txt:21352-21355; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20256-20258]. But it is **shared-background-only** support: it should not be misread as a warrant to replace the live row target with `hagol`, because DEV_NOTES itself immediately cashes the quotation out in nominative-singular terms and says the TSV deliberately chose the `*NomSg* unbroken/*æ*-form` [Germanic/docs/DEV_NOTES.md:30621-30621].

## Superseded or diagnostic material

- The only clearly relevant superseded project history is the rejected idea of broadening `OEARestorationIntervening` so that `*l` would count as licit cluster material for restoration. DEV_NOTES rejects that move as a weakening of the rule and says an unconditional `*Cl*` permission “would over-apply (likely to break `næġl, hæġl, seġl` NomSg outputs unless very carefully scoped)” [Germanic/docs/DEV_NOTES.md:30744-30750]. For row 2050 this is **diagnostic/superseded**, not live support: the row is one of the cases used to prove that the wider repair would be wrong.
- The debug snapshot is diagnostic confirmation, not a DEV_NOTES fragment. Its value is implementation-facing only: it shows that the current cascade already derives `hæġl` from `*xáglą` with no workaround, so the row does not belong in an unresolved exception bucket at present [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1927-1947; Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` and the absence of a manifest entry are likewise diagnostic only. They do not supply phonological argument; they simply confirm that no packet, memo, or manifest-backed lexeme report currently exists for this row and that this slice is replacing a DEV_NOTES lookup rather than condensing an existing row dossier [Germanic/docs/lexeme_reports/coverage_audit.md:262-262; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If a packet or memo is later created, decide whether the attestation paragraph should explicitly normalize the dictionary/headword mix `hægl ~ hægel ~ hagol` against project `hæġl`, so future reporting does not flatten the paradigm background into a single undifferentiated spelling [docs/references/bright_anglo_saxon_reader.vision.txt:21352-21355; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20256-20258].
- If `dev_notes_slices/index.tsv` is updated in a later pass, the main current anchor for row 2050 should be the row-local block at `30621` and `30668-30676`; the Campbell quotation is useful but should stay tagged as shared-background-only rather than as a standalone row-specific dossier [Germanic/docs/DEV_NOTES.md:30403-30413; Germanic/docs/DEV_NOTES.md:30621-30621; Germanic/docs/DEV_NOTES.md:30668-30676].
- If orthographic-normalization policy is revisited later, keep the distinction sharp between project `hæġl` with palatal `ġ` and dictionary spellings such as `hægl`, `hægel`, `hagol`; the current row evidence supports the same lexeme across those notational layers, but it does not yet contain a dedicated row-local normalization note in DEV_NOTES [Germanic/data/old_english_wiktionary.tsv:114-114; docs/references/bright_anglo_saxon_reader.vision.txt:21352-21355; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20256-20258].
