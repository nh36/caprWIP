# Ij-contraction

### Sound-change report

#### Historical formulation

SC009 `PWGmcIjContraction` isolates a contraction of `*ijo` to `*iu` in the `friend` family. In the current trace and source material, that family is essentially the whole historical argument.

That narrowness is not incidental. This is exactly the kind of rule whose existence may be historically real while still being too lexically restricted to support broad generalization.

#### Source tradition

Ringe and Taylor describe a roughly similar change of `*ijo` to `*iu` in the word `friend`, giving the pathway PGmc `*frijond-` > PWGmc `*friund` > OE *friond* and related WGmc forms [@RingeTaylor2014, p. 62]. They immediately warn, however, that the word is unique: the sequence `*ijo` with stressed `*i` is so singular that it is inadvisable to attempt wider generalizations from this single history [@RingeTaylor2014, p. 62].

That is enough to justify backend documentation of the phenomenon. It is also strong reason to keep the report modest and explicit about its lexical narrowness.

#### CAPR implementation

CAPR models the contraction with an explicit environment:

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

The implementation carries a stronger general shape than the historical source base does. It should therefore be read as a CAPR formalization of a very narrow lexical development, not as a broad rule independently supported across many families.

#### Place in the cascade

In the inventory ordering, SC009 follows SC008 `PWGmcCoronalWAssimilation` and precedes SC010 `PWGmcJGemination`. In the production cascade it remains inside bundled `PWGmcChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

That means chronology testing is procedurally ready even though the historical source base remains narrow.

#### Order evidence

No validated chronology card exists yet for SC009. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC009 resolves as the sixth rule in that expanded profile.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should be claimed.

#### Interpretation

SC009 is best treated as a cautious backend note rather than a strong core report. The historical change is real enough to record, but the source base itself warns against broad generalization beyond the `friend` sequence.

#### Remaining cautions

The key caution is lexical uniqueness. Any later prose should keep the `friend` family at the center and should not let CAPR's formal rule read like a major chapter-scale West Germanic vowel change. Even with future chronology output, this change may remain better suited to a short note than to a broad standalone discussion.
