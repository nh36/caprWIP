---
row_id: 2033
concept: friend
counterpart: frēond
proto: "*fríjōndz"
protoform: "*fríjōndz"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/notable_findings.md
current_status: current
needs_literature_agent: yes
---

# DEV_NOTES material — 2033 friend / frēond

## Current row state

- The live OE row is `2033`, with `CONCEPT friend`, `COUNTERPART frēond`, `PROTO *fríjōndz`, `PROTOFORM *fríjōndz`, and `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:400-400].
- The row's project note field is empty, and the surviving row-local provenance is only the duplicated import string `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`, so the TSV itself does not preserve a separate project-authored argument for this lexeme [Germanic/data/germanic-aligned-final.tsv:400-400].
- `oe_known_problems.tsv` has no entry for row `2033`, for `frēond`, or for `*fríjōndz`, so the item is not currently parked in the OE exception ledger [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking still lists `| 2033 | friend | frēond | regular | no | - | - | - | none |`, and `report_manifest.tsv` has no row-2033 report entry; there is no existing packet or research-memo stem to reuse, so the canonical slice filename is appropriate here [Germanic/docs/lexeme_reports/coverage_audit.md:252-252; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The published OE derivation trace is already an exact match: `PROTO: *fríjōndz`, `EXPECTED: frēond`, `OUTPUTS: frēond`, with the staged path `PWGmc Ij Contraction: *fríundz`, `PGmc Final Z Deletion: *fríund`, and `OE Diphthong Leveling: *frēond` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1623-1642].

## Development-note summary

No dedicated row-2033 dossier survives in `DEV_NOTES.md`. The usable material is shared rather than row-local: one explicit PWGmc `*ijō > *iu` rule note built around `friend`, one later stocktake line showing that `*fríjōndz` is no longer a mismatch, and one indirect Campbell citation elsewhere in DEV_NOTES that names `frēond` as a regular OE contraction outcome [Germanic/docs/DEV_NOTES.md:1385-1402,20562-20563,40079-40082]. This slice therefore has to act as a replacement working note assembled from those shared fragments plus the current trace, not as an extraction from a lost packet.

The main surviving DEV_NOTES claim is precise but deliberately cautious. Ringe–Taylor are quoted as saying that “A roughly similar change of `*ijo` to `*iu` appears to have occurred in the word 'friend' in PWGmc,” but the same note immediately preserves their warning that “the uniqueness of the sequence `*ijo` (with stressed `*i`) makes it inadvisable to attempt any generalizations based on the history of this word” [Germanic/docs/DEV_NOTES.md:1387-1391]. In project terms, that means the row is currently treated as `regular` because the implemented cascade does derive `frēond`, not because the literature turns `*ijō > *iu` into a broad, well-populated sound law.

That distinction should remain explicit in later writing. The live row's stored comparative/project input is `PROTO = PROTOFORM = *fríjōndz`, while the OE target is `COUNTERPART = frēond` [Germanic/data/germanic-aligned-final.tsv:400-400]. DEV_NOTES often writes the same etymon in slightly different notation as `*frijōnd-` when illustrating the shared rule module, and the trace shows intermediate `*fríundz` and `*fríund`; those are derivational stages or notation variants, not rival row metadata [Germanic/docs/DEV_NOTES.md:1392-1399; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1632-1642].

The attached analysis file is useful because it states the methodological issue even more plainly: the FST had to formalize the change as `{*i}{*j}{*ō} → {*iu}`, effectively unconditional in current data, precisely because a transducer cannot leave the question at prose-level hesitation [Germanic/docs/analysis/notable_findings.md:506-518]. That analysis should still be treated as shared background, not as row-specific authority, but it explains why row `2033` can be both operationally stable and philologically narrow in evidentiary scope.

## Relevant DEV_NOTES fragments

The surviving DEV_NOTES material for `friend / frēond` is real but mostly shared-policy or shared-rule material. No fully row-local memo section survives.

### DEV_NOTES:line-1385-1399

- Source label: `DEV_NOTES:line-1385-1399`
- Source heading: `### 2. PWGmcIjContraction: *ijō → *iu (before consonant)`
- Source line or section hint: `lines 1385-1399`
- Fragment type: `shared_current_rule_note`
- Status: `current_but_shared`
- Issue tags: `friend_only_rule`; `ijō_to_iu`; `ringe_taylor_caveat`; `implemented_special_case`
- Recommended next use: `primary_DEV_NOTES_citation_for_row_2033_rule_history`
- Shared with row IDs:

This is the closest thing to a controlling DEV_NOTES fragment for row `2033`, but it is still framed as a shared sound-change module rather than as a dedicated lexeme packet. The note preserves the crucial Ringe–Taylor wording: “A roughly similar change of `*ijo` to `*iu` appears to have occurred in the word 'friend' in PWGmc” and immediately adds the equally important warning that “the uniqueness of the sequence `*ijo` (with stressed `*i`) makes it inadvisable to attempt any generalizations based on the history of this word” [Germanic/docs/DEV_NOTES.md:1387-1391]. For replacement-note purposes, both halves matter. The project is not claiming that the literature offers a broad, securely general law with many examples; it is preserving a lexeme-centered observation plus a caveat.

The same fragment also preserves the project's present operational choice. Under **Examples** it gives `PGmc *frijōnd- → PWGmc *friund → OE frēond ('friend')`, adds that `*iu` is later leveled to `*ēo` by `OEDiphthongLeveling`, and then records the implementation as `{*i} {*j} {*ō} -> {*iu}` with status `Implemented; only affects *frijōndz in current data` [Germanic/docs/DEV_NOTES.md:1392-1399]. That last clause is especially important for row `2033`: it confirms that the project does in fact encode this as a live derivational step, but also that the step is effectively attached to a single lexeme family in the current corpus.

### DEV_NOTES:line-20562-20563

- Source label: `DEV_NOTES:line-20562-20563`
- Source heading: `§16 Accent-Marking Conventions (Pre-merge Stocktake, 2026-04-21)`
- Source line or section hint: `lines 20562-20563`
- Fragment type: `brief_current_ledger`
- Status: `current`
- Issue tags: `resolved_item`; `post_fix_ledger`; `not_a_live_mismatch`
- Recommended next use: `cite_only_as_short_current_state_confirmation`
- Shared with row IDs: `2029; 2042; 2058; 2140; 2308`

This is not a philological argument, but it is a useful current-state guardrail. In a later regression stocktake DEV_NOTES lists “**8 items fixed** (no longer mismatching): `*fédwōr`, `*fríjōndz`, `*fúnxstiz`, `*gánsz`, `*júgunθ`, `*kéwwăną`, `*mēnōθz`, `*násō`” [Germanic/docs/DEV_NOTES.md:20562-20563]. For row `2033`, the practical force of that sentence is simply that by this stage of the project `*fríjōndz` had moved out of the live mismatch bucket.

Because the fragment is only a ledger, it should not be asked to prove more than it can. It does not explain *why* `frēond` is correct, and it does not restate the intermediate stages. What it does preserve is the project-historical fact that the row's earlier implementation problem was treated as solved rather than left open.

### DEV_NOTES:line-40079-40082

- Source label: `DEV_NOTES:line-40079-40082`
- Source heading: `### Source audit` (within the `three`/`þrīe` discussion)
- Source line or section hint: `lines 40079-40082`
- Fragment type: `shared_background_reference`
- Status: `current_but_indirect`
- Issue tags: `campbell_reference`; `contraction_background`; `not_row_local`
- Recommended next use: `cite_only_for_shared_OE_reflex_background`
- Shared with row IDs:

This later fragment is not a row-2033 note in its own right, but it is still worth preserving because it names `frēond` explicitly in a source-audit context. DEV_NOTES says that Campbell §120(c) treats prehistory-of-OE contractions as yielding final `-īe` in forms like ``þrīe`, `fēnd` < `*finhija-`, `frēond`, `frīo` etc.`, then concludes, “The contraction is a regular PGmc → OE sound change” [Germanic/docs/DEV_NOTES.md:40079-40082]. That gives later writers one more internal reminder that OE `frēond` itself is not being treated as a spelling accident or an unattested editorial normalization.

At the same time, this fragment is only indirect support for row `2033`. It appears inside a different lexical audit, not in a dedicated `friend` section, and it does not carry the weight of the earlier Ringe–Taylor caveat about the unique PWGmc `*ijō > *iu` step. It is therefore best used as shared OE-side background after the main `PWGmcIjContraction` fragment, not instead of it.

## Superseded or diagnostic material

- No clearly row-specific superseded DEV_NOTES dossier survives for `friend / frēond`. The non-row-local state of the evidence is itself part of the current diagnosis: support exists, but it survives mostly as shared rule prose and later audit ledgers rather than as a bespoke lexeme memorandum [Germanic/docs/DEV_NOTES.md:1385-1402,20562-20563].
- The spellings `*frijōnd-` and `*friund` in DEV_NOTES should not be copied mechanically into TSV-style metadata. In this slice they are best read as, respectively, handbook-style or rule-illustration notation and an intermediate PWGmc stage, whereas the live stored row metadata remains `*fríjōndz` / `*fríjōndz` [Germanic/docs/DEV_NOTES.md:1392-1399; Germanic/data/germanic-aligned-final.tsv:400-400].
- The `analysis/notable_findings.md` discussion is diagnostic background, not primary row authority. Its value is that it states the modelling dilemma explicitly — the FST had to implement a rule that the prose literature treats cautiously and almost lexeme-by-lexeme — and records the parallel `*Vwu > *Vu` comparison plus the warning that the two developments “cannot plausibly be reduced to a single phonological rule” [Germanic/docs/analysis/notable_findings.md:506-518].
- Coverage state `none` in `coverage_audit.md` should be read as a documentation gap, not as evidence that row `2033` is currently broken. The publish trace already lands on `frēond`, and DEV_NOTES' later ledger marks `*fríjōndz` as fixed [Germanic/docs/lexeme_reports/coverage_audit.md:252-252; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1623-1642; Germanic/docs/DEV_NOTES.md:20562-20563].
- No packet or research memo exists for the row, so there was no alternate established stem to inherit. This slice therefore correctly uses `2033-friend-frēond.md` rather than trying to imitate a nonexistent prior report filename [Germanic/docs/lexeme_reports/coverage_audit.md:252-252; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].

## Open questions for later work

- If a later literature pass is commissioned, the main question is still the one flagged inside DEV_NOTES and the analysis file: should `*ijō > *iu` remain modeled as a regular rule with only one surviving lexical witness in current data, or should later reporting describe it more overtly as a lexeme-specific historical irregularity that the FST happens to encode? [Germanic/docs/DEV_NOTES.md:1387-1399; Germanic/docs/analysis/notable_findings.md:520-542].
- If additional PGmc forms with stressed `*ijV` sequences are ever added to the dataset, row `2033` should be revisited immediately, because the present implementation note explicitly says the rule `only affects *frijōndz in current data` [Germanic/docs/DEV_NOTES.md:1398-1399].
- Any later final report should keep three layers distinct: live row metadata `*fríjōndz`, DEV_NOTES' illustrative spelling `*frijōnd-`, and the attested OE target `frēond`. Collapsing those labels would blur exactly the reconstructed-vs-attested distinction that matters most for this lexeme [Germanic/data/germanic-aligned-final.tsv:400-400; Germanic/docs/DEV_NOTES.md:1392-1399].
