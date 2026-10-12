---
row_id: 2120
concept: march
counterpart: mearc
proto: *márkō
protoform: *márkō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2120-march-mearc.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2120 march / mearc

## Current row state

- CONCEPT: `march`
- COUNTERPART: `mearc`
- PROTO: `*márkō`
- PROTOFORM: `*márkō`
- DERIVATION_CLASS: `regular`
- Live TSV row: `2120	m e a r c	*márkō	...	mearc	...	Old_English	Kroonen *markō- f. 'boundary' → OE mearc f.; mearcian is the verb 'to mark'` [Germanic/data/germanic-aligned-final.tsv:737]
- Live packet state is regular and successful: `PROTO: *márkō`, `EXPECTED: mearc`, `OUTPUTS: mearc`, with the compact trace `*márkō -> *márku -> *mærku -> *mearku -> mearc` via NWGmc final long-`ō` raising, Anglo-Frisian brightening, OE breaking, and high-vowel apocope [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:17-41].
- `oe_known_problems.tsv`: no matching row-level problem entry is attached; both packet and memo record `_None_` for row `2120`, `*márkō`, and `mearc` [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:44-46; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:37-40].
- Packet/memo identity check: the surviving row-local dossier files are `2120-march-mearc.md`, not `2120-marrow-mearg.md`, and both explicitly describe the row as noun `mearc` ‘boundary / march’, not as marrow `mearg` [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:1-10; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:1-11].
- Repo-local philological baseline aligns with the live row. Kroonen gives `*markō- f. 'boundary, region' ... OE mearc f. 'boundary, district'` and separately lists OE `mearcian` under the verbal family; Clark Hall gives `mearc ... 'mark,' sign, line of division ... boundary, limit, term, border`; Bosworth-Toller likewise preserves `mearc` under the boundary/limit headword [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18801-18806; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27659-27661; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:101965-101969].
- Current DEV_NOTES authority status: there is **no securely attachable current row-specific DEV_NOTES dossier for row 2120**. The attachable current material is shared implementation/background material that happens to include the exact pair `*márkō → mearc`; the only nearby DEV_NOTES occurrence of the string `mearg` is Campbell's quotation about inverted spelling for `mearh` ‘horse’, not a row-2120 decision block [Germanic/docs/DEV_NOTES.md:10931-10937; Germanic/docs/DEV_NOTES.md:29428-29435; Germanic/docs/DEV_NOTES.md:29457-29475; Germanic/docs/DEV_NOTES.md:36628-36629].
- Conservative file-scope warning: the requested slice filename `2120-marrow-mearg.md` does **not** match the current row state. No checked row-state source here attaches `marrow / mearg` to row `2120`; this replacement working note therefore documents the live row `march / mearc` and explicitly quarantines `mearg` material as separate or misleading unless future row evidence says otherwise [Germanic/data/germanic-aligned-final.tsv:737; Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:7-9; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:5-11].

## Development-note summary

No securely attachable current **row-specific** DEV_NOTES authority survives for row `2120` in the sense of a dedicated lexeme note or decision block. That needs to be said plainly. What does survive is narrower but still useful: shared 2026 implementation material in `DEV_NOTES.md` uses `*márkō → mearc` as an exact success case for the short-diphthong weight / apocope refactor and later records breaking-conditioned rows including `*márkō` as unaffected by the A-restoration audit [Germanic/docs/DEV_NOTES.md:29428-29435; Germanic/docs/DEV_NOTES.md:29457-29475; Germanic/docs/DEV_NOTES.md:36628-36629]. The packet and memo agree with that reading: the row is already regular, already outputs `mearc`, and does not need a rescue argument built around paradigm selection or an unresolved mismatch [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:17-41; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:47-55,67-76].

The essential distinctions for this row are therefore not paradigm-cell distinctions but **lexeme / modelling-input / OE target** distinctions. `PROTO = *márkō` is the comparative headword label for the cognate set; `PROTOFORM = *márkō` is also the actual PGmc input fed into the OE derivation for this row; and the OE target is the noun `mearc`, not the related verb `mearcian` [Germanic/data/germanic-aligned-final.tsv:737; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:49-55,67-76]. Kroonen's extract is especially useful because it keeps those noun/verb families adjacent but separate: `*markō-` gives OE `mearc`, while OE `mearcian` belongs to verbal `*markōjan- / *markjan-` material, not to the noun row itself [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:18801-18806].

The live phonological story is straightforward and should be copied into the slice instead of merely gesturing back to DEV_NOTES. The packet's compact trace and the memo's prose agree on the path `*márkō -> *márku -> *mærku -> *mearku -> mearc`: NWGmc final long-`ō` raising first, Anglo-Frisian brightening next, OE breaking before `rC`, then apocope of final high vowel in the now-heavy short-diphthong-plus-cluster configuration [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:27-41; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:40-55]. DEV_NOTES line `29435` and the verification table at `29466` are attachable precisely because they encode that same analysis in the current implementation state, with `*márkō → mearc` presented as the expected heavy `rk`-cluster outcome [Germanic/docs/DEV_NOTES.md:29434-29435; Germanic/docs/DEV_NOTES.md:29464-29466].

What makes this replacement note necessary is the collision around the string `mearg`. In the checked row-state sources, `mearg` does **not** belong to row `2120`; the live row is `mearc` [Germanic/data/germanic-aligned-final.tsv:737; Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:7-9]. In DEV_NOTES, the visible `mearg` quotation is Campbell on "inverted spellings like mearg ... for mearh horse," i.e. a horse-form orthographic warning, not boundary `mearc` and not marrow `mearg` [Germanic/docs/DEV_NOTES.md:10931-10937]. Campbell's grammar also separately distinguishes `Ep. mearc mark` from `merg marrow`, which confirms that `mearc` and marrow `mearg/merg` are different lexemes even within similar phonological surroundings [docs/references/campbell_old_english_grammar.txt:6704-6705]. Clark Hall likewise separates noun `mearc` ‘boundary’ from `mearg, mearh` ‘marrow’ and from `mearh, mearg` ‘horse’ [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27626-27626; 27659-27661; 27716-27718]. The safest current conclusion is therefore explicit: **no securely attachable marrow/mearg authority survives for row 2120**, and any such material would presently be a cross-lexeme contamination rather than row documentation.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-29428-29435

- Source heading: `§17.17.8 Implementation results (short-diphthong weight refactor)`
- Source line or section hint: `lines 29428-29435`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `breaking`; `short_diphthong_weight`; `high_vowel_apocope`; `rk_cluster`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2068`

This is the most directly usable current DEV_NOTES fragment for row `2120`, even though it is shared implementation material rather than a dedicated lexeme note. DEV_NOTES states the controlling generalization in full: `ShortDiphthong + C + C+` counts as heavy and therefore apocopates, giving examples `*xérdō → heord`, `*márkō → mearc`, and `*xállō → heall` [Germanic/docs/DEV_NOTES.md:29431-29435]. For this row that is not just incidental name-dropping. It captures the exact reason the post-breaking form loses final `-u`: once `*márkō` has reached broken `*mearku`, the stem contains a short diphthong followed by `rk`, so it falls on the heavy side of the apocope split and surfaces as `mearc` rather than any retained-vowel form [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:27-41; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:49-55]. This fragment should therefore be treated as current implementation authority for the row's regularity.

### DEV_NOTES:line-29457-29475

- Source heading: `§17.17.8 Verification probes and self-resolved regressions`
- Source line or section hint: `lines 29457-29475`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `verification`; `regression_check`; `rk_cluster`; `implementation_state`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2068`

The value of this second fragment is that it converts the rule statement above into explicit verification state. DEV_NOTES' probe table includes the exact row pair `| *márkō | mearc | mearc | HEAVY (rk cluster) |`, and the follow-up sentence says that `mearc` was one of the regressions that "self-resolved" after the round-3 short-diphthong-plus-cluster and related clauses were put in place [Germanic/docs/DEV_NOTES.md:29457-29475]. That matters because row `2120` is not being preserved as a fragile exception or hand-tuned output. DEV_NOTES records it as a checked success case inside a broader implementation repair, which matches the packet's current compact derivation and the memo's conclusion that the row is regular and stable in the present system [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:48-72; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:67-76].

### DEV_NOTES:line-36628-36629

- Source heading: `§17.25.5 Predicted side-effects`
- Source line or section hint: `lines 36628-36629`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `a_restoration`; `breaking_bleeding`; `class_background`; `negative_evidence`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment is not row-specific authority, but it is useful class-level background because it records a negative fact later readers might otherwise re-litigate. DEV_NOTES says that for breaking-conditioned rows such as ``*xármaz, *márkō, *kálbaz, *fállaną`` the A-restoration investigation changes nothing because restoration is "bled by breaking" [Germanic/docs/DEV_NOTES.md:36628-36629]. That matches the packet's background pointer to `arestoration_r_l_research.md`, where row `2120` is simply listed among the breaking cases, and it supports the memo's statement that later A-restoration work is not the place to solve or redefine this lexeme [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:94-104,140-148; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:43-45,55-56].

### DEV_NOTES:line-10931-10937

- Source heading: `Campbell §447 on h/g interchange`
- Source line or section hint: `lines 10931-10937`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `orthographic_collision`; `cross_lexeme_false_friend`; `mearg_string`; `not_row_2120`
- Recommended next use: `ignore_unless_debugging`
- Shared with row IDs:

This fragment must be preserved only as a warning against bad attachment. DEV_NOTES quotes Campbell: `"There are also inverted spellings like mearg ... for mearh horse"` and then explains that the passage shows non-categorical `h/g` alternation [Germanic/docs/DEV_NOTES.md:10931-10937]. The string `mearg` here is therefore **not** row `2120` boundary `mearc`, and it is not secure row evidence for marrow either; it is an orthographic variant in the `mearh` ‘horse’ discussion. Because the requested filename says `marrow-mearg`, this is exactly the sort of fragment that could be mis-harvested if the row identity were not checked against the live TSV, packet, and memo first [Germanic/data/germanic-aligned-final.tsv:737; Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:7-9; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:5-11]. Its best use is therefore diagnostic only: it explains why a naive search for `mearg` in DEV_NOTES is unsafe for row `2120`.

## Superseded or diagnostic material

- Older project-history files preserve the exact noun/verb confusion that the current row and note now reject. `Germanic/docs/germanic_transducer_report.md` still has `*markō → mearcian`, and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` still has `*markō → mearcō (exp. mearcian)`; the memo already classifies these as stale diagnostics rather than live authority [Germanic/docs/germanic_transducer_report.md:31-31; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:311-311; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:43-45].
- The packet's local lexical-table hit `march | mearcian` belongs in the same bucket. It is a Modern-English gloss collision with the related verb, not evidence against noun `mearc`, and the packet itself labels that hit as background only [Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:110-117; Germanic/docs/lexeme_reports/research_memos/2120-march-mearc.md:61-61,69-76].
- The filename-level `marrow / mearg` label should also be treated diagnostically until an actual row-state source ties it to row `2120`. Repo-local references show three separate near-homographic items that can contaminate one another if detached from context: `mearc` boundary, `mearg/merg` marrow, and `mearg` as an orthographic variant of `mearh` horse [docs/references/campbell_old_english_grammar.txt:6704-6705; docs/references/campbell_old_english_grammar.txt:11653-11655; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27626-27626; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27659-27661; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27716-27718]. That is precisely why this slice states the mismatch rather than silently pretending the filename matches the live row.

## Open questions for later work

- If `dev_notes_slices/index.tsv` is updated later, record explicitly that row `2120` has **no dedicated current row-specific DEV_NOTES dossier**; the attachable current material is shared implementation/background (`29428-29435`, `29457-29475`, `36628-36629`), while `10931-10937` is a misleading `mearg` false friend rather than row authority.
- If later curation revisits filenames, decide whether this slice should eventually be renamed to the live row identity `2120-march-mearc.md`; no such rename is part of the present task, but the current mismatch should not be forgotten [Germanic/data/germanic-aligned-final.tsv:737; Germanic/docs/lexeme_reports/packets/2120-march-mearc.md:1-10].
- If a real OE `marrow / mearg` row or dossier is identified elsewhere later, treat it as a separate lexeme problem. Do **not** backfill that material into row `2120` merely because the strings `mearg`, `mearh`, `merg`, and `mearc` occur near one another in Campbell or dictionary extracts [docs/references/campbell_old_english_grammar.txt:6704-6705; docs/references/campbell_old_english_grammar.txt:11653-11655; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27659-27661; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27716-27718].
