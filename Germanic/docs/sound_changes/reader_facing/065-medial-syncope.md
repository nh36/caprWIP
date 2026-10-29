# Medial syncope before dentals

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

Loss of medial \emph{*i} before dentals belongs to the late weak-tail history
described by Hogg, Ringe and Taylor, and Fulk
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6]. In Barrack's cascade the corresponding territory is
covered by his syncope rules 347 and 351 [@Barrack1975, pp. 86--87], with
further medial losses at rules 388 and 390, the latter citing \emph{meolc}
'milk' [@Barrack1975, p. 96]; his rules are broader than the
dental-conditioned statement here and are not coextensive with it.

```foma
define OEMedialSyncope FootCtx([
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
]);
```

The historical change is not in fact restricted to pre-dental position: the
handbooks describe a general loss of unstressed medial high vowels in open
syllables after heavy syllables [@RingeTaylor2014, pp. 264--267, §6.7.3;
@Campbell1959, pp. 157--159, §§388--393]. The dental enumeration here is a
deliberately narrow executable statement of the slice of that law required
at this point in the cascade, where high-vowel apocope (SC063, OE High
Vowel Apocope) has already applied and the open-syllable condition of the
handbooks can no longer be expressed. Controlled counterfactual experiments
show the narrowing is load-bearing rather than decorative: extending the
rule to \emph{*u} wrongly syncopates \emph{hēafod} 'head', dropping the
dental restriction destroys \emph{hierfest} 'harvest' and \emph{sċilling}
'shilling', and the faithful open-syllable formulation is vacuous at this
position, while moving it before apocope wrongly reduces \emph{sāwol}
'soul'.

The law is witnessed by the feminine abstracts in \emph{*-iþō}, which
uniformly show syncope: \emph{strengþu} 'strength', \emph{hǣlþ} 'health',
\emph{fȳlþ} 'filth', \emph{þīefþ} 'theft', \emph{wiermþu} 'warmth'
[@Campbell1959, p. 236, §589.6; @Bammesberger1990, pp. 117--118, §4.5].
The corpus tests the type through \emph{fȳlþ}, from \emph{*fūliþō}
[@Kroonen2013, p. 158], whose medial vowel survives in the Old Saxon
cognate \emph{fulitha} and Old High German \emph{fülida}
[@Toller1921, p. 276]: the loss is therefore English, not common West
Germanic. The same word fixes a relative chronology. Had syncope preceded
i-umlaut (SC055, OE I-Umlaut), the deleted \emph{*i} could not have
fronted the root vowel, and the result would have been unattested
\emph{fūlþ} rather than attested \emph{fȳlþ}; umlaut must therefore
precede this syncope. Campbell derives the endingless nominative singular
of these abstracts analogically after the \emph{lār} type
[@Campbell1959, p. 236, §589.6], whereas the cascade reaches the same form
by the regular phonological route through raising and apocope; both
accounts converge on the attested form, and the corpus does not decide
between them. No local ordering with respect to high-vowel apocope itself
can be demonstrated from the present lexicon, since the dental-conditioned
statement applies whether or not the final vowel is still in place.
