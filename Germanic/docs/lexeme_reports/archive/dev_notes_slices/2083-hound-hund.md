---
row_id: 2083
concept: hound
counterpart: hund
proto: "*xúndaz"
protoform: "*xúndaz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current_shared_background_only
needs_literature_agent: no
---

# DEV_NOTES material — 2083 hound / hund

## Current row state

- The live OE row is `2083 | hound | hund | *xúndaz | regular`; both `PROTO` and `PROTOFORM` are the same inherited input `*xúndaz`, while `COUNTERPART` is the attested/target OE output `hund`, not a rival proto-level reconstruction [Germanic/data/germanic-aligned-final.tsv:593-593].
- The row is infrastructure-thin: `coverage_audit.md` still lists `| 2083 | hound | hund | regular | no | - | - | - | none |`, and `report_manifest.tsv` has no row-2083 entry, so there is no packet stem, memo, or prior report object to recycle into this slice [Germanic/docs/lexeme_reports/coverage_audit.md:283-283; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no `hund` / `*xúndaz` entry, so the row is not being tracked as an open exception bucket, mismatch family, or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- The repo’s OE source list independently supports the inherited pairing `hound -> hund` with `template:inh`, which is consistent with the live aligned row and gives a second row-local source anchor outside DEV_NOTES [Germanic/data/old_english_wiktionary.tsv:146-146].
- The current published derivation snapshot is clean and minimal: `PROTO: *xúndaz`, `EXPECTED: hund`, `OUTPUTS: hund`, with the visible path `PGmc Final Z Deletion: *xúnda` > `PWGmc Final Bare A Loss: *xúnd` > `Outcome: hund` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2558-2578].

## Development-note summary

No dedicated row-specific DEV_NOTES block survives for `hound / hund`. What survives is narrower and should be described conservatively: one **row-explicit audit line plus one row-explicit explanatory bullet** in the March 2026 `*nd` review, and one later **shared-background-only decision block** that names `hund` inside a broader `*d/*ð` policy statement [Germanic/docs/DEV_NOTES.md:7540-7559,7879-7882].

That surviving material is still useful, but only for one precise point: `hund` is **not** a hidden Verner / `*nþ ~ *nð` / NSL case. DEV_NOTES explicitly records `| hund | *xundăz | *ku-ont- "dog" | original dental suffix | No |` and then glosses the row: `2. **hund** (Kroonen p.256): PIE *ku-ont- "dog" with dental suffix. Not from *t.` [Germanic/docs/DEV_NOTES.md:7546-7559]. For this slice, that is the strongest surviving row-relevant substance.

The live row therefore needs a careful distinction between present-row state and older DEV_NOTES notation. The row and trace now use accented `*xúndaz` [Germanic/data/germanic-aligned-final.tsv:593-593; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2558-2578], whereas the audit note writes unaccented/breve-marked `*xundăz` [Germanic/docs/DEV_NOTES.md:7546-7546]. Nothing in DEV_NOTES argues that these are competing lexical bases; the note’s job is classificatory, not to retarget `PROTOFORM`. The durable content is the consonant-source decision, not the exact accent/breve normalization of the audit table.

Support type should therefore be kept explicit. The `*nd` audit is **row-specific enough to reuse** because it names `hund` directly; the later “other `*nd` forms (bindan, windan, hund, etc.)” block is **shared-background-only** because it compresses several etymological subtypes into one policy sentence [Germanic/docs/DEV_NOTES.md:7879-7882]. There is no surviving row-local mismatch dossier, no repair chronology, no superseded target such as `×hond`, and no row-specific literature packet copied into DEV_NOTES for this lexeme.

## Relevant DEV_NOTES fragments

### DEV_NOTES:7540-7559

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)`
- Source line hint: `lines 7540-7559`
- Fragment type: `row_explicit_shared_audit`
- Status: `current`
- Issue tags: `hund_not_verner`; `nd_cluster`; `original_dental_suffix`; `not_from_t`
- Recommended next use: `cite_if_anyone_reopens_nþ_nð_or_nsl_for_hund`
- Shared-with rows if relevant: `1950 bindan`; `2048 grund`; `2294 windan`; broader `hand/land/sendan/funden` audit cohort

This is the main surviving DEV_NOTES material for row 2083, and it should be preserved almost verbatim because the row-local content is compact but decisive. The table line is exact: `| hund | *xundăz | *ku-ont- "dog" | original dental suffix | No |` [Germanic/docs/DEV_NOTES.md:7546-7546]. Immediately below, DEV_NOTES restates the point in prose: `2. **hund** (Kroonen p.256): PIE *ku-ont- "dog" with dental suffix. Not from *t.` [Germanic/docs/DEV_NOTES.md:7558-7558]. For this row, that means the preserved note substance is not about vowel repair, analogy, or a disputed OE surface form; it is about the **source of the dental** and the explicit conclusion that this lexeme does **not** belong in the `*þ/*ð` bucket.

The fragment is row-specific, but only in that narrow sense. It does not offer a bespoke derivational essay for `*xúndaz -> hund`; instead it prevents a specific later mistake: reinterpreting `hund` as though the `nd` cluster were a Verner-alternation environment comparable to `findan / funden`. It also matters that this fragment is more precise than the later generic decision block: here DEV_NOTES says `original dental suffix` and `Not from *t`, which is the row-local wording to preserve if future work needs to explain why `hund` is excluded from NSL/Verner discussion [Germanic/docs/DEV_NOTES.md:7546-7559].

### DEV_NOTES:7879-7882

- Source heading: `DECISION (2026-03-11): Option 2a Confirmed`
- Source line hint: `lines 7879-7882`
- Fragment type: `shared_policy_decision`
- Status: `current_shared_background_only`
- Issue tags: `d_vs_eth_policy`; `hund_named_in_shared_block`; `do_not_overread_etymology`
- Recommended next use: `use_as_policy_context_after_citing_the_row_specific_audit`
- Shared-with rows if relevant: `1950 bindan`; `2294 windan`; the full `*nd` policy cohort

The later decision block should be kept because it names the row, but it must be handled cautiously. DEV_NOTES says: `Other *nd forms (bindan, windan, hund, etc.) have ORIGINAL *d from PIE *dh ... They were never *þ or *ð at any stage` [Germanic/docs/DEV_NOTES.md:7879-7882]. The reusable part for row 2083 is the final policy claim — `hund` is not a `*þ/*ð` case, and later work should not invent one. But the block is **shared policy**, not precise row etymology. For `hund`, the earlier audit line is better evidence because it says `original dental suffix` / `Not from *t`, whereas the decision block compresses `hund` together with genuine PIE `*dh` rows like `bindan` and `windan`.

So this fragment is relevant but secondary. It is best used to show the project’s later system-wide representation policy, not as the primary lexical explanation. In other words: preserve it for the “no hidden Verner alternation” conclusion, but do not let its generalized wording overwrite the more exact hund-specific statement already preserved in the March audit [Germanic/docs/DEV_NOTES.md:7546-7559,7879-7882].

## Superseded or diagnostic material

- No row-specific DEV_NOTES mismatch block, reversal note, or repair proposal was found for `hound / hund`. The surviving DEV_NOTES footprint is classificatory and comparative, not a lexeme-level debugging dossier [Germanic/docs/DEV_NOTES.md:7540-7559,7879-7882].
- No superseded rival OE target survives in DEV_NOTES. The current trace already lands directly on `hund`, and nothing in the notes suggests an older project target such as `×hond`, `×hunde`, or a reclassified derivation type [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2558-2578].
- The current trace and source-row infrastructure are **diagnostic**, not DEV_NOTES substance: they confirm that the row is presently regular and thinly documented, but they do not themselves supply philological reasoning beyond successful inheritance and rule application [Germanic/data/germanic-aligned-final.tsv:593-593; Germanic/docs/lexeme_reports/coverage_audit.md:283-283; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2558-2578].
- The later decision block at `7879-7882` is also partly diagnostic for this row because its wording is broader than the row-specific audit. For `hund`, retain the anti-Verner conclusion, but prefer the earlier `original dental suffix` / `Not from *t` wording when precision matters [Germanic/docs/DEV_NOTES.md:7546-7559,7879-7882].

## Open questions for later work

- If a later lexeme packet is ever built for row 2083, decide whether the slice should be supplemented with the external Kroonen material alluded to in DEV_NOTES (`Kroonen p.256`) so that the `*ku-ont-` / dental-suffix claim is preserved from a source file rather than only through the DEV_NOTES paraphrase [Germanic/docs/DEV_NOTES.md:7558-7558].
- If protoform normalization is revisited, decide whether the DEV_NOTES audit spelling `*xundăz` should be harmonized explicitly with live-row `*xúndaz`, or simply documented as an audit-notation variant for the same lexeme. This slice does not treat them as competing lexical reconstructions because no surviving note argues for that [Germanic/data/germanic-aligned-final.tsv:593-593; Germanic/docs/DEV_NOTES.md:7546-7546].
- If future work revisits the `*d/*ð` representation policy, keep `hund` anchored in the `original dental suffix / not from *t` bucket and do not let the row drift into the `findan / funden` Verner-NSL problem set merely because it contains `nd` [Germanic/docs/DEV_NOTES.md:7546-7559,7879-7882].
