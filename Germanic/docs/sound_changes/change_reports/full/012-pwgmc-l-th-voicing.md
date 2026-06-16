# Word-internal lþ-voicing

### Sound-change report

#### Historical formulation

SC012 `PWGmcLThVoicing` isolates the development of word-internal `*lþ` to `*ld`, reflected in trace examples such as `field`, `fold`, `gold`, and `wold`. The historical phenomenon is clear enough to document, but the stage label is already more delicate than the current inventory makes it sound.

The source support recovered here points most clearly to a **northern West Germanic** development rather than to an unquestioned pan-PWGmc rule. That caution should remain visible from the beginning.

#### Source tradition

Ringe and Taylor state that word-internal `*lþ` became `*ld` by regular sound change in northern WGmc and give examples such as `fealdan`, `beald`, `wuldor`, and `gylden` [@RingeTaylor2014, pp. 170--171]. Campbell likewise states that medial `lþ` became `ld` in West Germanic and illustrates the outcome with forms such as `fealdan`, `wuldor`, `beald`, `gold`, and `feld` [@Campbell1959, §414].

That is enough to support the historical development itself. It is less enough to license a fully settled PWGmc label, because the strongest Ringe and Taylor wording is explicitly narrower than the inventory's present stage label.

#### CAPR implementation

CAPR models the change as:

```foma
define PWGmcLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

This is a compact formalization of the `lþ > ld` development. As the FST comments already note, some lexical families may also intersect with Verner's-law alternation, but the implementation keeps the historical center of gravity on the consonant cluster itself.

#### Place in the cascade

In the inventory ordering, SC012 follows SC011 `PWGmcSyllabicJ` and precedes SC013 `PWGmcDentalHardening`. In the live cascade it remains inside bundled `PWGmcChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That means the chronology path is procedurally available even though the source-layer stage label still needs caution.

#### Order evidence

Validated expanded-PWGmc first-break TSV output now exists for SC012, and the chronology card is complete. The earlier search moved safely across SC011, SC010, SC009, SC008, SC007, SC006, SC005, and SC004 to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break.

The later search likewise reached order `86` with no real break before the current SC087 boundary. Both sides are therefore boundary-only / chronology-negative in current testing.

#### Interpretation

SC012 can now stand as a cautious singleton note. The underlying sound change is credible and source-supported, and the sequence should account for it explicitly even though the validated chronology card supplies no positive local boundary on either side.

#### Remaining cautions

Two cautions matter most. First, the historical stage may be narrower than the inventory's plain PWGmc framing, since Ringe and Taylor describe the change as northern WGmc. Second, the validated chronology card is negative on both sides and therefore supplies no positive local ordering claim. The chapter should keep both cautions visible and should not present the rule as a tightly anchored local seam.
