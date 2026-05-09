---
row_id: 2285
concept: while
counterpart: hwīl
proto: *xwḯlō
protoform: *xwī́lō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2285 while / hwīl

## Current row state

- Live OE row `2285` currently reads `CONCEPT = while`, `COUNTERPART = hwīl`, `PROTO = *xwḯlō`, `PROTOFORM = *xwī́lō`, `DERIVATION_CLASS = regular`, with duplicated Wiktionary inheritance sourcing and no row-local caution note beyond that source string [Germanic/data/germanic-aligned-final.tsv:1379-1379; Germanic/data/old_english_wiktionary.tsv:342-342].
- The published OE derivation trace treats the row as a clean exact match. It records `PROTO: *xwḯlō`, `EXPECTED: hwīl`, `OUTPUTS: hwīl`, with only `NWGmc Final Long O Raising: *xwḯlu` and then `OE High Vowel Apocope: *xwḯl` before surface `Outcome: hwīl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5802-5822].
- Coverage infrastructure currently lists the row as `regular` with `none` in every support-file column, and the required support-file check likewise turned up no row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file to link here [Germanic/docs/lexeme_reports/coverage_audit.md:410-410].
- Repo-local comparative support for the lexeme itself is straightforward even if the English concept gloss is modernized. Ringe gives PGmc `*hwīlō 'time'` and cites `Goth. ƕeila, OE hwīl` from PIE zero grade `*kwih1-` [docs/references/ringe_vol1_pie_to_pgmc.txt:4448-4449; @Ringe2006, p. 97]. For this row, that is enough to show that OE `hwīl` is the inherited noun/adverbial time-word underlying the modern concept label `while`, not an ad hoc substitute target.
- The row also needs the same notation warning as the neighboring stressed-long-`ī` slices. Here `COUNTERPART = hwīl` is the OE surface output; `PROTO = *xwḯlō` is the current OE-facing machine-safe input using single-codepoint stressed `*ḯ`; and `PROTOFORM = *xwī́lō` preserves the older/shared combining-acute notation across the cognate set (`wijl / while / Weile`) [Germanic/data/germanic-aligned-final.tsv:1377-1380]. Those two proto spellings should not be treated as rival etymologies.

## Development-note summary

No dedicated row-specific mismatch dossier for `while / hwīl` survives in `DEV_NOTES.md`. That has to be said plainly. The securely attachable `DEV_NOTES` material is instead the stressed-long-`ī` migration note in `§17.46`, where row 2285 appears only because its root vowel belonged to the cohort that had to move from older combining-acute notation to single-codepoint `*ḯ` [Germanic/docs/DEV_NOTES.md:41893-42040]. This makes row 2285 a **thin but current** slice: the row is philologically plausible and derivationally regular, but the surviving development-note burden is mainly notation and verification history rather than a lexeme-specific dispute.

The most important thing to preserve is the distinction between the two proto spellings and the OE output. `COUNTERPART = hwīl` is the actual OE target and current exact-match output [Germanic/data/germanic-aligned-final.tsv:1379-1379; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5802-5822]. `PROTO = *xwḯlō` is the row's present live input into the OE cascade, where `ḯ` marks a stressed long root vowel in a way foma can reliably consume [Germanic/docs/DEV_NOTES.md:41925-41939]. `PROTOFORM = *xwī́lō` is the older/shared comparative spelling still visible across the cognate set and in neighboring non-OE rows [Germanic/data/germanic-aligned-final.tsv:1377-1380]. For current project purposes, these are two notation layers for the same inherited lexeme, not two chronological proto-stages and not competing editorial policies.

`DEV_NOTES` is explicit about the notation point in wording worth preserving directly: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. That sentence controls how row 2285 should be read. It means the project did **not** discover a special OE preform `*xwḯlō` different in substance from comparative `*xwī́lō`; it merely replaced a fragile input spelling with one the transducer could handle consistently. The same note immediately explains why that distinction disappears again at surface level: `OldEnglishRemoveStars` maps `{*ḯ} -> ī`, because OE orthography does not distinguish stressed-root long `ī` from other long `ī` once the internal rule gating has been done [Germanic/docs/DEV_NOTES.md:41952-41957]. That is exactly what the row trace shows in practice when `*xwḯlō` ends as ordinary written `hwīl`.

Row 2285's only direct naming inside `DEV_NOTES` comes in the migration inventory, where Batch 4 lists `2197, 2257, 2285 | slīm, **tīd** (i-umlaut trigger w/ *ḯ no-op ✓), hwīl` [Germanic/docs/DEV_NOTES.md:42020-42025]. The silence around `hwīl` inside that batch line is itself informative. Unlike `tīd`, which needed an explanatory parenthesis because its suffix still counts as an i-umlaut trigger, `hwīl` is present simply as a migrated stressed-`ī` row with no further complication recorded. In other words, `DEV_NOTES` does not preserve any claim that `hwīl` needed analogical rescue, a target switch, a paradigm-cell substitution, or an exception label. It appears as a regular member of the notation-migration cohort.

The trace evidence is therefore especially useful here because it shows what the thin `DEV_NOTES` note leaves implicit. The current derivation is short and orderly: `*xwḯlō` first undergoes `NWGmc Final Long O Raising` to `*xwḯlu`, then `OE High Vowel Apocope` removes the final high vowel and yields `*xwḯl`, after which ordinary OE orthography surfaces as `hwīl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5811-5822]. That matters because an older general apocope investigation still preserved `*xwīlō → hwīlō (exp. hwīl)` among unresolved `*-ō` outputs [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:304-310]. For this row, that older material is diagnostic only. The live published trace now shows that the row is no longer stranded at final `-ō`; the high-vowel-apocope path in the current cascade reaches the correct `hwīl` outcome.

The safest present conclusion is therefore conservative. Row 2285 is currently a regular exact-match row whose lexeme identity is not in serious doubt. The surviving `DEV_NOTES` value lies in documenting the stressed-long-`ī` encoding migration and in confirming that `hwīl` belongs to the same inherited `*hwīlō` family cited by Ringe [Germanic/docs/DEV_NOTES.md:41893-42040; docs/references/ringe_vol1_pie_to_pgmc.txt:4448-4449; @Ringe2006, p. 97]. What is missing is not evidence for the row's correctness, but a richer row-dedicated note. On present evidence this slice should remain cautious and should not overstate the surviving `DEV_NOTES` material as if there were a dedicated lexeme controversy.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `surface_mapping`
- Recommended next use: `cite_if_explaining_notation_layers`
- Shared with row IDs: `2101`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2286`; `2290`; `2296`

This is the controlling current fragment for row 2285 even though it is a shared infrastructure note rather than a `hwīl` dossier. It explains why stressed long `*ī` had to be moved onto a dedicated symbol and preserves the key wording: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. For row 2285, that sentence is what prevents later writers from misreading `PROTO = *xwḯlō` and `PROTOFORM = *xwī́lō` as rival reconstructions.

The same fragment also preserves the surface-side consequence that matters for this slice: `OldEnglishRemoveStars` maps `{*ḯ} -> ī`, because OE orthography does not encode the internal stress-tier distinction once the relevant rule interactions are over [Germanic/docs/DEV_NOTES.md:41952-41957]. That is exactly the bridge from live proto input `*xwḯlō` to surface `hwīl`.

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 ... E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42026`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `regular_row`
- Recommended next use: `cite_if_documenting_row_history`
- Shared with row IDs: `2197`; `2257`

This is the only securely attachable `DEV_NOTES` fragment that names row 2285 directly. Batch 4 lists `2197, 2257, 2285 | slīm, **tīd** (i-umlaut trigger w/ *ḯ no-op ✓), hwīl` [Germanic/docs/DEV_NOTES.md:42020-42025]. The fragment is thin, but it is still the row's best explicit anchor because it shows that `hwīl` participated in the deliberate migration from older `*ī` notation to stressed `*ḯ`.

The fragment should be read narrowly. It does not preserve a mismatch diagnosis, a target correction, or a philological dispute unique to `hwīl`. Its value is that it names the row and places it in a current verified implementation cohort.

### DEV_NOTES:line-42031-42040

- Source heading: `§17.46 ... F. Verification`
- Source line or section hint: `lines 42031-42040`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `shared_probe_block`; `regular_output`; `diagnostic_only`
- Recommended next use: `use_as_supporting_history_only`
- Shared with row IDs: migrated `*ḯ` rows

The verification block does not probe `hwīl` by name, but it is still relevant background for the row because it documents that the stressed-`ḯ` migration was checked immediately afterward and held the mismatch totals steady [Germanic/docs/DEV_NOTES.md:42031-42040]. For row 2285, the practical meaning is modest: the row entered the new notation cohort without creating a fresh regression bucket.

This fragment is therefore secondary. The actual row-local confirmation of success comes from the later published derivation trace, not from an explicit `hwīl` probe in this block [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5802-5822].

## Superseded or diagnostic material

- Older/shared combining-acute spelling `*xwī́lō` should stay visible in this slice because it still survives in the row's `PROTOFORM` field and across the non-OE cognate-set rows [Germanic/data/germanic-aligned-final.tsv:1377-1380]. But `DEV_NOTES` makes clear that the migration to `*xwḯlō` was driven by input-tokenization reliability, not by a change in etymology [Germanic/docs/DEV_NOTES.md:41925-41939].
- The earlier apocope investigation entry `*xwīlō → hwīlō (exp. hwīl)` is useful project history but should now be treated as superseded diagnostic material, not as the live row state [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:304-310]. The current published trace shows that the live cascade reaches `hwīl` successfully via final-`ō` raising and later high-vowel apocope [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5811-5822].
- No surviving `DEV_NOTES` fragment argues that row 2285 is analogical, dialectally aberrant, or dependent on an alternate paradigm cell. The slice's main limitation is thin row-local prose, not the presence of a serious competing analysis.

## Open questions for later work

- If a fuller lexeme report is ever written, decide whether the report should foreground the gloss issue explicitly: Ringe's comparator is `*hwīlō 'time'`, while the TSV concept label is modern English `while` [docs/references/ringe_vol1_pie_to_pgmc.txt:4448-4449; @Ringe2006, p. 97]. The present slice only needs to note that the OE target is the same inherited lexeme.
- If later documentation wants stronger OE dictionary support, add a direct dictionary citation for `hwīl` rather than relying chiefly on Ringe plus repo traces. The current slice is adequate, but its lexicographic support is lighter than rows with packets or memos.
- If `dev_notes_slices/index.tsv` is revisited later, row 2285 still looks better kept as a no-index slice. The only strong row-explicit anchor is `DEV_NOTES:line-42006-42026`, and that anchor documents notation migration history rather than a substantive lexeme-specific argument.
