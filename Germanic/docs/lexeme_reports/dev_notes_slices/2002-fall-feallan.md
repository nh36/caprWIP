---
row_id: 2002
concept: fall
counterpart: feallan
proto: '*fállaną'
protoform: '*fállaną'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2002 fall / feallan

## Current row state

- The live OE row is stable and fully regular: `ID = 2002`, `CONCEPT = fall`, `COUNTERPART = feallan`, `PROTO = *fállaną`, `PROTOFORM = *fállaną`, `DERIVATION_CLASS = regular`, with no live TSV note attached to the row [Germanic/data/germanic-aligned-final.tsv:278-278].
- `PROTO` and `PROTOFORM` are identical, so this row is not currently using a substitute paradigm cell, an editorially distinct protoform, or an OE-stage rescue target. The row target is the OE infinitive `feallan`; it should not be blurred with other cells of the verb such as preterite `feoll` or with Anglian `fallan` [Germanic/data/germanic-aligned-final.tsv:278-278; Germanic/docs/DEV_NOTES.md:33887-33890; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:695-700].
- The current derivation trace is an exact match. The compact published trace gives `PROTO: *fállaną`, `EXPECTED: feallan`, `OUTPUTS: feallan`, and spells out the active OE-side developments as `Anglo Frisian Brightening: *fællaną`, `OE Breaking: *feallaną`, `OE Heavy Syllable Nasal Apocope: *feallan`, `OE Secondary Nasalization: *fealląn`, and `OE Weak Tail Reduction: *feallan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1118-1137].
- The full trace confirms the same ordering in expanded rule form. After unchanged Proto-West-Germanic and Northwest Germanic stages, the row passes through `AngloFrisianBrightening`, then `OEBreaking`, and only afterward through the ordinary OE tail rules; nothing in the trace suggests a mismatch, workaround, or pending repair [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7452-7515,7540-7541].
- `oe_known_problems.tsv` currently contains unrelated exception and wontfix entries only; there is no row-local reservation for `2002`, `fall`, `feallan`, or `*fállaną` [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` classifies row 2002 among the regular rows with empty NOTE and no report requirement: `| 2002 | fall | feallan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:233-233]. `report_manifest.tsv` likewise has no manifest-backed report entry for this row among the currently listed report-backed cases [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- A directly relevant analysis file preserves an important comparative warning: in shared dialect notes the West Saxon form is `feallan`, while Anglian is `fallan`; the live row is therefore already selecting the breaking-bearing WS reflex rather than a pan-dialectal abstraction [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:398-404,695-700].

## Development-note summary

No dedicated row-2002 DEV_NOTES dossier survives. The usable internal material is shared rather than row-authored: an inventory entry marking `*fállaną / feallan` as a geminate-`ll` case, a later resolved-policy note saying that breaking-conditioned rows including `*fállaną` are unaffected in the A-restoration work because breaking bleeds restoration, and a preserved Hogg quotation using `feoll 'fell'` as a canonical OE breaking example before `l + C` [Germanic/docs/DEV_NOTES.md:30604-30618,30641-30647; Germanic/docs/DEV_NOTES.md:36533-36533,36628-36629; Germanic/docs/DEV_NOTES.md:33887-33890]. There is therefore some relevant DEV_NOTES substance, but it is shared background and diagnostic positioning, not a row-specific mini-essay.

The strongest current internal account of the row is phonological rather than editorial. The live trace shows a clean WS-style path `*fállaną > *fællaną > *feallaną > feallan`, and the later A-restoration verification note explicitly treats `*fállaną` as one of the rows where no further restoration intervention is needed because breaking has already taken the row onto its correct branch [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1118-1137; Germanic/docs/DEV_NOTES.md:36628-36629]. That is the main thing this replacement slice has to preserve: row 2002 is not a hidden problem row.

What does need preserving is the distinction among three different levels of evidence. First, the row's own target is the infinitive `feallan`, with `PROTO = PROTOFORM = *fállaną` in the live dataset [Germanic/data/germanic-aligned-final.tsv:278-278]. Second, shared DEV_NOTES and analysis material discuss the same lexeme under other cells or dialects, especially preterite `feoll` and Anglian `fallan`; those are relevant comparanda, but they are not the row target itself [Germanic/docs/DEV_NOTES.md:33887-33890; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:398-404,695-700]. Third, the surviving DEV_NOTES mentions are mostly negative or classificatory: they explain why `*fállaną` is outside the special `nafola`-type `*aCl` problem space and why it stays untouched by the A-restoration fix [Germanic/docs/DEV_NOTES.md:30615-30615,30641-30647; Germanic/docs/DEV_NOTES.md:36628-36629].

In short: row-specific DEV_NOTES material is sparse, but the surviving shared material is enough to say something concrete. The row currently represents the regular West Saxon breaking outcome, not an unresolved mismatch, not a paradigm-cell repair, and not an attested-vs-reconstructed ambiguity of the kind seen elsewhere.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30604-30618

- Source heading: `§17.19.4  Other potentially affected words`
- Source line or section hint: `inventory of OE rows with *-aCl-* or *-aCr-* before a back-vowel tail`
- Fragment type: `shared_inventory_and_scope_filter`
- Status: `current`
- Issue tags: `geminate_ll`; `scope_exclusion`; `shared_background`; `not_nafola_type`
- Recommended next use: `cite_for_scope_and_non-problem_status`
- Shared with row IDs: `1940; 1975; 2008; 2025; 2052; 2077; 2166; 2167; 2204; 2289; 2297`

This fragment preserves the clearest internal classification of row 2002 inside a broader scan of potentially similar OE rows. The table explicitly lists `| 2002 | *fállaną | feallan | geminate *ll* |` [Germanic/docs/DEV_NOTES.md:30609-30618]. That matters because the surrounding note is not really about `fall` itself; it is testing whether a proposed fix for another row (`*náblô > nafola`) would spill over into formally similar words. Row 2002 appears there as a checked comparator, not as the main problem.

The immediately following conclusion is the substantive part that should not be lost. DEV_NOTES says that the only TSV row with the exact `*[stressed a] + obstruent + l + back-vowel-tail*` shape, "with no breaking trigger and no geminate," is `2133 / *náblô / nafola` [Germanic/docs/DEV_NOTES.md:30641-30647]. By implication, `*fállaną` is excluded from that narrow problem class precisely because it has geminate `ll` and belongs with the breaking-conditioned forms instead. So this fragment is mostly negative evidence, but it is still useful current evidence: it records that row 2002 was reviewed during scope control and found not to belong to the special no-breaking `-Cl-` tail subset.

### DEV_NOTES:line-36533-36629

- Source heading: `§17.25.5  Expected impact on attested rows`
- Source line or section hint: `A-restoration verification note with explicit treatment of breaking-conditioned rows`
- Fragment type: `resolved_shared_policy`
- Status: `current`
- Issue tags: `a-restoration`; `breaking_bleeds_restoration`; `row_stable`; `shared_policy`
- Recommended next use: `primary_current_anchor`
- Shared with row IDs: `1940; 1975; 2008; 2025; 2056; 2077; 2120; 2166; 2167; 2204; 2271; 2289; 2297`

This is the strongest current DEV_NOTES authority for the row's present status. The note first preserves the Ringe/Taylor-style formulation: `"After breaking had run its course, those stressed *æ* which were immediately followed by a single or geminate consonant or sC-cluster which was in turn followed by a back vowel became *a*."` [Germanic/docs/DEV_NOTES.md:36533-36533]. Immediately afterward it applies that rule-ordering result to the actual dataset and says: `For breaking-conditioned rows (*xármaz, *márkō, *kálbaz, *fállaną* etc., 21 rows total), A-restoration is bled by breaking; unaffected` [Germanic/docs/DEV_NOTES.md:36628-36629].

For row 2002 this does two jobs at once. First, it confirms that geminate-`ll` `*fállaną` belongs in the breaking-conditioned class, not in some residual `æ`-restoration problem bin. Second, it shows that by the time this note was written the row was already understood as safe under the proposed change set: the A-restoration work should leave it alone. That is exactly the kind of current, reusable project judgment a replacement slice ought to preserve.

### DEV_NOTES:line-33887-33890

- Source heading: `§17.21.10.2  Does breaking apply across /st/ + r?`
- Source line or section hint: `quoted Hogg summary of canonical breaking examples`
- Fragment type: `shared_phonology_example`
- Status: `current_but_indirect`
- Issue tags: `breaking_before_l_plus_c`; `same_lexeme_other_cell`; `preterite_not_infinitive`; `quotation_preserved`
- Recommended next use: `use_as_background_only`
- Shared with row IDs: `2002; 2007; 2077`

This fragment is not a row-2002 note in the narrow sense, but it is still the only preserved DEV_NOTES quotation that names the same lexeme family while explicitly discussing OE breaking. DEV_NOTES quotes Hogg as follows: `"Breaking is described as diphthongization of front vowels before back consonants ... The canonical examples are: *feoh 'cattle', *eo 'horse', *weorpan 'throw', *weorčan 'work', *eald 'old', *feoll 'fell'. Breaking applies before /h/, /x/, /r/ + C, /l/ + C."` [Germanic/docs/DEV_NOTES.md:33889-33889]. The value here is the last sentence and the example `feoll`, which together preserve the internal scholarly rationale for treating `l + C` as a normal breaking environment.

The caution is equally important. The quoted form is `feoll`, i.e. the preterite cell 'fell', not the infinitive `feallan` that row 2002 actually stores [Germanic/docs/DEV_NOTES.md:33889-33890]. So this fragment should not be overused as if it directly documented the row target or its exact paradigm cell. Its proper role is narrower: it is shared background supporting the sound change environment that also underlies the live `*fállaną > feallan` derivation.

## Superseded or diagnostic material

There is no preserved row-specific superseded DEV_NOTES argument for row 2002. Nothing in the checked internal material suggests an abandoned target, a corrected `PROTOFORM`, or a past mismatch that later had to be rescued. The surviving diagnostic trail instead points the other way: the row already matches, and the shared notes classify it as a regular breaking case that should remain untouched [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1118-1137; Germanic/docs/DEV_NOTES.md:36628-36629].

The most useful non-DEV_NOTES diagnostic supplement is the dialect-comparison analysis. It records the familiar pairing `WS feallan` versus `Anglian fallan` and places `fall` alongside `old, all, hold, straw, salt` as part of the same WS-breaking vs. Anglian-retraction contrast [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:398-404,695-700]. That file is relevant because it explains what kind of OE form the row is targeting, but it is still secondary for this slice: it does not imply that the row should be changed away from `feallan`; it only warns against treating the WS form as the only imaginable OE reflex.

A smaller diagnostic pointer appears in the earlier A-restoration research inventory, which simply lists `| 2002 | *fállaną | feallan | breaking before geminate *ll* |` among broader-pattern rows [Germanic/docs/analysis/arestoration_r_l_research.md:722-730]. This is useful corroboration, but it adds no policy beyond what the later DEV_NOTES already states more explicitly.

## Open questions for later work

- If row 2002 ever needs fuller prose documentation, the most useful addition would be a direct capture of the underlying Campbell/Ringe-Taylor wording for the WS `feallan` versus Anglian `fallan` split, so the slice does not have to rely on the secondary analysis summary alone [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:398-404,695-700].
- If a future packet or memo is generated for this row, it should keep paradigm-cell distinctions explicit: infinitive `feallan` is the row target, while quoted `feoll` material is only shared evidence for the breaking environment [Germanic/data/germanic-aligned-final.tsv:278-278; Germanic/docs/DEV_NOTES.md:33887-33890].
- There is currently no internal sign that `PROTO` and `PROTOFORM` should diverge, that `oe_known_problems.tsv` needs a new entry, or that the row should move off the present West-Saxon-style target. Any later change would need stronger row-specific evidence than what presently survives [Germanic/data/germanic-aligned-final.tsv:278-278; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/DEV_NOTES.md:36628-36629].
