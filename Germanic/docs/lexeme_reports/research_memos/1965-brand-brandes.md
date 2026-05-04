# Research memo — 1965 brand / brandes

## Starting point

- **ID:** 1965
- **CONCEPT:** brand
- **COUNTERPART:** brandes
- **PROTO:** *brándaz
- **PROTOFORM:** *brándas
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Note: using gen.sg. *brandas (> brandes).

The live row is currently set up as a non-lemma paradigm-cell row: the cognate-set headword is PGmc nom.sg. `*brándaz`, but the derivational input is the gen.sg. `*brándas`, and the OE target is likewise the gen.sg. `brandes`.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing that the current cascade turns `*brándas` into `brandes`; and the packet's exact row metadata identifying the present setup as `PROTO = *brándaz`, `PROTOFORM = *brándas`, `COUNTERPART = brandes`.

**Useful background:** the packet's `old_english_wiktionary.tsv` hit for citation-form `brand`; the `DEV_NOTES.md:5028` excerpt showing that the project had already used `brand` as a no-metathesis control in a gen.sg.-style context; and the packet's concept-level `DEV_NOTES` hits showing that `brand` belonged to an earlier cluster of paradigm-form experiments.

**Stale or superseded:** the packet does not surface later repo evidence that the current FST also handles nominative `*brándaz -> brand` cleanly. The broad paradigm-work discussion at `DEV_NOTES.md:90` and the February 2026 debug history behind the shift from `brand` to `brandes` are useful chronology, but they are not by themselves proof that the present row still needs an oblique-cell workaround.

**Irrelevant or misleading:** the packet's lexical-table citation hit `brand` should not be mistaken for support for exact `brandes`; and the concept-only `DEV_NOTES` parallels to rows like `rast` are methodological background, not direct evidence that this row should remain an `early_analogy` entry.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 90, 1669-1674, 3216-3218, 5028, and 38129-38132.
- `Germanic/docs/germanic_notes/weak_tail_vowels_and_a_restoration.md` and `Germanic/docs/germanic_notes/analogical_leveling_analysis.md`.
- `Germanic/docs/debug_snapshots/mismatch_comparison_2026-02-06b.md`.
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run for this memo.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto.
- `Germanic/data/old_english_wiktionary.tsv` — citation/headword `brand` only.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — `*brandaz I ... OE brand` and `*brandaz II ... OE brand 'sword'`.
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt` — `bran-da-z (m) ... ae. brand`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `brand`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — headword `brand/brond` plus oblique/plural forms such as `brandas`, `branda`, `brandum`.

No full dossier or analysis file specifically named in the packet or TSV note was identified for this lexeme, and no pilot lexeme report exists for `brand / brandes`.

The manual probe is the key extra result:

- **nom.sg.** `*brándaz -> brand`
- **gen.sg.** `*brándas -> brandes`

## Reconstruction and early-stage forms

This row needs the standard three-way distinction kept explicit:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*brándaz`, the PGmc masculine a-stem lexeme.
2. **Current project input:** TSV `PROTOFORM` `*brándas`, a selected PGmc **gen.sg.** cell.
3. **Current OE target:** `brandes`, likewise a **gen.sg.** form, not the citation lemma.

The current gen.sg. derivation is straightforward: the packet trace gives `*brándas -> *brándæs -> brandes` via Anglo-Frisian fronting in the ending and later unstressed `æ > e` merger. But the extra repo check is crucial: current project evidence also shows that nominative `*brándaz` itself now gives regular OE `brand` (`DEV_NOTES.md:38129-38132`, confirmed by manual probe).

That means the row is no longer in the same position as cases where only an oblique cell yields the desired OE form. For `brand`, the repo now contains evidence for **both** a regular citation-form derivation (`*brándaz -> brand`) and the selected gen.sg. derivation (`*brándas -> brandes`).

## Old English philology

Repo-local philology supports the **citation lexeme** `brand` much more clearly than the exact target `brandes`.

- **Etymological dictionaries:** Orel and Seebold both give OE `brand` from PGmc `*brandaz`.
- **Old English lexica:** Clark Hall gives headword `brand`; Bosworth-Toller gives `brand/brond` and cites inflected forms such as `brandas`, `branda`, and `brandum`.
- **Supplementary lexical table:** `old_english_wiktionary.tsv` likewise gives only `brand`.

I did **not** find a repo-local citation for exact **`brandes`**. So if the current row is kept, `brandes` should be described as a regular/inferred OE gen.sg. cell, not as the dictionary headword and not as a directly documented exact form in the materials checked.

Philologically, then, the safest distinction is:

- **citation/headword:** `brand`;
- **documented inflectional background:** the noun clearly had ordinary oblique forms (`brandas`, `branda`, `brandum`, etc.);
- **current project target:** `brandes`, which is morphologically plausible but not directly supported in the checked repo sources with the same strength as `brand`.

## Project problem and solution

The project history appears to be: during the February 2026 A-restoration/gen.sg. debugging phase, the row was moved from citation `brand` to gen.sg. `brandes`, parallel to `hammer` and `swan`. That historical move is still visible in `mismatch_comparison_2026-02-06b.md`, which explicitly records the dataset update `*brandăz -> *brandas`, `brand -> brandes`.

But the present repo state is different from that debugging moment. Current evidence shows that nominative `*brándaz -> brand` is now already regular in the cascade, and the philological support in the checked reference corpus points to citation `brand`, not to exact `brandes`.

So the live row currently looks less like a necessary final solution and more like a leftover paradigm-cell workaround from an earlier debugging stage. If the project wants the lexeme-level OE row for 'brand', the strongest present solution is simply:

- keep **TSV `PROTO = *brándaz`**;
- restore **TSV `PROTOFORM = *brándaz`**;
- restore **TSV `COUNTERPART = brand`**;
- treat the row as a regular citation-form derivation rather than as an oblique-cell workaround.

If the team intentionally wants to preserve a separate gen.sg. row, then the current labeling should at least admit that this is a **paradigm-cell** choice and not an upstream `early_analogy` stem-reshaping case.

## Paradigm probe

A paradigm probe **is required to audit the current row**, because the row is presently using a paradigm-cell workaround rather than a straight lexeme-to-lexeme mapping.

The decisive contrast has already been checked manually:

- **nom.sg.** `*brándaz -> brand`
- **gen.sg.** `*brándas -> brandes`

There is still **no built-in row-specific probe spec** in `oe_paradigm_probe.py`, so the formal saved probe is missing. If the current paradigm-cell analysis were to be kept, the minimum saved probe should cover:

- **nom.sg.** `*brándaz`
- **gen.sg.** `*brándas`

No larger probe is needed before making the present memo recommendation, because those two cells already show that the citation-form derivation works and that the gen.sg. solution is optional rather than forced.

## Recommended final report

Recommend **not** drafting the final `### Lexeme report` until the row-level data decision is made. Preferred outcome: normalize the row back to regular `*brándaz -> brand`, in which case no special final lexeme report would be needed. If the current `brandes` row is retained, the final report should be brief and should state explicitly that `PROTO` is the lexeme headword, `PROTOFORM` is a selected gen.sg. cell, and exact `brandes` is only an inferred OE target in the checked repo evidence.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** **change recommended** — preferred fix is to revert from `*brándas` to citation-form `*brándaz`.
- **TSV `COUNTERPART`:** **change recommended** — preferred fix is to revert from `brandes` to `brand`.
- **TSV `DERIVATION_CLASS`:** **change recommended** — preferred fix is `regular`, because the current FST now derives `*brándaz -> brand` directly. If the team nevertheless keeps `brandes`, the fallback class should be `late_analogy`, not `early_analogy`.
- **TSV `NOTE`:** **change recommended** — either remove the current gen.sg. workaround note if the row is normalized back to `brand`, or rewrite it to say clearly that `brandes` is a selected/inferred gen.sg. cell rather than a directly evidenced citation form.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** **change recommended** — the February 2026 brand/brandes workaround history in `mismatch_comparison_2026-02-06b.md`, plus broader background writeups such as `weak_tail_vowels_and_a_restoration.md` and `analogical_leveling_analysis.md`, should be marked more clearly as historical debugging context so future packets do not over-treat the `brandes` workaround as settled final policy.
