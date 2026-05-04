# Research memo — 2314 learn (3sg) / liornaþ

## Starting point

- **ID:** 2314
- **CONCEPT:** learn (3sg)
- **COUNTERPART:** `liornaþ`
- **PROTO:** `*liznōjaną`
- **PROTOFORM:** `*líznōθi`
- **DERIVATION_CLASS:** `late_analogy`
- **NOTE:** Class II weak 3sg; regular `*-ōθi → -aþ`; root has `io` from breaking before `rn`; no i-umlaut because the 3sg ending never had `-j-`; `-eþ` forms are dialectal (Campbell §757) [@Campbell1959].

The live row already reflects the current project position: keep the learn-verb cognate set under i-grade `*liznōn-`, but target the regular Northumbrian-type 3sg cell `liornaþ` from `*líznōθi`, not a leveled West Saxon `leorn-` form.

## Packet evidence assessment

**Authoritative/current**

- The live TSV row and the packet’s compact derivation trace are current: `*líznōθi` now runs to `liornaþ`.
- The packet’s later DEV_NOTES excerpts from the weak-II 3sg correction are current: the project now treats `*-ōþi > -aþ` as regular, with `-eþ` only dialectal/background.

**Useful background**

- The packet correctly preserves the project’s reason for the OE vowel: rhotacism plus breaking give `liorn-`, and the 3sg ending itself does not supply an umlaut trigger.
- The packet is also useful for showing the earlier debugging path from `liorneþ` to `liornaþ`.

**Stale or superseded**

- The packet’s DEV_NOTES hits at old §14.518–14.760 recommending `*leznōθi` and `leorneþ` are superseded by later project work. They record a temporary West-Saxon-oriented workaround, not the current row policy.
- `Germanic/docs/analysis/compound_archaism_inventory.md` case 6 is stale for this row: it says the TSV “now targets” `*leznōn-` / `leornian`, but the live TSV instead keeps `*liznōjaną` and targets Northumbrian `liornian`/`liorna`/`liornaþ`.
- `Germanic/docs/analysis/mismatch_dossier_mizdo.md` is only diagnostic background where it cites the older `*liznōjan > *leznōjan` precedent.

**Irrelevant or misleading**

- Generic packet keyword hits on breaking/i-umlaut elsewhere in the repo are not lexeme-specific evidence for row 2314.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at the older `leornian` discussion (§14.518ff.), the later weak-II 3sg correction (§15.1), and the regression debugging around `liorneþ > liornaþ` (§15.5).
- `Germanic/docs/analysis/compound_archaism_inventory.md` case 6.
- `Germanic/docs/analysis/mismatch_dossier_mizdo.md` sections 4.5 and 8.5, because the packet pointed to that dossier as a precedent discussion.
- `Germanic/docs/lexeme_reports/packets/2313-learn-(iptv.2sg)-liorna.md`.
- `Germanic/data/germanic-aligned-final.tsv` rows 2095 and 2313, which show the same current policy for the infinitive `liornian` and imperative `liorna`.
- `Germanic/data/oe_known_problems.tsv` (no relevant entry).
- `Germanic/tools/oe_paradigm_probe.py` plus a manual probe for learn-cells.

No pilot lexeme report already exists for this lexeme. The only learn-specific repo prose is DEV_NOTES/analysis background, and some of that prose is now stale.

## Reconstruction and early-stage forms

The necessary distinctions are:

1. **Cognate-set proto / etymological headword:** the project still groups the lexeme under `*liznōjaną`, i.e. the inherited learn-verb with i-grade root, matching the standard PGmc reconstruction tradition summarized in Kroonen, Ringe-Taylor, and Fulk [@Kroonen2013; @RingeTaylor2014; @Fulk2018].
2. **Project input form for this row:** `*líznōθi`, the 3sg present indicative cell.
3. **OE target represented by the row:** `liornaþ`, a Northumbrian-type 3sg outcome.

For row 2314, the current repo evidence favors the i-grade input, not the old e-grade workaround. The relevant derivation is:

`*líznōθi` → rhotacized `*lírnōθi`/`*lírnōθ` → breaking `*líornōθ` → late unstressed shortening `*líornaθ` → orthographic `liornaþ`

That is different from the older, now-superseded project attempt to rewrite the row as `*leznōθi > leorneþ`. The e-grade proposal belonged to an earlier effort to force West Saxon `leorn-` outputs directly from the row; it is no longer the live solution.

## Old English philology

`liornaþ` is not a dictionary headword but a finite **3sg present indicative** form. The memo and any later report need to say that plainly.

The important OE distinction is not “attested vs unattested WS spelling” so much as **which OE variety the row is intended to model**. Current repo practice already uses Northumbrian-type forms for this lexeme family:

- row 2095: `liornian`
- row 2313: `liorna`
- row 2314: `liornaþ`

That means West Saxon `leornian`/`leorna-` belongs here as comparative philological background, not as the row’s target. For the 3sg ending specifically, the current note is right that `*-ōþi > -aþ` is the regular class-II outcome, while `-eþ` is dialectal or secondary background [@Campbell1959].

## Project problem and solution

The project’s older problem was twofold:

1. it once tried to force West-Saxon-looking `leorn-` forms by changing the proto input to `*lezn-`;
2. it also briefly treated weak class II 3sg `-eþ` as the expected outcome.

Later work superseded both moves. The current solution is better:

- keep the cognate-set proto as `*liznōjaną`;
- use the correct row-specific finite input `*líznōθi`;
- target the regular Northumbrian-type 3sg `liornaþ`;
- treat West Saxon `leorn-` and earlier `*lezn-` proposals as background history, not as the final row analysis.

So this row is “late_analogy” in the project’s operational sense because `PROTO` is the lexeme headword while `PROTOFORM` is a selected paradigm cell, even though the **3sg phonology itself is regular** once that cell is chosen.

## Paradigm probe

A paradigm probe is appropriate here, because the row distinguishes lexeme-level `PROTO` from cell-level `PROTOFORM`.

An in-session manual probe already gives a clean unique winner:

- infinitive `*líznōjaną` → `liornian`
- imperative 2sg `*líznô` → `liorna`
- 3sg present `*líznōθi` → `liornaþ`

So the 3sg cell is not in doubt. However, the repo does **not** yet contain a saved learn-specific probe. If one is added, it should at minimum probe:

- infinitive `*líznōjaną`
- imperative 2sg `*líznô`
- 3sg present indicative `*líznōθi`

Optionally it could add 2sg present `*líznōsi` and one umlauting 1sg/plural class-II cell, just to show why the non-`j` singular cells behave differently from the `-ōj-` part of the paradigm.

## Recommended final report

Recommend a short lexeme report that says: the cognate set remains `*liznōn-`; this row uses the finite input `*líznōθi`; the intended OE target is the regular Northumbrian-type 3sg `liornaþ`; earlier repo proposals with `*leznōθi`/`leorneþ` are superseded project history only.

## Data-change recommendations

- **TSV `PROTO`:** **No change.** Keep `*liznōjaną` as the cognate-set / lexeme-level proto label.
- **TSV `PROTOFORM`:** **No change.** Keep `*líznōθi`; do not revive the older `*leznōθi` workaround.
- **TSV `COUNTERPART`:** **No change.** `liornaþ` matches the current regular Northumbrian analysis.
- **TSV `DERIVATION_CLASS`:** **No immediate change.** `late_analogy` is still doing useful project work here by flagging the distinction between lexeme headword and selected paradigm cell, even though the chosen 3sg outcome is phonologically regular.
- **TSV `NOTE`:** **Minor change recommended.** Add one sentence making the project rationale explicit: this row intentionally targets the Northumbrian-type 3sg parallel to `liornian`/`liorna`, while West Saxon `leorn-` belongs only in background discussion.
- **`oe_known_problems.tsv`:** **No change.** The row now derives cleanly and does not need a known-problems entry.
- **`DEV_NOTES` / dossier text:** **Change recommended.** Old sections that still present `*leznōθi` / `leorneþ` or say the TSV “now targets” e-grade `leorn-` should be marked superseded or revised, especially in `DEV_NOTES.md`, `compound_archaism_inventory.md`, and the learn-precedent remarks in `mismatch_dossier_mizdo.md`.
