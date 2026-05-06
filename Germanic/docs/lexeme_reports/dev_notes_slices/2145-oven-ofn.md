---
row_id: 2145
concept: oven
counterpart: ofn
proto: *úfnaz
protoform: *úfnaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2145 oven / ofn

## Current row state

- The live OE row currently reads `COUNTERPART = ofn`, `PROTO = *úfnaz`, `PROTOFORM = *úfnaz`, `DERIVATION_CLASS = regular`, with concept `oven` and row ID `2145` [Germanic/data/germanic-aligned-final.tsv:835-835].
- The most directly relevant current DEV_NOTES audit already treats the row as internally solved: in the `-Cl/-Cn/-Cm#` check table, `*úfnaz | ofn | ofn | ✓` appears as a full target/output match [Germanic/docs/DEV_NOTES.md:29883-29899].
- The same audit also records that `ofn` is attested as an unbroken nominative singular and that broken `ofen` is attested too, specifically `Lindisfarne ofen` [Germanic/docs/DEV_NOTES.md:29905-29916].
- No row-specific `oe_known_problems.tsv` entry was found when checked for row ID `2145`, lexeme `ofn`, and protoform `*úfnaz` during slice preparation.

## Development-note summary

No securely attachable **row-numbered current** DEV_NOTES note survives for row 2145. The replacement authority is therefore composite: the live row itself, the early shared u/o-alternation discussion that mentions oven explicitly, and the later `-fn` cluster audit that confirms the dataset's present `ofn` choice as both derivationally matched and philologically defensible [Germanic/data/germanic-aligned-final.tsv:835-835; Germanic/docs/DEV_NOTES.md:122-128,29883-29916,30067-30083].

The first thing to keep explicit is that this row is **not** currently being treated like the classic OE u-retention exceptions (`wulf`, `full`, `wulle`, `fugol`, etc.). In the opening u-lowering discussion, DEV_NOTES says the FST's NWGmc u-lowering rule is regular and that the genuine problem words are those that keep `u` where `o` is predicted [Germanic/docs/DEV_NOTES.md:68-87,134-136]. `ofn` is different: the live OE target already shows the lowered vowel, so the row's present design is regular on its face, with `PROTO = PROTOFORM = *úfnaz` and no special replacement input or paradigm-cell workaround [Germanic/data/germanic-aligned-final.tsv:835-835]. What makes oven worth preserving in a slice is not a current mismatch but the fact that DEV_NOTES still records Luick's evidence for an OE-period `u/o` alternation: `*ufen/ofen* 'oven'` is listed among the later-inferred doublets, and DEV_NOTES explicitly concludes that the split “was not fully stable even in OE” and that the West Saxon literary standard “simply codified one variant” [Germanic/docs/DEV_NOTES.md:122-128]. For row 2145, that means the current target `ofn` should be read as the selected lowered variant, not as proof that no competing `u`-grade tradition ever existed.

The later cluster audit is the strongest current authority for what the dataset is actually doing with `ofn`. In §17.18.2 DEV_NOTES lists `*úfnaz | ofn | ofn | ✓`, showing that the present grammar already yields the chosen row target without extra repair [Germanic/docs/DEV_NOTES.md:29883-29899]. In §17.18.3 the same note sharpens the philological point: `ofn` has unbroken nominative-singular attestation, but broken `ofen` is also attested, specifically in Lindisfarne [Germanic/docs/DEV_NOTES.md:29905-29916]. DEV_NOTES then generalizes the register fact for the whole class: for nearly all eleven `-Cl/-Cn/-Cm#` words, the broken nominative singular is the late West Saxon prose norm, while the unbroken nominative singular survives as a poetic, earlier-prose, or Anglian variant; oblique forms such as `ofnes` remain uniformly unbroken [Germanic/docs/DEV_NOTES.md:29937-29946]. Row 2145 therefore sits at the intersection of two kinds of variation at once: root-vowel `u/o` variation in the earlier u-lowering discussion, and final-cluster `ofn/ofen` variation in the later parasiting discussion.

Current policy resolves that second variation explicitly in favor of the unbroken target. DEV_NOTES records the user's ruling: “If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them,” and then names `ofn` among the ten directly attested unbroken nominative targets that are “retained unchanged” because the dataset deliberately chooses the early / poetic / Anglian register [Germanic/docs/DEV_NOTES.md:30071-30083]. For this row, then, the distinction among the three levels is simple but still important to preserve: comparative `PROTO = *úfnaz`, OE-facing `PROTOFORM = *úfnaz`, and selected OE `COUNTERPART = ofn`. The row does **not** rely on a special OE-side proto alternant; the only thing that needs careful explanation is that the dataset currently prefers the attested unbroken lowered form `ofn` even though DEV_NOTES also preserves evidence for both vowel alternation (`*ufen/ofen`) and broken-cluster attestation (`ofen`) [Germanic/data/germanic-aligned-final.tsv:835-835; Germanic/docs/DEV_NOTES.md:122-128,29916-29916,30075-30083].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-122-128

- Source heading: `Luick's doublets evidence`
- Source line or section hint: `lines 122-128`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `u_o_alternation`; `luick`; `doublet_evidence`; `variant_history`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is the only early DEV_NOTES fragment that names oven directly in the u-lowering discussion. It says Luick's evidence includes doublets “inferred from later ME developments,” among them `*ufen/ofen* 'oven'`, and concludes that the `u/o` split “was not fully stable even in OE” while the WS literary standard simply fixed one variant [Germanic/docs/DEV_NOTES.md:124-128]. For row 2145, the fragment does not create a current exception status or a new PROTOFORM; what it establishes is narrower and still important: the lowered target `ofn` belongs to a historically variable lexical tradition, so later prose should not treat the row as though `o` were the only OE-side possibility ever contemplated in DEV_NOTES.

### DEV_NOTES:line-29883-29916

- Source heading: `§17.18 current dataset state` plus `§17.18.3 Attestation findings`
- Source line or section hint: `lines 29883-29916`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `cluster_philology`; `attestation`; `ofn_vs_ofen`; `row_selection`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current fragment for the row's actual present state. The FST/TSV table includes row 2145 as `*úfnaz | ofn | ofn | ✓`, so the live target is already a clean match rather than a pending repair [Germanic/docs/DEV_NOTES.md:29887-29895]. The immediately following attestation table then gives the lexical fact that makes the row usable as a dataset target: `ofn` has unbroken nominative-singular attestation, but broken `ofen` is also attested, explicitly “Lindisfarne *ofen*” [Germanic/docs/DEV_NOTES.md:29909-29916]. This fragment therefore secures both parts of the slice's core claim: the chosen target is derivationally correct in the current system, and the target is philologically defensible even though a broken rival form is also real.

### DEV_NOTES:line-29937-29946

- Source heading: `§17.18.3 Critical findings`
- Source line or section hint: `lines 29937-29946`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `register_choice`; `broken_vs_unbroken`; `late_ws_norm`; `oblique_forms`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1959,2136,2298`

This fragment supplies the register logic that the row-specific table entry alone does not spell out. DEV_NOTES says that for nearly all eleven words in the class, “the broken NomSg is the late-WS prose norm,” while the unbroken nominative survives as a poetic / earlier-prose variant; it then adds that the oblique stem is uniformly unbroken and lists `ofnes` among those forms [Germanic/docs/DEV_NOTES.md:29937-29946]. For row 2145, this is the clearest explanation of what kind of editorial choice the dataset is making: `ofn` is not being treated as the sole historical form, but as the deliberately selected unbroken register-form inside a system that also acknowledges late-WS `ofen`.

### DEV_NOTES:line-30067-30083

- Source heading: `§17.18.7.1 Resolved policy`
- Source line or section hint: `lines 30067-30083`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `resolved_policy`; `nom_sg_target`; `dataset_register`; `cluster_class`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1959,2136`

This is the governing current policy fragment. DEV_NOTES quotes the user rule to keep unbroken forms where they are attested, then names `ofn` among the ten rows whose unbroken nominative targets are “all directly attested manuscript spellings” and are therefore “retained unchanged” [Germanic/docs/DEV_NOTES.md:30071-30080]. It adds that the current no-parasiting behavior in `-Cl/Cn/Cm#` is correct for those lemmas because it matches the early / poetic / Anglian register chosen by the dataset [Germanic/docs/DEV_NOTES.md:30080-30083]. For row 2145, this is the best present-tense explanation of why the target is `ofn` rather than `ofen`.

## Superseded or diagnostic material

### DEV_NOTES:line-29959-29969

- Source heading: `Option 2 — Generalize FST parasiting + relemmatize TSV to broken NomSg`
- Source line or section hint: `lines 29959-29969`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `broken_nom_sg`; `ofen_proposal`; `cluster_strategy`; `rejected_option`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `1959,2136`

This fragment matters because it shows the main alternative that was explicitly considered and not adopted. DEV_NOTES briefly proposed a generalized parasiting rule plus wholesale retargeting of the class to broken nominative forms, and the sample list includes `ofen` as the row-2145 outcome [Germanic/docs/DEV_NOTES.md:29959-29965]. The same passage already notes the cost: such a move aligns the dataset with late-WS prose norms but discards the earlier / poetic / Anglian unbroken spellings [Germanic/docs/DEV_NOTES.md:29967-29969]. Since §17.18.7.1 later keeps `ofn` unchanged, this `ofen` plan belongs only to documented, rejected project history.

The broader opening section on NWGmc u-lowering should also be handled carefully for this row. It is current background, but if quoted loosely it can mislead by association: the section's central problem is the subset of lexemes that keep `u` where the rule predicts `o`, whereas row 2145 is the lowered `o`-grade row actually matching the regular rule [Germanic/docs/DEV_NOTES.md:68-87,134-136]. For oven, the usable part of that section is specifically Luick's `*ufen/ofen` doublet evidence, not the exception status attached there to `wulf`, `full`, `wulle`, `fugol`, and similar words [Germanic/docs/DEV_NOTES.md:122-128].

## Open questions for later work

- If the live TSV note is ever expanded, it would be useful to record both layers of variation explicitly: current row `*úfnaz -> ofn` is regular in the FST, but DEV_NOTES also preserves Luick's inferred `*ufen/ofen` doublet evidence and later `ofn/ofen` cluster variation [Germanic/data/germanic-aligned-final.tsv:835-835; Germanic/docs/DEV_NOTES.md:122-128,29916-29916].
- If `dev_notes_slices/index.tsv` is updated later, the securely attachable current anchors are the cluster-audit and resolved-policy fragments (`29883-29916`, `29937-29946`, `30067-30083`); the Luick doublet note (`122-128`) is best indexed as background, and the broken-`ofen` proposal (`29959-29969`) as superseded history [Germanic/docs/DEV_NOTES.md:122-128,29883-30083].
- A future source audit could tighten the manuscript-level distinction between unbroken `ofn` and broken `ofen`; the current slice can safely report only what DEV_NOTES itself securely states, namely that both are attested and that the dataset intentionally keeps the unbroken target [Germanic/docs/DEV_NOTES.md:29905-29916,30075-30083].
