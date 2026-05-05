# Research memo — 2069 hedge / heġġ

## Starting point
- **ID:** 2069.
- **CONCEPT:** hedge.
- **COUNTERPART:** `heġġ`.
- **PROTO:** `*xágjaz`.
- **PROTOFORM:** `*xágjaz`.
- **DERIVATION_CLASS:** `regular`.
- **NOTE:** “Note: heċġ is the more standard spelling; using heġġ here.”
- The live row is currently treated as a regular success case, but the note makes it report-relevant and the comparative stem-class behind the row needs checking.
- No pilot lexeme report for this item was found in `Germanic/docs/lexeme_reports/pilot/`.

## Packet evidence assessment
**Authoritative/current:** the live TSV row; the packet's compact derivation showing the current system now expects and outputs `heġġ`; the January 2026 `DEV_NOTES.md` entries recording the rollback of `{ʤj} -> {ċġ}` and the present expectation that OE output should stay `ġġ`; and the current March 2026 debug snapshots that still show `EXPECTED: heġġ`, `OUTPUTS: heġġ`.

**Useful background:** the packet's `old_english_wiktionary.tsv` hit `heċġ`; the `DEV_NOTES.md` chronology note on `*-gj-*` ordering and stressed `e`; and the packet's stale-history excerpts, which are still useful for explaining how the project moved from `hæġġ/hæċġ` nondeterminism to the current normalized output.

**Stale or superseded:** the packet's 2026-01-18 note that `hedge` still produced both `hæġġ` and `hæċġ`; that is debugging history, not the live row state. The packet also overweights the absence of dossier/analysis hits: that was only a packet-search result, not proof that no broader philological material exists in the repo.

**Irrelevant or misleading if taken too literally:** the packet's exact-pair evidence can make the current `*xágjaz` look philologically settled, but the repo's comparative reference files point instead toward a feminine `*hagjō-` / WGmc `*hagjō(n)` type for the hedge noun. So the packet is strong on current engineering state, but weak on stem-class adjudication.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at 1726-1729, 1750-1753, 2630-2638, and 3070-3074.
- `Germanic/fsts/germanic.txt` at 773-818, 820-822, and 3412-3418.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md` at 2487-2515.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt` at 6548-6588.
- `Germanic/docs/dossiers/g-palatalisation-conditioning.md`, especially the discussion of the geminate-affricate `ċġ` side of palatalized `g`.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, `kaluza_historische_grammatik_englisch.txt`, `kroonen_etymological_dictionary_pgmc.vision.txt`, `kluge_seebold_etymologisches_woerterbuch.txt`, `bammesberger_1990_morphologie.txt`, `pokorny_iew_pages/00000028.txt`, and `orel_handbook_germanic_etymology.vision.txt`.

The extra repo research changes the picture materially: the packet was mainly about orthographic/debug history, whereas the reference files raise a separate proto/stem-class issue.

## Reconstruction and early-stage forms
Three distinct levels need to be kept apart here:

1. **Current TSV cognate-set proto:** `*xágjaz`.
2. **Current project derivational input:** also `*xágjaz` in the TSV, with the live trace using the internal engineering spelling `*xagjăz` for the same row.
3. **OE target represented by the row:** project-normalized `heġġ`.

The live derivational chronology from the current reports is internally coherent for a `*-gj-*` input: gemination, palatalization, i-umlaut, and `JLossAfterHeavy` yield `heġġ`. But the checked comparative sources do not really support `*xágjaz` as the hedge noun's lexeme-level proto. Kaluza gives `hecg` from `*hagjö-`; Kroonen separates ON `heggr` from OE `hecg` and derives the hedge noun from `*hagjō-`; Kluge reconstructs WGmc `*hagjō(n)`; Bammesberger and Pokorny point the same way.

So the row currently has a **working OE-facing input** but probably the wrong **comparative stem-class label**. The engineering trace and the philological reconstruction should not be collapsed into one claim.

## Old English philology
The checked OE-side evidence supports plain dictionary/headword spellings such as `heċġ` / `hecg`, not `heġġ`, as the ordinary philological citation point. `old_english_wiktionary.tsv` gives `heċġ`; Bosworth-Toller has `hecg, hegg, e; f.`; Kaluza cites `hecg` as the OE reflex of `*hagjö-`. That is the strongest repo-local basis for the lexeme as an OE noun.

Accordingly:
- **attested / dictionary side:** `heċġ` / `hecg` (with spelling variation of the expected lexicographic kind);
- **project-normalized row target:** `heġġ`;
- **lexical status:** ordinary noun/headword, not a special inflected paradigm cell;
- **philological caution:** the row's `heġġ` should be presented as a project normalization or engineering target, not as the default dictionary spelling.

The checked repo materials do not suggest a dialect-selection problem or a citation-form-vs-oblique-form problem. The OE issue is representational, not paradigmatic.

## Project problem and solution
The project has had **two different problems** here.

First, there was an engineering orthography problem: older January notes showed nondeterministic `hæġġ` / `hæċġ`, then the project deliberately reverted `{ʤj} -> {ċġ}`, added `OECjCleanup`, and normalized the live target/output to `heġġ`. That problem is now resolved in the current traces.

Second, and more importantly for the memo stage, there is a **philological data problem** still visible in the live row: the project now derives the chosen OE-form target successfully, but it appears to do so from a comparative proto/stem class (`*xágjaz`) that is not what the repo's own reference files give for the hedge noun. The best project solution is therefore:
1. keep the current success state explicit (`heġġ` is the live project-normalized target and the FST now reaches it);
2. explain that standard OE headword evidence is `heċġ` / `hecg`;
3. review the row's proto data separately, because the orthography fix did not adjudicate the deeper stem-class question.

## Paradigm probe
No paradigm probe is required.

Reason: this is not a late-analogy or paradigm-cell-selection case. The live issue is normalized OE spelling plus likely proto/stem-class correction, not uncertainty about which OE cell should feed the row. A probe table would not resolve the main memo question.

## Recommended final report
Recommend a short final report that says the live row currently represents project-normalized `heġġ`, corresponding to standard OE `heċġ` / `hecg`, and that the January `hæġġ/hæċġ` nondeterminism is superseded engineering history. It should also note, concisely, that the current TSV `*xágjaz` looks philologically suspect against the repo's comparative references for a feminine `*hagjō-` type, so live derivation input and comparative reconstruction should be kept distinct.

## Data-change recommendations
- **TSV `PROTO`:** **change recommended.** Re-review and likely replace `*xágjaz` with a feminine `*xágjō` / WGmc `*xágjō(n)`-type reconstruction consistent with the repo's comparative references.
- **TSV `PROTOFORM`:** **change recommended.** It currently duplicates the same likely-wrong stem class; the OE-facing input should be reviewed alongside `PROTO`, not left at `*xágjaz` by default.
- **TSV `COUNTERPART`:** no immediate change recommended. Keep `heġġ` if the project intends to preserve its current normalized palatal-geminate policy, but the final report must state clearly that standard lexicographic OE is `heċġ` / `hecg`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `regular` still matches the row's current project role.
- **TSV `NOTE`:** **change recommended.** The note should say explicitly that `heġġ` is a project-normalized target, while source/headword evidence favors `heċġ` / `hecg`; if the proto review is adopted, the note should not imply that spelling is the only issue.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** **`DEV_NOTES` change recommended; dossier text no change recommended.** `DEV_NOTES.md` should mark the 2026-01-18 hedge nondeterminism note more explicitly as superseded by the later cleanup, and it would be useful to note that the later orthography fix did not itself settle the comparative proto/stem-class question. No hedge-specific dossier cleanup is needed from the materials checked.
