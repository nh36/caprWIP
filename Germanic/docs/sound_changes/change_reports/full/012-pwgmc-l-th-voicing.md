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

No validated chronology card exists yet for SC012. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC012 resolves as the ninth rule in the expanded PWGmc order.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should yet be claimed.

#### Interpretation

SC012 is a backend singleton candidate with real historical support, but it should be treated cautiously. The underlying sound change is credible, yet the best current source wording is narrower than the inventory's stage label, and the report should preserve that distinction rather than smoothing it away.

#### Remaining cautions

Two cautions matter most. First, the historical stage may be narrower than the inventory's plain PWGmc framing, since Ringe and Taylor describe the change as northern WGmc. Second, no validated chronology output exists yet. Until those points are resolved more fully, SC012 should remain out of `report_manifest.tsv`.
