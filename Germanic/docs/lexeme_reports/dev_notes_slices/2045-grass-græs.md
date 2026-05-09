---
row_id: 2045
concept: grass
counterpart: græs
proto: "*grásą"
protoform: "*grásą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
  - Germanic/docs/non_firing_rules_analysis.md
current_status: current_with_form_selection_tension
needs_literature_agent: yes
---

# DEV_NOTES material — 2045 grass / græs

## Current row state

- The live OE row is `ID 2045 | CONCEPT grass | COUNTERPART græs | PROTO *grásą | PROTOFORM *grásą | DERIVATION_CLASS regular`, with no row-local `NOTE`; the source field is only inherited-etymology provenance copied from Wiktionary templates [Germanic/data/germanic-aligned-final.tsv:446-446].
- Coverage infrastructure still treats the row as having no attached packet, memo, or prior report stub: `| 2045 | grass | græs | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:259-259].
- The current published derivation snapshot is uncomplicated and successful: `PROTO: *grásą`, `EXPECTED: græs`, `OUTPUTS: græs`, with only `Anglo Frisian Brightening: *græsą` and `OE Heavy Syllable Nasal Apocope: *græs` firing on the OE side [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1826-1845]. The full trace confirms that every other rule, including `OERMetathesis`, is `[no-change]` for this row [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:12183-12297].
- `oe_known_problems.tsv` currently has no entry for `*grásą`, so the row is not being tracked as an active exception bucket or known mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Repo attestation/reference files are mixed rather than uniform. `old_english_wiktionary.tsv` gives `grass | græs`, but `old_english_swadesh.tsv` gives `grass | gærs`; Clark Hall has both `gærs (græs)` and a separate `græs` entry, while Bosworth-Toller also records `gers` as a variant beside `gærs` in citation material [Germanic/data/old_english_wiktionary.tsv:109-109; Germanic/data/old_english_swadesh.tsv:61-61; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:17976-17977,19489-19489; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:45787-45791].

## Development-note summary

No row-specific `grass / græs / gærs` DEV_NOTES block survives. The usable DEV_NOTES material is therefore **shared-background-only plus philological side-material**, not a bespoke lexeme dossier, and this slice has to say that plainly [Germanic/docs/DEV_NOTES.md:4835-4985,12005-12012].

What survives divides into two distinct strands. First, one shared derivational note explicitly uses `*grasą` as the model neuter a-stem showing the regular chain `*grasą` → `*græsą` → `græs`, i.e. Anglo-Frisian brightening plus loss of final nasalized vowel, with no i-umlaut involved [Germanic/docs/DEV_NOTES.md:12005-12012]. That strand supports the **live FST row state**: `PROTO` and `PROTOFORM` are both still `*grásą`, and the current cascade reaches `græs` without workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1826-1845].

Second, a separate shared DEV_NOTES dossier on OE `r`-metathesis repeatedly uses ‘grass’ as a chronology example. Those quotations preserve three different surface shapes: Campbell's list of forms without metathesis includes `græs`; Campbell's breaking discussion cites `gers grass`; Ringe-Taylor and Luick give `gærs` as the metathesized form, with Luick explicitly contrasting West Saxon `gærs` and Mercian `gers` [Germanic/docs/DEV_NOTES.md:4839-4850,4882-4886,4914-4919,4938-4950]. The surviving DEV_NOTES evidence therefore does **not** amount to a single target-form verdict. It supports `græs` as the direct regular pre-metathesis derivational outcome, but it also preserves strong shared-background evidence that later/dialectal OE metathesized forms `gærs/gers` existed and mattered.

For this row the safest working distinction is: `PROTO` = comparative PGmc `*grásą`; `PROTOFORM` = the same input, because no alternate paradigm cell or substitute reconstruction is in play; current OE `COUNTERPART` field = `græs`, the form the live cascade actually derives; attested or normalized comparators in surviving DEV_NOTES/references = `græs`, `gærs`, and `gers`, which belong to the row's philological form-selection problem, not to protoform selection.

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:12005-12012

- Source heading: `Key insight` / comparison set in the `sæp` stem-class discussion
- Source line hint: `lines 12005-12012`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `anglo_frisian_brightening`; `heavy_syllable_nasal_apocope`; `neuter_a_stem`; `no_i_umlaut`
- Recommended next use: `cite_when_justifying_the_live_unmetathesized_derivation`
- Shared-with rows if relevant: `2168`; other simple a-stem brightening rows

This is the only surviving DEV_NOTES sentence that writes the row's derivation out directly: ``*grasą` → AFB → `*græsą` → apocope → `græs` ✓ (neuter a-stem, no i-umlaut)`` [Germanic/docs/DEV_NOTES.md:12011-12011]. For row 2045 that support is **shared-background-only**, not row-dedicated, but it is still the clearest project statement of why the current pipeline can land on `græs` without any special repair. It matches the live trace exactly: brightening applies, no i-umlaut or A-restoration intervenes, and heavy-syllable nasal apocope removes final `*ą` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1837-1845; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:12242-12247].

Its scope should not be overstated. This fragment supports the regular derivational path from `*grásą` to `græs`; it does **not** decide whether the lexeme should finally be normalized as un-metathesized `græs` or as later metathesized `gærs/gers` in a row whose reference evidence is mixed.

### Germanic/docs/DEV_NOTES.md:4835-4850

- Source heading: `Campbell, Old English Grammar §459`
- Source line hint: `lines 4835-4850`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `r_metathesis`; `non_metathesized_attestation`; `surface_variation`; `philological_background`
- Recommended next use: `cite_when_explaining_why_græs_cannot_be_dismissed_as_non_oe`
- Shared-with rows if relevant: `1974`; `2035`; other `r`-metathesis items

This fragment preserves the non-metathesized side of the evidence. DEV_NOTES quotes Campbell's discussion of OE `r`-metathesis and then his list of forms that occur “without metathesis,” which explicitly includes `græs` alongside `frost`, `cresse`, `drestan`, and others [Germanic/docs/DEV_NOTES.md:4842-4850]. For row 2045 that matters because it shows that `græs` is not merely a modern repo simplification invented by the current TSV: the shared literature excerpt copied into DEV_NOTES itself still recognizes a non-metathesized OE form.

The support here is philological, not derivational. It does not alter `PROTOFORM`, and it does not contradict the live FST trace. What it does is preserve the fact that a working note for this row must allow `græs` to remain a legitimate OE-side comparator even though other DEV_NOTES fragments favor metathesized outcomes for later/dialectal stages.

### Germanic/docs/DEV_NOTES.md:4880-4920

- Source heading: `Campbell §155: Breaking and metathesis interaction` plus `Ringe & Taylor, vol. 2, p.340–341`
- Source line hint: `lines 4880-4920`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `r_metathesis_chronology`; `breaking`; `gers`; `gærs`; `late_metathesis`
- Recommended next use: `cite_when_explaining_the_græs_vs_gærs_gers_split`
- Shared-with rows if relevant: `1974`; `2035`; other late-metathesis rows

This is the strongest surviving DEV_NOTES evidence that the row's form-selection problem is **chronological and dialectal**, not protoform-based. Campbell is quoted: “Metathesis of r (§ 459) usually took place too late for secondary r-groups to cause breaking, e.g. `gers` grass, `berst` he burst ...” [Germanic/docs/DEV_NOTES.md:4882-4886]. Ringe-Taylor then restates the point and lists “typical examples” that “underwent metathesis after breaking,” including `gærs` 'grass' [Germanic/docs/DEV_NOTES.md:4914-4919].

For row 2045, this means the comparative chain can remain `*grásą > *græs`, while `gærs/gers` are later OE surface developments conditioned by the timing of `r`-metathesis relative to breaking. The fragment is therefore **shared-background-only but highly relevant**: it does not require changing `PROTO` or `PROTOFORM`, but it warns against treating current `græs` as the only historically salient OE shape.

### Germanic/docs/DEV_NOTES.md:4934-4985

- Source heading: `Luick §136 Anm. 1` plus `The definitive study: Stanley (1952)`
- Source line hint: `lines 4934-4985`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `west_saxon_vs_mercian`; `gærs`; `gers`; `post_breaking_metathesis`; `normalization_question`
- Recommended next use: `cite_when_assessing_whether_the_row_should_stay_græs`
- Shared-with rows if relevant: `1974`; `2035`; other OE `r`-metathesis chronology rows

This fragment is the clearest surviving DEV_NOTES statement about dialect-normalized outcomes. Luick is quoted that, when `r + consonant` arose secondarily through metathesis, breaking “unterblieb ... namentlich im Westsächsischen,” with explicit examples including West Saxon `gærs` and Mercian `gers` [Germanic/docs/DEV_NOTES.md:4938-4950]. DEV_NOTES then summarizes Stanley's conclusions and makes the row-local implication fully explicit: “Metathesis in *grass, burst, thresh, fresh* was universally late (post-breaking),” with `gærs` derived from earlier `græs` in the example list [Germanic/docs/DEV_NOTES.md:4967-4985].

This is still **shared background**, not a direct instruction to rewrite row 2045, but it is the strongest evidence that a later West Saxon normalization would likely prefer `gærs`, with `gers` as an Anglian/Mercian comparator. In other words, the live row's `græs` is best treated as the direct pre-metathesis output currently chosen by the pipeline, while `gærs/gers` are preserved in DEV_NOTES as later/dialectal continuations that remain philologically relevant.

## Superseded or diagnostic material

- `Germanic/docs/non_firing_rules_analysis.md` preserves an **old diagnostic state**, not live row policy. In that earlier mismatch set the grammar over-applied A-restoration and produced ``*grasą -> grasa (expected græs)`` with the comment `s alone should block` [Germanic/docs/non_firing_rules_analysis.md:155-175]. The same document later marks “Fix A-F brightening over-application” as completed [Germanic/docs/non_firing_rules_analysis.md:577-582]. For row 2045 this material is useful only as project archaeology: the current trace already shows the problem is gone.
- The present trace's `[no-change]` at `OERMetathesis` is **diagnostic**, not yet a documented exception claim. DEV_NOTES' shared metathesis dossier treats ‘grass’ as a classic late-metathesis lexeme, but the live row is currently normalized to pre-metathesis `græs` and `oe_known_problems.tsv` does not flag that choice as an unresolved bug [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:12284-12287; Germanic/docs/DEV_NOTES.md:4882-4886,4914-4919,4967-4985; Germanic/data/oe_known_problems.tsv:1-8].
- The mixed lexicographic evidence (`græs`, `gærs`, `gers`) is also diagnostic rather than superseded. Nothing in surviving DEV_NOTES collapses those spellings into a single definitive row target, so later work should not pretend that the current `COUNTERPART` field already resolves the normalization question [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:17976-17977,19489-19489; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:45787-45791].

## Open questions for later work

- Decide whether row 2045 should stay normalized to derivationally direct `græs`, or whether the row should eventually target/annotate metathesized West Saxon `gærs` and/or Anglian-Mercian `gers`, since surviving DEV_NOTES material strongly preserves the latter forms while the live cascade currently outputs the former [Germanic/docs/DEV_NOTES.md:4882-4886,4914-4919,4938-4950,4967-4985].
- If `græs` is retained as the row target, document it explicitly as a conservative pre-metathesis or un-metathesized comparator rather than implying that it is the only relevant OE lexical form. The current slice should already be read that way, but later report prose could still flatten the distinction if not careful.
- Check whether `OERMetathesis` is intentionally left non-operative for this lexical environment, or whether row 2045 is simply not yet being used as a metathesis regression target. The trace and DEV_NOTES chronology are currently in tension, but not yet in an issue bucket [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:12284-12287; Germanic/data/oe_known_problems.tsv:1-8].
