# Dental hardening

### Sound-change report

#### Historical formulation

SC013 `PWGmcDentalHardening` isolates the hardening of voiced dental fricative `*ð` to stop `*d`. In the current trace layer it appears through forms such as `lade`, `needle`, `find`, and `cud`, but the historical point is broader than any one lexical family: this is a systemic statement about the status of PWGmc `*d`.

That gives the rule a stronger structural footing than some neighboring early PWGmc items, even though the present lexical witness set is still modest.

#### Source tradition

Ringe and Taylor state directly that in PWGmc the non-coronal voiced obstruents continued to show allophony, but `*d` became a stop in all positions [@RingeTaylor2014, p. 43]. That is unusually strong and explicit support for the historical phenomenon itself.

What the source layer does not yet provide in this pass is a fully expanded lexical dossier for every current trace witness. The systemic historical claim is well supported; the individual witness mapping is still lighter than it could be.

#### CAPR implementation

CAPR models the change as:

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

This is a direct formalization of the historical statement recovered from Ringe and Taylor. It is one of the cleaner cases in the early PWGmc bundle because the source tradition and the modeled rule align closely.

#### Place in the cascade

In the inventory ordering, SC013 follows SC012 `EAFLThVoicing` and stands as the last internal PWGmc component before the already established SC014 onward sequence. In the production cascade it remains inside bundled `EarlyEnglishLineChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That makes SC013 a natural right-edge singleton in the present backend-preparation sequence.

#### Order evidence

Validated expanded-PWGmc first-break TSV output now exists for SC013, and the chronology card is complete. The earlier search moved safely across SC012, SC011, SC010, SC009, SC008, SC007, SC006, SC005, and SC004 to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break.

The later search likewise reached order `86` with no real break before the current SC087 boundary. Both sides are therefore boundary-only / chronology-negative in current testing.

#### Interpretation

SC013 can still stand as a short finished singleton note. The source support for the basic change is direct, the implementation is straightforward, and the negative chronology card is acceptable so long as the note stays precise and does not claim a positive local ordering that current testing does not show.

#### Remaining cautions

The chief caution is methodological. The systemic historical statement is strong, but both sides of the validated chronology card are boundary-only. Any later prose should keep the rule precise and should not turn the tested-chain left edge or the SC087 search boundary into historical anchors.
