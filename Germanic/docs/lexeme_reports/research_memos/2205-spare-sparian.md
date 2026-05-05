# Research memo — 2205 spare / sparian

## Starting point

- **ID:** 2205
- **CONCEPT:** spare
- **COUNTERPART:** sparian
- **PROTO:** *sparēną
- **PROTOFORM:** *spárōjaną
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** Transponent row: inherited class-III cognate set, but OE target is the refashioned class-II verb; the note already cites the Anglian relics `spæria`, `spær`, `spærede`, VP `spearad`, and the two spar dossiers.

The live row is already mostly in the right place. The key task is to keep three things separate: the etymological cognate-set proto `*sparēną`, the project input form `*spárōjaną`, and the OE target `sparian`. Most repo disagreement is not about the OE target, but about whether the project should target the WS class-II citation form or an Anglian class-III relic.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*spárōjaną -> sparian`; the transponent policy in `DEV_NOTES` (`PROTO` as cognate-set form, `PROTOFORM` as FST input); and the live row note's core claim that OE `sparian` is a class-II refashioning of an inherited class-III verb.

**Useful background:** `DEV_NOTES §17.25` and `§17.32` for the diagnostic history; `dossier-spar-2025.md` for the class-III vs class-II comparison; `dossier-spar-apocope-2025.md` for the argument that Ritual `spær` is not the regular phonological output; and the dialect note in `ws_vs_anglian_dialect_differences.md` showing WS `sparian` beside Mercian `spearian`.

**Stale or superseded:** `DEV_NOTES §17.32.8` says the TSV `PROTO` was "actually applied" as `*spárōjaną`, but the live TSV keeps `PROTO = *sparēną`; that historical note should not override the current data. The apocope dossier's preferred Plan B′ recommendation to retarget the row to `spære` is also superseded by the current project decision to keep the row on the WS class-II citation form.

**Irrelevant or misleading:** packet material that treats `spær` as if it were a clean regular OE target for this row is misleading. The repo's own Brunner-based and apocope-dossier evidence says `spær` is not the regular output of `*spárē`; it is a mixed or analogically reshaped Anglian relic, not the target that row 2205 currently represents.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` at the transponent-policy sections (`§8`, `§15.7`) and the row-2205 sections `§17.25` and `§17.32`.
- `Germanic/docs/dossier-spar-2025.md`.
- `Germanic/docs/dossier-spar-apocope-2025.md`.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/tools/oe_paradigm_probe.py`, plus a manual probe run for this memo.
- `Germanic/docs/lexeme_reports/pilot/` (no existing pilot report for this lexeme).

The manual probe confirms the live project logic: `*spárōjaną -> sparian` is the unique winning input among the tested cells, while `*spárēną -> sparen`, `*spárē -> spære`, and `*spárēθi -> spæreþ` do not match the row target.

## Reconstruction and early-stage forms

Three levels need to stay distinct:

1. **Cognate-set proto / etymological reconstruction:** `*sparēną` (or `*sparēn-`), the inherited class-III weak verb reflected by ON `spara`, OHG `sparēn`, and the Anglian relic evidence.
2. **Project input form:** `*spárōjaną`, a PWGmc/pre-OE class-II transponent chosen because the FST cannot model the class-III -> class-II remap internally.
3. **OE target form:** `sparian`, the canonical OE class-II citation form represented by this row.

That means the live row's split between `PROTO` and `PROTOFORM` is philologically better than the older DEV_NOTES proposal to change both columns to `*spárōjaną`. The cognate-set proto should stay class III; the project input should stay class II.

The Anglian forms belong to a different evidential layer. `spæria`, `spær`, and `spærede` show that class-III material survived in Northumbrian, but the repo's own dossiers treat those forms as mixed or analogically contaminated, not as the clean basis for the row's current WS target.

## Old English philology

`sparian` is an **attested OE citation form**, and the repo consistently treats it as the West Saxon class-II norm. `spearian` is useful as a Mercian comparator, and the Durham-Ritual forms `spæria`, `spær`, `spærede` are useful as evidence that the inherited class-III history was not simply erased.

But the Ritual material does not license collapsing everything into one OE target. Campbell's discussion and the local dossiers both treat those Northumbrian forms as hybrid or levelled:

- `spæria` mixes a class-III stem signal with a class-II infinitive ending.
- `spærede` is likewise a hybrid past.
- `spær` is not a regular phonological output from `*spárē`; the apocope dossier argues that its lack of final `-e` is analogical, probably under pressure from the homophonous adjective `spær`.

So the philological contrast is not "attested vs unattested" so much as **canonical WS citation form vs mixed Anglian relic forms**. For row 2205, the WS citation form is still the right OE target.

## Project problem and solution

This is an **early_analogy / transponent** case, not a late-paradigm-cell case. The project problem is that the inherited cognate-set form is class III, but the OE row aims at the class-II verb `sparian`, and the FST does not perform that morphological remap by itself.

The correct solution is therefore:

- keep **TSV `PROTO`** as the etymological cognate-set identifier `*sparēną`;
- keep **TSV `PROTOFORM`** as the transponent `*spárōjaną`;
- keep **TSV `COUNTERPART`** as `sparian`;
- explain in the note that the Anglian relics are background evidence for the inherited class-III history, not alternate target forms for this row.

What should be resisted is the older project-history tendency to let `*spárōjaną` replace the cognate-set proto entirely, or to retarget the row to `spære`/`spær`. The first collapses etymological proto and project input; the second changes what row 2205 is for.

## Paradigm probe

**A paradigm probe is required.** Even though the row is labelled `early_analogy`, the argument depends on comparing multiple paradigm/citation inputs across the inherited class-III set and the chosen class-II transponent.

There is not yet a dedicated checked-in pilot probe for this lexeme, so the final-report workflow should probe at least these cells:

- inherited class-III infinitive: `*spárēną`
- chosen class-II transponent infinitive: `*spárōjaną`
- class-III imperative singular: `*spárē`
- class-III finite present cell used in the row note / dossiers: `*spárēθi`

The manual probe run for this memo already shows the expected pattern: only `*spárōjaną` yields `sparian`; the class-III competitors yield `sparen`, `spære`, and `spæreþ`. That is exactly the comparison the eventual final report should summarize.

## Recommended final report

Recommend a concise final report that says the cognate set is inherited class III `*sparēną`, but the row intentionally uses the class-II transponent `*spárōjaną` to reach the attested WS citation form `sparian`; the Anglian Ritual forms should be discussed briefly as mixed relic evidence, not as the row target. Include a short paradigm-probe subsection.

## Data-change recommendations

- **TSV `PROTO`:** **No change.** Keep `*sparēną` as the cognate-set proto; do not adopt the stale DEV_NOTES suggestion to replace it with `*spárōjaną`.
- **TSV `PROTOFORM`:** **No change.** `*spárōjaną` is the correct transponent input for the current project treatment.
- **TSV `COUNTERPART`:** **No change.** `sparian` remains the right OE target for this row.
- **TSV `DERIVATION_CLASS`:** **No change.** `early_analogy` is still the correct classification.
- **TSV `NOTE`:** **Yes, minor clarification recommended.** The current note is substantively good, but it would be clearer if it explicitly said that `PROTO` stays etymological while `PROTOFORM` is the transponent, and if it avoided implying that `DEV_NOTES §17.32` is fully current in every detail.
- **`oe_known_problems.tsv`:** **No change.** This row is not a live unresolved/known-problem item; the transponent solution is already the project's chosen resolution.
- **`DEV_NOTES` text:** **Yes, cleanup recommended.** `§17.32.8` should be corrected or annotated, because it says the TSV `PROTO` was changed to `*spárōjaną`, which is no longer true in the live data.
- **Dossier text:** **Yes, minor cleanup recommended.** `dossier-spar-apocope-2025.md` should be marked more explicitly as a rejected/alternative pathway for row 2205 rather than a live recommendation, and `dossier-spar-2025.md` could be updated to note that the adopted live row keeps etymological `PROTO` distinct from transponent `PROTOFORM`.
