# Early Northwest Germanic vowel developments

## Historical discussion

These two developments affect different parts of the vowel system.
[SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization)
monophthongizes unstressed \emph{*ai};
[SC015 PNWGmcILowering](#rule-PNWGmcILowering) represents the disputed lowering
of stressed short \emph{*i}. Their grouping here does not identify them as
successive stages of unstressed-vowel reduction.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the widespread monophthongization of unstressed
\emph{*ai} to a long mid vowel, largely merging with inherited unstressed
\emph{*ē}. Their examples include final dative-singular and nonfinal
inflectional syllables. They nevertheless question a single completed
Proto-Northwest Germanic merger: Runic evidence suggests that some
unstressed diphthongs survived later than others
[@RingeTaylor2014, pp. 25--26]. The stressed development of \emph{*ái}
to \emph{*ā} is treated separately as
[SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## SC014. Monophthongization of unstressed \emph{*ai} (`PNWGmcUnstressedAiMonophthongization`) {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization Ctx([
    {*ai} -> {*ē}
]);
```

The dative-singular endings span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed' carry this change; both give a final \emph{*ē}. If [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the \emph{*ē} is no longer present for shortening, so PGmc [spánnai]{.recon} 'span' yields [*spannē*]{.pred} rather than expected OE *spanne* 'span'. This shows that [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) in the modeled sequence.

## SC015. Lowering of stressed short \emph{*i} (`PNWGmcILowering`) {#rule-PNWGmcILowering}

### The traditional account and its limits

The traditional formulation lowers stressed \emph{*i} to \emph{*e} before a
mid or low vowel in the following syllable. It parallels the better-attested
lowering of \emph{*u} in
[SC017 PNWGmcULowering](#rule-PNWGmcULowering). Campbell's §114 explicitly
states this front-vowel change, while emphasizing its scant English evidence:
OE [nest]{.lex lang=oe} 'nest', [wer]{.lex lang=oe} 'man', and
[spec]{.lex lang=oe} 'bacon' beside [spic]{.lex lang=oe} 'bacon'.
His §§115--116 distinguish the more regular back-vowel development and
blocking before nasal-plus-consonant groups. This is an account of accented
vowels, distinct from the later unstressed developments of
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) and
[SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering)
[@Campbell1959, p. 43, §§114--116].

Fulk likewise accepts vowel-conditioned lowering, interpreting its uneven
distribution through earlier alternations and subsequent paradigmatic
levelling, especially the elimination of lowered vowels. He regards a
Northwest Germanic date as methodologically preferable, without excluding a
Proto-Germanic beginning. His treatment supplies substantial authority for
the central hypothesis represented here, although not for every consonantal
restriction in CAPR. The comparative irregularity is itself part of his
analysis, not evidence that the traditional account was universally accepted
[@Fulk2018, pp. 56--57, §4.3].

### Objections to general vowel-conditioned lowering

Lloyd's strongest objection is the class I participle: inherited short
\emph{*i} survives before the same non-high participial suffix that accompanies
lowered \emph{*u} in class II. He challenges the proposed morphological
links used to explain away this difference. In nouns, he questions whether
the reconstructed high-vowel endings could have supplied enough forms to
restore \emph{*i} throughout a paradigm. Uninflected OHG
[hina]{.lex lang=ohg} 'hence' and [nidana]{.lex lang=ohg} 'from below'
make indiscriminate appeals to case-based levelling still less persuasive
[@Lloyd1966, pp. 738--741].

Cercignani retains a role for assimilation and analogy but disputes uniform
conditioning and chronology across North and West Germanic. His earlier
defence of an inherited phonemic opposition between \emph{*i} and
\emph{*e} concerns a different proposition from the existence of a particular
lowering rule. Crucially, his later paper explicitly warns that the
preceding-velar restriction reported for North Germanic cannot simply be
transferred to West Germanic: Old High German provides counterevidence.
He also recognizes the difficulty of explaining the inherited adverbs and
fish vocabulary by analogy alone
[@Cercignani1979, pp. 75, 82; @Cercignani1980, pp. 129--131].

Ringe and Taylor question a general early West Germanic lowering. For OE
[nest]{.lex lang=oe} 'nest' and [wer]{.lex lang=oe} 'man', they leave open
whether Proto-Germanic already had \emph{*e}. They distinguish the more
extensive southern West Germanic lowering before labial and velar
obstruents from these widely shared correspondences. Their analogical
interpretation of particular strong-verb transfers depends on identifiable
paradigm coincidences. These empirical distinctions deserve consideration
without making independent daughter innovations the default explanation of
every difficulty [@RingeTaylor2014, pp. 34--36].

### Hill's consonant-conditioned alternative

Hill argues that the following consonants offer a more explanatory
generalization than the next vowel. His strongest proposed environments are
tautosyllabic \emph{*z}, the cluster \emph{*st}, and \emph{*r}.
Thus PGmc [iz]{.recon} 'he', [hiz]{.recon} 'this here', and
[mizdōn]{.recon} 'reward' supply the first environment; the nest and man
words supply the others. The contrasting preservation before \emph{*sk}
occurs in inherited vocabulary, including PGmc [wiskō]{.recon} 'wisp',
and cannot readily be dismissed as a late change of inflectional class.
The following table summarizes the principal comparisons
[@Hill2017, pp. 153--156].

| Earlier form | Comparative evidence | Diagnostic value |
| --- | --- | --- |
| PGmc [nistan]{.recon} 'nest' | OE [nest]{.lex lang=oe} 'nest' | Compatible with both following-vowel and \emph{*st} conditioning. |
| PGmc [wiraz]{.recon} 'man' | ON [verr]{.lex lang=on} 'man', OE [wer]{.lex lang=oe} 'man', Gothic *wair* 'man' | Supports lowering before \emph{*r}; Gothic breaking obscures its date. |
| PGmc [mizdōn]{.recon} 'reward' | OE [meord]{.lex lang=oe} 'reward', [mēd]{.lex lang=oe} 'reward', OHG [miata]{.lex lang=ohg} 'reward' | Supports a history with lowering before \emph{*z}, alongside separate consonant and quantity changes. |
| PGmc [fiskaz]{.recon} 'fish' | ON [fiskr]{.lex lang=on} 'fish', OE [fisc]{.lex lang=oe} 'fish' | Retained \emph{*i} before \emph{*sk}, despite the non-high ending. |
| [bitanaz]{.recon} 'bitten', [biðanaz]{.recon} 'awaited' | OE [biten]{.lex lang=oe} 'bitten', [biden]{.lex lang=oe} 'awaited' | Class I participles resist the proposed general vowel-conditioned lowering. |

The inherited root vowel of OE [nest]{.lex lang=oe} 'nest' also has a
comparative etymology independent of the English outcome: Kroonen connects
it with the downward adverb and the zero grade of the root 'sit'.
Hill's Northwest Germanic [nẹstijana]{.recon} 'to nest' and
[lẹstiz]{.recon} 'skill' illustrate how later i-mutation could restore a
high vowel after earlier consonant-conditioned lowering. Such a specified
sound change is stronger evidence than a generic invocation of analogy.
Nevertheless, \emph{*z}, \emph{*st}, and \emph{*r} do not by themselves
define one established natural class: their unification as a single process
remains a hypothesis [@Kroonen2013, p. 391; @Hill2017, pp. 153--156].

### Difficult counterevidence

The participial comparison requires particular care. Hill prints ON
[biðinn]{.lex lang=on} 'awaited', but Fulk discusses
[beðinn]{.lex lang=on} 'awaited' and expressly says that the high-vowel
variant does not occur. Seebold prints the corresponding
[beðenn]{.lex lang=on} 'awaited', allowing either regular lowering or,
preferentially, formal interference from the verb 'bid'. Fulk challenges
the latter explanation because independent early Norse evidence for that
interference is lacking; the English parallels he mentions are late and
never participial. Hill's argument that influence from a long-vowel
infinitive should also have introduced length is substantive, but the
printed discrepancy does not settle the historical alternatives
[@Hill2017, pp. 151--152; @Seebold1970, pp. 94--95;
@Fulk2018, pp. 58--59, especially p. 59, n. 6].

OHG [irh]{.lex lang=ohg} 'chamois leather' is a potential counterexample
to unrestricted lowering before \emph{*r}. Hill acknowledges this and
prefers a loanword analysis. Kroonen instead connects the leather and
he-goat vocabulary with wider European comparanda and reconstructs
[irha-]{.recon} 'he-goat'. These are competing etymological premises.
The inherited analysis would require an explanation under an unrestricted
pre-\emph{*r} law. CAPR's present formulation instead excludes the intervening
velar fricative. Calling the word a loan solely to protect a rule would beg
the question [@Hill2017, p. 156, n. 30; @Kroonen2013, p. 270].

Later phonology can also conceal a genuine difference between early
formulations. In the thistle comparison, a consonant-conditioned trial
lowers the root of selected [θístilas]{.recon} 'thistle', whereas the
incumbent leaves it high. Later i-mutation restores \emph{*i} in the
former path, and both finish as OE [þistles]{.lex lang=oe} 'thistle'.
Agreement of final forms therefore does not establish agreement about
the earlier history. This illustrates the kind of convergence invoked
in Hill's derivative comparisons, without proving every proposed
instance of it [@Hill2017, p. 153].

### Lowering and the history of 'here'

Hill's positive chronological argument begins with early PGmc
[hir]{.recon} 'here', formed like [hwar]{.recon} 'where' and
[þar]{.recon} 'there'. He proposes lowering to
[hẹr]{.recon} 'here', followed by monosyllabic lengthening to
[hẹ̄r]{.recon} 'here'. His dotted vowel indicates a close mid value;
the long result must not automatically be identified with inherited
\emph{*ē₁}. Lengthening first would instead produce a long high
vowel, for which the required general early lowering lacks independent
support [@Hill2017, pp. 148--149, 156--158].

The comparison depends on more than the vowel of Gothic *hēr* 'here'.
Hill relates the long-vowel monosyllables to disyllabic formations with
short vowels. OHG [hiar]{.lex lang=ohg} 'here' contrasts with
[hĕra]{.lex lang=ohg} 'hither', while the inherited disyllabic pronoun
[hwarja-]{.recon} 'which' could precede lengthening of its monosyllabic
base. The short vowel in Gothic *ƕarjis* 'which' consequently does not
require late lengthening of the adverb 'where'. Hill also argues that
North Germanic adverbial variants reflect the interaction of originally
distinct local and directional formations
[@Hill2017, pp. 146--148].

Three inferences should be separated. Shared North and West Germanic
reflexes support an early lowering before \emph{*r}. A Proto-Germanic
date remains possible because Gothic raising could conceal earlier
\emph{*e} before \emph{*z}, while Gothic breaking makes the man word
chronologically ambiguous. Hill's additional argument places lowering
before a lengthening which he reconstructs as Proto-Germanic, thus
positively dating the pre-\emph{*r} change. That conclusion depends on his
adverbial reconstruction and does not independently date lowering before
\emph{*z} or \emph{*st}. Ringe and Taylor retain alternative explanations
for the adverb, including a different pronominal vowel and lengthening
under deictic stress [@Hill2017, pp. 156--158;
@RingeTaylor2014, pp. 36--37].

### The implemented restriction

```foma
define PNWGmcILowering Ctx([
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
]);
```

The left boundary makes the affected vowel the first vowel of the word,
approximating stressed first-syllable lowering. Both plain and acute-marked
short \emph{*i} are handled; absence of an acute is not interpreted as
sentence stresslessness. A non-high vowel must follow one or more members
of the defined nonnasal coronal class: \emph{*d, l, r, s, t, z, ð, θ}.
Intervening nasals, labials, velars, and \emph{*j} are excluded.
Every consonant in the word-initial interval must also be nonvelar.
The operation therefore excludes an onset velar anywhere in that interval,
not just an immediately preceding velar.

The following-vowel condition has direct traditional authority; the exact
consonantal restrictions have more uneven support. Hill's \emph{*st/sk}
contrast does not establish transparency of every admitted coronal.
Cercignani explicitly restricts the reported preceding-velar condition
to its North Germanic evidence. Fulk's corresponding note is likewise
about North Germanic. Howell and Salmons' account of intervening
consonants principally concerns i-umlaut and its failure; it offers a
phonetic comparison, not direct authority for this lowering expression
[@Hill2017, pp. 153--155; @Cercignani1980, p. 130;
@Fulk2018, p. 57, n. 3; @HowellSalmons1988, pp. 96--97].

In particular, OE [hlid]{.lex lang=oe} 'lid' is protected by the onset
prohibition in the current selected derivation. Removing that prohibition
alone produces [*hled*]{.pred}. Independent English evidence for the
general onset restriction has not been established. A more selective
right-hand environment, such as Hill's proposed consonantal conditions,
would leave the dental-stop context untouched without that prohibition.
This identifies a weakness in the present approximation, while leaving
the historical status of a replacement to be decided.

### The three live witnesses and conditional chronology

The current rule changes exactly three selected forms:

| Selection | Selected input | Root-vowel change | Final output |
| --- | --- | --- | --- |
| Meed | [mízdai]{.recon} 'meed' | \emph{*í > *é} before \emph{*zdē} | OE [meorde]{.lex lang=oe} 'meed' |
| Nest | [nístą]{.recon} 'nest' | \emph{*í > *é} before \emph{*stą} | OE [nest]{.lex lang=oe} 'nest' |
| World | [wír-àldu]{.recon} 'world' | \emph{*í > *é} before \emph{*rà} | OE [weorold]{.lex lang=oe} 'world' |

These witnesses have different evidential weight. OE [nest]{.lex lang=oe}
'nest' supports lowering but distinguishes neither the following-vowel
hypothesis nor Hill's \emph{*st} hypothesis. The history of OE
[meord]{.lex lang=oe} 'reward' and [mēd]{.lex lang=oe} 'reward'
supports lowering before \emph{*z}, with separate histories of consonant
loss or rhotacism and vowel quantity. CAPR's selected
[mízdai]{.recon} 'meed' is a dative input, not Hill's nominative
[mizdōn]{.recon} 'reward'. The two must not be used as interchangeable
whole-word reconstructions [@Kroonen2013, pp. 370, 391;
@Hill2017, p. 153].

OE [weþer]{.lex lang=oe} 'wether' instead has the selected masculine
\emph{*wéθruz}, with inherited \emph{*e}. Kroonen's
[weþru-]{.recon} 'wether' and Orel's masculine
\emph{*weþruz}, alongside alternative \emph{*weþraz}, support
that reconstruction. Gothic [wiþrus]{.lex lang=goth} 'lamb, young ram'
provides positive evidence for the *u*-stem. This noun does not require
lowering and is not a live application of
[SC015 PNWGmcILowering](#rule-PNWGmcILowering)
[@Kroonen2013, p. 584; @Orel2003, pp. 459--460].

OE [weorold]{.lex lang=oe} 'world' likewise depends on the chosen
analysis. The selected [wír-àldu]{.recon} 'world' is a mixed-stage
transponent, combining earlier root vocalism with a later ending.
Ringe and Taylor give an already \emph{*e}-bearing Northwest Germanic
[weraldiz]{.recon} 'world', followed by
[weraldu]{.recon} 'world' and [weruld]{.recon} 'world'
[@RingeTaylor2014, p. 326].

With selected [wír-àldu]{.recon} 'world' held fixed, delaying the incumbent
beyond [SC036 OEInterStressRaising](#rule-OEInterStressRaising) produces
[*wuruld*]{.pred} in place of OE [weorold]{.lex lang=oe} 'world'.
[SC036 OEInterStressRaising](#rule-OEInterStressRaising) has raised the weak
vowel, removing the incumbent's non-high trigger.
The observation is genuine but conditional on both input and rule:
the vowel-independent Hill-style trial still lowers before \emph{*r}
after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), while the root-\emph{*e} control
[wér-àldu]{.recon} 'world' produces the expected form under every
tested placement, even without
[SC015 PNWGmcILowering](#rule-PNWGmcILowering). This displacement therefore
does not independently establish that the historical lowering preceded
interstress raising.

### Interim interpretation

Early stressed \emph{*i}-lowering remains a serious comparative hypothesis,
with a substantial traditional account and a consequential consonantal
alternative. A hybrid history would need independently justified component
changes and specific evidence for any subsequent levelling. The present
restricted executable is retained provisionally because neither the full
replacement domain nor the affected lexical premises are sufficiently
settled. Its successful outputs demonstrate computational compatibility,
not the correctness of every historical condition. Explicit competing
formulations make those premises testable without silently changing
lexical inputs to secure the preferred result.
