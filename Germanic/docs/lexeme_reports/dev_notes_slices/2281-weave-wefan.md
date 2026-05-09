---
row_id: 2281
concept: weave
counterpart: wefan
proto: *wébaną
protoform: *wébaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2281 weave / wefan

## Current row state

- CONCEPT: `weave`; COUNTERPART: `wefan`; PROTO: `*wébaną`; PROTOFORM: `*wébaną`; DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1363-1363].
- The row's live source note is extremely thin and duplicative: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1363-1363]. This slice therefore has to carry most of the durable philological explanation itself.
- No row-specific packet, research memo, or pilot file was located, and the coverage audit likewise marks row `2281` as having no linked support material (`none`) [Germanic/docs/lexeme_reports/coverage_audit.md:407-407].
- The current debug trace is uncomplicated and already matches the TSV row exactly: `PROTO: *wébaną`, `EXPECTED: wefan`, `OUTPUTS: wefan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5741-5760].
- That trace also makes the internal project derivation explicit: `*wébaną` passes through `OE Heavy Syllable Nasal Apocope: *wéban`, `OE Secondary Nasalization: *wébąn`, `PGmc B Allophony: *wéβąn`, and `OE Weak Tail Reduction: *wéβan` before surfacing as `wefan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5748-5760]. Even for a regular row, that staging matters because it explains why the project input keeps final `*ą` while the Old English output is plain `-an`.

## Development-note summary

This row is best treated as a **regular West-Saxon infinitive row with very little dedicated DEV_NOTES prose**. The live TSV already points to the correct normalized Old English target `wefan`, and the current derivation trace reaches that target without any repair rule, exception note, or paradigm-cell substitution [Germanic/data/germanic-aligned-final.tsv:1363-1363; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5741-5760]. Future work should therefore resist inventing a mismatch narrative merely because the surrounding documentation is sparse. The evidence presently available supports the conservative reading: row `2281` is a straightforward inherited strong verb.

The most important thing to preserve is the distinction among the row's three lexical layers. `COUNTERPART` is the attested Old English infinitive lemma `wefan` [Germanic/data/germanic-aligned-final.tsv:1363-1363; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47551-47552]. `PROTO` is the dataset's comparative/project label `*wébaną`, and `PROTOFORM` is the same string because this row currently needs no separate OE-facing surrogate or repaired input [Germanic/data/germanic-aligned-final.tsv:1363-1363]. That does **not** mean outside reference works use the same notation. Kroonen cites the comparative headword as `*weban-` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29219-29225; @Kroonen2013, s.v. *weban-], Orel uses `*webanan` [docs/references/orel_handbook_germanic_etymology.vision.txt:49737-49743; @Orel2003, s.v. *webanan], and Ringe-Taylor discuss `PGmc *webana 'to weave' ... > Merc. weofan (WS wefan)` [docs/references/ringe_taylor_linguistic_history_vol2.txt:18613-18614; @RingeTaylor2014]. Those dictionary headwords are source-faithful comparative labels, but they should not be collapsed into the row's own encoded `PROTOFORM = *wébaną`, whose final `*ą` is part of the project's morphophonological input convention.

The thin but still relevant DEV_NOTES material is not lexeme-specific; it is **shared infinitive machinery**. DEV_NOTES explicitly says that the TSV distinguishes infinitives from non-infinitival forms by using final `*ą`: “Infinitive uses `*ą` (nasalized vowel marking word-final coda nasal)” while participial material uses `*ă + *z` [Germanic/docs/DEV_NOTES.md:10546-10548]. A later explanatory note gives the phonological logic behind that encoding by quoting Ringe-Taylor: “unstressed *a was apparently nasalized when immediately followed by a nasal in the syllable coda, but not when immediately followed by an intervocalic nasal,” illustrated there with infinitive `*bind.an#` versus participle `*bind.an.az` [Germanic/docs/DEV_NOTES.md:25128-25140]. Row `2281` belongs squarely in that same infinitive class. In other words, the row's final `*ą` is not a stray orthographic flourish; it is the project's way of encoding the infinitive environment that ultimately yields OE `-an`.

The debug trace confirms that this general doctrine is what the live system is actually using for `wefan`. The row does not merely jump from `*wébaną` to `wefan`; it passes through an apocope/nasalization/lenition/weak-tail sequence that is fully compatible with the project-wide infinitive analysis [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5748-5760]. The step labeled `PGmc B Allophony: *wéβąn` is especially worth preserving in prose because it explains why comparative `*web-` corresponds to Old English `-f-` at the surface. Orel's direct wording already matches this lexeme cluster: “`*webanan str.vb.: ON vefa ‘to weave', OE wefan id., MLG weven id., OHG weban id.`” [docs/references/orel_handbook_germanic_etymology.vision.txt:49737-49738; @Orel2003, s.v. *webanan]. The row is therefore regular both in its vocalism and in its medial consonant development.

Old English philology adds one further point that should stay attached to the row even though DEV_NOTES does not spell it out specifically for `wefan`: the dataset is targeting the normalized West-Saxon infinitive, not every dialectal or paradigm variant. Clark Hall's headword is `wefan³ (eo) (±) to 'weave,' ... devise, contrive, arrange`, with a separate cross-reference `weofan (VPs) = wefan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47551-47552,47771-47771; @ClarkHall1960, s.v. wefan]. Ringe-Taylor make the same dialect split explicit from the historical side: `Merc. weofan (WS wefan)` [docs/references/ringe_taylor_linguistic_history_vol2.txt:18613-18614; @RingeTaylor2014]. Campbell's verb inventory likewise lists `wefan weave` among the expected strong-verb comparanda [docs/references/campbell_old_english_grammar.txt:21056-21057; @Campbell1959, §743]. The slice should therefore preserve `weofan` as comparative/background evidence, but not let it displace `COUNTERPART = wefan`.

Because DEV_NOTES support is so thin, the safest replacement note is intentionally conservative. There is no surviving dedicated row-2281 mismatch dossier, no project dispute over the correct counterpart, and no sign that `PROTOFORM` needs retargeting. The file's real value is to record that the row is regular **for identifiable reasons**: comparative sources support the lexeme, the debug trace already closes the derivation, and the only relevant DEV_NOTES anchors are shared infinitive-encoding notes rather than lexeme-specific policy text [Germanic/docs/DEV_NOTES.md:10546-10548,25128-25140; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5741-5760].

## Relevant DEV_NOTES fragments

No securely attachable dedicated row-2281 mini-dossier was located in `DEV_NOTES.md`. What survives is shared machinery that still matters for the row because the trace and the TSV encoding depend on it.

### DEV_NOTES:line-10546-10548

- Source heading: `Key encoding decision`
- Source line or section hint: `lines 10546-10548`
- Fragment type: `shared_infinitive_encoding_rule`
- Status: `current`
- Issue tags: `protoform_encoding`; `infinitive_marker`; `proto_vs_counterpart`; `shared_doctrine`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: many `*-aną` infinitive rows, including `2281`

This is the cleanest DEV_NOTES anchor for explaining why the live row uses `PROTO = PROTOFORM = *wébaną` instead of a dictionary-style headword such as `*weban-`. DEV_NOTES states: “Infinitive uses `*ą` (nasalized vowel marking word-final coda nasal)” and contrasts this with participial encoding `*ă + *z` [Germanic/docs/DEV_NOTES.md:10546-10548]. For row `2281`, that means the final nasalized vowel in `*wébaną` is an intentional project encoding choice, not an accidental mismatch with Kroonen's `*weban-`, Orel's `*webanan`, or Ringe-Taylor's `*webana`. This fragment is therefore the best current project-language support for keeping the row's proto columns exactly as they stand while still distinguishing them sharply from the Old English `COUNTERPART = wefan`.

### DEV_NOTES:line-25128-25140

- Source heading: `R/T vol.2 §5.1.2 p.142`
- Source line or section hint: `lines 25128-25140`
- Fragment type: `shared_infinitive_phonology`
- Status: `current`
- Issue tags: `coda_nasal`; `secondary_nasalization`; `infinitive_suffix`; `shared_doctrine`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: broad class of infinitive rows in `*-aną`

This fragment gives the phonological rationale behind the encoding just noted. DEV_NOTES quotes Ringe-Taylor that “unstressed *a was apparently nasalized when immediately followed by a nasal in the syllable coda, but not when immediately followed by an intervocalic nasal,” then illustrates the contrast with infinitive `*bind.an#` versus participle `*bind.an.az` [Germanic/docs/DEV_NOTES.md:25128-25140]. Although `wefan` is not named there, the same logic is directly applicable to row `2281`: the infinitive ending in `*wébaną` belongs to the coda-nasal class that yields OE `-an`, not to the fronted participial `-en` class. This is the strongest current DEV_NOTES fragment for explaining why the row's morphophonological input is an infinitive-specific form rather than a generic comparative headword.

### DEV_NOTES:line-1591-1612

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1612`
- Fragment type: `archived_rule_history`
- Status: `archived_diagnostic`
- Issue tags: `apocope`; `heavy_stem`; `trace_alignment`; `project_history`
- Recommended next use: `project_history_only`
- Shared with row IDs: many heavy-stem rows; potentially relevant to `2281`

This section is explicitly archived and should not be mistaken for a row-specific policy note, but it still deserves preservation because the live debug trace for `wefan` contains the stage label `OE Heavy Syllable Nasal Apocope` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5754-5754]. DEV_NOTES here records the broader project claim that heavy/light conditioning was extended to final `*-ą`, despite limited explicit handbook coverage [Germanic/docs/DEV_NOTES.md:1591-1612]. Since `*wébaną` has a heavy root syllable, this archived rule history is a plausible explanation for the trace stage `*wébaną → *wéban`. It is useful as diagnostic/project history, but too general and too archived to serve as a strong row-2281 indexing anchor by itself.

## Superseded or diagnostic material

- No superseded row-specific weave dossier was located. The main hazard here is not stale lexeme-specific analysis but false confidence created by generic infinitive notes.
- Comparative headwords `*weban-`, `*webanan`, and `*webana` should be kept, but only as comparative labels. They are not grounds for rewriting the live row's `PROTOFORM = *wébaną`, because the project encodes infinitive morphology differently from lexicographic headword practice [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29219-29225; docs/references/orel_handbook_germanic_etymology.vision.txt:49737-49743; docs/references/ringe_taylor_linguistic_history_vol2.txt:18613-18614].
- `weofan` is real evidence, but only as dialect/background evidence. Clark Hall and Ringe-Taylor both preserve it as a Mercian or variant form beside West-Saxon `wefan`; it should not be promoted into the row target unless the dataset is explicitly retargeted away from normalized West Saxon [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47551-47552,47771-47771; docs/references/ringe_taylor_linguistic_history_vol2.txt:18613-18614].
- Clark Hall's preterite forms `wæf` and `wafon` are useful only as paradigm background, reminding later editors not to collapse infinitive `wefan` into another verbal cell [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46454-46454,46504-46504].

## Open questions for later work

- If row `2281` is ever promoted into a full lexeme report, decide whether the top-line comparative label should foreground Kroonen's `*weban-`, Orel's `*webanan`, or the live project input `*wébaną`; at present the safest answer is to keep all three visible but functionally distinct.
- If indexability is revisited, treat expectations modestly. The row has usable DEV_NOTES anchors for shared infinitive encoding (`line-10546-10548`) and shared infinitive phonology (`line-25128-25140`), but no dedicated weave-only DEV_NOTES narrative.
- If later dialect coverage is expanded, note explicitly whether Mercian `weofan` deserves a linked cross-row discussion with other `eo ~ e` alternants; nothing in the current row state requires such a move, but the evidence is there [docs/references/ringe_taylor_linguistic_history_vol2.txt:18613-18614; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47771-47771].
