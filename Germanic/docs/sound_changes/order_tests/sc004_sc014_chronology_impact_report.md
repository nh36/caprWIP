# SC004 / SC014 chronology impact audit (corrected PROTOFORM pass)

First-break reruns after the SC004/SC014 correction, using the existing
`sound_change_order_sensitivity.py` machinery with the `expanded-pwgmc` order
profile (so SC014 is independently movable). Summaries in
`summaries/sc004corr_first_break_*`.

## Reruns (the moved rules)

| change | direction | result | boundary | witness(es) |
| --- | --- | --- | --- | --- |
| **SC014** `{*ai}->{*ē}` (pos 1) | earlier | head of cascade | none | — |
| **SC014** | later | first_break_found | **SC072 OE Unstressed Long Vowel Shortening** (order 69) | `span` spanne→spannē, `meed` meorde→meordē (370/372) |
| **SC004** `{*ái}->{*ā}` (pos 25) | earlier | no corpus break toward head | none (boundary-limited) | — |
| **SC004** | later | first_break_found | **SC036 OE Inter Stress Raising** (order 33) | `soul` sāwol→sāwel (371/372) |

SC014 is now **corpus-active** (span, meed) with a real later boundary at SC072;
the previous "corpus-inert / zero corpus load" record is superseded. SC004's
soul/SC036 boundary is reproduced with the corrected stressed-only rule, not
copied from the pre-split campaign.

## Affected neighbour rerun

Intersecting {cards mentioning SC004/SC014} × {targets whose earlier/later
movement interval crosses the new SC004 position (25) or SC014 position (1)} ×
{regenerated non-commuting pairs} yields one substantively affected card:

| change | direction | old boundary | new boundary | witness |
| --- | --- | --- | --- | --- |
| **SC036** OE Inter Stress Raising | earlier | SC019 (order 19) | **SC004 (order 28)** | `soul` sāwol→sāwel (371/372) |

SC004 moved from the cascade head into the interval between SC019 (pos 15) and
SC036 (pos 33), so SC036's earlier first-break is now the nearer SC004 crossing
(the reciprocal of the SC004 < SC036 soul dependency). The former SC019 boundary
remains a further earlier constraint. SC036's later side (SC040) is unchanged.
`sc004corr_first_break_sc036.tsv`; card and index row updated.

## Proved unaffected

- **SC005–SC013** (`PNWGmcAToUBeforeM` … `PWGmcDentalHardening`): their chronology
  cards now record a boundary-only earlier result against the real SC014 head,
  not the former bundled SC004 entry. The substance (no earlier break;
  boundary-only at the chain edge) is unchanged, and their real later boundaries
  (SC017, SC034, SC043, SC031, SC032, SC011, SC087 …) do not involve SC004/SC014.
- **SC015 `PNWGmcILowering`, SC017 `PNWGmcULowering`, SC005 `PNWGmcAToUBeforeM`,
  SC006 `PWGmcEarlyIApocope`**: these non-commute with SC004/SC014 in the formal
  matrix, but only on non-corpus `EnglishProtoInput` forms (feeding artefacts;
  `sc004_sc014_interaction_report.md`). Their corpus first-break boundaries are
  therefore unaffected by the SC004/SC014 move.

## Retained as superseded historical records

The pre-split / pre-correction first-break campaigns
(`summaries/order_sensitivity_first_break_*`, `expanded_pwgmc/*`) were run with
the bundled SC004 at the cascade head and are retained unchanged as historical
audit material. Where they cite "SC004 PWGmc Ai Monophthongization" as the
order-4 left boundary, read that as the former bundled head, superseded by the
split (SC014 at order 1) and this correction.
