---
row_id: 2197
concept: slime
counterpart: slīm
proto: *slḯmą
protoform: *slī́mą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2197 slime / slīm

## Current row state

- Live OE row `2197` is currently a regular exact-match row with `CONCEPT = slime`, `COUNTERPART = slīm`, `PROTO = *slḯmą`, and the shared cognate-set protoform field still written `*slī́mą`; the row carries no live NOTE beyond duplicated Wiktionary-inheritance sourcing and no exception label in the derivation-class columns [Germanic/data/germanic-aligned-final.tsv:1035-1035].
- The immediately adjacent cognate-set rows matter because they show what is and is not OE-specific here. Dutch, English, and German all keep the plain comparative stem spelling `*slīmą`, while the OE row alone now uses `*slḯmą` in the live derivational column; the shared concept-level protoform field remains `*slī́mą` across the set [Germanic/data/germanic-aligned-final.tsv:1033-1036]. That split is not evidence for a different lexeme or a different chronological stage. It is the row-level encoding choice created when stressed long `*ī` had to be represented with a machine-safe single codepoint in the OE cascade.
- The current published OE derivation trace confirms that the row is fully regular in the live grammar. For `# slime`, the trace gives `PROTO: *slḯmą`, `EXPECTED: slīm`, `OUTPUTS: slīm`, with no Proto-West-Germanic or Northwest-Germanic change at all and only `OE Heavy Syllable Nasal Apocope: *slḯm` before surface `Outcome: slīm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4366-4385].
- `oe_known_problems.tsv` currently has no row-local entry for `2197`, `slīm`, `slime`, `*slḯmą`, or `*slī́mą`; the row is therefore not being tracked as an OE exception bucket item, a wontfix item, or a live mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure likewise treats the row as unremarkable at present: `coverage_audit.md` lists `2197 | slime | slīm | regular | no | - | - | - | none`, so this slice is replacing the absence of any packet, memo, or prior row report rather than extending an existing report chain [Germanic/docs/lexeme_reports/coverage_audit.md:358-358].
- Local reference files align on the lexical identity of the item even though they do not all use the same lemma format. Kroonen gives `*slīma- n. 'slime'` and cites `OE slīm m./n. 'slime, mud'`; Orel gives `*slīman sb.n.` with `OE slím id.`; Clark Hall lists simply `slīm n. 'slime'`; Kluge–Seebold likewise derives German `Schleim` from Germanic `*slīma- m./n.` with OE `slīm` as a cognate [@Kroonen2013, p. 455; @Orel2003, p. 351; @ClarkHall1960; @KlugeSeebold2011]. Those reference forms are best treated here as dictionary-style stem-class notations for the same inherited noun, not as evidence that the row needs a different OE-facing `PROTOFORM`.

## Development-note summary

No row-dedicated mismatch dossier for `slime / slīm` survives in `DEV_NOTES.md`. The securely attachable project material is instead a current implementation note about the stressed long-`ī` tier and the live derivation trace that shows the row succeeding. That makes row 2197 a good example of a **regular no-index slice**: the row is stable and philologically plausible, but the surviving DEV_NOTES evidence is mostly notation-and-pipeline history rather than a substantive lexeme-specific controversy [Germanic/docs/DEV_NOTES.md:41893-42067; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4366-4385].

The main distinction that must stay explicit is the three-way one between comparative lemma format, project derivational encoding, and attested OE output. The attested OE target is straightforward: `slīm` is dictionary-attested and is what the live OE row expects and produces [@ClarkHall1960; Germanic/data/germanic-aligned-final.tsv:1035-1035]. The comparative dictionaries use ordinary stem notation such as Kroonen `*slīma-` and Orel `*slīman`; those are lexicographic lemma shapes, not direct instructions about which exact inflected ending the OE transducer should receive [@Kroonen2013, p. 455; @Orel2003, p. 351]. The live OE derivation, by contrast, feeds the cascade with `*slḯmą`, because the project's OE branch now marks stressed long root `*ī` with a dedicated symbol `ḯ` and then strips that distinction again at surface level, yielding ordinary written `ī` in `slīm` [Germanic/docs/DEV_NOTES.md:41923-41957].

That in turn explains the apparent `PROTO` versus `PROTOFORM` split. In the row data supplied for this slice, `PROTO = *slḯmą` and `PROTOFORM = *slī́mą`. For current project purposes those should be read as **notation variants of the same OE-facing derivational input**, not as different chronological stages and not as competing row policies. DEV_NOTES is explicit that `ḯ` was adopted because foma would not reliably accept combining-acute `ī́` on input; the diaeresis in `ḯ` is “purely notational,” and the surface rule collapses `{*ḯ} -> ī` because OE orthography does not distinguish stressed-root long `ī` from any other long `ī` [Germanic/docs/DEV_NOTES.md:41925-41939,41952-41957]. The row's live behavior matches that explanation exactly: the trace begins from `*slḯmą` and ends at ordinary `slīm`, not at any special marked spelling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4366-4385].

The only live row-specific DEV_NOTES mention of `slīm` occurs inside the stressed-long-`ī` migration inventory. There the row appears in Batch 4 (`2197, 2257, 2285 | slīm, tīd, hwīl`) as one of the OE rows moved from plain `*ī` to stressed `*ḯ` [Germanic/docs/DEV_NOTES.md:42006-42026]. That mention is important, but only in a narrow way. It says that row 2197 participated in a systematic encoding repair; it does **not** say that `slīm` required a new etymology, a different paradigm cell, a sound-law exception label, or any analogical rescue. The same section's verification summary reports that mismatch totals held steady through the migration batches, which is consistent with the trace evidence that `slīm` remained a regular exact match before and after the notation change [Germanic/docs/DEV_NOTES.md:42031-42051].

The derivational behavior itself is correspondingly simple. The published trace shows no PGmc-to-PWGmc or PWGmc-to-NWGmc transformation at all and only a final OE apocope step deleting `*-ą`, after which the surface mapping yields `slīm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4373-4385]. Within the project's own logic, then, row 2197 is not a place where DEV_NOTES is preserving a hidden dispute about umlaut, breaking, palatalization, analogical levelling, or stem-class substitution. What DEV_NOTES preserves is a record that the row had to be re-encoded as a stressed-long-`ī` input so that the OE machinery would distinguish stressed root vowels from the unstressed feminine in-stem suffix `*-īn` that triggers `NWGmcInStemNLoss` elsewhere [Germanic/docs/DEV_NOTES.md:41895-41922].

That point also constrains how far one should press the comparative references. Kroonen's `*slīma-` versus Orel's `*slīman` is a real difference in lemma presentation, and Kroonen's `OE slīm m./n.` versus Clark Hall's `slīm n.` means the handbooks do not all compress lexical gender the same way [@Kroonen2013, p. 455; @Orel2003, p. 351; @ClarkHall1960]. But none of that creates a current row problem. The live row is not selecting among competing oblique cells or between masculine and neuter surface forms; it is simply deriving the attested OE headword `slīm` from an inherited `*slīma-`-type noun represented in the transducer as `*slḯmą` [Germanic/data/germanic-aligned-final.tsv:1035-1035; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4366-4385].

The safest overall conclusion is therefore conservative. Row 2197 is currently index-poor not because it is doubtful, but because its surviving DEV_NOTES material is mostly implementation guardrail prose about Unicode-safe stressed long `ī`. The row is philologically ordinary, currently regular, and locally well supported by the trace and dictionaries. What is missing is not evidence for the row, but a richer row-specific DEV_NOTES narrative that would justify central index integration. On present evidence it should remain a no-index slice unless the project later decides to index notation-migration fragments as first-class row evidence.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `surface_mapping`
- Recommended next use: `cite_if_explaining_notation_layers`
- Shared with row IDs: `2101`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the controlling current fragment for understanding why row 2197 now shows `*slḯmą` in the live OE derivation. DEV_NOTES states that the project introduced a stressed long-`ī` tier because the relevant rule distinction is stress-based, not syllable-count-based, and then documents the encoding choice in unusually explicit form: combining-acute `ī́` compiled but failed under `apply down`, while single-codepoint `ḯ` worked and was therefore adopted [Germanic/docs/DEV_NOTES.md:41899-41939]. DEV_NOTES then states the crucial interpretive rule outright: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41940].

For row 2197, the later part of the same fragment is just as important. DEV_NOTES says that `OldEnglishRemoveStars` maps `{*ḯ} -> ī` and explains why: OE orthography does not distinguish stressed-root long `ī` from unstressed-suffix long `ī`; the special tier exists only to gate one internal rule, after which the two collapse at surface level [Germanic/docs/DEV_NOTES.md:41948-41957]. That is exactly the relationship that later writers need to preserve between row `PROTO = *slḯmą`, row-data `PROTOFORM = *slī́mą`, and attested OE `slīm`: not chronological succession, but two machine-facing spellings for one stressed long vowel plus one ordinary surface spelling.

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 ... E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42026`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `implementation_history`
- Recommended next use: `cite_if_documenting_row_history`
- Shared with row IDs: `2257`; `2285`

This is the only securely attachable DEV_NOTES fragment that names row 2197 directly. In the migration inventory, Batch 4 is listed as `2197, 2257, 2285 | slīm, tīd, hwīl` [Germanic/docs/DEV_NOTES.md:42020-42026]. The narrow but important force of the fragment is that `slīm` was part of the deliberate OE-row migration from plain `*ī` to stressed `*ḯ`.

The fragment should be used carefully. It does preserve real row history, but the history is engineering history, not etymological dispute. Nothing in this row entry suggests that `slīm` needed a substitute paradigm cell, a new target, a rescued oblique form, or an exception bucket. The item appears here because its stressed root vowel belonged to the migration cohort, not because its derivation was otherwise failing.

### DEV_NOTES:line-42031-42051

- Source heading: `§17.46 ... F. Verification`
- Source line or section hint: `lines 42031-42051`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `migration_regression_check`; `regular_row`; `diagnostic_only`
- Recommended next use: `use_as_supporting_history_only`
- Shared with row IDs: all migrated `*ḯ` rows

This verification block does not name `slīm` individually, but it is still the best current project-history support for saying that the migration did not create a new row problem. DEV_NOTES reports representative probes after the batch work and then gives the mismatch totals: pre-branch baseline `14`, phase 2 `13`, and phases 3-4 holding at `13` throughout [Germanic/docs/DEV_NOTES.md:42031-42051]. For row 2197, the practical implication is modest but useful: the row moved into the stressed-`ḯ` cohort without creating a fresh mismatch bucket, which agrees with the current published trace's exact-match result `OUTPUTS: slīm` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4366-4385].

Because the fragment is aggregate rather than row-local, it should remain secondary. It helps document that row 2197's migration was stable, but it is not by itself a strong candidate for central index extraction.

## Superseded or diagnostic material

- The older combining-acute spelling `*slī́mą` should stay visible in this slice because it still survives in the shared cognate-set protoform field and in the row data supplied for this task [Germanic/data/germanic-aligned-final.tsv:1033-1036]. But DEV_NOTES is explicit that the project abandoned combining-acute input not because the linguistic analysis changed, but because foma input tokenization did not reliably accept it under `apply down`; `*slī́mą` is therefore diagnostic of an older encoding layer, not evidence for a distinct chronological proto-stage [Germanic/docs/DEV_NOTES.md:41925-41939].
- The reference-handbook forms `*slīma-` and `*slīman` also need careful handling. They remain accurate comparative dictionary headwords for the noun family [@Kroonen2013, p. 455; @Orel2003, p. 351], but within this row they are best treated as lemma-format variants and stem-class presentations, not as competing live project `PROTOFORM`s. Later writers should not cite them as if DEV_NOTES had weighed and rejected one against the other for the OE row.
- Polomé's comparison of `ON, OE slim 'slime'` with `OHG slifan, OE slipan` is real and locally useful if someone later wants a brief note on the wider `(s)ley-` lexical family, but it is indirect family-comparison material rather than live row policy [@Polome1967, p. 68]. For the present slice it belongs to diagnostic background, not to the governing row analysis.

## Open questions for later work

- If a future packet or memo is ever created for this row, decide whether the prose should normalize the notation bridge explicitly as `project *slḯmą = older project *slī́mą = dictionary lemma type *slīma-/*slīman`, since that is the only real interpretive trap in the surviving materials.
- If later reporting wants fuller lexical philology, decide whether to mention the mild dictionary disagreement over gender (`OE slīm n.` versus `m./n.`) [@ClarkHall1960; @Kroonen2013, p. 455]. Current row behavior does not depend on that choice, so it is not a reason to alter the row.
- If `dev_notes_slices/index.tsv` is revisited later, decide whether a row whose surviving DEV_NOTES evidence is almost entirely notation-migration history should remain unindexed even when the row is perfectly regular. On present evidence, row 2197 looks better kept as a no-index slice than indexed on the strength of encoding-plumbing fragments alone.
