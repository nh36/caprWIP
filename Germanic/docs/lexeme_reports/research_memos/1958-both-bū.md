# Research memo — 1958 both / bū

## Starting point

- **ID:** 1958
- **CONCEPT:** both
- **COUNTERPART:** bū
- **PROTO:** *bō
- **PROTOFORM:** *bō
- **DERIVATION_CLASS:** regular
- **NOTE:** The live note says the row targets OE neuter dual `bū` rather than analogical `bēġen` or the earlier garbage target `bā]] [[þā`, and it distinguishes the unextended PGmc neuter dual `*bō` from the `*bai-þ-` stem behind ModE `both`; but the last sentence is now stale because it still says the mismatch persists pending `§17.31`.

This is a note-bearing `regular` row, so `coverage_audit.md` correctly marks it as needing eventual lexeme-report coverage. I found no existing pilot or full lexeme report for `both`.

## Packet evidence assessment

**Authoritative/current**

- The live TSV row and the packet’s compact derivation trace are current evidence for what the project now models: `*bō -> bū`.
- `DEV_NOTES.md` `§17.30` is still the main project dossier for why the row was retargeted from Wiktionary garbage to attested OE `bū`.
- `DEV_NOTES.md` 37749-37753 is decisive current status evidence: the `§17.31` fix landed and row 1958 now passes.

**Useful background**

- The packet’s attestation table from Brunner, Campbell, and Fulk is useful and should be retained as philological background: masc. `bēġen`, fem. `bā`, neut. `bā, bū`, with gen. `bēġra/bēġ(e)a` and dat. `bǣm`.
- Kroonen’s entry is important background for the three-way distinction: original PGmc paradigm `*bai, *bans, *bōz/*bōns, *bō`, with OE `bēġen` treated as analogical and OE `bū` as the inherited neuter form.
- The packet is also right that ModE `both` belongs with the extended `*bai-þ-` series, not directly with the OE row’s target.

**Stale or superseded**

- The packet preserves the live TSV note verbatim, including the outdated sentence that the row still mismatches pending `§17.31`; that is superseded by `DEV_NOTES.md` 37751-37753.
- The old `old_english_wiktionary.tsv` form `bā]] [[þā` is only diagnostic project history from bad template extraction, not current OE evidence.
- Earlier `DEV_NOTES.md` 37362-37377 predictions about the mismatch remaining open are now historical chronology only.

**Irrelevant or misleading if over-read**

- The packet has no dedicated analysis/dossier hit beyond `DEV_NOTES`; that absence should not be mistaken for lack of evidence, because the philological evidence is in the reference files.
- The supplementary lexical-table hit `both = bā]] [[þā` is actively misleading if weighted like dictionary or grammar evidence.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around 37222-37390 and 37749-37753.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which flags row 1958 as report-worthy because `NOTE` is non-empty.
- `Germanic/data/oe_known_problems.tsv`, which has no entry for row 1958 or `*bō / bū`; that now makes sense because the `§17.31` FST issue was closed.
- `Germanic/data/old_english_wiktionary.tsv`, which confirms that the earlier target came from bad Wiktionary-template extraction rather than from a usable OE lemma.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt` 13207-13217.
- `docs/references/campbell_old_english_grammar.txt` 4029-4045 and 18919-18953.
- `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` 15594-15600 and 15632-15667.
- `docs/references/legacy/etymological_dictionary_of_proto_germanic_kroonen.txt` 4678-4694.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` 4365-4375 and `docs/references/hogg_vol1.txt` 4760-4765 for general monosyllable-weight/word-final-vowel background relevant to the old `§17.31` problem.

I did **not** find a separate row-specific dossier or analysis file named in the packet or TSV note beyond the `DEV_NOTES` dossier section itself.

## Reconstruction and early-stage forms

This row needs three levels kept sharply apart.

1. **Cognate-set proto / etymological headword:** TSV `PROTO = *bō`. For this OE row, that is the unextended inherited neuter dual within Kroonen’s broader PGmc paradigm `*bai, *bans, *bōz/*bōns, *bō`.
2. **Project input form used for derivation:** TSV `PROTOFORM = *bō`. Unlike rows such as `cow`, there is no separate oblique-cell or alternate-form input in the live row.
3. **OE target form represented by the row:** attested OE neuter dual `bū`.

That must be distinguished from two different background formations:

- **`bēġen`**: an attested OE masculine form, but synchronically and historically more complex. Brunner/Orel/Fulk preserve the older `*bō-jen-` analysis, while Seebold objects and Kroonen instead treats `bēġen` as analogical, with `-en` remodelled after `twēġen`.
- **ModE `both` / continental `beide`-type forms**: these belong to the extended `*bai-þ-` series and should not be collapsed into the OE row’s derivational input.

So the row’s present `*bō -> bū` analysis is not claiming to solve the entire cognate set with one proto-shape. It is a row-specific choice to model the inherited OE neuter form.

## Old English philology

`bū` is **attested**, not reconstructed. The repo-local grammatical sources support a dual paradigm with:

- masc. `bēġen`
- fem. `bā`
- neut. `bā, bū`
- gen. `bēġra, bēġ(e)a`
- dat. `bǣm`

They also record compound numeral constructions such as `bā twā`, `bū tū`, and `bām twām`, sometimes written together (`būtwū`, `būtā`). That matters because the row target is not a generic dictionary headword in the modern sense; it is a specific nominative/accusative neuter dual paradigm form.

Philologically, the project should therefore avoid saying that OE had only `bēġen` or that `bū` is merely reconstructed from sound law. The evidence supports `bū` directly. At the same time, the row should not pretend that `bū` is the whole OE paradigm: `bēġen` and `bā` remain real attested partner forms, and the analogical status of `bēġen` is a historical explanation, not a denial of its attestation.

I found no reason to make this a dialect-specific or manuscript-specific row. Brunner’s dialectal notes are useful background, but the live row is simply targeting the inherited OE neuter dual form.

## Project problem and solution

The project had two separate problems, and the memo should keep them separate.

1. **Bad target selection:** the older row target `bā]] [[þā` was Wiktionary extraction garbage, not a defensible OE counterpart.
2. **A real but now-fixed FST issue:** after the row was retargeted to `bū`, the cascade still gave short `bu` until `§17.31` fixed stressed-monosyllabic final `*ō`.

The current project solution is coherent:

- keep `COUNTERPART = bū`;
- keep `PROTO = PROTOFORM = *bō`;
- keep `DERIVATION_CLASS = regular`;
- explain that `bēġen` is real OE evidence but not the row’s modelling target;
- explain that ModE `both` belongs to the Norse-/article-extended `*bai-þ-` history, not directly to this OE target.

What is now wrong is not the row design but the stale wording of the TSV note, which still describes the pre-`§17.31` mismatch state as if it were current.

## Paradigm probe

No new paradigm probe is required for the memo’s main recommendation.

This row is not waiting on a hidden cell-rescue test of the `late_analogy` kind. The decisive issues are already settled by philology and by the implemented `§17.31` closure: the row intentionally targets attested neuter dual `bū`, and the live cascade now derives it.

If a later final report wants a small explanatory probe, it should be optional and contrastive only: unextended neuter `*bō -> bū`, feminine `*bōz -> bā`, and the separate analogical/extended background represented by `bēġen` and `*bai-þ-` forms. But that would illustrate the report; it is not needed to decide the row.

## Recommended final report

Recommend a concise final report that says row 1958 deliberately models attested OE neuter dual `bū` from unextended `*bō`, distinguishes that target from analogical OE `bēġen` and from the `*bai-þ-` history of ModE `both`, and mentions the discarded `bā]] [[þā` target only as superseded extraction noise.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** Keep the core distinction between `*bō`, `bū`, `bēġen`, and ModE `both`, but remove or rewrite the stale sentence claiming that the mismatch still persists pending `§17.31`. The note should reflect that the fix landed and the row now passes.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** light cleanup recommended. `§17.30` is still useful project history, but a brief explicit cross-reference marking its predicted mismatch state as superseded by `§17.31` would reduce future packet confusion.
- **Dossier text:** no separate dossier change recommended; I found no row-specific dossier beyond the `DEV_NOTES` section itself.
