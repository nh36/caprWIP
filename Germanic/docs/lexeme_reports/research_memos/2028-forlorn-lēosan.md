# Research memo — 2028 forlorn / lēosan

## Starting point

- **ID:** 2028
- **CONCEPT:** forlorn
- **COUNTERPART:** `lēosan`
- **PROTO:** `*léusaną`
- **PROTOFORM:** `*léusaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Du verliezen / G verlieren are also prefixed forms of this verb.`

The live row is currently regular in derivational terms, but the note and row history show a headword-selection problem: the row was changed from prefixed past participle `forloren` to bare infinitive `lēosan` in order to match simplex `*leusan-`. The memo question is whether that de-prefixing is philologically justified for the OE row, or whether the row should instead model the prefixed OE lexeme that actually underlies English `forlorn`.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row and compact derivation trace are current evidence for what the project presently models: `*léusaną > lēosan`, with matching `EXPECTED` and `OUTPUTS`. `coverage_audit.md` also confirms that this note-bearing regular row still needs lexeme-report treatment.
- **Useful background:** the packet’s own `old_english_wiktionary.tsv` hit `forlorn = forloren` is useful because it points to the directly relevant OE participial form behind the English adjective. The row history is likewise useful because it records the exact project move from `forloren` to `lēosan`.
- **Stale or superseded:** the packet itself has no dedicated dossier material, but wider repo history preserves an older diagnostic stage where `forloren` was being treated as the expected OE target. Those mismatch snapshots are project history, not current live row authority.
- **Irrelevant or misleading if over-read:** the packet can make the present row look philologically settled simply because the FST now matches `lēosan`. But the packet’s strongest lexical-table evidence actually points to `forloren`, not to bare `lēosan`. The history note’s appeal to “Kroonen *leusan-” is also incomplete: Kroonen’s OE daughter evidence for this etymon is `for-lēosan`, not an unprefixed simplex [@Kroonen2013].

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` — no row-specific discussion of this lexeme.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto.
- `Germanic/docs/non_firing_rules_analysis.md` line 419 — older diagnostic `*leusăną -> lēosan (expected forloren)`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` — confirms row 2028 is report-required and currently uncovered.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — Kroonen gives PGmc `*leusan-` but cites OE `for-lēosan`, not bare `lēosan` [@Kroonen2013].
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — Orel likewise gives OE `for-leósan` under prefixed comparative evidence [@Orel2003].
- `docs/references/ringe_vol1_pie_to_pgmc.txt` — Ringe states that `*fraleusaną` “never lacks its prefix *fra-” in the daughters, and elsewhere lists OE `forlēosan` under prefixed WGmc evidence [@Ringe2006].
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — gives the OE strong-verb paradigm `forléosan, forléas, forluron, forloren` [@RingeTaylor2014].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — has `forleosan` and `forloren`, but no standalone dictionary headword here for `lēosan` [@ClarkHall1960].
- `docs/references/sweet_anglo_saxon_primer.txt` — lists `forleosan` as the class paradigm form.
- `docs/references/bright_anglo_saxon_reader.txt` — uses `(for)leosan`, showing a pedagogical de-prefixing convention rather than firm lexical-table proof of an independent row target.
- `docs/references/bammesberger_1990_morphologie.txt` and `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` — both use `lēosan` in comparative/family discussion, so bare `lēosan` does exist as a scholarly family label [@Fulk2018].
- `docs/references/seebold_vergleichendes_woerterbuch.vision.txt` — explicitly warns that isolated `loren` does not justify positing a separate strong unprefixed `*lēosan`/`lēoran` verb from OE evidence alone.
- `Germanic/data/old_english_wiktionary.tsv` — gives `forloren`, not `lēosan`, for this English gloss.

I found no dedicated dossier and no existing pilot/full lexeme report for this item.

## Reconstruction and early-stage forms

Three levels need to be kept separate here:

1. **Current TSV cognate-set proto / project input:** `*léusaną`, i.e. the simplex verbal etymon presently used by the row.
2. **Comparative lexicalized verb behind the daughter set:** repo-local comparative sources repeatedly treat the inherited “lose” verb as prefixed `*fraleusaną`, with OE `forlēosan`, Gothic `fraliusan`, and OHG `farliosan`/`firliosan` [@Ringe2006; @Orel2003; @Kroonen2013].
3. **Direct OE form behind English `forlorn`:** not the bare infinitive, but the prefixed lexeme `forlēosan`, especially its past participle `forloren`.

So the live row’s `PROTO = PROTOFORM = *léusaną` is best understood as a **de-prefixed project normalization**, not as the strongest available comparative statement for this particular lexeme. The simplex base `*leus- / *leusan-` remains important etymological background, but the row’s actual cognate set is centered on a lexicalized prefixed verb.

## Old English philology

The philological evidence inside the repo is much stronger for **prefixed** OE material than for an independent simplex row target:

- `forlēosan` is the ordinary paradigm form in local grammar/reference dumps [@RingeTaylor2014; @ClarkHall1960].
- `forloren` is the directly relevant attested past participle/adjectival form behind English `forlorn`.
- `old_english_wiktionary.tsv` supports `forloren`, not `lēosan`.

Bare `lēosan` is not wholly invented: Fulk and Bammesberger use it in comparative discussion, and Bright’s `(for)leosan` shows that scholars sometimes cite the verb with optional prefix. But that is weaker than a dictionary-style headword or lexical-table match for this row. In other words, `lēosan` is supportable as an **etymological or pedagogical family label**, not as the best-supported direct OE counterpart for concept `forlorn`.

There is also a headword caution. Seebold and Campbell treat isolated `loren` material as insufficient to prove an independent strong simplex verb distinct from the prefixed family; that prevents the project from using stray `loren` evidence to strengthen the case for a standalone OE target `lēosan` [@Campbell1959].

## Project problem and solution

The project issue here is not a sound-law failure. The live derivation `*léusaną > lēosan` is regular.

The real issue is that the row seems to have been corrected from one over-specific target to another:

- **old target:** `forloren`, which was too specific as a participial cell;
- **current target:** `lēosan`, which solves the participle problem by stripping away the very prefix that comparative and lexical evidence treat as integral to this lexeme.

The best project solution is therefore:

1. keep the idea that the row should use a **citation-form verb**, not a participial cell;
2. restore the lexeme’s prefixed status by modelling **`forlēosan`**, not bare `lēosan`;
3. if the row is updated, align TSV `PROTO` and `PROTOFORM` to prefixed **`*fraléusaną`** rather than simplex `*léusaną`.

That keeps the row regular while matching the actual lexicalized daughter evidence much better. If the project deliberately chooses to keep the de-prefixed normalization for cross-row reasons, the final report must say so explicitly and must not present `lēosan` as the straightforward attested OE counterpart of `forlorn`.

## Paradigm probe

A paradigm probe is **not required** for the main recommendation.

This is not a late-analogy or hidden-cell case. The central decision is whether the row should target the prefixed infinitive `forlēosan` or the de-prefixed normalization `lēosan`, not whether one special inflectional cell must be substituted to rescue the derivation.

If the team later wants a purely illustrative probe for the prefixed verb family, the useful cells would be:

- infinitive `forlēosan`;
- preterite singular `forlēas`;
- preterite plural `forluron`;
- past participle `forloren`.

But that would be optional exposition, not a prerequisite for the memo’s recommendation.

## Recommended final report

Recommend a short final report stating that the live row currently models regular simplex `*léusaną > lēosan`, but that the stronger comparative and OE lexical evidence for this cognate set is the prefixed verb `forlēosan`, with English `forlorn` continuing the past participle `forloren`. If the TSV is updated, the final report should treat `forlēosan` as the OE target and mention `forloren` as the direct source of the English adjective.

## Data-change recommendations

- **TSV `PROTO`:** **change recommended** — prefer prefixed `*fraléusaną` if row 2028 is meant to model the lexicalized “lose/forlorn” verb family rather than the abstract simplex base.
- **TSV `PROTOFORM`:** **change recommended** — same recommendation as `PROTO`; keep it aligned with prefixed `*fraléusaną`.
- **TSV `COUNTERPART`:** **change recommended** — prefer `forlēosan` over bare `lēosan`. This preserves citation-form status without reverting to over-specific participial `forloren`.
- **TSV `DERIVATION_CLASS`:** no change recommended; this should remain `regular` if the row is moved to prefixed infinitive `forlēosan`.
- **TSV `NOTE`:** **change recommended** — the note should say explicitly that English `forlorn` reflects OE `forloren`, that Dutch/German and the strongest OE evidence are prefixed, and that the previous appeal to Kroonen does not by itself justify bare `lēosan` as the OE target.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` or dossier text:** no change recommended. There is no dedicated row-specific dossier or `DEV_NOTES` section to revise. Older diagnostic material such as `non_firing_rules_analysis.md` is best treated as stale history rather than as something needing row-specific cleanup.
