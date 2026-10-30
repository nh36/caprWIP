# Medial syncope before dentals

## Historical discussion

Old English lost unstressed medial high vowels in open syllables after
heavy syllables. The handbooks state the law generally, as part of the
late weak-tail history of unstressed vowels: Ringe and Taylor describe a
weight-conditioned loss of medial \emph{*i} and \emph{*u}, and Campbell
surveys the same territory, with Hogg and Fulk in agreement on its late
Old English position [@RingeTaylor2014, pp. 264--267, §6.7.3;
@Campbell1959, pp. 157--159, §§388--393; @HoggPhonology1992, p. 121;
@Fulk2018, p. 91, §5.6]. The loss is English, not common West Germanic:
the continental cognates cited below keep their medial vowels.

The clearest witnesses are the feminine abstracts in \emph{*-iþō}, which
uniformly show syncope: \emph{strengþu} 'strength', \emph{hǣlþ} 'health',
\emph{fȳlþ} 'filth', \emph{þīefþ} 'theft', \emph{wiermþu} 'warmth'
[@Campbell1959, p. 236, §589.6; @Bammesberger1990, pp. 117--118, §4.5].
The corpus tests the type through \emph{fȳlþ}, from \emph{*fūliþō}, a
composite of Kroonen's base \emph{*fūla-} with the abstract suffix
[@Kroonen2013, p. 158]. The medial vowel survives in Old Saxon
[fulitha]{.iv lang=os sort=fulitha role=evidence_form} 'filth' and in
Old High German [fülida]{.iv lang=ohg sort=fulida role=evidence_form}
'filth' [@Toller1921, p. 276].

The same word fixes a relative chronology. Had syncope preceded i-umlaut
([SC055 OEIUmlaut](#rule-OEIUmlaut)), the deleted \emph{*i} could not have fronted the
root vowel, and the result would have been unattested \emph{fūlþ} rather
than attested \emph{fȳlþ}; umlaut must therefore precede this syncope.
Campbell derives the endingless nominative singular of these abstracts
analogically after the \emph{lār} type [@Campbell1959, p. 236, §589.6],
whereas the cascade reaches the same form by the regular phonological
route through raising and apocope; both accounts converge on the attested
form, and the corpus does not decide between them. No local ordering with
respect to high-vowel apocope itself can be demonstrated from the present
lexicon, since the dental-conditioned statement applies whether or not
the final vowel is still in place.

In Barrack's cascade the corresponding territory is covered by his
syncope rules 347 and 351 [@Barrack1975, pp. 86--87], with further medial
losses at rules 388 and 390, the latter citing \emph{meolc} 'milk'
[@Barrack1975, p. 96]; his rules are broader than the dental-conditioned
statement below and are not coextensive with it.

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

```foma
define OEMedialSyncope FootCtx([
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
]);
```

The dental enumeration here is a deliberately narrow executable statement
of the slice of the handbook law required at this point in the cascade,
where high-vowel apocope ([SC063 OEHighVowelApocope](#rule-OEHighVowelApocope)) has already
applied and the open-syllable condition of the handbooks can no longer be
expressed. No handbook restricts the historical syncope to pre-dental
position; the restriction is an architecture-level decision, not a
historical claim.

Controlled counterfactual experiments show the narrowing is load-bearing
rather than decorative: extending the rule to \emph{*u} wrongly
syncopates \emph{hēafod} 'head', dropping the dental restriction destroys
\emph{hierfest} 'harvest' and \emph{sċilling} 'shilling', and the
faithful open-syllable formulation is vacuous at this position, while
moving it before apocope wrongly reduces \emph{sāwol} 'soul'. With a
single admitted firing, the corpus cannot discriminate the dental
enumeration from narrower statements of the same slice; the enumeration
follows the handbook class of weak preterite and comparative
environments not yet in the pipeline. The retained operation represents
the changes presently required by the selected forms; it does not
delimit the whole historical phenomenon.
