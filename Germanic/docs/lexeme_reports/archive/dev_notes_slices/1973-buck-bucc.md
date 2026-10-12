---
row_id: 1973
concept: buck
counterpart: bucc
proto: *búkkaz
protoform: *búkkaz
derivation_class: unexplained_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1973-buck-bucc.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1973-buck-bucc.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1973 buck / bucc

## Current row state

- CONCEPT: `buck`
- COUNTERPART: `bucc`
- PROTO: `*búkkaz`
- PROTOFORM: `*búkkaz`
- DERIVATION_CLASS: `unexplained_unmodelled`
- Live TSV note (abridged): Campbell §115 names `bucca` as an exception to regular u-lowering/a-umlaut; the regular outcome is `**bocc` (cf. OHG `boch`/`boc`), while high-vowel cells create i-umlauted `**byċċ`-type outputs rather than the target `bucc`.
- `oe_known_problems.tsv` separately classifies `*búkkaz` as `wontfix / u_lowering_near_labial`, so the current project stance is already to document the row rather than reopen it as a presumed rule bug.
- Philological caution: handbook discussion often cites `bucca`, but the row itself targets `bucc`. DEV_NOTES treats that contrast as meaningful background rather than a reason to replace the row target.

## Development-note summary

The durable row-level conclusion is that `bucc` belongs to the same handbook-level exception cluster as `wulf`, `fugol`, and `wull`: regular stressed NWGmc/early-OE `*u` before a following non-high vowel should lower to `o`, so `*búkkaz` should produce `bocc`, not `bucc` [@RingeTaylor2014, §2.3.1; @Campbell1959, §115]. DEV_NOTES preserves the literature trail in detail rather than flattening it into a vague “labial exception” label. Bülbring explicitly includes `bucca` among forms where OE has `u` instead of expected `o`, especially “namentlich zwischen Labial und langem oder gedecktem l”, but he also concedes that “meist steht jedoch der Hauptregel gemäß o”, so the same consonantal neighborhood also yields regular lowered forms [@Bulbring1902, §116, pp. 45--46]. Luick therefore rejects a categorical phonological blocker and treats the pattern as analogical or lexical; Ringe-Taylor still accept the forms as genuine exceptions and conclude, in wording worth keeping, “We do not really know why *u failed to lower in these forms” [@Luick1914, §78 Anm. 3; @RingeTaylor2014, §2.3.1, pp. 32--33]. Campbell and Brunner preserve the same practical outcome: `bucca` belongs on the exception list, and no additional sound law is licensed by the evidence [@Campbell1959, §§115--116; @SieversBrunner1965, §68].

For row 1973 specifically, DEV_NOTES also preserves a more lexeme-specific historical complication that should not be lost. In expert consultation, Schuhmacher floated the possibility that `bucc` might “originally may have been a u-stem word,” which would make OE `u` less surprising. But DEV_NOTES immediately follows that suggestion with the repo’s own corrective check: Kroonen reconstructs the word as originally an **n-stem**, `*bukka(n)-`, with nominative `*bukō` and genitive `*bukkaz`, and Kluge-Seebold is cited for OE evidence of both `bucca` (n-stem) and `bucc` (a-stem) [@Kroonen2013, p. 82]. That means the u-stem idea survives only as an unverified hypothesis noted for completeness, not as a project-licensed solution. The useful positive takeaway is different: later reporting should keep the lexical history mixed enough to acknowledge `bucca` and `bucc`, while still treating row 1973’s target as the OE a-stem form represented in the TSV.

Project chronology matters here because this row briefly looked “solved” and then was unsolved again for good reason. A late DEV_NOTES pass tried to rescue the row by separating cognate-set headword from FST input and switching from nominative-style `*búkkaz → bucc` to gen.sg. `*búkkis → bucces`, on the theory that a following high vowel would regularly block u-lowering under Stiles’ environment (a). That proposal is now explicitly superseded. The rollback note records the deeper problem: the same `*i` that blocks u-lowering also triggers i-umlaut before apocope removes it, so paradigm cells divide into two bad groups only — low-vowel cells give lowered outputs such as `**bocc`, while high-vowel cells give fronted outputs such as `**byċċ` [@Stiles2012, §4.1.1.2]. DEV_NOTES states the row-level consequence without hedging: there is **no PGmc/NWGmc paradigm cell** from which attested `bucc` can be derived by regular sound change. That later correction, not the abandoned `*búkkis → bucces` detour, is the controlling note for current work.

The slice should therefore preserve three points together. First, the rule side is not in doubt: the FST’s `bocc`-type comparator is the regular result. Second, the philology is lexically mixed: handbook `bucca`, OE `bucca`, and OE `bucc` all matter, but they do not produce a better row-level `PROTOFORM`. Third, current project policy is deliberately conservative: keep `*búkkaz` as both `PROTO` and `PROTOFORM`, keep `bucc` as the row target, and document the lexeme as a genuine, non-derivable exception rather than forcing a paradigm-cell workaround.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-63-166

Source heading: NWGmc u-lowering Exceptions Near Labials  
Source line or section hint: lines 63-166  
Status: current  
Issue tags: u_lowering;known_exception;literature_survey;reconstruction_disagreement  
Recommended use: cite_in_final_report  
Shared with row IDs: 2030, 2162, 2298, 2300  
Text or paraphrase:
This opening survey remains the basic authority for why row 1973 is exceptional at all. It starts from the regular rule, not from the exception: stressed `*u` lowers before a following non-high vowel, so `*bukkăz` should give `bocc`/`boc`-type outcomes, just as OHG does [@RingeTaylor2014, §2.3.1; @Campbell1959, §115]. The fragment then places `bucc`/`bucca` in the small inherited cluster of OE forms that keep `u` anyway. Bülbring names `bucca` directly and frames the pattern as especially common “namentlich zwischen Labial und langem oder gedecktem l,” but in the same breath admits that “meist steht jedoch der Hauptregel gemäß o,” which prevents his consonantal observation from becoming a categorical sound law [@Bulbring1902, §116, pp. 45--46]. Luick's answer is crucial because it makes that limitation explicit: counterexamples such as `folc`, `folgian`, `bolt`, and `molcen` show that labial or velar proximity cannot simply be encoded as a blocker [@Luick1914, §78 Anm. 3]. Ringe-Taylor then preserve the negative conclusion in the most reusable form for later reporting: the forms are real exceptions, but “We do not really know why *u failed to lower in these forms” [@RingeTaylor2014, §2.3.1, pp. 32--33]. Brunner's additional wording — “In einigen Wörtern steht, zumal in der Nachbarschaft von Labialen, statt des zu erwartenden o ein u ... bucca Bock ...” — reinforces the exception status without licensing a new rule [@SieversBrunner1965, §68].

### DEV_NOTES:line-144-161

Source heading: expert consultation and follow-up on `bucc` stem history  
Source line or section hint: lines 144-161  
Status: current  
Issue tags: expert_consultation;stem_class;philology;u_lowering  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This short row-specific fragment is worth preserving separately because it records both a tempting idea and its immediate limitation. Schuhmacher remarks: “There may be additional complications such as the possibility that *bucc* originally may have been a u-stem word, in which case the vowel of Old English *bucc* would be what we expect.” DEV_NOTES does **not** adopt that as policy. The very next lines report the follow-up check against Kroonen: the lexeme is reconstructed as originally an n-stem, `*bukka(n)-`, with nominative `*bukō` and genitive `*bukkaz < *bhug-ōn, *bhug-n-ós`, and “Kluge-Seebold confirms OE had both bucca (n-stem) and bucc (a-stem). Whether there was ever a u-stem variant remains unverified” [@Kroonen2013, p. 82]. For row 1973, this fragment should be used to keep later prose honest: the u-stem idea may be mentioned as a floated possibility, but the current evidence base still points to mixed n-stem/a-stem history rather than to an attachable u-stem rescue.

### DEV_NOTES:line-25940-26067

Source heading: attempted paradigm-cell rescue for the u-lowering exception cluster  
Source line or section hint: lines 25940-26067  
Status: superseded  
Issue tags: paradigm_cell;protoform_vs_proto;project_history;source_conflict  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs: 2030, 2162, 2298  
Text or paraphrase:
This late note matters because it records the strongest abandoned attempt to regularize `bucc` without weakening the sound law. Its source audit is still useful background. Stiles is quoted for the strict conditioning of u-lowering, Campbell §115 for the explicit exception status of `bucca`, Brunner for preservation of `u` in high-vowel oblique cells, and Luick for the warning that retention near labials is still “irregular” [@Stiles2012, §4.1.1.2; @Campbell1959, §115; @SieversBrunner1965, §§68, 239]. On that basis the note proposed reinterpreting row 1973 as gen.sg. `*búkkis → bucces`, with `PROTO` left at `*búkkaz` but the row-level `PROTOFORM` switched to the `*-is` cell. That decision is no longer current. The fragment should be kept only as chronology showing that the project did test a paradigm-cell workaround and did not simply ignore it.

### DEV_NOTES:line-26126-26197

Source heading: rollback of the paradigm-cell switch; documented-exception status restored  
Source line or section hint: lines 26126-26197  
Status: current  
Issue tags: paradigm_cell;i_umlaut;u_lowering;row_policy  
Recommended use: cite_in_final_report  
Shared with row IDs: 2030, 2162, 2298  
Text or paraphrase:
This is the decisive current correction for `bucc`. After the `*-is` retargeting plan was actually applied, DEV_NOTES records that the strategy failed not just operationally but phonologically. The worked probe `wúlfi → wylf` shows the general principle: the same high vowel needed to block u-lowering also triggers i-umlaut before apocope removes it. DEV_NOTES then writes out the trap for the whole cluster, including row 1973: cells with low `*a/*ō/*ai` in the next syllable yield lowered forms such as `**bocc`, while cells with high `*i/*ī/*j` yield fronted forms such as `**byċċ` [@Stiles2012, §4.1.1.2]. The fragment states the conclusion in the form this slice should preserve: “There is no PGmc/NWGmc paradigm cell from which attested `wulf`, `fugol`, `bucc`, `rust` can be derived by regular sound change.” Campbell's exception list is then reread as evidence that these words are paradigm-wide analogical reshapes to surface `u`, not hidden regular outputs [@Campbell1959, §115]. For row 1973 this fragment is the authority that supersedes the `*búkkis → bucces` proposal and justifies the live TSV note's claim that no lautgesetzlich `PROTOFORM` is available.

## Superseded or diagnostic material

The only major superseded row-specific proposal that still needs to remain visible is the `*búkkis → bucces` detour. It is worth preserving because packets and older preserved argumentation can still surface it, and because it documents a real methodological experiment with separating `PROTO` from row-level `PROTOFORM`. But it should now be cited only as failed project history. The later rollback is explicit that high-vowel cells solve the lowering problem only by creating an i-umlaut problem, so the detour did not discover a hidden regular source for `bucc`.

A second diagnostic caution is philological rather than methodological. DEV_NOTES' live row is `bucc`, while much handbook prose and Campbell's exception list cite `bucca`. That is not noise to suppress. It is part of the lexeme's mixed OE history and should stay visible in later report writing, but it should not be turned into a claim that the row ought to be renormalized away from `bucc`.

## Open questions for later work

- Decide whether the final report should explicitly quote Campbell's `bucca buck ... OHG ... boch` formulation to keep the regular comparator visible.
- Decide how prominently to foreground the OE `bucca` / `bucc` split in the final report, so the lexeme's mixed stem history is acknowledged without obscuring that row 1973 specifically targets `bucc`.
- If later report prose mentions the floated u-stem idea, keep the caveat explicit that DEV_NOTES itself immediately followed it with Kroonen's n-stem reconstruction and the statement that any u-stem variant remains unverified.
