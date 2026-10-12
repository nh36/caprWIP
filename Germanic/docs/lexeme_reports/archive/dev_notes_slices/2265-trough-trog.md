---
row_id: 2265
concept: trough
counterpart: trog
proto: *trúgą
protoform: *trúgą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2265 trough / trog

## Current row state

- The live row now reads `CONCEPT = trough`, `COUNTERPART = trog`, `PROTO = *trúgą`, `PROTOFORM = *trúgą`, and `DERIVATION_CLASS = regular`; the row-history/source cell still preserves inherited-etymology placeholders, while the row-structure note states the operative normalization explicitly: `Normalizing to -g spelling per Kroonen, Hall; both trog/troh attested` [Germanic/data/germanic-aligned-final.tsv:1299-1299].
- `PROTO` and `PROTOFORM` are intentionally **not split** in the current row. `PROTO = *trúgą` is the comparative Proto-Germanic headword used for the cognate set; `PROTOFORM = *trúgą` is also the actual derivational input used by the OE cascade; `COUNTERPART = trog` is the selected OE target after the repo-wide decision to normalize this word-final alternation to `-g`, not to Late West Saxon `-h` [Germanic/data/germanic-aligned-final.tsv:1299-1299; Germanic/docs/DEV_NOTES.md:10990-11030].
- The published derivation trace already matches the live row without workaround: `*trúgą` undergoes NWGmc `u`-lowering to `*trógą`, then OE heavy-syllable nasal apocope to `*tróg`, surfacing as `trog` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5479-5498]. That means the current row is not using an analogical repair, alternate paradigm cell, or spelling-side exception flag.
- No row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found in the expected support locations during slice preparation. The only directly relevant repo-local support outside the live row is the shared `DEV_NOTES` discussion of word-final `g ~ h` spelling convention and the inherited Wiktionary extract still listing `troh`, which helps explain why the row note now documents a normalization choice rather than a source consensus [Germanic/data/old_english_wiktionary.tsv:324-324].

## Development-note summary

The surviving `DEV_NOTES` material for row 2265 is real but **shared and comparatively thin**. There is no long, row-specific dossier of the kind written for major paradigm-cell disputes. Instead, `trog` appears inside the shared section `Word-Final *g Spirantization Research (2026-03-15)`, where the project worked through whether final OE `g` should be normalized as `g` or `h` in this small cluster of forms [Germanic/docs/DEV_NOTES.md:10905-11030]. This slice therefore needs to preserve the project decision faithfully without overstating the amount of lexeme-local argumentation.

The starting problem is explicit. The mismatch report had treated `*trugą` as yielding `trog` while the then-current expected target was `troh`, pairing this row with `*laugō → lēag / lēah` as the same type of `g_vs_h` word-final discrepancy [Germanic/docs/DEV_NOTES.md:10907-10917]. `DEV_NOTES` does **not** frame that as a problem in the comparative reconstruction. The proto side remained `*trugą` throughout. The dispute was orthographic/normalizational at the Old English end: should the project encode a final-spirant spelling rule and target Late West Saxon `troh`, or should it keep the derivation unchanged and normalize the row to attested `trog` instead? That is the key distinction future work must keep clear. `PROTO` and `PROTOFORM` stayed stable; only the preferred OE `COUNTERPART` convention changed [Germanic/docs/DEV_NOTES.md:10965-11024].

The section's phonological background is drawn mainly from Campbell. `DEV_NOTES` quotes Campbell §446: “The voicing of medial spirants was followed by the unvoicing of final spirants ... but for final ɣ there is an increasing use of the symbol `h` after Alfred's time,” then immediately summarizes the chronological split: early texts mostly show `g`, late West Saxon uses `h` increasingly, and northern material uses `h` only rarely [Germanic/docs/DEV_NOTES.md:10920-10930; @Campbell1959, §446]. The follow-up quotation from Campbell §447 is equally important because it prevents over-regularization: “The interchange of `h` and `g` in forms like `burh—burge` leads in W-S to forms like `héage, bléoge` ... There are also inverted spellings like `mearg, burg ...` for `mearh, burh`” [Germanic/docs/DEV_NOTES.md:10931-10937; @Campbell1959, §447]. In other words, this is not a neat categorical sound-law split where every OE target must be either `-g` or `-h`; spelling competition is part of the evidence base.

That is exactly why the row settled where it did. `DEV_NOTES` explicitly judged the repo's existing targets to be inconsistent by convention rather than by derivation: `lēah, troh` reflected a Late West Saxon `-h` choice, while `bōg, dāg` reflected an earlier/northern `-g` choice [Germanic/docs/DEV_NOTES.md:10959-10961]. The note then canvassed four options and chose the one most conservative for the system: **do not add a new final-spirantization rule; normalize the affected OE rows to `-g` instead** [Germanic/docs/DEV_NOTES.md:10963-10986]. For row 2265 that means the live derivation remained regular and the row-level fix was purely a target update from `troh` to `trog` [Germanic/docs/DEV_NOTES.md:11021-11024].

The lexeme-specific support embedded in that shared section is concise but strong enough to preserve verbatim. Under “Research confirming `-g` spellings are attested,” `DEV_NOTES` lists four row-relevant authorities for `trog`: Kroonen, Hall, Kaluza, and Orel [Germanic/docs/DEV_NOTES.md:10996-11019]. The note quotes Kroonen's Proto-Germanic entry as `OE trog, troh m.`, Hall as `trog m. hollow vessel, 'trough'`, Kaluza as `ae. trog, roh` (clearly intended as `troh`, showing the OCR's weakness but still preserving the contrast), and Orel as `OE troʒ 'trough'` [Germanic/docs/DEV_NOTES.md:11013-11017]. Those are not four different reconstructions; they are four pieces of evidence that both spellings circulated, with `trog` sufficiently well attested to support project normalization.

The reference files in the repo support that reading closely enough for a working-note slice. Kroonen's dictionary gives `*truga- n. 'trough' - ON trog n. 'id.', OE trog, troh m. 'id.'` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:26745-26746; @Kroonen2013]. Clark Hall has separate support for both the normalized target and the competing late spelling: `trog m. hollow vessel, 'trough,' tray` and `troh (LWS) trog` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:41469-41475; @ClarkHall1960]. Kaluza's grammar likewise lists both spellings side by side in the final-spirant context: `genög, genöh ... trog, troh Trog` [docs/references/kaluza_historische_grammatik_englisch.txt:7607-7610; @Kaluza1901]. Bülbring is especially useful for the project's normalization policy because he both records `troh 'Trog'` and states more generally that even in younger texts spellings with `g` predominate and that some witnesses lack `h` forms entirely [docs/references/bulbring_altenglisches_elementarbuch.txt:9050-9055; @Bulbring1902, §489]. Orel, finally, keeps the lexeme in the same comparative set as the other West Germanic `trog` forms: `OE troʒ id., OFris trog id., MLG troch id., OHG trog id.` [docs/references/orel_handbook_germanic_etymology.vision.txt:45402-45404; @Orel2003, p. 410].

For future work, the practical takeaway is narrow but important. This row is **not** a protoform dispute, not a paradigm-cell dispute, and not an unresolved exception bucket. It is a settled target-normalization case inside a shared orthographic-policy note. `PROTO = *trúgą` remains the comparative and derivational source; `COUNTERPART = trog` is the chosen OE normalization because the project decided to prefer the conservative/early/northern `-g` convention wherever attestation supported it, rather than to make the transducer encode a late-spelling alternation [Germanic/docs/DEV_NOTES.md:10990-11030; Germanic/data/germanic-aligned-final.tsv:1299-1299]. The surviving `DEV_NOTES` evidence is therefore enough to justify the current row, but not enough to pretend there was a deep lexeme-only investigation beyond that policy choice.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-10905-10917

- Source heading: `Word-Final *g Spirantization Research (2026-03-15)` / `The Problem`
- Source line or section hint: `lines 10905-10917`
- Fragment type: `shared_problem_definition_with_row_specific_example`
- Status: `diagnostic_but_still_useful`
- Issue tags: `g_vs_h`; `row_history`; `expected_target_change`; `not_proto_change`
- Recommended next use: `use_to_explain_why_row_was_touched`
- Shared with row IDs: `2116`

This fragment preserves the exact mismatch state that generated the later target switch. It lists `*trugą → trog (expected troh)` beside `*laugō → lēag (expected lēah)` and therefore shows that row 2265 entered DEV_NOTES as a **spelling-convention conflict at the OE output end**, not as a challenge to the proto reconstruction or to the derivation itself [Germanic/docs/DEV_NOTES.md:10909-10917]. That is still worth citing because later documentation could otherwise misread the live row as if `*trúgą` had been specially adjusted to make `trog` work. It was not: the output already came out as `trog`; the dispute was whether the target should stay `troh`.

### DEV_NOTES:line-10920-10937

- Source heading: `Source Research`
- Source line or section hint: `lines 10920-10937`
- Fragment type: `shared_phonology_and_spelling_background`
- Status: `current`
- Issue tags: `Campbell`; `final_spirant`; `chronology`; `g_h_alternation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2116`

This is the best background anchor for why a `trog`/`troh` split can exist without forcing a row-local reconstruction change. DEV_NOTES quotes Campbell on the increasing use of final `h` after Alfred's time, then preserves the summary that early texts mostly show `g`, late West Saxon uses `h` more often, and northern material rarely does so [Germanic/docs/DEV_NOTES.md:10920-10930; @Campbell1959, §446]. The immediately following quotation about `burh—burge`, `héage`, and “inverted spellings” is equally valuable because it blocks any simplistic “OE must really have had only one correct spelling” narrative [Germanic/docs/DEV_NOTES.md:10931-10937; @Campbell1959, §447]. For row 2265, this shared fragment explains why both `trog` and `troh` can be genuine evidence while only one of them is chosen as the dataset target.

### DEV_NOTES:line-10959-11030

- Source heading: `Analysis`; `Options`; `Decision: Use -g Spelling Convention (2026-03-15)`
- Source line or section hint: `lines 10959-11030`
- Fragment type: `current_row_policy_in_shared_section`
- Status: `current`
- Issue tags: `live_row_policy`; `target_normalization`; `no_new_rule`; `indexable_anchor`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs: `2116`

This is the controlling current fragment for the live row. DEV_NOTES first states the policy conflict plainly: `lēah, troh` reflect a Late West Saxon `h` convention, while `bōg, dāg` reflect an earlier/northern `g` convention [Germanic/docs/DEV_NOTES.md:10959-10961]. It then chooses Option D with `-g` convention, says that no final-spirantization rule should be added, and gives the operational row update explicitly: `Update TSV targets: lēah → lēag, troh → trog` [Germanic/docs/DEV_NOTES.md:10990-11024]. For row 2265, this is the strongest available anchor for `index.tsv` if shared-policy anchors are admissible, because it records both the rationale and the exact accepted implementation.

### DEV_NOTES:line-10996-11019

- Source heading: `Research confirming -g spellings are attested`
- Source line or section hint: `lines 10996-11019`
- Fragment type: `row_local_attestation_list_inside_shared_policy_note`
- Status: `current`
- Issue tags: `attestation`; `Kroonen`; `Hall`; `Kaluza`; `Orel`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most lexeme-addressable passage surviving in DEV_NOTES itself. It gathers exactly the authorities used to justify the row's `-g` normalization: Kroonen `OE trog, troh m.`, Hall `trog m. hollow vessel, 'trough'`, Kaluza `ae. trog, roh`, and Orel `OE troʒ 'trough'` [Germanic/docs/DEV_NOTES.md:11013-11017]. The passage is short, but it does real work. It shows that the project did not switch the row merely for FST convenience; it switched because `trog` is explicitly attested in the source base and because both spellings coexist in the literature.

## Superseded or diagnostic material

- The superseded material for row 2265 is the **older target convention**, not the comparative reconstruction. Earlier project state treated `troh` as the expected normalized OE target; the current row instead treats that as a Late West Saxon spelling choice that has been replaced by `trog` under the adopted `-g` policy [Germanic/docs/DEV_NOTES.md:10909-10917,10990-11024].
- The inherited Wiktionary support file is now diagnostic rather than controlling for this row. It still lists `trough → troh`, which explains the duplicated inherited-etymology placeholders in the row history/source area, but the live row note explicitly documents the repo's divergence from that default normalization [Germanic/data/old_english_wiktionary.tsv:324-324; Germanic/data/germanic-aligned-final.tsv:1299-1299].
- The derivation trace is also diagnostic rather than argumentative. Its value is implementation-facing: it confirms that `*trúgą` already derives to `trog` regularly and that the accepted row change did not require a new sound-change rule or a modified protoform [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5479-5498].

## Open questions for later work

- If `index.tsv` later wants an anchor for this row, decide whether shared-policy notes count as sufficiently lexeme-addressable support. The row has no standalone lexeme dossier, but `10996-11019` and `10990-11024` are both explicit enough to function as working anchors.
- If a later full lexeme report is written, it should quote Clark Hall's `troh (LWS) trog` more directly alongside the Kroonen and Kaluza evidence, since that is the cleanest repo-local formulation of the dialect/normalization split [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:41469-41475].
- If row notes are ever tightened, consider making the Wiktionary divergence explicit in one sentence: current data selection prefers attested `trog` as the normalized early/northern spelling, while preserving `troh` as a real Late West Saxon competitor rather than denying its existence.
