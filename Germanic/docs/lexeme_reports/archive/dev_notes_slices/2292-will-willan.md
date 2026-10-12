---
row_id: 2292
concept: will
counterpart: willan
proto: *wéljaną
protoform: *wéljaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2292 will / willan

## Current row state

- The live OE row is a regular exact-match verb row: `CONCEPT = will`, `COUNTERPART = willan`, `PROTO = *wéljaną`, `PROTOFORM = *wéljaną`, `DERIVATION_CLASS = regular`, and the source note is still only the duplicated Wiktionary inheritance chain `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1405-1405].
- The local cognate cluster already separates the verbal and nominal lexemes that share the English concept label `will`. Rows `1662/1663/1664/2292` carry verbal `*wéljaną` with OE `willan`, while rows `215/216/217/2293` carry nominal `*wéljô` with OE `willa`; this slice therefore has to keep row `2292` explicit as the verb and not borrow noun-row evidence uncritically [Germanic/data/germanic-aligned-final.tsv:1402-1409].
- `old_english_wiktionary.tsv` independently gives `will -> willan`, so the row's basic OE lexeme identity is repo-local and not dependent on the duplicated note field alone [Germanic/data/old_english_wiktionary.tsv:349-349].
- `coverage_audit.md` classifies row `2292` as a regular row with no pre-existing report requirement (`Requirement basis = none`), so this slice is replacement working documentation rather than continuation of an older row-specific report chain [Germanic/docs/lexeme_reports/coverage_audit.md:416-416].
- The current published derivation trace is exact and fully regular: `Proto Input: *wéljaną`, `PWGmc J Gemination: *wélljaną`, `OE Heavy Syllable Nasal Apocope: *wélljan`, `OE Secondary Nasalization: *wélljąn`, `OE I Umlaut: *willjąn`, `OE Weak Tail Reduction: *willjan`, `OE J Loss After Heavy: *willan`, `Outcome: willan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5925-5944].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so row `2292` is **not** currently using a substitute paradigm cell, analogical rescue form, or notation split. Here `PROTO = *wéljaną` is both the comparative/project label and the actual FST input, while `COUNTERPART = willan` is the selected OE verbal citation form [Germanic/data/germanic-aligned-final.tsv:1405-1405; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5925-5944].
- Comparative references align with that verbal reading and also help keep row `2293` separate. Kroonen distinguishes `*weljan- 1` “to want” with OE `willan` from `*weljan- 2 m.` “will, wish” with OE `willa`, and separately lists `*waljan-` as the different verb “to choose” [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28917-28922,29294-29314; @Kroonen2013]. Kluge likewise gives `ae. willan` under the weak verb behind German `wollen`, while reserving `Wille` for a `*weljOn m.` noun that includes OE `willa` [docs/references/kluge_seebold_etymologisches_woerterbuch.txt:98946-98948,99539-99550; @KlugeSeebold2011].
- OE lexicography supports the same split. Clark Hall gives noun `willa m. ... mind, will, determination, purpose` separately from anomalous verb `willan (y) ... to 'will,' be willing, wish, desire`, while Sweet glosses `willa, sm. will` and `willan, swv. will, wish` as separate entries [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48525-48559; docs/references/sweet_anglo_saxon_primer.txt:6897-6903; @ClarkHall1960; @Sweet1953]. Campbell adds a caution useful for this row pair: under the verb he records East Kentish `1 sg. pres. indic. willa (< willu) beside wille`, so not every surface `willa` token is noun evidence for row `2293` [docs/references/campbell_old_english_grammar.txt:23639-23647; @Campbell1959].

## Development-note summary

No rich row-specific `willan` dossier survives in `DEV_NOTES.md`. The attachable DEV_NOTES evidence is thin but still more concrete than a bare concept-name match. One current implementation note on `l`-adjacent syncope explicitly names `*weljaną -> willan` as the kind of form that must **not** be damaged by an overly broad medial-vowel deletion rule; a later dry-run validation then lists `weljăną → willan ✓ (was willen)` among six temporarily fixed infinitives, but immediately records that the whole proposal was rejected because it caused broader regressions [Germanic/docs/DEV_NOTES.md:867-889,9493-9554]. This slice therefore replaces missing row-local prose with one current guardrail fragment plus one clearly superseded diagnostic fragment.

The current fragment is valuable because it says exactly what sort of evidence row `2292` is in project history. DEV_NOTES, while discussing `OELAdjacentSyncope`, warns that the rule must remain in medial position “to avoid deleting root vowels in words like `*weljaną` → `willan`” [Germanic/docs/DEV_NOTES.md:877-879]. That sentence does not argue for `willan` from first principles, but it does show that `willan` served as a negative control when syncope logic was being broadened. In other words, row `2292` is part of the project's **scope-control evidence**: the pipeline must permit syncope in genuinely medial environments without erasing the root vowel of this inherited verb.

The live derivation trace fits that use perfectly. The current cascade needs the root vowel to survive long enough for `PWGmc J Gemination`, `OE I Umlaut`, and later `OE J Loss After Heavy` to produce `*wéljaną > *wélljaną > *willjąn > willan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5934-5944]. So the DEV_NOTES guardrail is not incidental wording: it matches the actual dependency structure of the productive derivation. If the syncope rule were allowed to hit the wrong `i/e` slot, the row would collapse before the umlaut-and-j-loss pathway now visible in the published trace.

The superseded March 2026 dry run is more limited. DEV_NOTES reports that a temporary `{*ă}`-based A-restoration experiment changed `weljăną` from mismatching `willen` to matching `willan`, but then immediately labels the broader experiment a net failure because it regressed nine other rows and raised the mismatch count from `78` to `79` [Germanic/docs/DEV_NOTES.md:9493-9554]. For row `2292`, this fragment should be preserved as project history only. It shows that `willan` once appeared in a diagnostic infinitive cohort, but it does **not** describe the live row state, and its temporary `weljăną` spelling should not be confused with the current `PROTO = PROTOFORM = *wéljaną` entry [Germanic/data/germanic-aligned-final.tsv:1405-1405].

The main philological caution is lexical bookkeeping, not sound-law instability. The English concept label `will` covers both the verb row `2292` and noun row `2293`, and even OE surface forms can blur that boundary because Campbell's verbal paradigm includes a finite `willa` form under `willan` [docs/references/campbell_old_english_grammar.txt:23639-23647; @Campbell1959]. For this slice, `COUNTERPART = willan` is specifically the verb citation form; `PROTO = *wéljaną` and `PROTOFORM = *wéljaną` identify the verbal derivational input; and the separate noun row uses `*wéljô > willa` instead [Germanic/data/germanic-aligned-final.tsv:1405-1407; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29314; @Kroonen2013]. Later reporting should therefore resist citing generic `willa/will-` hits without first checking whether they belong to the verb paradigm, the noun lexeme, or the separate `*waljan-` “choose” family.

The safest replacement note is conservative. Current DEV_NOTES authority does support row `2292` as a **regular** verbal control case and does preserve one strong current row-explicit anchor, but it does not preserve a rich row-dedicated philological narrative. The slice should therefore be read as guarded working documentation: `*wéljaną -> willan` is stable in the live trace, the best DEV_NOTES anchor is a syncope-scope warning rather than a lexeme dossier, and the most visible later `willan` test block is explicitly diagnostic and superseded [Germanic/docs/DEV_NOTES.md:877-879,9493-9554].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-867-889

- Source heading: `l-adjacent syncope (IMPLEMENTED 2026-03-21, corrected 2026-03-21)`
- Source line or section hint: `lines 867-889`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `l_adjacent_syncope`; `scope_guardrail`; `root_vowel_preservation`; `verbal_will`
- Recommended next use: `cite_if_explaining_why_willan_is_a_negative_control`
- Shared with row IDs: `primary target is a shared syncope change; row 2292 is the explicit guardrail example`

This is the strongest surviving current DEV_NOTES attachment for row `2292`. The key sentence is explicit: the rule must stay medial “to avoid deleting root vowels in words like `*weljaną` → `willan`” [Germanic/docs/DEV_NOTES.md:877-879]. For future use, that wording is worth preserving exactly because it tells later editors what kind of evidence `willan` supplied: not a special exception, but a form whose inherited root vowel must remain untouched while syncope is broadened elsewhere.

The fragment should still be read narrowly. Its primary business is the `netle`/syncope repair, not a `willan` etymology. But because it names `*weljaną -> willan` directly and remains current, it is stronger than a generic concept-name hit and is probably the only line anchor in DEV_NOTES strong enough to support indexing this row on present evidence [Germanic/docs/DEV_NOTES.md:867-889].

### DEV_NOTES:line-9493-9554

- Source heading: `Empirical Validation (Dry Run 2026-03-13)`
- Source line or section hint: `lines 9493-9554`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `superseded`
- Issue tags: `a_restoration`; `temporary_proto_edit`; `infinitive_probe`; `regression_history`
- Recommended next use: `use_only_as_superseded_diagnostic_history`
- Shared with row IDs: `the six-row infinitive test cohort headed by bacan/grafan/wadan/wacan/wascan/willan`

This fragment names the row more directly than many later notes, but it is not live policy. DEV_NOTES reports the temporary success line `weljăną → willan ✓ (was willen)` and then immediately says the experiment regressed nine other rows and made the total mismatch count worse [Germanic/docs/DEV_NOTES.md:9506-9539]. That is useful project history because it shows that `willan` once sat inside a targeted infinitive-fix cohort.

For present purposes, however, the fragment is superseded. The live row no longer uses the trial spelling `weljăną`, and nothing in the current TSV or published trace suggests that row `2292` should be documented through the rejected `{*ă}` experiment rather than through the stable live input `*wéljaną` [Germanic/data/germanic-aligned-final.tsv:1405-1405; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5925-5944]. Preserve this block as evidence of earlier debugging, not as the main justification for the row.

## Superseded or diagnostic material

- No row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found for row `2292`; the linkage fields above are blank because the required support-file scan turned up only adjacent noun-row files for `2293 will / willa`, not row-2292 support [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:1-82; Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md:13-23,74-84].
- The dry-run spelling `weljăną` in DEV_NOTES is diagnostic-only and superseded. It should not be harmonized back into the row metadata without separate evidence, because the live row and the live trace both use `*wéljaną` [Germanic/docs/DEV_NOTES.md:9497-9554; Germanic/data/germanic-aligned-final.tsv:1405-1405; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5925-5944].
- Campbell's verbal paradigm warning matters for later citation hygiene: `willa` can be a finite form of `willan`, not just the noun row `2293` [docs/references/campbell_old_english_grammar.txt:23644-23647; @Campbell1959]. Any future evidence-gathering that relies on bare `willa` hits must therefore separate verbal inflection from noun citation-form evidence.
- The nearby row-2293 packet and memo preserve a stale clause saying that `willan` belongs with `*waljăną`; Kroonen's lexical split shows that this wording is not safe authority for row `2292`, because `*waljan-` is the separate “choose” verb while `willan` belongs under `*weljan- 1` [Germanic/docs/lexeme_reports/packets/2293-will-willa.md:9-9,41-41; Germanic/docs/lexeme_reports/research_memos/2293-will-willa.md:18-20,45-46,102-104; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28917-28922,29294-29314; @Kroonen2013].

## Open questions for later work

- If a final lexeme report is ever written, add a short note aligning project `*wéljaną` more explicitly with dictionary headword `*weljan- 1`, so readers do not mistake accenting/row-input notation for a different reconstruction [Germanic/data/germanic-aligned-final.tsv:1405-1405; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29294-29309; @Kroonen2013].
- If later reporting needs richer OE philology, add a DOE or Bosworth-Toller citation for `willan`; the current slice is adequate, but its direct lexical support still relies mostly on Clark Hall, Sweet, and Campbell rather than on a row-specific packet chain [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48556-48560; docs/references/sweet_anglo_saxon_primer.txt:6903-6903; docs/references/campbell_old_english_grammar.txt:23639-23647; @ClarkHall1960; @Sweet1953; @Campbell1959].
- If `index.tsv` is revisited later, `DEV_NOTES:line-867-889` is the only strong current anchor. `DEV_NOTES:line-9493-9554` should remain non-indexing background because it is explicitly superseded diagnostic history.
