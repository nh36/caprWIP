---
row_id: 2192
concept: sister
counterpart: swester
proto: *swéstēr
protoform: *swéstēr
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2192 sister / swester

## Current row state

- The live OE row now reads `CONCEPT = sister`, `COUNTERPART = swester`, `PROTO = *swéstēr`, `PROTOFORM = *swéstēr`, `DERIVATION_CLASS = regular`, with an explicit TSV note that the target was switched from `swustor` to Anglian `swester` because `swester` is the lautgesetzlich Anglian nominative singular attested in Rushworth² and Lindisfarne, while late-WS `swustor` reflects sporadic labio-velar rounding or analogical innovation rather than the regular sound-change chain [Germanic/data/germanic-aligned-final.tsv:1015-1015].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not currently using an oblique-cell surrogate, a diagnostic reconstruction, or a special OE-facing repair input. The row policy is: PGmc lexeme/protoform `*swéstēr`, attested OE target `swester` [Germanic/data/germanic-aligned-final.tsv:1015-1015].
- `coverage_audit.md` already reflects the retargeted row as `| 2192 | sister | swester | regular | no | - | - | - | none |`, so the slice is documenting a live row state that is already propagated into the audit infrastructure [Germanic/docs/lexeme_reports/coverage_audit.md:354-354].
- The current published derivation trace is an exact match and is unusually important here because it clarifies the live transducer pathway. The published trace gives `PROTO: *swéstēr`, `EXPECTED: swester`, `OUTPUTS: swester`; in the rule-by-rule trace there is no `OEBreaking`, no `OEBackMutation`, and no special repair rule. The active steps are instead `NWGmcLongELowering: *s*w*é*s*t*ǣ*r`, then `OEUnstressedLongVowelShortening: *s*w*é*s*t*æ*r`, then `OEUnstressedAEMerger: *s*w*é*s*t*e*r`, then surface `swester` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4266-4285; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29003-29117].
- Some repo-local artifacts still preserve the superseded pre-switch target and therefore must be treated as stale diagnostics, not current row authority. `oe_mismatch_report_new.txt` still records `*swestēr -> swester (expected swustor)` and labels the issue as a front-vs-back-vowel mismatch, and `old_english_sandbox_results_current.json` still carries `"counterpart": "swustor"` with no outputs for `sister` [Germanic/docs/debug_snapshots/oe_mismatch_report_new.txt:150-153; Germanic/tmp/old_english_sandbox_results_current.json:2467-2471].
- No row-specific packet, research memo, or dossier was found during slice preparation, so the YAML link fields are intentionally blank and this file serves as the replacement working note for the row.

## Development-note summary

The surviving DEV_NOTES material supports a firm row-level distinction that should not be blurred. `PROTO` and `PROTOFORM` both remain `*swéstēr`, i.e. the PGmc r-stem kinship noun in the nominative singular shape now used by the live row. The attested OE target represented by the row is not the late dictionary-style West-Saxon form `swustor`, but the Anglian form `swester` [Germanic/data/germanic-aligned-final.tsv:1015-1015; Germanic/docs/DEV_NOTES.md:33705-33724,34114-34117]. DEV_NOTES repeatedly tests other forms and other cells—`sweostor`, `swustor`, `swéstri`, `swésterų`, plural `swestra`, and the like—but those are comparative paradigm members or rejected alternative targets, not replacement live `PROTOFORM` values [Germanic/docs/DEV_NOTES.md:33328-33338,34010-34017,34080-34092].

The row note in the TSV compresses a much longer dossier. The basic philological result is that `swester` is not a conjectural normalization manufactured to placate the FST; it is directly attested Anglian evidence. DEV_NOTES cites Rushworth² as Northumbrian `swester`, with Brunner's paradigm `"nordh.: R² Sg. Nom. Akk. Gen. swester, Pl. Nom. Akk. swester, swestro"`; it also cites Rushworth¹ as showing `swester` alongside innovative `swuster`, and Lindisfarne as preserving `suoester, soester`, where the Northumbrian spellings still point to the Anglian `swester` base rather than to `u`-vocalism [Germanic/docs/DEV_NOTES.md:33531-33558]. The note's own verdict is explicit: "`swester` is directly attested in Rushworth¹, Rushworth², and (with orthographic variation) Lindisfarne" and should be preferred under the earlier `spere/speoru` and `tángō → tang` precedents when an early/Anglian lautgesetzlich form is available [Germanic/docs/DEV_NOTES.md:33556-33579].

Just as important is what DEV_NOTES says about `swustor`. The dossier does not preserve a single settled explanation that would make `swustor` the regular sound-law output. Instead it records two competing late explanations and leaves both outside the ordinary cascade. One is Brunner's late-WS phonological account, grouping `swustor` with `wurold` and `wurlde` as instances of a specifically late West-Saxon `eo -> u` rounding after labials: `"auf diese Weise dürfte zu erklären sein: spätws. swustor ... wurold ... und wurlde ..."` [Germanic/docs/DEV_NOTES.md:33304-33318]. The other is Brunner's and Campbell's analogical possibility: `"Spätws. swustor ... könnte auch auf eine Stammform mit germ. -i- zurückgehen"` and `swustor [...] could also be due to the influence of oblique forms with i-grade in the stem` [Germanic/docs/DEV_NOTES.md:33326-33361]. In other words, even the best source-preserving DEV_NOTES language treats `swustor` as either a late special innovation or an analogical generalization from oblique material, not as the ordinary reflex of row proto `*swéstēr`.

DEV_NOTES also makes clear that there is no successful paradigm-cell rescue that would preserve `swustor` while keeping the row "regular" in the same sense as the rest of the OE table. The 2D cell-by-form search reconstructs the PGmc r-stem paradigm (`NomSg *swéstēr`, `AccSg *swésterų`, `DatSg *swéstri`, `NomPl *swéstriz`, etc.) and then asks whether any cell yields an unbroken chain to the attested forms [Germanic/docs/DEV_NOTES.md:34004-34017,34080-34092]. Its result is explicit: `NomSg *swéstēr -> swester` is fully regular; `NomSg *swéstēr -> sweostor` is also fully regular as a WS outcome; but `NomSg *swéstēr -> swustor` is marked `✗ ANALOGICAL`, with the warning that `eo -> u` is "late WS innovation, not lautgesetzlich" [Germanic/docs/DEV_NOTES.md:34082-34087]. The same section explicitly rejects the idea that a different paradigm cell gives a regular `u`-stem outcome: oblique cells may explain why an analogical story was thinkable, but they do not supply the live row's derivational input [Germanic/docs/DEV_NOTES.md:33732-33737,34088-34092].

The live trace materially sharpens one point where DEV_NOTES itself evolved. Earlier parts of §17.21 still speak as if Anglian `swester` may have arisen through `*sweostēr` plus smoothing, and the recommendation section at `§17.21.8` still summarizes the FST as producing the "Anglian outcome ... via the regular sound-change cascade (breaking + smoothing)" [Germanic/docs/DEV_NOTES.md:33711-33716]. Later in the same dossier, however, the analysis revisits the pathway and argues that the earlier "breaking + smoothing" explanation is probably wrong for this lexeme: Anglian smoothing is canonically pre-velar, not pre-`st`, so the more economical account is that Anglian lacks breaking before `/st/ + r/` here and reaches `swester` directly. That later note ends with the clear statement that "The FST's current output of `swester` is historically correct for Anglian" and that "`swéstēr -> swester`" proceeds "without an intermediate `/eo/` stage" [Germanic/docs/DEV_NOTES.md:33917-33947,33971-33993]. The published trace now backs that later correction, since the actual live derivation shows neither `OEBreaking` nor `OEBackMutation` firing for the row [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29063-29079,29091-29117].

That chronological correction matters for notation as well. The repo currently contains both accented `*swéstēr` and unaccented `*swestēr` spellings. In the live TSV and the published trace the row uses `*swéstēr`; in stale sandbox JSON and old mismatch material the same lexeme sometimes appears as `*swestēr` [Germanic/data/germanic-aligned-final.tsv:1015-1015; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4267-4269; Germanic/docs/debug_snapshots/oe_mismatch_report_new.txt:151-151; Germanic/tmp/old_english_sandbox_results_current.json:2468-2469]. For this row those are notation-layer variants inside the repo, not evidence for competing lexical policies. By contrast, forms such as `*swéstri` or `*swésterų` in the 2D search are genuinely different reconstructed paradigm cells, and DEV_NOTES treats them as analytical comparanda rather than as candidates for the live `PROTOFORM` field [Germanic/docs/DEV_NOTES.md:34010-34017,34088-34092].

The safest row-level conclusion is therefore straightforward. `swester` is the current target because DEV_NOTES concludes that it is both directly attested and the best available early/Anglian lautgesetzlich outcome; `swustor` remains valuable evidence for later West-Saxon history, but only as a late rounded or analogically remodelled form. `sweostor` remains a regular West-Saxon comparator, but the row policy adopted in §17.21 follows the project's existing precedent of preferring the attested early/Anglian form when that form is philologically secure and derivationally cleaner [Germanic/docs/DEV_NOTES.md:33576-33617,33705-33724,34101-34117].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-33524-33617

- Source heading: `§17.21.6 The Anglian attestations of swester: the decisive evidence`
- Source line or section hint: `lines 33524-33617`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `dialect_split`; `row_retarget`; `precedent`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the most directly indexable row-specific fragment because it contains both the attestation dossier and the row-policy move. DEV_NOTES states that the decisive question is whether the "lautgesetzlich Anglian form swester" is actually attested, and answers yes with specific manuscript support: Rushworth² `swester`; Rushworth¹ `swester` beside innovative `swuster`; Lindisfarne `suoester, soester`, where `soester` is treated as an orthographic reflex of the same Anglian base [Germanic/docs/DEV_NOTES.md:33524-33558]. It then states the project consequence explicitly: `swester` should be preferred over `swustor` under the `§17.16 spere/speoru` and `§17.20 tángō → tang` precedents, and row 2192 should therefore be retargeted to `swester` without changing `germanic.txt` [Germanic/docs/DEV_NOTES.md:33576-33617].

The fragment is also important because it still preserves an older explanatory layer that later needs qualification. It writes the Anglian chain as `PGmc *swestēr -> early OE *sweoster -> Anglian *swester`, i.e. a breaking-plus-smoothing story [Germanic/docs/DEV_NOTES.md:33561-33568]. That pathway is part of the row's document history, but later DEV_NOTES and the live trace now suggest that this was probably not the best mechanical account of how the current FST reaches `swester`; the row still remains solidly supported because the attestation claim and the target-switch recommendation do not depend on that older intermediate-stage wording [Germanic/docs/DEV_NOTES.md:33917-33947,33981-33993; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29063-29079].

### DEV_NOTES:line-33703-33747

- Source heading: `§17.21.8 Recommendation`
- Source line or section hint: `lines 33703-33747`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_policy`; `precedent`; `attested_target`; `implementation_choice`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest row-policy fragment. DEV_NOTES says "Option A is the clear choice: change the TSV target from swustor to swester," and then spells out why that is not just an editorial preference but the preferred implementation decision: the FST already produces `swester`; `swester` is directly attested in the Anglian record; `swustor` is a late-WS innovation; adding a late-WS rounding rule would conflate systematic sound change with a late lexical innovation; cell-switching fails; skip-listing is unnecessary because the regular form is already attested [Germanic/docs/DEV_NOTES.md:33705-33737]. This is the fragment most directly aligned with the live TSV row note [Germanic/data/germanic-aligned-final.tsv:1015-1015].

The one caution is that this recommendation still summarizes the regular chain in the older "breaking + smoothing" language [Germanic/docs/DEV_NOTES.md:33711-33716]. Because later DEV_NOTES and the published trace revise that pathway, this fragment is best used for the row-policy decision itself—why the target was switched and why `swustor` should not control the row—while the exact mechanical pathway should be cited from the later reevaluation and the current trace [Germanic/docs/DEV_NOTES.md:33971-33993; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4277-4285].

### DEV_NOTES:line-33917-33993

- Source heading: `§17.21.10.2–10.3 So how does Anglian get swester? / The FST's current behavior`
- Source line or section hint: `lines 33917-33993`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `pathway_reanalysis`; `breaking`; `smoothing`; `trace_alignment`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This late reevaluation is the best current authority for the exact derivational story. DEV_NOTES explicitly rejects the easy assumption that Anglian `swester` must come from ordinary `*sweostēr` plus canonical smoothing, because canonical Anglian smoothing is pre-velar and "`smoothing doesn't apply before /st/!`" [Germanic/docs/DEV_NOTES.md:33921-33924]. It then narrows the options and concludes that the most parsimonious account is that Anglian lacks the relevant breaking here, so `*swéstēr -> swester` directly, with no obligatory intermediate diphthong stage [Germanic/docs/DEV_NOTES.md:33926-33947].

The same fragment then reinterprets the FST accordingly. DEV_NOTES notes that the current system does not have a back-mutation rule applying before `/st/`, that `swester` therefore probably arises without WS-style breaking, and that the current output is "historically correct for Anglian" precisely because it goes straight from `*swéstēr` to `swester` [Germanic/docs/DEV_NOTES.md:33951-33961,33971-33993]. That later claim is now strongly corroborated by the published trace, where `OEBreaking` and `OEBackMutation` are both explicitly `[no-change]` for this row and the only live vowel-changing steps are suffix-side lowering/shortening/merger [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29063-29079,29091-29117].

### DEV_NOTES:line-34051-34117

- Source heading: `§17.21.11.3–11.4 Attested OE forms / Cell × form matching`
- Source line or section hint: `lines 34051-34117`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation_matrix`; `paradigm_cells`; `regular_vs_analogical`; `target_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is useful because it places the row inside the full attested form-set instead of treating `swester` and `swustor` as the only options. DEV_NOTES lists `swester`, `suoester`, `soester`, `swuster`, `sweostor`, `swostor`, `swustor`, `swyster`, and `swiostor`, with dialect and period labels, and then matches those forms against reconstructed paradigm cells [Germanic/docs/DEV_NOTES.md:34055-34072,34080-34092]. That matrix matters because it keeps three separate claims visible at once: `swester` is a real attested Anglian form; `sweostor` is also a real regular WS comparator; `swustor` is attested too, but only as a broken/analogical or innovative late form [Germanic/docs/DEV_NOTES.md:34082-34087].

The fragment's explicit winner statement is the best short-form justification for the live target if later indexing wants a single sentence. DEV_NOTES says the winning pair is `Proto cell: *swéstēr (NomSg)` and `Attested form: swester (Anglian: Northumbrian Ru², Li.; Mercian Ru¹ base layer)`, with the chain `*swéstēr -> swester` and "attestation strength" as a standard Northumbrian/Mercian form in the 9th–10th centuries [Germanic/docs/DEV_NOTES.md:34094-34117]. It also preserves the important caveat that regular WS `sweostor` remains a valid comparator, but the row policy breaks the tie in favor of Anglian `swester` by the project's earlier precedents [Germanic/docs/DEV_NOTES.md:34101-34110].

## Superseded or diagnostic material

The main superseded material is not the choice of `swester` itself but the older explanatory scaffolding around it. Early parts of §17.21 preserve two non-live attempts to explain or retain `swustor`: first, a specifically late West-Saxon labio-velar rounding account, with Brunner's quotation grouping `swustor` beside `wurold`; second, an oblique-stem analogy account in which `swustor` could be generalized from i-grade oblique material [Germanic/docs/DEV_NOTES.md:33304-33322,33326-33361]. Those explanations remain useful because they tell later writers what the sources actually said about late `swustor`, but they are not authority for the live row target.

There is also a smaller but important superseded pathway claim internal to DEV_NOTES itself. The recommendation section still summarizes `swester` as if it came from Anglian breaking plus smoothing [Germanic/docs/DEV_NOTES.md:33711-33716], whereas the later reevaluation and the current published trace now indicate that the live derivation reaches `swester` without any active `OEBreaking` or `OEBackMutation` step [Germanic/docs/DEV_NOTES.md:33971-33993; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29063-29079]. That older wording should therefore be treated as stale analytical scaffolding, not as the row's best current mechanical explanation.

Finally, stale repo-local artifacts still preserve the pre-switch state and should be fenced off as diagnostics only. The old mismatch report's "`expected swustor`" line and the sandbox JSON's stale `"counterpart": "swustor"` entry simply show that some generated artifacts have not been regenerated since the row was retargeted [Germanic/docs/debug_snapshots/oe_mismatch_report_new.txt:150-153; Germanic/tmp/old_english_sandbox_results_current.json:2467-2471]. They should not be cited against the live row, whose authoritative TSV, coverage audit, and published derivation trace now all agree on `swester` [Germanic/data/germanic-aligned-final.tsv:1015-1015; Germanic/docs/lexeme_reports/coverage_audit.md:354-354; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4266-4285].

## Open questions for later work

- If `index.tsv` is updated later, decide whether to index only the clean row-policy fragments (`33524-33617`, `33703-33747`, `33917-33993`, `34051-34117`) or also a diagnostic fragment for the late-WS `swustor` explanations; the latter are useful, but they are secondary to the live `swester` policy.
- If a later full report wants one sentence on notation, keep the distinction explicit: accented `*swéstēr` and unaccented `*swestēr` are repo-internal notation variants of the same proto lexeme, but oblique forms like `*swéstri` are genuinely different reconstructed cells and were examined only diagnostically [Germanic/data/germanic-aligned-final.tsv:1015-1015; Germanic/docs/DEV_NOTES.md:34010-34017].
- If stale generated artifacts are refreshed later, verify that the old `"expected swustor"` mismatch line and the stale sandbox `"counterpart": "swustor"` entry disappear, so that all published diagnostics consistently reflect the live row state [Germanic/docs/debug_snapshots/oe_mismatch_report_new.txt:150-153; Germanic/tmp/old_english_sandbox_results_current.json:2467-2471].
