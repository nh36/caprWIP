---
row_id: 1967
concept: break
counterpart: brecan
proto: *brékaną
protoform: *brékaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1967 break / brecan

## Current row state

- The live OE row reads `1967 | break | brecan | *brékaną | *brékaną | regular`. The row currently has no OE-facing project note of its own; the only row-local provenance in the TSV is duplicated Wiktionary inheritance metadata [Germanic/data/germanic-aligned-final.tsv:139-139].
- `PROTO` and `PROTOFORM` currently coincide. Nothing in the surviving DEV_NOTES material argues for splitting them for this row, introducing an OE-only proxy input, or reclassifying the verb away from `regular` [Germanic/data/germanic-aligned-final.tsv:139-139; Germanic/docs/DEV_NOTES.md:2427-2427,43229-43243].
- No matching packet or research memo for row `1967` was found under `Germanic/docs/lexeme_reports/`, so this slice has to serve as the replacement working note.
- `oe_known_problems.tsv` does not currently list `*brékaną`, `brecan`, or row `1967`; the file's active entries concern other exception buckets only [Germanic/data/oe_known_problems.tsv:1-8].

## Development-note summary

DEV_NOTES support for row `1967` is real but mostly shared rather than row-dedicated. No surviving section in `Germanic/docs/DEV_NOTES.md` is a bespoke `break / brecan` dossier. Instead, the lexeme appears in two different kinds of material: (1) early OE diagnostic notes where `break` was one of several verbs still surfacing with bad weak-tail output `-ana`, and (2) later palatalisation/source-canvass material where `brecan` is cited as a handbook example showing that a velar remains velar when a back vowel is present on one side of the consonant [Germanic/docs/DEV_NOTES.md:2422-2485,43154-43243].

The early diagnostic layer should be preserved, but labelled correctly. In the consolidated PGmc→OE TODO block, DEV_NOTES said weak-tail cleanup had to make verbs such as `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`, and the ending diagnostics repeated `brecana` in the sample list of `-ana` outputs whose targets should be simple infinitival `-an` [Germanic/docs/DEV_NOTES.md:2427-2427,2481-2485]. For this row, that does **not** amount to a special lexeme theory; it is just evidence that `break` once sat in the general OE infinitive-ending cleanup bucket.

The later palatalisation material is philologically more substantive for the current row. While diagnosing an over-greedy `OEVelarPalatalization` rule, DEV_NOTES quoted Campbell §429: “Velar consonants … remained when there was a back vowel … either before or after them, e.g. `wicu` week, `brecan` break, `aces` g.s. oak, `séoce` n.p.m. sick, `wegas` ways, `nigon` nine, `þinga` g.p. things” [Germanic/docs/DEV_NOTES.md:43165-43174]. The follow-up source canvass then retained that same conditioning as the handbook consensus and explicitly retracted the too-narrow interim fix from the previous subsection [Germanic/docs/DEV_NOTES.md:43214-43243,43296-43315]. For row `1967`, the point to preserve is straightforward: `brecan` is a canonical repo-local example of **non-palatal** velar retention in a front-vowel/back-vowel environment, so later row prose should not import normalized `ġ`-style reasoning here merely because the consonant follows `e`.

DEV_NOTES also duplicates the Campbell quotation in a separate `nigon` literature matrix, again citing `brecan` as one of the examples where a velar remains before a back-vowel context [Germanic/docs/DEV_NOTES.md:42824-42824]. That duplicated appearance adds no new row-specific argument, but it confirms that the repo repeatedly treated `brecan` as a standard conditioning example rather than as a problematic lexeme.

The conservative row-level conclusion is therefore narrow. The live row state `*brékaną → brecan` is not supported by a dedicated lexeme memo, but the surviving DEV_NOTES record is fully compatible with it: earlier generic OE cleanup explains why a temporary `brecana` output would have been treated as ordinary weak-tail noise, and later rule/literature notes explicitly support plain velar `c` in `brecan` under the standard OE palatalisation conditioning [Germanic/data/germanic-aligned-final.tsv:139-139; Germanic/docs/DEV_NOTES.md:2427-2427,2481-2485,43165-43174,43229-43243].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2422-2485

- Source heading: `PGmc→OE TODOs (consolidated)` / `Ending diagnostics (old_english.bin)`
- Source line or section hint: `lines 2422-2485`
- Fragment type: `shared_diagnostic_bucket_with_row_explicit_hit`
- Status: `diagnostic_only`
- Issue tags: `weak_tail_cleanup`; `infinitive_-an`; `historical_mismatch`; `oe_evaluator`
- Recommended next use: `preserve_as_old_mismatch_history_not_current_policy`
- Shared with row IDs: `1942`; `1959`; `1968`; `1970`

This is the earliest surviving DEV_NOTES material that names the lexeme directly. DEV_NOTES first states the engineering task: “Weak-tail cleanup (`-ana` → `-an`): reshape or drop weak-tail `ă/ą` endings in verbs so outputs like `bacana/gennana/brecana/brengana/brūcana` converge on attested `-an`” [Germanic/docs/DEV_NOTES.md:2427-2427]. The same diagnostic pass then repeats `brecana` in the sample list of bad `-ana` outputs [Germanic/docs/DEV_NOTES.md:2481-2485]. For row `1967`, this fragment is worth keeping only as labelled history. It shows that `break` once belonged to the general OE infinitive-ending cleanup problem, but it does not supply a row-specific philological claim beyond that.

### DEV_NOTES:line-43154-43212

- Source heading: palatalisation overgeneration diagnosis inside the `nigon` repair section
- Source line or section hint: `lines 43154-43212`
- Fragment type: `shared_rule_diagnosis_with_lexeme_example`
- Status: `superseded_but_explanatory`
- Issue tags: `g_palatalisation`; `front_vowel_back_vowel`; `campbell_quote`; `rule_scope`
- Recommended next use: `cite_for_conditioning_but_note_that_the_proposed_fix_was_retracted`
- Shared with row IDs: `2118`

This fragment matters because it is where DEV_NOTES most explicitly quotes the handbook evidence that bears on `brecan`. While diagnosing an over-broad `*g -> ʤ` clause, DEV_NOTES says Campbell §429 is “explicit” that velars remain when a back vowel stands before or after them, quoting the example string that includes `brecan` [Germanic/docs/DEV_NOTES.md:43165-43174]. The immediate engineering proposal in the same subsection was later retracted, so this is not current rule authority by itself [Germanic/docs/DEV_NOTES.md:43296-43315]. But the Campbell quotation preserved here remains directly relevant to row `1967`: it is an in-repo source claim that `brecan` exemplifies retained velar quality, not palatal `ġ`.

### DEV_NOTES:line-43214-43315

- Source heading: `§17.50.4 — Scholarly conditioning of the OE *g palatalisation: source canvass`
- Source line or section hint: `lines 43214-43315`
- Fragment type: `shared_source_canvass_with_current_conditioning`
- Status: `current`
- Issue tags: `handbook_consensus`; `velar_retention`; `retraction_of_interim_fix`; `conditioning_summary`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2118`; `2140`; `2206`

This is the controlling shared rule discussion for the row. DEV_NOTES says the source canvass records the handbook consensus and “retracts the over-narrow rule fix proposed in §17.50.3” [Germanic/docs/DEV_NOTES.md:43214-43222]. In the consensus summary, Campbell is quoted again with `brecan` among the examples where velars remain before or after a back-vowel context [Germanic/docs/DEV_NOTES.md:43229-43243]. The same subsection then abstracts the rule as: palatalisation after a front vowel applies iff the right context is anything except a back vowel, with `_ back-V` explicitly yielding velar outcomes [Germanic/docs/DEV_NOTES.md:43273-43287]. For row `1967`, this is the strongest current DEV_NOTES support: the lexeme belongs on the velar-retention side of the conditioning split.

### DEV_NOTES:line-42824-42824

- Source heading: Campbell entry inside the `nigon` literature matrix
- Source line or section hint: `line 42824`
- Fragment type: `duplicated_source_quote`
- Status: `background`
- Issue tags: `campbell`; `duplicate_support`; `velar_retention`
- Recommended next use: `do_not_treat_as_independent_row_note`
- Shared with row IDs: `2118`

This single-line matrix entry is materially relevant because it independently preserves the same Campbell §429 quotation in another DEV_NOTES context: `brecan` is again one of the examples where a velar remains when a back vowel is present on one side of the consonant [Germanic/docs/DEV_NOTES.md:42824-42824]. It should be kept as duplicated support only, not mistaken for a second row-specific analysis.

## Superseded or diagnostic material

- The `brecana` diagnostic is superseded as current row policy. It documents an earlier stage where OE infinitives still carried unreduced weak tails, not a lasting exception or an alternative target for row `1967` [Germanic/docs/DEV_NOTES.md:2427-2427,2481-2485].
- The interim §17.50.3 engineering fix is also superseded. DEV_NOTES first proposed narrowing palatalisation to word-final and front-vowel-right-context cases, but the immediately following source canvass states that this was “too narrow” because it would wrongly lose preconsonantal palatal cases such as `*náglaz` and `*séglą` [Germanic/docs/DEV_NOTES.md:43188-43201,43296-43315]. For `brecan`, the retained value is the source quotation and conditioning logic, not the discarded implementation proposal.
- The separate `nigon` literature matrix entry is diagnostic duplication, not new analysis. Its value is simply to show that the repo reused Campbell's `brecan` example consistently across more than one DEV_NOTES thread [Germanic/docs/DEV_NOTES.md:42824-42824].

## Open questions for later work

- If a fuller lexeme report is ever written, add direct source support for the OE strong-verb lexeme itself; the surviving DEV_NOTES material is enough for palatalisation conditioning, but thin as a standalone monograph on `break / brecan`.
- If `index.tsv` is reconsidered later, this slice is probably a borderline case: the material is current enough to be useful, but most of it is shared rule history rather than a dedicated row dossier.
- If later row documentation wants a compact citation set, the safest pair to foreground is the weak-tail diagnostic (`brecana`) plus the current source-canvass consensus (`brecan` as a velar-retention example), while clearly labelling the former as historical/diagnostic only [Germanic/docs/DEV_NOTES.md:2427-2427,43214-43243].
