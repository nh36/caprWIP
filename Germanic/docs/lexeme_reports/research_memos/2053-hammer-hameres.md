# Research memo — 2053 hammer / hameres

## Starting point

- **ID:** 2053
- **CONCEPT:** hammer
- **COUNTERPART:** hameres
- **PROTO:** *xámaraz
- **PROTOFORM:** *xámaras
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** Note: using gen.sg. *xamaras (> hameres). Both hamor and hamer attested; hameres is the regular reflex via a-fronting (R/T §5.1.2, §6.9.6). hamores has unexplained -o- in unstressed syllable (R/T §3.1.5).

The live row is already a paradigm-cell row: the cognate-set headword is PGmc nom.sg. `*xámaraz`, but the derivational input is the gen.sg. `*xámaras`, and the OE target is the gen.sg. `hameres`.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*xámaras -> hameres`; the `DEV_NOTES.md` precedent at 39964-39969 saying hammer is one of the rows where `PROTOFORM` was intentionally switched to a paradigm cell; and `analysis/unstressed_e_o_before_r.md`, which directly argues that `hameres` is the regular neogrammarian outcome while `hamor/hamores` reflect the messy unstressed `a/o` variation.

**Useful background:** the packet's `analysis/compound_archaism_inventory.md` excerpt, which correctly treats hammer as a methodological parallel for paradigm-cell targeting; `analysis/arestoration_r_l_research.md`, which is not about hammer specifically but does confirm that the current FST already returns `hameres`; and the packet's local lexical-table hit `old_english_wiktionary.tsv: hamor`, which is useful for the citation form.

**Stale or superseded:** the packet itself is fairly clean, but it does not surface older repo history in which the row still targeted nominative `hamor` from `*xamarăz` or even proposed a different oblique-cell workaround. That older history survives elsewhere in the repo and should not be treated as current authority.

**Irrelevant or misleading:** broad packet hits for unrelated gen.sg. cases are methodological parallels only. The packet's procedural note that no built-in probe spec exists is workflow metadata, not philological evidence.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 3206-3210, 17923-17929, and 39964-39969.
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe run for this row.
- `Germanic/data/oe_known_problems.tsv` — no entry for row 2053.
- `Germanic/data/old_english_wiktionary.tsv` — gives citation-form `hamor`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — PGmc `*hamara-`, OE `hamor`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt` — OE `hamor, hamer`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — headword `hamor (o¹, e²)`, explicitly acknowledging an `e`-variant.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — direct attestation of both `hameres` and `hamor/hameron`.
- `docs/references/brunner_1965_altenglische_grammatik.txt` — paradigm citation `hamor - hamores`.
- `docs/references/hogg_vol1.txt`, `docs/references/luick_historische_grammatik.txt`, and `docs/references/kaluza_historische_grammatik_englisch.txt` — useful for the broader `hamor/hamer` and `hameres` vocalism history.
- `Germanic/docs/germanic_notes/analogical_leveling_analysis.md` and `Germanic/docs/non_firing_rules_analysis.md` — stale pre-update project history.
- No pilot lexeme report for hammer is present under `Germanic/docs/lexeme_reports/pilot/`.

The manual paradigm probe gives the decisive contrast:

- **nom.sg.** `*xámaraz -> hamer` (non-match to current row target)
- **gen.sg.** `*xámaras -> hameres` (exact match)

## Reconstruction and early-stage forms

This row needs the usual three-way distinction kept explicit:

1. **Cognate-set proto / etymological headword:** TSV `PROTO` `*xámaraz`, the PGmc masculine a-stem lexeme 'hammer'.
2. **Project derivational input:** TSV `PROTOFORM` `*xámaras`, the selected PGmc **gen.sg.** cell.
3. **OE target form:** `hameres`, likewise a **gen.sg.** form, not the citation lemma.

The current row does not claim that `*xámaras` replaced `*xámaraz` as the lexeme-level proto. It only says that the project derives this row through the genitive singular cell. That distinction matters because the FST still gives a different nominative-style outcome from the headword proto (`*xámaraz -> hamer`) than from the chosen oblique input (`*xámaras -> hameres`).

At the sound-change level, the current project analysis is coherent: the gen.sg. suffix vowel fronts and merges in unstressed position, so `*xámaras` yields `hameres`; the troublesome `-o-` forms belong to the later/unstable unstressed-vowel history, not to the regular early derivation the row is meant to capture.

## Old English philology

Repo-local philology is stronger here than the packet alone suggests.

- **Citation/headword evidence:** Kroonen gives OE `hamor`; Orel gives OE `hamor, hamer`; Clark Hall has `hamor (o¹, e²)`, so the dictionary tradition already recognizes both `o`- and `e`-vocalism in the simplex.
- **Inflected-form evidence:** Bosworth-Toller directly cites `beátendes hameres`, so exact `hameres` is attested in the repo's reference corpus. The same entry also has accusative/dative material with `hamor/hameron`.
- **Competing oblique spelling:** Brunner cites `hamor - hamores`, so `hamores` should not be described as an invented form; it is better treated as an attested but non-lautgesetzlich or later/spelling-variant `-o-` oblique beside regularized `hameres`.

So the safest philological framing is:

- **citation lemma:** `hamor`, with variant `hamer`;
- **selected project target:** `hameres`, an attested gen.sg. and the regularized outcome the project wants to represent;
- **competing variant:** `hamores`, also present in the tradition but not the regular form chosen by the row.

## Project problem and solution

The project problem is not whether OE had the word; it is which OE form the row should represent. The citation lexeme is messy: the simplex is transmitted as `hamor` and `hamer`, while the FST from lexeme-level `*xámaraz` gives `hamer`. Instead of forcing the row to choose between competing nominative spellings, the project follows the now-established oblique-cell method and represents the lexeme by a cleaner gen.sg. cell.

That solution is:

- keep **TSV `PROTO`** as the cognate-set headword `*xámaraz`;
- set **TSV `PROTOFORM`** to the gen.sg. `*xámaras`;
- target **OE `hameres`**, which the current FST derives directly and which is also directly attested in Bosworth-Toller.

`late_analogy` remains the right project label because the row is still solving an OE headword/analogy problem by choosing an oblique paradigm cell rather than the unstable citation-form tradition.

## Paradigm probe

A paradigm probe **is required** for this row, because the whole point of the entry is the contrast between lexeme-level nominative input and the selected genitive input.

The repo still lacks a built-in `oe_paradigm_probe.py` spec for hammer, so the missing formal probe should cover at least these cells:

- **nom.sg.** `*xámaraz` -> expected FST output `hamer`
- **gen.sg.** `*xámaras` -> expected FST output `hameres`

That is the minimum necessary probe. Extra cells such as **dat.sg.** and **nom./acc.pl.** would be optional completeness work, but they are not needed to justify the present row.

## Recommended final report

Recommend a short final report that says row 2053 keeps PGmc lexeme-level `*xámaraz` but uses gen.sg. `*xámaras` as the derivational input because the project wants the regular, attested oblique `hameres` rather than the unstable nominative tradition `hamor/hamer`. It should explicitly note that `hameres` is directly attested in Bosworth-Toller and that `hamores` is a competing attested `-o-` variant, not the form the row selects.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `hameres` is both derivationally clean and directly attested.
- **TSV `DERIVATION_CLASS`:** no change recommended; `late_analogy` still fits the paradigm-cell solution.
- **TSV `NOTE`:** **change recommended** — keep the current analysis, but tighten the wording so it explicitly distinguishes `PROTO` vs `PROTOFORM`, says that exact `hameres` is directly attested in Bosworth-Toller, and avoids implying that `hamores` is merely hypothetical rather than an attested competing `-o-` variant.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** **change recommended** in stale background material. `Germanic/docs/germanic_notes/analogical_leveling_analysis.md` and `Germanic/docs/non_firing_rules_analysis.md` still preserve superseded pre-update analyses (`*xamarăz -> hamor`, or proposed dat.pl. workarounds) and should be marked historical or cleaned up so future packets do not over-weight them.
