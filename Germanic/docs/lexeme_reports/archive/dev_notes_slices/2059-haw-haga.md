---
row_id: 2059
concept: haw
counterpart: haga
proto: *xágô
protoform: *xágô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: ""
linked_research_memo_file: ""
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md
  - Germanic/docs/dossier-shoulder-paradigm-survey-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2059 haw / haga

## Current row state

- Live OE row `2059` currently reads `CONCEPT = haw`, `COUNTERPART = haga`, `PROTO = *xágô`, `PROTOFORM = *xágô`, `DERIVATION_CLASS = regular`; the row carries no exception note, only duplicated Wiktionary inheritance sourcing [Germanic/data/germanic-aligned-final.tsv:501-501].
- `old_english_wiktionary.tsv` likewise gives `haw | haga | inh | template:inh`, so the selected OE counterpart in the aligned TSV is consistent with the repo's lexical source table [Germanic/data/old_english_wiktionary.tsv:123-123].
- `oe_known_problems.tsv` has no entry for `*xágô`, `haga`, or row `2059`; this row is not currently treated as an open OE exception or a documented mismatch bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists row `2059 | haw | haga | regular | no | - | - | - | none`, and `report_manifest.tsv` still contains only the pilot-report rows, so there is no packet, research memo, or report-manifest stub to reuse for this lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:266-266; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The current published derivation trace is an exact match: `PROTO: *xágô`, `EXPECTED: haga`, `OUTPUTS: haga`, with the OE-side chain `Anglo Frisian Brightening: *xægô` → `OE Velar Fricative Palatalization: *çægô` → `OE A Restoration: *çagô` → `OE Unstressed Long Vowel Shortening: *çaga` → orthographic `haga` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2074-2094]. The compact trace duplicates the same path and is useful as a second current-state witness [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md:2436-2456].
- Two non-DEV_NOTES companion files are relevant only as classification/diagnostic background. The trimoraic-vowel dossier lists `*xágô` among the `ô` inputs (“trimoric oral *ō (weak masc. n-stem NSg, etc.)”), and the weak-tail/A-restoration note uses older notation `*xagōn → OE haga` as one of the positive controls showing that this noun type ends in `-a` and triggers restoration [Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67; Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:199-204].

## Development-note summary

No row-specific `DEV_NOTES.md` block for `haw / haga / *xágô` survives. The usable support is therefore **shared-background-only**, not a dedicated lexeme essay: (i) the general A-restoration repair and chronology note, and (ii) the later trimoraic `*ô` analysis explaining why weak masculine n-stem nominatives keep a back trigger long enough to retract `*æ` and then shorten to final `-a` [Germanic/docs/DEV_NOTES.md:1649-1674,3556-3590].

That shared material is sufficient for the current row because the live trace is simple and fully regular. `PROTO` and `PROTOFORM` coincide as `*xágô`; there is no alternate paradigm-cell protoform in play. The derivation currently assumed by the project is: inherited `*a` first fronts under Anglo-Frisian Brightening (`*xægô`), then the fronted vowel is retracted by A-restoration before the back trimoraic suffix (`*çagô`), and only after that does the suffix shorten to `-a`, yielding `haga` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2081-2094; Germanic/docs/DEV_NOTES.md:3558-3590].

So the support profile for this row should be stated plainly: **row-specific DEV_NOTES support: none surviving**; **shared-background current support: yes**; **superseded row-specific material: none identified**; **diagnostic companion material: yes, but only as background and with notation differences (`*xagōn` vs live `*xágô`)** [Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:199-204; Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1649-1674

- Source heading: `A-Restoration Fix (2026-02-06)`
- Source line hint: `lines 1649-1674`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `a_restoration`; `rule_context`; `chronology`; `companion_note`
- Recommended next use: `cite_when_explaining_why_restoration_precedes_final_shortening`
- Shared-with rows if relevant: `1963`; `2059`; `2148`; other trimoraic/back-vowel A-restoration rows

This fragment is not about `haw` specifically, but it is the clearest surviving DEV_NOTES authority for the ordering that row 2059 now relies on. DEV_NOTES says: “Fixed critical foma syntax bug causing A-restoration to apply unconditionally, then implemented chronology fix to move apocope after restoration,” and it identifies the operative consequence: the rule must see the genuine back-vowel context before later tail reduction obscures it [Germanic/docs/DEV_NOTES.md:1649-1663]. DEV_NOTES then explicitly points to `docs/germanic_notes/weak_tail_vowels_and_a_restoration.md` for the broader paradigm and trigger analysis [Germanic/docs/DEV_NOTES.md:1668-1674].

For row 2059, this survives only as shared background, but it remains directly useful. The current haw trace shows exactly the kind of chronology the fragment is protecting: fronting first, restoration while the suffix is still back-vocalic, then later shortening to surface `-a` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2087-2094]. In other words, this fragment does not tell us anything lexeme-unique about `haga`; it tells us why a row of this shape can regularly end up with restored `a` rather than stranded `æ`.

### DEV_NOTES:line-3556-3590

- Source heading: `Where the sources agree` / `Pipeline verification`
- Source line hint: `lines 3556-3590`
- Fragment type: `shared_background_only`
- Status: `current`
- Issue tags: `trimoric_o`; `weak_masc_n_stem`; `a_restoration_trigger`; `late_shortening`
- Recommended next use: `cite_when_documenting_the_suffix_class_of_*xágô`
- Shared-with rows if relevant: `1963`; `2059`; `2148`; other `*ô` rows

This is the strongest current DEV_NOTES material for the row's suffix behavior. DEV_NOTES states, in words worth preserving, “Trimoraic final *-ô → a in OE: All sources agree on the OE outcome. ... Examples: n-stem nom.sg. *namô → nama” [Germanic/docs/DEV_NOTES.md:3558-3560]. It then adds the pipeline statement that matters most for row 2059: “`{*ô}` is defined as a back vowel trigger for A-restoration ... so trimoraic suffixes correctly trigger A-restoration of root `*a` (e.g., `*namô → nama`, not `*næma`)” and “`OEUnstressedLongVowelShortening` handles `{*ô} → {*a}` as a late change ... after AFB and A-restoration” [Germanic/docs/DEV_NOTES.md:3585-3590].

Applied conservatively to row 2059, this is shared-background-only support, but it is enough to justify the live chain `*xágô -> *xægô -> *çagô -> *çaga -> haga` without inventing a special lexeme note. The fragment does not name `haga`, yet it gives the exact class logic the row needs: `*xágô` belongs to the trimoraic `*ô` noun type, that suffix still counts as a back trigger during restoration, and its later shortening to `-a` is expected rather than exceptional [Germanic/docs/DEV_NOTES.md:3578-3590; Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67].

## Superseded or diagnostic material

- No dedicated `DEV_NOTES.md` discussion of row `2059` has been located, so there is no surviving row-specific block to mark as superseded. The slice therefore has to be built from shared current material plus present trace state, not from a lost lexeme essay [Germanic/docs/DEV_NOTES.md:1649-1674,3556-3590].
- The companion note `weak_tail_vowels_and_a_restoration.md` is useful but only diagnostic/background. Its example uses older notation `*xagōn → OE haga`, whereas the live OE row uses `PROTO = PROTOFORM = *xágô`; the point that survives is the class behavior (`-ōn/-ô` noun yielding OE `-a` with restoration), not a proposal to rewrite the live row's protoform spelling [Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:199-204; Germanic/data/germanic-aligned-final.tsv:501-501].
- Nearby DEV_NOTES mentions of `*haw-ja-` / `*haw(w)ja-` are **not** evidence for row 2059. Those passages belong to the `*aw + j` research cluster for `hay`/`hīeġ` and related `-g-` outcomes, not to simple noun `*xágô -> haga` [Germanic/docs/DEV_NOTES.md:26979-26993,27184-27218]. They should be treated as false friends created by English gloss overlap (`haw` vs `hay`), not as row-relevant lexeme notes.
- The dossier entry listing `*xágô` under trimoraic `ô` is classificatory only. It is good support for row typing, but it is not a derivational argument by itself and should not be cited as if it replaced the DEV_NOTES chronology or the live trace [Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2081-2094].

## Open questions for later work

- If a later indexing pass asks whether row 2059 deserves a DEV_NOTES index entry, the honest answer is probably no unless the project starts indexing short shared-rule notes. At present the row is regular, matched, and documented only through shared A-restoration / trimoraic-suffix material rather than a dedicated haw essay [Germanic/docs/lexeme_reports/coverage_audit.md:266-266; Germanic/docs/DEV_NOTES.md:1649-1674,3556-3590].
- If future literature work turns up a lexeme-specific handbook discussion of OE `haga`, that evidence could replace this background-built slice. Until then, later writers should keep the present distinction explicit: no row-specific DEV_NOTES block survives, but the regular derivation is still well supported by shared current notes plus the live trace [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2074-2094].
- If notation is revisited, do not silently collapse older diagnostic spellings like `*xagōn` into a claim that the live row is wrong. The current project state intentionally uses `PROTO = PROTOFORM = *xágô`; any future change would need explicit argument about mora marking and stem encoding, not just citation of an older companion note [Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md:199-204; Germanic/docs/dossier-shoulder-paradigm-survey-2026.md:63-67; Germanic/data/germanic-aligned-final.tsv:501-501].
