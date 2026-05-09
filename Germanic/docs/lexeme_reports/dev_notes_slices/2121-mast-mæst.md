---
row_id: 2121
concept: mast
counterpart: mæst
proto: *mástaz
protoform: *mástaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt
  - Germanic/docs/germanic_notes/oe_a_restoration_debug.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2121 mast / mæst

## Current row state

- The live OE row is stable and minimal: `row_id = 2121`, `CONCEPT = mast`, `COUNTERPART = mæst`, `PROTO = *mástaz`, `PROTOFORM = *mástaz`, `DERIVATION_CLASS = regular`. `PROTO`/`PROTOFORM` therefore still coincide, while the attested OE-side target remains the distinct counterpart `mæst`; the row carries no manual note, only duplicated imported provenance (`template:der`) in `HISTORY` [Germanic/data/germanic-aligned-final.tsv:741-741].
- `oe_known_problems.tsv` has no entry for row `2121`, for `*mástaz`, or for `mæst`, so this lexeme is not currently bucketed as an exception, unresolved mismatch, or known OE defect [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/audit infrastructure still treats the row as an uncovered-but-unproblematic regular item: `| 2121 | mast | mæst | regular | no | - | - | - | none |`. `report_manifest.tsv` still lists only pilot rows, so there is no packet, memo, or legacy report to inherit here [Germanic/docs/lexeme_reports/coverage_audit.md:305-307; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current derivation snapshots are a clean match. The compact and lexeme-report traces both give `PROTO: *mástaz`, `EXPECTED: mæst`, `OUTPUTS: mæst`, with only three displayed changes: `PGmc Final Z Deletion: *másta`, `PWGmc Final Bare A Loss: *mást`, and `Anglo Frisian Brightening: *mæst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3686-3705; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:3464-3483].
- The fuller trace confirms that nothing else is secretly doing work on this row. After `ProtoInput: *m*á*s*t*a*z`, every stage is `[no-change]` except `PGmcFinalZDeletion`, `PWGmcFinalBareALoss`, and `AngloFrisianBrightening`; `OEARestoration` is explicitly `[no-change]`, and the surface stage is simply `mæst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17915-18021].

## Development-note summary

No dedicated mast-specific DEV_NOTES essay survives. The only row-specific DEV_NOTES residue located for this lexeme is diagnostic: a failed March 2026 A-restoration experiment that temporarily regressed `mastăz` to `mast` and explicitly logged that as wrong [Germanic/docs/DEV_NOTES.md:9520-9565]. That fragment is useful because it proves the row was once used as a canary for overfiring A-restoration, but it is not the row’s current analysis.

The conservative replacement note is therefore built from shared-background DEV_NOTES chronology plus the live successful trace. On current evidence, row 2121 is an ordinary regular derivation: `*mástaz > *másta > *mást > *mæst`, i.e. final `*-z` deletion, then final bare `*-a` loss, then Anglo-Frisian brightening of stressed `*á` to `*æ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:3471-3483; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17932-18021].

Shared DEV_NOTES background is enough to say why this works. The current notes insist that final short low vowels were lost in PWGmc before later OE brightening, and that original PGmc suffixal `*a` does **not** count as a back-vowel trigger for A-restoration once it has fronted or disappeared; only genuine back suffix vowels such as `*o`/`*u` trigger restoration [Germanic/docs/DEV_NOTES.md:21434-21439,3171-3178]. For `*mástaz`, that means there is no reason to retract the brightened root vowel back to `a`; the matched output `mæst` is exactly what the current rule ordering predicts.

Support classification for this slice should stay explicit. **Row-specific support:** only the superseded regression note `mastăz → mast (should be mæst) - REGRESSED` [Germanic/docs/DEV_NOTES.md:9524-9539]. **Shared-background-only support:** yes, especially the z-loss chronology, final-`*a` chronology, and A-restoration conditioning notes [Germanic/docs/DEV_NOTES.md:3459-3494,21407-21439,3171-3178]. **Diagnostic support:** yes, the full trace and the older A-restoration debug memo show what breaks when weak-tail `*a/*ă` is mishandled [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17915-18021; Germanic/docs/germanic_notes/oe_a_restoration_debug.md:26-65].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3459-3494

- Source heading: `Historical phonology of final *-z loss and its interaction with rhotacism`
- Source line hint: `lines 3459-3494`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `final_z_loss`; `weak_tail_chronology`; `regular_a-stem_tail`
- Recommended next use: `cite_when_explaining_why_*mástaz_first_becomes_*másta_with_no_intermediate_r-stage`
- Shared-with rows if relevant: `regular OE *-az rows with matched outputs`

This fragment is not about mast specifically, but it supplies the first half of the row’s live derivation. The preserved quotation is decisive: “On the WGmc side, the loss of word-final *z in unstressed syllables ... must likewise have preceded the merger of *z with *r,” followed by the project’s summary, “Final *-z was **never rhotacized**. It was already gone by the time rhotacism occurred” [Germanic/docs/DEV_NOTES.md:3463-3477]. For row 2121 the practical substance is simple: the final consonant of `*mástaz` is directly deleted to give `*másta`, exactly as the live trace now shows, and nothing row-specific suggests a special exception or alternate paradigm-cell input here [Germanic/docs/DEV_NOTES.md:3471-3494; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:3471-3478].

Because mast has no medial `*z` and no inherited `*r` issue, the rhotacism discussion itself is background only. What survives for this row is the ordering claim and the direct consequence that the weak tail begins collapsing with `*-az > *-a`, not with any hypothetical `*-ar` intermediate [Germanic/docs/DEV_NOTES.md:3471-3494].

### DEV_NOTES:line-21407-21439

- Source heading: `§17.10.5 — Phase 1b (Role 3) research findings: AFB chronology blocks naive rule-target migration`
- Source line hint: `lines 21407-21439`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `final_bare_a_loss`; `AFB_chronology`; `weak_tail_deletion_before_brightening`
- Recommended next use: `cite_when_explaining_why_the_tail_*a_of_*mástaz_does_not_survive_to_trigger_later_OE_effects`
- Shared-with rows if relevant: `other regular rows whose successful output depends on PWGmc final bare a loss`

This fragment matters because it preserves the historical ordering that the current mast trace now instantiates. DEV_NOTES quotes R/T: “Another sweeping sound change that characterizes all WGmc languages is the loss of unstressed *a and *ą word-finally and before final *-z. ... the loss of word-final short low vowels was clearly a **PWGmc change**” [Germanic/docs/DEV_NOTES.md:21434-21439]. The surrounding prose explains why a naive migration broke words like `weþer`: by the time OE Anglo-Frisian brightening runs, a word-final weak-tail `*a` should already be gone, not still available as live material for later fronting [Germanic/docs/DEV_NOTES.md:21415-21433].

Applied conservatively to row 2121, the fragment says the tail vowel of `*másta` should disappear before any later OE-stage interpretation of a remaining suffix vowel. That is exactly what the trace shows: `PGmc Final Z Deletion: *másta`, then `PWGmc Final Bare A Loss: *mást`, leaving only the stressed root vowel to undergo brightening [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:3475-3483].

### DEV_NOTES:line-3171-3178

- Source heading: `A-restoration in ō-stems and n-stems: ræst, tæppa, stemn`
- Source line hint: `lines 3171-3178`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `A-restoration`; `suffix_vowel_quality`; `fronting_vs_restoration`
- Recommended next use: `cite_when_explaining_why_mast_should_brighten_to_mæst_and_not_be_retracted_back_to_a`
- Shared-with rows if relevant: `day`; `craft`; `staff`; other fronting/restoration-sensitive rows

This fragment is the clearest surviving statement of the conditioning distinction that protects row 2121 in the current system. DEV_NOTES states: “The critical insight comes from R/T's paradigm of ‘dæg’,” then summarizes the rule as: “Principle: **original PGmc *a in suffixes is fronted by AFB and does NOT trigger restoration. Original PGmc *o, *u in suffixes stay back and DO trigger restoration**” [Germanic/docs/DEV_NOTES.md:3173-3178]. That principle is shared background, but it is directly applicable here.

For `*mástaz`, the suffix vowel is the ordinary thematic `*a`, not a back-vowel trigger like `*o` or `*u`. Once `*-z` is deleted and final bare `*-a` is lost, there is no surviving back vowel in the tail that could justify `OEARestoration`; the full trace’s explicit `OEARestoration [no-change]` on `*m*æ*s*t` is therefore the expected outcome, not an accidental one [Germanic/docs/DEV_NOTES.md:3173-3178; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17964-17970].

### DEV_NOTES:line-9520-9565

- Source heading: `Empirical Validation (Dry Run 2026-03-13)`
- Source line hint: `lines 9520-9565`
- Fragment type: `diagnostic`
- Status: `superseded`
- Issue tags: `row_specific_regression_witness`; `A-restoration_overgeneralization`; `fronting_missing__afb`
- Recommended next use: `cite_only_when_explaining_a_failed_experiment_that_temporarily_broke_row_2121`
- Shared-with rows if relevant: `craft`; `day`; `raven`; `staff`; `tap`; `wain`; `lap`; `wasp`

This is the only surviving DEV_NOTES fragment that names the row directly, and it survives only as failure logging. The crucial quotation should be preserved exactly: `mastăz → mast (should be mæst) - REGRESSED` [Germanic/docs/DEV_NOTES.md:9524-9528]. The same block diagnoses the failure as “**phonological overgeneralization**”: adding `{*ă}` to `OEARestorationTriggerVowel` made A-restoration fire for “ALL forms with `{*ă}` in suffix position — including a-stem nouns like `*kraftăz` where the suffix `{*ă}` is just a thematic vowel before `*-z`” [Germanic/docs/DEV_NOTES.md:9541-9553].

For row 2121, this diagnostic fragment is useful precisely because it is superseded. It does **not** mean mast needs an exception analysis; it means the failed experiment incorrectly turned a regular fronting case into `mast`. The row-specific residue here is therefore a warning label for future rule edits: if a proposed A-restoration change again causes `*mástaz`/`mastăz` to surface as `mast`, the edit has reintroduced the same overgeneralization already rejected in March 2026 [Germanic/docs/DEV_NOTES.md:9524-9565; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md:3464-3483].

## Superseded or diagnostic material

- No mast-specific explanatory block survives in DEV_NOTES beyond the regression log. The replacement slice therefore should not pretend that there was once a dedicated mast memorandum; the surviving row-specific evidence is just the failed-note witness `mastăz → mast (should be mæst) - REGRESSED` [Germanic/docs/DEV_NOTES.md:9524-9539].
- The older A-restoration debug memo is diagnostic background, not row argumentation. Its probe `*b*a*s*t*ą` “**does** A-restore to `*a`, even though `*ą` should be weak-tail,” which is valuable because it documents the same blocker failure family that later harmed mast-like forms during experimental rewrites, but it is not row-2121-specific evidence [Germanic/docs/germanic_notes/oe_a_restoration_debug.md:26-33,56-65].
- The current debug traces supersede the regression state. They now agree that the row is fully regular and matched, with only z-loss, bare-a loss, and brightening active; `OEARestoration` is a no-op for the current row [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3686-3705; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:17964-18021].
- `coverage_audit.md` remains workflow-diagnostic only. Its `none` status means “no report required under current coverage rules,” not “no useful row history exists”; for this slice, it mainly records that documentation had not previously been broken out into a row file [Germanic/docs/lexeme_reports/coverage_audit.md:305-307].

## Open questions for later work

- If later packetization wants more than this conservative slice, the missing ingredient is a genuine row-local philological note or external lexical dossier for OE `mæst`; current project-history evidence is mostly about rule ordering, not about lexical semantics or attestation depth.
- Any future A-restoration or Anglo-Frisian-brightening refactor should re-test row 2121 explicitly. The March regression note shows that `mast / mæst` is a good canary for unwanted restoration over weak tails [Germanic/docs/DEV_NOTES.md:9524-9565].
- If future documentation distinguishes more sharply between comparative lemma format and project input notation, keep the labels separate: `PROTO` and `PROTOFORM` currently remain the project input `*mástaz`, while `COUNTERPART` is the OE target `mæst` [Germanic/data/germanic-aligned-final.tsv:741-741].
