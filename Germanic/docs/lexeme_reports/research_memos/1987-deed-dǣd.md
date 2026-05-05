# Research memo — 1987 deed / dǣd

## Starting point

- **ID:** 1987
- **CONCEPT:** deed
- **COUNTERPART:** dǣd
- **PROTO:** *dḗdiz
- **PROTOFORM:** *dḗdiz
- **DERIVATION_CLASS:** regular
- **NOTE:** R/T vol.2 13823: PGmc *dēdiz > WS OE dǣd (not Anglian dēd)
- **HISTORY:** none in the live TSV row.

This is a note-bearing regular row. `coverage_audit.md` marks it as needing lexeme-report coverage because the TSV `NOTE` is non-empty, and no pilot/full report for this lexeme was found.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row and the packet's compact derivation trace are current for the project's present target: `*dḗdiz > dǣd`.
- `DEV_NOTES.md` 42679-42739 is current project evidence for why this row now uses stressed `*ḗ`: the stressed-long-ē refactor explicitly promoted root-syllable `*ē` items and cites `*dḗdiz → dǣd` as a stable sample output.
- The packet correctly preserves the live note's distinction between **WS `dǣd`** and **Anglian `dēd`**.

**Useful background:**
- `old_english_wiktionary.tsv` gives `deed = dēd`, which is useful as evidence that repo lexical tables still carry a non-WS or undifferentiated headword alongside the current WS target.
- The reference files (`Campbell`, `Brunner`, `Clark Hall`, `Orel`, `Ringe vol. 1`, `Ringe/Taylor vol. 2`, `Bammesberger`) support the broader philological picture: PGmc `*dēdiz` / `*dédiz`, with WS `dǣd` versus non-WS/Anglian `dēd`.

**Stale or superseded:**
- Older debug snapshots from 2026-02-07 still expected and output `dēd` from unstressed `*dēdiz`. Those are useful project chronology, but they are no longer current authority after the stressed-`*ḗ` refactor.
- The packet does not surface those older snapshots, so without extra repo research it would be easy to miss that `dēd` was an earlier project target rather than current evidence.

**Irrelevant or misleading:**
- Most packet hits under the keyword `Anglian` are false positives from unrelated lexemes (`widuwe`, `meord`, `rēc`, etc.). They are not evidence for row 1987 and should not be treated as such.
- `old_english_wiktionary.tsv` is supplementary only. Taken by itself, it could misleadingly suggest that the row should be retargeted to `dēd`; the stronger repo evidence instead supports the live row's explicit WS selection `dǣd`.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` 42679-42739.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_short_o_fix.txt` 1059-1105.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_post_root_noun_fix.txt` 963-1009.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md` 854-873.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` (no relevant entry).
- `Germanic/data/old_english_wiktionary.tsv`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/ringe_vol1_pie_to_pgmc.txt`.
- `docs/references/orel_handbook_germanic_etymology.vision.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bammesberger_1990_morphologie.txt`.

No full dossier or analysis file specifically for this lexeme was named in the packet or TSV note, and no pilot lexeme report for this item appears to exist.

## Reconstruction and early-stage forms

Three levels need to be kept separate here:

1. **Cognate-set proto / comparative headword:** the comparative sources give ordinary etymological forms like PGmc `*dēdiz` / `*dédiz` (`Orel`, `Ringe vol. 1`, `Ringe/Taylor vol. 2`).
2. **Project input form:** the live TSV now uses stress-marked `*dḗdiz` in both `PROTO` and `PROTOFORM`. That acute-on-macron spelling is a project-internal modelling device added by the stressed-long-ē refactor, not a separate comparative reconstruction.
3. **OE target form:** the row is intended to represent **West Saxon** `dǣd`, explicitly contrasted with Anglian `dēd`.

The current derivational logic is coherent on project terms: `*dḗdiz` loses final `-z`, then the stressed `*ḗ` participates in the newly encoded long-ē lowering path (`*dḗdi > *dǣdi`), and OE apocope yields `dǣd`. Earlier project traces with plain `*dēdiz` gave `dēd`; that is now superseded project history, not the live modelling choice.

So the memo should not collapse these layers into one statement like "PGmc `*dḗdiz` gives OE `dǣd`." The better formulation is: comparative proto `*dēdiz`; project input `*dḗdiz`; OE target `dǣd`.

## Old English philology

This is an **attested lexeme**, not a reconstructed-OE case, but the repo's sources preserve a dialect/headword distinction that matters.

- `Campbell` §128 states that Primitive Germanic `ē` appears as **WS `ǣ`** but in other OE dialects mostly as `ē`, and it lists *deed* among the examples.
- `Brunner` explicitly contrasts **ws. `dǣd`** with **außerws. `dēd`**.
- `Clark Hall` gives `dēd I. (A)=dad`, i.e. Anglian `dēd` cross-referred to the main headword; despite OCR flattening, this again points to a WS vs Anglian doublet rather than a single undifferentiated form.
- `Orel`, `Ringe vol. 1`, and `Bammesberger` align the OE reflex with the same inherited PGmc noun and support the long-vowel etymology behind OE `dǣd`.

So the philological issue is not whether OE had this noun, but **which OE citation form the project wants to target**. The live row's note makes that explicit: the target is the WS form `dǣd`, not the Anglian form `dēd`. `old_english_wiktionary.tsv` is therefore not wrong in a broad lexicographic sense, but it is too coarse for this row's dialect-specific target.

This is also not a paradigm-cell problem. The row targets the citation form noun, not a special oblique or plural cell. The main philological caution for the future report is simply to avoid presenting `dēd` as though it were the chosen OE target, or presenting `dǣd` as though it were the only form ever cited in OE dictionaries.

## Project problem and solution

The project problem here was a **target-selection and modelling-notation problem**, not an unresolved sound-change bug.

Earlier project snapshots treated the lexeme with plain `*dēdiz` and correspondingly produced `dēd`. The later stressed-long-ē refactor intentionally changed a small set of rows, including this one, to stress-marked `*ḗ` inputs so that the cascade could distinguish stressed inherited long `ē` from unstressed `ē`. For row 1987, that change lets the pipeline derive the live WS target `dǣd`, matching the row note.

The current project solution is therefore:

1. keep the row as **regular**;
2. keep the current row target **`dǣd`** as the intended WS form;
3. treat **`dēd`** as the Anglian / non-WS counterpart and as lower-authority background in `old_english_wiktionary.tsv`;
4. explain in reporting that `*dḗdiz` is the project's modelling input, while comparative etymological sources usually cite `*dēdiz` / `*dédiz`.

## Paradigm probe

No paradigm probe is required.

Reason: this row is not choosing among competing paradigm cells, analogical forms, or inflectional survivors. The live issue is citation-form dialect targeting (`dǣd` vs `dēd`) plus the project's stress-tier input notation, which `oe_paradigm_probe.py` is not meant to settle.

## Recommended final report

Recommend a short final lexeme report that says the row intentionally targets **WS `dǣd`**, contrasts it with **Anglian `dēd`**, and explains that live TSV `*dḗdiz` is a project modelling input layered over comparative proto `*dēdiz` / `*dédiz`. It should mention that earlier repo snapshots still showed `dēd`, but only as superseded project history.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. The current `*dḗdiz` matches the project's stressed-long-ē modelling convention.
- **TSV `PROTOFORM`:** no change recommended for the same reason.
- **TSV `COUNTERPART`:** no change recommended. `dǣd` is the row's intended WS target and is better supported than retargeting to `dēd`.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** It should explicitly say that comparative proto is ordinarily cited as `*dēdiz` / `*dédiz`, but the project uses stress-marked `*dḗdiz` to derive the selected WS target `dǣd`, contrasted with Anglian `dēd`.
- **`oe_known_problems.tsv`:** no change recommended.
- **DEV_NOTES / dossier text:** no change recommended. `DEV_NOTES.md` already records the stressed-`*ḗ` change clearly enough, and there is no dedicated dossier text for this lexeme that needs cleanup.
