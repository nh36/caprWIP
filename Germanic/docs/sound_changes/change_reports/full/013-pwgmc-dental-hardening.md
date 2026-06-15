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

In the inventory ordering, SC013 follows SC012 `PWGmcLThVoicing` and stands as the last internal PWGmc component before the already established SC014 onward sequence. In the production cascade it remains inside bundled `PWGmcChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That makes SC013 a natural right-edge singleton in the present backend-preparation sequence.

#### Order evidence

No validated chronology card exists yet for SC013. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC013 resolves as the tenth rule in the expanded PWGmc order.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should yet be claimed.

#### Interpretation

SC013 is a strong backend singleton candidate. The source support for the basic change is direct, the implementation is straightforward, and the rule stands at a clean structural edge before the SC014 onward sequence. Its main missing piece is validated chronology output.

#### Remaining cautions

The chief caution is evidential balance. The systemic historical statement is strong, but the current lexical witness layer is still fairly compact, and no validated chronology card exists yet. Any later prose should keep the rule precise and should not pretend that the chronology is already established before the first-break TSVs have been validated.
