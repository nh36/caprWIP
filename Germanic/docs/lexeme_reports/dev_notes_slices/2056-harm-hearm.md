---
row_id: 2056
concept: harm
counterpart: hearm
proto: "*xármaz"
protoform: "*xármaz"
derivation_class: regular
source_file: Germanic/data/germanic-aligned-final.tsv
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
  - Germanic/docs/germanic_notes/analogical_leveling_analysis.md
current_status: "No surviving row-specific DEV_NOTES block; shared breaking background survives. Published trace reaches hearm, but current sandbox snapshots regress after ProtoRhoticFronting/PostVocalicRLoss."
needs_literature_agent: true
---

# DEV_NOTES material — 2056 harm / hearm

## Current row state

Row 2056 is the Old English entry for concept **harm**, with target/counterpart **hearm**, PROTO and PROTOFORM both **`*xármaz`**, and derivation class **regular**; the live TSV gives no row-specific explanatory note beyond generic Wiktionary etymology sourcing. The OE source table likewise pairs Modern English **harm** with inherited OE **hearm**. [Germanic/data/germanic-aligned-final.tsv:488-489] [Germanic/data/old_english_wiktionary.tsv:120-120]

Coverage status is currently blank for row-specific documentation: the lexeme-report coverage audit marks row 2056 as having **no** report/slice and `none` under notes, and `*xármaz` does **not** appear in `oe_known_problems.tsv`, so the row is not presently treated as a known exception bucket. [Germanic/docs/lexeme_reports/coverage_audit.md:265-265] [Germanic/data/oe_known_problems.tsv:1-8]

Current derivation/debug state is split. A published derivation snapshot shows the expected regular pathway: `*xármaz` > final `-z` loss `*xárma` > bare final `a` loss `*xárm` > Anglo-Frisian brightening `*xærm` > OE breaking `*xearm` > velar-fricative palatalization `*çearm` > orthographic **hearm**. [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2032-2052] By contrast, the current sandbox JSON uses normalized proto **`*xarmăz`** (note: this is a debugging/procedural normalization, not the live TSV PROTOFORM), gives no final outputs, flags `ProtoRhoticFronting` as the first failing stage, and then shows a clearly bad downstream path in which `PostVocalicRLoss` removes the `r`, producing `*xæm*a`, then `hæ`, with fallback surface `harma`. Treat that sandbox state as diagnostic regression evidence, not as the row’s intended historical analysis. [Germanic/tmp/old_english_sandbox_results_current.json:1139-1143] [Germanic/tmp/old_english_sandbox_results_with_stages.json:17744-17883]

## Development-note summary

No dedicated `harm/hearm` discussion block survives in `DEV_NOTES.md`. The only explicit surviving mention of **`*xármaz`** there is a shared side-effects note classing it among **breaking-conditioned rows** and stating that those rows were **unaffected** by an A-restoration fix because breaking bleeds restoration. That is the nearest thing to row-specific DEV_NOTES residue. [Germanic/docs/DEV_NOTES.md:36612-36629]

Accordingly, the conservative row reading is: this lexeme belongs to the ordinary OE **breaking** pathway, not to a special exception class and not to an A-restoration repair bucket. The relevant shared DEV_NOTES material says breaking was implemented/reordered so that `*a/*æ → *ea` in `rC/lC/h/w` environments, and it separately warns that breaking/retraction before `h`, `rC`, `lC` was dialect-conditioned and not uniform across OE. [Germanic/docs/DEV_NOTES.md:2439-2445] [Germanic/docs/DEV_NOTES.md:2575-2579]

Later supporting analysis outside `DEV_NOTES.md` is consistent with that reading. The A-restoration research docket simply lists row 2056 `*xármaz → hearm` as **breaking**. [Germanic/docs/analysis/arestoration_r_l_research.md:722-745] A dialect note quoting Campbell §144 is also relevant: “**æ was broken, and appears as ea with very great regularity, before r followed by a consonant. Retraction to a is practically limited to North.**” The same passage’s Northumbrian examples include **`harm`**, while Mercian/WS comparanda show broken forms such as **`wearm`**. That supports treating **hearm** as the default broken target here while keeping plain **harm** as dialectal background, not as a reason to rewrite the row. [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:236-247]

## Relevant DEV_NOTES fragments

### Fragment 1 — OE breaking reorder + diagnostics

- **Source heading:** `### OE breaking reorder + diagnostics (2025-12-22)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:2575-2579`
- **Fragment type:** shared-background-only
- **Status:** still relevant
- **Issue tags:** `breaking`, `chronology`, `rC`, `shared-rule`
- **Recommended next use:** use as the default phonological pathway for this row unless stronger row-specific attestation evidence overrides it
- **Shared-with rows:** other `rC/lC` breaking rows, including 2057 `*xárbistuz`, 2077 `*xáldaną`, 2120 `*márkō`, 2269 `*wárpą`, 2271 `*wártōn`

The surviving note says: “**Breaking now precedes GH-marking and W-glide so the conditioning consonants are still visible when OE breaking applies**,” and that the “**sandbox breaking rules [are] aligned to OE (`*a/*æ → *ea`, `*e → *eo`, `*i → *ie` in `rC/lC/h/w` contexts)**.” [Germanic/docs/DEV_NOTES.md:2575-2579] For row 2056, this is the core shared derivational substance: after brightening to `*xærm`, the `rC` cluster should feed OE breaking to `*xearm`, after which ordinary OE orthography yields **hearm**. There is no surviving DEV_NOTES evidence that this row needed any bespoke workaround beyond that shared chronology.

### Fragment 2 — PGmc→OE chronology audit

- **Source heading:** `### PGmc→OE chronology audit (2025-12-21)`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:2439-2445`
- **Fragment type:** shared-background-only
- **Status:** still relevant but broad
- **Issue tags:** `breaking`, `dialect`, `retraction`
- **Recommended next use:** use to frame dialectal plain-`harm` evidence as background variation, not immediate row correction
- **Shared-with rows:** essentially all OE breaking/retraction rows

The chronology audit condenses the standard caution as follows: “**Breaking/retraction of front vowels before h, rC, lC (and some w contexts) is dialect-conditioned and not uniform across OE.**” [Germanic/docs/DEV_NOTES.md:2441-2441] For this row, that means the broken outcome **hearm** is still the default dataset target, but unbroken **harm** should not be treated as impossible noise; it is compatible with the broader dialectal warning later made explicit in the Campbell-derived analysis note. This fragment is therefore shared background, not row-specific instruction.

### Fragment 3 — §17.25.5 Predicted side-effects

- **Source heading:** `### §17.25.5 Predicted side-effects`
- **Source line hint:** `Germanic/docs/DEV_NOTES.md:36612-36629`
- **Fragment type:** shared-background-only with row-name mention
- **Status:** still relevant; nearest surviving row mention
- **Issue tags:** `a-restoration`, `breaking`, `regression-scope`
- **Recommended next use:** treat row 2056 as outside the A-restoration problem set
- **Shared-with rows:** the 21 “breaking-conditioned rows” named as a class

This is the only place in `DEV_NOTES.md` where `*xármaz` is named directly. After listing side-effects for an A-restoration fix, the note says: “**For breaking-conditioned rows (`*xármaz, *márkō, *kálbaz, *fállaną` etc., 21 rows total), A-restoration is bled by breaking; unaffected.**” [Germanic/docs/DEV_NOTES.md:36628-36629] That is important because it sharply limits what kind of surviving support exists for this row: the row is not being singled out as problematic in its own right; instead, it is being used as an example of the opposite category, namely rows whose expected output is already accounted for by breaking and therefore should not move when restoration logic is changed elsewhere.

## Superseded or diagnostic material

An exploratory analogical-leveling note once listed `*xarmăz → hearm` as a **candidate** that “**Could use dat.pl. `*xarmum`**.” [Germanic/docs/germanic_notes/analogical_leveling_analysis.md:157-164] For slicing purposes this is **superseded/exploratory**, not live row guidance: the later DEV_NOTES residue explicitly reclassifies `*xármaz` as a **breaking-conditioned** row that is unaffected by A-restoration work. [Germanic/docs/DEV_NOTES.md:36612-36629]

The published derivation trace yielding clean **hearm** is useful only as a control snapshot for intended behavior, while the current sandbox `[]` / `hæ` / `harma` outputs are useful only as diagnostics of a present implementation regression around rhotic handling and/or postvocalic `r` loss. Neither debug state should be mistaken for additional philological evidence beyond the shared breaking pathway already summarized above. [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2032-2052] [Germanic/tmp/old_english_sandbox_results_current.json:1139-1143] [Germanic/tmp/old_english_sandbox_results_with_stages.json:17744-17883]

The Campbell-derived dialect note that includes Northumbrian **harm** is likewise diagnostic/background rather than a mandate to change the row target: it explains why unbroken forms can exist in the record, but it does not overturn the current row’s WS-style target **hearm**. [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:236-247]

## Open questions for later work

1. If this row later gets a fuller packet, should it explicitly record the dialect split between broken **hearm** and Northumbrian **harm**, rather than leaving the dialect issue implicit? Current support for that split is in later analysis, not in a dedicated DEV_NOTES row block. [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:236-247]
2. When the current sandbox regression is repaired, confirm exactly why normalized `*xarmăz` first fails at `ProtoRhoticFronting` and why later logs still show catastrophic `r` loss (`*xæm*a`, `hæ`, `harma`) even though the published trace preserves the intended `*xearm > hearm` path. [Germanic/tmp/old_english_sandbox_results_with_stages.json:17744-17883] [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2032-2052]
3. No surviving row-specific DEV_NOTES block currently preserves attestation detail beyond generic inheritance sourcing. A later literature pass could firm up whether the slice should quote an OE dictionary or edition directly for **hearm** and/or note dialectal **harm** more explicitly. [Germanic/data/germanic-aligned-final.tsv:488-489] [Germanic/data/old_english_wiktionary.tsv:120-120]
