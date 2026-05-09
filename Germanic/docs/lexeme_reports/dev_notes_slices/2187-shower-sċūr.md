---
row_id: 2187
concept: shower
counterpart: sċūr
proto: *skūrō
protoform: *skūrō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2187 shower / sċūr

## Current row state

- The live OE row reads `CONCEPT = shower`, `COUNTERPART = sċūr`, `PROTO = *skūrō`, `PROTOFORM = *skūrō`, `DERIVATION_CLASS = regular`; the TSV note field is empty, so the row currently carries no row-local explanatory note in the dataset itself [Germanic/data/germanic-aligned-final.tsv:996-996].
- `PROTO` and `PROTOFORM` are identical in the live TSV. The row is therefore not using a separate OE-facing substitute stem, a retargeted paradigm cell, or a different handbook-stage proxy input. The modelling input remains the same `*skūrō` that labels the cognate set [Germanic/data/germanic-aligned-final.tsv:996-996].
- `oe_known_problems.tsv` has no surviving entry for row `2187`, for `shower`, for `sċūr`, or for `*skūrō`, so the row is not currently managed as an OE exception, unresolved mismatch, or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still treats the row as ordinary uncovered material rather than as a report-backed case: `coverage_audit.md` lists `2187 | shower | sċūr | regular | no | - | - | - | none` [Germanic/docs/lexeme_reports/coverage_audit.md:350-350].
- The current published derivation trace is an exact match and already states the whole live pathway compactly: `PROTO: *skūrō`, `EXPECTED: sċūr`, `OUTPUTS: sċūr`, with `NWGmc Final Long O Raising: *skūru`, `OE Sk Palatalization: *ʃūru`, and `OE High Vowel Apocope: *ʃūr` before orthographic output `sċūr` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4184-4198].
- The full trace confirms the same sequence in rule-by-rule detail. Nothing else fires materially for the row: final `*ō` first raises to `*u`, initial `*sk` becomes `*ʃ`, final `*u` is then deleted, and the orthographic layer writes the result as `sċūr` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28423-28536].

## Development-note summary

No dedicated, row-length `DEV_NOTES.md` audit for `2187 shower / sċūr / *skūrō` appears to survive. That has to be said plainly, because this slice cannot honestly pretend to preserve a lost lexeme-specific controversy comparable to rows with explicit retargeting or exception dossiers. The usable material is instead (i) the live row, (ii) the live exact-match derivation trace, and (iii) a small number of shared DEV_NOTES rule discussions that explain the two operations this row actually depends on: final `*-ō > *-u` in Northwest Germanic, followed by later OE high-vowel apocope after a heavy syllable, with initial `*sk` written in normalized OE as `sċ-` [Germanic/data/germanic-aligned-final.tsv:996-996; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4184-4198; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28423-28536; Germanic/docs/DEV_NOTES.md:2711-2720,18624-18657,2987-2993]. That evidentiary shape is enough for a replacement working note, but it is still thin and mostly shared; on present evidence this should remain a no-index slice.

The notation layers need to stay distinct because the local reference files do not all write the same reconstruction in the same way. The live row stores both `PROTO` and `PROTOFORM` as singular-form `*skūrō` [Germanic/data/germanic-aligned-final.tsv:996-996]. Kroonen instead writes the lexeme as `*skūra/ō- m./f. 'short shower (of rain/hail)'`, which is a stem-class dictionary notation rather than a competing OE-facing row protoform [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23312-23327]. Orel gives a headword `*skūrō` but immediately writes the body as `*skūraz sb.f./m.` while listing `OE scúr id.`; that is likewise dictionary presentation, not evidence that the row should split into a different live project protoform [docs/references/orel_handbook_germanic_etymology.vision.txt:38722-38728]. On the OE side, Bright writes plain `scur, m., shower`, not dotted `sċūr` [docs/references/bright_anglo_saxon_reader.txt:24631-24631]. The conservative reading is therefore: `*skūrō` is the project's live modelling input; `*skūra/ō-` and Orel's mixed `*skūrō` / `*skūraz` are lexicographic notation layers; and `sċūr` is the project's normalized OE target corresponding to source spellings such as `scur` or `scúr`, not a separate lexical item [Germanic/data/germanic-aligned-final.tsv:996-996; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23325-23327; docs/references/orel_handbook_germanic_etymology.vision.txt:38722-38728; docs/references/bright_anglo_saxon_reader.txt:24631-24631].

The current derivation itself is straightforward but still needs to be stated explicitly rather than summarized as merely “regular.” First, shared DEV_NOTES rule inventory says that word-final bimoraic PGmc `*-ō` became PNWGmc `*-u`, modelled by `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. The live trace shows exactly that first step for this row: `*skūrō > *skūru` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28448-28457]. Second, the row does not undergo any of the common vowel complications: there is no fronting, no breaking, no umlaut, and no palatal diphthongization; every such stage is `[no-change]` in the full trace [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28468-28500]. Third, `OESkPalatalization` changes initial `*sk-` to `*ʃ-`, after which `OEHighVowelApocope` deletes the final short `*u`, giving `*ʃūr`, orthographic `sċūr` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28490-28536]. The row therefore stays fully within the basic pipeline: inherited long `ū` survives, raised final `u` is lost, and the only consonantal change of consequence is the regular OE treatment of initial `*sk`.

The orthographic normalization point should also be kept explicit, because this is one of the few places where DEV_NOTES still preserves wording relevant to the row even though the row itself is never named. DEV_NOTES says of an older `sk/sc` debugging issue that “The sk → sc change is not palatalization but a general OE shift of /sk/ → /ʃ/ spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. Campbell likewise says that in the course of OE “every initial sc and sé became [ʃ]” (OCR-corrupted in the file, but the statement is clear in context), Hogg says the usual spelling `<sc>` was used both for `/ʃ/` and `/sk/` and that editors commonly dot the `<c>` when `/ʃ/` is intended, and Fulk says PGmc `*sk` is preserved as /sk/ only in limited medial/final back-vowel environments and is otherwise palatal in OE [docs/references/campbell_old_english_grammar.txt:2408-2412; docs/references/hogg_vol1.txt:4610-4616; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:7904-7908]. For this row, that means source `scur/scúr` and dataset `sċūr` should be treated as orthographic/editorial variants of the same OE outcome, not as a reason to multiply forms or to infer a special row-specific sound law.

Philological support is consistent and uncomplicated. Kroonen lists `Go. skura`, `ON skúr`, `OE scur`, `E shower`, `MDu. schuur`, `OHG skūr`, `G Schauer`; Orel gives essentially the same cognate set and explicitly states `OE scúr id.`; Bright records `scur, m., shower`; and Orel separately lists the compound `*rezna-skūrō` with `OE rezn-scúr id.` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23325-23329; docs/references/orel_handbook_germanic_etymology.vision.txt:33699-33701,38722-38728; docs/references/bright_anglo_saxon_reader.txt:24631-24631]. None of this suggests an analogical OE substitute stem, a paradigm-cell retarget, or a known mismatch hidden elsewhere in the repo. The row looks like a genuine regular-control item whose main documentation need is not repair but explicit separation of project notation, dictionary notation, and normalized OE spelling.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2711-2720

- Source heading: `Path A: PNWGmc Raising (bimoric *ō that is word-final in PGmc)`
- Source line or section hint: `lines 2711-2720`
- Fragment type: `current_shared_rule_statement`
- Status: `current`
- Issue tags: `final_long_o_raising`; `protoform_scope`; `regular_pathway`; `nwgmc_stage`
- Recommended next use: `cite_if_explaining_why_live_proto_ends_in_*ō_but_trace_passes_through_*u`
- Shared with row IDs:

This is the clearest current DEV_NOTES statement for the row's first nontrivial step. DEV_NOTES says PGmc word-final bimoraic `*-ō` became PNWGmc `*-u`, quotes Ringe–Taylor on that development, and states that the FST models it as `NWGmcFinalLongORaising: {*ō} → {*u} || _ .#.` [Germanic/docs/DEV_NOTES.md:2711-2720]. For row 2187 that is exactly the live first stage: the stored input remains `*skūrō`, but the derivation immediately passes through `*skūru` before any OE-only rule applies [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28448-28457].

The fragment is shared rather than row-local, but it is genuinely current and does real explanatory work here. Without it, later prose could flatten the row into a misleading pseudo-rule like “final `ō` just disappears,” whereas the live cascade demonstrably routes the noun through intermediate `*-u`, which is then lost only at the OE apocope stage [Germanic/docs/DEV_NOTES.md:2711-2720; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4191-4197].

### DEV_NOTES:line-18624-18657

- Source heading: `§15.1: Two Distinct Stages of High Vowel Apocope`
- Source line or section hint: `lines 18624-18657`
- Fragment type: `shared_chronology_background`
- Status: `current_background`
- Issue tags: `high_vowel_apocope`; `late_oe_loss`; `heavy_syllable`; `chronology`
- Recommended next use: `cite_if_explaining_why_final_*u_is_deleted_in_oe_not_in_pgwmc`
- Shared with row IDs:

This fragment is not about `shower` by name, but it preserves the project's clearest general statement that high-vowel apocope had two stages and that the later OE-stage process operated after stressed heavy syllables [Germanic/docs/DEV_NOTES.md:18624-18657]. That is the right background classification for row 2187, because once `*skūrō` has become `*skūru`, the trace deletes the final `*u` only at the OE stage and only after the heavy long-vowel stem has already been established [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28490-28536].

The fragment matters because it keeps two different losses from being collapsed. The row does not go directly from PGmc `*skūrō` to OE `sċūr` by one undifferentiated final-vowel deletion. DEV_NOTES instead supports the chronological split `*-ō > *-u` first, then late apocope of that high vowel under OE conditions [Germanic/docs/DEV_NOTES.md:18624-18657; Germanic/docs/DEV_NOTES.md:2711-2720].

### DEV_NOTES:line-2987-2993

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line or section hint: `lines 2987-2993`
- Fragment type: `diagnostic_but_reusable`
- Status: `diagnostic_only`
- Issue tags: `orthography`; `sk_shift`; `normalized_sċ`; `source_spelling_vs_project_spelling`
- Recommended next use: `cite_for_notation_clarity_only`
- Shared with row IDs: `2186`; `2317`; `2318`

This fragment is stale as row diagnosis for the show-family material it originally discussed, but one sentence remains directly useful here: DEV_NOTES says that the `sk → sc` change is “not palatalization but a general OE shift of /sk/ → /ʃ/ spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. For row 2187, that is the cleanest in-repo statement explaining why reference works can write `scur/scúr` while the dataset writes normalized `sċūr`.

The rest of the fragment should not be imported as if it were a shower-specific argument. Its original context is an older `show` debugging problem, not a `shower` dossier [Germanic/docs/DEV_NOTES.md:2987-2993]. But the orthography warning is still worth carrying over because without it the row's exact-match trace could be misread as though dotted `sċ` were itself an attested manuscript spelling contrast rather than the project's editorial normalization of an OE `/ʃ/` outcome.

### DEV_NOTES:line-34538-34653

- Source heading: `Apocope (Campbell §§356-357; FST line 2644, OEHighVowelApocope)`
- Source line or section hint: `lines 34538-34653`
- Fragment type: `current_shared_rule_body`
- Status: `current`
- Issue tags: `oe_high_vowel_apocope`; `rule_body`; `final_*u_loss`; `heavy_stem_condition`
- Recommended next use: `cite_if_a_later_report_needs_the_actual_FST_clause`
- Shared with row IDs:

This fragment sits inside another lexeme analysis, but it preserves the actual current rule body for `OEHighVowelApocope`, including the clause `{*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.` [Germanic/docs/DEV_NOTES.md:34538-34653]. That is directly relevant to row 2187 because after `NWGmcFinalLongORaising` and `OESkPalatalization`, the live row reaches exactly the kind of heavy-stem `*ʃūru` environment from which the final short `*u` is then deleted [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28490-28536].

This is better treated as rule-body evidence than as row-specific prose. It should not be cited as though `shower` had its own DEV_NOTES case study here. But for later final reporting it is valuable because it gives the exact transducer clause that the trace for `sċūr` is visibly instantiating [Germanic/docs/DEV_NOTES.md:34647-34649; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4191-4197].

## Superseded or diagnostic material

- The January 2026 `liquid_lowering_trace_summary_2026-01-27.txt` records `*skūrō ... Surface [carry] sċūroː` [Germanic/docs/debug_snapshots/liquid_lowering_trace_summary_2026-01-27.txt:27-27]. For this row that file is purely diagnostic history. It predates the current full OE derivation trace and still shows the form before the later final-`ō > u` plus OE apocope pathway is carried through to surface `sċūr` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28423-28536].
- The source-spelling layer is also diagnostic if treated incautiously. Bright's `scur`, Orel's `scúr`, and the compound evidence `rezn-scúr` are all useful for lexeme identification, but they are not reasons to replace the normalized dataset target `sċūr` or to posit multiple OE row targets [docs/references/bright_anglo_saxon_reader.txt:24631-24631; docs/references/orel_handbook_germanic_etymology.vision.txt:33699-33701,38722-38728; Germanic/data/germanic-aligned-final.tsv:996-996].
- The most important negative fact is that no securely attachable shower-specific DEV_NOTES problem narrative survives. Later writeups should not invent one out of shared rule prose merely to make the row sound more dramatic than it is. On current evidence, the row is regular, exact-match, and thinly documented rather than controversial [Germanic/data/germanic-aligned-final.tsv:996-996; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4184-4198].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is reconsidered later, the safest present judgment is to keep row `2187` as a no-index slice unless a genuinely row-specific DEV_NOTES section, packet, or memo is added. The current dossier is usable, but nearly all of its DEV_NOTES anchors are shared rule material rather than shower-specific notes.
- Any later report should keep four layers explicit near the top: live row `PROTO = PROTOFORM = *skūrō`; dictionary stem notation such as Kroonen's `*skūra/ō-`; source-side OE spellings such as `scur/scúr`; and project-normalized OE target `sċūr` [Germanic/data/germanic-aligned-final.tsv:996-996; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23312-23327; docs/references/bright_anglo_saxon_reader.txt:24631-24631; docs/references/orel_handbook_germanic_etymology.vision.txt:38722-38728].
- If a later philological cleanup wants an illustrative citation, the local reference files already provide enough to note the lexeme and one compound (`rezn-scúr`) without reopening the derivation itself [docs/references/orel_handbook_germanic_etymology.vision.txt:33699-33701,38722-38728].
- If future rule work changes `NWGmcFinalLongORaising`, `OESkPalatalization`, or `OEHighVowelApocope`, row 2187 is a useful control case to recheck, because the live successful derivation depends almost entirely on those shared baseline rules and on little else [Germanic/docs/DEV_NOTES.md:2711-2720,34538-34653; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28448-28536].
