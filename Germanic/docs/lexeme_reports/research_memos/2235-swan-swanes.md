# Research memo — 2235 swan / swanes

## Starting point

- **ID:** 2235
- **CONCEPT:** swan
- **COUNTERPART:** swanes
- **PROTO:** *swánaz
- **PROTOFORM:** *swánas
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** empty in the live TSV

The live row is currently a paradigm-cell row rather than a citation-form row: the cognate-set proto/headword is PGmc nom.sg. `*swánaz`, the project input is the PGmc gen.sg. `*swánas`, and the OE target is likewise the gen.sg. `swanes`. The workaround explanation is not in TSV `NOTE`; it currently survives only as note-like text in TSV `STRUCTURE` (`Note: using gen.sg. *swanas (> swanes)`).

## Packet evidence assessment

**Authoritative/current:** the live TSV identity of the row (`PROTO = *swánaz`, `PROTOFORM = *swánas`, `COUNTERPART = swanes`, `DERIVATION_CLASS = early_analogy`) and the packet's compact derivation trace showing that the current cascade does produce `*swánas -> swanes`.

**Useful background:** the packet's `old_english_wiktionary.tsv` hit for citation-form `swan`; and the packet's two `DEV_NOTES` excerpts as evidence of earlier debugging history around `*swanăz` and paradigm-cell workarounds.

**Stale or superseded:** the packet does not surface later repo evidence that the current FST also handles nominative `*swánaz -> swan` directly. Its `DEV_NOTES.md:2539` tail-bucket note is diagnostic history from a 2025 debugging pass, not current row authority; and the `DEV_NOTES.md:3216` `rast` parallel is only a methodological analogy, not direct evidence for retaining `swanes`.

**Irrelevant or misleading:** the packet can easily be over-read as if lexicographic support existed for exact `swanes`; in fact the packet's only lexical-table hit is `swan`. The packet also obscures that live TSV `NOTE` is actually empty, while the workaround explanation sits in `STRUCTURE` instead.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 2531-2545 and 3208-3218.
- `Germanic/docs/germanic_notes/analogical_leveling_analysis.md`.
- `Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md`.
- `Germanic/docs/debug_snapshots/mismatch_comparison_2026-02-06b.md`.
- `Germanic/tools/oe_paradigm_probe.py` plus manual probe runs for `*swánaz`, `*swánas`, and `*swanum`.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto.
- `Germanic/data/old_english_wiktionary.tsv` — citation/headword `swan` only.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*swanaz ... OE swan`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `swan`.
- `docs/references/bright_anglo_saxon_reader.vision.txt` — glossary explicitly gives `swan, m., swan: gs. swanes` and cites the textual phrase `swanes feðre`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — checked, but the quick repo hits were incidental phrase occurrences rather than a clean headword line.

No full dossier or analysis file specifically named in the packet or TSV note was identified, and no pilot/full lexeme report already exists for `swan / swanes`.

The decisive extra probe results are:

- **nom.sg.** `*swánaz -> swan`
- **gen.sg.** `*swánas -> swanes`
- **older proposal from stale analysis:** `*swanum -> swanum`, not `swan`

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*swánaz`, the PGmc masculine a-stem lexeme.
2. **Current project input:** TSV `PROTOFORM` `*swánas`, a selected PGmc **gen.sg.** cell.
3. **Current OE target:** `swanes`, likewise a **gen.sg.** form, not the citation lemma.

The current gen.sg. derivation is straightforward in-project: `*swánas -> *swánæs -> swanes`. But extra repo research shows that the present FST also derives the citation form directly: `*swánaz -> swan`.

That matters because older project history treated nominative `*swanăz -> *swæn` as the blocking problem and proposed oblique-cell workarounds, including an earlier `*swanum` idea in `analogical_leveling_analysis.md`. In the current repo state, that `*swanum` proposal is stale: the live row is not `*swanum`, and the current FST gives `swanum`, not `swan`.

## Old English philology

Repo-local philology supports the **citation lexeme** `swan` most strongly, but it also gives direct support for exact **gen.sg. `swanes`**.

- **Etymological dictionary evidence:** Orel gives PGmc `*swanaz` with OE `swan`.
- **Dictionary/headword evidence:** Clark Hall gives headword `swan`.
- **Supplementary lexical table:** `old_english_wiktionary.tsv` again gives only `swan`.
- **Exact inflected-form support:** Bright's reader/glossary explicitly lists `swan, m., swan: gs. swanes` and cites the phrase `swanes feðre`.

So unlike rows such as `brand / brandes`, this row's exact oblique target is not merely morphologically imaginable: `swanes` is directly supported in repo-local reference material. But that does **not** make `swanes` the lexical headword. The philological distinction remains:

- **citation/headword:** `swan`;
- **attested inflected cell:** gen.sg. `swanes`;
- **current project target:** `swanes`, which is therefore a real OE form, but still an inflected paradigm cell rather than the default lexeme label.

## Project problem and solution

The project history appears to be: during the February 2026 A-restoration debugging phase, the row was shifted away from nominative `*swanăz -> swan` and repointed to a safer oblique cell. `mismatch_comparison_2026-02-06b.md` records that move explicitly as `*swanăz -> *swanas`, `swan -> swanes`, while older `analogical_leveling_analysis.md` still preserves an even earlier `*swanum` proposal.

But the present repo state is not the same as that historical debugging moment. The current FST already derives nominative `*swánaz -> swan`, and the row no longer needs an oblique-cell workaround merely to get a usable OE outcome. The exact gen.sg. `swanes` is genuine OE, but keeping it as the main row target would now be a **project choice to model a paradigm cell**, not a forced phonological rescue.

So the strongest present recommendation is to normalize the row back to the lexeme-level citation setup:

- keep **TSV `PROTO = *swánaz`**;
- restore **TSV `PROTOFORM = *swánaz`**;
- restore **TSV `COUNTERPART = swan`**;
- classify the row as a regular citation-form derivation rather than as `early_analogy`.

If the team intentionally wants a separate gen.sg. row because `swanes` is directly attested, then it should be described explicitly as a selected paradigm-cell entry and not as an `early_analogy` stem-shaping case.

## Paradigm probe

A paradigm probe **is required to audit the current row**, because the live row is using a selected inflectional cell rather than the citation form.

The key cells have already been checked manually:

- **nom.sg.** `*swánaz -> swan`
- **gen.sg.** `*swánas -> swanes`

There is still **no built-in row-specific saved probe** in `oe_paradigm_probe.py`, so a formal reusable probe is still missing. If one is saved, the minimum cells that should be probed are:

- **nom.sg.** `*swánaz`
- **gen.sg.** `*swánas`

A dat.pl. cell is not required for the main decision, but `*swanum` can be included as a historical control if the team wants to document that the older `analogical_leveling_analysis.md` proposal is now stale.

## Recommended final report

Recommend **not** drafting the final `### Lexeme report` until the row-level data decision is made. Preferred outcome: normalize the row back to regular `*swánaz -> swan`, in which case no special final lexeme report would be needed. If `swanes` is retained intentionally, the final report should be brief and should state explicitly that `PROTO` is the lexeme headword, `PROTOFORM` is a selected gen.sg. cell, and `swanes` is a genuine attested OE inflected form rather than the citation lemma.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** **change recommended** — preferred fix is to revert from `*swánas` to citation-form `*swánaz`.
- **TSV `COUNTERPART`:** **change recommended** — preferred fix is to revert from `swanes` to `swan`.
- **TSV `DERIVATION_CLASS`:** **change recommended** — preferred fix is `regular`, since the current FST now derives `*swánaz -> swan` directly. If the team nevertheless keeps `swanes`, the fallback class should be `late_analogy`, not `early_analogy`.
- **TSV `NOTE`:** no change required under the preferred normalization path (it can remain empty). If the team keeps `swanes`, then **change recommended**: add an explicit paradigm-cell note in `NOTE` instead of relying on note-like text in `STRUCTURE`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** **change recommended** — `analogical_leveling_analysis.md` and `mismatch_comparison_2026-02-06b.md` should be marked more clearly as historical debugging context, especially the stale `*swanum` proposal and the temporary `swan -> swanes` workaround framing. No full dossier text was identified for this row.
