---
row_id: 2209
concept: spoon
counterpart: spōn
proto: *spḗnuz
protoform: *spḗnuz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2209 spoon / spōn

## Current row state

- CONCEPT: `spoon`
- COUNTERPART: `spōn`
- PROTO: `*spḗnuz`
- PROTOFORM: `*spḗnuz`
- DERIVATION_CLASS: `regular`
- Live TSV row `2209` already treats the item as a regular derivation with no row note and no row-level split between comparative headword and OE-directed input: `PROTO = PROTOFORM = *spḗnuz`, `COUNTERPART = spōn` [Germanic/data/germanic-aligned-final.tsv:1082-1082].
- `oe_known_problems.tsv` has no row-specific problem entry for `*spḗnuz` / `spōn`; current exception tracking does not classify the row as unresolved or wontfix [Germanic/data/oe_known_problems.tsv:1-8].
- No row-specific packet or research memo stem currently exists under `Germanic/docs/lexeme_reports/packets/` or `.../research_memos/`, so the canonical row-based slice has to serve as the working note for the row.
- The current published derivation trace is fully regular and explicit: `Proto Input: *spḗnuz`; then `PGmc Final Z Deletion: *spḗnu`; then `NWGmc Long E Nasal Rounding: *spōnu`; then `OE High Vowel Apocope: *spōn`; final outcome `spōn` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4567-4585].
- Background lexicographic material is compatible with the live row, but it uses ordinary comparative citation practices rather than the project's stress-marked `*ḗ`: Orel gives `*spēnuz ~ *spōnuz sb.m.` with OE `spón 'chip'`, and Bülbring includes OE `spōn 'Spahn'` among the forms showing nasal `ō` [@Orel2003; @Bulbring1902, §124; @ClarkHall1960, s.v. "spōn"].

## Development-note summary

Current DEV_NOTES authority for row `2209` is thin but still usable. There is no long lexeme-specific dossier weighing rival stem classes, paradigm cells, or exception status. The surviving attachable material instead consists of one **current** shared refactor note and one **diagnostic** earlier regression note. That is enough to explain why the live row now reads `*spḗnuz → spōn`, but not enough to pretend that DEV_NOTES already contain a fully developed spoon report [Germanic/docs/DEV_NOTES.md:24443-24510,42683-42739].

The controlling current material is the stressed-long-`ē` refactor. DEV_NOTES says the project had already introduced stressed long-vowel symbols such as `*ḗa` and `*ḗo`, and therefore had to represent stressed inherited long `ē` consistently too: “if we mark stress on long *ī, we must mark it on long *ē too” [Germanic/docs/DEV_NOTES.md:42683-42692]. `*spēnuz` is named explicitly among the roughly sixteen root-syllable long-`ē` lemmas promoted to `*ḗ` in both `PROTOFORM` and `PROTO` [Germanic/docs/DEV_NOTES.md:42688-42728]. For this row, that means the live TSV spelling `*spḗnuz` is a **project modelling convention for stressed root-syllable long `ē`**, not a claim that comparative dictionaries have stopped citing the etymon in ordinary unaccented form [Germanic/data/germanic-aligned-final.tsv:1082-1082; @Orel2003].

That distinction matters even though `PROTO` and `PROTOFORM` happen to be identical here. `PROTO` remains the row's comparative/cognate-set headword as stored in the live TSV, while `PROTOFORM` is the exact OE-facing input fed into the cascade. For row `2209` no special paradigm-cell choice, class shift, or analogical rescue is needed, so the two fields coincide. The crucial point is simply that both now carry the stress-marked project notation `*spḗnuz`, because the row belongs to the same stressed-long-`ē` batch as `*dḗdiz`, `*mḗnōθz`, and `*jḗrą` [Germanic/docs/DEV_NOTES.md:42688-42728,42735-42739].

The row's present derivation is therefore straightforward and regular in current project terms. The published trace shows `*spḗnuz` losing final `-z`, then undergoing `NWGmc Long E Nasal Rounding` to `*spōnu`, and then losing final high vowel by `OE High Vowel Apocope`, yielding `spōn` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4575-4585]. DEV_NOTES confirms that this was not merely assumed to work: the refactor verification line preserves `*spḗnuz → spōn` as one of the explicit sample outputs used to show that mismatch totals stayed stable through the change [Germanic/docs/DEV_NOTES.md:42735-42739].

The only substantial older DEV_NOTES material that mentions the row is diagnostic rather than current. In the earlier `*-uz` regression note, the row appears as `*spēnuz → spōno (expected spōn)` after `PGmcFinalZDeletion` had been moved too late in the cascade [Germanic/docs/DEV_NOTES.md:24443-24510]. That note predates the later stressed-`*ḗ` retrofit, so the protoform is still written `*spēnuz`; the spelling difference is chronological notation, not a different lexical policy. The actual problem was temporary rule ordering: final `-z` was still present when unstressed-`u` lowering checked for a following consonant, so word-final `*-uz` behaved as though it were medial and produced bad outputs ending in `-o`. Once that chronology was corrected, the row went back to the regular derivation now shown in the live trace [Germanic/docs/DEV_NOTES.md:24466-24510; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4575-4585].

Because the surviving DEV_NOTES support is both thin and heavily shared, the honest replacement note has to say so. There is enough current authority to justify the live row metadata, to explain why the proto columns now use `*spḗnuz`, and to label `spōno` as stale regression history. There is **not** enough row-specific DEV_NOTES prose yet to support a richly indexed lexeme dossier on the same level as rows with dedicated source canvasses or stem-class arguments. For now, this slice should be treated as a careful working note, probably no-index, until or unless a packet or literature memo is built around the row [Germanic/docs/DEV_NOTES.md:24443-24510,42683-42739].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-42683-42728

- Source heading: `stressed long-ē refactor motivation and TSV root-syllable promotion`
- Source line or section hint: `lines 42683-42728`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `stress_marking`; `proto_vs_protoform`; `row_policy`; `shared_sound_change`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current fragment for row `2209`. DEV_NOTES explains that the project had already added other stressed long-vowel symbols and therefore needed a parallel symbol for stressed long `ē`; the motivating sentence is preserved verbatim: “if we mark stress on long *ī, we must mark it on long *ē too” [Germanic/docs/DEV_NOTES.md:42690-42692]. The same fragment names `*spēnuz` in the list of root-syllable long-`ē` lemmas and then says that sixteen such lemmas were promoted from `*ē` to `*ḗ` in both `PROTOFORM` and `PROTO` [Germanic/docs/DEV_NOTES.md:42688-42728]. For this row, the fragment's practical use is narrow but decisive: it explains why the live TSV now writes `*spḗnuz`, and it shows that this spelling is a current modelling decision rather than an accidental respelling or a new claim about comparative dictionary headword practice [Germanic/data/germanic-aligned-final.tsv:1082-1082; @Orel2003].

### DEV_NOTES:line-42735-42739

- Source heading: `verification sample after stressed long-ē refactor`
- Source line or section hint: `lines 42735-42739`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `verification`; `regular_output`; `stress_marking`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short verification fragment is the clearest row-local proof that the refactor left the live derivation working. DEV_NOTES says mismatch totals remained stable and then gives the sample outputs as “`*dḗdiz → dǣd*, *lḗtaną → lǣtan*, *rḗdaną → rǣdan*, *mḗnōθz → mōnaþ*, *spḗnuz → spōn* ...” [Germanic/docs/DEV_NOTES.md:42735-42739]. For row `2209`, this matters because it shows `spōn` not merely as an inferred consequence of the new notation, but as one of the explicit checked successes of the branch.

### DEV_NOTES:line-24443-24510

- Source heading: `§17.10.25 — Case 3 Option δ post-reorder: *-uz cluster regression`
- Source line or section hint: `lines 24443-24510`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `rule_ordering`; `final_z_deletion`; `stale_regression`; `shared_-uz_problem`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2009; 2143; 2152`

This fragment should be preserved only as project-history diagnostics. DEV_NOTES lists `*spēnuz | spōno | spōn` among eight new `*CVCuz` regressions after `PGmcFinalZDeletion` had been pushed below `OEMedUnstressedULowering` [Germanic/docs/DEV_NOTES.md:24451-24464]. The note then explains the mechanism: while final `-z` was still present, the `u` in forms like `*bebruz` or `*spēnuz` looked medial because a consonant still stood to its right, so unstressed `u` lowered to `o` and later surfaced as bad final `-o` after z-loss [Germanic/docs/DEV_NOTES.md:24466-24510]. For row `2209`, two cautions matter. First, the fragment predates the later stressed-`*ḗ` refactor, so its `*spēnuz` spelling is older notation, not a rival current row form. Second, `spōno` is not an alternative lexical analysis; it is just a stale regression output from a temporary rule-ordering mistake.

## Superseded or diagnostic material

- The only real superseded row history inside DEV_NOTES is the temporary regression `*spēnuz → spōno`. It should be cited, if at all, only to explain why some older branch diagnostics showed final `-o` instead of `spōn` [Germanic/docs/DEV_NOTES.md:24451-24510].
- The older spelling `*spēnuz` in that regression note is not itself superseded philology. It is merely the pre-refactor notation from before the project started marking stressed inherited long `ē` with `*ḗ` in live row metadata [Germanic/docs/DEV_NOTES.md:24462-24462,42683-42728].
- No fuller lexeme-specific DEV_NOTES argument survives for spoon. Later work should not invent one by overstating these fragments; if a final lexeme report needs broader etymological discussion, it will have to draw on fresh packet or source work rather than on a nonexistent spoon dossier in `DEV_NOTES.md`.

## Open questions for later work

- If a packet or research memo is later created for row `2209`, decide whether it should foreground the simple regular trace (`*spḗnuz > *spḗnu > *spōnu > spōn`) or begin with the notation point that comparative dictionaries still tend to cite `*spēnuz` / `*spōnuz` without the project stress mark [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4575-4585; @Orel2003].
- If `index.tsv` is updated later, keep the row conservative: the likely candidates are the current stressed-long-`ē` promotion fragment and the short verification fragment, while the `spōno` regression note belongs only as diagnostic history.
- If older debug or packet material ever surfaces with `*spēnuz` or `spōno`, annotate it explicitly as pre-`*ḗ` notation or stale rule-ordering output rather than as evidence against the live regular row.
