---
row_id: 2227
concept: strew
counterpart: strīeġan
proto: *stráwjaną
protoform: *stráwjaną
derivation_class: reconstructed_oe
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2227-strew-strīeġan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2227-strew-strīeġan.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2227 strew / strīeġan

## Current row state

- The live OE row is `2227`, `CONCEPT strew`, `COUNTERPART strīeġan`, `PROTO *stráwjaną`, `PROTOFORM *stráwjaną`, `DERIVATION_CLASS reconstructed_oe` [Germanic/data/germanic-aligned-final.tsv:1153-1153].
- The live TSV note is already explicit that the OE target is **reconstructed, not directly attested**: “Unattested West Saxon cognate; reconstructed *strīeġan per regular WS development of PGmc *straujan-. Attested Anglian strēgan (cf. Ringe & Taylor vol.2 §6.1) proves the class 1 weak verb was inherited into English; the WS form was remodelled as class 2 strewian. We target the predicted WS reflex and deliberately do not model the Anglian-specific smoothing *ēa → *ē / _ġ” [Germanic/data/germanic-aligned-final.tsv:1153-1153].
- `PROTO` and `PROTOFORM` should be kept distinct conceptually even though they are identical in the live row. For row `2227`, both currently remain the inherited PGmc class-I input `*stráwjaną`, while `COUNTERPART` is the project’s reconstructed OE output label `strīeġan`, i.e. reconstructed WS `*strīeġan`, not the attested Anglian `strēgan` and not the attested remodelled WS class-II lemma `strewian/streowian/strēawian` [Germanic/data/germanic-aligned-final.tsv:1153-1153; @RingeTaylor2014, §6.1; @Campbell1959, §753.7].
- `oe_known_problems.tsv` has no row-local entry for row `2227`, for `strīeġan`, `strēgan`, or `*stráwjaną`; the project is therefore not currently treating this row as a separate exception-table item outside the TSV note and DEV_NOTES record [Germanic/data/oe_known_problems.tsv:1-8].
- The linked packet/research-memo infrastructure already points in the same direction as the live row: keep reconstructed WS `strīeġan`, contrast attested Anglian `strēgan`, and treat older `strēgan`/`strewian` option trees as superseded project history rather than current row policy [Germanic/docs/lexeme_reports/research_memos/2227-strew-strīeġan.md:12-16,30-37,49-70].

## Detailed development-note summary

The DEV_NOTES history for row `2227` is substantial but internally layered, so the replacement note has to separate live policy from earlier option analysis. The live row now targets reconstructed West Saxon `*strīeġan`, stored in the TSV as `COUNTERPART strīeġan`, while keeping inherited class-I `*stráwjaną` as both `PROTO` and `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:1153-1153]. That means the row is **not** presently using the attested Anglian inherited form `strēgan`, and it is **not** presently using the attested WS remodelled class-II verb `strewian/streowian/strēawian` as the OE target [Germanic/data/germanic-aligned-final.tsv:1153-1153; @RingeTaylor2014, §6.1; @Campbell1959, §753.7].

The earliest row-dedicated DEV_NOTES audit was written before that decision was settled. It opened from mismatch state `*stráwjaną → strewan` against then-target `strewian`, surveyed cognate and handbook evidence, and concluded that the inherited PGmc verb was certainly class I, while the attested WS verb was a later class-II remodelling [Germanic/docs/DEV_NOTES.md:26375-26512]. That audit preserved the crucial Ringe–Taylor quotation:

> `A WS class II weak verb streowian is well attested and must reflect remodelling of the inherited class I verb.` [Germanic/docs/DEV_NOTES.md:26433-26438; @RingeTaylor2014, §6.1 n. 27]

That quotation remains current and should be kept. What is superseded is the audit’s recommendation structure. At that stage DEV_NOTES still treated three outcomes as open project options: (A) retarget the row to a post-transfer class-II input/output such as `strēawian`, (B) retarget it to attested Anglian `strēgan`, or (C) leave `strewan` as a documented exception path [Germanic/docs/DEV_NOTES.md:26513-26575]. Those options are valuable project chronology, but they are no longer the controlling row state.

The next DEV_NOTES layer sharpened the phonological and dialectal problem. The chronology/research material accepted that whatever one thinks about earlier PWGmc `*w` gemination, both major literature camps converge on an OE-stage sequence `*au + *j`, then `*ēa + *j`, then a retained or strengthened glide written `g/ġ` in the relevant aw-series class [Germanic/docs/DEV_NOTES.md:26712-27113]. This matters because row `2227` belongs with `hīeġ`, `īeġ`, and `cīeġan`, not with ordinary `niowe/siowan`-type `*iw/*uw + j` outcomes. DEV_NOTES preserves a direct Lück passage that makes that contrast explicit and includes the row’s exact inherited lexeme class:

> `... mit ursprünglichem a: *hauwja- 'Heu', *auwjō- 'Insel', *frauwjō 'Herr', *strauwjan 'streuen', *kauwjan 'rufen' ... Die altenglischen Formen haben die normale Entwicklung durchlaufen ... angl. hēg, ēg, strēgan, cēgan, ws. hīeġ, īeġ, *frīeġea (> frīġea), cīeġan).` [Germanic/docs/DEV_NOTES.md:27192-27200; @Luick1914, §98]

The decisive shift comes in the later Q3 material. There DEV_NOTES records that Q1 and Q2 had already been implemented, that row `2061` (`hīeġ`) now matched, and that row `2227` still mismatched only because intervocalic `*j` was being vocalized to `i` instead of retained/spelled `ġ` [Germanic/docs/DEV_NOTES.md:27120-27131]. Crucially, DEV_NOTES also records the row-policy decision in plain language: “The user accepted an Option-B style TSV treatment ... target unattested WS *strīeġan, note in TSV that Anglian strēgan proves class-1 inheritance but we do not model Anglian-specific smoothing” [Germanic/docs/DEV_NOTES.md:27127-27130]. That statement matches the live TSV note and is the controlling project decision for the slice.

The Q3 literature synthesis is therefore current in result even where scholars disagree on mechanism. DEV_NOTES summarizes the convergence this way: `*j` is retained after aw-derived long front diphthongs; both Anglian and WS participate; Anglian gives `strēgan`; WS would give `strīeġan`; and the rule is narrower than a blanket “after any long diphthong” statement because the `*iu` series does **not** show the same behavior [Germanic/docs/DEV_NOTES.md:27270-27291]. The note also preserves Fulk’s useful skeptical-but-compatible formulation:

> `Rather, EWS *strīegan may be derived unproblematically from PGmc. *straujanan ...` [Germanic/docs/DEV_NOTES.md:26953-26966; @Fulk2018, §4.10 n. 1]

That quotation remains useful because it supports reconstructed WS `*strīeġan` even while rejecting a stronger gemination-and-reversal account.

The final current DEV_NOTES layer is the regression-probe section. Its practical importance is narrow but real: after i-umlaut, the entire OE corpus contained only two relevant `*Vw + *j` cases, one already solved word-finally (`hīeġ`) and one intervocalic (`strīeġan`) [Germanic/docs/DEV_NOTES.md:27367-27439]. DEV_NOTES therefore judged the new rule’s regression surface to be “empirically zero” and recommended adopting the narrow aw-series/front-diphthong `j`-retention rule so that `*stráwjaną` would surface as `strīeġan` and nothing else would move [Germanic/docs/DEV_NOTES.md:27460-27479]. For the slice, the important preserved conclusion is not merely “a rule was added,” but the contrastive lexical framing: inherited PGmc class-I `*stráwjaną`; attested Anglian inherited `strēgan`; attested WS remodelled class-II `strewian/streowian/strēawian`; project target reconstructed WS inherited `*strīeġan` [Germanic/data/germanic-aligned-final.tsv:1153-1153; Germanic/docs/DEV_NOTES.md:27127-27131,27460-27479; @RingeTaylor2014, §6.1; @Campbell1959, §753.7; @Kroonen2013, p. 483].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-26368-26575

- Source heading: `strewian / streowian / strēawian / strēgan: opinio-communis audit + lautgesetzlich-stretch analysis`
- Source line or section hint: `lines 26368-26575`
- Fragment type: `row_specific_audit_with_superseded_option_tree`
- Status: `superseded_but_explanatory`
- Issue tags: `class_i_vs_class_ii`; `attested_ws_remodelling`; `anglian_inherited_form`; `proto_vs_protoform_vs_counterpart`
- Recommended next use: `use_to_explain_project_history`
- Shared with row IDs:

This is the indispensable early row audit because it preserves the comparative and handbook split clearly. It shows that the inherited PGmc verb is class I, that attested WS `streowian/strewian/strēawian` is remodelled, and that the longest direct inherited phonological chain reaches Anglian `strēgan` [Germanic/docs/DEV_NOTES.md:26394-26487; @RingeTaylor2014, §6.1; @Campbell1959, §753.7]. Its option tree is no longer current, but its source framing still matters because it is the clearest place where DEV_NOTES states why the attested WS class-II material should not be mistaken for the direct inherited reflex of `*stráwjaną`.

> `A WS class II weak verb streowian is well attested and must reflect remodelling of the inherited class I verb.` [Germanic/docs/DEV_NOTES.md:26435-26437; @RingeTaylor2014, §6.1 n. 27]

> `PGmc *strawjanǭ → ... → Anglian OE strēgan` [Germanic/docs/DEV_NOTES.md:26471-26477; @RingeTaylor2014, §6.1]

For current row work, this fragment should be cited as superseded-but-useful chronology: it preserves the philological problem accurately, but its final A/B/C recommendation block does not control the live row anymore.

### DEV_NOTES:line-26825-26859

- Source heading: `What this means for our two targets` / `The dialect-mixing problem`
- Source line or section hint: `lines 26825-26859`
- Fragment type: `diagnostic_transition_note`
- Status: `superseded_but_explanatory`
- Issue tags: `dialect_mixing`; `anglian_smoothing`; `predicted_ws_reflex`; `target_choice_transition`
- Recommended next use: `use_to_explain_why_strēgan_was_abandoned`
- Shared with row IDs: `2061`

This fragment is worth keeping because it is the point where DEV_NOTES first states the exact target-choice dilemma later resolved in the TSV. It gives the inherited Anglian path `*strawjaną → ... → strēgan`, then immediately states the predicted but unattested WS path `*strawjaną → ... → *strīeganą → strīegan` and frames the project decision as a choice between Anglian attestation and predicted WS defaulting [Germanic/docs/DEV_NOTES.md:26825-26859].

> `WS pathway would yield (predicted but unattested): *strawjaną → ... → *strīeganą → strīegan` [Germanic/docs/DEV_NOTES.md:26835-26837]

Because the live row now explicitly chooses reconstructed WS `*strīeġan`, this fragment should be read as diagnostic chronology rather than as an open decision memo.

### DEV_NOTES:line-27116-27355

- Source heading: `Q3 RESOLUTION RESEARCH: j-strengthening / j-retention after long front diphthongs`
- Source line or section hint: `lines 27116-27355`
- Fragment type: `current_row_policy_and_literature_synthesis`
- Status: `current`
- Issue tags: `reconstructed_ws_target`; `aw_series_j_retention`; `anglian_vs_ws`; `literature_synthesis`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2061`

This is the controlling DEV_NOTES fragment for the live row state. It records that the TSV was updated to unattested WS `*strīeġan`, explains that Anglian `strēgan` remains evidential rather than target-defining, and surveys the source tradition for retaining/spelling the glide after aw-derived front diphthongs [Germanic/docs/DEV_NOTES.md:27120-27325]. It is also the best place to preserve the direct project-decision wording:

> `The user accepted an Option-B style TSV treatment ... target unattested WS *strīeġan, note in TSV that Anglian strēgan proves class-1 inheritance but we do not model Anglian-specific smoothing.` [Germanic/docs/DEV_NOTES.md:27127-27130]

The literature synthesis inside the same fragment is also important because it narrows the rule correctly. DEV_NOTES says the row belongs to the aw-series class where Anglian `strēgan` and reconstructed WS `strīeġan` are expected, but `niowe/siowan`-type iu-series forms are not comparable [Germanic/docs/DEV_NOTES.md:27270-27309; @Fulk2018, §4.10 n. 1; @Campbell1959, §402; @RingeTaylor2014, §6.1].

### DEV_NOTES:line-27359-27483

- Source heading: `q3-probes — REGRESSION PROBES`
- Source line or section hint: `lines 27359-27483`
- Fragment type: `current_probe_and_implementation_support`
- Status: `current`
- Issue tags: `narrow_rule_scope`; `row_local_match`; `zero_regression_surface`; `intervocalic_j`
- Recommended next use: `cite_if_explaining_why_rule_is_safe`
- Shared with row IDs: `2061`

This fragment matters because it turns the Q3 synthesis into a row-level engineering verdict. DEV_NOTES shows that only two OE rows contain the relevant `*Vw + *j` pattern, that row `2061` is word-final and unaffected by the medial rule, and that row `2227` is the only intervocalic case the new rule changes [Germanic/docs/DEV_NOTES.md:27367-27458]. The closing conclusion is unusually concrete and still current:

> `The rule changes exactly one form: *stráwjaną → strīeġan ... with no other form affected.` [Germanic/docs/DEV_NOTES.md:27462-27465]

That is valuable replacement-note material because it explains why the project can now keep inherited `PROTO/PROTOFORM *stráwjaną` while also keeping reconstructed WS `COUNTERPART strīeġan`, rather than retreating to a class-II workaround or an Anglian target.

## Superseded or diagnostic material

- Earlier DEV_NOTES stages that treated `strewian` or `strēawian` as possible row targets are superseded as row policy. They remain useful only to document why attested WS class-II material must not be confused with the inherited class-I reflex of the row’s `PROTO`/`PROTOFORM` [Germanic/docs/DEV_NOTES.md:26513-26575; @Campbell1959, §753.7; @RingeTaylor2014, §6.1 n. 27].
- Earlier DEV_NOTES stages that treated Anglian `strēgan` as the preferred `COUNTERPART` are likewise superseded. `strēgan` remains philologically important because it proves inheritance of the class-I verb into English, but the live project now deliberately declines to model Anglian smoothing and therefore does not use `strēgan` as the row target [Germanic/docs/DEV_NOTES.md:26825-26859,27127-27130; Germanic/data/germanic-aligned-final.tsv:1153-1153].
- The literature disagrees about mechanism — gemination residue, direct `j`-retention, or later analogical spread — but not about the practical row conclusion that aw-series material can yield Anglian `strēgan` and reconstructed WS `strīeġan` [Germanic/docs/DEV_NOTES.md:26953-27025,27285-27291; @Fulk2018, §4.10 n. 1; @RingeTaylor2014, §6.1; @Campbell1959, §§402, 753.7]. Later report writing should preserve that disagreement instead of flattening it into a falsely settled single-mechanism story.
- The live row’s spelling `strīeġan` should stay authoritative for current project work, even though some DEV_NOTES quotations and comparative discussions write predicted WS forms without the asterisk or with slightly different intermediate notation such as `strīegan`. Those are staging/orthographic variants in project history, not rival row states [Germanic/docs/DEV_NOTES.md:26835-26837,27122-27131; Germanic/data/germanic-aligned-final.tsv:1153-1153].

## Open questions for later work

- If a final lexeme report is written, it should probably quote at least one of the direct German-grammar passages now preserved in DEV_NOTES, because those passages are the clearest source-level support for reconstructed WS `*strīeġan` as distinct from attested Anglian `strēgan` and attested WS `strewian/streowian/strēawian` [Germanic/docs/DEV_NOTES.md:27174-27204; @SieversBrunner1965, §129 Anm. 2; @Luick1914, §98].
- If `index.tsv` is revisited later, decide whether the row now has enough current, row-addressable DEV_NOTES substance to index the Q3 fragments, or whether the heavy sharing with row `2061` and the amount of superseded chronology still argue for leaving the slice as no-index infrastructure.
- If later cleanup touches the TSV note, the only likely editorial improvement would be to name the attested WS remodelled variant set more fully (`strewian/streowian/strēawian`) rather than only `strewian`; no current evidence supports changing `PROTO`, `PROTOFORM`, `COUNTERPART`, or `DERIVATION_CLASS` [Germanic/data/germanic-aligned-final.tsv:1153-1153; Germanic/docs/lexeme_reports/research_memos/2227-strew-strīeġan.md:63-69].
