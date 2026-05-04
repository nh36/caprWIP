# Research memo — 2119 man / mannes

## Starting point

- **ID:** 2119
- **CONCEPT:** man
- **COUNTERPART:** mannes
- **PROTO:** *mánnaz
- **PROTOFORM:** *mánnas
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** Gen.sg. paradigm cell: *mannas → mannes. Word-final geminates are phonologically simplified (Kurath 1956, Brunner §231); using gen.sg. preserves medial geminate orthographically.

The live TSV already treats this as a paradigm-cell row rather than a lemma-to-lemma row. No pilot report exists for `man / mannes`, so the packet and repo sources need to carry the evidential load directly.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*mánnas -> mannes`; and the `DEV_NOTES.md` material at 13645-13803 plus 25306-25310, which records the shift from nominative-style targeting to the gen.sg. paradigm-cell solution and treats `mannes` as one of the project's methodological precedents.

**Useful background:** the packet's excerpts on final-geminate simplification and unstressed-fronting behavior; the packet's diagnostic preservation of the older row state `*mannăz -> mann`; and the packet's local lexical-table hits showing that supplementary dictionaries still index the lexeme under citation-form `mann`.

**Stale or superseded:** the packet includes older development history in which row 2119 still targeted nominative `mann`. That history is useful diagnostically, but it is not the current row. Within the packet's own `DEV_NOTES` excerpts, the earlier illustrative form `*mannăs -> mannes` is superseded by the later explicit correction that the selected gen.sg. input must use full `*a`, i.e. `*mannas`, not breve `*ă`.

**Irrelevant or misleading:** packet hits about OE `wer` 'man' and broader `i > e` discussions concern a different lexeme, not row 2119. Likewise, lexical-table headwords `mann` and `wer` are useful for citation-form orientation but do not by themselves settle the row's selected inflected target `mannes`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/prosodic_tier_research.md` — records `*mannas -> mannes` as the standing workaround for paradigm-cell geminates.
- `Germanic/data/oe_known_problems.tsv` — no entry for this row/proto.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/old_english_swadesh.tsv` — both give citation-form `mann`, confirming the headword/inflected-cell distinction.
- `Germanic/tools/oe_paradigm_probe.py` — no built-in probe spec exists for `man / mannes`.
- Manual FST probe run during this memo: `*mannăz -> man`, `*manną -> man`, `*mannăi -> manne`, `*mannas -> mannes`.
- `docs/references/campbell_old_english_grammar.txt` — gives the root-noun paradigm `mann/man, mannes, menn, manna, mannum` and notes that the gen.sg. is taken over from the a-declension.
- `docs/references/brunner_1965_altenglische_grammatik.txt` — cites `man mannes` as a geminate example and explicitly treats final simplification (`man ... monnes`) as the normal pattern behind analogical double spellings.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — treats the lexeme at a broader comparative level as PGmc `*mann- > OE mann ~ monn`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — gives a more complicated lexeme-level reconstruction `*mannan-` and discusses an analogical paradigm with gen. `*mannaz`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — gives a simplified lexeme citation `*mannz`, OE `mann`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `mann`.

No separate full dossier file for this lexeme was identified beyond the packet and the general methodological notes above.

## Reconstruction and early-stage forms

This row needs a three-way distinction kept explicit:

1. **Cognate-set proto / project citation form:** TSV `PROTO` is `*mánnaz`, the row's lexeme-level label. Repo reference works show that the larger reconstruction is not perfectly uniform: Kroonen prefers `*mannan-`, Orel gives `*mannz`, and Ringe-Taylor cite PGmc `*mann-`.
2. **Project derivational input:** TSV `PROTOFORM` is `*mánnas`, i.e. the selected PGmc **gen.sg.** cell. In FST-normalized spelling this is `*mannas`, and `DEV_NOTES` is explicit that the vowel must be full `*a`, not breve `*ă`, so that unstressed fronting can yield `-es`.
3. **OE target form:** `mannes`, likewise a **gen.sg.** form, not the citation lemma.

So the important contrast is not between two rival OE outputs, but between two different project levels: lexeme-level `PROTO` versus the cell actually fed to the FST. The older nominative-style input `*mannăz` is still useful as a diagnostic control, because it shows why the row was changed: it yields `man`, not `mannes`.

## Old English philology

Philologically, the row is stronger than a mere ad hoc reconstruction.

- **Citation/headword:** supplementary lexical tables and Clark Hall give `mann`; Ringe-Taylor also frame the OE lexeme as `mann ~ monn`.
- **Selected inflected cell:** Campbell's paradigm explicitly includes gen.sg. `mannes`, and Brunner likewise cites `man mannes` / `monnes` in the discussion of gemination and final simplification.
- **Attested vs reconstructed:** `mannes` is therefore supported in repo-local reference grammars as a real OE paradigm form, not just an invented project output. But the current repo evidence is grammatical/lexicographic rather than a row-specific manuscript dossier, so the final report should not attach unsupported dialect or manuscript claims to the exact form.
- **Dictionary/headword issue:** the row's `COUNTERPART` is not the lexicographic lemma. It is an inflected singular cell chosen because it preserves medial `nn`, whereas the citation form participates in the well-known `mann/monn` and final-geminate simplification problem.

## Project problem and solution

The project problem is the mismatch between lexeme headword practice and OE final-geminate phonology. If the row targeted the nominative/citation input, the FST gives `man` from `*mannăz`, and even the acc.sg. control `*manną` also gives `man`. That is phonologically regular under the final-geminate analysis preserved in `DEV_NOTES`, Campbell, and Brunner.

The project solution is therefore to represent the lexeme through the conservative **gen.sg.** cell `*mannas -> mannes`, where the geminate remains medial and the unstressed ending develops regularly to `-es`. The row is thus best read as: "the OE man-lexeme, represented by its gen.sg. paradigm cell," not as a claim that the dictionary headword is `mannes`.

## Paradigm probe

A paradigm probe **is required** for this row, because the whole rationale of the entry is the contrast between citation-form input and selected paradigm-cell input.

The repo does **not** yet have a built-in `oe_paradigm_probe.py` spec for `man / mannes`, so the formal saved probe is still missing. The minimum cells that should be probed are:

- **nom.sg.** `*mannăz -> man`
- **acc.sg.** `*manną -> man`
- **dat.sg.** `*mannăi -> manne`
- **gen.sg.** `*mannas -> mannes`

A manual probe already confirms those outputs, and it shows that the gen.sg. is the uniquely relevant winning cell for the current target. Plural cells would be optional completeness work, not a blocker for the final report.

## Recommended final report

Recommend a concise final report that says row 2119 keeps lexeme-level `PROTO` `*mánnaz` but uses gen.sg. `PROTOFORM` `*mánnas`/`*mannas` to derive OE `mannes`, because final geminates simplify in citation-form position while medial geminates survive in the oblique cell. It should note that `mannes` is supported by standard OE grammatical paradigms, while avoiding any stronger manuscript/dialect claim and avoiding presentation of the TSV `PROTO` as the only possible handbook reconstruction.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended for now. Reference works vary (`*mannan-`, `*mannz`, `*mann-`), but this memo does not establish a single replacement that should override the project's current citation label.
- **TSV `PROTOFORM`:** no change recommended; `*mánnas` / normalized `*mannas` is the correct selected gen.sg. input.
- **TSV `COUNTERPART`:** no change recommended; `mannes` is the right target for the row's chosen paradigm cell and is supported in repo-local reference grammars.
- **TSV `DERIVATION_CLASS`:** no change recommended; `late_analogy` still matches the paradigm-cell solution.
- **TSV `NOTE`:** **change recommended** — tighten it so it explicitly distinguishes citation-form `mann` from selected gen.sg. `mannes`, and so it notes that the input must be full `*mannas`, not the older illustrative `*mannăs` spelling.
- **`oe_known_problems.tsv`:** no change recommended; this row is not a live mismatch or an unmodelled exception.
- **DEV_NOTES / dossier text:** **change recommended** in `DEV_NOTES.md` to clean up the stale `*mannăs -> mannes` example and to keep pre-update `*mannăz -> mann` material clearly marked as historical diagnostics rather than current row analysis. No separate lexeme-specific dossier was found, so no additional dossier cleanup is currently identifiable.
