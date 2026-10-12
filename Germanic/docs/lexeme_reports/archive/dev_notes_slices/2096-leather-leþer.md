---
row_id: 2096
concept: leather
counterpart: leþer
proto: *léθrą
protoform: *léθrą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2096 leather / leþer

## Current row state

- CONCEPT: `leather`
- COUNTERPART: `leþer`
- PROTO: `*léθrą`
- PROTOFORM: `*léθrą`
- DERIVATION_CLASS: `regular`
- The live TSV row is sparse and stable: it gives `Old_English` `leþer` from `*léθrą`, marks the row `regular`, and carries only Wiktionary inheritance sourcing, with no row-local NOTE/HISTORY guidance preserved in the visible row state [Germanic/data/germanic-aligned-final.tsv:641-643].
- Current derivation/debug state is fully regular. The compact trace gives `PROTO: *léθrą`, `EXPECTED: leþer`, `OUTPUTS: leþer`, with the only overt OE operations being `OE Heavy Syllable Nasal Apocope: *léθr` and `OE Epenthetic Vowel: *léθer`, followed by orthographic `þ` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3191-3211]. The full trace confirms the same sequence at rule level: `OEHeavySyllableNasalApocope` removes final `*ą`, `OEEpentheticVowel` inserts the vowel before final `*r`, and the surface stage yields `leþer` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18099-18213].
- There is no row-local exception bookkeeping. `oe_known_problems.tsv` contains only a short exception list for other protoforms and does not include `2096`, `*léθrą`, or `leþer` [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage bookkeeping currently treats the row as not requiring a manifest-backed report: coverage audit line 289 marks `2096 | leather | leþer | regular | no | - | - | - | none`, and the manifest itself contains only pilot entries, with no `2096` row [Germanic/docs/lexeme_reports/coverage_audit.md:284-292; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- No packet, research memo, dossier, or prior slice currently exists for this row. This replacement note therefore has to be built from the live row plus shared DEV_NOTES process discussions and current trace output, not from a surviving lexeme-local note block.

## Development-note summary

No row-specific DEV_NOTES block for `leather / leþer` survives. There is no `2096`, `leather`, `leþer`, or `*léθrą` hit in `DEV_NOTES.md`, so this slice must say plainly that all usable DEV_NOTES support is **shared-background-only** rather than lexeme-specific [Germanic/docs/DEV_NOTES.md:1-39869].

The shared material nevertheless matches the live derivation unusually cleanly. The row's present FST path is: (1) heavy-stem loss of final `*ą`, giving `*léθr`; (2) late OE parasitic vowel insertion in the resulting final `CR` cluster, with front-vowel coloring yielding `*léθer`; (3) orthographic `þ` for inherited `*θ`, giving surface `leþer` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18161-18213; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2720-2740].

What survives from DEV_NOTES is therefore process guidance, not leather-specific decision prose. The current epenthesis note is directly applicable shared background; the late chronology quotation from Ringe-Taylor explains why such epenthesis belongs after vowel loss; and the archived heavy-syllable `*ą` apocope note is the only DEV_NOTES passage that squarely discusses the process needed for `*léθrą > *léθr`, but it is still archived/diagnostic rather than a leather-specific current policy statement [Germanic/docs/DEV_NOTES.md:16661-16691; Germanic/docs/DEV_NOTES.md:30262-30288; Germanic/docs/DEV_NOTES.md:1591-1645].

## Relevant DEV_NOTES fragments

This row has **no surviving row-specific DEV_NOTES fragment**. The fragments below are retained because they explain the exact rule path seen in the live trace, but each one is shared process material rather than leather-only discussion.

### DEV_NOTES:line-16661-16691

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Source line hint: `lines 16661-16691`
- Fragment type: `shared_process_note`
- Status: `current`
- Issue tags: `epenthesis`; `final_CR_cluster`; `front_vowel_coloring`; `shared_background_only`
- Recommended next use: `cite_as_current_process_support`
- Shared-with rows if relevant: `2060?, 2129?, 2160, 2230, 2280, 2295 and other final-CR outputs; especially rows whose trace ends in OE epenthetic -er/-or`

DEV_NOTES states explicitly that `OEEpentheticInsertion` "inserts an epenthetic vowel before final `*r` (and `*l` in specific contexts) when preceded by a consonant cluster," with rule sketch ``{*r} -> {*E} {*r} || (V) C+ _ .#.`` [Germanic/docs/DEV_NOTES.md:16663-16669]. It further insists this is a "real phonological rule" for "parasitic vowel insertion" / "anaptyxis," not a local hack, and gives the vowel-quality split that matters directly here: "After back vowels: `*E → *o` ... After front vowels: `*E → *e`" [Germanic/docs/DEV_NOTES.md:16677-16691]. For row `2096`, this is the clearest current DEV_NOTES support for the trace step `*léθr -> *léθer`: the final cluster is `*θr`, and the preceding stressed vowel is front `é`, so the row's `-er` outcome is exactly the front-colored branch of the shared epenthesis rule rather than an ad hoc leather-specific repair [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18202-18213].

This fragment is **shared-background-only**, not row-specific. It never names leather, and its examples are `finger`, `timber`, `winter`, and `hungor` [Germanic/docs/DEV_NOTES.md:16671-16675]. Still, the fit to the live leather trace is exact enough that later reporting can safely treat it as the current process-level authority for the `-er` portion of `leþer`.

### DEV_NOTES:line-30262-30288

- Source heading: `###### (c) §6.9.5 (printed p. 327ff.) — Epenthesis is a separate, much later change`
- Source line hint: `lines 30262-30288`
- Fragment type: `shared_literature_quote`
- Status: `current`
- Issue tags: `epenthesis_chronology`; `Ringe_Taylor`; `loss_of_earlier_vowel`; `shared_background_only`
- Recommended next use: `cite_for_chronology_and_scope`
- Shared-with rows if relevant: `2133 and other rows where late OE epenthesis must be kept distinct from inherited medial vowels`

This fragment preserves the most useful direct quotation for the chronology behind the leather trace. DEV_NOTES quotes Ringe-Taylor: "By the PWGmc loss of word-final short low vowels ... numerous word-final CR-clusters arose; the apocope of short high vowels after heavy stressed syllables ... created a few more. Early in the attested history of OE short vowels were inserted in some of those consonant clusters; the process is variously referred to as **epenthesis, anaptyxis, syllabification, or 'parasiting'** ... epenthesis cannot have begun much before the middle of the 7th century and might have begun within the 8th" [Germanic/docs/DEV_NOTES.md:30266-30273]. DEV_NOTES then sharpens the point: epenthesis applies to word-final clusters "that arose by the *loss* of an earlier vowel" [Germanic/docs/DEV_NOTES.md:30275-30281].

For row `2096`, that chronology maps neatly onto the trace: `*léθrą` first loses final `*ą`, yielding the final cluster `*θr`; only after that does OE epenthesis create `*léθer` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18161-18203]. This is again **shared-background-only** support, because the fragment is embedded in a navel discussion, not a leather note. But it is materially relevant and should be preserved because it explains why the `-e-` of `leþer` is a late OE syllabification response to cluster creation, not an inherited vowel already present in `PROTO` or `PROTOFORM`.

### DEV_NOTES:line-1591-1645

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `lines 1591-1645`
- Fragment type: `archived_process_note`
- Status: `diagnostic`
- Issue tags: `heavy_syllable_apocope`; `final_*ą_loss`; `archived_but_row_relevant`; `shared_background_only`
- Recommended next use: `use_cautiously_for_rule_history`
- Shared-with rows if relevant: `many heavy-stem neuters and any row whose current trace uses OEHeavySyllableNasalApocope`

This is the only DEV_NOTES passage that squarely discusses the process needed for the first leather step `*léθrą -> *léθr`, but it is explicitly archived and empirical rather than a polished lexeme note. It records the discovery that many spurious final vowels involved heavy stems and states: "Neither source explicitly extends this pattern to `*-ą`" but "The same heavy/light conditioning that applied to `*-i/*-u` **also applied to `*-ą`**" [Germanic/docs/DEV_NOTES.md:1604-1612]. It also records the rule implementation, `{*H} {*ą} -> 0 || _ .#.`, and gives successful examples such as `*bergą → beorg`, `*wurdą → word`, and `*blōdą → blōd` [Germanic/docs/DEV_NOTES.md:1617-1633].

For row `2096`, this fragment is not current leather-specific authority, but it is the best surviving DEV_NOTES explanation for why the full trace begins its OE-specific work with `OEHeavySyllableNasalApocope: *léθr` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18161-18163]. Use it conservatively: it supports the process seen in the live grammar, yet because the section is archived and presents the rule as an empirically discovered extension rather than a settled handbook quotation, later writers should label it as **diagnostic/shared-background** support, not as a definitive leather memorandum.

## Superseded or diagnostic material

- No leather-specific DEV_NOTES block survives at all. The absence itself is important: there is nothing row-local to quote, supersede, or reconcile against the live TSV beyond shared process notes and the current trace [Germanic/docs/DEV_NOTES.md:1-39869].
- The heavy-syllable `*ą` apocope note is the most row-relevant DEV_NOTES material for the first derivational step, but it is explicitly archived and framed as an "EMPIRICAL DISCOVERY," so it should not be cited as if DEV_NOTES had a polished, lexeme-specific leather decision section [Germanic/docs/DEV_NOTES.md:1591-1645].
- Manifest/coverage metadata are diagnostic only. Coverage audit marks row `2096` as `none`, and the manifest contains no entry; this tells us only that the lexeme never received a packet-backed report in the current documentation workflow, not that the derivation is uncertain [Germanic/docs/lexeme_reports/coverage_audit.md:289-289; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The live trace should outrank any attempt to infer extra hidden complexity from the absence of row notes. At present the grammar derives `leþer` cleanly from `*léθrą` with no detours, exceptions, or competing outputs in the cited snapshots [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:3191-3211; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:18099-18213].

## Open questions for later work

- If a later packet/memo is created, add direct external-literature citations for the two operative steps separately: heavy-stem loss of final `*ą` and late OE parasitic vowel insertion in final `CR` clusters. Right now the slice relies on shared DEV_NOTES summaries plus trace output rather than a leather-specific source audit.
- Consider promoting the archived heavy-syllable `*ą` apocope discussion into a stable current reference section somewhere in DEV_NOTES or companion analysis. Rows like `2096` currently depend on an archived discovery note for the apocope half of an otherwise regular derivation.
- If final prose later compares cognate-set structure, keep the distinctions explicit: `PROTO`/`PROTOFORM` here are both `*léθrą`; the attested OE target is `leþer`; the inserted `-e-` belongs to late OE epenthesis after cluster creation, not to the inherited proto representation [Germanic/data/germanic-aligned-final.tsv:641-643; Germanic/docs/DEV_NOTES.md:30275-30288].
