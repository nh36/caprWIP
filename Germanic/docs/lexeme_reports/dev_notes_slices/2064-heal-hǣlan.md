---
row_id: 2064
concept: heal
counterpart: hǣlan
proto: *xáilijaną
protoform: *xáilijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2064 heal / hǣlan

## Current row state

- Live row `2064` currently reads `heal / hǣlan / *xáilijaną / regular`; `PROTO` and `PROTOFORM` coincide, the row carries no live `NOTE`, and the row-local source strings are only duplicated Wiktionary inheritance provenance [Germanic/data/germanic-aligned-final.tsv:519-521].
- Coverage status is explicitly non-escalated: `| 2064 | heal | hǣlan | regular | no | - | - | - | none |`. So this slice is being created even though the normal coverage workflow did **not** require a packet or manifest-backed report for the row [Germanic/docs/lexeme_reports/coverage_audit.md:271-271].
- `oe_known_problems.tsv` has no entry for `2064`, `hǣlan`, or `*xáilijaną`; the current OE exception list remains limited to unrelated rows such as `*búkkaz`, `*fūri`, and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` still contains only the pilot subset and does not include row `2064`; there is therefore no linked pilot report to inherit wording from [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- Repo-local lexical support for the OE target is straightforward but thin: `old_english_wiktionary.tsv` has `heal -> hǣlan` [Germanic/data/old_english_wiktionary.tsv:128-128].
- Current derivation snapshots are clean and exact. The compact/published OE trace records `PROTO: *xáilijaną`, `EXPECTED: hǣlan`, `OUTPUTS: hǣlan`, with the effective chain `PWGmc Ai Monophthongization: *xālijaną` > `OE Heavy Syllable Nasal Apocope: *xālijan` > `OE Secondary Nasalization: *xālijąn` > `Sievers Law Syncope: *xāljąn` > `OE I Umlaut: *xǣljąn` > `OE Weak Tail Reduction: *xǣljan` > `OE J Loss After Heavy: *xǣlan` > orthographic `h*ǣlan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2180-2199; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2404-2423].
- The full trace confirms that this is a regular derivation, not a hidden rescue: virtually all earlier OE and NWGmc rules are `[no-change]` until the heavy-weak-verb sequence just listed, and the derivation finishes with `OldEnglishSurface: hǣlan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14388-14501].

## Development-note summary

No dedicated row-specific prose dossier for `2064 heal / hǣlan` survives in `DEV_NOTES.md`. The surviving support is instead a conservative bundle of (a) shared Sievers'-Law implementation notes that explicitly include this lexeme, (b) a row-explicit source-attestation table entry quoting Ringe-Taylor's `*hailijană 'to heal, to cure'`, and (c) a later regression probe that uses `xáilijaną` as a negative control for a different `*j` rule [Germanic/docs/DEV_NOTES.md:8903-9044; Germanic/docs/DEV_NOTES.md:27358-27438].

That surviving material is enough to state the row's working position precisely. `PROTO` and `PROTOFORM` are both the current project input `*xáilijaną`; there is no evidence here for a paradigm-cell substitution or a split between comparative proto and OE-directed protoform. The lexeme is treated as a **heavy-stem Class I weak verb** with root `xail-` / `xāl-`, so the relevant inherited weak-verb notation is `-ij-`, not bare `-j-`, and the live OE cascade reaches `hǣlan` through ordinary heavy-verb syncope, i-umlaut, weak-tail reduction, and post-heavy `j` loss [Germanic/docs/DEV_NOTES.md:8911-8913; Germanic/docs/DEV_NOTES.md:8984-9018; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14450-14501].

The main caution is documentary rather than phonological. Because no row-specific DEV_NOTES essay survives, later use should label the support correctly: the strongest material is **shared-background-only but lexeme-explicit**, not a bespoke `hǣlan` problem note. Nothing in the checked files suggests that row `2064` is exceptional, analogical, reconstructed-OE-only, or presently unstable. The surviving DEV_NOTES evidence instead says the opposite: this is one of the verbs that motivated the heavy-stem `*-ijăną` cleanup, and the current trace still derives the OE target exactly [Germanic/docs/DEV_NOTES.md:8903-9044; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2180-2199].

## Relevant DEV_NOTES fragments

### DEV_NOTES:8903-8937

- Source heading: `Sievers' Law Implementation Status (2026-03-13)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8903-8937`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current substance; older literal notation`
- Issue tags: `sievers_law`; `heavy_class_i_weak_verb`; `protoform_cleanup`; `old_vs_new_notation`
- Recommended next use: `cite when explaining why the row uses heavy-verb *-ij- and not bare *-j-`
- Shared-with rows if relevant: `1961`; `2093`; `2102`; other heavy Class I weak verbs updated in the same sweep

This is the clearest surviving record of the row's protoform cleanup. DEV_NOTES says the grammar change added a `*-ijăną` pattern and a `SieversLawSyncope` rule, and that the TSV was updated so that it now `Updated ALL heavy-stem Class I weak verbs to use *-ijăną notation` [Germanic/docs/DEV_NOTES.md:8907-8913]. Row `2064` is named directly in the update table as ``*xailjăną`` → ``*xailijăną`` [Germanic/docs/DEV_NOTES.md:8915-8937]. The literal string there is older than the current acute-marked row spelling `*xáilijaną`, but the substantive point is still current: the row should be documented as a heavy weak verb with inherited `-ij-`, not as a light-stem `-j-` form [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:519-521; Germanic/data/germanic-aligned-final.tsv:519-521].

For this row, that update history is row-relevant rather than merely ambient background, because it explains why the present `PROTO`/`PROTOFORM` field already has the right shape without needing any further rescue. The current full trace confirms DEV_NOTES' rationale line `The SieversLawSyncope rule correctly handles them anyway`: after heavy-syllable nasal apocope and secondary nasalization, the rule deletes the pre-`j` vowel (`*xālijąn` > `*xāljąn`), exactly the behavior the March cleanup was meant to formalize [Germanic/docs/DEV_NOTES.md:9040-9044; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14450-14458].

### DEV_NOTES:8954-9018

- Source heading: `Source Attestation of *-ijăną Forms (2026-03-13)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:8954-9018`
- Fragment type: `lexeme_explicit_shared_support`
- Status: `current`
- Issue tags: `ringe_taylor`; `attestation`; `stem_weight`; `sievers_law`
- Recommended next use: `cite as the strongest surviving philological support for the row's current protoform`
- Shared-with rows if relevant: `1961`; `2027`; `2093`; `2102`; other heavy Class I weak verbs cited in the same source table

This is the strongest surviving DEV_NOTES fragment for row `2064`. In the Ringe-Taylor evidence table, DEV_NOTES preserves the exact lexeme line ``*xailijăną`` | ``*hailijană`` | `hǣlan` | `p.234: "PGmc *hailijană 'to heal, to cure'"` [Germanic/docs/DEV_NOTES.md:8972-8985]. Immediately below, DEV_NOTES states the governing criterion in general form: `A heavy-stem Class I weak verb should have -ijăną (Sievers' Law)`, and it classifies ``*xailijăną`` as root `xail- (CVVC) | heavy | R/T p.234` [Germanic/docs/DEV_NOTES.md:8989-9018]. That is the key surviving substantive note for this row.

Its evidential status should be described carefully. This is not a bespoke `hǣlan` dossier discussing attestation problems or competing OE outcomes; it is shared-background-only in format. But it is also lexeme-explicit, and for row `2064` it does real work: it preserves the exact primary-source quotation backing the heavy `-ijan-` analysis and identifies the stem-weight reason that the row now carries `*xáilijaną` in both proto columns [Germanic/docs/DEV_NOTES.md:8984-9018]. Combined with the live OE trace `*xālijąn > *xāljąn > *xǣljąn > *xǣljan > *xǣlan`, it supports the present working note that `hǣlan` is the regular OE outcome of the heavy weak verb, not a repaired exception [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2190-2199].

### DEV_NOTES:27358-27438

- Source heading: `§17.10.36-q3-probes — REGRESSION PROBES (2026-04-23)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:27358-27438`
- Fragment type: `diagnostic_shared_background`
- Status: `current diagnostic`
- Issue tags: `regression_probe`; `oejstrengthening`; `post_i_umlaut`; `negative_scope`
- Recommended next use: `cite only when explaining which later *j-related rule changes do NOT affect this row`
- Shared-with rows if relevant: `509`; `1153`; all 43 `*j`-bearing OE forms sampled in the probe

This fragment is diagnostic, but it is worth preserving because it records a later non-effect on the row. DEV_NOTES ran a corpus-wide regression probe for a proposed `OEJStrengtheningAfterFrontDiphthong` rule and sampled `xáilijaną` explicitly at the post-i-umlaut stage: `xáilijaną    → *x*ǣ*l*j*ą*n      (long V + C + *j, not diphthong + *j → rule does NOT fire ✓)` [Germanic/docs/DEV_NOTES.md:27417-27426]. DEV_NOTES then generalizes that `All 43 *j-bearing forms examined do not match the proposed rule's trigger pattern except the two target forms in Probe 2a` [Germanic/docs/DEV_NOTES.md:27437-27438].

For row `2064`, this is not primary derivational support; it is **diagnostic scope control**. The point is that later `*j`-handling work did not reopen `hǣlan` as a problem case. At the relevant stage the row has long `ǣ` plus consonant plus `j`, not front diphthong plus `j`, so it remains outside that rule's intervention zone and continues down the ordinary `OE Weak Tail Reduction` + `OE J Loss After Heavy` path seen in the live trace [Germanic/docs/DEV_NOTES.md:27424-27426; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14458-14501].

## Superseded or diagnostic material

- The older row spelling `*xailjăną` is superseded as live metadata. It survives in the backup TSV and in the March DEV_NOTES update table only as project history for the Sievers'-Law cleanup; the current row-level working form is `*xáilijaną`, with the substantive change being `-j-` → `-ij-`, not a new etymology [Germanic/data/germanic-aligned-final.tsv.backup-2026-02-06:519-521; Germanic/docs/DEV_NOTES.md:8915-8937; Germanic/data/germanic-aligned-final.tsv:519-521].
- The Modern English sandbox material for concept `heal` is diagnostic only for a different workflow. It uses English-side proto `*xailjaną` and outputs modern reflex candidates such as `hēl` and `hīl`; that should **not** be imported into the OE row note as if it were direct support for `hǣlan`, because it tracks another doculect and an older protoform spelling [Germanic/tmp/english_sandbox_results_current.json:1197-1205; Germanic/tmp/english_sandbox_results_with_stages.json:13380-13479].
- No row-specific mismatch bucket or exception note survives. The absence of a `oe_known_problems.tsv` entry, together with the exact-match OE traces, means the row should not be described as unresolved, “papered over,” or pending an analogy/paradigm-cell fix [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:2404-2423].

## Open questions for later work

- If later slice cleanup standardizes older DEV_NOTES notation, decide whether lexeme-explicit quotations like ``*xailijăną`` should be silently normalized to live `*xáilijaną` in prose or always reproduced verbatim and then glossed as older project spelling.
- If a packet/memo workflow is eventually created for row `2064`, keep the evidential hierarchy explicit: the row currently rests on exact live derivation traces plus shared-but-lexeme-explicit Sievers'-Law DEV_NOTES material, not on a dedicated `hǣlan` dossier [Germanic/docs/DEV_NOTES.md:8954-9018; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:14388-14501].
- Additional lexicographic enrichment is optional rather than urgent. The checked repo evidence already supports `hǣlan` and the row is derivationally stable, so no literature-agent escalation is needed now; any future literature pass should be for denser attestation texture, not for repairing the derivation [Germanic/data/old_english_wiktionary.tsv:128-128; Germanic/docs/lexeme_reports/coverage_audit.md:271-271].
