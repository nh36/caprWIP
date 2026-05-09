---
row_id: 2297
concept: wold
counterpart: weald
proto: *wálθuz
protoform: *wálθuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2297-wold-weald.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current_row_kept_as_regular_weald_with_variant_background_only
needs_literature_agent: no
---

# DEV_NOTES material — 2297 wold / weald

## Current row state

- The live OE row is `2297 | ... | weald | ... | regular`, with TSV note `Kroonen p.572 *walθu- > OE weald; wald is Anglian (R/T p.313 WS wealdan vs Merc. waldan)`; in the live table, `PROTO` and `PROTOFORM` are both `*wálθuz`, while the OE target/counterpart is `weald` [Germanic/data/germanic-aligned-final.tsv:1424-1424].
- Coverage status is still unresolved at report level rather than derivation level: the coverage audit lists row `2297 | wold | weald | regular | yes | ... | no report`, and `report_manifest.tsv` has no row-specific manifest entry for 2297 [Germanic/docs/lexeme_reports/coverage_audit.md:171-173; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The packet and research memo both already converge on the same operational reading: keep the row targeted to normalized OE `weald`; treat `wald` and cross-referred `wold` as variant/background evidence only, not as replacement row targets [Germanic/docs/lexeme_reports/packets/2297-wold-weald.md:5-10,15-18,37-41; Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:5-17,31-37,56-66].
- Current supporting lexicography is consistent with that choice. Kroonen's noun entry gives the etymon as OCR `*walpu-` (= `*walþu-`) with `OE weald m. 'wood'`, alongside OFri./OS/OHG `wald`; Clark Hall gives `wald (N,VPs) weald`, then the main headword `weald ... forest, wood, grove`, with explicit cross-reference `['wold']`, and finally `wold weald` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28989-28991; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47025-47025,47214-47218,49487-49487].
- `oe_known_problems.tsv` presently has no entry for `*wálθuz` / `weald`; that matches the memo's conclusion that the row is not a live mismatch-class item [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:37-37].
- A caution from current debug material: the sandbox snapshots in `Germanic/tmp/` still show a stale OE counterpart/output set centered on `wald` and even a failed staged surface `walþ`; those files are diagnostic only and do **not** reflect the live aligned TSV target or the packet/memo recommendation [Germanic/tmp/old_english_sandbox_results_current.json:3489-3498; Germanic/tmp/old_english_sandbox_results_with_stages.json:52629-52769].

## Development-note summary

No substantial row-specific DEV_NOTES block survives for 2297. The surviving in-repo DEV_NOTES material is thin and should be treated conservatively: one shared phonology note on PWGmc `*lþ → *ld`, and one later inventory line explicitly classifying row 2297 as `breaking` [Germanic/docs/DEV_NOTES.md:1320-1358,30630-30639]. There is **not** a bespoke DEV_NOTES narrative for why `wold / weald` was debated, repaired, or retargeted.

The safe row reading is therefore composite:

- **PROTO / comparative etymon:** the noun family belongs with Kroonen's `*walþu-` stem (OCR `*walpu-` in the local text), i.e. the lexeme whose cognates include OE `weald`, OFri./OS `wald`, and OHG `wald` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28989-28991].
- **PROTOFORM / project input:** the live derivational input remains nominative-singular `*wálθuz`; nothing in surviving DEV_NOTES proposes a different engineering protoform, a paradigm-cell switch, or a diagnostic surrogate [Germanic/data/germanic-aligned-final.tsv:1424-1424; Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:41-48].
- **OE target / counterpart:** the row is normalized to `weald`, not `wald` and not `wold`; `wald` is retained only as dialectal/Anglian-style background, and `wold` as a cross-referred variant spelling/form in dictionary material [Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:49-55,58-66; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47025-47025,47214-47218,49487-49487].

The only strong DEV_NOTES anchor for the actual OE development is the inventory line `| 2297 | *wálθuz | weald | breaking |` [Germanic/docs/DEV_NOTES.md:30639-30639]. That should be read together with the earlier shared note that, per DEV_NOTES' Ringe-Taylor summary, word-internal `*lþ → *ld` was a regular change in Northern/Proto-West Germanic [Germanic/docs/DEV_NOTES.md:1324-1333]. For this row, then, the working phonological path is still the ordinary one preserved in the packet and memo: `*wálθuz > *wálduz > *wáldu > *wældu > *wealdu > weald` [Germanic/docs/lexeme_reports/packets/2297-wold-weald.md:17-42; Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:43-48].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30630-30639

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line hint: `Germanic/docs/DEV_NOTES.md:30630-30639`
- Fragment type: `shared_row_classification_inventory`
- Status: `current`
- Issue tags: `breaking`; `row_classification`; `regular_target`; `shared_background_only`
- Recommended next use: `primary_in_repo_anchor_for_row_2297`
- Shared-with rows if relevant: `1975; 2025; 2077; 2118; 2166; 2167; 2204; 2289; 2297`

This is the only clearly row-naming DEV_NOTES fragment that survives in directly reusable form. The row appears as the bare but decisive line `| 2297 | *wálθuz | weald | breaking |` [Germanic/docs/DEV_NOTES.md:30639-30639]. Its value is row-specific but narrow: it does **not** supply a special controversy, only the classification that the row belongs with the ordinary OE breaking set. Because the surrounding inventory also includes closely parallel `a + liquid/cluster` rows such as `*fálþaną > fealdan`, `*xáldaną > healdan`, and `*sáltą > sealt`, the line is best read as evidence that 2297 was reviewed as one more regular member of that class rather than as an exception requiring a custom repair [Germanic/docs/DEV_NOTES.md:30631-30638].

### DEV_NOTES:line-1320-1358

- Source heading: `PWGmc *lþ → *ld Voicing and Verner's Law Overlap`
- Source line hint: `Germanic/docs/DEV_NOTES.md:1320-1358`
- Fragment type: `shared_phonology_background`
- Status: `shared-background-only`
- Issue tags: `lþ_to_ld`; `pre_breaking_stage`; `verner_boundary`; `not_row_specific`
- Recommended next use: `use_for_proto_side_stage_explanation_only`
- Shared-with rows if relevant: `2025 fealdan; 2297 weald; and any other *lþ items`

This is not a row-2297 note, but it preserves the background change needed before the row can reach the later breaking environment. DEV_NOTES states: `R/T vol.2 §5.1.3 (pp. 170-171): word-internal *lþ → *ld was a regular sound change in Northern WGmc (= PWGmc). Implemented as PWGmcLThVoicing` [Germanic/docs/DEV_NOTES.md:1324-1326]. The exemplars are other lexemes (`*falþaną → *faldaną → OE fealdan`, `*balþaz → *bald → OE beald`, etc.), not `*wálθuz` itself [Germanic/docs/DEV_NOTES.md:1328-1333]. For 2297, its role is therefore shared-background-only: it licenses the intermediate `*wáld-` stage but does not by itself decide the OE headword or dialect choice.

### DEV_NOTES:line-30641-30647

- Source heading: same `*-aCl-* / *-aCr-*` section, immediately after the row inventory
- Source line hint: `Germanic/docs/DEV_NOTES.md:30641-30647`
- Fragment type: `negative_scope_note`
- Status: `diagnostic`
- Issue tags: `not_about_2297`; `nafola_focus`; `scope_boundary`
- Recommended next use: `cite_only_to_show_that_the_live_problem_shifted_elsewhere`
- Shared-with rows if relevant: `shared section context, but active prose centers on row 2133`

The prose immediately following row 2297 is important mainly because it shows what the section is **really** about. After listing `2297 | *wálθuz | weald | breaking`, DEV_NOTES continues: `The only TSV row that has the exact shape ... is the present row, 2133 / *náblô / nafola itself` [Germanic/docs/DEV_NOTES.md:30641-30643]. That means the section's active analytic burden had already moved away from `weald` and onto `nafola`; row 2297 survives there only as a comparator inside the breaking inventory. This fragment is therefore diagnostic rather than substantive for 2297.

## Superseded or diagnostic material

- No row-specific DEV_NOTES repair block survives for 2297. There is no preserved note of a withdrawn protoform, failed paradigm-cell probe, or exception-class reclassification. The absence matters: for this row, silence is evidence that the project did **not** ultimately treat `weald` as a major problem case [Germanic/docs/DEV_NOTES.md:1320-1358,30630-30647].
- The strongest superseded/diagnostic material is outside DEV_NOTES, in current sandbox snapshots. Those files still show `counterpart: "wald"`, OE outputs `wald / waldu / walduz / waldiz`, and even a staged surface `walþ`, which conflicts with the live TSV, packet, and research memo [Germanic/tmp/old_english_sandbox_results_current.json:3489-3498; Germanic/tmp/old_english_sandbox_results_with_stages.json:52629-52769]. Treat these as stale instrumentation or pre-normalization snapshots, not as live row authority.
- The TSV note's Anglian support via Ringe-Taylor is secondary and comparative, not noun-specific proof by itself. The relevant R/T line is verbal: `deriv. of PGmc *waldang 'to control, to rule' > WS wealdan, Merc. waldan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:13407-13409]. It is useful for the existence of a WS/Mercian `weald- ~ wald-` alternation pattern, but it should remain supporting background only.
- The old-English Wiktionary-derived table is likewise diagnostic rather than controlling: it gives `wold    wald`, which is useful evidence that the Anglian-looking form circulated in supplementary lexical material, but it is weaker than Kroonen + Clark Hall for deciding the aligned row target [Germanic/data/old_english_wiktionary.tsv:353-353].

## Open questions for later work

- If later report prose wants a tighter philological statement of the dialect issue, it should distinguish clearly among three levels: Kroonen's comparative noun stem `*walþu-`, the project input `*wálθuz`, and OE lexicographic normalization `weald`, with `wald`/`wold` only as later OE variant evidence [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28989-28991; Germanic/data/germanic-aligned-final.tsv:1424-1424; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47025-47025,47214-47218,49487-49487].
- If the sandbox/debug layer is regenerated later, check whether the stale `wald`/`walþ` outputs disappear and whether the compact derivation once again matches the packet's regular pathway to `weald`; until then, the tmp snapshots should not be cited as current-state evidence [Germanic/docs/lexeme_reports/packets/2297-wold-weald.md:17-42; Germanic/tmp/old_english_sandbox_results_with_stages.json:52629-52769].
- If a future literature pass is commissioned, the only likely gain would be firmer noun-specific evidence for the dialect distribution of `wald` versus `weald`; nothing in surviving DEV_NOTES suggests that such a pass is required to keep the present row stable now [Germanic/docs/lexeme_reports/research_memos/2297-wold-weald.md:49-55,74-88].
