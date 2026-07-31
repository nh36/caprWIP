# Chapter 1. From Proto-Germanic to Proto-Northwest Germanic

## Historical interval

This chapter covers developments that took place within the Proto-Germanic
period, from the inherited consonant system to the first changes that separate
the Northwest Germanic line from the rest of the Germanic family.

The reconstruction labelled Proto-Germanic here is the common ancestor of Gothic,
North Germanic, and West Germanic, reconstructed through the classical comparative
method from attested descendant languages. The label Proto-Northwest Germanic
designates the hypothetical node linking the ancestors of North Germanic (Old
Norse and its relatives) and West Germanic (Old English, Old High German, Old
Saxon, and Old Frisian among others), to the exclusion of Gothic and the other
East Germanic varieties.

## What this chapter contains

The changes implemented in CAPR that belong historically to this stage are few.
The current lexical corpus witnesses only one well-supported change in the
CAPR rule set that is unambiguously Proto-Germanic internal: the simplification
of the cluster [*gm]{.recon} 'consonant group' in the families behind
[*draugma-]{.recon .iv lang=pgmc sort=draugma} 'dream' and [*taugma-]{.recon .iv lang=pgmc sort=taugma} 'team'
[@Kroonen2013, pp. 101, 511].

A second change with a Proto-Germanic historical label in the CAPR implementation,
the allophony of initial labial stops (SC049), belongs here historically but is
checkpointed later in the transducer cascade for computational reasons. Its
chapter placement therefore diverges from its cascade position; the historical
account is given here, and the reader-facing section cross-references this chapter.

The thinness of Chapter 1 is real: the CAPR corpus does not yet have strong
lexical witnesses that establish the relative chronology of early Proto-Germanic
consonant changes. Most of the changes that traditional comparative grammars
treat as Proto-Germanic-stage developments are either not represented in the CAPR
corpus or are implemented as part of the input proto-forms rather than as explicit
rule steps.

## Scope and genealogical context

Changes in this chapter are pan-Germanic in scope: they apply to ancestral forms
that feed both the North Germanic and West Germanic descendants, or they represent
internal Proto-Germanic processes visible across the Germanic family.

The boundary between Proto-Germanic and Proto-Northwest Germanic is not sharp in
the textbook literature. Ringe and Taylor treat many of the traditionally
"Proto-Germanic" changes as part of a shared innovation package that is
diagnostically older than North–West Germanic divergence but not necessarily
earlier than the separation of the East Germanic line
[@RingeTaylor2014, pp. 1--30]. For book purposes, the distinction matters
primarily because it separates the features inherited uniformly from all Germanic
from those shared selectively by North and West Germanic to the exclusion of
Gothic.

## A note on the rule names

The CAPR rules implemented in this chapter carry names beginning with `PGmc`.
Those names are intended as stable internal identifiers, not as claims about
the precise historical stage of every rule so labelled. A rule named `PGmcX`
may in some cases be a later development that affects only the West Germanic
or Northwest Germanic branch; the chapter assignment in this staging map takes
priority over the rule-name prefix for historical organization purposes.
