# Research memo — 2272 wash / wascan

## Starting point

- **ID:** `2272`
- **CONCEPT:** `wash`
- **COUNTERPART:** `wascan`
- **PROTO:** `*wáskaną`
- **PROTOFORM:** `*wáskaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1 | Medial sc before back vowel: not palatalized in early OE (Campbell §440); wascan [sk] is the conservative form.`

This is the ordinary OE lemma row for 'wash'. The live row already frames the problem as a combination of A-restoration and conservative medial `sc` before a back-vowel tail, not as a paradigm-cell or analogical-selection issue.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation `*wáskaną -> wascan`; the exact-pair `DEV_NOTES` hit at `30637`, which correctly classifies `wascan` as an `sC`-cluster A-restoration case; and the packet's Campbell/Luick quotations in `analysis/arestoration_r_l_research.md`, which explicitly include `wascan` among the canonical `sC` examples.
- **Useful background:** the packet's March 2026 `DEV_NOTES` dry-run material (`9504`, `9512`, `9538`) is useful for project chronology, because it shows why `wash` kept surfacing during A-restoration debugging; the `old_english_swadesh.tsv` background hit (`þwēan, wascan`) is also useful for reminding us that `wash` had more than one OE lexical expression.
- **Stale or superseded:** the packet's lexical-table hit `wash -> wasċan` from `old_english_wiktionary.tsv` is supplementary only and should not outrank the live row plus handbook evidence for conservative `wascan`; older debug snapshots that expected `wasċan` and output `wæsċan` are likewise superseded project history, not current lexical authority. The March 2026 proposal to rewrite the input as `*waskăną` belongs in the same diagnostic bucket: it explains an abandoned debugging path, not the current canonical row.
- **Irrelevant or misleading:** generic table-of-contents hits for A-restoration, concept-only lines such as `Fixed: 6 ( ... wash ...)`, and other non-row-specific mentions are not lexical evidence for row `2272`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at `3138-3151`, `9218-9539`, `21738-21950`, `30637`, and `36561-36574`.
- `Germanic/docs/analysis/arestoration_r_l_research.md` at the Campbell and Luick quotations (`77-87`, `208-220`).
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv`.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `docs/references/campbell_old_english_grammar.txt` (`11476-11484`).
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` (`7594-7596`, `11772-11780`, `13481-13483`).
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` (`47118-47119`).
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` (`15964-15989`).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` (`29170-29173`) and `docs/references/orel_handbook_germanic_etymology.vision.txt` (`49670-49673`).
- Current live probe of `old_english.bin`, which returns `*wáskaną -> wascan`.

Main findings from the extra check:

- Repo-local handbook evidence strongly supports `wascan` as the conservative OE lemma for this row's target environment.
- Lexicographic material also preserves variant history: `Clark Hall` heads the verb under `wascan` while noting `æ` and `x` variants; `Brunner` likewise lists `wascan, wæscan`.
- `Ringe/Taylor` explicitly describe medial `*sk` as non-palatalized before a following back vowel, matching the row note and supporting `wascan` rather than a normalized `wasċan` as the row target.
- No wash-specific dossier, pilot report, or `oe_known_problems.tsv` entry was found.

## Reconstruction and early-stage forms

Three levels need to remain distinct.

1. **Cognate-set proto / comparative etymon:** comparative sources cite the verb as PGmc `*waskan-` / `*waskanan` (Kroonen, Orel), i.e. the cognate set behind OE `wash`, OS `waskan`, OHG `wascan`, etc.
2. **Project input form for this row:** the current TSV uses accented `*wáskaną`. In current project chronology that plain suffix vowel is part of the engineering input that lets A-restoration fire for this Class VI infinitive.
3. **OE target represented by the row:** conservative OE `wascan`, not the project's internal proto input and not an automatically normalized `wasċan` spelling.

For the early OE phonological staging, the packet's derivation is consistent with the handbook evidence: fronting gives an intermediate `*wæskaną`, and A-restoration before the `sC` cluster plus back-vowel tail returns `*waskaną`, yielding OE `wascan`. The March 2026 debugging form `*waskăną` should be treated only as an experimental project input, not as the row's preferred reconstruction now that the live row and live FST both use and support `*wáskaną`.

## Old English philology

- **Attested/citation-form side:** repo-local reference works support `wascan` as a real OE lemma/headword. `Clark Hall` gives `wascan` and notes variant spellings; `Brunner` explicitly lists `wascan, wæscan`.
- **Variant and normalized forms:** `wæscan` is a real variant in the lexicographic tradition, and `old_english_wiktionary.tsv` gives `wasċan`; but neither of those should automatically replace this row's target. For row `2272`, the decisive phonological point is the conservative infinitive environment with back-vowel-following medial `sc`.
- **Phonology of `sc`:** Campbell and `Ringe/Taylor` both support the row note's basic claim: medial `sk/sc` is not palatalized here when a back vowel follows, so `wascan` with conservative `[sk]` is the right project target for the lemma row.
- **Broader verbal family:** `old_english_swadesh.tsv` lists both `þwēan` and `wascan` for 'to wash', and `Ringe/Taylor` mention a late non-strictly-WS `3sg wescep`. Those are relevant family background, but they do not change the lemma row's target.

So the final report should say clearly that `wascan` is the row's conservative citation form, while `wæscan`, `wasċan`, and other family variants belong to secondary philological background.

## Project problem and solution

The project problem here has two layers.

1. **A-restoration encoding history:** older `DEV_NOTES` sections disagree about whether these Class VI infinitives should use plain `-aną` or experimental `-ăną`. For row `2272`, current project authority is the live TSV plus live FST output: `*wáskaną -> wascan`.
2. **Headword/normalization drift:** older snapshots and the supplementary Wiktionary table pull toward `wasċan` / `wæsċan`, but the row note and the stronger handbook evidence point to conservative `wascan` with non-palatalized medial `sc` before the back-vowel tail.

The right project solution is therefore conservative and narrow: keep row `2272` as the ordinary lemma row for `wascan`, keep the current `regular` classification, and treat `*waskăną` or `wasċan` expectations as superseded debugging/normalization history rather than as reasons to rewrite the live data row.

## Paradigm probe

**No dedicated paradigm probe is required for row `2272` itself.** This row is not selecting an oblique cell or late-analogy cell; the live derivation, handbook quotations, and lexicographic support already establish the lemma target well enough.

If the project later wants a broader wash-family probe, the useful cells would be:

- infinitive / citation form (`wascan`);
- preterite singular (`wōsc` / variant `wox`);
- preterite plural (`wōscon`, with note of late `weoscan` where relevant);
- past participle (`wascen`);
- the late `3sg wescep` noted by `Ringe/Taylor`.

But that family-level probe is optional background work, not a prerequisite for the final lexeme report on row `2272`.

## Recommended final report

Recommend a short final report: distinguish the comparative proto etymon from the project's input `*wáskaną`, present OE `wascan` as the conservative lemma supported by A-restoration before an `sC` cluster and by non-palatalized medial `sc` before a back-vowel tail, and mention `wæscan`/`wasċan`/`wescep` only as secondary variant history or stale project-debugging background.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** no change recommended. The current note already captures the two live issues that matter: A-restoration encoding and conservative non-palatalized medial `sc`.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** change recommended for `DEV_NOTES`, not for dossier text. The conflicting March/April 2026 discussions of `-aną` vs `-ăną`, and older expectations of `wasċan`/`wæsċan`, should be marked explicitly as superseded by the current live row and live `*wáskaną -> wascan` behaviour. No wash-specific dossier text was found, so no dossier cleanup is currently needed.
