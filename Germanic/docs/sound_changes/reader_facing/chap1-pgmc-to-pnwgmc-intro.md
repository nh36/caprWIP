# Chapter 1. From Proto-Germanic to Proto-Northwest Germanic

<!-- NOTE: This intro is not currently used by the part-one build. Chapters now
follow contiguous executable-cascade intervals (see
build_reader_facing_local_section_20_docker.sh), and no chapter currently opens
at a Proto-Germanic-stage rule. Retained pending the renaming/retitling pass. -->

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

Chapter 1 contains one reader-facing sound-change section: the positional
allophony of Proto-Germanic \emph{*b}, implemented as `SC049 PGmcBAllophony`.
The rule governs the distribution of \emph{*b} as a stop versus a voiced
bilabial fricative \emph{*β} depending on syllabic environment. Hogg, Ringe
and Taylor, and Luick all identify this distribution as a Proto-Germanic
feature [@Hogg1992, pp. 101--102; @RingeTaylor2014, p. 121; @Luick1914, p. 107].

CAPR implements this rule late in the computational cascade because the
alternation interacts with environments shaped by intermediate rule
applications. The cascade placement therefore diverges from the historical
stage; the reader-facing section notes this divergence explicitly.

One other historically Proto-Germanic change, Gm-simplification
(`SC002 PGmcGmSimplification`), is documented in the book-entry plan and
its literature dossier confirms the source base is narrow (two lexical
families: [draugma-]{.recon .iv lang=pgmc sort=draugma} 'dream' and
[taugma-]{.recon .iv lang=pgmc sort=taugma} 'team'; [@Kroonen2013, pp. 101, 511]).
A reader-facing section for SC002 awaits a stronger explanatory source base
and is not yet assembled in the reader-facing sequence.

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
