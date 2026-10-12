---
row_id: 2161
concept: run
counterpart: rinnan
proto: *rínnaną
protoform: *rínnaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2161 run / rinnan

## Current row state

- CONCEPT: `run`
- COUNTERPART: `rinnan`
- PROTO: `*rínnaną`
- PROTOFORM: `*rínnaną`
- DERIVATION_CLASS: `regular`
- Live TSV row `2161` currently keeps the ordinary OE infinitive `rinnan` and carries no row-local explanatory note beyond inherited source markers; there is no live-row instruction to prefer a metathesized WS or Anglian variant [Germanic/data/germanic-aligned-final.tsv:895-895].
- `old_english_wiktionary.tsv` likewise maps English `run` to OE `rinnan`, so the repo's basic lexical-target layer agrees with the live row's un-metathesized infinitive [Germanic/data/old_english_wiktionary.tsv:222-222].
- Direct row/lexeme search of `Germanic/data/oe_known_problems.tsv` returned no hit for row `2161`, `rinnan`, or `*rínnaną`, so the row is not currently managed as an OE exception bucket.
- Coverage audit still lists row `2161` as uncovered, with no packet, memo, or dossier yet attached; the metadata fields therefore remain blank in this slice [Germanic/docs/lexeme_reports/coverage_audit.md:332-332].
- The current derivation snapshot is exact-match regular: `PROTO: *rínnaną`, `EXPECTED: rinnan`, `OUTPUTS: rinnan`. The published trace shows only the routine OE tail developments (`Heavy Syllable Nasal Apocope`, `Secondary Nasalization`, `Weak Tail Reduction`) and no metathesis or breaking step in the live cascade [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3751-3770].

## Development-note summary

The securely relevant DEV_NOTES material for row `2161` is not a row-local failure dossier, but the larger r-metathesis discussion that uses the `burn/run` verb pair as its best lexical evidence. The first point that has to be preserved is that DEV_NOTES explicitly records the un-metathesized form as genuine OE evidence, not as an implementation miss. In the Campbell §459 quotation copied into DEV_NOTES, the key wording is: “Beside *eornan* occurs *rinnan*,” directly pairing the metathesized and un-metathesized run-forms in the documentary record [Germanic/docs/DEV_NOTES.md:4842-4852]. For this row, that matters more than any abstract metathesis rule: the live OE target `rinnan` is not merely a placeholder standing in for `eornan` or `irnan`; it is one of the actual forms the note says coexist.

The second point is that DEV_NOTES treats the `run` family as a chronology-and-dialect problem, not as a single obligatory output. Campbell §155, Ringe-Taylor, and Luick are all quoted to show that `rinnan` belongs to the same lexical cluster as metathesized `irnan/iornan/eornan`, but the timing differs by dialect. DEV_NOTES summarizes Campbell's position that metathesis in these verbs was “early enough for breaking to occur” in Anglian, giving Northumbrian `iorna` and VP/Mercian `eornan`, while in West Saxon metathesis came later, yielding WS `irnan ~ iernan` instead of the Anglian broken forms [Germanic/docs/DEV_NOTES.md:4880-4894,4898-4920]. Luick is quoted in the same direction: Northumbrian `iorna` and reconstructed Mercian `*iornan` underlie later `eornan`, whereas West Saxon more typically shows the unbroken outcomes because metathesis usually happened after breaking [Germanic/docs/DEV_NOTES.md:4934-4958]. Row `2161` therefore needs a very explicit distinction between layers: the live row's `PROTO` and `PROTOFORM` both remain `*rínnaną`; the DEV_NOTES forms `*irnan`, `*iornan`, `eornan`, and `irnan` are comparative OE-stage variants used to explain dialectal chronology, not replacement protoforms for this row [Germanic/data/germanic-aligned-final.tsv:895-895; Germanic/docs/DEV_NOTES.md:4910-4916,4945-4958].

The third point is practical project policy. DEV_NOTES' FST implementation section says the grammar intentionally models only a restricted r-metathesis rule in `*rVst` clusters and does **not** model the `-rn-` cases represented by `brinnan/rinnan`. The note is explicit on both counts: the system models a single “standard late WS” output, so “The Anglian forms with breaking (*beornan, eornan*) are not generated,” and “Metathesis before n” is also outside the present implementation, with `*brinnan -> birnan/beornan` named as the example class [Germanic/docs/DEV_NOTES.md:5001-5014,5031-5039]. For row `2161`, that is the controlling current conclusion: the project has preserved the r-metathesis evidence, but it has deliberately **not** turned that evidence into a live-row demand to derive `eornan`, `iornan`, or even WS `irnan`. The current pipeline therefore remains coherent in outputting ordinary `rinnan`, and the exact-match debug trace confirms that this is a stable, intentional regular row rather than a silent omission [Germanic/docs/DEV_NOTES.md:5031-5050; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3751-3770].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-4842-4852

- Source heading: `Campbell §459: scope of r-metathesis`
- Source line or section hint: `lines 4842-4852`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `r_metathesis`; `attestation`; `target_choice`; `oe_variation`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the most directly attachable row-specific fragment because it names the live counterpart itself. DEV_NOTES quotes Campbell on the common OE metathesis of `r` before a short vowel plus `s/n`, then adds the clause that matters for row `2161`: “Beside *eornan* occurs *rinnan*” [Germanic/docs/DEV_NOTES.md:4842-4852]. That sentence establishes a concrete documentary point for this slice: un-metathesized `rinnan` is an attested member of the run-family variation, so the live row does not need to be defended as a mere fallback produced by an incomplete metathesis module.

### DEV_NOTES:line-4878-4958

- Source heading: `Campbell §155: Breaking and metathesis interaction`
- Source line or section hint: `lines 4878-4958`
- fragment_type: `phenomenon_context_for_lexeme`
- current_status: `current`
- Issue tags: `r_metathesis`; `breaking`; `dialect_variation`; `chronology`; `protoform_vs_proto`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the shared chronology fragment that explains why multiple OE outcomes coexist without forcing a row rewrite. DEV_NOTES quotes Campbell that Anglian metathesis in the `burn/run` verbs was early enough for breaking, producing Northumbrian `biorna, iorna` and VP `beornan, eornan`, while West Saxon had later metathesis and so kept unbroken `birnan, irnan` [Germanic/docs/DEV_NOTES.md:4880-4894]. Ringe-Taylor are then quoted more explicitly for the `run` chain: `PGmc *rinnanan ... > *irnan > Angl. OE *iornan ... > Merc. eornan, North. iorna`, with WS instead showing `irnan ~ iernan` because metathesis there followed breaking [Germanic/docs/DEV_NOTES.md:4896-4920]. Luick's discussion preserves the same conclusion in another formulation: these differences arise because metathesis “gewöhnlich erst nach, zum Teil aber auch vor der Brechung eintrat,” i.e. usually after but partly before breaking [Germanic/docs/DEV_NOTES.md:4934-4958]. For row `2161`, this fragment establishes that `eornan/iorna/irnan` are dialectal chronological comparators, not automatic replacements for the live row's `PROTOFORM` `*rínnaną` or its current OE target `rinnan`.

### DEV_NOTES:line-4999-5050

- Source heading: `FST implementation`
- Source line or section hint: `lines 4999-5050`
- fragment_type: `copied_shared_lexeme_fragment`
- current_status: `current`
- Issue tags: `fst_policy`; `r_metathesis`; `transducer_scope`; `late_ws_model`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the current implementation-policy fragment that explains why the live row remains regular. DEV_NOTES says the implemented `OERMetathesis` rule is deliberately restricted to `*r + V + st` clusters, with examples such as `*brestanan -> berstan` and `*frustą -> forst` [Germanic/docs/DEV_NOTES.md:5001-5029]. It then states what the grammar does **not** model: “The Anglian forms with breaking (*beornan, eornan*) are not generated,” and “Metathesis before n: We do not currently model *brunna -> burna* or *brinnan -> birnan/beornan*” because those verbs require lexical conditioning [Germanic/docs/DEV_NOTES.md:5031-5050]. For row `2161`, this fragment is the operational explanation for why the exact-match output is still `rinnan`: the project has intentionally not generalized the r-metathesis discussion into live `-rn-` derivation rules.

## Superseded or diagnostic material

- There is **no dedicated superseded row-local repair** for `2161` in DEV_NOTES comparable to the paradigm-cell rescues or target rewrites found for harder rows. The risk here is over-reading the shared metathesis survey as if it required the row to be rewritten to `eornan`, `iornan`, or WS `irnan`; DEV_NOTES does not make that recommendation, and the implementation section explicitly says the relevant `-rn-` metathesis class is not currently modeled [Germanic/docs/DEV_NOTES.md:5031-5050].
- The comparative intermediate forms cited in DEV_NOTES—`*irnan`, `*iornan`, `eornan`, `iorna`, WS `irnan ~ iernan`—should be preserved only as chronological and dialectal explanation. They are useful because they show what the run-family could look like under earlier or later metathesis relative to breaking, but they should not be copied into row metadata as though they replaced live `PROTO`/`PROTOFORM` `*rínnaną` [Germanic/docs/DEV_NOTES.md:4910-4916,4934-4958].
- The strongest positive evidence for retaining `rinnan` is not a modern implementation convenience but the source quotation “Beside *eornan* occurs *rinnan*.” Later review should keep that sentence visible whenever the row is discussed, so the un-metathesized target is not mistaken for a failure to notice the better-known `eornan` tradition [Germanic/docs/DEV_NOTES.md:4849-4852].

## Open questions for later work

- If later project policy wants a dialect-normalized OE target instead of the present ordinary infinitive, decide explicitly whether that means late-WS `irnan` or Anglian `eornan/iornan`; current DEV_NOTES material documents both families but does not choose one as row `2161` policy [Germanic/docs/DEV_NOTES.md:4880-4920].
- If metathesis before `n` is ever implemented, test `run` together with the paired `burn` material and with non-target comparators like `bringan`, since DEV_NOTES itself warns that the environment needs careful lexical conditioning to avoid overapplication [Germanic/docs/DEV_NOTES.md:5036-5055].
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is updated later, index this row as a stable regular row with one lexeme-specific attestation fragment, one shared chronology fragment, and one shared implementation-policy fragment rather than as a mismatch or exception dossier.
