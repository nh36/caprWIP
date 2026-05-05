# Research memo — 2086 knight / cniht

## Starting point

- **ID:** 2086
- **CONCEPT:** knight
- **COUNTERPART:** `cniht`
- **PROTO:** `*kníxtaz`
- **PROTOFORM:** `*knéxtaz`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** “Proto corrected to *knextăz per R/T vol.2 p.127, Orel p.220, Kluge-Seebold”

The live OE row already shows the key tension: the row’s citation-level `PROTO` is still `*kníxtaz`, but the project input `PROTOFORM` has already been corrected to `*knéxtaz` (`Germanic/data/germanic-aligned-final.tsv`, row 2086). The current output trace in the packet confirms that `*knéxtaz` yields `cniht` without further special handling.

## Packet evidence assessment

**Authoritative/current:**
- The live TSV row and the packet’s compact derivation trace are current evidence: the row now feeds `*knéxtaz` into the OE cascade and the trace reaches `cniht`.
- The packet’s DEV_NOTES hit at `Germanic/docs/DEV_NOTES.md:39280` is still useful current evidence that row 2086 belongs to the `*xt`-preservation set.
- The packet’s lexical-table hit from `Germanic/data/old_english_wiktionary.tsv` is valid for the headword `cniht`.

**Useful background:**
- The long DEV_NOTES section “OE cniht 'knight, servant' — Palatal Umlaut Analysis (2026-04-08)” is good background on the philology and on the literature behind `*kneht/*knextaz` versus `*knixtaz`, with relevant references to [@RingeTaylor2014; @Campbell1959; @SieversBrunner1965; @Orel2003; @KlugeSeebold2011].
- Its discussion of `cniht` versus plural `cneohtas` is useful philological context for the singular/plural alternation.

**Stale or superseded:**
- The same DEV_NOTES section is partly superseded project history. It still says “Row: 2016” and recommends two fixes: correcting the TSV proto and adding `{*io} -> {*i}` to `OEWsPalatalUmlaut`. Both are now historically informative rather than current instructions: row 2086 already has `PROTOFORM = *knéxtaz`, and the live FST already contains the `{*io} -> {*i}` clauses in `Germanic/fsts/germanic.txt`.
- The packet correctly flags the row-number mismatch as diagnostic only; it should not be treated as live row metadata.

**Irrelevant or misleading:**
- There are no dossier or analysis hits in the packet, so the packet by itself does not settle whether this is really an `early_analogy` case.
- The packet can mislead if one reads the 2026-04-08 DEV_NOTES recommendation as still-open engineering work; it is now mostly a record of how the row got into its present partial-cleanup state.

## Additional repo research

Beyond the packet, I checked:
- `Germanic/docs/DEV_NOTES.md` around the 2026-04-08 analysis and the later mismatch log.
- `Germanic/fsts/germanic.txt`, which now includes `{*io} -> {*i}` in `OEWsPalatalUmlaut`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`, `docs/references/campbell_old_english_grammar.txt`, and `docs/references/hogg_vol1.txt` for the lexical and phonological background.
- `docs/refs.bib` for the actual bibliography keys.
- `Germanic/data/oe_known_problems.tsv` (no entry for this lexeme).
- `Germanic/docs/lexeme_reports/report_schema.md` and `source_inventory.md` for the meaning of `early_analogy`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` (row 2086 is still queued for coverage because it has both a note and a non-regular derivation class).
- `Germanic/docs/germanic_transducer_report.md`, which still contains a stale sweep entry with `*knixtăz → cniht`.

I also checked the live transducer behavior directly: the current FST maps both `*knéxtaz` and `*kníxtaz` to `cniht`. That means the older “missing `{*io}` rule” diagnosis has already been implemented in the live grammar; it should not be treated as an unresolved problem for this row.

No full dossier, analysis memo, or pilot lexeme report for knight/cniht appears to exist elsewhere in the repo.

## Reconstruction and early-stage forms

The literature cited in the row note and DEV_NOTES supports a Proto-Germanic / early West Germanic form with **`*e`**, not `*i`: Ringe & Taylor give `*kneht` leading to OE `cniht`, and Orel gives `*knextaz` [@RingeTaylor2014; @Orel2003]. Kluge-Seebold likewise supports a `kneht-` reconstruction [@KlugeSeebold2011].

That matters for three separate layers:
- **Cognate-set proto:** the row’s current `PROTO = *kníxtaz` looks stale against the cited literature.
- **Project input form:** `PROTOFORM = *knéxtaz` already reflects the corrected reconstruction and is the form actually fed to the FST.
- **OE target form:** `cniht` is the Old English singular outcome being modeled.

Because the corrected `PROTOFORM` is not an analogically reshaped special stem distinct from the best-supported proto, this row does **not** currently look like a strong `early_analogy` case in the schema’s sense. It looks more like a row where the citation proto was never fully cleaned up after the reconstruction was corrected.

## Old English philology

`cniht` is an attested Old English lexeme, not a reconstructed OE target. The key philological point is the well-known singular/plural alternation discussed by Campbell and Brunner: singular `cniht` beside plural `cneohtas`, with later analogical leveling in both directions [@Campbell1959; @SieversBrunner1965]. Ringe & Taylor likewise describe PWGmc `*kneht` > OE early West Saxon `cniht ~ cnieht`, plural `cneohtas`, with analogical spread [@RingeTaylor2014].

For this row, however, the target is just the citation singular `cniht`. The row is not trying to encode the whole paradigm, a dialectal variant, or a reconstructed form. The plural evidence is important background because it explains why the `eo > i` development is conditioned by following environment, but it does not force the row itself to be treated as a paradigm-cell selection.

## Project problem and solution

The real project problem is **stale bookkeeping**, not a live early-analogy analysis.

Earlier project history had two issues:
1. the lexeme was stored with a stale citation proto `*knixtăz/*kníxtaz`; and
2. the FST once lacked the `{*io} -> {*i}` branch needed to make an `*i`-based path converge on `cniht`.

The current repo has already solved most of that history in practice:
- the row’s active `PROTOFORM` is already corrected to `*knéxtaz`; and
- the live FST already includes the `{*io}` palatal-umlaut clauses.

What remains is a half-cleaned row: `PROTO` and `DERIVATION_CLASS` still preserve the old story, even though the live derivation now behaves like an ordinary corrected-input case. My recommendation is therefore to treat row 2086 as representing the ordinary singular OE reflex of corrected `*knéxtaz`, not as a genuine early-analogy workaround.

## Paradigm probe

A paradigm probe is **not required** for this row.

Reason: the row is not best analyzed as a late analogical choice of one paradigm cell over another. The current issue is whether the citation proto and derivation-class metadata should be regularized to match the already-correct `PROTOFORM`, not whether the OE target depends on choosing a special oblique or plural input. The `cniht`/`cneohtas` alternation is real philological background, but it does not need a probe to justify the current singular target.

If a future final report wants an illustrative appendix, an optional manual probe could compare the singular citation input against a plural cell with a back-vocalic ending, but that is not needed to resolve the row-level decision here.

## Recommended final report

If the row is cleaned up first, I would **not** prioritize a substantive final `### Lexeme report`: after `PROTO` and `DERIVATION_CLASS` are regularized, this should become an ordinary regular row with little left to explain. If the row is reported before cleanup, the report should be brief and should explicitly say that the apparent `early_analogy` status reflects stale proto bookkeeping rather than a live analogical stem-selection problem.

## Data-change recommendations

- **TSV `PROTO`: change.** Update `*kníxtaz` to the corrected `*knéxtaz` (or the project’s preferred normalized equivalent) so the cognate-set proto matches the cited literature and the already-correct `PROTOFORM`. This likely wants cognate-set-wide cleanup, not OE-only cleanup.
- **TSV `PROTOFORM`: no change.** `*knéxtaz` is already the right project input for the current FST.
- **TSV `COUNTERPART`: no change.** `cniht` is the right OE target.
- **TSV `DERIVATION_CLASS`: change.** Reclassify `early_analogy` to `regular` unless the project intentionally wants to preserve a cross-row legacy distinction that no longer corresponds to the schema definition.
- **TSV `NOTE`: change.** The current note is mainly a cleanup reminder. After fixing `PROTO`, either remove it or replace it with a short philological note only if Nathan wants to preserve the `cniht`/`cneohtas` background explicitly.
- **`oe_known_problems.tsv`: no change.** I found no evidence that this row belongs in the known-problems ledger once the metadata cleanup is done.
- **`DEV_NOTES` / dossier text: change in `DEV_NOTES`, no dossier change currently available.** The 2026-04-08 cniht section should be marked as resolved or annotated to show that the row number was stale and the `{*io}` fix is already live. There is no knight-specific dossier text to update. Separately, `Germanic/docs/germanic_transducer_report.md` still has a stale `*knixtăz` mention and could be cleaned in the same maintenance pass.
