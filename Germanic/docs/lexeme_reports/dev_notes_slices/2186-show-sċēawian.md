---
row_id: 2186
concept: show
counterpart: sċēawian
proto: *skáwōjaną
protoform: *skáwōjaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2186-show-sċēawian.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2186-show-sċēawian.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2186 show / sċēawian

## Current row state

- The live OE row reads `CONCEPT = show`, `COUNTERPART = sċēawian`, `PROTO = *skáwōjaną`, `PROTOFORM = *skáwōjaną`, `DERIVATION_CLASS = regular`, with row note `Normalized sċ: initial sc always [ʃ] in OE (Campbell §440)` [Germanic/data/germanic-aligned-final.tsv:993-993].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not using an oblique-cell surrogate, an OE-only substitute stem, or a split between cognate-set label and OE-facing modelling input. The live derivational feed is the same `*skáwōjaną` that labels the row [Germanic/data/germanic-aligned-final.tsv:993-993].
- The current published derivation trace is an exact match: `*skáwōjaną > *skḗawōjaną > *skḗawōjan > *skḗawōjąn > *ʃḗawōjąn > *ʃḗawējąn > *ʃḗawejąn > *ʃḗawejan > *ʃḗaweian > *ʃḗawian > sċēawian`, with the labelled steps `OE Aw Long Diphthong`, `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `OE Sk Palatalization`, `OE I Umlaut`, `OE Unstressed Long Vowel Shortening`, `OE Weak Tail Reduction`, `OE Intervocalic J Vocalization`, and `OE Unstressed EI Contraction` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4163-4183; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28307-28420].
- `oe_known_problems.tsv` has no surviving entry for row `2186`, for `show`, for `sċēawian`, or for `*skáwōjaną`, so the row is not currently managed as a live OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still lists the row as a note-bearing regular OE item with no integrated report path: `2186 | show | sċēawian | regular | yes | - | - | - | NOTE` [Germanic/docs/lexeme_reports/coverage_audit.md:133-133].

## Development-note summary

No dedicated row-length DEV_NOTES dossier survives for `show / sċēawian`. The usable evidence is instead a mixture of (i) one current shared rule note on `*aw > ēaw` before a following vowel, (ii) one current shared safety sweep stating explicitly that row `2186` is fine because Class II `*-ōjan-` puts `*ō` between `*w` and `*j`, and (iii) older show-family debugging notes that are now only project history [Germanic/docs/DEV_NOTES.md:3628-3649,26631-26632,26680-26681,2821-2834,2987-2993]. That is enough for a replacement working note, but it is materially thinner than rows that still preserve a row-specific DEV_NOTES argument copied from primary or secondary sources. That thinness is the main reason this slice should presently remain no-index.

The notation layers must be kept separate. The live row stores `PROTO = PROTOFORM = *skáwōjaną` [Germanic/data/germanic-aligned-final.tsv:993-993]. Older DEV_NOTES tables instead write `*skawōjăną`, with different accenting and the older short-vowel breve on the suffixal `ă`; in context that is only an older house-notation spelling of the same lemma input, not a different chronological stage and not a different row policy [Germanic/docs/DEV_NOTES.md:2821-2829,3647-3649]. By contrast, the trace form `*skḗawōjaną` is a genuine chronological stage inside the current derivation, created by `OE Aw Long Diphthong`, not an alternate stored protoform [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4172-4183; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28352-28358]. And source-spelled `scēawian` versus project-normalized `sċēawian` is an orthographic/editorial distinction rather than a separate lexical target [Germanic/data/germanic-aligned-final.tsv:993-993; docs/references/bright_anglo_saxon_reader.vision.txt:24606-24612].

The current live derivation is explicit enough that the row should not be described vaguely as “regular” without stating how it works. First, `OE Aw Long Diphthong` changes `*aw` to `*ḗaw` before a following vowel, so `*skáwōjaną` becomes `*skḗawōjaną` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28352-28358]. Then final nasalized `*ą` is removed after the heavy stem, secondary nasalization reassigns nasality to the preceding vowel sequence, initial `*sk` shifts to `*ʃ`, suffixal `*ō` is fronted by `OE I Umlaut` to `*ē`, that unstressed long vowel shortens to `*e`, the weak tail reduces to `-jan`, `j` vocalizes intervocalically to `i`, and unstressed `ei` contracts to `i`, yielding `*ʃḗawian`, orthographic `sċēawian` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28370-28420]. The compact trace shows the same ordered chain in summary form [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4176-4183].

The most important analytical distinction preserved in later DEV_NOTES is that row `2186` is **not** one of the troublesome true `*aw+j` cases. The shared safety sweep says this outright: `2186 *skáwōjaną sċēawian sċēawian ✓ Class II *-ōjan-: *ō intervenes between *w and *j`, and the regression table repeats that `*skáwōjaną (row 2186)` is low-risk because `*ō between *w and *j blocks rule` [Germanic/docs/DEV_NOTES.md:26631-26632,26680-26681]. That distinction matters because the same DEV_NOTES section is mainly about real `*aw+j` items such as `hew` and `strew`, where `j` sits directly after the `aw` sequence and feeds the separate `ēġ/-g-` problem space [Germanic/docs/DEV_NOTES.md:26592-26610,26653-26667]. For row `2186`, the Class II suffix keeps the lemma outside that bucket.

Philological source support is consistent with the live row, but it mostly supports the lemma and stem shape rather than a special row-specific controversy. Orel reconstructs `*skawōjanan` and cites `OE sceáwian 'to look, to observe'`; Kroonen likewise gives `OE scēawian ... < *skawōjan-`; Bright lists `scēawian (W. II.)` and also the related imperative `scēawa`; Brunner lists `scēawian, scāwian (scēawiza)` and separately notes preterite material `scēawde (scēaude, scēode)` [docs/references/orel_handbook_germanic_etymology.vision.txt:37608-37612; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22888-22890; docs/references/bright_anglo_saxon_reader.vision.txt:24606-24612; docs/references/brunner_1965_altenglische_grammatik.vision.txt:27306-27310,17795-17796]. These are useful because they show that the surviving source-side lemma is `scēawian` and that `scāwian` is a recorded source-side variant, but they do not amount to a dedicated in-repo DEV_NOTES lexeme audit.

The row note on `sċ` must also be read as editorial normalization, not as a claim that the attested sources literally write the dotted character. Campbell's local OCR states that “every initial sc and sé became [ʃ]” in OE, though the symbol is OCR-corrupted in the file; Hogg says the sound from earlier `*/sk/` was normally written `<sc>` and that editors often distinguish it by dotting; Fulk likewise says PGmc `*sk` is ordinarily palatal in OE outside the narrow medial-back-vowel environment [docs/references/campbell_old_english_grammar.txt:2410-2412; docs/references/hogg_vol1.txt:4610-4615,5271-5286; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:7904-7908]. The row's `sċēawian` is therefore best understood as the project's normalized spelling of source `scēawian`, not as a separate attested form.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3628-3649

- Source heading: `OEAwLongDiphthong: PGmc *aw → OE ēaw before vowels (Campbell §272)`
- Source line or section hint: `lines 3628-3649`
- fragment_type: `mixed_current_rule_and_stale_row_hit`
- current_status: `partly_current`
- Issue tags: `oe_aw_long_diphthong`; `rule_scope`; `source_spelling_vs_normalization`; `show_family`
- recommended_next_use: `cite_for_aw_to_eaw_rule_but_not_as_live_expected_spelling`
- Shared with row IDs: `1989`; `2074`; `2186`; `2317`; `2318`

This is the most useful surviving DEV_NOTES fragment for the row's actual vowel history. The rule statement is current: DEV_NOTES says `*a w -> *ēa w` before a following vowel and places the rule before Anglo-Frisian brightening [Germanic/docs/DEV_NOTES.md:3628-3640]. That is exactly what the live show trace now does when it turns `*skáwōjaną` into `*skḗawōjaną` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28352-28358].

What is stale inside the same fragment is the row-local expectation line `*skawōjăną → sċēawian (expected scēawian)` [Germanic/docs/DEV_NOTES.md:3647-3649]. The older note still assumes manuscript-style `scēawian` as the expected spelling, whereas the live TSV now deliberately normalizes initial `sc-` to `sċ-` [Germanic/data/germanic-aligned-final.tsv:993-993]. The fragment is therefore usable as current evidence for the `*aw > ēaw` rule, but only as superseded history for the exact orthographic expectation.

### DEV_NOTES:line-2987-2993

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line or section hint: `lines 2987-2993`
- fragment_type: `diagnostic_but_reusable`
- current_status: `diagnostic_only`
- Issue tags: `sk_shift`; `orthography`; `normalization`; `family_history`
- recommended_next_use: `cite_for_notation_clarity_only`
- Shared with row IDs: `2175`; `2181`; `2186`; `2317`; `2318`

This fragment is stale as row diagnosis but still valuable for one narrow reason. DEV_NOTES says, “The `sk -> sc` change is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. That sentence remains the cleanest in-repo warning not to collapse phonological `/sk/ > /ʃ/` with editorial dotted-`sċ` normalization.

The rest of the fragment reflects an older broken state: `*skawô → sċawa` and `*skawōθi → sċaweþ` were then missing `ēa`, and `scēawa/scēaweþ` were still written as source-style expectations [Germanic/docs/DEV_NOTES.md:2987-2993]. For row `2186`, only the orthography/terminology distinction remains current.

### DEV_NOTES:line-26631-26632

- Source heading: `§17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology`
- Source line or section hint: `lines 26631-26632`
- fragment_type: `current_shared_safety_check`
- current_status: `current`
- Issue tags: `class_ii_verb`; `aw_plus_w_plus_o_plus_j`; `row_safe`; `protoform_scope`
- recommended_next_use: `cite_if_explaining_why_show_is_not_an_aw_plus_j_problem`
- Shared with row IDs: `2317`; `2318`

This is the clearest current DEV_NOTES statement directly naming row `2186`: `*skáwōjaną        sċēawian       sċēawian        ✓ Class II *-ōjan-: *ō intervenes between *w and *j` [Germanic/docs/DEV_NOTES.md:26631-26632]. Even though it sits inside a wider investigation of other lexemes, its substance is current and exact. It states that row `2186` already behaves correctly and also states why: the show lemma is structurally shielded from the true `*aw+j` problem because the Class II suffix inserts `*ō` between the root glide and the suffixal `*j`.

That makes this fragment more valuable than its brevity might suggest. It is not merely a pass/fail table; it preserves the row policy that later writers need in order to keep `*skáwōjaną` separate from the non-lemma companion cells `*skáwô` and `*skáwōθi`, and separate again from genuine `*aw+j` rows like `hīeġ` and `strēgan` [Germanic/docs/DEV_NOTES.md:26617-26639,26653-26667].

### DEV_NOTES:line-26680-26681

- Source heading: `Regression risk assessment`
- Source line or section hint: `lines 26680-26681`
- fragment_type: `current_shared_risk_note`
- current_status: `current`
- Issue tags: `regression_scope`; `class_ii_verbs`; `w_j_blocking`; `row_stability`
- recommended_next_use: `cite_if_later_rule_changes_touch_aw_plus_j`
- Shared with row IDs: `2317`; `2318`

The companion risk table is brief but worth preserving separately because it translates the same point into maintenance guidance: `Class II verbs  *skáwōjaną (row 2186) — *ō between *w and *j blocks rule` [Germanic/docs/DEV_NOTES.md:26678-26681]. In other words, later fixes aimed at genuine `*aw+j` material should not be expected to alter row `2186`.

That is useful row dossier material because the earlier show-family mismatch notes can otherwise make the row look like part of the `hew/strew` bug cluster. The current risk note says the opposite: the lemma row is now supposed to be boring, and if a future `*aw+j` repair changes it, that would itself look suspicious.

## Superseded or diagnostic material

- The earliest surviving show-specific DEV_NOTES entry is the February Class II weak-verb table `*skawōjăną | sċaweian | scēawian | breaking_missing__ea` [Germanic/docs/DEV_NOTES.md:2821-2834]. This is doubly superseded. First, the output `sċaweian` predates the later `OEAwLongDiphthong` repair; second, the expected form `scēawian` predates the project's current dotted-`sċ` normalization. The older `*skawōjăną` spelling here is best treated as a notation variant of live `*skáwōjaną`, not as a different stage or a different row policy [Germanic/docs/DEV_NOTES.md:2821-2829; Germanic/data/germanic-aligned-final.tsv:993-993].
- The March debugging note `Missing ēa diphthong + sk/sc issue` is likewise superseded as a live problem statement for the lemma family [Germanic/docs/DEV_NOTES.md:2987-2993]. Its reusable part is only the terminological warning about `/sk/ -> /ʃ/` and spelling `<sc>`; the row itself no longer lacks `ēa`, and the orthographic expectation has shifted from source-style `scēawian` to project-normalized `sċēawian` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4163-4183; Germanic/data/germanic-aligned-final.tsv:993-993].
- The mixed rule note at `3647-3649` should also be read carefully. It preserves the history that the vowel problem had already been fixed before the normalization issue was cleaned up, but it is not current row metadata anymore [Germanic/docs/DEV_NOTES.md:3642-3649]. The live row now matches exactly, is absent from `oe_known_problems.tsv`, and is treated in later DEV_NOTES as a low-risk control case rather than as an unresolved mismatch [Germanic/docs/DEV_NOTES.md:26631-26632,26680-26681; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If this row is reconsidered for `dev_notes_slices/index.tsv`, the safest upgrade path would be a fuller row-specific DEV_NOTES section or a compact final report anchored to the current trace and source lemma evidence. At present the surviving DEV_NOTES anchors are real but thin: one current safety check, one current risk note, one mixed rule note, and older debugging history.
- Any later report should keep four layers explicit near the top: live row input `*skáwōjaną`; older DEV_NOTES notation `*skawōjăną` as a notation variant of the same row input; chronological trace stages such as `*skḗawōjaną` and `*ʃḗawian`; and source-spelled `scēawian` versus project-normalized `sċēawian` [Germanic/data/germanic-aligned-final.tsv:993-993; Germanic/docs/DEV_NOTES.md:2821-2829,3647-3649; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28352-28420; docs/references/bright_anglo_saxon_reader.vision.txt:24606-24612].
- If later philological cleanup wants to mention source variation, it should say only that local reference files support `scēawian` and also record `scāwian` as a source-side variant; that is not grounds by itself for changing the row target or multiplying lemma rows [docs/references/brunner_1965_altenglische_grammatik.vision.txt:27306-27310; docs/references/orel_handbook_germanic_etymology.vision.txt:37608-37612].
