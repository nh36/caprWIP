---
row_id: 2246
concept: thief
counterpart: þēof
proto: *θéubaz
protoform: *θéubaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2246 thief / þēof

## Current row state

- CONCEPT: `thief`
- COUNTERPART: `þēof`
- PROTO: `*θéubaz`
- PROTOFORM: `*θéubaz`
- DERIVATION_CLASS: `regular`
- Live TSV row: the current Old English row keeps `PROTO = *θéubaz`, `COUNTERPART = þēof`, and `DERIVATION_CLASS = regular`; the source column contains only inherited-etymology placeholders rather than a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:1225-1225].
- Existing row infrastructure: `coverage_audit.md` still records row 2246 as having no packet, no memo, no attached DEV_NOTES fragment, and no other report infrastructure to reuse, so the canonical row-based filename is appropriate for this slice [Germanic/docs/lexeme_reports/coverage_audit.md:390-390].
- Known-problems status: no row-specific `oe_known_problems.tsv` entry was needed for this pass; nothing in the current repo marks row 2246 as an exception bucket or unresolved mismatch.
- Current implementation trace: the published derivation snapshot already returns the live target without repair — `*θéubaz` > `*θéuba` (final `-z` deletion) > `*θēoba` (OE diphthong leveling) > `*θēob` (final bare `-a` loss) > `*θēoβ` (PGmc `b` allophony) > `þēof` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5172-5192].

## Development-note summary

No lexeme-specific DEV_NOTES dossier for `þēof` survives in the live file, and that absence matters: the replacement working note should not invent a row history that the project never actually wrote down. The usable DEV_NOTES support is instead **shared sound-change material** confirming that inherited stressed PGmc `*eu` normally yields OE `ēo`, plus the fact that no DEV_NOTES passage flags `*θéubaz > þēof` as problematic. Given the live row state, that thin/shared support is enough to keep the row conservative and straightforward rather than to promote it into an indexed exception narrative [Germanic/data/germanic-aligned-final.tsv:1225-1225; Germanic/docs/lexeme_reports/coverage_audit.md:390-390].

The central philological point is simple and should stay simple. `PROTO` is the comparative headword `*θéubaz` / `*þeubaz` ‘thief’; `PROTOFORM` is the same form because no paradigm-cell substitution, alternate input, or repair preform is currently in play; and `COUNTERPART` is the regular Old English reflex `þēof`, not a special analogue or a reconstructed substitute target [@Orel2003, p. 422; @Kroonen2013; Germanic/data/germanic-aligned-final.tsv:1225-1225]. Orel lists `*þeubaz sb.m.` with OE `ðeóf`, and Kroonen likewise gives Proto-Germanic `*þeuba-` with OE `þēof`, so the lexical equation itself is not controversial [@Orel2003, p. 422; @Kroonen2013]. Clark Hall also preserves the OE noun entry (`deof I. ... 'thief, robber'`), which is enough for this slice's limited purpose even though the OCR normalizes thorn/eth inconsistently [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:42503-42504].

The shared DEV_NOTES material that actually bears on row 2246 is the project's explicit use of `*eu > ēo` as a regular OE outcome. In the `brēost` note, DEV_NOTES states that Campbell confirms `brēost` as an example of the `*eu > ēo` outcome and treats that sound law as sufficient to justify a regular derivation from `*breustą` to OE `brēost` [DEV_NOTES:line-5968-6005; @Campbell1959, §115]. Later, while discussing a different lexeme family, DEV_NOTES restates the same principle in even plainer terms: PGmc `*eu` “would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [DEV_NOTES:line-43943-43949]. Row 2246 needs exactly that shared rule and nothing more exotic: once `*θéubaz` is accepted as the input, the appearance of `ēo` in `þēof` is the expected OE development, not a special-case repair [@Campbell1959, §115; @RingeTaylor2014].

The current trace aligns cleanly with that reading. Ringe and Taylor explicitly list `PGmc *peubaz 'thief' ... > OE péof`, which matches the live row's regular classification and the FST's current output [@RingeTaylor2014; docs/references/ringe_taylor_linguistic_history_vol2.txt:10064-10068]. The derivation snapshot then spells out the mechanics the project is actually using: inherited `*éu` levels to `ēo`, final `-z` and bare final `-a` are removed in the ordinary way, and intervocalic/postvocalic `b` surfaces as `f` orthographically after the usual allophonic stage `β` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5179-5192]. Nothing in DEV_NOTES contradicts that pathway for this lexeme, and nothing in the current repo suggests that `þēof` should be treated as anything other than the regular OE target.

The main practical conclusion is therefore negative but important: row 2246 does **not** presently have the kind of row-local project chronology that would justify indexed lexeme-report infrastructure. The useful note content is real, but it is shared and generic — inherited `*eu > ēo`, ordinary noun continuation, ordinary FST success. The slice should preserve that fact explicitly so later work does not mistake the absence of a big DEV_NOTES section for missing philology. The evidence is enough to support the live row, but it is not enough to claim a row-specific DEV_NOTES argument beyond “regular reflex, no exception identified” [Germanic/docs/lexeme_reports/coverage_audit.md:390-390; DEV_NOTES:line-5968-6005,43943-43949].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-5968-6005

- Source heading: `Campbell (1959) §115 (OE breaking)` within the `brēost` note
- Source line or section hint: `lines 5968-6005`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `inherited_eu_to_eo`; `shared_sound_change`; `regular_reflex`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is not about `þēof` by name, but it is current and genuinely relevant because it states the exact shared sound law row 2246 depends on. DEV_NOTES says that Campbell confirms `brēost` as an example of the `*eu > ēo` outcome and uses that point to defend a regular OE derivation from a `*breust-` input [DEV_NOTES:line-5970-5989; @Campbell1959, §115]. For row 2246 the value of the fragment is narrow but real: it supports treating the `ēo` of `þēof` as ordinary inherited development from PGmc `*eu`, not as analogical distortion or a target-selection patch.

### DEV_NOTES:line-43943-43949

- Source heading: `Origin of the 3pl pret. choice`
- Source line or section hint: `lines 43943-43949`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `shared_sound_change`; `regular_oe_eo`; `comparator_bēogan`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This later fragment is useful because it restates the same rule in a way that is directly portable to row 2246. DEV_NOTES says that the long `ū` of `būgan/sċūfan` is an OE innovation, “NOT from PGmc *eu, which would regularly give OE *ēo — cf. *béuganą → bēogan attested in early Anglian” [DEV_NOTES:line-43946-43949]. For `*θéubaz > þēof`, that sentence is exactly the needed project-level precedent: inherited PGmc `*eu` belongs with regular OE `ēo`, so the row does not need a special note beyond correct identification of the proto input.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES analysis was located for `þēof`. The absence of a local controversy is itself part of the row's current status: there is no preserved project history of protoform swapping, alternate counterpart selection, or exception triage to carry forward.
- The published derivation trace is useful diagnostic support, but it is not a DEV_NOTES fragment and should not be mistaken for one. Its value is implementation-facing: it shows that the current cascade already derives `þēof` from `*θéubaz` without workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5172-5192].
- `coverage_audit.md` is also diagnostic rather than argumentative. Its `none` entry for row 2246 correctly reflects the present state of the repo: no packet stem, no memo stem, no prior attached fragment, and therefore no reason to pretend that this row already has deeper lexeme-local DEV_NOTES support than it actually does [Germanic/docs/lexeme_reports/coverage_audit.md:390-390].

## Open questions for later work

- If later indexing work wants row 2246 represented in `index.tsv`, decide whether shared `*eu > ēo` fragments alone are enough to justify indexing, or whether the row should stay unindexed until a more lexeme-specific report need appears.
- If a future lexeme report is written, add a cleaner dictionary citation for exact headword `þēof` from repo reference files; the OCR extracts currently make Clark Hall easier to quote than Bosworth-Toller for this lexeme.
- If later DEV_NOTES work creates a consolidated shared note on inherited PGmc `*eu` outcomes in OE, row 2246 would be a natural example to attach there alongside `brēost` and `bēogan`.
