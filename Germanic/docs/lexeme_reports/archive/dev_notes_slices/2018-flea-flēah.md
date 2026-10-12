---
row_id: 2018
concept: flea
counterpart: flēah
proto: *fláuxz
protoform: *fláuxz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-leek-2026.md
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2018 flea / flēah

## Current row state

- CONCEPT: `flea`
- COUNTERPART: `flēah`
- PROTO: `*fláuxz`
- PROTOFORM: `*fláuxz`
- DERIVATION_CLASS: `regular`
- Live TSV row 2018 currently stands as a plain inherited OE row with `COUNTERPART = flēah`, `PROTO = *fláuxz`, and no row-local note beyond inherited-etymology placeholders [Germanic/data/germanic-aligned-final.tsv:339-342].
- Coverage infrastructure is still absent for this row: `coverage_audit.md` marks row 2018 as `no` packet, `-` memo, `-` attached DEV_NOTES fragment, and `none` under other infrastructure, so this slice is replacing missing row-local working notes rather than condensing an existing packet stack [Germanic/docs/lexeme_reports/coverage_audit.md:240-242].
- `oe_known_problems.tsv` has no entry for `*fláuxz`, so the row is not currently parked as an exception, unresolved mismatch, or editorially frozen special case [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation snapshot already reaches the target without workaround: `*fláuxz` > `*fláux` by final `-z` deletion, then `OE Au Fronting: *fláeux`, then `OE Diphthong Leveling: *flēax`, with orthographic output `*flēah` and final outcome `flēah` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1361-1381].
- For attestation/dialect background, the best directly relevant repo-side quotation presently at hand is Campbell §225 as preserved in the leek dossier: “The smoothing of éa has still not taken place in a number of forms preserved in Ep.: léag lye, **fléah flea**, géacaes- g.s. cuckoo, téac tye ...” [Germanic/docs/dossier-leek-2026.md:71-80]. This is useful because it shows an unsmoothed `fléah`-type form is not merely a mechanical FST output; but the same passage is about glossary distribution and later smoothing, so it should not be overstated into a single universal OE norm.
- The broader dialect comparison file keeps the contrast explicit: it lists `*flauh > WS fléah, Merc./North. ge-fleh 'fled'` and then quotes Brunner §119 with `fleh / fleg` beside WS `fleah`, i.e. unsmoothed WS versus Anglian smoothed reflexes before `h` [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:132-166]. That evidence is not noun-specific in every example, but it is directly relevant to the row's present status: `flēah` is best read as the repo's WS-default unsmoothed target, with `fleh`-type material as dialectal comparator rather than live replacement target.

## Development-note summary

No lexeme-specific DEV_NOTES section for row 2018 survives in the live `DEV_NOTES.md`, and this slice should say that plainly. The row is currently supported mainly by **shared** DEV_NOTES policy on OE dialect handling plus the successful debug trace, not by a preserved flea-only research block [Germanic/docs/lexeme_reports/coverage_audit.md:240-242; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1361-1381].

The shared DEV_NOTES material is still enough to explain why the live row stays conservative. First, DEV_NOTES explicitly preserves Brunner's statement that Anglian smoothing reduces the diphthongs from Germanic `au, eu, iu` to simple vowels before `c, g, h`, and DEV_NOTES itself glosses this with examples including `heh 'high', fleh 'fled'` [Germanic/docs/DEV_NOTES.md:33863-33865]. Second, DEV_NOTES elsewhere states programmatically that “Anglian smoothing is NOT modeled in the FST. Our FST is ‘WS-default’ in dialect choice elsewhere” [Germanic/docs/DEV_NOTES.md:26784-26810]. Third, a later current note warns that adding an unconditional smoothing rule would regress unsmoothed WS forms such as `*hēah`, `*ēage`, `*sēah`, `*tēah`; DEV_NOTES calls smoothing “dialectally restricted (Anglian)” and only lexically diffused into WS in a small set [Germanic/docs/DEV_NOTES.md:37945-37953].

For row 2018, that means the working distinction should remain sharp. `PROTO` and `PROTOFORM` are both the same comparative input `*fláuxz`; no alternate preform or paradigm-cell substitution is currently in play [Germanic/data/germanic-aligned-final.tsv:341-341]. `COUNTERPART = flēah` is the live OE target because the present WS-default cascade derives it directly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1370-1381]. Smoothed `fleh`-type outcomes are real dialect evidence in the project's shared literature notes, but they are **shared comparator material**, not row-specific instructions to replace the current counterpart [Germanic/docs/DEV_NOTES.md:33863-33865,37945-37953; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:148-166].

## Relevant DEV_NOTES fragments

### DEV_NOTES:33863-33865

- Source label line: `DEV_NOTES shared dialect fragment`
- Source heading: `Brunner §119 on "Ebnung" (quoted inside the swester investigation)`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md lines 33863-33865`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `anglian_smoothing`; `dialect_split`; `shared_comparator`; `before_h`
- Recommended next use: `cite_when_explaining_why_fleh_is_comparator_not_target`
- Shared with row IDs: `2151 and other au/eu/iu > ēa/eo rows with possible Anglian smoothing comparators`

DEV_NOTES preserves Brunner's wording directly: “Vor c, 3, h stehen in den anglischen Mundarten für die aus germ. au, eu, iu entstandenen ea, eo, io ... **einfache Vokale**,” and immediately glosses this as Anglian smoothing before velars, “reducing diphthongs to monophthongs. Examples: becen 'sign', ec 'also', heh 'high', **fleh 'fled'**” [Germanic/docs/DEV_NOTES.md:33863-33864]. For row 2018 this is not row-specific proof about the noun `flea`; it is shared comparative support showing that a `fleh`-type outcome belongs to the expected Anglian side of the dialect split.

The note should therefore use this fragment conservatively. It supports the proposition that the `flēah`/`fleh` contrast is philologically real and already recognized in the project's literature handling, but it does **not** by itself instruct us to replace `flēah` with a smoothed form. The fragment survives as a warning against flattening all OE reflexes of `*fláuxz` into a single dialect-neutral shape [Germanic/docs/DEV_NOTES.md:33863-33865].

### DEV_NOTES:26784-26810

- Source label line: `DEV_NOTES shared FST-policy fragment`
- Source heading: `STAGE 5 — Dialect split: Anglian smoothing vs WS i-umlaut`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md lines 26784-26810`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `ws_default_policy`; `anglian_smoothing_not_modeled`; `dialect_choice`
- Recommended next use: `cite_when_justifying_live_target_selection`
- Shared with row IDs: `2061 and other rows where Anglian smoothing is a possible but unmodeled comparator`

This fragment is not about `flea` by name, but it is one of the clearest current project-policy statements relevant to the row. DEV_NOTES sets out a dialect split and then states explicitly: “Anglian smoothing is NOT modeled in the FST. Our FST is ‘WS-default’ in dialect choice elsewhere” [Germanic/docs/DEV_NOTES.md:26803-26810]. Although the immediate examples concern `*éa + g` and umlauted developments, the policy sentence is broader than that example set and explains the present editorial stance for row 2018.

For this slice, the practical consequence is straightforward. Since the live cascade is WS-default unless a row is deliberately treated otherwise, `flēah` is the expected repository target once the derivation reaches `*flēax` and the orthography maps final `x`/`h` accordingly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1374-1381]. A later report can mention Anglian `fleh`-type comparators, but should not silently rewrite the row as though the project were already modeling Anglian smoothing by default [Germanic/docs/DEV_NOTES.md:26784-26810].

### DEV_NOTES:37945-37953

- Source label line: `DEV_NOTES shared anti-smoothing fragment`
- Source heading: `Why no FST fix`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md lines 37945-37953`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `no_unconditional_smoothing`; `ws_unsmoothed_forms`; `editorial_scope`
- Recommended next use: `cite_when_explaining_why_flēah_stays_regular`
- Shared with row IDs: `2151 and the broader hēah/ēage/sēah/tēah class`

This is the strongest current DEV_NOTES fragment for preserving `flēah` as the live counterpart. In a different lexeme dossier, DEV_NOTES says that to derive a smoothed Anglian-looking form one would need `ēa → ē / _velar`, but that “as an unconditional cascade rule this would regress at minimum *bēacen, *hēah, *ēage, *sēah, *tēah — all WS forms that retain the diphthong.” It then adds: “Smoothing is dialectally restricted (Anglian) and only lexically diffused into WS for a small set” [Germanic/docs/DEV_NOTES.md:37945-37953].

Row 2018 belongs on the unsmoothed side of exactly that policy unless a future row-local dossier proves otherwise. The note does not name `flēah`, but the structural relevance is close: an `ēa`-before-`h` form from a Germanic `au` input should not be normalized automatically to an Anglian monophthong when the project is explicitly protecting WS forms that retain the diphthong [Germanic/docs/DEV_NOTES.md:37945-37953]. In other words, this fragment is shared policy, not flea-specific philology, but it is still current and directly useful.

## Superseded or diagnostic material

- No surviving flea-specific DEV_NOTES memo was located. That absence should be preserved rather than disguised: the row currently depends on shared dialect-policy fragments plus the successful derivation trace, not on a lost or implied lexeme dossier [Germanic/docs/lexeme_reports/coverage_audit.md:240-242].
- A nearby diagnostic cluster in DEV_NOTES on preconsonantal `*x`-loss is useful mainly as negative evidence. It inventories rows whose protoforms contain medial `*xC` patterns and names rows such as 2017 `*fláxsą -> fleax`, 2015 `*fúnxstiz -> fȳst`, and 2092 `*xláxjaną -> hliehhan`, but row 2018 does not appear there [Germanic/docs/DEV_NOTES.md:39260-39310]. That fits the current trace: `*fláuxz` loses final `-z`, then surfaces as final `-h` orthographically after ordinary OE developments; it is not being managed as a preconsonantal `x`-loss problem-row [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1370-1381].
- The dossier and analysis material on `fléah`/`fleh` are diagnostic support, not replacement authority. They are useful for keeping WS unsmoothed versus Anglian smoothed outcomes apart, but they do not override the live row's present WS-default target selection [Germanic/docs/dossier-leek-2026.md:71-80; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:148-166].

## Open questions for later work

- If this row later receives a full packet or memo, decide whether to document exact attestation for noun `flēah`/`fléah` from dictionary reference files, rather than relying only on the aligned row plus shared Campbell/Brunner discussion.
- If repo policy ever shifts away from a WS-default OE target layer, revisit row 2018 together with the broader unsmoothed `ēa` before velar/`h` set (`hēah`, `ēage`, `sēah`, `tēah`, and comparable rows), not in isolation [Germanic/docs/DEV_NOTES.md:37945-37953].
- If later work needs dialect-rich reporting, add an explicit note distinguishing present live target `flēah` from Anglian smoothed comparator `fleh`; at present that distinction is real but supported mainly by shared literature policy rather than a flea-only DEV_NOTES argument [Germanic/docs/DEV_NOTES.md:33863-33865; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:148-166].
