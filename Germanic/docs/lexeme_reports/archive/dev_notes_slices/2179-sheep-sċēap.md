---
row_id: 2179
concept: sheep
counterpart: sċēap
proto: *skḗpą
protoform: *skḗpą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2179 sheep / sċēap

## Current row state

- The live OE row currently reads `CONCEPT = sheep`, `COUNTERPART = sċēap`, `PROTO = *skḗpą`, `PROTOFORM = *skḗpą`, `DERIVATION_CLASS = regular`, with row note `R/T vol.2 12522: PWGmc *skap > OE scéap (WS)` [Germanic/data/germanic-aligned-final.tsv:966-966].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not currently using a separate OE-facing proxy input, a paradigm-cell retarget, or a substitute handbook stage as its derivational feed. The live stored input is the stressed PGmc-tier form `*skḗpą`; the attested OE target is `sċēap` [Germanic/data/germanic-aligned-final.tsv:966-966].
- The row note's `PWGmc *skap > OE scéap (WS)` is not a competing TSV protoform. It is a compressed handbook statement that starts from a later West Germanic stage and cites the OE outcome in traditional accent notation `scéap`; the live row instead stores the earlier comparative/project input `*skḗpą` and derives `sċēap` through the full cascade [Germanic/data/germanic-aligned-final.tsv:966-966; docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523].
- `oe_known_problems.tsv` has no surviving entry for row `2179`, for `sheep`, for `sċēap`, or for `*skḗpą`, so the row is not currently being tracked as a live OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still shows this row as uncovered documentation rather than as a resolved packet/dossier case: `coverage_audit.md` lists `2179 | sheep | sċēap | regular | yes | - | - | - | NOTE` [Germanic/docs/lexeme_reports/coverage_audit.md:129-129].
- The current published derivation trace is an exact match and makes the live stage sequence explicit: `*skḗpą > *skǣpą > *skǣp > *ʃǣp > *ʃēap > sċēap`, labelled respectively by `NWGmcLongELowering`, `OEHeavySyllableNasalApocope`, `OESkPalatalization`, and `OEWsPalatalDiphthongization`, with `OEIUmlaut [no-change]` in between [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4058-4078; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27495-27609].
- Local reference files support both the lexical identification and the West-Saxon-style vocalism. Ringe–Taylor explicitly give `PWGmnc *skap 'sheep' ... > WS OE scéap (Merc., Kent. scép)`; Campbell lists `sééap sheep` under the `éa` outcomes after palatals and separately notes dialectal `scip sheep`, presumably from `*sciep`; Clark Hall gives `scēap (æ, ē, i) n. 'sheep'`; Orel cites `*skēpan sb.n.: OE sceáp 'sheep', OFris skep, OS skāp, OHG scāf` [docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523; docs/references/campbell_old_english_grammar.txt:5188-5192,5236-5237; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:34698-34698; docs/references/orel_handbook_germanic_etymology.vision.txt:37891-37898].

## Development-note summary

No securely attachable, row-dedicated DEV_NOTES dossier survives for `2179 sheep / sċēap`. That has to be said plainly at the top, because the slice cannot honestly pretend that `DEV_NOTES.md` contains a `sheep` section comparable to rows like `2178 sheath / sċēaþ`. The present row dossier is therefore built from three things: live row metadata, live published derivation traces, and shared DEV_NOTES policy sections that explain the notation and sound-change machinery now producing the exact-match output `sċēap` [Germanic/data/germanic-aligned-final.tsv:966-966; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4058-4078; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27495-27609]. That is enough for a replacement working note, but it is not the same evidentiary quality as a row-local DEV_NOTES analysis, and that difference is the main reason to keep this as a no-index slice for now.

The notation layers must be kept explicit. In the live row, both **PROTO** and **PROTOFORM** are `*skḗpą`, the stressed PGmc-tier input now used by the project; the attested OE target is `sċēap` [Germanic/data/germanic-aligned-final.tsv:966-966]. The row note, however, cites Ringe–Taylor's later-stage formulation `PWGmc *skap > OE scéap (WS)` [Germanic/data/germanic-aligned-final.tsv:966-966; docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523]. Those are not rival guesses about one single layer. `*skḗpą` is the project's live comparative-and-derivational input; `*skap` is a handbook West Germanic stage after long-ē lowering and fronting are no longer being written in the same way; `scéap` is a handbook spelling of the OE outcome; and `sċēap` is the row's normalized OE target spelling in the dataset [Germanic/data/germanic-aligned-final.tsv:966-966; docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:34698-34698]. The acute on `*skḗpą` is not a different etymon from older `*skēpą`; it reflects the later project stress-tier convention for stressed long `ē`, whereas the handbook note's `*skap` is a genuinely later chronological stage.

The live trace clarifies the actual derivation now in force. First, `NWGmcLongELowering` changes stressed `*ḗ` to `*ǣ`, giving `*skǣpą`; then `OEHeavySyllableNasalApocope` removes final nasalized `*ą`, giving `*skǣp`; then `OESkPalatalization` yields initial `*ʃ`, producing `*ʃǣp`; `OEIUmlaut` does nothing; and `OEWsPalatalDiphthongization` finally converts `*ǣ` to `*ēa` after the initial palatal, giving `*ʃēap`, orthographic `sċēap` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27532-27568,27604-27609]. This is important because the row note `*skap > scéap` compresses away exactly the steps that matter for project policy: the row does not begin life in the grammar as `*skap`, and its `ēa` is not inserted ad hoc. It is the output of the current ordered cascade from `*skḗpą` through `*ǣ` and then through West Saxon palatal diphthongization [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4065-4078; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27532-27568].

The row also needs a clear statement about what does **not** happen. Unlike `sċēaþ`, which required a row-specific DEV_NOTES defense of i-umlaut ordering, `sċēap` shows no umlaut-triggering suffixal environment in the live trace and no `OEIUmlaut` change at all [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27562-27568]. Shared DEV_NOTES chronology on West Saxon palatal diphthongization versus i-umlaut still matters here, but as background classification rather than as a sheep-specific repair story: `sċēap` belongs with forms where a front vowel remains available for diphthongization after palatalization, not with forms where i-umlaut first removes the relevant target vowel [Germanic/docs/DEV_NOTES.md:11309-11329; docs/references/campbell_old_english_grammar.txt:5188-5192].

Philological sources support that classification. Ringe–Taylor's handbook line is already West-Saxon-specific and explicitly contrasts `WS OE scéap` with `Merc., Kent. scép`, which matches the row's use of the West-Saxonized diphthongal target rather than a non-WS monophthongal spelling [docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523]. Campbell likewise lists `sééap sheep` among `éa` outcomes after palatals and then notes other dialect material with `scip sheep`, “presumably from *sciep,” again showing that different textual spellings belong to dialectal/orthographic history, not to a disagreement about the row's selected West-Saxon outcome [docs/references/campbell_old_english_grammar.txt:5188-5192,5236-5237]. Clark Hall's `scēap (æ, ē, i)` confirms orthographic variation around the same lexeme, while Orel's normalized `OE sceáp` confirms the underlying lexeme and the long-vowel base [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:34698-34698; docs/references/orel_handbook_germanic_etymology.vision.txt:37891-37898]. The conservative current reading is therefore: the live row is behaving regularly and transparently, but the surviving DEV_NOTES evidence is shared and policy-level, not row-dedicated.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42679-42728

- Source heading: `§17.49 Stressed long-ē tier (*ḗ) — extending the §17.46 stress-tier convention`
- Source line or section hint: `lines 42679-42728`
- fragment_type: `project_policy_relevant_to_lexeme`
- current_status: `current`
- Issue tags: `proto_notation`; `stress_tier`; `nwgmc_long_e_lowering`; `proto_vs_stage_form`
- recommended_next_use: `cite_if_proto_notation_needs_explanation`
- Shared with row IDs:

This is the most important surviving DEV_NOTES fragment for explaining why the live row stores `*skḗpą` rather than older plain-`ē` spellings. DEV_NOTES says the April 2026 `*ḗ` refactor “landed cleanly,” explains that stressed long `ē` now has its own project symbol, and states that `NWGmcLongELowering` was explicitly extended so `{*ḗ} -> {*ǣ}` in the live cascade [Germanic/docs/DEV_NOTES.md:1447-1449,42679-42728]. For row `2179`, that means the acute-bearing `*skḗpą` is current notation policy, not an alternate etymology; the row note's `*skap` remains a later handbook stage, while the live project input is a stress-tier PGmc form designed to feed the exact lowering step now visible in the trace [Germanic/data/germanic-aligned-final.tsv:966-966; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27532-27533].

### DEV_NOTES:line-11171-11200

- Source heading: `I-Umlaut / WS Palatal Diphthongization Chronology (2026-03-17)`
- Source line or section hint: `lines 11171-11200`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `ws_palatal_diphthongization`; `palatal_trigger`; `ǣ_to_ēa`; `shared_chronology`
- recommended_next_use: `keep_as_shared_background_only`
- Shared with row IDs: `2178`

This fragment is not about `sheep` by name, but it preserves a direct current DEV_NOTES statement of the exact last vocalic step that row `2179` uses: West Saxon palatal diphthongization converts `ǣ` to `ēa` after an initial palatal [Germanic/docs/DEV_NOTES.md:11186-11200]. The lexeme-specific discussion there concerns `sċēaþ`, where umlaut had to feed that result; row `2179` does **not** inherit the umlaut argument. What it does inherit is the explicit rule statement that once the row has reached `*ʃǣp`, the West Saxon reflex should be `*ʃēap`, exactly as the live sheep trace now shows [Germanic/docs/DEV_NOTES.md:11186-11200; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27562-27568]. Because the fragment is shared rather than row-dedicated, it is useful dossier material but weak index evidence on its own.

### DEV_NOTES:line-11309-11329

- Source heading: `Background: WS palatal diphthongization vs i-umlaut`
- Source line or section hint: `lines 11309-11329`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `with_vs_without_i_umlaut_trigger`; `palatal_diphthongization`; `no_umlaut_change`; `shared_background`
- recommended_next_use: `keep_as_shared_background_only`
- Shared with row IDs:

This fragment gives the cleanest current DEV_NOTES prose for classifying why `sċēap` is straightforward in the live grammar even though no sheep-specific DEV_NOTES section survives. DEV_NOTES contrasts forms without an i-umlaut trigger, where a front vowel remains available for West Saxon palatal diphthongization, against forms with an i-umlaut trigger, where the relevant vowel changes first and the diphthongization rule no longer applies [Germanic/docs/DEV_NOTES.md:11309-11329]. Row `2179` falls in the former class in practical terms: the live trace has `OEIUmlaut [no-change]` and then `OEWsPalatalDiphthongization: *ʃēap` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27566-27568]. That makes this fragment good explanatory background, but again it is not row-local enough to justify confident index integration by itself.

## Superseded or diagnostic material

- The older March 2026 full trace writes the input as `PROTO: *skēpą` rather than live `*skḗpą`, but the actual derivational logic and output are already the same there: `NWGmcLongELowering: *ʃǣpą`, `WsPalatalDiphthongization: *ʃēapą`, surface `sċēap` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:11168-11221]. After the later `*ḗ` stress-tier refactor, that older trace should be treated as superseded notation history, not as evidence for a different current row policy [Germanic/docs/DEV_NOTES.md:1447-1449,42679-42728].
- The live TSV row note `R/T vol.2 12522: PWGmc *skap > OE scéap (WS)` is still philologically useful, but only as an indirect handbook compression of the derivation. It should not be promoted into row-metadata identity, because the live grammar demonstrably starts from `*skḗpą`, not from stored `*skap`, and the project now distinguishes those notation layers intentionally [Germanic/data/germanic-aligned-final.tsv:966-966; docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27503-27568].
- The absence of any sheep-specific mismatch note is itself diagnostically important. The row does not appear in `oe_known_problems.tsv`, does not appear in current mismatch reports, and currently matches exactly in both the compact/published trace infrastructure and the full trace [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4058-4078; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27495-27609]. That means the present need is documentation of notation and stage distinctions, not repair of a live derivation failure.

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, the safest present judgment is to keep row `2179` as a no-index slice unless a genuinely row-specific DEV_NOTES section, packet, or memo is added. The current dossier is usable, but its DEV_NOTES anchors are shared project-policy fragments rather than sheep-specific notes.
- If a later packet or final report is written, keep four layers explicit near the top: live TSV `PROTO = PROTOFORM = *skḗpą`; older pre-§17.49 project notation `*skēpą`; handbook later-stage `PWGmc *skap`; and attested OE target `sċēap` / handbook `scéap` [Germanic/data/germanic-aligned-final.tsv:966-966; docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:11168-11221; Germanic/docs/DEV_NOTES.md:42679-42728].
- If later review wants a one-sentence dialect note, it should say plainly that this row intentionally keeps the West-Saxon diphthongized target `sċēap`, while handbook and dictionary sources also preserve non-identical spellings such as `scép`, `scip`, and orthographic variation summarized by Clark Hall's `scēap (æ, ē, i)` [docs/references/ringe_taylor_linguistic_history_vol2.txt:12522-12523; docs/references/campbell_old_english_grammar.txt:5236-5237; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:34698-34698].
