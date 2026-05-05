# Research memo — 2109 loam / lām

## Starting point

- **ID:** 2109
- **CONCEPT:** loam
- **COUNTERPART:** `lām`
- **PROTO:** `*laimōn` (cognate-set headword)
- **PROTOFORM:** `*láimą` (current per-row OE input form)
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** empty
- **HISTORY:** the row history already records the key project claim: Orel/Kroonen support a masculine n-stem cognate-set proto, while Old English has shifted to a neuter strong noun; because the cascade has no class-shift rule, the per-row input was changed from `*láimōn` to `*láimą` while the cognate-set proto stayed `*laimōn`.

## Packet evidence assessment

**Authoritative/current:** the aligned TSV row itself; the compact derivation trace showing `*láimą → lām`; the DEV_NOTES §17.39 source audit quoting Orel, Kroonen, Clark Hall, and Bosworth-Toller; and the lexical-table hit `old_english_wiktionary.tsv: loam → lām`. These are the current evidence base for the row as it now stands.

**Useful background:** DEV_NOTES §17.39's probe matrix is useful because it demonstrates that the issue is stem class, not an unexplained phonological failure: `*láimą`, `*láimaz`, and `*láimō` all reach `lām`, while inherited `*láimōn` does not. The shoulder dossiers are also useful as project-history evidence because they repeatedly cite loam as a precedent for a PROTOFORM-only stem-class correction.

**Stale or superseded:** the packet's older DEV_NOTES hit `*laimōn | lāme | ... | lām` and older full-trace snapshots with `OUTPUTS: lāme` are pre-fix diagnostics, not current lexical evidence. They matter only for chronology. Likewise the `*láimōn → lāfe` mismatch is current as a cascade artifact, but it is diagnostic only once the row has already been corrected to `*láimą`.

**Irrelevant or misleading if over-weighted:** the successful probe `*láimaz → lām` should not be treated as the historical solution for this row. DEV_NOTES explicitly treats the Wiktionary-style masculine a-stem as an outlier against the printed-dictionary consensus for n-stem PGmc. There is also no manifest entry and no dedicated loam dossier; their absence should not be turned into evidence either way.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around §17.39, including the follow-up artifact note at §17.39.1 and the older pre-fix table at line 3853.
- `Germanic/docs/dossier-shoulder-cellchoice-2026.md`, where loam is classified as a Class-A precedent: keep the NSg target and realign only the per-row proto to the OE-internal stem class.
- `Germanic/docs/dossier-shoulder-2026.md` and `Germanic/docs/dossier-shoulder-lautgesetz-2026.md`, which cite loam only as precedent/background, not as fresh lexical evidence.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which confirms row 2109 still lacks a manual pilot/full lexeme report and is in scope because `DERIVATION_CLASS=early_analogy`.
- `Germanic/docs/lexeme_reports/pilot/` (no pilot report for loam found).
- `docs/debug_snapshots/oe_full_trace_report.txt`, which preserves the older `*laimōn → lāme` state and confirms that some repo history is now superseded.
- `docs/refs.bib`, which contains the expected bibliography keys `[@Orel2003]`, `[@Kroonen2013]`, `[@ClarkHall1960]`, and `[@BosworthToller1898]`.

No full loam-specific dossier or analysis file appears to exist in the repo.

## Reconstruction and early-stage forms

The important distinction is three-way:

1. **Cognate-set proto (`PROTO`):** `*laimōn`, the masculine n-stem headword represented across the Germanic cognate set and supported in repo-local source audit from Orel and Kroonen.
2. **Project input form (`PROTOFORM`):** `*láimą`, an OE-targeted neuter a-stem input chosen so the cascade can derive the attested Old English form without needing an unimplemented class-shift rule.
3. **OE target form:** `lām`, the Old English neuter strong lemma.

The repo's current best interpretation is not that Proto-Germanic itself was an a-stem, but that Old English underwent an early class shift from inherited n-stem material into a neuter strong noun. DEV_NOTES rejects Wiktionary's `*laimaz` as the main basis for the row and instead treats `*láimą` as an OE-internal modelling choice. So the right reconstruction story is: cognate-set PGmc `*laimōn` remains intact, while row-level `PROTOFORM` is deliberately adjusted to the early OE class that actually yields `lām`.

## Old English philology

Repo-local lexicographic evidence is consistent: Clark Hall gives `lām n.` and Bosworth-Toller gives `lām, es; n.`; DEV_NOTES summarizes Orel and Kroonen as likewise flagging the OE reflex as neuter. That makes `lām` an attested dictionary headword, not a reconstructed OE form.

The row is therefore not about choosing among competing attested OE spellings. It is about correctly modelling the lexical class behind an attested citation form. The target should be understood as the lemma/citation form of a neuter strong noun, effectively the nominative/accusative singular. Nothing in the checked repo sources justifies a stronger dialect or manuscript claim, so the final report should stay with the ordinary lexicographic statement that OE `lām` is neuter strong.

## Project problem and solution

The project problem was a mismatch between the cognate-set proto and the OE-specific stem class. Feeding inherited `*láimōn` directly into the cascade produced spurious outputs (`lāme` in older history, later `lāfe` in the explicit §17.39 mismatch note) because the machine has no rule that reclassifies an inherited masculine n-stem as the neuter strong noun reflected in Old English.

The current project solution is the right one: keep TSV `PROTO` as the cognate-set form `*laimōn`, keep the OE target as attested `lām`, and use TSV `PROTOFORM = *láimą` to encode the OE-specific class shift at the row level. That is exactly the kind of Class-A precedent later dossiers cite. The separate `*aim:ōn → ā:β:e` artifact logged in DEV_NOTES §17.39.1 should remain a cascade follow-up, not a reason to undo the row-level fix.

## Paradigm probe

A dedicated paradigm probe is **not required** for the final report. This row is not a late-analogy cell-selection problem with multiple competing OE paradigm cells; it is a stem-class realignment while keeping the same attested NSg target. DEV_NOTES already contains the essential diagnostic probe matrix (`*láimōn`, `*láimą`, `*láimaz`, `*láimō`) showing why the row uses `*láimą`.

If a formal probe table is ever wanted for documentation symmetry, it should compare only citation-form candidates, not missing inflectional cells: inherited n-stem `*láimōn`, OE-targeted neuter a-stem `*láimą`, and the outlier a-stem comparator `*láimaz` against target `lām`.

## Recommended final report

The final `### Lexeme report` should be brief. It should say that printed etymological sources support PGmc `*laimōn` but also treat OE `lām` as a neuter noun; the row therefore keeps cognate-set `PROTO` unchanged and uses OE-specific `PROTOFORM *láimą` as an early class-shift modelling choice, with `lām` as the attested neuter strong target. It should also note that older `*láimōn → lāme/lāfe` traces are project diagnostics, not the chosen lexical analysis.

## Data-change recommendations

- **TSV `PROTO`:** **no change**. `*laimōn` is the correct cognate-set headword for the wider Germanic set.
- **TSV `PROTOFORM`:** **no change**. `*láimą` is the right per-row modelling input for the attested OE noun class.
- **TSV `COUNTERPART`:** **no change**. `lām` is the right OE target/headword.
- **TSV `DERIVATION_CLASS`:** **no change**. `early_analogy` accurately captures an early stem-class reassignment rather than a regular inherited path.
- **TSV `NOTE`:** **no change required**. The row already carries the necessary explanation in `HISTORY`, and the eventual lexeme report can carry the concise narrative.
- **`oe_known_problems.tsv`:** **no change required**. The row itself is now resolved; the residual `*aim:ōn → ā:β:e` artifact is a separate cascade issue already logged in DEV_NOTES and does not currently need a row-level OE known-problems entry.
- **`DEV_NOTES` / dossier text:** **no substantive change required**. Current DEV_NOTES §17.39 already captures the lexical reasoning and the follow-up artifact. Older archival traces showing `lāme` are stale history, but they are acceptable as chronology rather than errors.
