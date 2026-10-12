---
row_id: 2314
concept: "learn (3sg)"
counterpart: liornaþ
proto: "*liznōjaną"
protoform: "*líznōθi"
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2314-learn-(3sg)-liornaþ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2314-learn-(3sg)-liornaþ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/compound_archaism_inventory.md
  - Germanic/docs/analysis/mismatch_dossier_mizdo.md
  - Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md
current_status: current_shared_weak_ii_3sg_plus_learn_family_background
needs_literature_agent: no
---

# DEV_NOTES material — 2314 learn (3sg) / liornaþ

## Current row state

- Live TSV row `2314` is `learn (3sg) / liornaþ`, with lexeme-level `PROTO = *liznōjaną`, row-level `PROTOFORM = *líznōθi`, and `DERIVATION_CLASS = late_analogy`. The live note already encodes the current project position: `Class II weak 3sg. Regular: *-ōθi → -aþ. Root has io from breaking before rn. No i-umlaut: 3sg ending never had -j-. Forms with -eþ are dialectal (Campbell §757).` [Germanic/data/germanic-aligned-final.tsv:1475-1475]
- The row is a **paradigm-cell companion**, not the learn-family lemma row. The ordinary OE lexeme row remains `2095 learn / liornian` with `PROTO = PROTOFORM = *líznōjaną`, and the sibling imperative row `2313` uses `PROTOFORM = *líznô` and target `liorna`; row `2314` is therefore the 3sg finite-cell member of the same Northumbrian-oriented learn-family treatment [Germanic/data/germanic-aligned-final.tsv:639-639,1474-1475].
- Coverage bookkeeping still treats this as a row needing its own report coverage: `coverage_audit.md` lists row `2314` under required rows with no report, `report_manifest.tsv` has no entry for `2314`, and `oe_known_problems.tsv` has no learn-row problem entry at all [Germanic/docs/lexeme_reports/coverage_audit.md:182-183; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].
- The published derivation snapshot now lands exactly on the row target: `PROTO: *líznōθi`, `EXPECTED: liornaþ`, `OUTPUTS: liornaþ`, with explicit trace stages `Rhotacism: *lírnōθi`, `PWGmc Early I Apocope: *lírnōθ`, `OE Breaking: *líornōθ`, `OE Late O Shortening: *líornaθ`, and orthographic `*líornaþ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7234-7255].
- The evidence packet and research memo are aligned with that live state. The packet marks the row as `*líznōθi -> liornaþ` and preserves both the old `*leznōθi` recommendation and the later `liorneþ -> liornaþ` correction as history; the memo explicitly says the row is late-analogy only in the operational sense that `PROTO` is the lexeme headword while `PROTOFORM` is a selected paradigm cell, even though “the **3sg phonology itself is regular** once that cell is chosen” [Germanic/docs/lexeme_reports/packets/2314-learn-(3sg)-liornaþ.md:7-14,17-44,52-86; Germanic/docs/lexeme_reports/research_memos/2314-learn-(3sg)-liornaþ.md:13-21,51-63,77-91].

## Development-note summary

Current support for row `2314` is split between **shared weak-class-II 3sg evidence** and **learn-family background**. The strongest current cell-level authority is the April 2026 DEV_NOTES correction that explicitly names rows `2310, 2312, 2314, etc.` and reverses the old assumption that regular `*-ōθi` should yield `-eþ`. DEV_NOTES now states: “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506]. For row `2314`, that is real **cell-specific** support, but it is shared with the other weak-II 3sg paradigm rows rather than unique to the learn lexeme.

The same correction supplies the row’s crucial ending analysis in quotable form. DEV_NOTES cites Campbell’s weak-class-II endings as “forms of weak verbs of Class II, **lufas, -aþ**, -od, -ad (< **-ōsi, -ōþi** …)” and adds the row-relevant principle: “There is **NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19510-19515,19540-19549]. That matches the live TSV note exactly and directly supports `PROTOFORM *líznōθi -> COUNTERPART liornaþ`, not `liorneþ` [Germanic/data/germanic-aligned-final.tsv:1475-1475].

The learn-family vowel, however, is not supported by a current row-local DEV_NOTES block devoted specifically to `2314`. What exists instead is (a) the live family alignment in the TSV (`liornian`, `liorna`, `liornaþ`) and (b) a current shared policy note that treats `líznōjaną → liornian` as an accepted transponent-style regular derivation alongside other refashioned verbs [Germanic/data/germanic-aligned-final.tsv:639-639,1474-1475; Germanic/docs/DEV_NOTES.md:37888-37898]. For the 3sg row this is **lexeme-level / family-level** support, not 3sg-only support: it tells us why the project keeps the learn family under `*lizn-` and allows Northumbrian `liorn-`, but it does not itself prove the `-aþ` ending.

The most useful learn-specific quotations still come from the older April 2026 learn note, but that note is now mixed in status. Its row-local recommendation to rewrite row `2314` as `*leznōθi` and target West-Saxon-style `leorneþ` is superseded. Its source audit remains valuable, though, because it preserves Campbell’s dialectal warning: “Beside leornian, forms with io are found in North., where original eo and io are well distinguished …” and, more specifically, “the mutation of eo was io … and never have ie” [Germanic/docs/DEV_NOTES.md:14889-14916]. Those quotations are still useful background for why the live learn-family rows may legitimately target `liorn-` rather than treating West Saxon `leorn-` as compulsory; but they should now be cited as **background retained from a superseded note**, not as the row’s live recommendation [Germanic/docs/DEV_NOTES.md:14748-14854,14889-14916].

Implementation history also matters here. DEV_NOTES preserves the intermediate regression stage where the pipeline had moved off the old `liorneþ` target but still only reached `liornoþ`, then the later stage where `*líznōθi` was listed among the forms “currently produc[ing] `liorneþ`” while `liornaþ` was the expected outcome [Germanic/docs/DEV_NOTES.md:19385-19402,19567-19576,19951-19986]. The published trace now shows that the chronology issue has been resolved and that row `2314` no longer needs to be treated as a live mismatch [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7234-7255].

## Relevant DEV_NOTES fragments

### DEV_NOTES: weak class-II 3sg correction (`§15.1`)

- Source heading: `§15.1: CORRECTION — Weak Class II 3sg Should Be -aþ, Not -eþ`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:19497-19620`
- Fragment type: `current_shared_cell_specific`
- Status: `current`
- Issue tags: `weak_class_ii_3sg`; `-ōθi_to_aþ`; `no_i_umlaut`; `dialectal_eþ`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2310`, `2312`, `2316`, `2318`

This is the controlling current DEV_NOTES fragment for row `2314`. DEV_NOTES first quotes the older TSV logic only to reject it: “Regular phonology: `*ōθi → -eþ` (i-umlaut of `*ō`).” It then states, “**This is BACKWARDS.** The actual regular outcome is `-aþ`, and the `-eþ` forms (where they occur) are the result of vowel harmony or dialectal variation” [Germanic/docs/DEV_NOTES.md:19501-19506].

For this row, the most important direct quotations are the handbook quotations preserved inside DEV_NOTES itself: Campbell §355.4 is copied as “forms of weak verbs of Class II, **lufas, -aþ**, -od, -ad (< **-ōsi, -ōþi** …)” and Campbell §757 is quoted for the caution that 2sg/3sg can “sometimes” show `-o-` or `-e-` in certain dialectal/written traditions [Germanic/docs/DEV_NOTES.md:19510-19526]. DEV_NOTES then makes the row-local phonological point explicit: “There is **NO i-umlaut** in the 3sg because: the ending `*-ōþi` never contained `-j-`” [Germanic/docs/DEV_NOTES.md:19540-19549].

Row `2314` is explicitly present in the correction tables: `| *líznōθi | liornoþ | liorneþ ❌ | liornaþ ✓ |` and later `| 2314 | liorneþ | liornaþ | Regular *ōθi → -aþ. Forms with -eþ are dialectal. |` [Germanic/docs/DEV_NOTES.md:19569-19602]. That makes this fragment more than generic class-II background: it directly covers the exact row input and output pair.

### DEV_NOTES: chronology/debugging of the `liorneþ → liornaþ` fix (`§15.0`, `§15.5`, `§15.7`)

- Source heading: regression table before `§15.1`, `§15.5 BUG ANALYSIS`, and the later chronology discussion
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:19385-19402,19951-19986,20177-20203`
- Fragment type: `current_diagnostic_implementation_history`
- Status: `current_diagnostic`
- Issue tags: `regression_history`; `late_o_shortening`; `fronting_chronology`; `row_2314`
- Recommended next use: `cite_when_explaining_why_live_trace_now_works`
- Shared with row IDs: `2310`, `2312`, `2316`, `2318`

This material is diagnostic rather than lexicographic, but it is still row-relevant. Before the correction, DEV_NOTES logged row `2314` among the affected forms as ``*líznōθi | liornoþ | liorneþ | -o- not -e-`` [Germanic/docs/DEV_NOTES.md:19385-19390]. Immediately after the correction, DEV_NOTES still described `*líznōθi → liornaþ` as a form that “currently produces `liorneþ`,” showing that the problem had shifted from the old e-grade/WS target to a chronology bug inside the weak-II pipeline [Germanic/docs/DEV_NOTES.md:19951-19986].

The decisive chronology quotation is Campbell’s: “even when shortened late, **ō became a**, but that **this a was of too late origin to become æ by Anglo-Frisian fronting** … Thus **ō if shortened early gives OE æ(e), but if shortened late it gives a**” [Germanic/docs/DEV_NOTES.md:20179-20203]. For row `2314`, this is the implementation-facing explanation of why the correct form is `liornaþ`, not `liorneþ`: the `a` in the 3sg ending is late and therefore never fronts.

### DEV_NOTES: current learn-family transponent policy (`§17.32.7`)

- Source heading: `§17.32.7 The choice: very-early vs very-late analogy`
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:37888-37898`
- Fragment type: `current_shared_lexeme_background`
- Status: `current`
- Issue tags: `learn_family`; `transponent_policy`; `lizn_family`; `family_alignment`
- Recommended next use: `cite_as_family_background_only`
- Shared with row IDs: `2095`, `2313`

This fragment is current, but it is **not** 3sg-specific. DEV_NOTES says the project has taken the “Very-early analogy” route for class-III→II refashioned verbs and then explicitly lists ``líznōjaną → liornian`` among the shapes the FST now derives “by regular sound change from this shape” [Germanic/docs/DEV_NOTES.md:37888-37898].

For row `2314`, the value of this fragment is family alignment: it confirms that the live learn-family rows may keep the `*lizn-` cognate-set label and Northumbrian-oriented `liorn-` outcomes without treating the family as an open mismatch. It does **not** by itself justify the 3sg ending `-aþ`; that part comes from the weak-II 3sg correction above [Germanic/data/germanic-aligned-final.tsv:639-639,1474-1475; Germanic/docs/DEV_NOTES.md:19497-19620].

### DEV_NOTES: superseded learn note with still-useful dialect quotations (`2026-04-07`)

- Source heading: `Extended Research (2026-04-07)` plus the preceding recommendation/solution block
- Source line or section hint: `Germanic/docs/DEV_NOTES.md:14748-14916`
- Fragment type: `background_from_superseded_note`
- Status: `mixed — superseded as row policy, still useful as source audit`
- Issue tags: `northumbrian_io`; `ws_eo`; `lezn_workaround`; `quoted_scholarship`
- Recommended next use: `cite_only_with_status_label`
- Shared with row IDs: `2095`, `2313`

This fragment must be handled carefully. Its operative row recommendation is superseded: it proposed `Row 2314: Change *liznōθi to *leznōθi` and later tabulated `2314 | *liznōθi | *leznōθi | leorneþ` [Germanic/docs/DEV_NOTES.md:14830-14854]. That is no longer the live project position.

However, the same note preserves the best still-usable learn-family quotations. Campbell §123 fn.2 is quoted as: “Beside leornian, forms with io are found in North., where original eo and io are well distinguished …” and Campbell §202 is quoted as saying that “the mutation of eo was io … and never have ie” [Germanic/docs/DEV_NOTES.md:14889-14916]. Those quotations remain useful because they support the current caution that the learn family has a real WS/Northumbrian `eo ~ io` split and that Northumbrian `liorn-` should not be erased merely because an older WS-oriented workaround once dominated the notes.

## Superseded or diagnostic material

- The earliest class-II paradigm-cell exploration for this family is purely diagnostic now. In the February 2026 results table DEV_NOTES still had `liznōθi | lierneþ | leorneþ | ✗ same root issue`, which belongs to the pre-correction stage when the project was still aiming the whole learn family at WS `leorn-` and had not yet fixed the weak-II 3sg ending analysis [Germanic/docs/DEV_NOTES.md:2948-2957].
- The April 2026 row-local rewrite to `*leznōθi / leorneþ` is superseded, not current authority. That includes both the explicit recommendation line for row `2314` and the broader note’s claim that the e-grade workaround was the correct solution for the learn family [Germanic/docs/DEV_NOTES.md:14748-14854].
- `Germanic/docs/analysis/compound_archaism_inventory.md` is stale for this row. Case 6 still says `PROTO *leznōn-`, treats `leornian` as the simplex target, and even says `TSV now targets proto *leznōn-`; that no longer matches the live TSV family (`*liznōjaną`, `liornian`, `liorna`, `liornaþ`) [Germanic/docs/analysis/compound_archaism_inventory.md:144-159; Germanic/data/germanic-aligned-final.tsv:639-639,1474-1475].
- `Germanic/docs/analysis/mismatch_dossier_mizdo.md` and its supplement are also stale/diagnostic on this point. They reuse the learn case as a precedent and explicitly summarize it as a TSV change from `*liznōjăną` to `*leznōjăną` or a DEV_NOTES change to `*leznōją` to match WS `leornian`; those statements are useful only as records of an older project phase, not as current row-2314 authority [Germanic/docs/analysis/mismatch_dossier_mizdo.md:370-373,722-729; Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:842-850].
- The packet’s old DEV_NOTES hits at `14833` and its preserved `liornoþ / liorneþ / liornaþ` correction chain are useful, but only as scaffolding. The packet itself warns not to treat all hits as equally authoritative, so primary claims for the row should still be anchored in the live TSV, DEV_NOTES, and the published derivation trace [Germanic/docs/lexeme_reports/packets/2314-learn-(3sg)-liornaþ.md:1-4,50-86,240-260].

## Open questions for later work

- Decide whether `DERIVATION_CLASS = late_analogy` should keep being read mainly as a **data-model flag for a selected paradigm cell** rather than as a claim that row `2314` itself is still philologically irregular. The current TSV note and trace treat the 3sg derivation as regular once `PROTOFORM *líznōθi` is chosen [Germanic/data/germanic-aligned-final.tsv:1475-1475; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:7234-7255].
- If `index.tsv` is revised later, decide whether row `2314` deserves a shared weak-II-3sg index entry rather than a learn-only one. Most current support is shared with rows `2310`, `2312`, `2316`, and `2318`, while the learn-family material is mostly inherited from the broader `liornian / liorna` family treatment [Germanic/docs/DEV_NOTES.md:19497-19620; Germanic/docs/lexeme_reports/coverage_audit.md:182-183].
- Clean up or explicitly mark stale the analysis files that still imply the repo “now targets” e-grade `*lezn- / leorn-` for the learn family, so later readers do not mistake diagnostic background for the live row policy [Germanic/docs/analysis/compound_archaism_inventory.md:144-159; Germanic/docs/analysis/mismatch_dossier_mizdo.md:370-373,722-729].
