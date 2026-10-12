---
row_id: 2021
concept: flood
counterpart: flōd
proto: *flōduz
protoform: *flōduz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2021 flood / flōd

## Current row state

- CONCEPT: `flood`
- COUNTERPART: `flōd`
- PROTO: `*flōduz`
- PROTOFORM: `*flōduz`
- DERIVATION_CLASS: `regular`
- The live Old English row currently keeps `*flōduz` as both `PROTO` and `PROTOFORM`, with `flōd` as the OE counterpart and no row-local explanatory note beyond duplicated inherited-etymology placeholders in the source/history columns [Germanic/data/germanic-aligned-final.tsv:351-354].
- The lexical pairing itself is present in the repo's OE wordlist as `flood -> flōd` with an inherited-etymology tag, so the current slice does not need to argue for a replacement counterpart; it only needs to preserve what DEV_NOTES actually says about the row's project history [Germanic/data/old_english_wiktionary.tsv:86-86].
- `coverage_audit.md` still lists row 2021 as uncovered (`no` packet, no memo, no attached fragment, `none`), and `report_manifest.tsv` has no row-2021 entry; there is therefore no pre-existing packet stem to override the canonical filename used here [Germanic/docs/lexeme_reports/coverage_audit.md:244-244; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no entry for `*flōduz` or `flōd`, which matches the current implementation state: the row is not presently tracked as an exception bucket or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace already returns the live target cleanly: `PROTO: *flōduz`, `EXPECTED: flōd`, `OUTPUTS: flōd`, with the effective path `PGmc Final Z Deletion: *flōdu` > `OE High Vowel Apocope: *flōd` > `Outcome: flōd` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1423-1442].

## Development-note summary

No dedicated lexeme dossier for `flood / flōd / *flōduz` survives in `DEV_NOTES.md`. The row's usable DEV_NOTES material is much narrower: one row-explicit diagnostic table showing that `*flōduz` briefly regressed to `flōdo`, plus the shared follow-up analysis explaining why that happened and why the project expected the problem to disappear once final `*-z` deletion was moved back to an earlier stage [Germanic/docs/DEV_NOTES.md:24443-24524].

That distinction matters for how this slice should be read. `COUNTERPART = flōd` is the live OE target and the current trace already reaches it directly; `PROTO` and `PROTOFORM` both remain `*flōduz`; and DEV_NOTES does **not** preserve a rival protoform, an analogical rescue, or a claim that `flōd` is only a reconstructed substitute target. The only row-explicit DEV_NOTES note for this lexeme is diagnostic and superseded: in the §17.10.25 regression table the row appears as `*flōduz | flōdo | flōd`, i.e. a stray final vowel remained after a chronology change [Germanic/docs/DEV_NOTES.md:24451-24459].

The shared explanation is more substantial than the row-explicit one. DEV_NOTES says the reordered pipeline let `OEMedUnstressedULowering` see word-final `*-uz` as if it were medial because `PGmcFinalZDeletion` had been moved too late; in that configuration, the short `*u` of forms like the `*CVCuz` cohort lowered to `*o`, so later cleanup yielded outputs like `flōdo` instead of the expected apocopated `flōd` [Germanic/docs/DEV_NOTES.md:24466-24490]. DEV_NOTES then states the project remedy in chronology terms: z-loss belongs after final-`ō` raising but before OE-stage rules such as `OEMedUnstressedULowering`, so that “the ‘OE stage’ begins with word-final *-z already gone” [Germanic/docs/DEV_NOTES.md:24500-24524].

For row 2021, then, the replacement note should stay conservative. The row is currently regular and currently successful, but the DEV_NOTES support is mostly shared implementation chronology rather than a lexeme-specific philological discussion. What survives is enough to explain why `flōdo` once appeared and why the project does **not** treat that form as a competing OE target; it is not enough to claim a deeper row-local DEV_NOTES argument beyond “regular `*flōduz > flōd`, with one now-superseded *CVCuz regression during z-loss reordering work” [Germanic/docs/DEV_NOTES.md:24443-24524; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1423-1442].

## Relevant DEV_NOTES fragments

### DEV_NOTES:24443-24459

- Source heading: `1. Probe outcome (vs. post-§17.10.23 baseline of 38)`
- Source line or section hint: `lines 24443-24459`
- Fragment type: `row_explicit_diagnostic_table`
- Status: `superseded_but_row_specific`
- Issue tags: `cvcuz_regression`; `stray_final_vowel`; `z_loss_ordering`
- Recommended next use: `cite_as_project_history_only`
- Shared with row IDs: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This is the one place where row 2021 is named directly in surviving DEV_NOTES material. The probe summary says there were “Eight **new** mismatches, all sharing the shape *CVCuz,” and the table includes the exact row-local line `| *flōduz | flōdo | flōd |` [Germanic/docs/DEV_NOTES.md:24451-24459]. For this slice, that explicit line needs to be preserved because it is the clearest evidence that `flōdo` was a transient debug output, not a philological proposal for the row.

The diagnostic value is precise. At this stage the project had already kept the inherited long vowel `ō` and the stem-final `d`; the remaining mismatch was the unwanted final `-o`. So the fragment should be read narrowly: it records a chronology regression in final-vowel handling, not doubt about the OE counterpart `flōd`, not a reopened debate over `PROTOFORM`, and not any claim that row 2021 required analogical repair [Germanic/docs/DEV_NOTES.md:24453-24464].

### DEV_NOTES:24466-24490

- Source heading: `2. Root-cause: z-loss fires too late, spoofing OEMedUnstressedULowering`
- Source line or section hint: `lines 24466-24490`
- Fragment type: `shared_root_cause_analysis`
- Status: `diagnostic_but_still_explanatory`
- Issue tags: `oemedunstressedulowering`; `pgmc_final_z_deletion`; `false_medial_u`; `shared_cvcuz_cohort`
- Recommended next use: `cite_when_explaining_why_flōdo_is_not_a_real_target`
- Shared with row IDs: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This shared fragment contains the actual mechanism behind row 2021's brief failure. DEV_NOTES quotes the lowering rule as ``{*u} -> {*o} || [V - u/ū] C+ _ C`` and explains that the rule should only affect truly medial unstressed `*u`; after §17.10.24's reorder, however, word-final `*-uz` still retained a real final `*z` when `OEMedUnstressedULowering` ran, so the rule misread the vowel as if “some consonant follows” and lowered it [Germanic/docs/DEV_NOTES.md:24468-24482].

Even though the worked example in the prose is `*bébruz`, the note explicitly generalizes the problem: “Ten different forms fail for this exact reason” [Germanic/docs/DEV_NOTES.md:24480-24489]. Row 2021 belongs to that cohort. Applied to `*flōduz`, the same logic explains the stray `-o`: if `*-z` survives too long, the word-final high vowel is no longer protected as final `*u`, and the pipeline is pushed toward `flōdo` instead of preserving `*flōdu` long enough for the expected apocope to yield `flōd`.

### DEV_NOTES:24500-24524

- Source heading: `4. Proposed fix — tighten z-loss to PWGmc stage, not OE stage`
- Source line or section hint: `lines 24500-24524`
- Fragment type: `shared_fix_rationale`
- Status: `current_shared_policy`
- Issue tags: `chronology_repair`; `z_loss_before_oe_rules`; `expected_resolution`
- Recommended next use: `cite_with_current_trace_as_confirmation`
- Shared with row IDs: `1941, 1960, 2009, 2021, 2048` and the then-unrepaired pre-correction row `1983`

This fragment is the best surviving DEV_NOTES statement of why row 2021 is now back in the regular bucket. DEV_NOTES says `PGmcFinalZDeletion` should fire “immediately after raising” in the PNWGmc/PWGmc cluster, not down in the OE cluster, because OE-stage rules such as `OEMedUnstressedULowering` must see z-free inputs [Germanic/docs/DEV_NOTES.md:24502-24524]. The most portable sentence for later report prose is the closing one: the reorder restores the chronology in which “the ‘OE stage’ begins with word-final *-z already gone” [Germanic/docs/DEV_NOTES.md:24521-24524].

For row 2021 this remains shared rather than lexeme-specific support, but it is still important. It explains why the current trace again shows the simple path `*flōduz > *flōdu > *flōd` and why the row no longer appears in `oe_known_problems.tsv` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1430-1442; Germanic/data/oe_known_problems.tsv:1-8]. The slice should preserve that explanatory connection while still being clear that the DEV_NOTES prose here is about chronology repair across a cohort, not about a special `flood`-only argument.

## Superseded or diagnostic material

- No row-specific packet, research memo, or lexeme-local DEV_NOTES essay for `flōd` survives in the current repo. The absence should be stated plainly: the row's preserved DEV_NOTES footprint is mostly one diagnostic table entry plus shared chronology analysis, not a full lexeme dossier [Germanic/docs/lexeme_reports/coverage_audit.md:244-244; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The superseded output to remember is `flōdo`, and it should stay quarantined as diagnostic history. It was a by-product of the temporary z-loss ordering problem, not an alternative counterpart and not an instruction to change the row metadata [Germanic/docs/DEV_NOTES.md:24453-24459].
- The current debug snapshot is useful confirmation but not itself DEV_NOTES material. Its value is implementation-facing: it shows that the row now derives regularly again, which is consistent with the shared §17.10.25 fix rationale but should not be confused with older row-specific note prose [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1423-1442].

## Open questions for later work

- If row 2021 later receives a full packet or memo, decide whether the report should add lexicographic or textual support for the attested OE noun `flōd`; the current slice relies mainly on live row data plus DEV_NOTES chronology, not on a separate attestation dossier.
- If future indexing work wants a concise row verdict, keep the wording narrow: `regular *flōduz > flōd; one superseded *CVCuz z-loss-ordering regression produced flōdo`. Anything stronger would overstate the surviving DEV_NOTES record.
- If additional *CVCuz slices are drafted, consider whether the shared §17.10.25 chronology discussion should be normalized across that cohort so each row-local slice can stay brief about the common z-loss/OEMedUnstressedULowering mechanism.
