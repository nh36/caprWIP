---
row_id: 2034
concept: fright
counterpart: fyrhte
proto: *furxtīn
protoform: *fúrxtīnaz
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2034-fright-fyrhte.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2034-fright-fyrhte.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/fryhtu_investigation.md; Germanic/docs/analysis/four_complex_tsv_items.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2034 fright / fyrhte

## Current row state

- CONCEPT: `fright`
- COUNTERPART: `fyrhte`
- PROTO: `*furxtīn`
- PROTOFORM: `*fúrxtīnaz`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note (quoted closely): the row now targets the attested oblique paradigm cell `fyrhte`; bare-stem nominal `*fyrht` is treated as unattested; `*fúrxtīnaz` was chosen deliberately as a true PGmc oblique input whose longer tail tests the repaired chronology, while `*fúrxtīni`, `*fúrxtīnų`, `*fúrxtīniz`, and post-apocope `*fúrxtīn` also converge on `fyrhte` in the current cascade [Germanic/data/germanic-aligned-final.tsv:403; Germanic/docs/lexeme_reports/packets/2034-fright-fyrhte.md:7-9].
- `oe_known_problems.tsv` has no row for this item, so current project policy treats row 2034 as a documented row-design decision rather than an open mismatch bucket [Germanic/docs/lexeme_reports/packets/2034-fright-fyrhte.md:45-47].
- `report_manifest.tsv` has no entry for row 2034, so this slice has to function as the working replacement note rather than as a pointer to a pilot/full report [Germanic/docs/lexeme_reports/packets/2034-fright-fyrhte.md:11-13].
- The packet and research memo agree on the row's three-way distinction: lexeme-level `*furxtīn-`, row-level derivational input `*fúrxtīnaz`, and OE target `fyrhte`; older analyses in `*fúrxtiθō`, `fyrhtu`, and bare `*fyrht` survive only as project history [Germanic/docs/lexeme_reports/research_memos/2034-fright-fyrhte.md:56-65,77-95].

## Development-note summary

The first durable conclusion is philological, not merely technical: the OE fear noun behind this row is not a primary `*-iþō` abstract. DEV_NOTES preserves Orel's wording, "`*furxtīn` sb.f.: Goth faurhtei 'fright, fear', OE fyrhtu id. Cf. also OHG forahta id. Derived from *furxtaz`," and then aligns that with Ringe–Taylor's statement that the in-stems "`do not owe their ending -u to the *iþō-stems ...; the reverse is much more likely`" [DEV_NOTES:line-40667-40732; @Orel2003, p. 120; @RingeTaylor2014, pp. 380-381]. Campbell's in-stem discussion gives the same basic shape from the OE side: oblique forms should show `-e < -i < -in`, while nominative `-u/-o` is later analogical spread [DEV_NOTES:line-40715-40732; @Campbell1959, §589.7]. That means the old repo use of `*fúrxtiθō` was not a rival scholarly reconstruction; it was a project hack introduced to force `fyrhtu`, and DEV_NOTES now explicitly says so [DEV_NOTES:line-40753-40833].

The next durable conclusion is that the first corrective answer, bare nominal `*fyrht`, is also not the surviving row policy. DEV_NOTES' corpus review writes out the regular in-stem paradigm and then makes the row-level claim that matters most: "`every singular case` of `*fúrxtīn-` is `fyrhte`," whereas `fyrhtu / fyrhto` are analogically remodeled nominatives [DEV_NOTES:line-40877-41015; @RingeTaylor2014, pp. 380-381; @Campbell1959, §589.7; @SieversBrunner1965, §280]. That dossier also preserves the attested oblique evidence the row now depends on: BT examples such as `mid mycelre fyrhte was geslegen`, `Mid fyrhte fornumene`, `Hi swyde mid þære fyrhte wæron geslegene`, and `oppe on fyrhte` show that `fyrhte` is not a reconstructed convenience form but an attested oblique noun [DEV_NOTES:line-40921-40944]. Just as importantly, the same note rejects bare `fyrht` as the target because Clark Hall and Bosworth–Toller do not attest it as the noun: Clark Hall has "`fyrht  I. afraid, timid. [forht]   II. = freht`," while BT gives only the divination homonym there [DEV_NOTES:line-40945-40971]. The working consequence is explicit: row 2034 should target attested oblique `fyrhte`, not dictionary-lemma `fyrhtu` and not unattested nominal `*fyrht`.

The sound-law basis for that target is also now stable enough to carry forward without repeated return to DEV_NOTES. The controlling note is the in-stem suffix chronology: after PGmc final-`z` deletion and high-vowel losses have reduced the oblique endings to bare `*-īn`, a regular post-PWGmc change removes final `-n` after unstressed `*ī`, yielding `*-ī`; OE unstressed long-vowel shortening then gives `*-i`, and OE unstressed lowering/surface realization yields `-e` [DEV_NOTES:line-41164-41230; @RingeTaylor2014, §3.3.1, pp. 87-88; @Campbell1959, §§473, 589.7; @Fulk2018, §7.34]. DEV_NOTES quotes the key textbook formulation directly: "`-e < -i < -in`" for the oblique cases of these abstract feminines [DEV_NOTES:line-41201-41205; @Campbell1959, §589.7]. The row therefore does not depend on a special OE-side analogical `-e`; `fyrhte` is the regular oblique continuation once the lexeme is correctly treated as an in-stem.

What changed later was not the row target but the preferred PGmc input used to exercise the cascade. DEV_NOTES first proved the oblique-cell solution with post-apocope `*fúrxtīn`, then widened the proto-gate to true PGmc oblique forms and exposed chronology bugs: an early probe gave mixed results (`*fúrxtīnaz → fyrhten`, `*fúrxtīni → fyrhte`, `*fúrxtīniz → fyrhte`), and a second round fixed gen.sg. at the cost of breaking other cells [DEV_NOTES:line-41332-41505]. Those rounds are no longer current policy, but they remain useful because they document why the final chronology had to be placed where it now is. After the final move of `NWGmcInStemNLoss` to the post-apocope position, DEV_NOTES records the current stable result: `*fúrxtīnaz`, `*fúrxtīni`, `*fúrxtīnų`, `*fúrxtīniz`, and `*fúrxtīn` all derive `fyrhte` [DEV_NOTES:line-41751-41765]. The later stressed-long-`ī` tier note then explains why row 2034 itself stays on plain `*ī`: among the rows with long `ī`, this one is the lone case where the vowel is the **unstressed feminine in-stem suffix**, "`*fúrxtīn → fyrhte` — kept as `*ī` (this is the form `NWGmcInStemNLoss` is supposed to consume)`" [DEV_NOTES:line-41893-42040]. That is why the live TSV now prefers gen.sg. `*fúrxtīnaz`: it is a true PGmc surface form, it exercises the full oblique tail, and it still converges on the same attested OE target as the other oblique cells [Germanic/data/germanic-aligned-final.tsv:403; Germanic/docs/lexeme_reports/research_memos/2034-fright-fyrhte.md:97-107].

The row's `late_analogy` label therefore needs to be read carefully. `fyrhte` itself is not the analogical problem; it is the regular oblique output. The analogical material belongs to the better-known nominative lemma forms `fyrhtu / fyrhto` and to the older project attempts either to force those lemma forms directly from the FST or to retreat to unattested `*fyrht` [DEV_NOTES:line-40683-40713; DEV_NOTES:line-41003-41015; Germanic/docs/lexeme_reports/research_memos/2034-fright-fyrhte.md:81-95]. Later reporting should keep that distinction explicit.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-40667-40732

- Source heading: `source claims on the OE fear noun as an in-stem, not an iþō-stem`
- Source line or section hint: `lines 40667-40732`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `proto_reconstruction`; `in_stem`; `analogical_u`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the first row-specific authority that still survives intact. It preserves the scholarly correction that made later row work possible. Orel is quoted directly: "`*furxtīn` sb.f.: Goth faurhtei 'fright, fear', OE fyrhtu id. Cf. also OHG forahta id. Derived from *furxtaz.`" DEV_NOTES then aligns that with Ringe–Taylor's explanation that native learners replaced original nom.sg. `*-i` with `*-u`, and that "`the in-stems do not owe their ending -u to the *iþō-stems ...; the reverse is much more likely`" [@Orel2003, p. 120; @RingeTaylor2014, pp. 380-381]. Campbell's in-stem summary is used in the same way: oblique `-e < -i < -in`, nominative `-u/-o` analogical [@Campbell1959, §589.7]. For row 2034 this fragment is the philological baseline: any analysis that still starts from `*fúrxtiθō` is already off the current path.

### DEV_NOTES:line-40753-40833

- Source heading: `diagnosis of the old fúrxtiθō workaround and interim fyrht recommendation`
- Source line or section hint: `lines 40753-40833`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `project_history`; `hack_protoform`; `retargeting`; `superseded_decision`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment should be kept because it explains two older repo states that later packet work can still surface. DEV_NOTES says outright that `*fúrxtiθō` was a TSV fix introduced so the older cascade would output `fyrhtu`, and that once the apocope gap was closed the hack collapsed to `fyrht`. The note then recommends the first "honest phonology" repair: restore `*furxtīn-` and retarget the row to bare `fyrht`. That recommendation is no longer current, but it remains valuable chronology because it shows the project did not move directly from `fyrhtu` to `fyrhte`; there was an intermediate stage where unattested `*fyrht` looked methodologically cleaner than the analogical lemma.

### DEV_NOTES:line-40877-41015

- Source heading: `expected paradigm, attested oblique fyrhte, and rejection of bare nominal fyrht`
- Source line or section hint: `lines 40877-41015`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `paradigm_cell`; `oblique_target`; `homonymy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core attachment for the current row design. DEV_NOTES writes out the inherited paradigm and then states the row-level conclusion in reusable form: "`every singular case` of `*fúrxtīn-` is `fyrhte`," while `fyrhtu / fyrhto` are analogical nominatives [@RingeTaylor2014, pp. 380-381; @Campbell1959, §589.7; @SieversBrunner1965, §280]. It then backs that up with attested noun examples from Bosworth–Toller: `mid mycelre fyrhte was geslegen`, `Mid fyrhte fornumene`, `Hi swyde mid þære fyrhte wæron geslegene`, `oppe on fyrhte`, and `þære fyrhte`. The same fragment also preserves the decisive negative evidence against retargeting to bare `fyrht`: Clark Hall's "`fyrht  I. afraid, timid. [forht]   II. = freht`" and BT's divination entry show that the noun is not attested there. For row 2034, this fragment is why the present target is specifically the oblique cell `fyrhte`.

### DEV_NOTES:line-41164-41230

- Source heading: `post-PWGmc n-loss after unstressed long ī and the route to OE -e`
- Source line or section hint: `lines 41164-41230`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `sound_change`; `n_loss`; `suffix_chronology`; `derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment preserves the actual phonological chain that justifies `fyrhte` as a regular oblique outcome rather than a documentation-only compromise. DEV_NOTES quotes Ringe–Taylor's statement that "`By regular sound changes the obl. sg. of in-stems became *-īn`" and then assembles the next step from R/T, Campbell, Brunner, and Fulk: post-PWGmc word-final `-n` after unstressed `*ī` is lost, producing `*-ī`, which later shortens to `*-i` and surfaces as `-e` [@RingeTaylor2014, §3.3.1, pp. 87-88; @Campbell1959, §§473, 589.7; @SieversBrunner1965, §280; @Fulk2018, §7.34]. Campbell's concise formula "`-e < -i < -in`" is the part later writers will actually need to quote. The fragment still uses post-apocope `*fúrxtīn` as the worked comparator, so later notes should pair it with the final protoform fragment below rather than treat `*fúrxtīn` as the current TSV input.

### DEV_NOTES:line-41332-41505

- Source heading: `gate widening and failed probe rounds while testing true PGmc oblique forms`
- Source line or section hint: `lines 41332-41505`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `probe_history`; `chronology_bug`; `protoform_selection`; `implementation_diagnostics`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is diagnostic rather than authoritative, but it should survive because it explains why `*fúrxtīnaz` was not adopted casually. DEV_NOTES first widened the proto-gate to full PGmc oblique forms and immediately found that the chronology was wrong: round one gave `*fúrxtīnaz → fyrhten` and `*fúrxtīnun → fyrhtenon`, while round two fixed the genitive only by breaking dative, accusative, and plural cells. The note's lasting value is methodological: it records that the row was stress-tested against several true PGmc cells before the current protoform was accepted, and that the final decision depends on resolving chronology, not on pretending the first true-PGmc probe already worked.

### DEV_NOTES:line-41751-42040

- Source heading: `final five-cell convergence and stressed-long-ī distinction`
- Source line or section hint: `lines 41751-42040`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `probe_confirmation`; `protoform_choice`; `stress_tier`; `current_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the final current authority for the live row state. After the chronology repair, DEV_NOTES records that all five relevant oblique inputs now converge: `*fúrxtīnaz`, `*fúrxtīni`, `*fúrxtīnų`, `*fúrxtīniz`, and `*fúrxtīn` all yield `fyrhte`. The immediately following stressed-long-`ī` note then explains why row 2034 keeps plain `*ī` while other rows with stressed root `ī` migrate to `*ḯ`: "`1` is the unstressed feminine in-stem suffix in `*fúrxtīn → fyrhte` — kept as `*ī` (this is the form `NWGmcInStemNLoss` is supposed to consume)`." That is the missing bridge between the earlier n-loss dossier and the live TSV choice of gen.sg. `*fúrxtīnaz`: the row now uses a true PGmc oblique form, but the suffixal `*ī` must remain on the unstressed tier so the repaired chronology still produces `fyrhte`.

## Superseded or diagnostic material

The major superseded material falls into three layers. First, the old `*fúrxtiθō → fyrhtu` solution is now useful only as history of an abandoned workaround; it should never again be cited as current lexeme reconstruction [DEV_NOTES:line-40753-40833]. Second, the interim `*furxtīn → fyrht` recommendation is also superseded, not because its phonology was impossible, but because DEV_NOTES later established that the noun `fyrht` is unattested and that attested oblique `fyrhte` is the better row target [DEV_NOTES:line-40945-40971].

Third, the first two true-PGmc probe rounds are diagnostic only. Their value is that they preserve the chronology failures that had to be fixed before `*fúrxtīnaz` could be adopted confidently, but they should not be mistaken for the present derivation state [DEV_NOTES:line-41332-41505]. The packet and memo also flag two related analysis files as stale for current work: `Germanic/docs/analysis/fryhtu_investigation.md` and the row-2034 material in `Germanic/docs/analysis/four_complex_tsv_items.md` still argue from older `*furhtiþō/*fúrxtiθō` or `fyrhtu` assumptions and should be cited, if at all, only as superseded project history [Germanic/docs/lexeme_reports/research_memos/2034-fright-fyrhte.md:27-31,121-122].

## Open questions for later work

- Decide whether the final report should quote one or two of the BT oblique examples directly, so the choice of `fyrhte` is visibly anchored in attestation rather than only in paradigm reconstruction.
- Decide how prominently to foreground the nominative-lemma problem (`fyrhtu / fyrhto / fryhto`) in the final report, since it explains `late_analogy` but is no longer the row target.
- If a future row-level report includes a derivation table, reuse the five-cell oblique probe explicitly and label bare `*fúrxtīn` as a post-apocope convenience comparator, not as the current TSV `PROTOFORM`.
- If stale dossier material is ever refreshed, make the supersession chain explicit: `*fúrxtiθō` hack → interim `*fyrht` proposal → current `*fúrxtīnaz → fyrhte` oblique-cell solution.
