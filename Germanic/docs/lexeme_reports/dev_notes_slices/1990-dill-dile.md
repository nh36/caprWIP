---
row_id: 1990
concept: dill
counterpart: dile
proto: *déljaz
protoform: *déliz
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1990-dill-dile.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1990-dill-dile.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/dill_stem_class_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1990 dill / dile

## Current row state

- CONCEPT: `dill`
- COUNTERPART: `dile`
- PROTO: `*déljaz`
- PROTOFORM: `*déliz`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note (abridged): Kroonen p. 93 is treated as the controlling row-level authority for the split between an OE i-stem and continental ja-stems: “evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli).” The row therefore keeps cognate-set `PROTO = *déljaz` but uses OE-facing `PROTOFORM = *déliz`.
- `oe_known_problems.tsv`: no row-level entry.
- `report_manifest.tsv`: no manifest entry for row 1990.
- Packet and research memo both exist and are useful, but the live TSV plus the implemented DEV_NOTES correction are the current authority; older wording that still speaks as if row 1990 itself were `*deljăz → dile` is preserved only as project history.

## Development-note summary

This row is no longer a live mismatch, but DEV_NOTES preserves why it used to be one. The abandoned row state paired OE `dile` with ja-stem `*deljăz`, and the transducer therefore gave `dill`, because `*-lj-` triggers West Germanic gemination. DEV_NOTES states the phonological point plainly: if the OE form really continued `*deljăz`, the expected outcome would be geminate `*dill`, not single-`l` `dile`. The mismatch was therefore not evidence for a missing OE repair rule; it was evidence that the OE row needed a different derivational input from the continental ja-stem rows.

The core surviving authority is Kroonen's stem-class discussion, which DEV_NOTES quotes directly and should continue to quote directly: “The material offers evidence for both an **i-stem** (OE *dile*) and a **ja-stem** (OS *dilli*, OHG *tilli*) ... the original paradigm probably had ablaut of the root, viz. nom. `*deliz`, gen. `*duljaz`” [@Kroonen2013, p. 93]. DEV_NOTES uses that quotation in the most practical row-level way possible. For Old English, the decisive fact is the single `l`, which matches i-stem `*deliz > dile`; for Old Saxon and Old High German, the decisive fact is geminate `ll`, which matches ja-stem `*deljăz > dilli/tilli`. The slice should therefore preserve daughter-language stem divergence as the real solution, not merely “variation in the dictionaries.”

DEV_NOTES also keeps the comparative source positions distinct rather than pretending all handbooks agree on the same reconstruction. Orel is reported as keeping only the ja-stem headword and listing OE `dile`, OS `dilli`, and OHG `tilli` together under that headword, which is useful for the cognate set but “does not distinguish i-stem from ja-stem” and so does not explain the OE single `-l-` [@Orel2003]. Kluge-Seebold is likewise preserved as ja-stem-leaning continental evidence, not as the row's final OE authority. Fulk is the important supporting counterweight on the OE side: DEV_NOTES quotes him on OE `dili` and early West Saxon accusative `dile` as evidence that some former ja-stems were transferred to the i-stems in OE [@Fulk2018, §7.11]. That makes the current row policy stronger than a narrow “one-off exception” claim: OE `dile/dili` belongs to a known morphological transfer pattern.

The implemented project decision is correspondingly narrow and explicit. DEV_NOTES recommends “Option A” — “Change row 1990 from `*deljăz` to `*deliz`” — because “Kroonen explicitly reconstructs `*deliz` as the i-stem nominative,” because OE `dile` is “incompatible with j-gemination,” and because the same paradigm-cell / stem-selection principle already used elsewhere should be used here too. The same note then records the implementation date and the concrete test result: row 1990 was changed on 2026-04-06, `echo "deliz" | flookup -i old_english.bin` returned `dile`, and the mismatch count dropped by one. For current workflow, that is the controlling row policy: keep the cognate-set headword `*déljaz`, but derive the OE row from `PROTOFORM = *déliz`.

The only later DEV_NOTES authority tied directly to row 1990 is verification rather than reinterpretation. In the late unstressed-`i` cleanup, the project explicitly retained `*déliz → dile` as a sentinel pair, first among the “two formerly-passing forms used as extra checks” and then again among the 14 sentinels preserved after the dead `*ĭ` machinery was removed. That matters because it shows the `dile` fix was not a brittle local hack: even after unrelated cleanup in the OE medial-`i` machinery, the row still derives correctly.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-5811-5817

Source heading: opening mismatch statement for `dile` under the old ja-stem row  
Source line or section hint: lines 5811-5817  
Status: diagnostic_only  
Issue tags: project_history;stem_class;j_gemination;old_row_state  
Recommended use: use_as_project_history_only  
Shared with row IDs:  
Text or paraphrase:
This short opening problem statement should be kept only as labelled chronology. It records the pre-fix row state exactly: “TSV row 1990: `*deljăz → dile`,” “FST output: `*deljăz → dill`,” and the explanation that ja-stem `*deljăz` triggers `*-lj- > -ll-` gemination. The logic is still useful, but the row state is no longer current. Its value now is diagnostic: it preserves why the project stopped treating OE `dile` as if it were directly derivable from the continental ja-stem input.

### DEV_NOTES:line-5819-5920

Source heading: OE `dile` “dill”: i-stem vs. ja-stem  
Source line or section hint: lines 5819-5920  
Status: current  
Issue tags: protoform_vs_proto;stem_class;early_analogy;source_audit;implementation  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This is the controlling row fragment. It preserves Kroonen's quotation that the material shows “both an **i-stem** (OE *dile*) and a **ja-stem** (OS *dilli*, OHG *tilli*)” and even sketches an older ablauting paradigm with nominative `*deliz` and genitive `*duljaz` [@Kroonen2013, p. 93]. DEV_NOTES then turns that comparative statement into a row policy: OE `dile` is the regular i-stem outcome, while OS `dilli`, OHG `tilli`, and Dutch `dille` are regular ja-stem outcomes. Orel and Kluge-Seebold are preserved as useful but less discriminating comparanda because they keep only a ja-stem headword and do not solve the OE single-`l` problem [@Orel2003]. Fulk's quotation — OE `dili` in the Corpus Glossary and acc. sg. `dile` in early West Saxon as evidence that some ja-stems were transferred to the i-stems in OE — is the strongest supporting note for how the OE side should be narrated [@Fulk2018, §7.11]. The same fragment then records the project decision and implementation: choose `*deliz` for row 1990, keep the continental ja-stem rows as they are, verify `deliz -> dile`, and count the row as a resolved mismatch rather than as an unexplained exception.

### DEV_NOTES:line-38484-38520

Source heading: late sentinel verification after medial-`i` cleanup  
Source line or section hint: lines 38484-38520  
Status: current  
Issue tags: verification;sentinel_pair;medial_i_lowering;regression_check  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This late verification note is brief but important. After the project rewrote the OE unstressed-`i` machinery, DEV_NOTES explicitly checked that `*déliz → dile` still survived first as one of “two formerly-passing forms used as extra checks” and then as part of the 14-sentinel verification set. The fragment therefore functions as durable regression evidence: row 1990's corrected `PROTOFORM` remains stable even after unrelated cleanup in the surrounding cascade.

## Superseded or diagnostic material

The only securely attachable DEV_NOTES material that is superseded for this row is the opening mismatch framing from the old `*deljăz → dile` state. It should stay visible because later packet work or stale analysis notes can still surface that wording, and because it preserves the exact diagnostic that motivated the change: ja-stem `*-lj-` produces geminate `-ll-`, not the single `-l-` needed for OE `dile`.

Outside DEV_NOTES, the linked analysis file is also chronological rather than current authority. It still describes a stage where all four cognate rows shared `*deljăz` and where the proposed change was still waiting on further consultation. The live TSV, the implemented DEV_NOTES note, and the later sentinel checks supersede that state.

## Open questions for later work

- In any final report, make the `PROTO` / `PROTOFORM` split explicit: `*déljaz` remains the cognate-set headword, but `*déliz` is the OE derivational input.
- Decide whether the final report should quote Fulk's transfer-to-i-stem wording alongside Kroonen, since that gives the OE single-`l` result a clearer morphological context than Kroonen alone.
- Keep rare OE `dyle` and the rounded-vowel comparanda as comparative background only unless later report work needs them; nothing in the current row requires replacing target `dile`.
