---
row_id: 2279
concept: weasel
counterpart: wesle
proto: *wéslōn
protoform: *wéslōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2279 weasel / wesle

## Current row state

- The live OE row now reads `CONCEPT = weasel`, `COUNTERPART = wesle`, `PROTO = *wéslōn`, `PROTOFORM = *wéslōn`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1355-1355].
- The live row note already compresses the two decisive editorial moves: `target switched from Anglian/glossary weosule to regular WS wesle ...; PROTOFORM short -on → long -ōn (ō-stem fem.)` [Germanic/data/germanic-aligned-final.tsv:1355-1355]. That note is accurate but far too compressed to replace the underlying DEV_NOTES reasoning.
- The duplicated source-note field remains only `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`. For the current row policy, that inherited source marker is not the controlling authority; the real authority is the row-specific DEV_NOTES section plus the dictionary/headword evidence cited there [Germanic/data/germanic-aligned-final.tsv:1355-1355; Germanic/docs/DEV_NOTES.md:38553-38621].
- No obvious row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found under the required support directories during the mandated check. This slice therefore has to carry the documentary burden itself rather than delegating to parallel row infrastructure.

## Development-note summary

The surviving DEV_NOTES material for row 2279 is strong and unusually self-contained, but it has to be read chronologically. The section title and mismatch snapshot preserve the **pre-fix** state: ``*wéslon → weslon (expected: weosule)`` in a bucket labelled `breaking_missing__expected_eo_got_e` [Germanic/docs/DEV_NOTES.md:38527-38535]. DEV_NOTES immediately corrects that bucket diagnosis. The problem was **not** missing breaking in a West-Saxon cascade. It was a compound row-alignment problem: the row had an OE target from an Anglian/glossary register (`weosule`) while also carrying a protoform spelling (`*wéslon`) that omitted both the long `ō` required by the ō-stem feminine and the weak-tail behavior needed to reach final `-e` [Germanic/docs/DEV_NOTES.md:38537-38550].

That two-part diagnosis remains the most important thing to preserve. First, the proto-side error: DEV_NOTES states that the old TSV input `*wéslon` lacked the medial/weak-tail configuration required for the OE derivation, and that short `-on` was not even licensed by the relevant weak-tail cell, whereas long `-ōn` was. The note is explicit: `wéslōn → wesle` works, but `wéslon → weslon` does not [Germanic/docs/DEV_NOTES.md:38545-38550]. Second, the target-side error: the expected OE form had been set to `weosule`, but DEV_NOTES argues that this is not the unmarked West Saxon target for the row; it is the glossary/Anglian form, whereas the regular West Saxon citation form is `wesle` [Germanic/docs/DEV_NOTES.md:38555-38561,38583-38588].

The source audit inside DEV_NOTES is the decisive philological core. Orel gives `*wes(u)lōn sb.f.` with `OE wesle`, not `weosule` [Germanic/docs/DEV_NOTES.md:38555-38557; docs/references/orel_handbook_germanic_etymology.vision.txt:50600-50602; @Orel2003, p. 456]. Clark Hall's headword is equally clear about hierarchy: `wesle, weosule (GL) f. 'weasel.'` The unqualified lemma is `wesle`; `weosule` is retained only as a glossary-marked form [Germanic/docs/DEV_NOTES.md:38559-38561; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48099-48099; @ClarkHall1960, s.v. "wesle"]. DEV_NOTES then preserves the older evidence strand that had pulled the row toward `weosule`: Bülbring uses Corpus Glossary `uueosule 'Wiesel'` as an example of back-mutation/u-umlaut development, but also describes West Saxon as favoring the change only across labials and liquids, with dentals and nasals tending to inhibit it [Germanic/docs/DEV_NOTES.md:38563-38568; docs/references/bulbring_altenglisches_elementarbuch.txt:4884-4894,4915-4917; @Bulbring1902, §§229.1, 229.4]. In other words, Bülbring helps explain **why** `weosule` exists, but not why it should control the main WS row target.

Campbell is used in DEV_NOTES as the dialectal arbiter. The note quotes §205 to the effect that in West Saxon back-mutation applies only when the intervening consonant is a labial or liquid, whereas Anglian is much broader [Germanic/docs/DEV_NOTES.md:38570-38581; @Campbell1959, §205]. That matters directly because the consonant between stressed `e` and the following back-vocalic environment in `wesle / weosule` is `s`, exactly the sort of environment DEV_NOTES says the current `OEBackMutation` rule **should not** mutate in a WS-target cascade [Germanic/docs/DEV_NOTES.md:38579-38588]. The section therefore treats the FST as **right** and the earlier row specification as wrong-register and wrong-protoform, not as a sound-change defect requiring code work.

The probe matrix makes the chronology concrete. DEV_NOTES records `*wéslōn → wesle ✓`, `*wéslōz → wesle ✓`, `*wéslon → weslon ✗`, and `*wésulô → wesola ✗` across `/s/`, while parallel labial/liquid controls like `*xébulô → heofola`, `*wéfulô → weofola`, `*wélulô → weolola`, `*wérulô → weorola` succeed [Germanic/docs/DEV_NOTES.md:38596-38608]. This is exactly the evidentiary pattern required for the current editorial conclusion: the cascade already behaves like West Saxon, so the row should be aligned to `wesle`, not broadened to an Anglian back-mutation target.

The `PROTO` / `PROTOFORM` / `COUNTERPART` distinction is especially important here because the row changed on both the proto side and the OE side. `PROTO = *wéslōn` is now the comparative proto label attached to the cognate set in the aligned TSV [Germanic/data/germanic-aligned-final.tsv:1355-1355]. `PROTOFORM = *wéslōn` is the actual derivational input now fed into the OE cascade; the crucial change from the older DEV_NOTES heading is that the live row no longer uses short `-on` [Germanic/docs/DEV_NOTES.md:38545-38550; Germanic/data/germanic-aligned-final.tsv:1355-1355]. `COUNTERPART = wesle` is the selected OE citation form. `weosule` survives only as a superseded target and as a genuine dialectal/glossarial comparator, not as the live `COUNTERPART` [Germanic/docs/DEV_NOTES.md:38559-38561,38614-38618].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-38531-38550

- Source heading: `§17.37 *wéslon → weslon (expected weosule): triage as TSV target/proto issue`
- Fragment type: `diagnosis_of_pre_fix_row_state`
- Status: `mixed_current_and_diagnostic`
- Issue tags: `protoform_length`; `weak_tail`; `misbucketed_breaking`; `pre_fix_snapshot`
- Recommended next use: `cite_for_row_history_and_proto_correction`
- Shared with row IDs:

This fragment is partly stale in surface form but still essential. It preserves the exact mismatch string and the immediate technical reason the old row could not possibly derive: `*wéslon` stayed unchanged because no rule fired, and short `-on` did not match the weak-tail environment that would yield final `-e` [Germanic/docs/DEV_NOTES.md:38531-38550]. Future work should quote this block only with the explicit caveat that the live row has already adopted the recommended repair `*wéslōn`; otherwise the old heading can misleadingly look like the current row specification. As row history, however, it is the strongest surviving statement of why the protoform correction was not cosmetic but structurally necessary.

### DEV_NOTES:line-38553-38588

- Source heading: `§17.37 ... Source audit` / `Diagnosis`
- Fragment type: `row_specific_source_audit`
- Status: `current`
- Issue tags: `wesle_vs_weosule`; `west_saxon_targeting`; `back_mutation_scope`; `dictionary_hierarchy`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs:

This is the best single anchor for the row's present documentary status. It quotes Orel and Clark Hall directly, explains that `weosule` is glossary-marked while `wesle` is the unqualified lemma, and ties that lexical evidence to Campbell's West-Saxon restriction on back-mutation [Germanic/docs/DEV_NOTES.md:38555-38561,38570-38588]. It is also the clearest place where the note says, in near-final policy language, that "`weosule` is the **Anglian / Corpus-Glossar** form" and that "The **regular West Saxon outcome is `wesle`**" [Germanic/docs/DEV_NOTES.md:38585-38587]. If any DEV_NOTES lines deserve later indexing, these do.

### DEV_NOTES:line-38596-38621

- Source heading: `§17.37 ... FST probe matrix` / `Plan`
- Fragment type: `verification_and_row_action`
- Status: `current_for_reasoning`
- Issue tags: `probe_matrix`; `ws_control_forms`; `row_edit_plan`; `no_fst_change`
- Recommended next use: `cite_for_implementation_rationale`
- Shared with row IDs:

This fragment matters because it turns the philological argument into an implementation policy: `*wéslōn → wesle` already works, the `/s/` environment correctly resists West-Saxon back-mutation, and the recommended action was to edit only row 2279 rather than touch `OEBackMutation` [Germanic/docs/DEV_NOTES.md:38596-38621]. Although the section still says `pending user confirmation`, the live TSV now reflects exactly that plan, so the block should be read as an already-executed recommendation rather than an open proposal [Germanic/data/germanic-aligned-final.tsv:1355-1355]. This is the best fragment for explaining why the row remains `regular`: the fix was alignment, not an exception class or a code patch.

## Superseded or diagnostic material

- The section title `*wéslon → weslon (expected weosule)` is no longer the live row state. It should be preserved as pre-correction history only. Both `PROTO` and `PROTOFORM` in the TSV are now `*wéslōn`, and the live `COUNTERPART` is already `wesle` [Germanic/docs/DEV_NOTES.md:38527-38535; Germanic/data/germanic-aligned-final.tsv:1355-1355].
- The bucket label `breaking_missing__expected_eo_got_e` is explicitly called misleading by DEV_NOTES itself. The row is not a smoothing/breaking failure in the relevant current account; it is a back-mutation register issue compounded with a protoform-length/weak-tail issue [Germanic/docs/DEV_NOTES.md:38534-38538].
- Bülbring's `uueosule` evidence should remain in the slice because it explains the origin of the superseded target, but it should not be cited as if it overruled the current WS-targeting decision. In present project policy it is diagnostic support for the existence of an Anglian/glossarial variant, not authority for the row's main `COUNTERPART` [Germanic/docs/DEV_NOTES.md:38563-38568; docs/references/bulbring_altenglisches_elementarbuch.txt:4915-4917; @Bulbring1902, §229.4].
- The alternative plan to keep `weosule` and model a broader Anglian `OEBackMutation` is likewise preserved only as an explicitly non-recommended branch. DEV_NOTES rejects it because it would conflict with established WS-target policy and would risk silent regressions across other rows [Germanic/docs/DEV_NOTES.md:38623-38633].

## Open questions for later work

- If this row is ever promoted into a final lexeme report, it should keep the chronology explicit: first identify the old `*wéslon` / `weosule` mismatch, then separate the protoform repair (`-on` → `-ōn`) from the target repair (`weosule` → `wesle`), rather than collapsing both into a single vague "normalization" statement [Germanic/docs/DEV_NOTES.md:38545-38550,38614-38618].
- The live row note is usable but still too compressed for independent philological review. A later cleanup could profitably spell out that `weosule` remains a real Anglian/glossarial comparator while `wesle` is the selected West Saxon headword target [Germanic/data/germanic-aligned-final.tsv:1355-1355; Germanic/docs/DEV_NOTES.md:38559-38561,38585-38588].
- For `index.tsv`, the strongest candidate anchors are the source-audit/diagnosis lines `DEV_NOTES:line-38553-38588` and the probe/plan lines `DEV_NOTES:line-38596-38621`. The earlier mismatch snippet `DEV_NOTES:line-38531-38550` is useful context, but it is less safe as a primary anchor because its title and example preserve the superseded pre-fix row state.
