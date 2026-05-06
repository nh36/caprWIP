---
row_id: 2182
concept: shine
counterpart: sċīnan
proto: *skḯnaną
protoform: *skī́naną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2182 shine / sċīnan

## Current row state

- CONCEPT: `shine`
- COUNTERPART: `sċīnan`
- PROTO: `*skḯnaną`
- PROTOFORM: `*skī́naną`
- DERIVATION_CLASS: `regular`
- Live TSV row `2182` currently has no row-specific explanatory note; the operative row state is simply the regular OE row with `PROTO` `*skḯnaną`, `PROTOFORM` `*skī́naną`, and inherited source markers only [Germanic/data/germanic-aligned-final.tsv:977-977].
- `old_english_wiktionary.tsv` also maps English `shine` to OE `sċīnan`, so the target is the ordinary attested infinitive rather than a special analogical or reconstructed substitute [Germanic/data/old_english_wiktionary.tsv:243-243].
- Coverage audit still treats row `2182` as a regular row with no NOTE and no required lexeme report (`Requirement basis: none`), which explains the blank packet/memo metadata in this slice [Germanic/docs/lexeme_reports/coverage_audit.md:348-348].
- The current published derivation trace is stable and fully successful: `PROTO: *skḯnaną`, `EXPECTED: sċīnan`, `OUTPUTS: sċīnan`, with the OE-side chain reducing to `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, `OE Sk Palatalization`, and `OE Weak Tail Reduction` before orthography `sċīnan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4121-4141].

## Development-note summary

The surviving DEV_NOTES material for row `2182` is real but thin. It does **not** preserve a shine-specific argument about disputed reconstruction, analogical replacement, or a row-level exception. Instead, it preserves two narrower kinds of evidence: first, an older diagnostic showing that this row once appeared among near-miss orthography cases; second, a later notation-migration/verification note showing that the row remained correct after stressed-root long `*ī` was re-encoded as `*ḯ` in OE-facing inputs [Germanic/docs/DEV_NOTES.md:2614-2621,42006-42040].

The older diagnostic should be read carefully. In the 2026-01-02 mismatch-closeness note, DEV_NOTES says the normalized-distance report included `*skīnăną → scīnan` versus expected `sċīnan`, and immediately classifies the cluster as “orthography/diacritic alignment issues rather than phonology failures” [Germanic/docs/DEV_NOTES.md:2618-2621]. That is important because it shows the row was already behaving like a **successful phonological derivation** at that stage: the only defect recorded there was plain `sc` versus editorial `sċ`, not a wrong vowel, wrong stem class, or wrong suffix. The matching 2026-02-07 full trace confirms that interpretation: the earlier pipeline form `*skīnăną` goes straight through palatalisation and weak-tail processing to orthographic `sċīnan` with no compensatory repair step [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_short_o_fix.txt:4083-4129].

The later DEV_NOTES material is about notation policy, not about a new historical stage. Phase 4 of the `*ḯ` migration states that 16 OE rows had `*ī` in `PROTOFORM`, of which 15 were really stressed-root long `*ī` and were therefore migrated to `*ḯ`; row `2182` appears in Batch 3 as `rīdan, sċīnan, sīde`, with the explicit verification gloss “palatalization on *ḯ ✓”, and the verification probe repeats `skḯnaną → sċīnan` [Germanic/docs/DEV_NOTES.md:42010-42040]. In other words, the DEV_NOTES evidence does **not** say that `*skīnăną`, `*skḯnaną`, and `*skī́naną` are three chronologically different lexical reconstructions. The evidence instead shows three notation layers used by the project at different times for different purposes:

- earlier diagnostic/live-input notation: `*skīnăną`, where stressed root long `ī` had not yet been migrated to `ḯ` and the infinitive tail still used the older breve-marked engineering notation [Germanic/docs/DEV_NOTES.md:2620-2621; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_short_o_fix.txt:4083-4129];
- current OE-pipeline `PROTO`: `*skḯnaną`, where stressed-root long `ī` is marked as `ḯ` specifically because the 2026 migration separated stressed-root long `ī` from the unstressed `*ī` cases that certain rules still need to see [Germanic/docs/DEV_NOTES.md:41977-42015,42017-42040; Germanic/data/germanic-aligned-final.tsv:977-977];
- current lexical/cognate-set `PROTOFORM`: `*skī́naną`, the acute-accent canonical form retained in the aligned TSV alongside the OE-directed `PROTO` input [Germanic/data/germanic-aligned-final.tsv:977-977].

That distinction matters because otherwise the row can be misread as if the project were vacillating between competing proto-forms. The surviving evidence points the other way. An older backup of the aligned TSV used the undifferentiated form `*skīnăną`, while the live row now splits the information between `PROTO *skḯnaną` and `PROTOFORM *skī́naną`; the attested OE target `sċīnan` stayed unchanged across that cleanup [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:977-977; Germanic/data/germanic-aligned-final.tsv:977-977]. For this row, then, the durable working conclusion is simple but precise: `shine / sċīnan` is a **regular control row** whose DEV_NOTES footprint is mostly diagnostic history plus successful notation migration, not a substantive lexeme-specific controversy.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2614-2621

- Source heading: `OE diagnostics: mismatch closeness + diacritics (2026-01-02)`
- Source line or section hint: `lines 2614-2621`
- fragment_type: `diagnostic_only`
- current_status: `diagnostic_only`
- Issue tags: `orthography_alignment`; `palatalization`; `notation_history`; `protoform_vs_proto`
- recommended_next_use: `use_as_project_history_only`
- Shared with row IDs:

This fragment is the earliest surviving DEV_NOTES attachment for `shine`, and it is explicitly diagnostic rather than prescriptive. DEV_NOTES says the normalized-distance file “lists 11 cases where normalized (diacritic-stripped) distance is 0,” giving `*skīnăną → scīnan` vs expected `sċīnan` as one example, then adds that the diacritic-mismatch traces “confirm these are orthography/diacritic alignment issues rather than phonology failures” [Germanic/docs/DEV_NOTES.md:2620-2621]. For row `2182`, that wording is the main point to preserve. It shows that the older issue was not a failed derivation of OE long `ī` or a failure to palatalize inherited `sk`; it was a surface-notation mismatch in an otherwise correct run.

The older notation inside the fragment is also worth keeping, but only with the right label. `*skīnăną` belongs to the project's pre-migration engineering notation, not to a rival historical reconstruction that should compete with the current row. The fragment therefore helps mainly with provenance: before the later `*ḯ` migration and before the current publication formatting, this row already behaved as a near-miss/control item rather than as an OE exception requiring row-level intervention.

### DEV_NOTES:line-41977-42040

- Source heading: `TSV migration (Phase 4)` plus `Verification`
- Source line or section hint: `lines 41977-42040`
- fragment_type: `current_verification`
- current_status: `current`
- Issue tags: `long_vowel_notation`; `palatalization`; `verification_history`; `protoform_vs_proto`
- recommended_next_use: `cite_if_row_policy_needs_notation_explanation`
- Shared with row IDs: `2153`, `2188`, `2257`

This is the controlling current DEV_NOTES fragment for row `2182`, even though it is still shared rather than row-local. DEV_NOTES first defines the policy distinction that motivated the migration: stressed-root long `*ī` rows were moved to `*ḯ`, while the single genuinely unstressed long-`*ī` suffix case was left alone because `NWGmcInStemNLoss` still has to consume it [Germanic/docs/DEV_NOTES.md:41977-42015]. Row `2182` is then named directly in Batch 3, and the gloss attached to `sċīnan` is specific: “palatalization on *ḯ ✓” [Germanic/docs/DEV_NOTES.md:42017-42025]. The verification block repeats the probe as `skḯnaną → sċīnan` [Germanic/docs/DEV_NOTES.md:42031-42040].

For this slice, the fragment's value is twofold. First, it establishes that the live `PROTO` spelling `*skḯnaną` is not ad hoc; it comes from a repo-wide notation cleanup with an explicit rule/rationale. Second, it shows exactly what later reviewers are supposed to trust about row `2182`: once the stressed-root `*ī` rows were re-encoded as `*ḯ`, this row still passed, and the property explicitly checked for it was palatalization. That is useful evidence, but it remains verification evidence rather than a full philological dossier.

## Superseded or diagnostic material

- The older `*skīnăną → scīnan` diagnostic should not be cited as current row policy. It belongs to an earlier notation regime and to an orthography-focused mismatch scan; its lasting value is only that DEV_NOTES itself classed the problem as diacritic alignment rather than phonological failure [Germanic/docs/DEV_NOTES.md:2618-2621].
- The form-pair `*skīnăną` / `*skḯnaną` / `*skī́naną` should not be turned into a false chronology of three historical stages. For this row the evidence supports a tooling/policy distinction: earlier unified engineering notation, current OE-facing migrated `PROTO`, and current canonical/cognate-set `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:977-977; Germanic/data/germanic-aligned-final.tsv:977-977; Germanic/docs/DEV_NOTES.md:41977-42040].
- The shared Batch 3 migration note is useful but narrow. It confirms that row `2182` survived notation cleanup and still palatalizes correctly; it does **not** by itself supply a lexeme-specific source discussion, semantic discussion, or argument for index integration.

## Open questions for later work

- If a future final report wants this row indexed, it will need more than the current DEV_NOTES residue: ideally a row-specific source audit explaining the canonical `PROTOFORM`/OE-facing `PROTO` split in one place, rather than relying on a shared migration log and an old diagnostic note.
- If no such additional material is assembled, this row is best kept as a **no-index slice**: the surviving evidence is accurate and worth preserving, but mostly shared verification plus stale diagnostics rather than standalone lexeme analysis.
- If later documentation cites this row as a successful control case for `sk > sċ` before front vocalism, pair the current publish trace with the Phase 4 migration note so readers can see both the live derivation and the reason `*ḯ` is now used in the OE input.
