---
row_id: 2057
concept: harvest
counterpart: hierfest
proto: *xárbistuz
protoform: *xárbistuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2057-harvest-hierfest.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/analysis/fryhtu_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2057 harvest / hierfest

## Current row state

- CONCEPT: `harvest`
- COUNTERPART: `hierfest`
- PROTO: `*xárbistuz`
- PROTOFORM: `*xárbistuz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `R/T 14594-14603: hærfest is Anglian loan (Bammesberger 1997); WS hierfest attested (Toller); regular PGmc *harbistuz > WS hierfest via AFB+breaking+i-umlaut` [Germanic/data/germanic-aligned-final.tsv:493-493].
- Packet status: the current cascade already derives `*xárbistuz -> hierfest`, and the packet explicitly records `_None_` for matching `oe_known_problems.tsv` entries and `_No manifest entry._` for this row [Germanic/docs/lexeme_reports/packets/2057-harvest-hierfest.md:11-13,17-43,45-47].
- Memo status: the derivation to `hierfest` is currently coherent, but the memo's main caution is that the row's OE target behaves like a **reconstructed native West Saxon outcome**, whereas the securely attested OE lexical tradition in repo reference files is `hærfest` with variant `herfest` [Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md:15-20,39-40,43-49,55-64,94-100].
- Source-audit baseline from repo reference files: `old_english_wiktionary.tsv` gives `hærfest`; Bosworth-Toller has the headword `hærfest`; Clark Hall gives `hærfest (e)` and cross-references `herfest` to it, but these excerpts do not supply exact headword `hierfest` [Germanic/data/old_english_wiktionary.tsv:121-121; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:80422-80428; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20102-20102,21832-21832].

## Development-note summary

Current row-specific DEV_NOTES authority **does exist**, but it is narrower than the live TSV note suggests. The securely current DEV_NOTES material governs the **derivational** question—why the FST should output `hierfest` rather than older `hierfist`—and it also preserves a source audit showing that exact `hierfest` is best treated as the expected **native WS reflex**, not as securely transmitted ordinary OE headword evidence [DEV_NOTES:line-6585-6752; Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md:15-20,55-64,88-100].

On the derivational side, DEV_NOTES is explicit that the old mismatch was technical and now solved: `*xarbistuz` had been surfacing as `hierfist` because the grammar lacked the late OE unstressed front-vowel merger in medial syllables. The note quotes Hogg's formulation that “by about 700 all unstressed front vowels had become /e/,” Campbell's statement that “æ, e, and i fell together in a sound written e in unaccented syllables,” and Ringe-Taylor's description of the merger of unstressed `æ` and `i` as `e`; on that basis it treats `hierfest`, not `hierfist`, as the regular native WS output once the missing medial lowering is added [DEV_NOTES:line-6636-6659]. The same note then writes the full row-specific chain out: PGmc `*harbistaz` > Anglo-Frisian fronting `*hærbist-` > breaking `*hearbist-` > i-umlaut `*hierbist-` > unstressed `i > e` `*hierbest-` > `hierfest`, with the crucial warning that the medial `*i` first triggers umlaut and only later lowers in the unstressed syllable [DEV_NOTES:line-6674-6691]. For this row, `PROTO` and `PROTOFORM` remain the same PGmc input `*xárbistuz`; the OE-facing target is the later stage `hierfest`, not the intermediate `*hierbist-` and not the attested comparator `hærfest/herfest`.

The philological side is more delicate, and the slice has to preserve that delicacy rather than flatten it into “attested hierfest.” DEV_NOTES' Bammesberger summary is current and explicit: the older `*harubist-/*haruvist-` double-umlaut proposal is rejected, because if that preform were right, Bammesberger says one would expect OE `*hærefest`, and Middle English `hervest` would also be badly explained; the inherited comparative form is instead `*harbist-` with medial `*i` [DEV_NOTES:line-6693-6733]. More importantly, the same DEV_NOTES cluster carries the line that governs later reporting: “Die den Lautregeln des Westsächsischen entsprechende Fortsetzung *hierfest, *hyrfest von urg. *harbist- ... ist nicht überliefert,” followed by the conclusion that `hærfest` and `herfest` are explainable within non-WS phonology and that WS `hærfest` belongs among Anglian borrowings [DEV_NOTES:line-6735-6752; docs/references/bammesberger_1997_herfest.txt:430-438]. Ringe-Taylor's discussion at the exact location cited in the TSV note says the same thing in English: `heerfest`/`herfest` are difficult precisely because they lack expected breaking, and Bammesberger “argues persuasively” that they are Anglian forms borrowed into WS [docs/references/ringe_taylor_linguistic_history_vol2.txt:14594-14604].

That means the replacement working note must keep three levels separate. `PROTO` is the comparative PGmc headword family `*xárbistuz`; `PROTOFORM` is the same row-specific FST input because the live cascade does not currently require a substitute paradigm cell or altered input; and the live OE `COUNTERPART` field is `hierfest`, which current repo evidence supports as the **regular reconstructed native WS outcome** of that input [Germanic/data/germanic-aligned-final.tsv:493-493; DEV_NOTES:line-6674-6691]. By contrast, `hærfest` and `herfest` are the attested OE lexical comparators/background forms preserved in dictionaries and in Bammesberger/Ringe-Taylor, not alternative spellings to be silently collapsed into the live row target [Germanic/data/old_english_wiktionary.tsv:121-121; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:80422-80428; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20102-20102,21832-21832; DEV_NOTES:line-6735-6752].

The implementation history also needs one explicit caution. DEV_NOTES first tried to add a simple medial unstressed `i > e` rule, which fixed harvest but wrongly damaged `begin`; the successful repair therefore used explicit unstressed-`*i` marking before lowering. Harvest is the positive control for that repair: the note's worked trace marks medial `*i` in `*harbistuz`, lowers it to `e`, and reports `hierfest`; a much later sentinel table keeps `*xárbistuz -> hierfest` as “the canonical case” through the incremental `*ĭ` cleanup [DEV_NOTES:line-6766-6875,38371-38387]. So current DEV_NOTES authority is not absent. It is strong on the **sound-change/implementation** side and strong on the **reconstructed-vs.-attested distinction**, but it does **not** securely support repeating the raw TSV wording “WS hierfest attested” without qualification.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6585-6691

- Source heading: `OE hierfest 'harvest' — Unstressed Front Vowel Merger`
- Source line or section hint: `lines 6585-6691`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `unstressed_front_vowel_merger`; `hierfist_to_hierfest`; `breaking`; `i_umlaut`; `row_derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core current row-specific DEV_NOTES authority. It states the old mismatch directly—`*xarbistuz` had been yielding `hierfist`—and then fixes it by adducing the late OE merger of unstressed front vowels. The note preserves three handbook quotations that are still the best compact justification for the row's medial vowel: Hogg's “by about 700 all unstressed front vowels had become /e/,” Campbell's “æ, e, and i fell together in a sound written e in unaccented syllables,” and Ringe-Taylor's summary that the merger of unstressed `æ` and `i` as `e` affected “word-final and other inflectional syllables” [DEV_NOTES:line-6636-6657]. It then gives the row-local derivation in full—`*harbistaz` > `*hærbist-` > `*hearbist-` > `*hierbist-` > `*hierbest-` > `hierfest`—and insists that the medial `*i` must be kept distinct from its own later reflex, since it first triggers root umlaut and only later lowers in the unstressed syllable [DEV_NOTES:line-6674-6691]. For row 2057 this fragment is current and sufficient on the derivational side.

### DEV_NOTES:line-6693-6752

- Source heading: `Bammesberger (1997): What He Did and Didn't Address` plus `WS hærfest as Anglian Borrowing`
- Source line or section hint: `lines 6693-6752`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `attestation_vs_reconstruction`; `harubist_rejected`; `anglian_borrowing`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is current because it keeps the row's source hierarchy straight. DEV_NOTES first says Bammesberger's article addresses two issues: rejection of the older `*harubist-/*haruvist-` preform and explanation of WS `hærfest` as borrowed Anglian/non-WS material rather than native WS continuation [DEV_NOTES:line-6693-6712]. It then preserves the decisive direct quotation: “Die den Lautregeln des Westsächsischen entsprechende Fortsetzung *hierfest, *hyrfest von urg. *harbist- ... ist nicht überliefert,” followed by the conclusion that both `hærfest` and `herfest` can be explained within non-WS phonology and that WS `hærfest` belongs among Anglian borrowings [DEV_NOTES:line-6737-6748; docs/references/bammesberger_1997_herfest.txt:430-438]. That is exactly why the memo warns against treating `hierfest` as straightforwardly attested OE: current repo authority supports it as the expected native WS reflex, while the attested lexical tradition remains `hærfest/herfest` [Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md:55-64,88-100].

### DEV_NOTES:line-6766-6784

- Source heading: `Implementation Attempt #1: Simple Parallel Rule (FAILED)`
- Source line or section hint: `lines 6766-6784`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `failed_fix`; `shared_with_begin`; `overbroad_lowering`; `project_chronology`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `1943`

This fragment should be kept because it preserves the failed first fix rather than letting later writers imagine that `hierfest` dropped out of the grammar trivially. DEV_NOTES attempted a simple medial unstressed `i > e` rule parallel to the medial `u > o` rule, and the harvest side did look right, but the same rule wrongly lowered the stressed root vowel in `*biginnăną`, producing `beġennan` instead of `beġinnan` [DEV_NOTES:line-6766-6784]. For row 2057 the value of the fragment is diagnostic: it explains why the present solution uses explicit unstressed-vowel marking instead of a naïve direct lowering rule.

### DEV_NOTES:line-6824-6875

- Source heading: `Implementation Attempt #3: Three-Step Marking (SUCCESSFUL)`
- Source line or section hint: `lines 6824-6875`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `successful_fix`; `unstressed_i_marking`; `shared_implementation`; `worked_trace`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1943`

This is the current implementation fragment that supersedes the failed simple rule. DEV_NOTES lays out the three-step `*ĭ` marking system and then gives a worked harvest trace: in `*harbistuz` the medial `*i` is marked as unstressed, lowered to `e`, and the note reports the output `hierfest ✓`; the paired `begin` trace shows why the root vowel there is restored before lowering so that `beġinnan` remains intact [DEV_NOTES:line-6824-6875]. For row 2057 this fragment is worth copying because it makes the implementation logic explicit and also records that harvest is the positive control for the successful repair.

### DEV_NOTES:line-38371-38387

- Source heading: `§17.36 *ĭ (i-breve) cleanup — sentinel test set`
- Source line or section hint: `lines 38371-38387`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `sentinel_verification`; `canonical_case`; `post_cleanup_stability`; `verification_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1943`

This late sentinel table matters because it shows that row 2057 remained stable after later cleanup, not just at the moment of the March fix. The row appears explicitly as ``*xárbistuz`` → `hierfest` with the note “medial *i lowering (the canonical case),” inside a regression set used to dismantle the earlier `*ĭ` scaffolding without losing established behavior [DEV_NOTES:line-38371-38387]. For this slice the fragment is pure current verification: it confirms that `hierfest` stayed the intended native-WS output even after subsequent implementation simplification.

## Superseded or diagnostic material

- The live TSV note's wording “WS hierfest attested (Toller)” is **misleading if uncontextualized**. Current repo evidence does not securely attach exact `hierfest` as the ordinary attested headword; the safer source-backed statement is that `hierfest` is the regular native WS reflex, while attested OE dictionary/headword material in the repo is `hærfest` with variant `herfest` [Germanic/data/germanic-aligned-final.tsv:493-493; Germanic/data/old_english_wiktionary.tsv:121-121; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:80422-80428; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:20102-20102,21832-21832; DEV_NOTES:line-6735-6752].
- The older `*harubist-/*haruvist-` hypothesis is superseded source history, not live row policy. DEV_NOTES preserves Bammesberger's objections that strict application of that preform would yield OE `*hærefest` and that Middle English `hervest` would not be directly explained, so later note-writing should keep this material only as checked diagnostic history [DEV_NOTES:line-6713-6733; docs/references/bammesberger_1997_herfest.txt:241-259].
- `Germanic/docs/analysis/arestoration_r_l_research.md` and `Germanic/docs/analysis/fryhtu_investigation.md` are background/diagnostic only for this row. The first simply lists row 2057 among breaking + i-umlaut items, and the second uses `hierfest` as a no-regression control while discussing medial syncope elsewhere; neither is row-specific authority on attestation or target choice [Germanic/docs/analysis/arestoration_r_l_research.md:735-735; Germanic/docs/analysis/fryhtu_investigation.md:201-205,227-227,286-307].
- `oe_known_problems.tsv` has no entry for this row, so the row is not currently managed as an open exception bucket; the remaining tension is documentary/source-classification tension, not an unresolved FST failure [Germanic/docs/lexeme_reports/packets/2057-harvest-hierfest.md:45-47; Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md:15-20,92-100].

## Open questions for later work

- Decide whether row 2057 should later be reclassified from `regular` to `reconstructed_oe`, since the current evidence bundle supports `hierfest` primarily as reconstructed native WS rather than as straightforwardly attested OE [Germanic/docs/lexeme_reports/research_memos/2057-harvest-hierfest.md:92-100; Germanic/docs/lexeme_reports/research_memo_index.tsv:43-43].
- Before any final report repeats the TSV wording about Toller, verify whether the repo contains a securely usable exact citation for `hierfest`; absent that, report prose should keep the contrast explicit: reconstructed WS `hierfest` versus attested `hærfest/herfest`.
- Decide how much of the rejected `*harubist-/*haruvist-` discussion belongs in later report prose. It is valuable for source audit and for explaining why the medial vowel must be PGmc `*i`, but it may belong in a source-history paragraph rather than the main derivation narrative.
