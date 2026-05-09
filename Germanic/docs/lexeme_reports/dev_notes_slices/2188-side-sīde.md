---
row_id: 2188
concept: side
counterpart: sīde
proto: *sḯdōn
protoform: *sī́dōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2188 side / sīde

## Current row state

- CONCEPT: `side` [Germanic/data/germanic-aligned-final.tsv:999-999]
- COUNTERPART: `sīde` [Germanic/data/germanic-aligned-final.tsv:999-999]
- PROTO: `*sḯdōn` [Germanic/data/germanic-aligned-final.tsv:999-999]
- PROTOFORM: `*sī́dōn` [Germanic/data/germanic-aligned-final.tsv:999-999]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:999-999]
- The live OE row carries only inherited source markers from Wiktionary; it does not currently carry a row-local explanatory note, exception label, or repair instruction in the aligned TSV [Germanic/data/germanic-aligned-final.tsv:999-999].
- `old_english_wiktionary.tsv` independently maps English `side` to OE `sīde`, so the row target is the ordinary attested OE noun rather than a special analogical surrogate or a hand-normalized reporting form [Germanic/data/old_english_wiktionary.tsv:249-249].
- `oe_known_problems.tsv` has no row-local entry for `2188`, `sīde`, or `*sḯdōn`, so the row is not currently being tracked as an OE exception, wontfix, or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage audit still lists row `2188` as a regular uncovered row with no packet, memo, dossier, or requirement basis; this slice is therefore replacing absent row-level notes rather than summarizing an existing report stack [Germanic/docs/lexeme_reports/coverage_audit.md:351-351].
- The current published derivation trace is fully successful and uncomplicated: `PROTO: *sḯdōn`, `EXPECTED: sīde`, `OUTPUTS: sīde`, with the explicit intermediate chain `NWGmc N Stem N Loss: *sḯdǭ`, then `OE Unstressed Long Vowel Shortening: *sḯdæ`, then `OE Unstressed AE Merger: *sḯde`, before surface `Outcome: sīde` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4206-4224].
- Local comparative reference material aligns with the live row rather than challenging it: Kroonen gives the feminine formation `*sīdōn-` for the Germanic ‘side’ word and explicitly groups OE `side` with ON `síða`, OS `sīda`, Dutch `zij(de)`, and OHG `sita`, adding that the noun was “derived from the adjective through a meaning ‘broad surface’” [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22573-22576].

## Development-note summary

No dedicated lexeme-specific `side / sīde` discussion survives in `DEV_NOTES.md`. The usable DEV_NOTES evidence for row `2188` is therefore narrow and has to be read with care. What survives is not a philological controversy dossier, not an exception memo, and not a row-specific repair history. It is primarily a notation-policy and verification trace: the project recorded that stressed-root long `*ī` rows were migrated from undifferentiated `*ī` notation to `*ḯ`, and row `2188` was one of the rows checked and committed in that migration batch [Germanic/docs/DEV_NOTES.md:42010-42024].

That surviving note is important because the live row now preserves a three-way distinction that could otherwise be misread as three competing reconstructions. The current `PROTO` `*sḯdōn` is the OE-pipeline input notation used after the stressed-root long-vowel migration; the current `PROTOFORM` `*sī́dōn` is the canonical acute-accent comparative form kept in the aligned TSV; and the older backup TSV used undifferentiated `*sīdōn` in both slots before the migration/column cleanup [Germanic/data/germanic-aligned-final.tsv:999-999; Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:999-999; Germanic/docs/DEV_NOTES.md:42010-42024]. For this row, those are notation layers and repository-policy layers, not chronological sound stages and not mutually exclusive lexical analyses.

The currently live derivation confirms that no special repair is hiding behind the notation split. The debug snapshot reaches attested OE `sīde` directly from live `PROTO` `*sḯdōn` by a short regular path: Northwest Germanic n-stem `n` loss, then Old English shortening of the unstressed long final vowel, then the OE unstressed `æ > e` merger [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4212-4224]. In other words, `PROTO` and `PROTOFORM` are distinct labels in the row, but the row does not currently show a conflict between comparative reconstruction and OE-facing derivation. The comparative side is also ordinary rather than ad hoc: Kroonen's `*sīdōn-` entry supports the same lexical family and gives a plausible derivational background from an adjective meaning something like ‘broad’ or ‘extended surface’ [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22573-22576].

The practical row policy is therefore conservative. `sīde` is presently a regular control row, and the only securely current DEV_NOTES attachment is that the row survived the `*ḯ` migration rather than being rewritten or exception-tagged. Because the surviving DEV_NOTES material is so thin, later reporting should avoid overstating the evidence. Nothing in DEV_NOTES currently says that `*sḯdōn`, `*sī́dōn`, and older `*sīdōn` represent different chronological stages in the lexeme's history; nothing says the row needs a different paradigm cell; and nothing says the row has a hidden mismatch. The documentation basis is real, but it is mostly verification and notation provenance, not a substantive lexeme-specific analysis [Germanic/docs/DEV_NOTES.md:42010-42024; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4206-4224].

## Relevant DEV_NOTES fragments

### DEV_NOTES:no-row-specific-side-dossier

- Source heading: no dedicated `side / sīde` section survives in `DEV_NOTES.md`
- Source line or section hint: direct row/lexeme search yields only the Phase 4 migration table mention at line `42024`
- Fragment type: `negative_result_with_current_implication`
- Status: `current`
- Issue tags: `missing_row_specific_authority`; `notation_history`; `verification_only`; `no_exception_dossier`
- Recommended next use: `preserve_as_no_index_context`
- Shared with row IDs:

The negative result is itself the first fact that needs preserving. A direct search of `DEV_NOTES.md` for `2188`, `sīde`, and the `*sīdōn/*sḯdōn` family does **not** uncover a row-local analytical block explaining the noun's semantics, stem class, or a mismatch problem. The only secure hit is the migration table entry `2153, 2182, 2188 | rīdan, sċīnan, sīde` in Phase 4 [Germanic/docs/DEV_NOTES.md:42020-42024]. That means later extraction work should not pretend there is a lost or implicit lexeme dossier hiding elsewhere in DEV_NOTES.

This absence has practical consequences. For row `2188`, the slice has to rely on the live TSV, the current derivation snapshot, and local reference material for the actual lexical dossier, while using DEV_NOTES mainly to explain notation provenance and verification status. That is enough to support a careful working note, but it is thinner than the lexeme-specific exception dossiers preserved for genuinely problematic rows [Germanic/data/germanic-aligned-final.tsv:999-999; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4206-4224].

### DEV_NOTES:line-42006-42024

- Source heading: `E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42024`
- Fragment type: `current_verification`
- Status: `current`
- Issue tags: `long_vowel_notation`; `verification_history`; `protoform_vs_proto`; `shared_fragment`
- Recommended next use: `cite_if_notation_split_needs_explanation`
- Shared with row IDs: `2153`, `2182`

This is the controlling current DEV_NOTES fragment for row `2188`, even though it is shared and terse. DEV_NOTES states the policy first: “16 OE rows have `*ī` in PROTOFORM,” of which “15 are stressed-root `*ī` ... migrated to `*ḯ`,” and row `2188` is then named in Batch 3 among the rows “rebuilt + probed + mismatch-checked + committed” [Germanic/docs/DEV_NOTES.md:42010-42024]. For `sīde`, the surviving note therefore establishes a concrete repository fact: the live `PROTO` spelling with `ḯ` is the result of a deliberate migration and subsequent verification, not an accidental editorial variant.

The fragment is also the best available evidence for how to read the row's notation layers. Because the migration note is explicitly about stressed-root long `*ī`, the contrast between current `PROTO *sḯdōn` and current `PROTOFORM *sī́dōn` should be treated as a repository representation distinction: OE-facing rule-sensitive input on one side, canonical comparative spelling on the other. The fragment does **not** imply that `*sḯdōn` is a later historical stage than `*sī́dōn`, nor that `*sī́dōn` was abandoned as false. It records a tooling and row-policy cleanup that left the lexical target `sīde` intact [Germanic/docs/DEV_NOTES.md:42010-42024; Germanic/data/germanic-aligned-final.tsv:999-999].

## Superseded or diagnostic material

- The older backup TSV entry with undifferentiated `*sīdōn` in both proto columns is diagnostic project history, not a rival live-row analysis. It predates the Phase 4 long-vowel migration and the sharper separation of OE-facing `PROTO` from canonical `PROTOFORM`; later writeups should not turn the backup spelling into evidence for a different lexical policy [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:999-999; Germanic/data/germanic-aligned-final.tsv:999-999; Germanic/docs/DEV_NOTES.md:42010-42024].
- The current debug trace is positive evidence for regularity, but it is not itself a DEV_NOTES fragment and should not be mistaken for a hidden analytical memo. Its value here is diagnostic confirmation that the row already works as-is: `*sḯdōn > *sḯdǭ > *sḯdæ > *sḯde > sīde` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4214-4224].
- Because DEV_NOTES preserves only shared verification material, this slice should be treated cautiously in any later indexing pass. It is accurate and useful, but it preserves mostly notation/verification provenance rather than a standalone row-specific argument.

## Open questions for later work

- If `dev_notes_slices/index.tsv` is updated later, decide whether a shared verification fragment alone is enough to justify indexing, or whether row `2188` should remain a no-index slice until a fuller lexeme-specific source audit is assembled.
- If later reporting cites the row, keep the label distinction explicit: `PROTO *sḯdōn` is the live OE-directed input notation, `PROTOFORM *sī́dōn` is the canonical comparative form, and older `*sīdōn` is legacy unified notation rather than a third historical stage [Germanic/data/germanic-aligned-final.tsv:999-999; Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:999-999; Germanic/docs/DEV_NOTES.md:42010-42024].
- If a future packet or memo is created for this lexeme, include the regular derivation trace explicitly, since that is currently more informative than DEV_NOTES itself for the actual OE pathway `*sḯdōn > sīde` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4206-4224].
