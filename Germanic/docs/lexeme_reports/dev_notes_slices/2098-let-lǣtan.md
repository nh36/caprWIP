---
row_id: 2098
concept: let
counterpart: lǣtan
proto: "*lḗtaną"
protoform: "*lḗtaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/lexeme_reports/coverage_audit.md
  - Germanic/docs/lexeme_reports/report_manifest.tsv
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2098 let / lǣtan

## Current row state

- Live TSV row `2098` currently reads `let / lǣtan / *lḗtaną / regular`. `PROTO` and `PROTOFORM` coincide, the row has no embedded explanatory note, and the source strings are generic duplicated Wiktionary derivation provenance rather than a row-local argument block [Germanic/data/germanic-aligned-final.tsv:650-650].
- `coverage_audit.md` marks the row as uncovered regular infrastructure: `| 2098 | let | lǣtan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:291-291].
- `oe_known_problems.tsv` has no entry for row `2098`, for `lǣtan`, or for `*lḗtaną`; the current OE exception ledger still tracks only other lexemes such as `*fūri` and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` does not currently include row `2098`; the manifest remains limited to the pilot/production report set and has no `let / lǣtan` entry [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The published and audit derivation snapshots are exact matches. Both give `PROTO: *lḗtaną`, `EXPECTED: lǣtan`, `OUTPUTS: lǣtan`, with the compact pathway `NWGmc Long E Lowering: *lǣtaną` > `OE Heavy Syllable Nasal Apocope: *lǣtan` > `OE Secondary Nasalization: *lǣtąn` > `OE Weak Tail Reduction: *lǣtan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2762-2780; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:3050-3068].
- The full trace confirms that almost nothing exotic happens around the row. The only substantive steps are `NWGmcLongELowering`, then the ordinary OE tail-loss sequence; `OEAuFronting`, `OEDiphthongLeveling`, `SieversLawSyncope`, `OEIUmlaut`, `OEBackMutation`, and the later cleanup rules are all `[no-change]` for this input before surface `lǣtan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18358-18445].

## Development-note summary

No dedicated row-specific DEV_NOTES block for `2098 let / lǣtan / *lḗtaną` survives in the live `DEV_NOTES.md`. The usable material is instead the shared April 2026 stressed-long-`ē` refactor in `§17.49`, where this lexeme appears first in the motivating list as older plain `*lētaną`, and then in the verification sample as current `*lḗtaną → lǣtan` [Germanic/docs/DEV_NOTES.md:42683-42692,42727-42739]. The replacement slice therefore has to be explicit about evidential scope: current support is real, but it is mostly **shared-background** and **lexeme-explicit shared verification**, not a preserved row dossier.

That shared material still does important row-local work. DEV_NOTES says the project had become inconsistent by marking stressed long diphthongs without marking stressed long monophthong `*ḗ`, even though the TSV already contained root-syllable long-`ē` lexemes such as `*lētaną`; the governing principle is quoted directly as “if we mark stress on long *ī, we must mark it on long *ē too” [Germanic/docs/DEV_NOTES.md:42683-42692]. For row `2098`, this is the reason the live row now keeps `PROTO = PROTOFORM = *lḗtaną` rather than older plain `*lētaną` or pre-refactor `*lētăną` [Germanic/docs/DEV_NOTES.md:42688-42692; Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:650-650; Germanic/data/germanic-aligned-final.tsv:650-650].

The actual phonological pathway is also straightforward and current. DEV_NOTES records that `NWGmcLongELowering` was extended by adding `{*ḗ} -> {*ǣ}` and later reports the sample output `*lḗtaną → lǣtan` among the invariant probe checks for the branch [Germanic/docs/DEV_NOTES.md:42713-42719,42735-42739]. That matches the live row exactly: **PROTO/PROTOFORM** are the stress-marked project input `*lḗtaną`, the attested/target OE form is `lǣtan`, and the current trace shows the regular development `*lḗtaną > *lǣtaną > lǣtan` without any analogical repair, paradigm substitution, or known-problem override [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2770-2780; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18368-18445].

The distinction among row layers should stay explicit even though `PROTO` and `PROTOFORM` currently coincide. Here both fields carry the same live project notation because there is no split between comparative headword and OE-directed input, but they still remain row metadata, not identical with the surface OE form. The target is `lǣtan`; the stressed `*ḗ` notation belongs only to the pre-surface comparative/input layer; and DEV_NOTES explicitly says the branch uses stress to distinguish stressed root `*ḗ` from unstressed `*ē` for later rule control [Germanic/data/germanic-aligned-final.tsv:650-650; Germanic/docs/DEV_NOTES.md:42741-42749].

## Relevant DEV_NOTES fragments

### DEV_NOTES fragment A

- Source heading: `§17.49 Stressed long-ē tier (*ḗ) — extending the §17.46 stress-tier convention`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42679-42692`
- Fragment type: `lexeme_explicit_shared_support`
- Status: `current shared-background-only`
- Issue tags: `stress_tier`; `protoform_notation`; `root_syllable_long_e`; `no_row_specific_block`
- Recommended next use: `cite when explaining why the live row uses *lḗtaną rather than plain *lētaną`
- Shared-with rows if relevant: `1987`; `2001`; `2150`; `2209`; other stressed-*ḗ rows`

This is the main surviving DEV_NOTES anchor for the row even though it is not a dedicated `let` subsection. DEV_NOTES says the cascade needed a stressed long `*ḗ` tier because the TSV already had root-syllable long-`ē` lexemes “`(*dēdiz*, *lētaną*, *rēdaną*, *mēnōθz*, *nēdrōn*, *spēnuz*, etc.)`” and the governing convention is “`if we mark stress on long *ī, we must mark it on long *ē too`” [Germanic/docs/DEV_NOTES.md:42683-42692]. For row `2098`, the substance is specific but narrow: DEV_NOTES itself treats the older unaccented `*lētaną` spelling as one of the items that motivated the later stress-marked notation. This fragment is therefore **shared-background-only**, but it is still the clearest surviving explanation for why the live row now carries stressed `*lḗtaną` in both proto columns.

### DEV_NOTES fragment B

- Source heading: `§17.49 rule-by-rule parallel plumbing`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42713-42719`
- Fragment type: `shared_sound_change_context`
- Status: `current shared-background-only`
- Issue tags: `NWGmc_long_e_lowering`; `regular_pathway`; `stress_drop_on_output`; `trace_alignment`
- Recommended next use: `cite when glossing the derivation *lḗtaną > *lǣtaną`
- Shared-with rows if relevant: `1987`; `2001`; `2150`; `2209`; other stressed-*ḗ rows`

This fragment is not row-specific, but it gives the exact shared rule that the live trace uses. DEV_NOTES states that `NWGmcLongELowering` was extended by adding “`{*ḗ} -> {*ǣ}`,” with stress then dropped because this branch does not yet carry a separate stressed `*ǣ́` tier [Germanic/docs/DEV_NOTES.md:42713-42719]. For row `2098`, that is the entire phonological crux: once stressed `*ḗ` is admitted as input, the current row follows the ordinary inherited lowering path to `*lǣtaną`, after which only routine OE tail reduction remains. The fragment should therefore be cited as **shared phonological background**, not as a bespoke `lǣtan` argument.

### DEV_NOTES fragment C

- Source heading: `§17.49 TSV root-syllable promotion and verification`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42727-42739`
- Fragment type: `lexeme_explicit_shared_support`
- Status: `current`
- Issue tags: `tsv_promotion`; `verification_sample`; `row_control_case`; `current_output`
- Recommended next use: `cite as the strongest direct surviving support for the live row state`
- Shared-with rows if relevant: `1987`; `2150`; `2209`; other lexemes named in the *ḗ verification sample`

This is the strongest surviving fragment for row `2098`. DEV_NOTES says that “`16 lemmas promoted from *ē to *ḗ in PROTOFORM and PROTO columns`” and then records the verification sentence: “`Probe outputs invariant across the refactor (sample: *dḗdiz → dǣd*, *lḗtaną → lǣtan*, *rḗdaną → rǣdan*, *mḗnōθz → mōnaþ*, *spḗnuz → spōn* ...)`” [Germanic/docs/DEV_NOTES.md:42727-42739]. For this row that does real work. It shows that the old unaccented proto notation is superseded in current project metadata, and it also shows that `lǣtan` was one of the explicit regression-proof sample outputs used to verify the branch rather than a merely assumed consequence.

### DEV_NOTES fragment D

- Source heading: `§17.49 stress-on-output convention`
- Source line hint: `Germanic/docs/DEV_NOTES.md:42741-42749`
- Fragment type: `shared_notation_policy`
- Status: `current shared-background-only`
- Issue tags: `stressed_vs_unstressed_long_e`; `OEUnstressedLongVowelShortening2`; `proto_vs_target`; `notation_policy`
- Recommended next use: `cite when clarifying why stressed *ḗ belongs to proto/input layers rather than the OE surface`
- Shared-with rows if relevant: `1987`; `2001`; `2150`; `2209`; other stressed-*ḗ rows`

This fragment matters because it prevents a common misreading of the row. DEV_NOTES says stress is preserved only where the receiving long-vowel tier exists and that, in the current branch, stress is used “`to differentiate *ē (unstressed) from *ḗ (stressed)`” for the purposes of `OEUnstressedLongVowelShortening2` [Germanic/docs/DEV_NOTES.md:42741-42749]. For row `2098`, the practical consequence is that `*lḗtaną` is a modelling/input notation, not an OE surface claim. The OE target stays plain `lǣtan`; the stress mark is not meant to survive past the NWGmc lowering step.

## Superseded or diagnostic material

- No row-specific DEV_NOTES essay for `2098 let / lǣtan` survives. The slice should continue to say that plainly rather than implying a lost bespoke dossier; what survives is the shared stressed-`*ḗ` infrastructure note plus current exact-match traces [Germanic/docs/DEV_NOTES.md:42679-42749].
- The older row spellings `*lētaną` in `DEV_NOTES.md` and `*lētăną` in the February backup TSV are **superseded project notation**, not competing proto analyses. Their only current value is diagnostic/project-historical: they show the row before the stressed-`*ḗ` refactor was propagated into live metadata [Germanic/docs/DEV_NOTES.md:42688-42689; Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:650-650; Germanic/data/germanic-aligned-final.tsv:650-650].
- The current trace reports are essential diagnostics but they are not themselves DEV_NOTES fragments. Their role is to confirm that the live row already succeeds regularly and that nothing beyond `NWGmcLongELowering` plus ordinary OE tail handling is active for this lexeme [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2762-2780; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18368-18445].
- `coverage_audit.md`, `oe_known_problems.tsv`, and `report_manifest.tsv` are likewise status diagnostics, not philological evidence. Together they confirm the present repo state: no special-report infrastructure, no known-problem bucket, and no manifest-backed report for the row [Germanic/docs/lexeme_reports/coverage_audit.md:291-291; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If future stress-tier work adds output-side stressed vowels such as `*ǣ́`, revisit whether this row should preserve any stress marking beyond `NWGmcLongELowering`; §17.49 currently says it does not because downstream rules do not consume stress on `*ǣ` yet [Germanic/docs/DEV_NOTES.md:42741-42749].
- If later packet or index work covers row `2098`, classify it conservatively as a **current shared-support/control-case slice**, not as an exception dossier: the strongest surviving row-shaped support is still the verification sample `*lḗtaną → lǣtan` [Germanic/docs/DEV_NOTES.md:42727-42739].
- If older materials surface with `*lētaną` or `*lētăną`, annotate them explicitly as pre-§17.49 notation rather than as evidence for a different `PROTOFORM`; the current live row keeps `PROTO = PROTOFORM = *lḗtaną`, target `lǣtan`, derivation class `regular` [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:650-650; Germanic/data/germanic-aligned-final.tsv:650-650].
