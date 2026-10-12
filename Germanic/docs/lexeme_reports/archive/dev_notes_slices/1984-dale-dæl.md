---
row_id: 1984
concept: dale
counterpart: dæl
proto: *dálaz
protoform: *dálaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1984 dale / dæl

## Current row state

- The live OE row currently reads `ID 1984 | CONCEPT dale | COUNTERPART dæl | PROTO *dálaz | PROTOFORM *dálaz | DERIVATION_CLASS regular`, with no row-specific `NOTE`; the only `HISTORY` text is duplicated Wiktionary inheritance provenance [Germanic/data/germanic-aligned-final.tsv:207-207].
- Coverage infrastructure still lists the row as uncovered and unattached: `| 1984 | dale | dæl | regular | no | - | - | - | none |`. In practice this means there is no row-specific packet or research memo already wired up for the lexeme, so the present slice has to stand in as the replacement working note [Germanic/docs/lexeme_reports/coverage_audit.md:219-219].
- The live published OE trace is clean and minimal. It gives `PROTO: *dálaz`, `EXPECTED: dæl`, `OUTPUTS: dæl`, with the effective derivation `PGmc Final Z Deletion: *dála` > `PWGmc Final Bare A Loss: *dál` > `Anglo Frisian Brightening: *dæl` > `Outcome: dæl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:793-812].
- The full trace confirms the same point in rule-by-rule form: after `PGmcFinalZDeletion` and `PWGmcFinalBareALoss`, the form is already monosyllabic `*dál`, and every later OE rule is `[no-change]` except `AngloFrisianBrightening`, which yields `*dæl`; surface cleanup then simply removes stars [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:5455-5569].
- `oe_known_problems.tsv` has no entry for `*dálaz`, which is consistent with the live traces: the row is not being tracked as an exception or mismatch bucket [Germanic/data/oe_known_problems.tsv:1-8].
- The row does, however, sit inside a broader repo analysis of A-restoration before single `*r/*l`. That analysis names row `1984` explicitly and already marks it as stable: `*dálaz | dæl | dæl | dæl | monosyllabic; final *-az → ∅, no surviving back trigger`. The same analysis also quotes the Campbell-style closed-monosyllable class and includes `dæl` in the list `fæt, dæg, hwæl, dæl, bæþ, bæc, blæd, fæc, stæf, pæþ` [Germanic/docs/analysis/arestoration_r_l_research.md:709-715,385-392].

## Development-note summary

DEV_NOTES support for row `1984` is real but indirect. No row-dedicated `dale` / `dæl` / `*dálaz` lexeme section survives in `Germanic/docs/DEV_NOTES.md`; the materially relevant evidence is instead shared A-restoration discussion that explains why this row stays brightened and why it never needed the later `*r/*l` conditioning repair [Germanic/docs/DEV_NOTES.md:3131-3148,3171-3178,36524-36629].

The first substantive point preserved in DEV_NOTES is the trigger logic. In the A-restoration cleanup, DEV_NOTES says that the old idea that fronted suffix `*æ` could still count as “underlyingly back” was wrong, and that Ringe–Taylor’s `dæg` paradigm proves the opposite: `*dagas → dæges` because `*-as` fronts and does **not** trigger restoration, whereas `*dagos → dagas` and `*dagum → dagum` do restore because `*-os` and `*-um` contain genuine back vowels [Germanic/docs/DEV_NOTES.md:3131-3138,3171-3178]. For row `1984`, that is the key interpretive point. Once `*dálaz` loses final `*z` and then loses bare final `*a`, no back-vowel trigger survives to retract `*æ` back to `a`; the published trace `*dála > *dál > *dæl` is exactly what that DEV_NOTES logic predicts [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:802-812].

The second substantive point is negative but important. DEV_NOTES later re-opened A-restoration before single `*r` and `*l` and concluded that liquids themselves do **not** block restoration: Campbell is quoted as saying that “The restoration of *a* is common before all single consonants and geminates,” R/T says retraction applies when `*æ` is followed by “a single or geminate consonant or sC-cluster” plus a back vowel, and Luick is cited for restoration being independent of “the quality of the intervening single consonant” [Germanic/docs/DEV_NOTES.md:36526-36536]. That matters here because row `1984` superficially fits the structural template `*a/á + l + back-vowel tail` catalogued in the later `*r/*l` audit. The note to preserve is that `dæl` is **not** correct because `l` blocks A-restoration; it is correct because by the time OE A-restoration could have applied, there is no surviving trigger vowel left.

DEV_NOTES also preserves the downstream project judgement that this row never became a problem case in that audit. In the predicted side-effects note for the `*r/*l` fix, DEV_NOTES says that of the eight relevant TSV rows, two needed change and the “Other six rows” were “already correct; unaffected by the change” [Germanic/docs/DEV_NOTES.md:36614-36629]. DEV_NOTES does not spell out those six rows by name there, but the attached analysis file does, and row `1984` is one of them with the explicit explanation `monosyllabic; final *-az → ∅, no surviving back trigger` [Germanic/docs/analysis/arestoration_r_l_research.md:709-715]. So the replacement note should preserve both halves of the evidence: the row is regular and stable, but the row-specific statement survives mostly in linked analysis rather than in a bespoke DEV_NOTES lexeme paragraph.

## Relevant DEV_NOTES fragments

No lexeme-explicit `dæl` fragment currently survives in `DEV_NOTES.md`. The attachable material is therefore shared rule discussion whose relevance has to be stated explicitly rather than overstated.

### DEV_NOTES:line-3131-3148

- Source heading: `Water fix: PWGmc ō-shortening and A-restoration correction`
- Source line or section hint: `lines 3131-3148`
- Fragment type: `shared_rule_background`
- Status: `current`
- Issue tags: `a_restoration_trigger_logic`; `fronted_suffix_non_trigger`; `day_paradigm_background`
- Recommended next use: `cite_when_explaining_why_dæl_stays_brightened`
- Shared with row IDs: `1985`; `2003`; other `a/æ` restoration rows

This fragment preserves the core rule statement needed for row `1984`. DEV_NOTES says the earlier trigger analysis was wrong and that “only genuine back vowels (*o, *u, *ō, *ū, *ô) trigger A-restoration. Fronted suffix vowels (*æ from AFB'd *a) do NOT trigger it” [Germanic/docs/DEV_NOTES.md:3131-3138]. The worked `*watōr → *watar → *wætær → (A-restoration: NO trigger, *æ is not back) *wætær` derivation is not about `dæl` itself, but it preserves the exact logic row `1984` needs: after `*dálaz` loses `*-az`, there is no genuine back-vowel trigger left to undo brightening [Germanic/docs/DEV_NOTES.md:3146-3148; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:802-812].

### DEV_NOTES:line-3171-3178

- Source heading: `Background: A-restoration and paradigmatic leveling`
- Source line or section hint: `lines 3171-3178`
- Fragment type: `shared_rule_background`
- Status: `current`
- Issue tags: `dæg_paradigm`; `a_restoration`; `suffix_quality`
- Recommended next use: `cite_in_any_final_row_explanation`
- Shared with row IDs: `1985`; `2152`; other rows discussed through the `dæg` paradigm

This is the clearest compact statement of the trigger principle. DEV_NOTES says: `*dagas → dæges` because `*-as` fronts and “does NOT trigger restoration,” but `*dagos → dagas` and `*dagum → dagum` do restore because `*-os` and `*-um` remain back; the principle is then stated explicitly: “original PGmc *a in suffixes is fronted by AFB and does NOT trigger restoration. Original PGmc *o, *u in suffixes stay back and DO trigger restoration” [Germanic/docs/DEV_NOTES.md:3171-3178]. For row `1984`, this is materially relevant even though `dæl` is not named. The comparative shape `*dálaz` belongs on the non-triggering side of the contrast: the old `*-az` tail does not leave a back vowel behind, so the OE outcome remains brightened `dæl`, not restored `dal`.

### DEV_NOTES:line-36526-36552

- Source heading: `The canonical conditioning of A-restoration (literature consensus)`
- Source line or section hint: `lines 36526-36552`
- Fragment type: `shared_rule_discussion`
- Status: `current`
- Issue tags: `single_r_l`; `cluster_conditioning`; `campbell_quote`; `ringe_taylor_quote`
- Recommended next use: `cite_with_negative_scope_note`
- Shared with row IDs: `2003`; `2205`; `2141`; the wider `*r/*l` restoration cohort

This fragment matters because row `1984` was later swept into the `*r/*l` audit by shape, and DEV_NOTES is explicit that liquids are **not** blockers. The note quotes Campbell: “The restoration of *a* is common before all single consonants and geminates,” quotes R/T: retraction applies when `*æ` is followed by “a single or geminate consonant or **sC-cluster**” plus a back vowel, and cites Luick's “unabhängig von der Art der dazwischen stehenden Konsonanten” [Germanic/docs/DEV_NOTES.md:36531-36536]. For row `1984`, the important consequence is interpretive. Any explanation that says `dæl` stayed fronted because `l` blocked restoration would misread the surviving DEV_NOTES discussion. The correct explanation is that `l` would be compatible with restoration **if** a back-vowel trigger survived; here none does [Germanic/docs/analysis/arestoration_r_l_research.md:709-715].

### DEV_NOTES:line-36614-36629

- Source heading: `Predicted side-effects`
- Source line or section hint: `lines 36614-36629`
- Fragment type: `shared_row_bucket_status`
- Status: `current_but_indirect`
- Issue tags: `r_l_audit`; `unaffected_rows`; `manual_trace_verification`
- Recommended next use: `cite_if_explaining_why_row_never_needed_fix`
- Shared with row IDs: the eight-row `*a/á + r/l + back vowel` cohort

This fragment is the closest DEV_NOTES comes to a row-status judgement for `1984`. DEV_NOTES says that among the eight TSV rows with `*a/á + r/l + back vowel`, two required change and the “Other six rows” were “all already correct; unaffected by the change” [Germanic/docs/DEV_NOTES.md:36614-36629]. The note is indirect because row `1984` is not named there, but the linked analysis file identifies it as one of those six and explains why: `monosyllabic; final *-az → ∅, no surviving back trigger` [Germanic/docs/analysis/arestoration_r_l_research.md:709-715]. That is probably the sharpest replacement-note formulation available in the current repo.

## Superseded or diagnostic material

- No row-specific superseded repair proposal for `1984` currently survives. Unlike the true mismatch rows in the same research neighborhood, `dale / dæl` was already matching before and after the later `*r/*l` A-restoration work [Germanic/docs/DEV_NOTES.md:36614-36629].
- The main diagnostic trap is to confuse structural inclusion in the `*r/*l` audit with row-local instability. Row `1984` appears in that cohort only because its protoform contains `á + l +` a historical tail; the live trace shows that the historical tail disappears before any restoration opportunity, so the row's correct surface `dæl` is not a special exception case [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:802-812; Germanic/docs/analysis/arestoration_r_l_research.md:709-715].
- The most explicit row-local wording now lives outside DEV_NOTES proper, in attached analysis rather than a dedicated packet or memo. That is useful working evidence, but it also means later writers should not pretend that `DEV_NOTES.md` already contains a bespoke lexeme paragraph for `dæl` [Germanic/docs/analysis/arestoration_r_l_research.md:385-392,709-715; Germanic/docs/lexeme_reports/coverage_audit.md:219-219].

## Open questions for later work

- If a final lexeme report is ever drafted, decide whether the current shared-rule evidence is strong enough for indexing or whether row `1984` should remain a no-index slice until a row-specific packet/memo exists. The row itself looks stable, but the DEV_NOTES footprint is still indirect.
- If stronger philological support is wanted later, add direct lexicographic or handbook citations for OE `dæl`; the current slice relies mainly on shared A-restoration logic plus the linked row-analysis table, not on a dedicated lexeme-by-lexeme source review.
- If later presentation material summarizes the row in one sentence, it should say something like “regular brightening after loss of `*-az`, with no surviving back-vowel trigger for A-restoration,” not merely “`l` blocks restoration,” because the latter would contradict the surviving DEV_NOTES discussion [Germanic/docs/DEV_NOTES.md:36526-36536; Germanic/docs/analysis/arestoration_r_l_research.md:709-715].
