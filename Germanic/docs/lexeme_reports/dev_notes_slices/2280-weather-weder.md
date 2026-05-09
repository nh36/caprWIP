---
row_id: 2280
concept: weather
counterpart: weder
proto: *wédrą
protoform: *wédrą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2280 weather / weder

## Current row state

- CONCEPT: `weather` [Germanic/data/germanic-aligned-final.tsv:1359-1359]
- COUNTERPART: `weder` [Germanic/data/germanic-aligned-final.tsv:1359-1359]
- PROTO: `*wédrą` [Germanic/data/germanic-aligned-final.tsv:1359-1359]
- PROTOFORM: `*wédrą` [Germanic/data/germanic-aligned-final.tsv:1359-1359]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1359-1359]
- The live TSV source-note field is still only the duplicated inherited placeholder `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`. That placeholder is not a real row-local rationale and should not be mistaken for the authority behind the present `regular` classification [Germanic/data/germanic-aligned-final.tsv:1359-1359].
- No row-specific packet, research memo, pilot file, or other clearly row-addressed dossier was found under `Germanic/docs/lexeme_reports/`. The coverage audit likewise still records row 2280 as `none`, i.e. no prior report infrastructure to reuse [Germanic/docs/lexeme_reports/coverage_audit.md:406-406].
- No row-specific `oe_known_problems.tsv` entry was found during the required check.
- The extant full-trace snapshot already derives the live target without repair: `PROTO: *wedrą`, `EXPECTED: weder`, `OUTPUTS: weder`, with the decisive late steps `ProtoToOEApocope: *w*e*d*r`, then `Epenthesis: *w*e*d*e*r`, then `Orthography: weder` [docs/debug_snapshots/oe_full_trace_report.txt:15953-16006].
- The trace writes the proto input as accentless `*wedrą`, while the TSV writes `*wédrą`. For this row that difference is orthographic normalization inside different project artifacts, not a competing reconstruction [Germanic/data/germanic-aligned-final.tsv:1359-1359; docs/debug_snapshots/oe_full_trace_report.txt:15954-15958].

## Development-note summary

No lexeme-specific DEV_NOTES dossier for `weather / weder` survives in the live notes file. That absence should be stated plainly. The row is supported, but the support is **shared phonological material** on final-vowel loss and OE epenthesis rather than a dedicated lexeme controversy, target swap, or exception memo. This slice therefore replaces thin inherited metadata with a conservative record of which shared DEV_NOTES passages actually explain why the row is currently uncomplicated and `regular` [Germanic/data/germanic-aligned-final.tsv:1359-1359; Germanic/docs/lexeme_reports/coverage_audit.md:406-406].

The basic lexical equation itself is not in doubt. Kroonen reconstructs Proto-Germanic `*wedra n. 'weather'` and explicitly lists `OE weder n. 'id.'` beside the other West Germanic cognates [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29550-29558]. Orel likewise gives `*wedran sb.n.` with `OE weder id.` and `OHG wetar 'weather, air'` [@Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:49797-49807]. Clark Hall's dictionary entry is correspondingly plain: `weder I. n. 'weather,' air` [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47527-47530]. Nothing in those lexical sources suggests that row 2280 is a disguised analogue, a paradigm-cell substitute, or a late spelling preference.

The row's internal labels still need to be distinguished explicitly. `PROTO = *wédrą` is the comparative / cognate-set headword carried in the TSV. `PROTOFORM = *wédrą` is also the row-specific derivational input because this row does **not** currently use a special oblique-cell or repair preform. `COUNTERPART = weder` is the selected Old English reflex that the row actually targets [Germanic/data/germanic-aligned-final.tsv:1359-1359]. Unlike rows where `PROTO` and `PROTOFORM` deliberately diverge, nothing in the current evidence requires a separate input form here. The equivalence of `PROTO` and `PROTOFORM` is itself part of the present project position.

The most useful surviving DEV_NOTES material is the shared epenthesis note. DEV_NOTES now states, in implementation-facing language, that “Epenthesis is now a real phonological stage **before** star removal and appears in the full trace” [Germanic/docs/DEV_NOTES.md:1754-1757]. It then expands the point in the dedicated rule note: `OEEpentheticInsertion` is “a **real phonological rule** representing ‘parasitic vowel insertion’ (also called ‘anaptyxis’ or ‘svarabhakti vowel’)” and inserts a vowel before final `*r` in final consonant clusters [Germanic/docs/DEV_NOTES.md:16661-16691]. That general note does not name `weder`, but it explains the exact late step seen in the trace: after loss of the weak final vowel, the bare stem `*wedr` is repaired to `*weder`, with front-vowel environment producing `e` rather than `o` [Germanic/docs/DEV_NOTES.md:16687-16691; docs/debug_snapshots/oe_full_trace_report.txt:15998-16005].

Ringe and Taylor supply the historical framework that makes the trace credible rather than ad hoc. First, they date the environment: “By the PWGmc loss of word-final short low vowels ... numerous word-final CR-clusters arose” [@RingeTaylor2014, §6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18711-18716]. Second, they state the operative phonotactic outcome for the relevant cluster type: “In word-final Cr-clusters a vowel was always inserted ... Normally the inserted vowel agreed in frontness with the vowel of the preceding syllable” [@RingeTaylor2014, §6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18725-18729]. For row 2280, that is almost a direct prose gloss on the trace sequence `*wedrą > *wedr > *weder`. The row does not need a bespoke historical argument when the shared handbooks already describe the class behavior.

Campbell's treatment points in the same direction and helps classify the output shape. In §363 he treats these forms as outcomes of parasitic-vowel development after loss of final vowels: “Normal OE forms are ... `wundor wonder, winter winter, ... æcer acre`” [@Campbell1959, §363; docs/references/campbell_old_english_grammar.txt:9953-9970]. Later, in the noun morphology discussion, he explicitly lists `weder weather` alongside `fodor`, `wuldor`, and `wundor` as members of the same structural type [@Campbell1959, §574.3; docs/references/campbell_old_english_grammar.txt:14503-14507]. That does not create a special DEV_NOTES dossier for row 2280, but it does show that the live target belongs to a well-described OE class rather than to an isolated spreadsheet decision.

The wether note in DEV_NOTES is also relevant, but only in a narrow and carefully delimited way. In §17.10.5–§17.10.7 DEV_NOTES quotes Ringe and Taylor on the PWGmc loss of word-final `*a` and `*ą`, and then uses `*wíθrą > weþer` to show how a bare or near-bare final `Cr` stem reaches OE `-er` through the same epenthesis machinery [Germanic/docs/DEV_NOTES.md:21434-21605]. Much of that section is row-specific to `wether` and its i-lowering problem, so it should **not** be imported wholesale into row 2280. But the shared chronology does apply: final weak-tail loss creates the consonant cluster, and epenthesis then supplies the vowel before final `r`. `weather / weder` is simply the easier case because it does not depend on the extra `i > e` conditioning that `wether` required.

The practical consequence is that row 2280 is well supported yet thinly dossiered. The support is strong enough to justify the current `regular` label, because the project trace, the shared DEV_NOTES rule note, and the handbook phonology all converge on the same pathway. But the support is **not** row-local in the way that would justify claiming a special DEV_NOTES history for `weder`. This slice should preserve that distinction explicitly: the row is regular and well-behaved, but its documentary backbone is shared-rule material, not a lexeme-specific exception narrative.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1754-1757

- Source heading: `OE epenthesis update (2026-01-04)`
- Source line or section hint: `lines 1754-1757`
- Fragment type: `shared_implementation_fragment`
- Status: `current`
- Issue tags: `epenthesis_stage`; `trace_visibility`; `shared_rule`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short fragment is worth preserving because it records a project-level change that matters directly for row 2280's interpretability. DEV_NOTES says that epenthesis is now a real stage “before star removal” and is therefore visible in the full trace [Germanic/docs/DEV_NOTES.md:1754-1757]. That is exactly why the trace for `weather` now shows `*wedr` becoming `*weder` as an explicit stage rather than as an opaque surface-side normalization [docs/debug_snapshots/oe_full_trace_report.txt:15998-16005].

### DEV_NOTES:line-16661-16710

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Source line or section hint: `lines 16661-16710`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `epenthesis`; `final_cr_cluster`; `shared_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the strongest current DEV_NOTES anchor for row 2280 even though it is not lexeme-specific. The fragment defines the rule, explains that it is a real phonological process rather than a hack, and states the front/back conditioning of the inserted vowel [Germanic/docs/DEV_NOTES.md:16663-16691]. For `*wédrą > weder`, that is the central explanatory note: after apocope produces final `-dr`, the existing OE epenthesis rule yields `-der`, exactly as the current trace already shows [docs/debug_snapshots/oe_full_trace_report.txt:15998-16005; @RingeTaylor2014, §6.9.5; @Campbell1959, §§363, 365-367].

### DEV_NOTES:line-21434-21605

- Source heading: `§17.10.5 — Role 3 migration: *wíθră should become *wíθr, not *wíθra`; `§17.10.7 — Correction: *wíθr fails i-lowering; migrate to *wíθrą instead`
- Source line or section hint: `lines 21434-21605`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `diagnostic_only`
- Issue tags: `final_vowel_loss`; `shared_cr_chronology`; `wether_comparator`
- Recommended next use: `background_only`
- Shared with row IDs:

This fragment is mixed and should be used carefully. Its main subject is row `wether`, not row `weather`, and the i-lowering discussion is not transferable. What *is* transferable is the chronology quoted there from Ringe and Taylor — word-final short `*a/*ą` loss preceding later OE developments — plus the concrete demonstration that a final `Cr` stem can reach OE `-er` by the same epenthesis rule now used in the main pipeline [Germanic/docs/DEV_NOTES.md:21434-21449,21587-21599]. For row 2280 it is therefore background support, not a primary indexing anchor.

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES argument was located for `weather / weder`. The absence of a lexeme-local controversy is itself part of the row's present status.
- The duplicated Wiktionary placeholder in the TSV should be treated as inherited metadata, not as the documentary basis for the current row [Germanic/data/germanic-aligned-final.tsv:1359-1359].
- The wether note is useful only as a comparator for final-vowel-loss chronology and `Cr > Cer` behavior. Its i-lowering problem, migration debate, and row-edit instructions are not evidence that row 2280 ever needed analogous intervention [Germanic/docs/DEV_NOTES.md:21463-21605].
- The full trace is diagnostic implementation support, not a DEV_NOTES fragment. It is valuable because it confirms that the live pipeline already produces `weder` from the live proto input without workaround [docs/debug_snapshots/oe_full_trace_report.txt:15953-16006].

## Open questions for later work

- If `index.tsv` is reconsidered later, decide whether row 2280 should remain unindexed unless a genuinely lexeme-specific DEV_NOTES note is written. At present the best anchors are shared-rule anchors, not row-local dossier anchors.
- If a later final report is needed, add a cleaner direct dictionary citation from Bosworth-Toller or another repository source for the noun headword `weder`; Clark Hall is sufficient for this slice, but only minimally so.
- If DEV_NOTES is later reorganized into shared phonology modules, row 2280 belongs with the `final Cr-cluster + epenthesis` class alongside forms like `winter`, `wundor`, `wuldor`, and `fodor`, rather than in an exceptions section.
