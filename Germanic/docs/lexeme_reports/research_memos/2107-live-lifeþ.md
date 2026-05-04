# Research memo — 2107 live / lifeþ

## Starting point

- **ID:** 2107
- **CONCEPT:** live
- **COUNTERPART:** lifeþ
- **PROTO:** *libēną
- **PROTOFORM:** *líbēθi
- **DERIVATION_CLASS:** late_analogy
- **NOTE:** 3sg pres. indic. (archaic North. lifed); infinitive libban shows j-gemination from *libjăną stem, not *-ē- stem.

The live TSV row is already a paradigm-cell choice: it does **not** target the OE lemma/infinitive, but an archaic 3sg present form chosen to preserve the inherited *-ē- stem while the OE infinitive was remodelled.

## Packet evidence assessment

**Authoritative/current:** the TSV row itself; the packet's compact derivation trace showing `*líbēθi -> lifeþ`; the DEV_NOTES row-2107 analysis once it reaches the 2026-03-09 continuation and decision; and the current trace/coverage material showing row 2107 as a matched, report-requiring late-analogy row.

**Useful background:** the packet's excerpts from Campbell and Ringe/Taylor on the class-III alternation, the note that Anglian `lifgu/lifgaþ/lifgende` are innovations rather than archaisms, and Kroonen's use of OE `libban` under `*libēn-` [@Campbell1959; @RingeTaylor2014; @Kroonen2013].

**Stale or superseded:** the earlier DEV_NOTES stage where the 3sg pathway was still marked "NOT TESTED"; the interim recommendation that Option 1 (`*libjăną -> libban`) was the strongest single-row solution; and the packet-era mismatch diagnostics that still show `*libēθi -> +?`. Those are historical workflow traces, not the current project state.

**Irrelevant or misleading:** the absence of an `oe_known_problems.tsv` entry should not be read as evidence against the row; and generic concept-name hits elsewhere in DEV_NOTES are not row-specific lexical evidence.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` at the full row-2107 analysis (`4066-4374`), plus the later notation/convention notes on `*libjăną` vs `*libjaną`.
- `Germanic/data/oe_known_problems.tsv` (no entry for this lexeme).
- `Germanic/data/old_english_wiktionary.tsv` (`live -> lifian` only, useful as dictionary background but not decisive for row design).
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `docs/debug_snapshots/oe_derivation_class_trace_report*.md`, which confirm that row 2107 currently matches and still requires lexeme-report coverage.
- `Germanic/tools/oe_paradigm_probe.py`, which has no built-in probe spec yet for `live / lifeþ` but supports manual candidate comparison.
- `Germanic/docs/dossier-shoulder-cellchoice-2026.md`, which treats row 2107 as an explicit precedent for paradigm-cell switching to a 3sg present form.
- `Germanic/docs/dossier-spar-2025.md`, for general class-III background and Campbell's discussion of residual class-III verbs.

No pilot/full lexeme report for this row appears to exist yet; current coverage files still list it as missing.

## Reconstruction and early-stage forms

Three levels must stay separate:

1. **Cognate-set proto:** `*libēną` is the comparative headword for the inherited class-III weak verb 'live' [@Kroonen2013].
2. **Project input form:** `*líbēθi` is the selected finite 3sg present input, representing the inherited non-geminating *-ē- stem of the class-III alternation.
3. **OE target form:** `lifeþ` is the project's normalized OE outcome for that finite cell; the directly cited manuscript form is late Northumbrian `lifed`.

That distinction matters because the conservative OE infinitive belongs to the **other** stem: `libban < *libjaną/*libjăną`, i.e. the j-stem side of the inherited alternation, not the finite *-ē- stem. So `PROTO = *libēną` and `PROTOFORM = *líbēθi` are not contradictory; they are different levels of representation.

## Old English philology

The philological picture is not "PGmc `*libēną` -> OE `lifian`". Kroonen cites OE `libban`, not `lifian`, under `*libēn-`, and Ringe/Taylor reconstruct an inherited alternation between `*libja-` and `*libai-/*libē-` stems [@Kroonen2013; @RingeTaylor2014].

In OE, the ordinary lemma situation is already remodelled:

- **Conservative infinitive:** `libban` (j-stem, geminated).
- **WS 2sg/3sg/imperative:** `leofast, leofaþ, leofa`, showing class-II intrusion.
- **Anglian `lifgu, lifgaþ, lifgende`:** not archaisms, but secondary `*-ē- ~ *-ēja-` remodelling [@RingeTaylor2014].
- **Late Northumbrian `lifed`:** the archaic 3sg present singled out by Ringe/Taylor as preserving the older pattern.

Accordingly, `lifeþ` in the TSV should be understood as a **normalized orthographic target for an attested inflected form**, not as an attested citation lemma. The attested form is `lifed`; `lifeþ` is the regular OE orthographic normalization underlying the project output, with Northumbrian `<d>` treated as an orthographic variant of unstressed /ð/ in that tradition (as summarized in DEV_NOTES from Campbell).

## Project problem and solution

The project problem was that the inherited cognate-set verb is real, but the obvious OE lemma forms are morphologically split:

- `lifian` is the later class-II-style infinitive and is not the conservative reflex the row ought to represent.
- `libban` is conservative, but it reflects the j-stem side of the paradigm rather than the inherited *-ē- finite stem.

The adopted project solution is therefore sensible: keep `PROTO` as the cognate-set headword `*libēną`, but let the row's actual derivational target be the archaic 3sg finite cell `*líbēθi -> lifeþ`, while the note explains that the infinitive evidence belongs to `libban` from the j-stem. That is exactly a paradigm-cell choice, so `late_analogy` remains the right derivation-class label.

## Paradigm probe

**Yes — a paradigm probe is still required.** This row is a paradigm-cell case, and `oe_paradigm_probe.py` still has no built-in `live / lifeþ` specification.

A proper probe should include at least these cells:

- **3sg pres.** `*libēþi -> lifeþ` (the chosen TSV pathway).
- **Infinitive** `*libjaną` (or project-equivalent notation `*libjăną`) -> `libban`, to show the competing conservative lemma pathway.
- **Optional diagnostic cells:** 2sg pres. `*libēsi` and imperative sg. `*libē`, to demonstrate why the surviving WS forms are remodelled (`leofast`, `leofa`) rather than the row target.

A manual probe run on the current repo already confirms `*libēþi -> lifeþ`. It also shows that the infinitive comparison works with `*libjaną -> libban`; the current probe/tooling is notation-sensitive about `*libjăną`, so any built-in spec should normalize that input carefully rather than treating the no-output result as philological evidence.

## Recommended final report

Recommend a concise final lexeme report that says the row deliberately targets the **archaic Northumbrian 3sg present** rather than the OE lemma, and that distinguishes clearly between `*libēną` (cognate-set proto), `*líbēθi` (selected project input), `lifeþ`/`lifed` (target vs attested orthographic variant), and `libban`/`lifian` as competing OE lemma-level outcomes. Include a short paradigm-probe section once the probe spec exists.

## Data-change recommendations

- **TSV `PROTO`:** **No change.** `*libēną` is the right cognate-set headword.
- **TSV `PROTOFORM`:** **No change.** `*líbēθi` is the right project input for the chosen finite-cell solution.
- **TSV `COUNTERPART`:** **No change.** Keep normalized `lifeþ`; explain attested Northumbrian `lifed` in note/report prose.
- **TSV `DERIVATION_CLASS`:** **No change.** `late_analogy` correctly flags a non-lemma paradigm-cell choice driven by later OE remodelling.
- **TSV `NOTE`:** **Yes, minor clarification recommended.** Make explicit that `lifeþ` is the normalized 3sg target and that attested `lifed` is the Northumbrian orthographic variant; that would reduce the risk of readers mistaking `lifeþ` for a directly cited lemma.
- **`oe_known_problems.tsv`:** **No change.** This row is not a live known-problem exception; the current selected pathway is productive.
- **`DEV_NOTES` text:** **Yes, minor cleanup recommended.** Mark the earlier `NOT TESTED` and "Option 1 remains strongest" passages more explicitly as superseded by the later 2026-03-09 decision, so packet extraction does not keep surfacing obsolete state as quasi-current evidence.
- **Dossier text:** **No mandatory change.** The precedent dossier is usable as background; the row-specific clarification is mainly needed in TSV note wording and DEV_NOTES chronology.
