---
row_id: 2191
concept: singe
counterpart: senġan
proto: *sángijaną
protoform: *sángijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2191 singe / senġan

## Current row state

- The live OE row reads `CONCEPT = singe`, `COUNTERPART = senġan`, `PROTO = *sángijaną`, `PROTOFORM = *sángijaną`, `DERIVATION_CLASS = regular`. The row currently has no OE-facing `NOTE`, and its only source strings are duplicated Wiktionary inheritance provenance rather than a row-specific project note [Germanic/data/germanic-aligned-final.tsv:1011-1011].
- The row is currently fully aligned in the published OE trace output. The compact published report gives `PROTO: *sángijaną`, `EXPECTED: senġan`, `OUTPUTS: senġan`, and the row-level derivation path `OE Heavy Syllable Nasal Apocope > OE Secondary Nasalization > Sievers Law Syncope > OE Velar Palatalization > OE I Umlaut > OE Weak Tail Reduction > OE J Loss After Heavy` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4245-4265].
- The expanded trace confirms the same path in rule-by-rule form: `*sángijaną` remains unchanged through Proto-West-Germanic and Northwest-Germanic sections; in the OE section it passes through `*sángijan`, `*sángijąn`, `*sángjąn`, `*sánʤjąn`, `*senʤjąn`, `*senʤjan`, and `*senʤan`, then surfaces orthographically as `senġan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28888-29001].
- `oe_known_problems.tsv` has no dedicated exception row for `*sángijaną`, `senġan`, or row `2191`, which is consistent with the trace evidence that the current grammar already derives the target without a row-specific workaround [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists the row as uncovered: `| 2191 | singe | senġan | regular | no | - | - | - | none |`. This slice therefore has to function as the row's working dossier rather than as an abstract of an already-written packet or memo [Germanic/docs/lexeme_reports/coverage_audit.md:353-353].
- Local reference files support the target lexeme but mostly preserve plain-`g` dictionary spelling rather than the row's normalized `ġ`. Campbell includes `sengan singe` among the front-vowel-plus-consonant palatalization examples and then again cites `sengan` among verbs showing assibilation; Clark Hall gives `sengan (æ) to 'singe,' burn slightly`; Bosworth-Toller likewise has `sengan`; and the local palatalisation dossier explicitly uses *singe* as the post-nasal affricate example [docs/references/campbell_old_english_grammar.txt:11302-11318,11410-11418; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:35979-35980; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:113560-113561; Germanic/docs/dossiers/g-palatalisation-conditioning.md:360-364].

## Development-note summary

The surviving DEV_NOTES evidence for row 2191 is real but fragmentary. There is **no** dedicated `§17.xx` singe dossier in `DEV_NOTES.md`; instead the row survives through a small number of shared implementation notes plus the live derivation traces. That matters for later use. The row is currently stable in the transducer and philologically straightforward enough to document, but the DEV_NOTES record itself is thinner than for rows with a bespoke repair section, so later index work has to be careful not to treat a couple of brief shared notes as if they were a full lexeme monograph [Germanic/docs/DEV_NOTES.md:1750-1753,8903-8936,2322-2324; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4245-4265].

At the level of the **live row**, there is no split between comparative input and OE-facing derivational input: both `PROTO` and `PROTOFORM` are `*sángijaną`, and the active grammar returns the attested OE infinitive `senġan` exactly [Germanic/data/germanic-aligned-final.tsv:1011-1011; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28888-29001]. The row should therefore not be described as one of the cases where the project is deliberately feeding an OE-only proxy form or a paradigm-cell substitute while keeping a different comparative proto label. The attested OE target is `senġan`; the live FST input is also `*sángijaną`.

The main complication is that DEV_NOTES preserves more than one notation layer for that input, and those layers are **not all the same kind of difference**. The January 2026 chronology check still wrote the form as `*sangjăną` and reported the successful output `**senġan**` [Germanic/docs/DEV_NOTES.md:1750-1753]. The later March 2026 Sievers-law implementation table rewrote the heavy-stem class-I weak verb as `*sangijăną`, explicitly listing `*sangjăną | *sangijăną | by analogy (CVCC heavy)` among the global TSV updates [Germanic/docs/DEV_NOTES.md:8903-8936]. The **difference between `*sangjăną` and `*sangijăną` is chronological/project-policy substance**, not mere orthographic decoration: the March note is the explicit statement that heavy stems of this class should keep `-ij-` in the underlying notation and let `SieversLawSyncope` delete the `i` later. By contrast, the live TSV spelling `*sángijaną` is best read as the same structural analysis as `*sangijăną`, just in the repo's current stress-marking/diacritic notation: acute `á` replaces the older unaccented `a`, and the unstressed `a` before `ną` is no longer marked with breve [Germanic/data/germanic-aligned-final.tsv:1011-1011; Germanic/docs/DEV_NOTES.md:8907-8913,8917-8929]. In other words: `*sangjăną` is an older shorthand now superseded for heavy stems; `*sangijăną` and live `*sángijaną` are the same chosen analysis in different house notations.

The derivational chronology in the live trace is much more explicit than the terse DEV_NOTES mention, and it should be carried forward in detail because it shows exactly why the row now works. The first crucial step is not palatalization but weak-tail handling: `OEHeavySyllableNasalApocope` removes the segmental `-ą`, `OESecondaryNasalization` moves the nasal feature onto the preceding vowel, and `SieversLawSyncope` then deletes the `i` in the heavy stem, taking `*sángijąn` to `*sángjąn` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28950-28953]. Only after that does `OEVelarPalatalization` convert the post-nasal velar to `ʤ`, `OEIUmlaut` front-mutinates stressed `á > e`, `OEWeakTailReduction` simplifies the ending, and `OEJLossAfterHeavy` removes the remaining `j`, yielding `*senʤan` before orthographic rendering as `senġan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28955-28958,28981-29001]. This order is exactly what the January chronology note was preserving in compressed form when it said the implementation now lets palatalized consonants count as intervening segments for i-umlaut and that the result is `*sangjăną -> senġan` [Germanic/docs/DEV_NOTES.md:1750-1753]. The note is short, but the trace shows that its claim is live and not stale.

The philological value of the row is not only that the surface form matches, but that the shape of the OE medial consonant is exactly the one the handbook tradition predicts. Campbell's palatalization chapter includes `sengan singe` in the list of forms where a front vowel before a consonant licenses palatalization of medial `g`, and later cites `sengan` again among verbs showing assibilation beside `pencan`, `pyncan`, and `sécan` [docs/references/campbell_old_english_grammar.txt:11302-11318,11412-11418]. The local palatalisation dossier makes the allophonic point explicit: inherited post-nasal `[ŋɡ]` yields an affricate outcome, and `*singe*` is listed with *bridge* as the exact type for which Campbell §430 is said to be decisive [Germanic/docs/dossiers/g-palatalisation-conditioning.md:360-364]. That background matters because the row's normalized spelling `senġan` can look more marked than dictionary headword `sengan`; in practice they are not rival targets. Clark Hall and Bosworth-Toller both head the word under plain `sengan`, but Campbell's own discussion shows that the lexeme belongs to the assibilated/palatal class, and the project's normalized `ġ` is simply making that OE phonological value explicit [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:35979-35980; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:113560-113561; docs/references/campbell_old_english_grammar.txt:11412-11418].

The only other DEV_NOTES mention of “singe” is not row authority and should be labelled that way. In the English attested-form harness note, `sieve/singe/timber` are grouped together as “suffixal analogies” still missing from the English brace sandbox, i.e. the Modern English attested-form project rather than the OE row transducer [Germanic/docs/DEV_NOTES.md:2322-2324]. That note is diagnostically useful only because it proves that the string “singe” also appears in a different subsystem with different goals. It should **not** be imported as evidence that OE row 2191 itself is unstable, analogical, or in need of repair. The live OE row is already an exact match and `oe_known_problems.tsv` does not flag it [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4245-4265].

The conservative dossier-level conclusion is therefore fairly sharp. `PROTO`, `PROTOFORM`, and the attested OE target are distinct categories in principle, but for the current live row the first two coincide as `*sángijaną` and the third is `senġan` [Germanic/data/germanic-aligned-final.tsv:1011-1011]. `*sangjăną` in older DEV_NOTES is stale shorthand from before the heavy-stem `-ij-` policy was written out explicitly; `*sangijăną` in the March table and live `*sángijaną` are effectively the same chosen input in older versus current notation; and `senġan` is the attested/normalized OE output supported both by the trace and by Campbell's treatment of `sengan` as a palatal-assibilated verb [Germanic/docs/DEV_NOTES.md:1750-1753,8903-8936; docs/references/campbell_old_english_grammar.txt:11302-11318,11412-11418]. What the slice cannot honestly claim is that DEV_NOTES already preserves a tidy, row-dedicated final note suitable for effortless index extraction. The live row is secure; the DEV_NOTES footprint is still mostly shared implementation history.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1750-1753

- Source heading: `OE *-gj- chronology check (2026-01-22)`
- Source line or section hint: `lines 1750-1753`
- Fragment type: `shared_row_verification`
- Status: `current_but_brief`
- Issue tags: `palatalization_order`; `i_umlaut_after_palatalization`; `gj_cluster`; `trace_alignment`
- Recommended next use: `cite_with_trace_not_alone`
- Shared with row IDs: `1943; 1961; 2069`

This is the only genuinely row-explicit DEV_NOTES statement now attached to `senġan`. It says that the implementation was adjusted so palatalized consonants can count as intervening segments for i-umlaut, and that the result is `*sangjăną -> **senġan**` [Germanic/docs/DEV_NOTES.md:1750-1753]. On its own, the fragment is too compressed to serve as a final report note, because it does not spell out the full derivation, distinguish old from new notation, or explain why `singe` belongs to the `*-gj-` chronology bucket. But it is still current in an important sense: the live full trace now visibly instantiates the same ordering claim, with `SieversLawSyncope`, `OEVelarPalatalization`, and `OEIUmlaut` firing in the order the note presupposes [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:28950-28959].

### DEV_NOTES:line-8903-8936

- Source heading: `Sievers' Law Implementation Status (2026-03-13)`
- Source line or section hint: `lines 8903-8936`
- Fragment type: `row_policy_and_notation`
- Status: `current`
- Issue tags: `heavy_stem_class_i`; `sievers_law`; `notation_policy`; `protoform_normalization`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2093; 2172; 2173; 2232`

This is the fragment that explains why the live row now contains explicit `-ijan-` notation while an older DEV_NOTES success note still wrote `*sangjăną`. The March status block says the grammar added `*-ijăną` patterns and `SieversLawSyncope`, and its update table explicitly rewrites `*sangjăną` to `*sangijăną` for this verb [Germanic/docs/DEV_NOTES.md:8907-8929]. For row 2191 that is not a minor cosmetic change: it marks the shift from older shorthand to an explicitly pre-syncope heavy-stem representation. At the same time, this fragment should be read together with the live TSV, because current `*sángijaną` is the same structural choice rendered in newer project notation rather than a third competing proto-analysis [Germanic/data/germanic-aligned-final.tsv:1011-1011].

### DEV_NOTES:line-2322-2324

- Source heading: `KIT sweep (WIP)`
- Source line or section hint: `lines 2322-2324`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `english_attested_form_project`; `suffixal_analogy`; `cross_project_name_collision`
- Recommended next use: `exclude_from_oe_indexing`
- Shared with row IDs: `2189; 2258`

This fragment mentions “singe,” but only in the Modern English attested-form sandbox. DEV_NOTES says the remaining English KIT-bucket failures included “suffixal analogies (`sieve/singe/timber`),” i.e. an English reconstruction problem entirely separate from the OE row transducer [Germanic/docs/DEV_NOTES.md:2322-2324]. It is useful to preserve because later readers searching DEV_NOTES for `singe` will hit it and may otherwise assume it belongs to row 2191. For the OE dossier, however, it is purely diagnostic and should not be indexed as row-defining evidence.

## Superseded or diagnostic material

The main superseded material is the older January shorthand `*sangjăną`. It is not wrong in the sense of pointing to a different lexeme, but it is no longer the project's preferred heavy-stem notation after the March 2026 Sievers-law normalization to explicit `*-ij-` inputs [Germanic/docs/DEV_NOTES.md:1750-1753,8903-8929]. Any later report that quotes the January line should therefore explain that it preserves an earlier notation layer rather than a rival protoform policy.

The other diagnostic trap is the plain-`g` lexicographic spelling `sengan`. Clark Hall and Bosworth-Toller use that spelling, and Campbell also writes `sengan`; none of those sources are thereby denying palatalization or assibilation. Campbell's own discussion is explicit that `sengan` belongs to the palatal/assibilated set, so the repo's `senġan` is a normalization choice, not a new lexical claim [docs/references/campbell_old_english_grammar.txt:11302-11318,11412-11418; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:35979-35980; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:113560-113561].

Finally, the English attested-form note `sieve/singe/timber` is diagnostic cross-project noise for this slice. It documents a separate sandbox's unresolved Modern English analogy problems and should remain outside any OE row-level indexing decision [Germanic/docs/DEV_NOTES.md:2322-2324].

## Open questions for later work

- If row 2191 is ever indexed, decide whether the index should point only to the March 2026 `Sievers' Law Implementation Status` block, or to that block plus the January `*-gj- chronology check`; the former carries the stable notation policy, while the latter carries the only explicit `senġan` result line.
- If a future full report is written, keep the notation history explicit: `*sangjăną` is older shorthand, `*sangijăną` is the explicit pre-syncope heavy-stem notation, and live `*sángijaną` is the current TSV spelling of that same analysis rather than a third independent reconstruction.
- If later row documentation quotes dictionary support, label plain `sengan` as lexicographic spelling for the same verb and not as evidence against normalized `senġan`.
- If later indexing standards require a row-dedicated DEV_NOTES paragraph rather than shared implementation fragments, this row may need a fresh synthesized packet or memo before it becomes a clean index candidate even though the underlying derivation itself is already stable.
