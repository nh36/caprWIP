---
row_id: 2060
concept: hawk
counterpart: hafoc
proto: *xábukaz
protoform: *xábukaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2060 hawk / hafoc

## Current row state

- CONCEPT: `hawk`
- COUNTERPART: `hafoc`
- PROTO: `*xábukaz`
- PROTOFORM: `*xábukaz`
- DERIVATION_CLASS: `regular`
- Live TSV row 2060 currently has `PROTO = PROTOFORM = *xábukaz`, `COUNTERPART = hafoc`, `DERIVATION_CLASS = regular`, and no surviving row note in the row itself [Germanic/data/germanic-aligned-final.tsv:505-505].
- Coverage audit currently treats row 2060 as a regular row with no note, no report path, and no report requirement (`none`) [Germanic/docs/lexeme_reports/coverage_audit.md:266-268].
- `report_manifest.tsv` still contains only the pilot/report-backed rows and has no entry for 2060, so there is no manifest-linked report packet for this row yet [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` does not currently register `*xábukaz`/`hafoc` as an open OE exception bucket; the live problem list is occupied by other items such as `*búkkaz`, `*fūri`, and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- Current debug snapshots show the row as a clean success case: `# hawk / PROTO: *xábukaz / EXPECTED: hafoc / OUTPUTS: hafoc`, with the derivation `*xábuka > *xáboka > *xæbok > *çæbok > *çabok > *çaβok > hafoc` via medial unstressed `u > o`, Anglo-Frisian brightening, OE A-restoration, and regular orthography [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2460-2480; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6163-6216].

## Development-note summary

No row-specific DEV_NOTES block for hawk/hafoc survives in the current `DEV_NOTES.md`. The usable material is therefore conservative and mostly **shared-background-only**: (1) early diagnostic history showing that `*xabukăz` once failed the proto gate, (2) later A-restoration discussion that explicitly includes `hafoc` among textbook nominal outcomes with inherited medial `*u`, and (3) a source-comparison table that treats `hawk` as an inherited medial-`u` lexeme (`*habukaz` / `*xaƀukaz`) rather than as a paradigm-cell workaround or special exception [Germanic/docs/DEV_NOTES.md:2414-2425; Germanic/docs/DEV_NOTES.md:30235-30245; Germanic/docs/DEV_NOTES.md:30422-30505; Germanic/docs/DEV_NOTES.md:31316-31339].

For row 2060, the surviving DEV_NOTES substance supports a straightforward reading of the current trace, not a hidden controversy. The row behaves as a regular medial-`u` nominal: the medial vowel is already present before OE A-restoration, the root vowel passes through ordinary Anglo-Frisian brightening to `*æ`, and the following back-vowel environment then licenses restoration back to `a`, yielding the attested-looking OE surface `hafoc` after regular `b > β` orthographic development [Germanic/docs/DEV_NOTES.md:30241-30245; Germanic/docs/DEV_NOTES.md:30424-30505; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2471-2480].

The important row-level distinction is therefore narrow but real. `PROTO` and `PROTOFORM` are currently identical in the TSV (`*xábukaz`), and the surviving comparative DEV_NOTES material does not force a separate paradigm-cell `PROTOFORM`; instead it aligns hawk with comparative spellings `*habukaz` (Kroonen, R/T) and `*xaƀukaz` (Orel), all of which preserve the same medial `-u-` structure that the current OE derivation needs [Germanic/data/germanic-aligned-final.tsv:505-505; Germanic/docs/DEV_NOTES.md:31316-31339]. If later work wants deeper lexicographic/source cleanup, that would be a comparative-notation question, not evidence that the current OE derivation is unmodelled.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30235-30245

- Source heading: `§17.19.10.2.d R/T exemplar list of nominals with derivational suffixes containing *u* or *ō`
- Source line hint: `lines 30235-30245`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `shared_background_only`
- Issue tags: `medial_u`; `suffixal_u`; `A_restoration`; `parallel_nominals`
- Recommended next use: `cite when justifying that hawk already contains inherited medial *u before OE developments`
- Shared-with rows if relevant: `2133 (navel); other *-ul-/*-uk- A-restoration nominals`

This is the cleanest surviving DEV_NOTES mention of the hawk lexeme itself. In the navel/A-restoration dossier, the note says that Ringe–Taylor's list of “Nominals with derivational suffixes containing *u* or *ō*” includes `*habukaz > hafoc`, alongside `*sadulaz > sadol`, `*stapulaz > stapol`, and `*gabulu > gafol`; DEV_NOTES then draws the methodological conclusion that “All of these have an inherited (PNWGmc/PWGmc) medial *u* that R/T treat as present at the time of A-restoration” [Germanic/docs/DEV_NOTES.md:30235-30245]. For row 2060 this matters directly: the surviving note is not asking the reader to invent a later epenthetic vowel or a special OE-only insertion. It is saying that hawk belongs to the same inherited medial-`u` nominal class as the standard `-ul-/-uk-` textbook comparanda, so the live row's `PROTO = PROTOFORM = *xábukaz` remains structurally plausible even though DEV_NOTES' comparative spellings use `h/ƀ` rather than the TSV's normalized `x/b`.

### DEV_NOTES:line-30391-30505

- Source heading: `§17.19.2 The A-restoration rule itself`
- Source line hint: `lines 30391-30505`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `shared_background_only`
- Issue tags: `A_restoration`; `single_consonant_environment`; `Campbell_158`; `row_derivation`
- Recommended next use: `cite for the row's actual sound-law chain`
- Shared-with rows if relevant: `2133 especially; broader regular A-restoration rows`

This is the strongest surviving phonological support for row 2060. DEV_NOTES quotes Campbell's core rule statement: “The restoration of *a* is **common before all single consonants and geminates** ...” and then immediately makes the hawk application explicit in its own prose: “This covers *bacan, faran*; the textbook nominals **stapol, sadol, hafoc, gafol, latost** ...” [Germanic/docs/DEV_NOTES.md:30393-30403; Germanic/docs/DEV_NOTES.md:30424-30431]. The same section then inventories the relevant environment row by row and records `*hafoc* (V-f-uk) | single | restored: *a*` [Germanic/docs/DEV_NOTES.md:30497-30505]. For row 2060, this is the key working substance that replaces generic consultation of DEV_NOTES: hawk is not being treated as a cluster-edge case or an analogical rescue. The operative environment is a **single consonant** between the root vowel and the back-vowel trigger, exactly matching the current trace `*xæbok > *çæbok > *çabok` before regular `b` allophony and orthography produce `hafoc` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2471-2480].

### DEV_NOTES:line-31316-31339

- Source heading: `§17.19.10.2.e Comparison with parallel l-stems`
- Source line hint: `lines 31316-31339`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `shared_background_only`
- Issue tags: `comparative_sources`; `protoform_vs_proto`; `medial_u`; `reconstruction_notation`
- Recommended next use: `cite when discussing why no separate PROTOFORM is currently needed`
- Shared-with rows if relevant: `2133, 2030`

This fragment is source-audit background rather than a hawk-only decision block, but it is the surviving place where DEV_NOTES lines up the comparative reconstructions. In the parallel-stem table, hawk appears as `*habukaz` in Kroonen, `*habukaz` in R/T, and `*xaƀukaz` in Orel, with the final column marked `inherited` [Germanic/docs/DEV_NOTES.md:31316-31325]. DEV_NOTES then comments that Kroonen writes the medial `*u` overtly when the daughters show it consistently, and specifically includes `habukaz` among those overt-`u` headwords [Germanic/docs/DEV_NOTES.md:31331-31339]. For row 2060 this does two jobs. First, it supports preserving the distinction between the live TSV spelling `*xábukaz` and the comparative bibliography's `*habukaz/*xaƀukaz` without pretending they are different derivational objects. Second, it supports the conservative claim that no special row-local `PROTOFORM` has yet emerged from DEV_NOTES beyond the same medial-`u` stem already in the live data.

### DEV_NOTES:line-2414-2425

- Source heading: `Old English core refactor + diagnostics` / `PGmc→OE TODOs (consolidated)`
- Source line hint: `lines 2414-2425`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic`
- Issue tags: `proto_gate`; `no_output_history`; `early_pipeline_state`
- Recommended next use: `use only as project-history context`
- Shared-with rows if relevant: `2068, 2087, other early proto-gate failures`

This fragment preserves an early state that is no longer row policy but is still worth recording so later writers do not misread older debug files. During the OE-core refactor, DEV_NOTES listed remaining proto-input failures and named `*xabukăz` among them: “remaining ProtoInput failures are elsewhere (e.g., `*xabukăz`, `*xemenăz`, `*xnakkăz`, `*regna-bugōn`, `*sumerăz`)” [Germanic/docs/DEV_NOTES.md:2422-2425]. For row 2060 that is purely diagnostic history. It shows that hawk once lived in the `no_output` bucket during proto-gate cleanup, but it has been overtaken by the current compiled traces, which now derive `hafoc` cleanly end to end [Germanic/docs/non_firing_rules_analysis.md:463-478; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6163-6216].

## Superseded or diagnostic material

- The old proto-gate failure is superseded. DEV_NOTES' early TODO list still remembers `*xabukăz` as a ProtoInput reject, and `non_firing_rules_analysis.md` preserves the same state as ``*xabukăz -> +? (expected hafoc)``; neither reflects the current grammar, which now outputs `hafoc` with a transparent trace [Germanic/docs/DEV_NOTES.md:2422-2425; Germanic/docs/non_firing_rules_analysis.md:463-478; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:6163-6216].
- No dedicated hawk subsection survives in `DEV_NOTES.md`. The row should therefore be written up from shared A-restoration / medial-`u` material plus the live trace, not as though there were a lost hawk-only controversy dossier [Germanic/docs/DEV_NOTES.md:30235-30245; Germanic/docs/DEV_NOTES.md:30422-30505].
- Current repo bookkeeping does **not** treat hawk as an open exception row. It is absent from `oe_known_problems.tsv`, absent from the manifest-backed report list, and the coverage audit marks it as a regular row with no note and no report requirement [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/docs/lexeme_reports/coverage_audit.md:266-268].

## Open questions for later work

- If later lexeme-report work wants stricter bibliography alignment, decide whether prose should normalize the comparative form as `*habukaz` / `*xaƀukaz` while leaving the live TSV `PROTO`/`PROTOFORM` spelling `*xábukaz` untouched. The surviving DEV_NOTES evidence supports the medial-`u` structure, but not a mandatory spelling reform [Germanic/docs/DEV_NOTES.md:31316-31339; Germanic/data/germanic-aligned-final.tsv:505-505].
- If a packet or memo is later created for row 2060, it should make explicit that the useful DEV_NOTES support is shared-background-only. The strongest row-facing evidence is the Campbell/R/T A-restoration classification plus the current derivation trace, not a hawk-specific standalone note [Germanic/docs/DEV_NOTES.md:30235-30245; Germanic/docs/DEV_NOTES.md:30391-30505; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2460-2480].
- If final-report prose ever needs attestation-level lexical sourcing beyond the current derivational note, add direct dictionary/reference citations there; the surviving DEV_NOTES material for hawk is primarily phonological/classificatory, not a full attestation dossier.
