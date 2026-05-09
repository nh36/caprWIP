---
row_id: 2044
concept: goose
counterpart: gōs
proto: "*gánsz"
protoform: "*gánsz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current_from_shared_background_only
needs_literature_agent: yes
---

# DEV_NOTES material — 2044 goose / gōs

## Current row state

- The live OE row is `2044`, with `CONCEPT goose`, `COUNTERPART gōs`, `PROTO *gánsz`, `PROTOFORM *gánsz`, and `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:442-442].
- The TSV preserves no project-authored row note for this item. Its only surviving provenance text is the duplicated import string `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:442-442].
- `oe_known_problems.tsv` has no entry for row `2044`, for `gōs`, or for `*gánsz`, so the lexeme is not currently parked in the OE exception ledger [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still lists `| 2044 | goose | gōs | regular | no | - | - | - | none |`, and `report_manifest.tsv` has no row-2044 entry; there is no packet or research-memo stem to inherit, so this slice has to stand on its own [Germanic/docs/lexeme_reports/coverage_audit.md:258-258; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The published derivation trace is already an exact match: `PROTO: *gánsz`, `EXPECTED: gōs`, `OUTPUTS: gōs`, with the intermediate path `PGmc Final Z Deletion: *gáns`, `NWGmc Nasal Spirant Lengthening: *gōns`, `NWGmc Nasal Spirant Loss: *gōs` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1806-1825].
- For this row the distinction among reconstructed inputs and attested target matters, even though the two proto columns are identical. `PROTO = PROTOFORM = *gánsz` is the row’s stored reconstructed input; `*gáns` and `*gōns` are only traced intermediate stages; `gōs` is the attested OE target [Germanic/data/germanic-aligned-final.tsv:442-442; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1815-1825].

## Development-note summary

No dedicated row-2044 dossier survives in `DEV_NOTES.md`. The usable material is limited to shared NSL / Ingvaeonic-nasal-loss discussion plus a later stocktake ledger. The best surviving note is a general `Nasal Spirant Lengthening (NSL)` section quoting Fulk on North Sea Germanic loss of nasals before voiceless fricatives and explicitly giving `*gans → *gōs → OE gōs 'goose'` as the `*ns` example [Germanic/docs/DEV_NOTES.md:7013-7024]. A later restatement under `Ingvaeonic Nasal Loss (Campbell §121, §332)` again uses goose as an example, but that fragment is partly diagnostic because its shorthand environment label does not line up cleanly with the actual `*ns` cluster in `*gans` [Germanic/docs/DEV_NOTES.md:19329-19339].

That means this file is necessarily a conservative replacement note assembled from shared material plus the current trace, not an extraction from a lost row-local memorandum. The core surviving claim is still straightforward: the row is currently treated as regular because the implemented cascade already derives `gōs` from `*gánsz` through final `-z` loss and the North Sea Germanic / Ingvaeonic `*ns` > long-vowel-plus-`s` development, with no additional OE repair step visible in the trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1815-1825; Germanic/docs/DEV_NOTES.md:7017-7024].

The later DEV_NOTES stocktake reinforces the same practical conclusion. It lists `*gánsz` among the “**8 items fixed** (no longer mismatching),” so whatever earlier mismatch history once existed for this lexeme had already been treated as resolved by that stage of the project [Germanic/docs/DEV_NOTES.md:20555-20563]. Because no row-specific discussion survives, however, that ledger should be used only as current-state confirmation, not as the main historical argument.

## Relevant DEV_NOTES fragments

The surviving DEV_NOTES evidence for `goose / gōs` is real but shared rather than row-local.

### DEV_NOTES:line-7013-7024

- Source heading: `#### 3. Nasal Spirant Lengthening (NSL)`
- Source line hint: `lines 7013-7024`
- Fragment type: `shared_current_rule_note`
- Status: `current_but_shared`
- Issue tags: `nsl`; `ingvaeonic_nasal_loss`; `ns_cluster`; `compensatory_lengthening`
- Recommended next use: `primary_DEV_NOTES_citation_for_row_2044`
- Shared-with rows if relevant:

This is the most important surviving DEV_NOTES fragment for row `2044`, even though it is a shared rule note rather than a goose-specific packet. It quotes Fulk directly: “In North Sea Germanic a nasal consonant was lost before any voiceless fricative, with nasalization and compensatory lengthening of the preceding vowel. The change thus affects **mf, ns, nþ**...” [Germanic/docs/DEV_NOTES.md:7015-7019]. The bullet list then applies that rule to the exact cluster type needed here: ``*ns` → `*s̃` (e.g., `*gans` → `*gōs` → OE `gōs` 'goose')`` [Germanic/docs/DEV_NOTES.md:7021-7024].

For replacement-note purposes, the fragment’s value is twofold. First, it preserves the project’s explicit theoretical frame: this row is being explained through the North Sea Germanic nasal-loss/lengthening module, not through analogy, spelling normalization, or a hidden paradigm form [Germanic/docs/DEV_NOTES.md:7013-7024]. Second, it lines up cleanly with the live trace once notation differences are kept straight. DEV_NOTES uses simplified `*gans`; the row metadata stores accented `*gánsz`; the trace inserts `*gáns` after final `-z` deletion and then `*gōns` before nasal loss [Germanic/data/germanic-aligned-final.tsv:442-442; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1815-1825]. Those are not competing protoforms, just different representational stages.

### DEV_NOTES:line-20555-20563

- Source heading: `#### Regressions Identified (56 vs 43 mismatches)`
- Source line hint: `lines 20555-20563`
- Fragment type: `brief_current_ledger`
- Status: `current`
- Issue tags: `resolved_item`; `post_fix_ledger`; `not_a_live_mismatch`
- Recommended next use: `cite_only_as_current_state_confirmation`
- Shared-with rows if relevant:

This fragment is not a phonological explanation, but it is still useful current-state evidence. DEV_NOTES records “**8 items fixed** (no longer mismatching): `*fédwōr`, `*fríjōndz`, `*fúnxstiz`, `*gánsz`, `*júgunθ`, `*kéwwăną`, `*mēnōθz`, `*násō`” [Germanic/docs/DEV_NOTES.md:20562-20563]. For row `2044`, the only safe inference is that `*gánsz` had been removed from the active mismatch bucket by this point in project history.

The fragment should not be asked to do more than that. It does not restate the `*ns` rule, it does not specify the intermediate forms, and it does not preserve any goose-specific scholarly citation. Its force is administrative rather than explanatory: the row’s earlier problem state had become closed, not ongoing [Germanic/docs/DEV_NOTES.md:20555-20563].

### DEV_NOTES:line-19329-19339

- Source heading: `### Ingvaeonic Nasal Loss (Campbell §121, §332)`
- Source line hint: `lines 19329-19339`
- Fragment type: `shared_background_only_or_diagnostic`
- Status: `diagnostic_with_usable_core`
- Issue tags: `rule_restatement`; `campbell_label`; `cluster_notation_mismatch`; `goose_example`
- Recommended next use: `use_for_background_only_not_as_primary_row_authority`
- Shared-with rows if relevant:

This later fragment restates the same broad process in a different vocabulary: “The rule: nasals are lost before voiceless fricatives (θ, f, s) with compensatory lengthening of the preceding vowel” [Germanic/docs/DEV_NOTES.md:19329-19332]. It then gives a goose example inside the “Applies to” list: ``*anθ-` → `*āθ-` (e.g., `*gans` → `gōs` 'goose')`` [Germanic/docs/DEV_NOTES.md:19334-19336].

For row `2044`, only part of this fragment is reliable as working support. The general rule statement and the goose example both agree with the live trace’s basic story that nasal loss plus compensatory lengthening is the relevant development [Germanic/docs/DEV_NOTES.md:19329-19336; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1817-1825]. But the shorthand environment label `*anθ- → *āθ-` does not match the actual goose cluster, which is `*ns`, not `*nþ`. So this fragment is best preserved as shared-background-only plus diagnostic evidence that DEV_NOTES was reusing goose as a stock example, not as a clean row-specific statement of the exact segmental pathway.

## Superseded or diagnostic material

- No clearly row-specific DEV_NOTES block survives for `goose / gōs`. The absence of a dedicated memorandum is itself part of the current diagnosis: row support survives only as shared NSL / nasal-loss prose and later audit ledgers [Germanic/docs/DEV_NOTES.md:7013-7024,19329-19339,20555-20563].
- The spellings `*gans` in DEV_NOTES and `*gáns` / `*gōns` in the trace should not replace live row metadata `*gánsz`. In this slice they are, respectively, a simplified citation form without final `-z`, the post-`z`-deletion intermediate, and the post-lengthening intermediate; the stored `PROTO` / `PROTOFORM` remains `*gánsz` [Germanic/docs/DEV_NOTES.md:7023-7024; Germanic/data/germanic-aligned-final.tsv:442-442; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1815-1825].
- The `Ingvaeonic Nasal Loss` fragment at lines `19329-19339` is partly diagnostic rather than clean authority, because its formula line uses `*anθ-` while its example is goose from `*gans`. Later reporting should therefore cite the earlier `NSL` fragment first whenever exact cluster conditioning matters [Germanic/docs/DEV_NOTES.md:19329-19339,7013-7024].
- Coverage status `none` in `coverage_audit.md` is a documentation gap, not evidence of a live derivational failure. The publish trace already lands on `gōs`, and DEV_NOTES later lists `*gánsz` among fixed items [Germanic/docs/lexeme_reports/coverage_audit.md:258-258; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1806-1825; Germanic/docs/DEV_NOTES.md:20562-20563].
- No packet, research memo, or manifest row currently exists for this lexeme, so there was no alternate report stem or richer row dossier to preserve here [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/docs/lexeme_reports/coverage_audit.md:258-258].

## Open questions for later work

- If a later literature pass is commissioned, it would be useful to attach a direct handbook quotation specifically for `goose / gōs`, not just the shared DEV_NOTES/Fulk NSL statement, because the surviving row support is philologically thin even though the derivation is operationally stable [Germanic/docs/DEV_NOTES.md:7015-7024].
- Later reporting should decide whether to standardize terminology as `Nasal Spirant Lengthening`, `Ingvaeonic Nasal Loss`, or explicitly both. Current DEV_NOTES uses both labels for overlapping material, and this row depends on that shared process family rather than on a row-local special rule [Germanic/docs/DEV_NOTES.md:7013-7024,19329-19339].
- Any future final lexeme report should keep four levels distinct: stored row input `*gánsz`, traced post-`z` stage `*gáns`, traced post-lengthening stage `*gōns`, and attested OE target `gōs`. Collapsing those labels would erase the exact derivational information that the current trace still preserves [Germanic/data/germanic-aligned-final.tsv:442-442; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1815-1825].
