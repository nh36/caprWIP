---
row_id: 1956
concept: bore
counterpart: borian
proto: *búrōjaną
protoform: *búrōjaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/lexeme_reports/coverage_audit.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1956 bore / borian

## Current row state

- The live OE row is `1956	bore	borian`, with `PROTO = *búrōjaną`, `PROTOFORM = *búrōjaną`, and `DERIVATION_CLASS = regular`; the only row-local note currently in the TSV is duplicated inherited-etymology provenance rather than a substantive lexeme note [Germanic/data/germanic-aligned-final.tsv:96-96].
- `old_english_wiktionary.tsv` matches the live target exactly as `bore	borian	inh	template:inh	bore`, so the imported OE source layer presently agrees with `COUNTERPART = borian` but does not itself explain the modelling choice [Germanic/data/old_english_wiktionary.tsv:24-24].
- `oe_known_problems.tsv` has no entry for `*búrōjaną`, `borian`, or row `1956`, so this lexeme is not currently being carried as an active OE exception bucket even though older DEV_NOTES discussion treated this Class II weak-verb shape as problematic [Germanic/data/oe_known_problems.tsv:1-8].
- The current published OE derivation trace is an exact match: `PROTO: *búrōjaną`, `EXPECTED: borian`, `OUTPUTS: borian`, with the explicit path `*búrōjaną > *bórōjaną > *bórōjan > *bórōjąn > *bórējąn > *bórejąn > *bórejan > *bóreian > *bórian > borian` through Northwest Germanic `u`-lowering, heavy-syllable nasal apocope, i-umlaut, unstressed long-vowel shortening, weak-tail reduction, intervocalic `j` vocalization, and unstressed `ei` contraction [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:369-388].
- No matching row-stem packet or research memo file was found for `1956-bore-borian`; `coverage_audit.md` correspondingly still lists the row as uncovered infrastructure: `| 1956 | bore | borian | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:204-204].

## Development-note summary

The surviving DEV_NOTES material for row `1956` is real and materially relevant, but it is not a single settled row dossier. It preserves two different project phases that later reporting should keep distinct rather than collapse into a false impression of uninterrupted agreement.

The earlier phase treats `borian` as part of a **mismatch class** affecting Class II weak-verb infinitives in `*-ōja-`. DEV_NOTES puts `*burōjăną → boreian (expected borian)` in the `suffix_form__eian_vs_ian` bucket, then states the basic reason in programmatic terms: “The infinitive suffix *-ōja- is a MORPHOLOGICAL innovation … It is not a regular sound change. OE -ian does not derive by regular phonology from *-ōjanan” [Germanic/docs/DEV_NOTES.md:2761-2769]. That is not a casual aside. It is the main surviving explanation of why row `1956` originally looked non-regular even though the target form itself was not in dispute.

That same early note then records the concrete policy problem the project faced. The full Class II table again lists `*burōjăną | boreian | borian | suffix_form__eian_vs_ian`, and DEV_NOTES generalizes from the table that “ALL share the -eian issue. The *-ōja- suffix is morphological … Our FST cannot and SHOULD NOT model this analogical change” [Germanic/docs/DEV_NOTES.md:2821-2836]. The note therefore explored resolution options rather than claiming the row was already solved: switch citation forms to a regular imperative or 3sg shape, or else document these infinitives as known non-regular cases [Germanic/docs/DEV_NOTES.md:2838-2861]. For row `1956`, that earlier discussion remains important project history and should not be erased merely because the present trace now succeeds.

The later phase moves in a different direction and is closer to the current live row state. In the `sparian` dossier, DEV_NOTES explicitly adopts a **very-early analogy / transponent** policy for class-III-to-class-II refashioned verbs and cites `búrōjaną → borian` as one of the already-admitted comparanda. The key statement is that the TSV `PROTOFORM` can encode “the class-II shape that the attested OE paradigm presupposes,” after which the FST derives the OE form “by regular sound change from this shape,” just as it does for “`búrōjaną → borian`, `líznōjaną → liornian`, `xándlōjaną → handlian`, `súndrōjaną → sundrian`, etc.” [Germanic/docs/DEV_NOTES.md:37888-37898]. The rejected alternative was to keep a class-III comparative form and force a very-late OE repair; DEV_NOTES rejects that as contrary to the project's aim of maintaining “the longest possible lautgesetzlich span from a genuinely reconstructable PGmc form to an actually attested OE form” [Germanic/docs/DEV_NOTES.md:37900-37914].

Taken together, those passages explain the present row better than either one alone. The old Class II note explains why `borian` once counted as a morphological `-eian` problem; the later transponent note explains why the current system is willing to accept an OE-facing class-II `PROTOFORM` and treat the resulting `borian` output as a regular derivation from that modelling input. The live trace confirms that the latter operational policy is now what the grammar actually does [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:369-388]. What remains thin is not derivational success but row-local narrative closure: there is still no dedicated packet, memo, or lexeme-specific DEV_NOTES dossier written just for `bore / borian`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2759-2779

- Source heading: `Implications for Class II Weak Verbs`
- Source line or section hint: `lines 2759-2779`
- Fragment type: `diagnostic_background_for_lexeme`
- Status: `current_background`
- Issue tags: `class_ii_weak_verbs`; `suffix_form__eian_vs_ian`; `morphological_suffix`; `original_mismatch_statement`
- Recommended next use: `cite_to_explain_why_row_once_looked_non_regular`
- Shared with row IDs: `1956; 2141; 2310`

This is the clearest surviving statement of the original `borian` problem. DEV_NOTES names the row directly: “`*burōjăną → boreian (expected borian)`,” then immediately states the governing claim: “The infinitive suffix `*-ōja-` is a MORPHOLOGICAL innovation … It is not a regular sound change. OE `-ian` does not derive by regular phonology from `*-ōjanan`” [Germanic/docs/DEV_NOTES.md:2761-2769]. For row `1956`, this fragment matters because it preserves the reasoning, not just the mismatch label: the issue was not that the target `borian` was philologically doubted, but that the inherited infinitive shape was understood as morphologically remodelled rather than phonologically automatic.

> “`*burōjăną → boreian (expected borian)`” [Germanic/docs/DEV_NOTES.md:2761-2763]

> “The infinitive suffix `*-ōja-` is a MORPHOLOGICAL innovation … It is not a regular sound change. OE `-ian` does not derive by regular phonology from `*-ōjanan`.” [Germanic/docs/DEV_NOTES.md:2766-2769]

### DEV_NOTES:line-2821-2861

- Source heading: `All 8 Class II Weak Verbs in TSV (all produce -eian)` plus `Options for Resolution`
- Source line or section hint: `lines 2821-2861`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded_as_live_problem_state`
- Issue tags: `class_wide_table`; `resolution_options`; `document_vs_recode`; `project_chronology`
- Recommended next use: `keep_as_project_history`
- Shared with row IDs: `1956; 2141; 2310; 2055`

This fragment records the project's pre-transponent decision space. The table again lists the row as `*burōjăną | boreian | borian | suffix_form__eian_vs_ian`, then generalizes: “ALL share the `-eian` issue. The `*-ōja-` suffix is morphological … Our FST cannot and SHOULD NOT model this analogical change” [Germanic/docs/DEV_NOTES.md:2821-2836]. DEV_NOTES then lays out four possible responses, recommending a split between regular citation-form substitution where possible and plain documentation elsewhere [Germanic/docs/DEV_NOTES.md:2838-2861]. This is superseded as a description of the current row state, because the live system now outputs `borian`; but it is still worth preserving as project chronology and as evidence that the present `regular` row label was not the repo's only earlier framing.

> “ALL share the `-eian` issue. The `*-ōja-` suffix is morphological … Our FST cannot and SHOULD NOT model this analogical change.” [Germanic/docs/DEV_NOTES.md:2834-2836]

> “**Recommendation**: Option A (iptv. 2sg with trimoric `*ô`) for verbs where it works cleanly, combined with Option C (documentation) for verbs where the iptv. form introduces other complications.” [Germanic/docs/DEV_NOTES.md:2858-2861]

### DEV_NOTES:line-37888-37914

- Source heading: `Very-early analogy (Plan A, taken)` in the `sparian` dossier
- Source line or section hint: `lines 37888-37914`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `transponent`; `early_analogy`; `class_iii_to_class_ii_refashioning`; `borian_named_example`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1956; 2141; 2055; 2220`

This is the strongest current project-local support for leaving row `1956` as a working OE-facing derivation rather than as an unresolved mismatch. DEV_NOTES says the class-II `PROTOFORM` can be a “transponent in the strict sense,” encoding “the class-II shape that the attested OE paradigm presupposes,” and then explicitly names `búrōjaną → borian` among the verbs that the FST derives “by regular sound change from this shape” [Germanic/docs/DEV_NOTES.md:37888-37898]. The same passage rejects the rival late-analogy strategy because it would either depend on unattested targets or on a non-Lautgesetz workaround [Germanic/docs/DEV_NOTES.md:37900-37914]. For row `1956`, this shared fragment is thin but important: it does not give a full `borian` dossier, yet it does show that later DEV_NOTES work treated the row as an admissible early-analogy/transponent case rather than as a standing infinitive mismatch.

> “The TSV `PROTOFORM` `*spárōjaną` is a **transponent** in the strict sense — it encodes the class-II shape that the attested OE paradigm presupposes … exactly as it does for the other class-III→II refashioned verbs already in the TSV (`búrōjaną → borian`, `líznōjaną → liornian`, `xándlōjaną → handlian`, `súndrōjaną → sundrian`, etc.).” [Germanic/docs/DEV_NOTES.md:37889-37898]

> “Plan A is therefore the only admissible route.” [Germanic/docs/DEV_NOTES.md:37910-37914]

## Superseded or diagnostic material

- The old `boreian` mismatch diagnosis is **superseded as a live output state**, because the published OE trace now reaches `borian` exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:369-388]. It should still be kept as diagnostic history, since it is the only surviving note that explains why Class II infinitives in `*-ōja-` once looked non-regular in the first place [Germanic/docs/DEV_NOTES.md:2759-2861].
- The option discussion around imperative `2sg` or present `3sg` citation forms is likewise diagnostic only for this row's current state. It documents one abandoned resolution strategy, not the active one. Its main value now is to show that the project explicitly considered keeping `borian` outside the regular derivational path before later transponent policy made rows like this acceptable again [Germanic/docs/DEV_NOTES.md:2838-2861].
- The shared note on non-final unstressed `*ō` is relevant only as background to those abandoned alternative citation forms. DEV_NOTES remarks that in medial position “bimoric and trimoric `*ō` MERGED to `*ō`” and uses `*salbōþi … > OE sealfaþ` to motivate a possible 3sg-based modelling route [Germanic/docs/DEV_NOTES.md:2802-2819]. That background helps explain the old option set, but it is not itself a row-local argument for the current `*búrōjaną > borian` line.
- `coverage_audit.md` remains purely infrastructural. Its `no / none` entry confirms that this slice is filling an actual coverage gap, but it is not philological authority for the row [Germanic/docs/lexeme_reports/coverage_audit.md:204-204].

## Open questions for later work

- If row `1956` is ever given a full packet or final report, decide whether the row should continue to be described simply as `regular` or more explicitly as an **OE-facing early-analogy / transponent** case. The current trace supports the latter interpretation more directly than the bare label does [Germanic/docs/DEV_NOTES.md:37888-37914; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:369-388].
- A later report should state the chronology explicitly rather than smoothing it over: earlier DEV_NOTES called the infinitive `*-ōja-` row type morphological and non-phonological, while later DEV_NOTES accepted `búrōjaną → borian` inside a transponent policy. Both phases are part of the row's real project history [Germanic/docs/DEV_NOTES.md:2759-2861,37888-37914].
- If future indexing requires stronger row-local support, this slice is probably still a borderline case. The row now has meaningful DEV_NOTES support, but most of it is shared class-level policy rather than a dedicated `bore / borian` dossier, and there is still no row-specific packet or research memo to anchor a richer note infrastructure [Germanic/docs/lexeme_reports/coverage_audit.md:204-204].
