---
row_id: 2063
concept: head
counterpart: hēafod
proto: *xáubudą
protoform: *xáubudą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current_no_row_specific_block
needs_literature_agent: no
---

# DEV_NOTES material — 2063 head / hēafod

## Current row state

- Live TSV row: `row_id 2063`, `CONCEPT = head`, `COUNTERPART = hēafod`, `PROTO = *xáubudą`, `PROTOFORM = *xáubudą`, `DERIVATION_CLASS = regular`; the source column is only Wiktionary inheritance metadata, with no row-local explanatory note in the TSV itself [Germanic/data/germanic-aligned-final.tsv:517-517].
- Coverage/report infrastructure: `coverage_audit.md` marks row 2063 as `none`, and the current `report_manifest.tsv` contains only older pilot-format entries, not this row; there is therefore no pre-existing packet, memo, or manifest-linked report to reuse for the slice [Germanic/docs/lexeme_reports/coverage_audit.md:270-270; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- Current derivation snapshot is successful and explicit: `*xáubudą` already yields `hēafod`, with the traced OE-side chain `OE Au Fronting: *xáeubudą` > `OE Diphthong Leveling: *xēabudą` > `OE Med Unstressed U Lowering: *xēabodą` > `OE Velar Fricative Palatalization: *çēabodą` > `OE Heavy Syllable Nasal Apocope: *çēabod` > `PGmc B Allophony: *çēaβod`, orthographic `h*ēaβod`, outcome `hēafod` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2158-2178].
- Basic lexical attestation in repo reference files is straightforward: `old_english_wiktionary.tsv` lists `head	hēafod` [Germanic/data/old_english_wiktionary.tsv:127-127].
- Literature in the repo distinguishes the project’s operational row input from fuller historical reconstruction. Ringe/Taylor says OE `héafod` “clearly reflects a preform *haubud” although PWGmc was “probably *haubid” and PGmc “certainly *haubida,” and elsewhere gives the chain `PGmc *haubida ... > *haubud ... > OE *héabud ... > héafod, héafdes` [docs/references/ringe_taylor_linguistic_history_vol2.txt:14850-14855,15533-15535]. For this row, that means the live `PROTO`/`PROTOFORM` field `*xáubudą` is the project’s current operational FST input, while the literature-facing prehistory is richer and should not be silently collapsed into the same stage label.

## Development-note summary

No dedicated `head / hēafod` DEV_NOTES section survives as a row-specific block. The usable DEV_NOTES support is thin and must be classified carefully: one fragment is **shared-background-only** material on the ordinary OE development of medial unstressed `u > o`, explicitly citing `héafod` as an example; another is **diagnostic** material from a different lexeme note, where `héafod < *xaubudą` is used as the positive control showing that final `*-ą` drops by `OEHeavySyllableNasalApocope` [Germanic/docs/DEV_NOTES.md:267-285,13312-13324].

That surviving material is still enough to support the current row conservatively. The live cascade already derives `hēafod`, so row 2063 is not presently an open exception bucket. But the slice should not pretend that DEV_NOTES preserves a bespoke lexeme dossier here. What survives is: (i) shared support for the medial vowel (`-fo-`, from unstressed `u > o`), and (ii) diagnostic support for the final-vowel loss (`*-ą > 0` in this heavy-syllable environment) [Germanic/docs/DEV_NOTES.md:271-279,13313-13324; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2171-2178].

Because the row’s live metadata keeps `PROTO` and `PROTOFORM` as `*xáubudą`, the slice should also preserve the distinction between the project’s operational input and the comparative historical staging found in literature (`*haubida` > `*haubud` > OE `*héabud` > `héafod`). The attested/target OE form for the row is `hēafod`; the literature’s intermediate preforms are explanatory background, not replacement row metadata [Germanic/data/germanic-aligned-final.tsv:517-517; docs/references/ringe_taylor_linguistic_history_vol2.txt:14850-14855,15533-15535].

## Relevant DEV_NOTES fragments

### DEV_NOTES: medial unstressed `u` note citing `héafod`

- Source heading: `Key source found: Campbell §373`
- Source line hint: `Germanic/docs/DEV_NOTES.md:267-285`
- Fragment type: `shared-background-only`
- Status: `current`
- Issue tags: `medial_unstressed_u_lowering`; `campbell_373`; `ws_examples`; `heafod_as_example`
- Recommended next use: `use for background when explaining why the medial vowel is -o- rather than retained -u-`
- Shared-with rows if relevant: `shared with rows using OE medial unstressed u > o, especially heaven/seven-type comparators`

This fragment is not a row-2063 dossier, but it is the clearest surviving DEV_NOTES support for the row’s medial vowel. DEV_NOTES quotes Campbell §373 directly: “**Unaccented u is preserved in all instances in the early North. short texts... In Ep., however, protected u > o very often... Ordinary OE forms are, however, e.g. héafod head, heofon heaven, tungol star, past indic. pl. -on...**” and then immediately adds the exception statement “**u is always well preserved after accented u** ...” [Germanic/docs/DEV_NOTES.md:271-279]. For row 2063, the important point is narrow: `héafod` is being cited there as an ordinary OE example of the medial unstressed `u > o` outcome, so this is valid **shared background** for the trace step `*xēabudą > *xēabodą`. It does not, by itself, establish anything about target selection, analogical history, or whether the live row’s `*xáubudą` perfectly matches comparative literature staging.

### DEV_NOTES: trisyllable/apocope control using `héafod < *xaubudą`

- Source heading: `Correction after testing`
- Source line hint: `Germanic/docs/DEV_NOTES.md:13312-13324`
- Fragment type: `diagnostic`
- Status: `current`
- Issue tags: `heavy_syllable_nasal_apocope`; `trisyllables`; `heafod_control_case`; `final_a_loss`
- Recommended next use: `use when explaining why final *-ą disappears in the current derivation`
- Shared-with rows if relevant: `shared diagnostically with heaven and similar trisyllabic OE noun checks`

This fragment is diagnostic rather than lexeme-authoritative, but it is row-relevant because it names `head` explicitly as the successful control case. DEV_NOTES says, under “Looking at other trisyllabic examples in OE,” that “**héafod (head) < *xaubudą — the final -ą is lost via OEHeavySyllableNasalApocope (different rule!)**” [Germanic/docs/DEV_NOTES.md:13312-13314]. It then records the actual test result: “**Traced both `xaubudą` (heafod) and `xemonų` (heofon) through the pipeline: `xaubudą → hēafod` ✓ — works because it ends in `*ą`, handled by `OEHeavySyllableNasalApocope`**,” contrasting that with the failure of `heofon` because `*ų` depends on `OEHighVowelApocope` instead [Germanic/docs/DEV_NOTES.md:13316-13324]. For row 2063 this is valuable **diagnostic** material because it confirms the rule type responsible for the final-vowel loss in the live derivation; it is not evidence for a special exception or for revising the row’s current classification.

## Superseded or diagnostic material

- No dedicated row-specific `head / hēafod` DEV_NOTES block survives. That absence should be stated plainly: later writers should not infer a lost lexeme dossier and should not overclaim row-local authority where the live file only preserves shared and diagnostic mentions [Germanic/docs/lexeme_reports/coverage_audit.md:270-270].
- The DEV_NOTES `héafod` material is therefore asymmetrical. The Campbell §373 quotation is **shared-background-only** support for medial `u > o`; the `xaubudą → hēafod` control trace is **diagnostic** support for final `*-ą` loss by heavy-syllable nasal apocope. Neither fragment is a superseded row-specific narrative, and neither should be rewritten as though DEV_NOTES had a bespoke “head” section [Germanic/docs/DEV_NOTES.md:271-279,13312-13324].
- Comparative literature in the repo points to a fuller prehistory (`PGmc *haubida` and/or preform `*haubud`) than the live row metadata encodes [docs/references/ringe_taylor_linguistic_history_vol2.txt:14850-14855,15533-15535]. For this slice that material is best treated as **diagnostic/explanatory**, not as grounds to rewrite the row’s operational `PROTO` or `PROTOFORM` fields, since the current cascade already succeeds with `*xáubudą` [Germanic/data/germanic-aligned-final.tsv:517-517; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2159-2178].
- The lack of any `oe_known_problems.tsv` or manifest entry for row 2063 is consistent with the current derivational state: the row is not presently managed as an exception case, only as a row whose DEV_NOTES support is sparse [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- Should row 2063 eventually expose the comparative staging more explicitly—e.g. distinguishing literature `PGmc *haubida` / preform `*haubud` from the operational row input `*xáubudą`—or is the current TSV abstraction deliberate and sufficient?
- If a packet or memo is later created, should it discuss the likely levelling of `*-ud-` into the singular that Ringe/Taylor invokes for OE `héafod`, or leave that as background literature outside row metadata [docs/references/ringe_taylor_linguistic_history_vol2.txt:14850-14855]?
- If stronger dictionary/report infrastructure is later needed, add a cleaner repo-local lexical citation for simplex `hēafod` beyond the current Wiktionary row, since the present slice relies mainly on derivation traces plus comparative literature rather than a preserved row-specific project memo [Germanic/data/old_english_wiktionary.tsv:127-127].
