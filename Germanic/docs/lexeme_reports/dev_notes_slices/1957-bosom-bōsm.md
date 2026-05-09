---
row_id: 1957
concept: bosom
counterpart: bōsm
proto: *bōsmaz
protoform: *bōsmaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1957 bosom / bōsm

## Current row state

- The live OE row reads `1957 | bosom | bōsm | *bōsmaz | *bōsmaz | regular`, with only duplicated imported provenance in the history field (`Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`) and no row-local explanatory note in the TSV itself [Germanic/data/germanic-aligned-final.tsv:100-100].
- For current project purposes, the live row authority is therefore `PROTO = *bōsmaz`, `PROTOFORM = *bōsmaz`, `COUNTERPART = bōsm`, `DERIVATION_CLASS = regular`; this replacement slice should not silently substitute a different proto spelling unless and until the TSV itself changes [Germanic/data/germanic-aligned-final.tsv:100-100].
- The published OE derivation trace is an exact match: `PROTO: *bōsmaz`, `EXPECTED: bōsm`, `OUTPUTS: bōsm`, with the compact path `*bōsmaz > *bōsma > *bōsm` through final `-z` deletion and final bare `-a` loss [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:390-408].
- `oe_known_problems.tsv` has no entry for `*bōsmaz`, `bōsm`, or row `1957`, so the row is not currently tracked as an OE exception or known failure case [Germanic/data/oe_known_problems.tsv:1-8].
- No matching packet or research memo file was found for this row, and `coverage_audit.md` still records it as uncovered regular material: `| 1957 | bosom | bōsm | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:205-205].

## Development-note summary

The surviving DEV_NOTES material for row 1957 is real but mostly **shared-class** material rather than a dedicated bosom dossier. The two main contexts are: (1) a regression note where `bōsm` appears as one of several heavy a-stem nominatives that briefly acquired an incorrect final vowel, and (2) the later `-Cl/-Cn/-Cm#` cluster note that explicitly treats `bōsm` as one of the ten unbroken nominative targets the dataset intentionally keeps [Germanic/docs/DEV_NOTES.md:22065-22137; Germanic/docs/DEV_NOTES.md:29853-30083].

The regression note matters because it preserves an explicit wrong intermediate output for this lexeme. DEV_NOTES says that after Phase 1d-β, forms such as `*bárdaz` began surfacing with a spurious final `e`, including “`bōsme`” instead of correct `bōsm` [Germanic/docs/DEV_NOTES.md:22067-22070]. Although the worked trace there is shown with `*bárdaz`, `bōsm` is not incidental name-dropping; it is one of the concrete witness forms for the same bug. The note's argument is chronological as well as diagnostic: word-final short `*a` should already be gone before Anglo-Frisian fronting can touch it, so the correct output requires early apocope rather than a late cleanup of fronted final `*æ` [Germanic/docs/DEV_NOTES.md:22099-22137]. For row 1957, the substance to preserve is that `bōsm` served as a control form showing why final-vowel loss must precede any OE-internal fronting effects.

The later cluster note is even more directly relevant. DEV_NOTES lays out the shared background for stem-final obstruent + sonorant clusters and explicitly lists `bōsom` as the kind of broken late form that can arise when the cluster is word-final: “*e* after front stressed vowels ...; *o* after back stressed vowels: `fugol, wuldor, wundor, māþum, bōsom`” [Germanic/docs/DEV_NOTES.md:29857-29862]. But the same note then classifies `-sm` as “relatively parasiting-resistant” and records the live TSV/FST state as `| 2 | *bōsmaz | bōsm | bōsm | ✓ |` [Germanic/docs/DEV_NOTES.md:29879-29879; Germanic/docs/DEV_NOTES.md:29887-29903]. In the attestation table, `bōsm` is specifically marked as an attested unbroken nominative — “standard (Beowulf, Genesis A)” — while broken `bōsom` is only “late (Ælfric)” [Germanic/docs/DEV_NOTES.md:29909-29913].

That evidence feeds directly into the resolved project policy. DEV_NOTES preserves the ruling that if unbroken forms are attested in Beowulf/poetic and early/Anglian usage, the dataset should keep them, changing only thistle to another paradigm cell [Germanic/docs/DEV_NOTES.md:30069-30073]. `bōsm` is named among the ten rows retained unchanged, and DEV_NOTES says the current FST behavior “is correct for these ten lemmas: it produces an unbroken cluster which matches the early / poetic / Anglian register chosen by the dataset” [Germanic/docs/DEV_NOTES.md:30075-30083]. For row 1957, that is the strongest current project-level authority: `bōsm` is not a gap awaiting parasitic `bōsom`, but an intentionally retained unbroken nominative target.

The safest replacement-note conclusion is therefore narrow. Row 1957 is currently stable, regular, and successfully derived; DEV_NOTES preserves meaningful shared support for why `bōsm` is kept, but that support is largely class-wide rather than row-exclusive [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:390-408; Germanic/docs/DEV_NOTES.md:29853-30083]. This makes the slice useful and more substantial than a pure “no notes found” case, but still somewhat thin compared with rows that have dedicated packets, memos, or lexeme-specific implementation history.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-22065-22137

- Fragment type: `shared_regression_note`
- Status: `current_as_engineering_history`
- Issue tags: `final_vowel_extra`; `apocope`; `chronology`; `shared_heavy_a_stem_control`
- Recommended next use: `cite_when_explaining_why_bōsm_must_not_surface_as_bōsme`
- Shared with row IDs: `1940; 1957; 1959`

This fragment preserves the regression in the repo's own wording:

> “The largest bucket (60 cases) is `final_vowel_extra`: heavy a-stem nom.sg.
> forms such as `*bárdaz` now surface with a spurious final `e`
> (`bearde`, `bōsme`, `botme`, …) instead of the correct apocoped
> `beard`, `bōsm`, `botm`.” [Germanic/docs/DEV_NOTES.md:22067-22070]

The later part of the same block states the chronology claim that makes the example matter:

> “Both are pre-OE PWGmc changes... Hence at AFB time, no
> short word-final `*a` exists to front.” [Germanic/docs/DEV_NOTES.md:22114-22121]

For row 1957, the value of the fragment is not that it gives a bespoke bosom derivation. Its value is that `bōsm` is explicitly one of the lexemes used to diagnose why final weak-vowel deletion must be protected from word-final fronting. That makes the fragment worth carrying forward even though the detailed sandbox trace is shown with `*bárdaz`, not with `*bōsmaz` [Germanic/docs/DEV_NOTES.md:22072-22137].

### DEV_NOTES:line-29853-29947

- Fragment type: `shared_cluster_background`
- Status: `current`
- Issue tags: `parasiting`; `cluster_nouns`; `attestation`; `late_vs_early_register`
- Recommended next use: `cite_in_any_final_report_for_1957`
- Shared with row IDs: `1957; 1959; 2053; 2183; 2246; 2250; 2260`

This is the core philological background for the row. DEV_NOTES first gives the class-wide rule:

> “In the **NomSg/AccSg** of masc/neut a-stems (zero
> ending) the cluster falls **word-finally**, where late OE develops a
> **parasite vowel** ...
> ... *o* after back stressed vowels: `fugol, wuldor, wundor, māþum, bōsom`.”
> [Germanic/docs/DEV_NOTES.md:29857-29862]

But the same section immediately narrows the relevance for `bōsm` specifically. It says `-tm, -fn, -sm` are “relatively parasiting-resistant” [Germanic/docs/DEV_NOTES.md:29876-29879], then records the current TSV/FST pair as an exact match:

> `| 2 | *bōsmaz | bōsm | bōsm | ✓ |` [Germanic/docs/DEV_NOTES.md:29887-29890]

The attestation table is the most useful row-facing part:

> `| 2 | bōsm | ✅ standard (Beowulf, Genesis A) | ✅ late (Ælfric) | **bōsm** |`
> [Germanic/docs/DEV_NOTES.md:29909-29913]

Together, those lines preserve the substance that later reporting needs: broken `bōsom` is a real late OE possibility, but the project has documentary grounds for keeping unbroken `bōsm` as the target because that form is directly attested and belongs to the older / poetic side of the distribution [Germanic/docs/DEV_NOTES.md:29937-29946].

### DEV_NOTES:line-30067-30083

- Fragment type: `shared_resolved_policy`
- Status: `current`
- Issue tags: `row_policy`; `unbroken_nom_sg_retained`; `editorial_register_choice`
- Recommended next use: `strongest_current_project_authority`
- Shared with row IDs: `1957; 1959; 2053; 2183; 2246; 2260`

This is the clearest current policy statement touching row 1957. DEV_NOTES preserves the governing ruling:

> “If unbroken versions are attested in Beowulf/poetic and early/Anglian,
> let's stick with them. Move ONLY thistle to another paradigm cell which
> is lautgesetzlich and attested.” [Germanic/docs/DEV_NOTES.md:30071-30073]

It then applies that ruling to the actual retained set:

> “The dataset's existing unbroken NomSg targets (#2–#11: *bōsm, botm, hæsl,
> nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn*) are all directly attested
> manuscript spellings ... They are therefore retained unchanged.” [Germanic/docs/DEV_NOTES.md:30075-30080]

For row 1957 this is stronger than a mere mention in a candidate table. It is the explicit statement that the dataset's present `bōsm` target is intentional and that the current no-parasiting FST behavior is the desired one for this lexeme class [Germanic/docs/DEV_NOTES.md:30080-30083].

## Superseded or diagnostic material

- DEV_NOTES seriously considered a broader parasiting solution that would have changed this row to broken `bōsom`: “update all 11 TSV targets to broken forms: `þistel, bōsom, botem, hæsel, nǣdel, ofen, hræfen, scofol, stefen, tācen, wǣpen`” [Germanic/docs/DEV_NOTES.md:29959-29969]. For row 1957, that proposal is superseded. It remains useful only as evidence that the project explicitly weighed, and then declined, a late-WS-prose-oriented normalization.
- The `bōsme` form in the Phase 1d-β regression note is likewise diagnostic only. It records a temporary bad output caused by rule ordering, not a rival target or a legitimate attested lemma form for the row [Germanic/docs/DEV_NOTES.md:22067-22085].
- The live row's duplicated imported provenance strings are source bookkeeping, not analysis. They should not be mistaken for a lexeme-specific argument about why `bōsm` was chosen [Germanic/data/germanic-aligned-final.tsv:100-100].

## Open questions for later work

- If a later report wants stronger row-local support, the obvious next step is a dedicated packet or memo for row 1957; at present the best evidence is shared DEV_NOTES class material plus the exact-match debug trace, not a bosom-only note [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:390-408; Germanic/docs/lexeme_reports/coverage_audit.md:205-205].
- If `index.tsv` is reconsidered later, the strongest anchors are probably the current shared fragments `DEV_NOTES:line-29853-29947` and `DEV_NOTES:line-30067-30083`; the row has genuine support, but much of it is class-level rather than individually bespoke.
- If the proto spelling is revisited in a later philological pass, the live TSV and current debug traces should be treated as the present authority: both currently use `*bōsmaz`, not another proto label [Germanic/data/germanic-aligned-final.tsv:100-100; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:390-408].
