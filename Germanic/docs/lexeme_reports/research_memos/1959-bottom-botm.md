# Research memo — 1959 bottom / botm

## Starting point

- **ID:** 1959
- **CONCEPT:** bottom
- **COUNTERPART:** botm
- **PROTO:** *búdmaz
- **PROTOFORM:** *búttmaz
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Kroonen p.82: OE < *buttma- (oblique stem variant via PIE dissimilation)

The live TSV already treats this as an early analogical-stem selection, not as a straight inherited run from the cognate-set proto. A pilot report exists at `Germanic/docs/lexeme_reports/pilot/bottom.md`, but it is background only, not final authority.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing `*búttmaz -> botm`; the exact-pair `DEV_NOTES.md` hits at 1025-1238 and 29887-29893; and the control-style note at 42113-42115 showing that the current cascade already treats `*búttmaz -> botm` as a working derivation.
- **Useful background:** `pilot/bottom.md`; the packet’s report-manifest notice that a pilot exists; `old_english_wiktionary.tsv` listing `botm`; and the packet’s bibliography suggestions pointing toward Kroonen, Campbell, Orel, and Kluge-Seebold.
- **Stale or superseded:** the packet’s diagnostic implementation-history note at `DEV_NOTES.md:1314`, which is useful chronology but not current evidence; and the packet’s “possibly stale or diagnostic” concept-only hits, which are not row-specific proof.
- **Irrelevant or misleading:** broad concept-word hits such as unrelated “bottom line” headings; and any attempt to treat the packet alone as sufficient authority for the PIE/PGmc reconstruction question.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 1025-1238, 1299-1316, 29887-29893, and 42113-42115.
- `Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md` at 403-425 and 446-452.
- `Germanic/docs/lexeme_reports/pilot/bottom.md`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/docs/lexeme_reports/report_manifest.tsv` and `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.

This extra pass matters because the packet foregrounds the early-analogy problem, while the later medial-`u` dossier shows that `botm` is only partial evidence for the separate `u`-before-`m` conditioning question: its medial vowel is better treated as epenthetic/nuclearizing material, not as a clean inherited unstressed `*u` test case.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*búdmaz` is the project’s lexeme-level headword shorthand. Repo reference material is more specific: Kroonen gives `*budmō, gen. *buttaz` and also summarizes the stem complex as `*budman- ~ *buttman-`. So the live `PROTO` is not meant as the exact philological citation Kroonen would print.
2. **Project input form for derivation:** TSV `PROTOFORM` `*búttmaz` is the modelable pre-OE input chosen for the row. It is the project’s normalized way of encoding Kroonen’s stem variant `*buttma-`, i.e. a nominative-like input carrying the analogically generalized oblique root `*butt-`.
3. **OE target form:** `botm` is the attested Old English target represented by the row.

The reconstruction logic in `DEV_NOTES` is coherent. The inherited PGmc paradigm had a nominative-side `*budm-` and an oblique `*butt-`; Old English belongs with the languages that generalized the oblique consonantism while retaining the nominative `-m-` material, yielding pre-OE `*buttma-` and then regular OE `botm`. That is why `PROTOFORM` differs from `PROTO`: the row is not claiming two rival cognate-set protos, but separating etymological headword from derivational input.

## Old English philology

`botm` should be treated as an ordinary attested OE lexeme, not as a reconstructed West-Saxon convenience form and not as a paradigm-cell substitute. `old_english_wiktionary.tsv`, Clark Hall, and Bosworth-Toller all give `botm`; Bosworth-Toller also cross-references `bodan`, showing that the lexical history is broader than a single normalized spelling, but the row’s target `botm` itself is solid.

The philological issue here is therefore not attestation but prehistory. `DEV_NOTES` is right to separate the OE `t` from Campbell’s later WS `pm > tm` discussion: the decisive point for this row is the older analogical spread of `*butt-`, not a late OE hardening trick. The later `dossier-medial-u-lowering-conditioning-2026.md` adds an important caution: `botm` behaves like other epenthetic-vowel cluster cases and should not be overused as primary evidence for the independent medial-`u` conditioning dossier. That does not weaken the row’s `PROTOFORM`; it only limits what one should infer from `botm` for other sound laws.

## Project problem and solution

The original project problem was that a direct run from the cognate-set form with voiced dental produced the wrong OE outcome (`bodm`), whereas the target lexeme has `t`. The current solution is the right type of solution: keep the cognate-set proto separate, but feed the OE derivation from the analogically levelled stem `*búttmaz`, reflecting Kroonen’s `*buttma-`.

So the row should be understood as follows: the project is modelling an **attested OE lemma** whose pre-OE history already includes paradigmatic leveling. This is why the row belongs in `early_analogy`, not `late_analogy`, and why the special move belongs in `PROTOFORM` rather than in an OE-side paradigm-cell probe.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` row where the project must choose among OE inflectional cells such as nom.sg. vs gen.sg. The decisive contrast is upstream: cognate-set `*búdmaz` versus derivational `*búttmaz`. If a future audit wants an illustrative control, a simple comparison of those two inputs is enough; no missing OE paradigm cells need to be probed for the memo stage.

## Recommended final report

Recommend a concise final report that says row 1959 targets attested OE `botm`, while distinguishing lexeme-level `PROTO = *búdmaz` from derivational `PROTOFORM = *búttmaz`, the project’s normalized reflex of Kroonen’s pre-OE `*buttma-` with oblique-stem `*butt-` generalized into the nominative formation.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended for now. It is a project headword shorthand, even if Kroonen’s fuller citation is `*budmō, gen. *buttaz` / `*budman- ~ *buttman-`.
- **TSV `PROTOFORM`:** no change recommended; `*búttmaz` correctly captures the intended derivational input.
- **TSV `COUNTERPART`:** no change recommended; `botm` is the right OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended; `early_analogy` is correct.
- **TSV `NOTE`:** minor editorial change **is recommended**. The present note is basically right, but it should more explicitly distinguish the cognate-set proto from the derivational input and say that `*buttma-` reflects analogical spread of the oblique `*butt-` onto the nominative `-m-` stem material, not just “PIE dissimilation” in isolation.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES/dossier text:** at most light cleanup/cross-referencing is recommended. The main early-analogy section is still useful, but it would help future packeting if it explicitly pointed readers to `dossier-medial-u-lowering-conditioning-2026.md` so `botm` is not over-read as a clean inherited-`u` control case.
