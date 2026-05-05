# Research memo — 2114 lung / lungen

## Starting point

- **ID:** 2114
- **CONCEPT:** lung
- **COUNTERPART:** lungen
- **PROTO:** `*lungō`
- **PROTOFORM:** `*lúnganjō`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `*lunganjō (ō-stem feminine with *-anjō suffix; Wiktionary Reconstruction:Proto-Germanic/*lunganjō). OE lungen specifically reflects the *-anjō derivative.`

The live row already separates the cognate-set base from the OE-facing derivational input. No pilot/full lexeme report is listed for row 2114 in `report_manifest.tsv`, so the packet is the starting dossier rather than evidence that a vetted report already exists.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet trace showing that the current cascade now derives `*lúnganjō -> lungen`; and the later `DEV_NOTES.md` implementation note at 17910-17929 confirming that the current grammar deliberately accepts this input and outputs `lungen`.
- **Useful background:** the packet's March 2026 `DEV_NOTES.md` section on the original mismatch; the dictionary-form reminders (`lungen`, `lungenne`, `lungena`); `old_english_wiktionary.tsv`; and the coverage notice showing the row is report-worthy because of both `NOTE` and `DERIVATION_CLASS=early_analogy`.
- **Stale or superseded:** the packet's earlier mismatch state `*lungō -> lung (expected lungen)`; the March 2026 recommendation to leave the row as an unmodelled exception; and the packet's presentation of the Wiktionary-style `*lunganjō` derivation as if it were the only philological authority.
- **Irrelevant or misleading:** concept-only snippets that are really implementation-history diagnostics; and any reading of the packet that collapses Kroonen's base noun, the project's model input, and the attested OE target into one undifferentiated form history.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at 13401-13780 and 17844-17929.
- `Germanic/data/oe_known_problems.tsv`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/docs/lexeme_reports/report_manifest.tsv`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- The live FST (`old_english.bin`) via direct lookup.

Main findings from that extra pass:

- The live FST now gives `lunganjō -> lungen`, while `lungō -> lung` and `lungunjō -> +?`.
- `Clark Hall` and `Bosworth-Toller` support attested OE `lungen` as a feminine noun; Bosworth-Toller also shows oblique forms such as `lungenne`, `lungene`, and `lungena`.
- The strongest repo-local lexicographic source is Kroonen, and it does **not** match the packet's simplified story exactly: the Kroonen extract gives base `*lungōn- f. 'lung'` and explicitly says OE `lungen` etc. are from `*lungunjō-`.
- No separate dossier or analysis file named in the packet/row note turned up for this lexeme; the relevant extra evidence is in `DEV_NOTES` and the reference extracts.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / headword:** TSV `PROTO = *lungō` is the project's headword shorthand for the basic lexeme. Kroonen's fuller citation in the repo is `*lungōn- f.`, so the live `PROTO` is already a simplified project label rather than a full dictionary-style stem citation.
2. **Project input form used for derivation:** TSV `PROTOFORM = *lúnganjō` is the live modelling input because the current FST accepts it and derives `lungen`.
3. **OE target form:** `lungen` is the attested Old English lexeme represented by the row.

The important complication is that the repo's strongest lexicographic evidence does not straightforwardly support the exact live `PROTOFORM`. Kroonen connects OE `lungen` with `*lungunjō-`, not with a Wiktionary-style `*lunganjō`. So the current row should be read as: base noun `*lungō` / `*lungōn-` at the cognate-set level, an OE-facing derivative must be modelled for the target, and the live project input `*lúnganjō` is at least partly a project transponent rather than an unproblematic statement of the best PGmc reconstruction.

## Old English philology

`lungen` should be treated as an attested Old English citation form, not as a reconstructed ghost form and not as a late paradigm-cell substitute. `old_english_wiktionary.tsv`, `Clark Hall`, and `Bosworth-Toller` all support the headword `lungen`, and Bosworth-Toller further attests oblique forms including `lungenne`, `lungene`, and `lungena`.

That makes one earlier project option clearly obsolete: changing the OE target to bare `lung` would replace an attested noun with an unattested abstraction. The philological issue is not whether OE had `lungen`; it did. The real issue is how best to represent the pre-OE derivational stage behind that attested form.

The packet's wording also needs caution on morphology. It is safe to say that OE `lungen` is a derived feminine lexeme with `-en-` in the stem. It is less safe to present the exact PGmc derivational label `*-anjō` as settled when Kroonen's repo-local entry instead points to `*lungunjō-`.

## Project problem and solution

The original project problem was real: a direct run from the basic noun (`*lungō`) yields `lung`, while the row is meant to model attested OE `lungen`. The project was therefore right to separate the cognate-set base from an OE-facing derivative and right to reject any retargeting to unattested `lung`.

The current computational solution is also real: grammar work plus later rule cleanup now allow `*lúnganjō -> lungen` in the live FST. But that does **not** mean the March/April 2026 project history has fully settled the philology. The present row solves the derivation mechanically while still needing a cleaner statement of what is authoritative: the OE target is secure, the need for a derivative input is secure, but the exact derivative should be described against Kroonen's `*lungunjō-`, not only against the packet's Wiktionary-based `*lunganjō` story.

So the best project reading is: row 2114 is an `early_analogy` / pre-OE derivational-selection case, not a late-analogy paradigm-cell case. The row represents attested OE `lungen`, while keeping the base noun and the derivative-input question distinct.

## Paradigm probe

No paradigm probe is required.

This is not a `late_analogy` problem where the project needs to choose among OE inflectional cells to avoid a nominative mismatch. The decisive issue is upstream derivational input selection (`*lungō` vs a derived pre-OE input), and the row already targets an attested OE lemma rather than an oblique-cell workaround. If a future appendix wants illustration, the attested forms `lungen`, `lungenne`, and `lungena` are philological support, but no missing paradigm cells need to be probed for this memo.

## Recommended final report

Recommend a concise final report stating that OE `lungen` is an attested feminine lexeme, that the row must distinguish base `PROTO = *lungō` from a derivative modelling input, and that the final prose should explicitly note the tension between the live project input `*lúnganjō` and Kroonen's repo-local `*lungunjō-` evidence instead of presenting the Wiktionary-style form as settled fact.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. `*lungō` is acceptable as a project headword shorthand, even if Kroonen's fuller citation is `*lungōn-`.
- **TSV `PROTOFORM`:** change recommended. The live `*lúnganjō` works computationally, but the strongest repo-local lexicographic evidence points to `*lungunjō-` behind OE `lungen`; at minimum this field needs review rather than being treated as settled authority.
- **TSV `COUNTERPART`:** no change recommended. `lungen` is the right OE target.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` is still the right project bucket because the issue is pre-OE derivational/stem selection, not a late OE inflectional-cell choice.
- **TSV `NOTE`:** change recommended. It should stop presenting `*lunganjō` + Wiktionary as the whole story and should explicitly acknowledge the stronger repo-local Kroonen evidence for base `*lungōn-` and derivative `*lungunjō-`, while also saying that the live project input is currently a modelling choice.
- **`oe_known_problems.tsv`:** no change recommended for now. This looks more like TSV/`DEV_NOTES` curation than a separate known-problem entry, unless the project decides to retain a provisional workaround input indefinitely.
- **`DEV_NOTES` / dossier text:** change recommended. The 2026 `lungen` section should be annotated so that its now-superseded March diagnosis and its Wiktionary-based `*lunganjō` framing are clearly distinguished from the later computational fix and from Kroonen's stronger `*lungunjō-` evidence. No separate dossier text change is needed because no dedicated dossier was identified for this row.
