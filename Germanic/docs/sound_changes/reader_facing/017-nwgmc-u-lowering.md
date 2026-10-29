# Northwest Germanic u-lowering

## Historical discussion

Northwest Germanic lowered \emph{*u} to \emph{*o} when the following
syllable contained a non-high vowel. Campbell describes the change and
lists *ġeoc* 'yoke' among its regular outcomes [@Campbell1959, pp. 42--43,
§115]; Fulk gives the same word as a standard example — "OIcel. ok, OE
geoc, OHG joh beside juh and OS juk" — and notes the paradigmatic
alternation between lowered and unlowered stems that the conditioning
produced [@Fulk2018, p. 56, §4.3]. A word-initial \emph{*j} does not block
the change: the blocking effect of \emph{j} concerns only a consonantal
\emph{j} standing between the target vowel and the conditioning vowel, as
in the class I weak verbs of the *cnyssan* 'strike' type
[@Fulk2018, p. 56, §4.3]. Ringe and Taylor accordingly reconstruct the
Proto-West Germanic paradigm of 'yoke' with the lowering applied
[@RingeTaylor2014, p. 129].

Regular corpus witnesses include [ġeoc]{.iv lang=oe sort=geoc role=evidence_form} 'yoke', *nosu* 'nose',
*sċofl* 'shovel', and *sorg* 'sorrow'. Where the following syllable kept a
high vowel the lowering did not apply, as in *ġeoguþ* 'youth', whose root \emph{u}
survived [@SieversBrunner1965, pp. 64--65, §92.1].

Regular lowering does not imply that every attested inherited word preserves
the lowered vowel. The masculine noun
[rust]{.iv lang=oe sort=rust role=comparison_form} 'rust' is a lexical residue:
selected PGmc [rústaz]{.recon} 'rust' regularly predicts
[rost]{.recon form_role=regular_output} 'rust'. Orel's alternative
[rustō]{.recon} 'rust' gives the same lowered root; his masculine alternative
is independently supported by Ringe [@Orel2003, p. 309;
@Ringe2017, pp. 247--248]. Since [frústą]{.recon} 'frost' regularly gives
[forst]{.iv lang=oe sort=forst role=comparison_form} 'frost', a general
_-st-_ exemption is unwarranted. The retained *u* remains unexplained,
alongside the other retained-*u* cases such as *bucc* 'buck', *fugol*
'bird', *wulf* 'wolf' and *wulle* 'wool'; their consonantal environments
do not establish a general replacement law [@Campbell1959, p. 43, §115;
@RingeTaylor2014, pp. 27--34]. The lowering law is retained; its non-high
conditioning class includes nasalized long \emph{*ǭ}, not just oral
\emph{*ō}. The independently reconstructed accusative \emph{*wullǭ}
therefore lowers just as the nominative \emph{*wullō} does under the
preferred chronology [@Ringe2017, pp. 242--243]. This does not merge either
ending with trimoric \emph{*ô}. The
[rust lexical discussion](#rust-oe-rust) distinguishes the selected
masculine citation, Orel's alternative and diagnostic paradigm constructions.

### The second root of rainbow

The independent noun *boga* 'bow' supplies an important comparison.
Its short \emph{o} continues inherited \emph{u} lowered before a
following non-high vowel; Kroonen identifies the noun as a masculine
n-stem derived from 'bend'. Colman explicitly gives this early explanation
of *boga*, while Ringe and Taylor include its ancestor among the lowering
examples [@Kroonen2013, p. 82; @Colman2011, pp. 95--96;
@RingeTaylor2014, pp. 27--29].

CAPR extends the same assimilation to the subordinate-stressed root in
\emph{*régna-bùgô} 'rainbow'. The reconstruction retains primary
accent on 'rain' and subordinate accent on 'bow'; these are reconstructed
prosodic properties, not manuscript accent marks. The proposed development
is \emph{*régna-bùgô > *régna-bògô > *régnbògô > *régnbogô},
followed by palatalization of the first velar and the ordinary ending
developments to *reġnboga* 'rainbow'. The early non-high ending still
conditions lowering, and the resulting \emph{ò} retains the grave read by
[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope).
The ordinary removal of that annotation follows syncope.
Neither early lowering nor syncope requires an optional rewrite.

The general early change is source-backed; its extension to this precise
compound and its reconstructed secondary accent is CAPR's phonological
inference. The authorities do not print the complete accented derivation
[@Campbell1959, p. 43, §§115--116;
@HoggGrammar2011, pp. 54--55, §§3.10--3.11;
@Fulk2018, pp. 56--57, §4.3]. Analogy from the independent noun is
conceivable but is not independently demonstrated here. The significant
consequence is chronological: *rainbow* already has \emph{o} before
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
It therefore cannot establish that secondary stress had to disappear
before that late lowering.

Colman's moneyer-name evidence remains a genuine qualification.
*Buga* beside *Boga*, including coin spellings with both vowels, cannot
be dismissed by exempting names from sound change. Transmission to
die-cutters and the interpretation of individual spellings complicate
phonological and dialect attribution. The ordinary noun's regular early
history does not by itself resolve the name's retained vowel
[@Colman2011, pp. 95--98].

## SC017. Lowering of \emph{*u} before following non-high vowels (`PNWGmcULowering`) {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering [Ctx([
    [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
    ]
]) .o. Ctx([
    {*ù} -> {*ò}
        || _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
])];
```

The plain and acute clauses lower the first nucleus; the grave clause
recognizes subordinate root stress without lowering ordinary unstressed
medial \emph{u}. Each uses a consonantal interval without \emph{*j};
the immediately following consonant must not be nasal.
This literal guard is not a claim that every nasal anywhere in the interval
blocks the historical process. Fulk distinguishes tautosyllabic and
heterosyllabic nasal environments [@Fulk2018, p. 56].

The lowering feeds the much later West Saxon palatal-glide spelling
([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)): the \emph{o} that the
scribes wrote in *ġeoc* 'yoke' is the output of this change, so PGmc
[júką]{.recon} 'yoke' passes through \emph{*joką} on its way to the
attested spelling [@Fulk2018, p. 56, §4.3; @RingeTaylor2014, p. 129].
If lowering is placed after
[SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), selected
[núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu*,
PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected
*sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather
than expected *sorg*. These are conditional computational consequences,
not independent proof that those paradigms underwent no levelling.
CAPR provisionally prefers lowering before final raising because it
regularly accounts for these low-root forms without additional,
individually unproved analogical generalizations. Nose already involves
earlier stem remodelling, and the retained high vowels of wool and love
remain a genuine cost of that preference. The main comparison of Fulk,
Ringe and Taylor, and Stiles, including the Runic evidence and the
plausible but unproved nominative-generalization account of wool, is in
[SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising).
