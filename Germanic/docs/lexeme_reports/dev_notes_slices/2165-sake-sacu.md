---
row_id: 2165
concept: sake
counterpart: sacu
proto: *sákō
protoform: *sákō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2165 sake / sacu

## Current row state

- CONCEPT: `sake` [Germanic/data/germanic-aligned-final.tsv:911-911]
- COUNTERPART: `sacu` [Germanic/data/germanic-aligned-final.tsv:911-911]
- PROTO: `*sákō` [Germanic/data/germanic-aligned-final.tsv:911-911]
- PROTOFORM: `*sákō` [Germanic/data/germanic-aligned-final.tsv:911-911]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:911-911]
- `oe_known_problems.tsv` has no row-local entry for row `2165`, lexeme `sacu`, concept `sake`, or proto/protoform `*sákō`; the row is not currently tracked as an OE exception or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- The current derivation trace is fully successful and explicit about the rule sequence: `PROTO: *sákō`, `EXPECTED: sacu`, `OUTPUTS: sacu`; NWGmc applies `Final Long O Raising: *sáku`, OE then applies `Anglo Frisian Brightening: *sæku` and `OE A Restoration: *saku`, and the surface outcome is `sacu` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3813-3832].
- The cognate-set neighbors in the live TSV currently show unaccented `*sakō` for Dutch, English, and German, while the OE row itself keeps accented `*sákō`; the DEV_NOTES material gathered here explains the rule pathway to `sacu` but does not itself adjudicate that accent-marking inconsistency [Germanic/data/germanic-aligned-final.tsv:909-912].

## Development-note summary

No dedicated `sake / sacu / *sákō` mini-dossier appears to survive in `Germanic/docs/DEV_NOTES.md`. For row 2165, the securely relevant authority is therefore shared rule-level material plus the live row and its current derivation trace. Those sources line up cleanly. The row is presently a regular-control item with `PROTO = PROTOFORM = *sákō` and OE target `sacu`, and the published trace derives that target without workaround or analogical override: word-final `*ō` first raises to `*u`, then root `a` brightens to `æ`, then `a` is restored before the following back vowel, yielding `sacu` as the exact surface output [Germanic/data/germanic-aligned-final.tsv:911-911; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3813-3832].

The first part of that pathway is explicitly preserved in DEV_NOTES' bimoric-versus-trimoric `*ō` analysis. The current statement for “Path A” says: “PGmc word-final bimoric non-nasalized long `*-ō` became short `*-u` in unstressed syllables in PNWGmc,” and the grammar models this as `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. That is exactly the row's first successful step, `*sákō > *sáku`. Just as importantly, DEV_NOTES distinguishes this from other final-`ō` histories: it is not the trimoric `*ô` pathway that yields OE `-a`, and it is not the later “surviving bimoric” path that yields PWGmc `*a` and then OE `-e` [Germanic/docs/DEV_NOTES.md:2711-2740]. For row 2165, the practical row-level conclusion is simple: the OE feminine ending `-u` is already the expected reflex of a word-final bimoric `*ō`.

The second part of the pathway is the ordinary A-restoration cycle after brightening. The row trace shows `*sáku > *sæku > *saku`, and the best current DEV_NOTES authority for that sequence is the late A-restoration literature summary. DEV_NOTES says Campbell's rule restores `a` “before all single consonants and geminates” and quotes Ringe-Taylor that stressed `*æ` followed by a single or geminate consonant and then a back vowel becomes `a`; the same table also preserves the class-II examples `macian`, `talian`, `bacian`, `lapian`, alongside nominal forms like `nacod`, `nafola`, `sadol`, `stapol` [Germanic/docs/DEV_NOTES.md:36524-36536]. `sacu` itself is not named there, but its structural environment is the same one those examples secure: root `a`, single `k`, and a following back vowel in the next syllable. The row therefore does not need a special lexeme-specific rescue note to explain `*sæku > *saku`; it belongs to the ordinary restored-`a` environment.

The late post-fix verification note strengthens that reading because it checks the same `sak-/mak-` phonological neighborhood after the restoration bug fixes. DEV_NOTES records as successful probes: “`*sákōjaną → sacian`, `*mákōjaną → macian` ✓” [Germanic/docs/DEV_NOTES.md:36757-36767]. Those are not this noun row, but they matter because they show that the repaired current grammar still handles the same root shape with `k` plus a following back-vocalic tail exactly as expected. Combined with the live trace for `*sákō > sacu`, that is enough to treat row 2165 as a regular success case rather than as a silent exception. The row-level distinction among stages is therefore minimal but still worth keeping explicit: comparative `PROTO = *sákō`, OE-facing `PROTOFORM = *sákō`, and attested OE target `COUNTERPART = sacu` are all aligned in the present analysis [Germanic/data/germanic-aligned-final.tsv:911-911; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3813-3832].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2711-2720

- Source heading: `Bimoraic vs. Trimoraic *ō: Comprehensive Analysis`
- Source line or section hint: `lines 2711-2720`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `final_ō_raising`; `bimoric_vs_trimoric`; `regular_pathway`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best current DEV_NOTES authority for the row's final vowel. It states the rule in exactly the way the live trace uses it: “PGmc word-final bimoric non-nasalized long `*-ō` became short `*-u` in unstressed syllables in PNWGmc,” and the FST implementation line immediately underneath says `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. For row 2165, that establishes the first indispensable step `*sákō > *sáku` and explains why OE `sacu` ends in `-u` without needing any separate OE-only analogical ending.

The same fragment is also useful because it excludes the wrong competing analyses. DEV_NOTES puts trimoric `*ō` in a different path with OE `-a`, and “surviving bimoric” `*ō` in another path with PWGmc `*a` and OE `-e` [Germanic/docs/DEV_NOTES.md:2722-2740]. Row 2165 belongs to neither of those. Its current successful trace fits Path A exactly, so later writeups should preserve that classification rather than flattening the row into a generic “final long vowel shortened” note.

### DEV_NOTES:line-36524-36536

- Source heading: `The canonical conditioning of A-restoration (literature consensus)`
- Source line or section hint: `lines 36524-36536`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `a_restoration`; `handbook_consensus`; `brightening`; `back_vowel_trigger`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This current literature table is the strongest shared authority for the middle of the row's derivation, where the trace shows `*sáku > *sæku > *saku`. DEV_NOTES quotes Campbell that “The restoration of `a` is common before all single consonants and geminates” and quotes Ringe-Taylor that stressed `*æ` became `a` when “immediately followed by a single or geminate consonant or `sC`-cluster which was in turn followed by a back vowel” [Germanic/docs/DEV_NOTES.md:36529-36534]. That is the exact structural logic needed for `*sæku > *saku`: one intervening `k`, then back `u`.

The examples preserved in the same table are not row-2165-specific, but they are still concrete enough to matter for this row. DEV_NOTES lists class-II weak verbs such as `macian` and `talian`, and nouns/adjectival forms such as `nacod`, `nafola`, `sadol`, `stapol`, all showing that the restored-`a` environment is not limited to one stem class or one morphological category [Germanic/docs/DEV_NOTES.md:36531-36536]. For `sacu`, that means the brightening/restoration cycle should be treated as ordinary shared phonology, not as special pleading for this lexeme.

### DEV_NOTES:line-36757-36767

- Source heading: `§17.25.8 Post-fix verification`
- Source line or section hint: `lines 36757-36767`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `post_fix_validation`; `a_restoration`; `sak_base`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is not a noun-specific `sacu` note, but it is the closest late validation that DEV_NOTES preserves for the same phonological environment. After the A-restoration bug fixes, the verification list reports: “`*sákōjaną → sacian`, `*mákōjaną → macian` ✓” [Germanic/docs/DEV_NOTES.md:36757-36767]. That matters for row 2165 because it shows the repaired grammar still handles the `sak-/mak-` base with `k` plus a following back-vocalic tail as expected.

For later reporting, this fragment should be used carefully but positively. It does not prove the noun row by itself, and it should not be cited as if DEV_NOTES had a dedicated `sacu` subsection. What it does establish is that the same restoration-sensitive environment remained stable in late regression testing, so the live successful derivation `*sákō > sacu` is not a fragile accident or a pathway that later fixes broke [Germanic/docs/DEV_NOTES.md:36757-36767; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3813-3832].

## Superseded or diagnostic material

- No securely attachable row-local superseded `sacu` dossier currently survives in `Germanic/docs/DEV_NOTES.md`. The usable material for row 2165 is shared-rule material, not a lexeme-specific correction history [Germanic/docs/DEV_NOTES.md:2711-2720,36524-36536,36757-36767].
- The main caution is editorial rather than phonological. The live cognate set currently mixes accented OE-row `*sákō` with unaccented sibling-row `*sakō`, but the DEV_NOTES fragments gathered here do not treat that as a resolved note topic; later reviewers should not manufacture a phonological problem out of that spelling mismatch without separate authority [Germanic/data/germanic-aligned-final.tsv:909-912].
- The `*sákōjaną → sacian` verification line is best read as shared post-fix support, not as a hidden substitute for direct noun-specific source discussion. It helps confirm pathway stability, but it does not turn the verb derivative into the controlling authority for row 2165 [Germanic/docs/DEV_NOTES.md:36757-36767].

## Open questions for later work

- Decide whether the accent mismatch inside the live cognate set (`*sákō` in the OE row versus `*sakō` in neighboring rows) is intentional house style or an editorial normalization issue; the current DEV_NOTES material used for this slice does not settle it [Germanic/data/germanic-aligned-final.tsv:909-912].
- If a later final report wants a direct lexeme-specific quotation naming OE `sacu`, that evidence will need to come from primary-source or packet-level literature work rather than from a surviving dedicated `DEV_NOTES` subsection. The present slice is secure on rule mechanics, but not rich in row-specific quotation [Germanic/docs/DEV_NOTES.md:2711-2720,36524-36536,36757-36767].
- If `dev_notes_slices/index.tsv` is updated later, the securely attachable current anchors are the final-`ō` Path A rule (`2711-2720`), the late A-restoration literature summary (`36524-36536`), and the post-fix `sak-/mak-` verification cluster (`36757-36767`) [Germanic/docs/DEV_NOTES.md:2711-2720,36524-36536,36757-36767].
