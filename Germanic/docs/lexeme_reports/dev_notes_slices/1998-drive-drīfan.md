---
row_id: 1998
concept: drive
counterpart: drīfan
proto: "*drī́baną"
protoform: "*drḯbaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1998 drive / drīfan

## Current row state

- The live OE row currently reads `ID = 1998`, `CONCEPT = drive`, `COUNTERPART = drīfan`, `PROTO = *drī́baną`, `PROTOFORM = *drḯbaną`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:262-262].
- The current published derivation trace already lands exactly on the row target: `PROTO: *drḯbaną`, `EXPECTED: drīfan`, `OUTPUTS: drīfan`. The OE-side trace shows `OE Heavy Syllable Nasal Apocope: *drḯban`, `OE Secondary Nasalization: *drḯbąn`, `PGmc B Allophony: *drḯβąn`, `OE Weak Tail Reduction: *drḯβan`, and final `Outcome: drīfan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1037-1056].
- `coverage_audit.md` still lists row `1998` as uncovered regular material (`| 1998 | drive | drīfan | regular | no | - | - | - | none |`), so there is no packet or research memo already attached to preserve row-local notes for this lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:229-229].
- `oe_known_problems.tsv` contains no entry for row `1998`, `drive`, or `drīfan`, so the row is not currently being managed as an active OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

Surviving DEV_NOTES support for row `1998` is real but thin, and almost all of it is either **early diagnostic history** or **shared Class I / phonology context** rather than a dedicated row dossier. The only clearly row-local DEV_NOTES fragment is an older mismatch bucket that recorded `*drībăną → drīban` where `drīfan` was expected [Germanic/docs/DEV_NOTES.md:1575-1576]. That fragment is still worth preserving because it shows exactly what used to go wrong: the pipeline once failed to surface the expected fricative/orthographic `f` in this verb.

Current row policy, however, is no longer a mismatch story. The published trace now reaches `drīfan` cleanly from live `PROTOFORM = *drḯbaną`, and it does so by the pathway one would expect for a postvocalic labial: `*b` survives through the earlier OE steps, appears as `*β` in the `PGmc B Allophony` stage, and then surfaces as `f` in the final OE form [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1044-1056]. The replacement note therefore needs to preserve two things at once: the older `drīban` failure as project history, and the fact that the row is currently regular.

The later philological material in DEV_NOTES is mostly shared rather than row-local, but it is still directly relevant. Hogg's quoted paradigm `drīfan, drāf, drifon, drifen 'drive'` is the clearest surviving lexeme citation, and DEV_NOTES explicitly glosses the third and fourth forms as carrying voiced Verner outcomes: `"the third and fourth have [v,z] due to Verner's Law"` [Germanic/docs/DEV_NOTES.md:7084-7088]. That quotation does **not** argue that row `1998` should be retargeted away from infinitive `drīfan`; instead, it is useful as family-level evidence that the infinitive belongs to a paradigm with voiced alternants elsewhere, so later reporting should not collapse infinitive `drīfan` and non-infinitival `drifon/drifen` into one undifferentiated row claim.

A second shared but still relevant block is the March 2026 B-allophony chronology fix. DEV_NOTES says an earlier ordering bug had made `PGmcBAllophony` fire too early and insists that `"The spirantization to [β] is a late allophonic rule, not an early phonemicization"` [Germanic/docs/DEV_NOTES.md:4021-4040]. That section is not about `drīfan` by name, but it matters because the live `drive` trace now explicitly depends on exactly that late `*b -> *β` step before the surface `f` appears [Germanic/docs/DEV_NOTES.md:4042-4055; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1050-1056]. The safest interpretation is conservative: DEV_NOTES no longer preserves a row-specific controversy over the target, only an older failure state plus shared phonological notes that explain why the current derivation is plausible.

Finally, the only later note that names row `1998` directly is the `*ḯ`-migration table. Row `1998` appears in Batch 1 (`1998, 2047, 2101 | drīfan, grīpan, līf`) among forms that were rebuilt, mismatch-checked, and committed during the long-`ī` notation migration [Germanic/docs/DEV_NOTES.md:42006-42023]. For this row, that matters less as philology than as workflow history: it confirms that current `PROTOFORM = *drḯbaną` belongs to the post-migration verified state, not to the older diagnostic spelling `*drībăną` seen in the mismatch note.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1575-1576

- Source heading: `intervocalic_voicing_missing`
- Source line or section hint: `lines 1575-1576`
- Fragment type: `lexeme_specific_diagnostic`
- Status: `superseded_but_row_specific`
- Issue tags: `old_mismatch`; `postvocalic_b`; `missing_fricativization`; `project_history`
- Recommended next use: `cite_if_explaining_why_row_once_failed`
- Shared with row IDs: `1941`

This is the only plainly row-local DEV_NOTES fragment that survives. Under the bucket `intervocalic_voicing_missing`, DEV_NOTES gives the example `*drībăną → drīban (expected drīfan)` [Germanic/docs/DEV_NOTES.md:1575-1576]. Even though the category label is somewhat early-project and broad, the substance is clear and still worth carrying forward: the row once failed by preserving a stop/spelling `b` where the OE output required fricative/surface `f`.

The fragment should now be used as diagnostic history only. It does **not** describe the current row state, and its proto-side spelling with breve `*ă` belongs to that earlier project stage rather than to the current row metadata. Still, if later reporting wants one sentence on why the slice exists at all, this is the sentence to keep: there used to be a direct `drīban` mismatch, and that mismatch was explicitly noticed in DEV_NOTES [Germanic/docs/DEV_NOTES.md:1575-1576].

### DEV_NOTES:line-4017-4055

- Source heading: `J-Gemination/BAllophony Chronology Fix (2026-03-09)`
- Source line or section hint: `lines 4017-4055`
- Fragment type: `shared_phonology_support`
- Status: `current_but_indirect`
- Issue tags: `b_allophony`; `chronology`; `late_spirantization`; `surface_f`
- Recommended next use: `cite_if_explaining_how_current_trace_reaches_f`
- Shared with row IDs:

This fragment is shared technical support rather than a `drive` dossier, but it is still materially relevant because the live row's successful trace now passes through `PGmc B Allophony`. DEV_NOTES explains the general repair in explicit chronology terms: an older ordering had applied `*b → *β` too early, but the corrected analysis treats that change as late and allophonic, stating that `"The spirantization to [β] is a late allophonic rule, not an early phonemicization"` [Germanic/docs/DEV_NOTES.md:4021-4040].

For row `1998`, the important use of this fragment is explanatory, not evidentiary in a narrow philological sense. The current trace `*drḯbąn -> *drḯβąn -> drīfan` matches the revised chronology exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1050-1056]. That does not prove the lexeme from an external source, but it does explain why the old `drīban` mismatch no longer survives in the live build.

### DEV_NOTES:line-7072-7097

- Source heading: `The Levelling Chronology`
- Source line or section hint: `lines 7072-7097`
- Fragment type: `shared_family_background`
- Status: `current`
- Issue tags: `class_i_strong_verb`; `verners_law`; `paradigm_context`; `attested_oe_forms`
- Recommended next use: `cite_if_explaining_paradigm_context_not_row_retargeting`
- Shared with row IDs:

This is the strongest surviving philological fragment that actually names the lexeme. DEV_NOTES quotes Hogg: `"Old English spelling never shows these changes, so that we find in strong verbs alternations such as drīfan, drāf, drifon, drifen 'drive'... the third and fourth have [v,z] due to Verner's Law"` [Germanic/docs/DEV_NOTES.md:7084-7088]. The force of the quotation is carefully limited: it preserves the OE paradigm context around `drīfan`, especially the fact that non-infinitival cells can show voiced reflexes, but it does not argue that the infinitive row itself is unstable.

That limitation matters for this slice. The current row targets the infinitive/citation form `drīfan`, not the preterite plural or participial cells. The Hogg quotation is therefore best used to prevent overstatement in either direction: it supports the family context of the row, but later report writing should not cite it as if it directly licensed a new `PROTOFORM`, a new `COUNTERPART`, or a special derivation class for row `1998` [Germanic/data/germanic-aligned-final.tsv:262-262; Germanic/docs/DEV_NOTES.md:7084-7088].

### DEV_NOTES:line-42006-42023

- Source heading: `E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42023`
- Fragment type: `verification_history`
- Status: `current`
- Issue tags: `protoform_notation`; `long_i_migration`; `row_verification`; `workflow_history`
- Recommended next use: `cite_if_questioned_about_current_*ḯ_protoform`
- Shared with row IDs: `2047`; `2101`

This fragment is workflow evidence, not a lexeme analysis, but it is one of the few later DEV_NOTES passages that names the row directly. DEV_NOTES says fifteen stressed-root `*ī` rows were migrated to `*ḯ`, then lists Batch 1 as `1998, 2047, 2101 | drīfan, grīpan, līf` among rows that were rebuilt, mismatch-checked, and committed [Germanic/docs/DEV_NOTES.md:42010-42023].

For row `1998`, the main value of that note is to anchor current notation. It supports treating live `PROTOFORM = *drḯbaną` as the verified post-migration form, while the older mismatch note's `*drībăną` should be read as historical diagnostic spelling rather than as the current row encoding [Germanic/data/germanic-aligned-final.tsv:262-262; Germanic/docs/DEV_NOTES.md:42010-42023].

## Superseded or diagnostic material

- The old mismatch `*drībăną → drīban` is preserved here because it is the only unambiguously row-specific DEV_NOTES material, but it is no longer current row policy. The live trace now gives exact `drīfan`, so the earlier note should be cited only as project history, not as evidence that the row still needs rescue [Germanic/docs/DEV_NOTES.md:1575-1576; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1037-1056].
- No surviving DEV_NOTES fragment argues that row `1998` needs a different `COUNTERPART`, a different derivation class, or a special paradigm-cell workaround. The row's present support is mostly a combination of the exact live trace, shared B-allophony chronology, and shared strong-verb paradigm context [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1044-1056; Germanic/docs/DEV_NOTES.md:4021-4055,7084-7088].
- The Hogg quotation should not be overread. It is valuable because it preserves actual OE paradigm forms with `drīfan`, but it is still family-level context. It does not by itself supply a row-local argument for rewriting `PROTO = *drī́baną` or `PROTOFORM = *drḯbaną`; it mainly warns later writers to distinguish the infinitive row from voiced alternants in other cells [Germanic/docs/DEV_NOTES.md:7084-7088; Germanic/data/germanic-aligned-final.tsv:262-262].

## Open questions for later work

- If a later packet or memo is ever created for Class I `b/f` strong verbs, add a short source audit specifically on infinitive `drīfan` and on how the comparative proto labels `*drī́baną` / `*drḯbaną` relate to handbook reconstructions. The current slice is usable, but its strongest surviving support is still shared or project-internal rather than a row-local literature dossier [Germanic/docs/DEV_NOTES.md:7084-7088,42010-42023].
- If future reporting needs one compact claim about the row, the safest one is narrow: row `1998` used to misfire as `drīban`, but the current build now derives regular `drīfan`, and the remaining DEV_NOTES support is mainly shared phonology plus shared paradigm context rather than a live exception narrative [Germanic/docs/DEV_NOTES.md:1575-1576,4021-4055; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1037-1056].
- If notation cleanup is revisited later, keep the chronological distinction explicit between older diagnostic spelling `*drībăną` and current row metadata `PROTO = *drī́baną`, `PROTOFORM = *drḯbaną`. DEV_NOTES preserves both project states, and collapsing them would make the row history harder to read than it needs to be [Germanic/docs/DEV_NOTES.md:1575-1576,42010-42023; Germanic/data/germanic-aligned-final.tsv:262-262].
