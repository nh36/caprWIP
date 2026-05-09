---
row_id: 2301
concept: word
counterpart: word
proto: "*wúrdą"
protoform: "*wúrdą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2301 word / word

## Current row state

- The live OE row is `2301`, `CONCEPT = word`, `COUNTERPART = word`, `PROTO = *wúrdą`, `PROTOFORM = *wúrdą`, `DERIVATION_CLASS = regular`. There is no live row-level split between PROTO and PROTOFORM; both still point to the singular neuter input, while `word` is the attested OE citation form [Germanic/data/germanic-aligned-final.tsv:1440-1440].
- The published derivation trace is an exact match and shows the active regular path now in force: `Proto Input: *wúrdą`, `NWGmc U Lowering: *wórdą`, `OE Heavy Syllable Nasal Apocope: *wórd`, `Outcome: word` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6045-6063; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.txt:34525-34595].
- Shared workflow background aligns with that trace. The apocope investigation note states for strong neuter a-stems that heavy stems take zero in the nominative/accusative singular, with the paradigm `word / word / wordes / worde / wordum`, and it glosses the proto-side rule as `Proto neuter *-ą ... Zero after heavy syllables` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:70-105].
- Coverage infrastructure treats the row as ordinary rather than exception-driven: the coverage audit lists row `2301 | word | word | regular | no | - | - | - | none`, which is consistent with a regular row lacking a dedicated packet/report trail at present [Germanic/docs/lexeme_reports/coverage_audit.md:419-419].

## Development-note summary

No row-specific DEV_NOTES block survives for row 2301. The usable DEV_NOTES material is therefore conservative and mostly shared-background-only. What survives is still enough to replace a trip back into DEV_NOTES for this row: (1) DEV_NOTES repeatedly uses `word : worde` as the model regular neuter a-stem paradigm, which preserves genuine OE paradigm substance for this lexeme even though the note occurs inside the `fire / fȳre` discussion; and (2) DEV_NOTES preserves both archived and later-general statements of the heavy-syllable apocope logic that now drives the row's exact trace [Germanic/docs/DEV_NOTES.md:6237-6240; Germanic/docs/DEV_NOTES.md:6291-6327; Germanic/docs/DEV_NOTES.md:1591-1620; Germanic/docs/DEV_NOTES.md:28984-29140].

For row 2301 specifically, the safe reading is: the live singular input remains `PROTO = PROTOFORM = *wúrdą`; the active cascade lowers stressed NWGmc `*u` to `*o` before the non-high ending, then deletes final nasal vowel after the heavy stem, yielding OE `word`; and the only directly preserved DEV_NOTES paradigm expansion around the row is the attested OE dative comparator `worde`, not an alternative row target and not a rival proto input [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6045-6063; Germanic/docs/DEV_NOTES.md:6237-6240; Germanic/docs/DEV_NOTES.md:6301-6327].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6237-6240-and-6291-6327

- Source heading: `Update: Four-part analogical model for dative -e restoration (2026-03-10)`
- Source line hint: `6237-6240; 6291-6327`
- Fragment type: `shared paradigm background preserving row substance`
- Status: `shared-background-only`
- Issue tags: `word:worde`; `neuter_a-stem`; `dative_comparator`; `PROTO_vs_attested_paradigm`
- Recommended next use: `cite when the row needs its OE paradigm distinction stated without changing the live target`
- Shared-with rows if relevant: `2013 fire / fȳre`

This is the single most useful surviving DEV_NOTES material for row 2301 because it preserves real lexical substance even though it is not a row-2301 dossier. DEV_NOTES says that the `fire` dative could be restored by analogy with regular neuter a-stem datives, explicitly giving `word` as the model: `dat.sg. ending -e could have been restored by analogy with regular a-stem datives (e.g. word : worde)` [Germanic/docs/DEV_NOTES.md:6237-6240]. It then preserves the analogy itself in table form:

`word:  word   :  worde   = (regular a-stem, -e preserved throughout)`
`fȳr:   fȳr    :  X       → X = fȳre (by proportion)` [Germanic/docs/DEV_NOTES.md:6301-6306].

DEV_NOTES continues with the explicit prose generalization: `Regular neuter a-stems like word have a clear nom.sg. : dat.sg. distinction (word : worde). Native speakers expect this pattern` [Germanic/docs/DEV_NOTES.md:6321-6323]. For row 2301 this fragment should be treated as shared-background-only, not as a correction note. Its value is that it preserves the row's OE paradigm distinction inside DEV_NOTES itself: the live row target is the nominative/accusative citation form `word`, while `worde` survives as the dative comparator. That distinction matters because it keeps PROTO/PROTOFORM (`*wúrdą`) separate from non-headword inflected OE material without inventing a new row-local proto cell [Germanic/docs/DEV_NOTES.md:6237-6240; Germanic/docs/DEV_NOTES.md:6301-6327].

### DEV_NOTES:line-1591-1620

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `1591-1620`
- Fragment type: `rule-history`
- Status: `superseded_or_diagnostic`
- Issue tags: `heavy_syllable_nasal_apocope`; `*-ą loss`; `implementation_history`
- Recommended next use: `use only when explaining why the current trace contains OE Heavy Syllable Nasal Apocope`
- Shared-with rows if relevant: `broadly shared across heavy-stem rows`

This fragment is not row-specific, but it is the clearest surviving DEV_NOTES statement of how the project came to treat forms like `*wúrdą` as losing final nasal vowel after a heavy stem. DEV_NOTES records the 2026-02-06 discovery as follows: `Implemented experimental rule deleting proto *-ą after heavy syllables`, then glosses the literature background with `Ringe/Taylor §6.8.1: "short *i and *u were lost word-finally after a heavy syllable"` and `Hogg §3.3.2: Neuter strong nouns show zero ending after heavy stems, -u after light stems` [Germanic/docs/DEV_NOTES.md:1591-1607]. The crucial modeling conclusion is also preserved verbatim: `The same heavy/light conditioning that applied to *-i/*-u also applied to *-ą` [Germanic/docs/DEV_NOTES.md:1609-1612].

For row 2301, this is diagnostic history rather than a live row note. It explains why the modern trace legitimately contains `OE Heavy Syllable Nasal Apocope: *wórd` after NWGmc lowering, but it should not be mistaken for an unresolved problem or a row-local controversy. The current row no longer sits in a mismatch bucket; the archived note is useful only because it preserves the reasoning behind the rule that now regularizes `*wúrdą -> word` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6054-6058; Germanic/docs/DEV_NOTES.md:1591-1620].

### DEV_NOTES:line-28984-29140

- Source heading: `§17.16.15 Option D revised (lautgesetzlich justification)` / `§17.17.2 Affected forms (all should retain -u)`
- Source line hint: `28984-29140`
- Fragment type: `shared rule statement with paradigm control`
- Status: `shared-background-only`
- Issue tags: `phonological_not_morphological`; `heavy_vs_light`; `wordu_control`; `paradigm_guardrail`
- Recommended next use: `cite when distinguishing the row's singular *wúrdą from plural/control forms like *wordu`
- Shared-with rows if relevant: `rows affected by final high-vowel apocope and heavy/light conditioning`

This later DEV_NOTES material is shared-background-only, but it is the most explicit current statement that the apocope pattern relevant to `word` is phonological rather than a special lexical trick. DEV_NOTES says: `This rule is purely phonological: it refers to syllable weight (a property of the stem), never to stem-class or grammatical number`, and immediately gives the `word` paradigm as the heavy-stem control: `neut. NPl: *skipu → sċipu (retained) vs *wordu → word (lost)` [Germanic/docs/DEV_NOTES.md:28984-28990]. It then warns that this should not be reinterpreted as a morphological workaround: `It is not a case where we want to encode a morphological distinction (plural vs singular)` [Germanic/docs/DEV_NOTES.md:28992-28996].

The control table later repeats the point in concrete probe form: `*wordu | word | word ✓` [Germanic/docs/DEV_NOTES.md:29123-29140]. For row 2301 that matters in two ways. First, it confirms that the project treats heavy-stem final-vowel loss around `word` as regular shared phonology. Second, it is a guardrail against confusion: `*wordu` in these lines is not a rival PROTOFORM for row 2301, but a separate paradigm/control form used to test final high-vowel apocope. The live row remains singular `*wúrdą -> word`; the plural/control material only helps explain the broader paradigm behavior around it [Germanic/data/germanic-aligned-final.tsv:1440-1440; Germanic/docs/DEV_NOTES.md:28984-29140].

## Superseded or diagnostic material

- No securely row-specific DEV_NOTES block survives for `2301 word / word`, and no surviving DEV_NOTES fragment suggests a superseded row-local `COUNTERPART`, substitute `PROTOFORM`, or exception-classification workflow. The row should therefore be treated as conservative-current, not as a hidden repair case [Germanic/data/germanic-aligned-final.tsv:1440-1440; Germanic/docs/lexeme_reports/coverage_audit.md:419-419].
- The 2026-02-06 `Archived: Heavy Syllable Nasal Apocope` section is still worth preserving, but only as diagnostic rule history. It records how the project generalized heavy/light apocope to `*-ą`; it does not signal that row 2301 remains disputed today [Germanic/docs/DEV_NOTES.md:1591-1620].
- The `*wordu -> word` passages in later DEV_NOTES are likewise diagnostic/shared rather than row-local. They belong to a plural/control discussion and should not be promoted into the row metadata as if `PROTOFORM` needed changing from singular `*wúrdą` to plural `*wordu` [Germanic/docs/DEV_NOTES.md:28984-29140].

## Open questions for later work

- If row 2301 ever receives a full packet or memo, decide whether to index any DEV_NOTES fragment at all or simply link shared apocope/paradigm background. The strongest candidate fragments are the `word : worde` analogy block and the heavy-syllable-apocope rule history, but neither is a dedicated row dossier [Germanic/docs/DEV_NOTES.md:6237-6240; Germanic/docs/DEV_NOTES.md:1591-1620].
- If later documentation needs a fuller OE paradigm note, keep the distinctions explicit: live row `PROTO = PROTOFORM = *wúrdą`; live OE headword/counterpart `word`; shared attested inflectional comparators `worde`, `wordes`, `wordum`. Do not collapse those into one another [Germanic/data/germanic-aligned-final.tsv:1440-1440; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:78-105].
- If future literature cleanup wants a stricter external anchor, the missing piece is not a new derivational fix but a direct grammar citation for the `word` paradigm itself. The current row already traces exactly and needs no literature agent for resolution, only possibly for enrichment [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:6045-6063].
