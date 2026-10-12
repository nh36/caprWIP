---
row_id: 1999
concept: earth
counterpart: eorþe
proto: *érθōn
protoform: *érθōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1999 earth / eorþe

## Current row state

- The live TSV row is `ID 1999`, `CONCEPT earth`, `COUNTERPART eorþe`, `PROTO *érθōn`, `PROTOFORM *érθōn`, `DERIVATION_CLASS regular`. `PROTO` and `PROTOFORM` are identical here; there is no separate OE-facing repair input stored for the row [Germanic/data/germanic-aligned-final.tsv:266-266].
- `coverage_audit.md` still marks the row as uncovered background material — `| 1999 | earth | eorþe | regular | no | - | - | - | none |` — and `report_manifest.tsv` still contains only the small pilot set, with no row-1999 entry. No packet or research memo is presently linked for this lexeme [Germanic/docs/lexeme_reports/coverage_audit.md:230-230; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- `oe_known_problems.tsv` has no surviving entry for row `1999`, for `earth`, for `eorþe`, or for `*érθōn`, so the row is not currently being tracked as a live OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation is already exact. The compact trace gives `PROTO: *érθōn`, `EXPECTED: eorþe`, `OUTPUTS: eorþe`, with the visible path `*érθōn > *érθǭ > *éorθǭ > *éorθæ > *éorθe > eorþe` via Northwest Germanic n-stem `n` loss, OE breaking, unstressed long-vowel shortening, and unstressed `æ > e` merger [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1057-1077; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7079-7168].

## Development-note summary

DEV_NOTES support for row 1999 is real but thin and mostly shared rather than row-local. No dedicated `earth / eorþe` dossier survives. The strongest directly row-relevant material is the 2026 research note on two-stage shortening of unstressed `*ō`, because that note explicitly records a regression `*érθōn → eorþæ` and then uses weak-noun `*-ōn > -e` outcomes, including `eorþe`, as the key evidence for why that regression was wrong [Germanic/docs/DEV_NOTES.md:20467-20558].

That material matters because it distinguishes several things that should not be collapsed. The live row's stored proto input is `*érθōn`; the attested OE counterpart is `eorþe`; the temporary bad output was `eorþæ`; and the DEV_NOTES argument is not “change the lexical target,” but “respect the chronology of unstressed-vowel shortening so weak noun endings in `*-ōn` still land in `-e`” [Germanic/docs/DEV_NOTES.md:20469-20518]. In other words, the main surviving DEV_NOTES attachment is about class behaviour and rule ordering, not about a disputed OE lexeme identity.

The only other explicit `earth` mention in DEV_NOTES is downstream and shared: the paused OE→Modern English roadmap says the project should “note explicitly why RP keeps /θ/ in `earth/hearth` but /d/ in `herd/word/sword`,” then restates the historical split as native `{*rθ/ð}` clusters retaining /θ/ while `{*rd}` words level to /d/ later [Germanic/docs/DEV_NOTES.md:2354-2374]. That is useful to preserve, but only conservatively: it is a later English-classification note, not primary support for the OE row itself.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-20465-20558

- Source heading: `§15.8 Two-Stage *ō Shortening: Early vs Late (Research)` / `The Problem` / `Key Finding from Campbell §355` / `Supporting Evidence`
- Source line or section hint: `lines 20465-20558`
- Fragment type: `shared_research_note_with_explicit_row_regression`
- Status: `diagnostic_but_still_material`
- Issue tags: `weak_noun_-ōn`; `eorþæ_regression`; `early_vs_late_shortening`; `Campbell_355`; `weak_noun_-e`
- Recommended next use: `primary anchor for explaining why row 1999 belongs with weak-noun *-ōn > -e outcomes, not with late stable-a endings`
- Shared with row IDs: `1933; 2005; other rows named in the same regression cluster`

This is the most important surviving DEV_NOTES fragment for row 1999 because it names the row's exact bad intermediate and explains why that output was rejected. DEV_NOTES says that an earlier reordering “introduced regressions: forms like `*érθōn → eorþæ` (expected `eorþe`) now show `-æ` instead of `-e`,” and immediately diagnoses the mistake: “The `*æ → *e` reduction ran too early—before these forms had their `*ō` shortened” [Germanic/docs/DEV_NOTES.md:20469-20472]. For this row, that is the key preserved project memory. The problem was not uncertainty over whether the counterpart should be `eorþe`; it was that an attempted chronology fix temporarily produced the wrong unstressed ending for a form that DEV_NOTES treats as belonging in the `-e` class.

DEV_NOTES then preserves the crucial Campbell quotation in full:

> “With regard to all these shortenings, it will be observed that, even when shortened late, *ō became *a, but that this *a was of too late origin to become *æ by Anglo-Frisian fronting (§333). Thus *ō if shortened **early** gives OE *æ(e)*, but if shortened **late** it gives *a*.” [Germanic/docs/DEV_NOTES.md:20478-20482]

The row-specific force of that quotation is spelled out in the example list immediately below it. DEV_NOTES identifies weak noun endings among the early-shortening class: “Weak noun endings: `*-ōn → -e` (tunge, éage, eorþe)” [Germanic/docs/DEV_NOTES.md:20490-20492]. It then adds two more preserved source quotations: “But in all areas *ō > *a when a nasal had followed ... and so n.s.f. of weak nouns, *tunge < *-ōn*,” and “Except before nasals, unaccented *a > *æ (later e, §369), e.g. n.s.f. and n. of weak nouns, OE *tunge, éage*” [Germanic/docs/DEV_NOTES.md:20509-20518]. Even though the current trace now derives `eorþe` correctly, this fragment remains materially useful because it states exactly why `eorþe`, not `eorþæ`, is the intended class outcome and ties that claim to preserved handbook evidence rather than to a bare project preference.

### DEV_NOTES:line-2354-2374

- Source heading: `Modern English (OE→Modern) roadmap — paused` / `Detailed blueprint (grounded in the standard OE/ME chronology)` / `Consonant outcomes`
- Source line or section hint: `lines 2354-2374`
- Fragment type: `shared_downstream_classification_note`
- Status: `current_but_downstream_only`
- Issue tags: `earth_hearth_bucket`; `rθ_cluster`; `rp_theta_retention`; `not_direct_oe_proof`
- Recommended next use: `use only to preserve later shared classification of earth as an inherited *rθ item`
- Shared with row IDs: `2066`

This fragment is not an OE-row dossier, but it is still worth preserving because DEV_NOTES explicitly names `earth` and assigns it to a stable later bucket. First the roadmap says the project should “Note explicitly why RP keeps /θ/ in `earth/hearth` but /d/ in `herd/word/sword` (OE retention vs. later analogical leveling)” [Germanic/docs/DEV_NOTES.md:2357-2358]. A few lines later the detailed blueprint restates the same split more formally: “native `{*rθ/ð}` clusters retain /θ/ in RP (`earth/hearth`), while `{*rd}` words level to /d/ in late ME (`herd/word/sword/bird`)” [Germanic/docs/DEV_NOTES.md:2373-2374].

For row 1999, the value of this note is classificatory rather than lexical. It does **not** tell us whether OE `eorþe` is attested, nor does it replace the weak-noun ending evidence above. What it does preserve is a later shared project judgment that `earth` belongs with inherited `rθ` material whose consonant history should not be conflated with the quite different `rd` set. If this slice is later used to rebuild row indexing, the fragment should therefore be cited as downstream shared support only, not as the main justification for the OE row [Germanic/docs/DEV_NOTES.md:2354-2374].

## Superseded or diagnostic material

- The explicitly superseded row-local bad state is `*érθōn → eorþæ`. DEV_NOTES preserves it as a regression caused by mistimed unstressed-vowel chronology, not as an alternate target worth keeping live [Germanic/docs/DEV_NOTES.md:20469-20472].
- The same §15.8 note is partly diagnostic because it was written during rule-order debugging. Its implementation discussion (`Early shortening → Fronting → Late shortening`) is preserved as research guidance, while the live row has already returned to an exact output `eorþe` in published traces [Germanic/docs/DEV_NOTES.md:20528-20554; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1057-1077].
- The OE→Modern `earth/hearth` vs. `herd/word/sword` note is current as a downstream classification reminder, but it is not row-specific OE evidence and should not be made to carry more philological weight than it has [Germanic/docs/DEV_NOTES.md:2357-2374].
- No row-1999 packet, research memo, or dedicated lexeme report was found. The replacement note therefore has to say plainly that surviving support is mainly one shared chronology note plus one downstream classification note, even though both are still genuinely relevant [Germanic/docs/lexeme_reports/coverage_audit.md:230-230; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- The live trace reaches `eorþe` through `OEUnstressedLongVowelShortening` and `OEUnstressedAEMerger`, while DEV_NOTES frames the class problem as an early-vs-late shortening chronology around fronting. If a later packet is created, it would be worth checking whether the current exact derivation is intended as a faithful implementation of the Campbell-style chronology or only as a surface-correct resolution [Germanic/docs/DEV_NOTES.md:20484-20554; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:7164-7168].
- If row 1999 later gets a fuller memo, the first literature task should probably be attestation-focused: gather direct lexicographic support for OE `eorþe` itself, because the strongest surviving DEV_NOTES material is still shared rule-order discussion rather than a lexeme dossier.
- If a future index links rows by shared DEV_NOTES material, row 1999 should probably be grouped with the weak-noun `*-ōn > -e` class first, and only secondarily with the downstream `earth/hearth` `rθ` bucket. The present evidence supports both links, but they answer different questions and should not be merged carelessly [Germanic/docs/DEV_NOTES.md:20490-20518,2357-2374].
