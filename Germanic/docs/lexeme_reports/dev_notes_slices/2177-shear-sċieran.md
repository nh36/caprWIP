---
row_id: 2177
concept: shear
counterpart: sċieran
proto: *skéraną
protoform: *skéraną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2177 shear / sċieran

## Current row state

- CONCEPT: `shear` [Germanic/data/germanic-aligned-final.tsv:958-958].
- COUNTERPART: `sċieran` [Germanic/data/germanic-aligned-final.tsv:958-958].
- PROTO: `*skéraną` [Germanic/data/germanic-aligned-final.tsv:958-958].
- PROTOFORM: `*skéraną` [Germanic/data/germanic-aligned-final.tsv:958-958].
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:958-958].
- The live aligned row has no row-local note beyond duplicated Wiktionary inheritance sourcing and already treats the lexeme as a regular derivation; the same cogset aligns Dutch `scheren`, English `shear`, OE `sċieran`, and German `scheren` under the same project transponent `*skéraną` [Germanic/data/germanic-aligned-final.tsv:956-959].
- `old_english_wiktionary.tsv` also gives `shear | sċieran`, but that only confirms the row's chosen OE headword at supplementary-source level; it is not stronger than the aligned row plus grammar/dictionary evidence [Germanic/data/old_english_wiktionary.tsv:238-238].
- `oe_known_problems.tsv` has no row-local entry for `2177`, `sċieran`, or `*skéraną`, so the row is not currently being tracked as a live OE exception [Germanic/data/oe_known_problems.tsv:1-9].
- `coverage_audit.md` still lists row `2177 | shear | sċieran | regular | no | - | - | - | none`, so no packet, research memo, dossier, or full report currently exists for this row and the linked metadata fields are intentionally blank here [Germanic/docs/lexeme_reports/coverage_audit.md:345-345].
- Current published debug snapshots are fully solved and agree with the row: `EXPECTED: sċieran`, `OUTPUTS: sċieran`. The compact/current derivation path is `*skéraną -> *skéran -> *skérąn -> *ʃérąn -> *ʃíerąn -> *ʃíeran -> sċieran`, labelled as OE Heavy Syllable Nasal Apocope, OE Secondary Nasalization, OE Sk Palatalization, OE Ws Palatal Diphthongization, and OE Weak Tail Reduction [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4016-4036; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:4695-4715; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27263-27377].
- Repo-local philological references support the lexeme but also show why notation layers must be kept apart. Orel cites normalized `*skeranan ... OE sceran 'to cut, to shear'`; Campbell explicitly contrasts `nW-S sceran, cut, beside W-S scieran, past scear, scéaron`; Bright gives the textbook sound-law example `*sceran > scieran, to shear` and the class-III paradigm `scieran ... scear ... scearon ... scoren`; Clark Hall has `scieran ... to cleave, hew, cut ... 'shear' sheep` [docs/references/orel_handbook_germanic_etymology.vision.txt:37766-37771; docs/references/campbell_old_english_grammar.txt:20988-20989,31986-31987; docs/references/bright_anglo_saxon_reader.txt:613-613,2567-2567; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:34974-34976].

## Development-note summary

No securely attachable **row-dedicated** DEV_NOTES dossier survives for row `2177`. That absence should be stated plainly. The current row is nevertheless stable: live TSV metadata, current derivation traces, and local reference works all converge on OE `sċieran`, and none of the surviving project materials treat the row as a mismatch or as an unresolved exception [Germanic/data/germanic-aligned-final.tsv:956-959; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4016-4036; Germanic/data/oe_known_problems.tsv:1-9]. What survives in `DEV_NOTES.md` is shared background on West Saxon palatal diphthongization, i-umlaut chronology, secondary nasalization notation, and later cleanup of obsolete breve spellings. That is enough for a working dossier, but not yet strong enough for confident index integration.

The three levels need to stay explicit. In live row metadata, **PROTO** and **PROTOFORM** are both the current project input string `*skéraną`; the **OE target** is the attested/selected row headword `sċieran` [Germanic/data/germanic-aligned-final.tsv:958-958]. The stage forms seen in debug traces — `*skéran`, `*skérąn`, `*ʃérąn`, `*ʃíerąn`, `*ʃíeran` — are chronological derivational states inside the OE pipeline, not rival row metadata [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27326-27335,27357-27377]. The literature adds a second distinction: normalized dictionary citation `OE sceran` in Orel and dialect label `nW-S sceran` in Campbell are not evidence that the row's live OE target is wrong; Campbell explicitly sets `W-S scieran` beside `nW-S sceran`, so the row's `sċieran` is best read as a West-Saxonized OE target choice rather than as a contradiction of the normalized `sceran` lemma [docs/references/orel_handbook_germanic_etymology.vision.txt:37766-37771; docs/references/campbell_old_english_grammar.txt:20988-20989].

The current live derivation is straightforward once that dialect/notation separation is kept in view. The published trace shows no Germanic-side changes before Old English. In OE, Heavy Syllable Nasal Apocope first removes final `*ą`, producing `*skéran`; Secondary Nasalization then yields `*skérąn`; `sk` palatalizes before the front vowel to `*ʃérąn`; West Saxon palatal diphthongization turns `*e` into `*ie` after the initial palatal, giving `*ʃíerąn`; and Weak Tail Reduction supplies the final `*ʃíeran`, orthographic `sċieran` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27322-27335,27357-27377]. The absence of any `OEIUmlaut` change in the live trace is important: this row behaves like an infinitive without an i-umlaut trigger, not like a suffixal `*-iz` noun where umlaut must feed or preempt later diphthongization [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27330-27335].

That is also the main lesson recoverable from shared DEV_NOTES. The relevant `DEV_NOTES.md` discussions are not about `sċieran` by name, but they repeatedly distinguish two environments that matter here: forms like `giefan`, where an infinitive in `*-aną` has **no i-umlaut trigger** and therefore keeps `*e` available for West Saxon palatal diphthongization, versus forms like `ġift` or `sċēaþ`, where i-umlaut changes the vowel before palatal diphthongization gets its chance [Germanic/docs/DEV_NOTES.md:6496-6504,11171-11200,11309-11329]. Row `2177` plainly belongs to the first group. Bright and Campbell reinforce that transfer directly, because both list `scieran` alongside `giefan` as an example of front-vowel diphthongization after a palatal [docs/references/bright_anglo_saxon_reader.txt:613-613; docs/references/campbell_old_english_grammar.txt:5174-5180].

The notation history also needs to be handled conservatively. An older March 2026 full trace wrote the input as `*skerăną`, with breve on the weak-tail vowel, and later ran through `WsPalatalDiphthongization: *ʃierăną` before ending at `sċieran` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:11113-11165]. That spelling is not a competing PROTOFORM for the row. Later DEV_NOTES cleanup makes the status explicit: by §17.13, “all TSV PROTOFORM cells were already breve-free,” the plain-`a` path was “the one actually fed into the FST,” and after the staged removal “no derivation in the pipeline introduced `{*ă}` anywhere” because “the grammar is now breve-free at every live code site” [Germanic/docs/DEV_NOTES.md:28153-28212,28292-28296]. So the older `*skerăną` trace survives only as engineering history of a notation layer that has since been retired.

A second notational caution concerns secondary nasalization. DEV_NOTES once proposed a new symbol `{*ã}` for secondary/contact nasalization while reserving `{*ą}` for primary nasalization from lost nasals before fricatives, and that proposal explicitly said secondary nasalization was “NOT yet in FST” at that stage [Germanic/docs/DEV_NOTES.md:9592-9650]. The live trace now does have an `OESecondaryNasalization` step, but it prints `*skérąn`, not a dedicated `*skérãn` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27326-27335]. For this row, then, the notation difference is project chronology, not lexical substance: older DEV_NOTES preserved a more fine-grained proposed symbol split, while current live traces collapse the nasalized stage into the ogonek notation actually used in the running pipeline.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6496-6504

- Source heading: `OE ġift 'gift' — I-Umlaut Blocks WS Palatal Diphthongization`
- Source line or section hint: `lines 6496-6504`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `ws_palatal_diphthongization`; `no_i_umlaut_trigger`; `giefan_comparator`; `shared_chronology`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is the closest current DEV_NOTES fragment to a row-2177 rule statement even though it names `giefan`, not `sċieran`. DEV_NOTES says of `*gebaną` that the infinitive `*-ăną` “has NO i-umlaut trigger,” that the vowel therefore “remains `*e`,” and that `WS palatal diphthongization: *e → *ie` applies, yielding “WS `giefan` (with diphthong ie) vs. Anglian `gefan` (without)” [Germanic/docs/DEV_NOTES.md:6496-6504]. Row `2177` has the same crucial structural profile: an OE infinitive in `*-aną`, no i-umlaut trigger in the suffix, and an initial segment that becomes palatal before a front vowel. Bright's `*sceran > scieran` and Campbell's `e > ie: scieran ... giefan` confirm that the transfer is not speculative but philologically standard [docs/references/bright_anglo_saxon_reader.txt:613-613; docs/references/campbell_old_english_grammar.txt:5174-5180].

### DEV_NOTES:line-11171-11200

- Source heading: `I-Umlaut / WS Palatal Diphthongization Chronology (2026-03-17)`
- Source line or section hint: `lines 11171-11200`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `i_umlaut_vs_palatal_diphthongization`; `ordering_control`; `sċēaþ_comparator`; `shared_chronology`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2178`

This fragment matters for row `2177` because it defines the competing chronology that **does not** apply here. DEV_NOTES uses `*skaiθiz -> sċēaþ` to show that when an i-umlaut trigger is present, “i-umlaut must precede WS palatal diphthongization” so that `ǣ` exists in time for the West Saxon `ēa` outcome [Germanic/docs/DEV_NOTES.md:11171-11200]. That is valuable negative control for `sċieran`: the live `shear` trace shows `OEIUmlaut [no-change]` followed by `OEWsPalatalDiphthongization: *ʃíerąn`, exactly because row `2177` lacks the umlaut-triggering suffixal environment that drives the `sċēaþ` problem [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27330-27335]. Keeping this contrast explicit prevents later writeups from importing `sċēaþ`-style umlaut reasoning into a verb whose OE diphthong comes from the simpler `e -> ie after palatal` pathway.

### DEV_NOTES:line-11309-11329

- Source heading: `Background: WS palatal diphthongization vs i-umlaut`
- Source line or section hint: `lines 11309-11329`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `with_vs_without_i_umlaut_trigger`; `giefan_vs_gift`; `row_classification`; `shared_chronology`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This later DEV_NOTES summary is the cleanest prose statement of the contrast row `2177` needs. DEV_NOTES splits forms into two groups: “Without i-umlaut trigger (e.g., `*gebaną` 'to give')” where `WS palatal diphthongization: *e -> *ie` produces `giefan`, and “With i-umlaut trigger (e.g., `*geftiz` 'gift')” where i-umlaut first changes `*e -> *i` and “WS palatal diphthongization: no effect” [Germanic/docs/DEV_NOTES.md:11309-11329]. `*skéraną -> sċieran` belongs unambiguously with the first class. The current live trace confirms that classification mechanically by leaving `OEIUmlaut` inactive and letting `OEWsPalatalDiphthongization` do the visible vocalic work [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27330-27335].

### DEV_NOTES:line-28153-28212

- Source heading: `§17.13 — Eliminating the remaining breve {*ă} (2026-04-24)`
- Source line or section hint: `lines 28153-28212`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `notation_cleanup`; `breve_retirement`; `protoform_policy`; `trace_interpretation`
- Recommended next use: `cite_if_notational_confusion_arises`
- Shared with row IDs:

This is the current project-policy fragment that explains why older row traces may show `*skerăną` even though the live row and live traces do not. DEV_NOTES states that “all TSV PROTOFORM cells were already breve-free,” that the remaining breve survived “only inside the grammar machinery,” and that once the dead source alternatives were removed, “no derivation in the pipeline introduced `{*ă}` anywhere” [Germanic/docs/DEV_NOTES.md:28153-28212]. For row `2177`, that means older weak-tail spellings with breve are stale engineering notation rather than alternate lexical reconstructions. The live row's `*skéraną` and the current published traces' plain-`a` stages should be treated as the authoritative current notation layer [Germanic/data/germanic-aligned-final.tsv:958-958; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27263-27377].

### DEV_NOTES:line-9592-9650

- Source heading: `Primary vs Secondary Nasalization: The Correct Solution`
- Source line or section hint: `lines 9592-9650`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `secondary_nasalization`; `symbol_proposal`; `notation_history`; `coda_nasal_environment`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This fragment should be preserved only as notation history. It distinguishes primary `{*ą}` from a proposed secondary `{*ã}` and says secondary/contact nasalization was “NOT yet in FST” at the time, even while arguing that coda-nasal contexts should block fronting [Germanic/docs/DEV_NOTES.md:9592-9650]. That background is relevant to row `2177` because the live derivation does pass through a coda-nasal stage after Heavy Syllable Nasal Apocope, but the fragment is not current symbol policy: the running trace now has an actual `OESecondaryNasalization` step yet still writes `*skérąn`, not `*skérãn` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27326-27335]. Later work can use this fragment to explain why older discussions talk about a separate nasalization symbol, but it should not be promoted over the live trace's notation.

## Superseded or diagnostic material

- The clearest stale engineering artifact is the older March 2026 full trace spelling `PROTO: *skerăną`, with the diphthongization stage `*ʃierăną` before final output `sċieran` [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:11113-11165]. Because later DEV_NOTES says PROTOFORM cells were already breve-free and that no live derivation now introduces `{*ă}`, this older trace should be kept only as diagnostic project history, not as evidence for changing row `2177` away from live `*skéraną` [Germanic/docs/DEV_NOTES.md:28153-28212,28292-28296].
- The normalized/headword form `OE sceran` in Orel and the dialect label `nW-S sceran` in Campbell are not superseded, but they are easy to misuse if uncontextualized. They belong to dictionary normalization or non-West-Saxon dialect description, whereas the live row and current traces target West-Saxon-style `sċieran`; Campbell explicitly preserves both within the same verbal lexeme [docs/references/orel_handbook_germanic_etymology.vision.txt:37766-37771; docs/references/campbell_old_english_grammar.txt:20988-20989,31986-31987; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4016-4036].
- No row-local problem note survives in `oe_known_problems.tsv`, and no row-local packet/memo exists. That silence is diagnostically important: it means the current need here is documentation and disambiguation of shared background, not repair of a known broken derivation [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/coverage_audit.md:345-345].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited later, decide whether row `2177` should stay a no-index slice unless a dedicated row-specific DEV_NOTES section, packet, or memo is created; the present dossier rests on shared background plus live trace evidence rather than on row-local DEV_NOTES authority.
- If a future packet or report is written, state the dialect distinction explicitly: normalized/general OE `sceran` and `nW-S sceran` are not reasons to rewrite the row's current West-Saxon target `sċieran`, but they do need to be named so later reviewers do not mistake them for contradictory targets [docs/references/orel_handbook_germanic_etymology.vision.txt:37766-37771; docs/references/campbell_old_english_grammar.txt:20988-20989].
- If later review wants to comment on nasalization notation, keep chronological layers separate: older DEV_NOTES proposed a dedicated secondary-nasalization symbol `{*ã}`, current live traces use `OESecondaryNasalization` but spell the stage as `*skérąn`, and neither notation issue changes the row's OE target `sċieran` [Germanic/docs/DEV_NOTES.md:9592-9650,28153-28212; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:27326-27335].
