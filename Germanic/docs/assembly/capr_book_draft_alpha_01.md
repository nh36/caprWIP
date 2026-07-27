\mainmatter

# Introduction

## From sound law to derivation

Historical linguists ordinarily test an etymology by carrying a reconstructed form through the sound changes that separate it from its alleged reflex. Most such derivations remain implicit. A scholar knows that Proto-Germanic \emph{*p} yields Old English \emph{f}, that West Germanic \emph{*z} became \emph{r} under the appropriate conditions, and that one change must have preceded another because the reverse order produces the wrong form. For a single word this mental arithmetic presents little difficulty. Across hundreds of words and scores of interacting changes it becomes treacherous. Each step may look familiar while the derivation as a whole is false.

In computer-assisted phonological reconstruction (CAPR), I represent each sound law as a finite-state transducer and compose the transducers in the order argued for below. The resulting cascade applies every change without discretion: the same rule, with the same environment, reaches every eligible form. A proposed reconstruction either yields the Old English comparator or it does not. Moving a rule may repair one derivation and destroy another. Both results deserve attention, for a failure locates the point at which phonology ceases to suffice and philology must decide among analogy, borrowing, dialect mixture, uncertain attestation, or a faulty reconstruction.

No new principle is involved. The Neogrammarians already demanded exceptionless sound laws and an account of apparent exceptions [@OsthoffBrugmann1881]. Their formula was the \emph{Ausnahmslosigkeit der Lautgesetze}. Formalization merely enforces that demand mechanically: every eligible form bears the stated consequences. The computer cannot decide which reconstruction is historically defensible, but it prevents the investigator from forgetting what that reconstruction entails.

I apply this method to the development of Proto-Germanic and early West Germanic forms into Old English. Germanic makes a severe test. Its historical grammar rests on two centuries of philological labor, while Old English offers abundant but orthographically and dialectally varied testimony [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. A computational account cannot plead scarcity of evidence. It must reproduce familiar developments, identify the evidence for their order, and explain why its input sometimes differs from the headword printed in an etymological dictionary.

## The formal claim

A sound change defines a relation between strings. For each etymology I supply a reconstructed input to an ordered series of such relations and compare the result with an Old English form. Kaplan and Kay demonstrated that the familiar rewrite rules of phonology admit a finite-state interpretation [@KaplanKay1994]; Foma gives that interpretation executable form [@Hulden2009]. A toy rule deleting final \emph{*z} may be written:

```foma
define ToyFinalZLoss [{*z} -> 0 || _ .#.];
```

The notation states a target, an output, and an environment. Actual rules also refer to segment classes, stress, syllable weight, word boundaries, and the output of earlier changes. A loose prose formulation can conceal choices that code must resolve. Does the rule affect every vowel or only short vowels? Does a following consonant block it? Does it apply before or after the loss of a final syllable? A transducer forces each question into the open.

Order gives the cascade its historical content. An early change may create the environment for a later one and thus feed it; alternatively, it may remove that environment and bleed it. A word affected by both changes can therefore establish their relative chronology. Other changes commute across the available lexicon: reversing them alters no checked output. Such a result does not prove simultaneity or historical indifference. It shows only that the present evidence fails to order them. Throughout this book I distinguish chronology compelled by the tested forms from placement adopted on the authority of the historical grammars.

Backward reconstruction requires a further restriction. An unrestricted inverse transducer will propose formally possible strings that no Germanic language could have inherited. I therefore restrict backward reconstruction with an inventory and a statement of permissible ancestral forms. Reconstruction always combines correspondences with a theory of what could count as a word in the \emph{Grundsprache}; this restriction states that theory rather than leaving it tacit.

## Inputs, targets, and success

I compare a selected earlier Germanic form with a selected Old English target. Neither selection is innocent. Dictionaries cite lexemes, but sound change operates on word-forms. The ancestor of an Old English plural, preterite, or oblique case may differ from the reconstructed lemma in precisely the material on which a later sound law acts. Kroonen and Orel provide indispensable lexical reconstructions, while the grammars often supply the paradigm history needed to choose the actual input [@Orel2003; @Kroonen2013; @RingeTaylor2014].

I therefore distinguish the citation reconstruction from the transducer input. The former identifies the etymon; the latter represents the paradigm cell or remodeled stem whose history is at issue. Where the two differ, the lexical entry states the difference and argues for it. This prevents a convenient input from masquerading as a received reconstruction. An unmotivated alteration made solely to secure the desired output would empty the exercise of historical meaning.

The distinction is concrete in Old English [*sċuldrum*]{.iv lang=oe sort=sculdrum source_ref="Germanic/docs/assembly/capr_book_intro_alpha_01.md:33"} ‘shoulders, dative plural’. Its inflectional history requires an input of the type [*skúldramiz*]{.iv lang=pgmc display=*skúldramiz sort=skuldramiz source_ref="Germanic/docs/assembly/capr_book_intro_alpha_01.md:33"}; the singular headword represents a different paradigm cell.

The target also requires judgment. Old English spelling varies by date, dialect, manuscript, and editorial practice. The cascade may produce an internal phonological symbol that an orthographic transducer then maps to a normalized written form. A string match at this final stage cannot by itself establish an etymology; conversely, a superficial spelling mismatch need not disprove one. I treat phonological development and orthographic normalization as separate operations so that exact computation does not confuse notation with history.

Within these limits a successful derivation has three senses. It succeeds formally when the output string matches the target. It succeeds philologically when the chosen input and comparator are the proper forms to compare. It succeeds historically when the proposed path agrees with the wider Germanic evidence. The first kind of success is cheap. The argument of the book concerns the conjunction of all three.

## The evidence of failure

Regular sound change makes irregularity legible. If an inherited form refuses to pass through an otherwise successful cascade, the mismatch demands a name. Analogy may have replaced the expected reflex with a form drawn from another paradigm cell. Borrowing may have introduced the word after the relevant changes. A dialectal form may lie outside the modeled West Saxon path. The target may be late, corrupt, or normalized beyond what the manuscript evidence warrants. Finally, either the reconstruction or the rule may be wrong.

These possibilities should not be suppressed by narrow, lexeme-specific “sound laws.” A system that derives every target by multiplying exceptions has only encoded its answers. I instead distinguish several classes of non-regular result: attested variants, early and late analogy, reconstructed Old English comparators, known but unmodeled remodeling, and unexplained exceptions. The categories are claims, not housekeeping labels. They identify where regular phonology ends and what additional history the evidence requires.

This treatment follows the original Burmish CAPR work, in which resistant forms often disclosed loans or mistaken cognate assignments. Old English shifts the balance toward morphology and analogy, but the methodological advantage remains the same. Failure concentrates inquiry. It tells us which assumption—input, target, environment, order, or lexical history—must bear the explanation.

## Evidence for relative chronology

The chronology chapters combine three kinds of evidence. First come the statements of the standard historical grammars. These establish the received description and often the broad order of developments [@Campbell1959; @Hogg1992; @RingeTaylor2014; @Fulk2018]. Second come individual witness words. A derivation that succeeds under one order and fails under the reverse order supplies direct lexical evidence for that relation. Third come exhaustive order tests across the active dataset. These reveal whether an apparently decisive relation is local, whether other words contradict it, and how far a rule can move without disturbing any output.

Suppose that a consonant change creates the environment for a later vowel change. Under the received order both apply and the Old English target emerges. Reverse them and the vowel change misses its environment. The word then supports the priority of the consonant change. The converse case is equally informative: if an early rule creates a segment that a later rule would wrongly alter, the creating rule must follow the other. When every checked form remains unchanged under reversal, the lexical evidence leaves the order open even if philological considerations still favor one placement.

Sims-Williams argues for mechanizing precisely this kind of reasoning [@SimsWilliams2018]. Computation does not replace the historical argument; it makes the extent of that argument measurable. A traditional chronology may prove correct but less tightly constrained than its customary presentation suggests. A relation described as local may in fact rest only on a broad terminus. Such negative results are salutary. They separate what the data demonstrate from what a convenient exposition merely presupposes.

## Rules and words

The book accordingly moves twice through the same history. Part I begins with the ordered rules. For each development it states the historical problem, gives the rule in formal notation, and examines the evidence for placement. The code appears because it is part of the claim, but the code-name is never an explanation. `OEIUmlaut`, for example, is only a rule name; its linguistic content lies in the stated environment, the historical discussion, and the words whose derivations depend upon it.

Part II begins with the words. Each entry identifies the reconstruction, the selected input, the Old English comparator, and the derivational class. A trace shows which rules altered the form; the accompanying prose explains the philological decisions that the trace cannot make. Short entries record ordinary derivations. Longer ones treat doubtful reconstructions, variant attestations, paradigm-cell selection, or analogy. The asymmetry is intentional: equal database rows do not warrant equal historical discussion.

The reader can thus move in either direction. A chronology chapter names the lexical witnesses that constrain a rule; their entries display the complete derivations. A lexical entry invokes a change; the corresponding chapter explains its formulation and place in the cascade. The index verborum provides a third route through the material, gathering reconstructed and attested forms by language.

## Reproducibility and disagreement

An executable derivation identifies the exact point of disagreement. One reader may accept a sound change but reject its environment; another may accept the rule and dispute its order; a third may object to the selected paradigm cell or to the normalization of the Old English target. Each objection addresses a recorded decision. Given the same inputs, rules, and order, the stated outputs follow. Reproducibility here concerns those consequences, not the surrender of philological judgment to an algorithm.

Prose can sound settled while concealing several incompatible derivations. Code is less accommodating. A rule that is too broad damages words it was never designed to explain; one that is too narrow leaves legitimate reflexes untouched. A reconstruction plausible in isolation may fail after three later changes. The resulting embarrassment is a virtue of the method. Applying every rule to the whole lexicon subjects local analyses to a global test.

The converse danger is false precision. A deterministic cascade may tempt the reader to mistake exact strings for exact history. Every result still depends on choices about segmentation, symbol inventory, reconstruction, morphology, dialect, chronology, and orthography. I therefore cite the philological sources, display the selected forms, preserve unresolved exceptions, and distinguish tested order from source-based order. Those choices remain accountable to philology.

## The argument

A book must advance an argument. Mine is that traditional rule-based reconstruction becomes clearer when every proposed derivation can be executed, every rule must face the whole lexicon, and every failure is reported. The Germanic-to-Old-English case shows both the power and the boundary of that claim. Much of the history admits a coherent ordered account. The residue does not disappear: it resolves into morphology, analogy, variation, borrowing, imperfect attestation, and a small number of genuine problems.

The sound-change chapters ask how tightly the lexical evidence constrains the cascade. The lexical chapters ask whether individual etymologies survive that cascade without philological sleight of hand. Neither inquiry suffices alone. A formal system that reaches the targets by hiding doubtful inputs is bad historical linguistics; elegant prose that never reproduces its derivations is an incomplete formal account. Executable derivations make those two standards answer to one another.

\part{Sound changes, formalization, and relative chronology}

# The ordered sound-change sequence

## Scope and orientation

The sequence begins with early West Germanic consonant and vowel changes and ends with Old English r-metathesis.

Rhotacism, brightening, breaking, umlaut, and apocope alternate with narrowly conditioned changes whose relative order rests on particular witness words.

The evidence ranges from broadly attested sound laws to lexical constraints that establish only one chronological boundary.

### Numbering note

The sequence follows the established rule numbering.

SC038, SC062, and SC084 mark technical or prosodic stages rather than sound changes; SC077 is unused.

## West Germanic rhotacism

### Historical discussion

Hogg states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Hogg1992, p. 37]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

The label [SC003 PGmcRhotacism](#rule-PGmcRhotacism) is historically misleading: the change is a later West Germanic rhotacism, not a Proto-Germanic one. It is also distinct from [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant becomes \emph{*r}.

### SC003. West Germanic rhotacism (`PGmcRhotacism`) {#rule-PGmcRhotacism}

```foma
define PGmcRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

Breaking supplies the decisive upper boundary. If rhotacism is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*líznōjaną} yields *lirnian* rather than expected OE *liornian* ‘learn’, PGmc \emph{*líznōθi} yields *lirnaþ* rather than expected *liornaþ*, PGmc \emph{*líznô} yields *lirna* rather than expected *liorna*, and PGmc \emph{*mízdai} yields *merde* rather than expected OE *meorde* ‘meed’. Moving rhotacism earlier within the tested range changes none of the checked forms.

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. Its placement after the earlier loss of final \emph{*z} rests on the historical analyses cited above.

\newpage

## Proto-West-Germanic ai-monophthongization

### Historical discussion

Ringe and Taylor treat the reduction of unstressed \emph{*ai} as one of the major early vowel shifts shared across the Northwest Germanic area [@RingeTaylor2014, pp. 40--41].

The historical support is strongest for unstressed \emph{*ai}, especially word-finally. The rule extends the change to nonfinal \emph{*ai > *ā}, a generalization stated more sharply than in the current handbook discussion.
Both developments have inherited \emph{*ai} as their input.

### \CAPRRuleHeading{SC004. Proto-West-Germanic ai-monophthongization}{PWGmcAiMonophthongization} {#rule-PWGmcAiMonophthongization}

```foma
define PWGmcAiMonophthongization [
    [{*ai} -> {*ē} || _ .#.]
    .o.
    [{*ai} -> {*ā}]
    .o.
    [{*ái} -> {*ā}]
];
```

The soul form fixes the relation to interstress raising. If monophthongization is delayed until after that change, PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’. No earlier placement changes a checked output.

This witness proves that monophthongization preceded interstress raising; it says nothing about the date of the wider nonfinal \emph{*ai > *ā} generalization. The word-final merger with long mid \emph{*ē} belongs among the early Northwest Germanic vowel shifts; the broader chronology remains less certain.

\newpage

## Unstressed \emph{*a}-raising before final \emph{*m}

### Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

### SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`NWGmcAToUBeforeM`) {#rule-NWGmcAToUBeforeM}

```foma
define NWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*skúldramiz} yields *sċoldrum* rather than expected OE *sċuldrum*; earlier placements converge on the expected output. The `shoulder` family therefore tests the chronology, while the inflectional endings justify restricting the change to noninitial unstressed material before \emph{*m}.

The evidence is confined to inflectional
material.

\newpage

## Early i-apocope

### Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* and *geogup* examples belong to the same pattern [@Campbell1959, §332].

The ending vowel disappears in a weak suffixal environment early enough to block later umlaut. This anti-umlaut chronology distinguishes the change from later final-vowel losses.

### SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

The absence of umlaut in *geoguþ* ‘youth’ provides the historical argument for early deletion. The ordered derivation supplies a different test: if apocope is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*skáwōθi} yields *sċēaweþ* rather than expected OE *sċēawaþ*.

Early i-apocope must therefore precede the long-diphthong development. Moving it earlier within the tested range leaves every checked output unchanged; its early date rests on the anti-umlaut evidence, not on a lower boundary supplied by the witness words.

\newpage

## Final \emph{*ō}-lowering before \emph{*r}

### Historical discussion

Ringe and Taylor treat the West Germanic lowering of final bimoric \emph{*ō} before word-final \emph{*r} as a specific inherited development and illustrate it above all with the families behind *fēower* ‘four’ and *wæter* ‘water’ [@RingeTaylor2014, pp. 58--59].

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

### \CAPRRuleHeading{SC007. Lowering of final bimoric \emph{*ō} before \emph{*r}}{PWGmcFinalOrLowering} {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc \emph{*wátōr} yields *water* rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no checked output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. The *fēower* ‘four’ and *wæter* ‘water’ families support the narrow environment before word-final \emph{*r}; no broader lowering of \emph{*ō} is attested.

\newpage

## Coronal-w assimilation

### Historical discussion

Ringe and Taylor treat the assimilation of `*dw` and `*zw` to `*ww` as a shared Proto-West-Germanic innovation and support it through the `four` family and plural-pronominal forms such as `you` and `your` [@RingeTaylor2014, pp. 56--57].

The historical support rests on a small witness set. Both coronal inputs
assimilate before \emph{*w}, but only the numeral and the pronominal forms
directly support the generalization.

### \CAPRRuleHeading{SC008. Assimilation of coronal consonants before \emph{*w}}{PWGmcCoronalWAssimilation} {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation must create \emph{*ww} while simplification can still reduce it. If [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*fédwōr} yields *fēowwer* rather than expected OE *fēower* ‘four’. Earlier placements alter no checked output.

The numeral fixes that relative order. The pronouns extend both input clusters beyond `four`; the earlier boundary remains undetermined.

\newpage

## \emph{ij}-contraction in \emph{friend}

### Historical discussion

Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family, with the pathway PGmc \emph{*frijond-} > PWGmc \emph{*friund} > OE *frēond* 'friend' [@RingeTaylor2014, p. 62]. The same source immediately warns that the `*ijo` sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62].

The change concerns a rare sequence confined to the `friend` family and cannot safely be generalized into a broadly productive rule.

### SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

Only the `friend` family tests this contraction. If the rare \emph{*ijō} sequence survives until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc \emph{*fríjōndz} yields *friund* rather than expected OE *frēond* 'friend'; moving contraction earlier within the tested range changes no checked output.

That single contrast places [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) before diphthong leveling but gives no lower boundary. It cannot establish a productive sound law beyond this family, precisely the reservation made by Ringe and Taylor.

\newpage

## West Germanic j-gemination

### Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

The change applies specifically after a short vowel before \emph{*j}, not to geminate consonants generally.

### SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

```foma
define PWGmcJGemination [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

OE *nett* 'net' fixes the order because the syllabic-\emph{j} development would remove the glide that conditions gemination. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) precedes [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc \emph{*nátją} yields *nete* rather than expected OE *nett* 'net'. Earlier movement of gemination changes no checked output.

The chronology is phonologically transparent: the consonant must geminate before \emph{*j} ceases to be consonantal. The witness establishes no earlier boundary.

\newpage

## Syllabic j after final-vowel loss

### Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

The sources establish the development, although the checked lexicon supplies
little independent evidence for its position. Its scope is postconsonantal j,
not high-vowel vocalization generally.

### SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

The same PGmc \emph{*nátją} witness supplies the only firm boundary. Placing [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) before [SC010 PWGmcJGemination](#rule-PWGmcJGemination) yields *nete* rather than expected OE *nett* 'net'; moving it later changes no checked output.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* and *rice* as outcomes. The lexicon adds only that vocalization followed gemination, not where it falls among subsequent changes.

\newpage

## \emph{lþ}-voicing

### Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan*, *beald*, *wuldor*, and *gylden* [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold*, and *feld* [@Campbell1959, p. 169, §414].

The comparative evidence supports \emph{lþ > ld} most clearly in northern West
Germanic, not as an unqualified pan-PWGmc development.

### SC012. \emph{lþ}-voicing (`PWGmcLThVoicing`) {#rule-PWGmcLThVoicing}

```foma
define PWGmcLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

The `field`, `fold`, `gold`, and `wold` families preserve \emph{*lþ} to \emph{*ld}, but none dates the change against a neighboring rule. Every checked output remains unchanged when the voicing is moved in either direction.

Comparative reconstruction therefore establishes northern West Germanic \emph{lþ > ld}, but the witness forms fix no date. Neither a pan-PWGmc attribution nor an exact local placement follows from the evidence presented here.

\newpage

## Dental hardening

### Historical discussion

Ringe and Taylor state directly that in PWGmc voiced dental fricative `*ð` became stop `*d` in all positions [@RingeTaylor2014, p. 43].

The change is systemic across early West Germanic and extends beyond any one
lexical family.

### SC013. Dental hardening (`PWGmcDentalHardening`) {#rule-PWGmcDentalHardening}

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

Dental hardening has systemic scope: voiced fricative \emph{*ð} became stop \emph{*d} throughout early West Germanic. Moving [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) earlier or later changes no checked output.

Comparative evidence establishes the sound law; the present lexicon leaves its exact position approximate.

\newpage

## Early unstressed vowel changes

### Historical discussion of the earliest unstressed vowel changes

The first change removes the remaining diphthongal quality of unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* ‘world’. Their chronological evidence differs: monophthongization is historically clear but not closely dated by the witness forms, whereas \emph{*i}-lowering has a diagnostic later boundary.

### Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e} [@RingeTaylor2014, pp. 37--41]. The historical change is thus established, although the order test determines no closer relative position.

### \CAPRRuleHeading{SC014. Monophthongization of unstressed \emph{*ai}}{NWGmcUnstressedAiMonophthongization} {#rule-NWGmcUnstressedAiMonophthongization}

```foma
define NWGmcUnstressedAiMonophthongization [
    {*ăi} -> {*ē}
];
```

Moving [SC014 NWGmcUnstressedAiMonophthongization](#rule-NWGmcUnstressedAiMonophthongization) earlier or later changes no checked form. The lexicon therefore cannot refine its source-based placement among the earliest Northwest Germanic simplifications of unstressed vowels.

Ringe and Taylor's merger of unstressed \emph{*ai} with \emph{*e} establishes the historical development; the current witnesses do not distinguish its position relative to neighboring changes.

### Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* and *weoruld* [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 NWGmcILowering](#rule-NWGmcILowering) with a firmer lexical basis than the preceding change.

### SC015. Leveling of early unstressed front vowels (`NWGmcILowering`) {#rule-NWGmcILowering}

```foma
define NWGmcILowering [
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

The *weorold* and *weoruld* variants turn the general source claim into an ordering test. If [SC015 NWGmcILowering](#rule-NWGmcILowering) is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc \emph{*wír-àldu} yields *wuruld* rather than expected OE *weorold* ‘world’; earlier movement changes no checked output.

The derivation thus fixes front-vowel leveling before interstress raising while leaving its earlier boundary open.

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 NWGmcULowering](#rule-NWGmcULowering) follow with a more tightly constrained local chronology.

\newpage

## West Saxon palatal glide and u-lowering

### Historical discussion of West Saxon palatal glide and u-lowering

The derivation of *ġeoc* ‘yoke’ passes through both rules. Campbell treats the West Saxon rising-diphthong spellings before back vowels, while the same handbook tradition describes the lowering of \emph{u} before a following non-high vowel separately [@Campbell1959, p. 17, §44; @Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

The first change creates the West Saxon \emph{ġeoc} type; the second carries the same material into the subsequent vowel history.

### Historical discussion of West Saxon palatal glide

West Saxon spellings such as *ġeoc* ‘yoke’, *ġeong* ‘young’, and *ġeoguþ*
‘youth’ reflect an early development before back vowels. Campbell gives the
most direct handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

The sources establish [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), although the checked forms provide only a later boundary.

### \CAPRRuleHeading{SC016. West Saxon palatal glide before back vowels}{OEWsPalatalGlide} {#rule-OEWsPalatalGlide}

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

OE *ġeoc* ‘yoke’ fixes the close relation between glide insertion before back-vocalic \emph{u} and the following change.

If glide insertion follows [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’; earlier placement changes no checked output. The witness therefore dates [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) before u-lowering without supplying an earlier boundary. The *ġeoc*, *ġeong*, and *ġeoguþ* material establishes the lexical scope of the West Saxon development.

### Historical discussion of u-lowering

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

[SC017 NWGmcULowering](#rule-NWGmcULowering) thus rests on a broader source base than the preceding West Saxon rule.

### \CAPRRuleHeading{SC017. Lowering of \emph{*u} before following non-high vowels}{NWGmcULowering} {#rule-NWGmcULowering}

```foma
define NWGmcULowering [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* ‘yoke’, *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc \emph{*júką} yields *ġoc* rather than expected OE *ġeoc* ‘yoke’. After [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*núsō} yields *nusu* rather than expected *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. The two witness sets place [SC017 NWGmcULowering](#rule-NWGmcULowering) after glide formation and before final long-\emph{o} raising.

\newpage

## Stressed monosyllable \emph{*ō}-raising

### Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

The change is historically secure, but the tested forms determine no close relative position for it.
Its input is final \emph{*ō} in a stressed monosyllable.

### \CAPRRuleHeading{SC018. Raising of final stressed monosyllabic \emph{*ō}}{NWGmcStressedMonosyllableORaising} {#rule-NWGmcStressedMonosyllableORaising}

```foma
define NWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

Campbell's *cū*, *hū*, and *tū* establish final stressed monosyllabic \emph{*ō} > \emph{*ū}.

Reversing [SC018 NWGmcStressedMonosyllableORaising](#rule-NWGmcStressedMonosyllableORaising) with neighboring changes leaves every checked output unchanged. The sound change is secure, but its exact position in the early history of long vowels rests on the handbooks.

\newpage

## Final long-\emph{o} raising and final \emph{z}-deletion

### Historical discussion of final long-\emph{o} raising and final \emph{z}-deletion

The same final-syllable structure undergoes both changes. Ringe and Taylor describe the change of unstressed final non-nasalized long \emph{*ō} to short \emph{*u}, while Hogg and Crist treat word-final \emph{*z} loss as a separate later step in West Germanic [@RingeTaylor2014, p. 30; @Hogg1992, p. 37; @Crist2002, p. 1].

The derivation of *ræste* ‘rest’ fixes their order: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must still see final \emph{*ō}, and [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) removes final \emph{*z} only afterward.

### Historical discussion of final long-\emph{o} raising

The first change in the pair is the Northwest Germanic raising of unstressed final long \emph{*ō} to \emph{*u}. Ringe and Taylor state that development directly in comparative terms [@RingeTaylor2014, p. 30].

The change supplies the final vowel of forms such as *nosu*, *sċofl*, and
*sorg*.

### \CAPRRuleHeading{SC019. Raising of final unstressed long \emph{*ō}}{NWGmcFinalLongORaising} {#rule-NWGmcFinalLongORaising}

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’ fix its lower boundary.

Before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*núsō} yields *nusu* rather than expected OE *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. After [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*rástōz} yields *rast* rather than expected *ræste* ‘rest’. These failures place [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.

### Historical discussion of final \emph{z}-deletion

The second change is the loss of word-final \emph{*z}. Standard handbook tradition and Crist's West Germanic discussion establish the development within broader accounts of inflectional morphology [@Hogg1992, p. 37; @Crist2002, p. 1].

Final z-loss follows long-o raising and precedes the later changes in weak
syllables.

### SC020. Deletion of word-final \emph{*z} (`PGmcFinalZDeletion`) {#rule-PGmcFinalZDeletion}

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
```

The chronology of word-final \emph{*z}-loss is unusually well delimited: *ræste* supplies its early boundary, while later weak syllables supply its late boundary.

Before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*rástōz} yields *rast* rather than expected OE *ræste* ‘rest’. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*bébruz} yields *befro* rather than expected *befer* ‘beaver’, PGmc \emph{*kwéðuz} yields *cwedo* rather than expected *cwedu* ‘cud’, and PGmc \emph{*félθuz} yields *feldo* rather than expected *feld* ‘field’, alongside eight other newly failing rows. Final \emph{z}-loss therefore follows [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) and precedes [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The \emph{*rástōz} derivation fixes the local relation to [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising). The distant boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) shows only that word-final \emph{*z}-loss precedes the later weak-syllable sequence; its placement within that wider interval follows the handbook chronology after final \emph{*ō}-raising.

\newpage

## Unstressed \emph{*o}-raising

### Historical discussion

The older history of *heofon* ‘heaven’ requires an unstressed-vowel adjustment before the later reshaping of medial vowels in Old English. Campbell derives the \emph{-o-} from an earlier unstressed environment, and Ringe and Taylor place the same family within the wider West Germanic record [@Campbell1959, pp. 155--156, §373; @RingeTaylor2014, p. 287].

The change is historically recognizable, but the checked forms provide only a later boundary.

### \CAPRRuleHeading{SC021. Raising of unstressed \emph{*o} before later \emph{*u}}{NWGmcUnstressedORaising} {#rule-NWGmcUnstressedORaising}

```foma
define NWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xémonų} yields *heofun* rather than expected OE *heofon* ‘heaven’; earlier placement changes no checked output. The witness therefore places [SC021 NWGmcUnstressedORaising](#rule-NWGmcUnstressedORaising) before medial unstressed-\emph{u} lowering.

Nothing in the present lexicon supplies the corresponding earlier boundary.

\newpage

## \emph{mn}-dissimilation

### Historical discussion

The handbooks describe the history of \emph{mn} sequences as a limited
descriptive pattern. Campbell discusses both loss of unstressed material and
later assimilation in forms of this type, including the special status of
*month*-type evidence [@Campbell1959, pp. 189, 195, §§470, 484].

The pattern is historically established, but the checked forms do not constrain its position.

### SC022. Dissimilation of \emph{mn} sequences (`NWGmcMnDissimilation`) {#rule-NWGmcMnDissimilation}

```foma
define NWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _
           EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
];
```

Campbell's *heofon* and *month* material supports early \emph{m} > \emph{β}
before a later nasal, but supplies no ordering witness.

Moving [SC022 NWGmcMnDissimilation](#rule-NWGmcMnDissimilation) earlier or later leaves every checked output unchanged. Its place among the early consonantal changes rests on the handbook account of \emph{mn}-dissimilation.

\newpage

## N-stem \emph{n}-loss

### Historical discussion

The broader history is the reduction and leveling of older n-stem endings in West Germanic. Ringe and Taylor describe the resulting syncretism in the n-stems, which is the wider morphological setting for the narrower step isolated here [@RingeTaylor2014, p. 72].

The path to *dōn* ‘do’ provides the clearest witness, but the change remains narrow in scope.

### SC023. Loss of n-stem \emph{*n} in final position (`NWGmcNStemNLoss`) {#rule-NWGmcNStemNLoss}

```foma
define NWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

After [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*dōną} fails entirely (\emph{+?}) instead of yielding expected OE *dōn* ‘do’; earlier placement changes no checked output. Thus [SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss) must feed the later apocope.

This failed derivation supplies a terminus ante quem, while the lower boundary remains unattested.

\newpage

## Long \emph{ē}-lowering

### Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

The change is historically recognizable, but the checked forms provide only a later boundary.

### \CAPRRuleHeading{SC024. Lowering of long \emph{ē} before non-nasal consonants}{NWGmcLongELowering} {#rule-NWGmcLongELowering}

```foma
define NWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

After [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), long \emph{ē} > \emph{ǣ} can no longer produce the expected West Saxon forms: PGmc \emph{*skḗpą} yields *sċīep* rather than OE *sċēap* ‘sheep’, and PGmc \emph{*jḗrą} yields *ġīer* rather than *ġēar* ‘year’. Earlier placement changes no checked output, so [SC024 NWGmcLongELowering](#rule-NWGmcLongELowering) has a secure upper boundary.

Its lower boundary remains a matter of handbook chronology.

\newpage

## Long \emph{ē} nasal-rounding

### Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* ‘month’ and *mōna* / *mōn*-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

The change is historically recognizable, but the tested forms supply no close relative chronology.

### SC025. Rounding of long \emph{ē} before nasals (`NWGmcLongENasalRounding`) {#rule-NWGmcLongENasalRounding}

```foma
define NWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

Reversing [SC025 NWGmcLongENasalRounding](#rule-NWGmcLongENasalRounding) with neighboring changes leaves every checked output unchanged. Its position beside the other \emph{ē}-developments therefore follows the handbooks.

\newpage

## Nasal spirant changes

### Historical discussion of nasal loss before spirants and compensatory lengthening

The two rules state successive phases of a single development. Campbell
describes nasal loss before voiceless spirants with compensatory lengthening and
nasalization of the preceding vowel. Ringe and Taylor assign the same outcomes
to inherited northern West Germanic, before late Old English
[@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

[SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the nasal-plus-spirant sequence remains present; [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal. The first rule must therefore precede the second.

### \CAPRRuleHeading{SC026. Lengthening before nasal plus spirant}{NWGmcNasalSpirantLengthening} {#rule-NWGmcNasalSpirantLengthening}

```foma
define NWGmcNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];
```

All three witnesses require the vowel adjustment while the nasal is still present. If [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) follows [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. Earlier placement changes no checked output. The evidence requires lengthening to precede nasal loss without supplying a lower boundary, in agreement with the handbook treatment of the two as successive phases.

### SC027. Loss of the nasal before spirants (`NWGmcNasalSpirantLoss`) {#rule-NWGmcNasalSpirantLoss}

```foma
define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

The converse test fixes the same boundary: placing [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) before [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) produces the same errors in *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’. Later placement changes no checked output. These forms prove that the vowel was adjusted before the nasal disappeared; they provide no upper boundary for the loss.

\newpage

## Preconsonantal \emph{*x}-loss

### Historical discussion

Campbell explicitly treats loss of \emph{x} and gives forms such as *fléam* ‘flight’ and *hēla* ‘heel’ as examples of the same broad development [@Campbell1959, p. 186, §461].

The historical evidence is firmer than the chronology: the checked forms do not constrain the rule's position.

### SC028. Loss of preconsonantal \emph{*x} (`NWGmcPreconsonantalXLoss`) {#rule-NWGmcPreconsonantalXLoss}

```foma
define NWGmcPreconsonantalXLoss [
    {*x} -> 0 || _ {*s} EnglishStarConsonant
];
```

No witness word dates preconsonantal \emph{*x}-loss before \emph{*s} plus another consonant: moving [SC028 NWGmcPreconsonantalXLoss](#rule-NWGmcPreconsonantalXLoss) in either direction leaves every checked output unchanged. Its position within this stretch therefore rests on the handbook chronology for \emph{x}-loss.

\newpage

## Awj glide formation and au-fronting

### Historical discussion of awj glide formation and au-fronting

The *hay* and *strew* material undergoes both changes. Glide formation reshapes the older \emph{awj} sequence, and fronting then affects the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

Glide formation creates the input to fronting; diphthong leveling follows both.

### Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

The sources establish glide formation, while the witness forms supply only a later boundary.

### SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

The *hīeġ* and *strīeġan* derivations show that \emph{awj} reshaping prepared the input to fronting. If fronting is applied first, PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. Earlier placement of glide formation changes no checked output, so these forms supply an upper boundary without a corresponding lower one.

### Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted
diphthongal outcomes of the broader West Saxon vowel history. Campbell
describes \emph{au} > \emph{ēa} [@Campbell1959, pp. 53--54, §135].

Fronting must follow glide formation and precede diphthong leveling, which applies to a wider set of derivations.

### SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Two distinct failure sets confine fronting. Placed before glide formation, it produces the wrong forms: PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. Placed after diphthong leveling, PGmc \emph{*galáubijaną}, \emph{*bráudą}, and \emph{*dráugmaz}, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. The lexical errors require fronting to follow glide formation, while the failed derivations require it to precede diphthong leveling.

The later failure set consists of failed derivations, not competing Old English
surface forms.

\newpage

## West Saxon diphthong sequence

### Historical discussion of the West Saxon diphthong sequence

Four distinct developments shape the West Saxon diphthongal field. Campbell
discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered
diphthongization, and later Anglian smoothing in connected but separate parts
of the vowel history; Hogg likewise distinguishes the palatal-diphthongal
developments [@Campbell1959, pp. 46, 53--54, 65--70, 95--96,
§§120, 135--136, 170--176, 185, 223--227; @Hogg1992, pp. 106--107, 111--112].

The closest interaction joins \emph{ww}-simplification and long-\emph{aw} diphthongization, which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. Diphthong leveling regularizes a wider field, while long-\emph{ew} diphthongization carries \emph{ēow} into the later environment of breaking.

### Historical discussion of WW simplification

West Germanic \emph{ww} sequences lie behind forms such as *dēaw* ‘dew’ and *hēawan* ‘hew’, and Campbell treats them as part of the early West Germanic diphthong history [@Campbell1959, p. 46, §120].

[SC031 OEWWSimplification](#rule-OEWWSimplification) precedes the later
long-diphthong outcomes.

### SC031. Simplification of \emph{*ww} sequences (`OEWWSimplification`) {#rule-OEWWSimplification}

```foma
define OEWWSimplification [
    {*w} {*w} -> {*w}
];
```

The *dēaw* and *hēawan* derivations establish that doubled \emph{w} was simplified before the long \emph{ēaw} development. If [SC031 OEWWSimplification](#rule-OEWWSimplification) follows [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. Earlier placement changes no checked output. The witnesses require simplification before the long-diphthong change and leave the lower boundary to the broader West Saxon chronology.

### Historical discussion of diphthong leveling

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* / *hēawan* developments.

### SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

```foma
define OEDiphthongLeveling [
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
];
```

The two edges of this interval fail differently. Before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc \emph{*galáubijaną}, \emph{*báug}, and \emph{*bráudą} produce no output (\emph{+?}) instead of expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*xáubudą} yields *hēafud* rather than expected *hēafod* ‘head’. Absence at the lower edge places diphthong leveling after fronting; the wrong surface form at the upper edge places it before medial unstressed-\emph{u} lowering.

### Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from *chew*,
*four*, and *knee* [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The only checked boundary for
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) lies ahead at
[SC044 OEBreaking](#rule-OEBreaking).

### \CAPRRuleHeading{SC033. Long \emph{ēow} before following vowels and weak endings}{OEEwLongDiphthong} {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The long \emph{ēow} of *ċēowan*, *fēower*, and *cnēow* supplies only a terminus ante quem. If [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) follows [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*kéwwaną} yields *ċeowan* rather than expected OE *ċēowan* ‘chew’, PGmc \emph{*fédwōr} yields *feower* rather than expected *fēower* ‘four’, and PGmc \emph{*knéwą} yields *cneow* rather than expected *cnēow* ‘knee’. Earlier placement changes no checked output. The sources associate \emph{ew} and \emph{iw} with the same diphthongal history but furnish no lower boundary.

### Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* and *hēawan*. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) follows [SC031 OEWWSimplification](#rule-OEWWSimplification) locally and must also precede [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening).

### SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

A local feeding relation and a later vowel change confine \emph{aw} > \emph{ēaw}. Before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc \emph{*dáwwō} yields *dawu* rather than expected OE *dēaw* ‘dew’, and PGmc \emph{*xáwwaną} yields *hawan* rather than expected *hēawan* ‘hew’. After [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*skáwōjaną} yields *sċawian* rather than expected OE *sċēawian* ‘show’, PGmc \emph{*skáwōθi} yields *sċawaþ* rather than expected *sċēawaþ*, and PGmc \emph{*stráwą} yields *stræw* rather than expected *strēaw* ‘straw’. The *dēaw* and *hēawan* forms require long-diphthong formation after simplification, while *sċēawian* requires it before brightening; the handbooks assign the same interval to the West Saxon development.

\newpage

## Prefix and compound adjustments

### Historical discussion of prefixal \emph{*a}-reduction

Weakly stressed prefixes can lose their older low vowel early in Old English,
and that is the historical setting for
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction). Campbell treats the
small class of pretonic losses directly, while Ringe and Taylor's derivation of
\emph{*galaubijana} supplies the comparative witness for the same development
[@Campbell1959, p. 147, §354; @RingeTaylor2014, p. 245;
@RingeTaylor2014, p. 267].

The rule has a narrow historical range and gives prefixed forms the weak vowel inherited by later vocalic changes.

### SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

The prefix of *ġelīefan* supplies the upper boundary for \emph{*ga-} > \emph{*ge-}. If [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) follows [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*galáubijaną} yields *ġealīefan* rather than expected OE *ġelīefan* ‘believe’. Earlier placement changes no checked output, so the witness dates prefix reduction before brightening without locating its beginning.

### Historical discussion of inter-stress raising

[SC036 OEInterStressRaising](#rule-OEInterStressRaising) has the strongest evidence of the three. Campbell's discussion of *weorold* / *weoruld* and Ringe and Taylor's derivation of \emph{*weraldu} > \emph{*weruldu} > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

The rule changes the vowel between stronger stress peaks, and its witnesses consequently constrain the relative chronology.

### \CAPRRuleHeading{SC036. Raising of medial \emph{*a} between stress peaks}{OEInterStressRaising} {#rule-OEInterStressRaising}

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

The two boundaries have unequal force. Before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*sáiwalō} yields *sāwel* rather than expected OE *sāwol* ‘soul’; after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), it yields *sāwul* rather than *sāwol*, while PGmc \emph{*wír-àldu} yields *weoruld* rather than *weorold* ‘world’. The distant lower boundary places inter-stress raising after final long-\emph{o} raising, and the local upper boundary places it before medial unstressed-\emph{u} lowering. In handbook terms, medial \emph{*a} > \emph{*u} belongs to the \emph{world}- and \emph{soul}-type low-stress vocalism that followed the earlier final-vowel changes.

### Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* ‘rainbow’. Its only checked boundary
is the immediately following technical stress-stripping stage, which is not a
sound change.

### \CAPRRuleHeading{SC037. Syncope of compound linking vowels}{OECompoundLinkingSyncope} {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc \emph{*régna-bùgô} yields *reġnefoga* rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).

\newpage

## Medial unstressed vowel changes

### Historical discussion of medial unstressed vowel changes

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* / *weoruld*
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, \emph{*weraldu}, and \emph{*jugunþi}
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.3.3].

[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) feeds the vowel
sequence subsequently reshaped by
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
Initial \emph{w} conditions the first change.

### SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

The *wuduwe* ‘widow’ derivation answers one narrow question about \emph{wi}-forms. If [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) follows [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe*; earlier placement changes no checked output. The witness requires combinative u-umlaut to precede medial lowering and supplies no lower boundary.

### \CAPRRuleHeading{SC040. Lowering of medial unstressed \emph{*u}}{OEMedUnstressedULowering} {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

The two witnesses date medial unstressed \emph{*u} > \emph{*o} at very different scales. Before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc \emph{*wíduwōn} yields *wudowe* rather than expected OE *wuduwe* ‘widow’; after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. The local *weorold* ‘world’ and *widow* evidence places lowering after combinative u-umlaut, while the youth form supplies only the distant requirement that lowering precede unstressed long-vowel shortening.

\newpage

## Final bare-\emph{a} loss

### Historical discussion

I isolate the loss of final short low vowels within the broader erosion of final syllables described by the handbooks [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

Final bare-a loss follows the medial unstressed vowel changes and
precedes restoration, which depends on the environment left by the loss.

### SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

The two sides of final bare-\emph{a} loss rest on different evidence. Applied before final \emph{z}-deletion, the change gives the wrong outputs: PGmc \emph{*bárdaz} yields *bearda* rather than expected OE *beard* ‘beard’, and PGmc \emph{*kámbaz} yields *camba* rather than expected *camb* ‘comb’. Applied after restoration, PGmc \emph{*kráftaz} yields *craft* rather than expected OE *cræft* ‘craft’, and PGmc \emph{*dágaz} yields *dag* rather than expected *dæġ* ‘day’. The distant lower limit follows final \emph{z}-loss; the local feeding relation precedes restoration, which requires the environment created by the vowel loss.

\newpage

## Surviving bimoric \emph{*ō} unrounding

### Historical discussion

The handbooks do not isolate a large independent sound change under this label.
The surviving bimoric \emph{*ō} in the pathway to *ræste* ‘rest’ nevertheless
undergoes unrounding before
[SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening). Campbell, Hogg,
and Ringe and Taylor describe the surrounding fronting and restoration history
without naming this feeder separately [@Campbell1959, pp. 52, 60,
§§131, 157--158; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158,
189--190].

The sole witness establishes a local relation to brightening but supports no broader generalization.

### \CAPRRuleHeading{SC042. Unrounding of the surviving bimoric \emph{*ō}}{PWGmcSurvivingBimoricOUnrounding} {#rule-PWGmcSurvivingBimoricOUnrounding}

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The single *ræste* ‘rest’ derivation carries the chronology of bimoric \emph{*ō} > \emph{*ā}. Before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) or after [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste*. Unrounding must therefore follow final \emph{z}-loss and precede brightening, although only the relation to brightening is local.

\newpage

## Anglo-Frisian brightening

### Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @Hogg1992, pp. 101, 119; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

### \CAPRRuleHeading{SC043. Fronting of low \emph{*a} outside nasal environments}{AngloFrisianBrightening} {#rule-AngloFrisianBrightening}

```foma
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

Two derivations place low \emph{*a} > \emph{*æ} between unrounding and breaking. Before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc \emph{*rástōz} yields *rasta* rather than expected OE *ræste* ‘rest’. After [SC044 OEBreaking](#rule-OEBreaking), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. The first witness requires brightening to receive the outcome of the surviving-bimoric \emph{*ō} development; the second requires breaking to receive the fronted vowel.

\newpage

## Breaking and velar-fricative palatalization

### Historical discussion of breaking and velar-fricative palatalization

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment, while velar-fricative palatalization follows it locally in the *feoh* and *feohtan* type derivations.

### SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Breaking must encounter the vowel created by brightening and must precede the fricative change seen in *feoh* ‘fee’ and *feohtan* ‘fight’. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*sláxaną} yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc \emph{*féxu} yields *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yields *fehtan* rather than expected *feohtan*. The two feeding relations place breaking between brightening and velar-fricative palatalization.

### \CAPRRuleHeading{SC045. Palatalization of velar fricatives beside front vowels}{OEVelarFricativePalatalization} {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*ɣ} -> {*j} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*ɣ} -> {*j} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j},
    {*ɣ} -> {*j} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The local chronology comes from *feoh* and *feohtan*. Before [SC044 OEBreaking](#rule-OEBreaking), palatalization of \emph{*x} and \emph{*ɣ} beside front vowels or \emph{*j} makes PGmc \emph{*féxu} yield *fehu* rather than expected OE *feoh*, and PGmc \emph{*féxtaną} yield *fehtan* rather than expected *feohtan*. The distant upper limit comes from *six*: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc \emph{*séxs} yields *sihs* rather than expected OE *six*. Breaking therefore feeds velar-fricative palatalization directly, while palatal umlaut supplies only the broader upper limit.

\newpage

## A-restoration and nasal changes

### Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}.

[SC046 OEARestoration](#rule-OEARestoration) has firmer handbook support than the two following nasal rules.

### \CAPRRuleHeading{SC046. Restoration of \emph{*a} before following back vowels}{OEARestoration} {#rule-OEARestoration}

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

Restoration must receive fronted \emph{*æ} and return \emph{*a} before the nasal-tail changes. Before [SC043 AngloFrisianBrightening](#rule-AngloFrisianBrightening), PGmc \emph{*bákaną} yields *bæcan* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*fáraną} yields *færan* rather than expected *faran* ‘fare’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), \emph{*bákaną} again yields *bæcan* instead of *bacan*, while PGmc \emph{*wádaną} yields *wædan* instead of *wadan* ‘wade’. These independent witness pairs place restoration after brightening and before secondary nasalization.

### Historical discussion of heavy-syllable nasal loss and secondary nasalization

Heavy-syllable nasal apocope removes the final nasalized vowel; secondary
nasalization then marks the preceding \emph{a} before final \emph{n}. The
handbooks do not isolate both developments under equally prominent labels.
Campbell describes later nasal loss and the back-mutation environment; Ringe
and Taylor provide the later relation to back mutation
[@Campbell1959, pp. 86, 166, §§205--206, 403;
@RingeTaylor2014, p. 319, §6.9.4].

The reciprocal failure set fixes the order: apocope removes the ending before
secondary nasalization acts on the remaining structure. Restoration receives
the fuller historical treatment in the handbooks.

### \CAPRRuleHeading{SC047. Heavy-syllable nasal apocope of final \emph{*ą}}{OEHeavySyllableNasalApocope} {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

The evidence for final nasalized \emph{*ą} loss is sharply asymmetric. Before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), the single PGmc witness \emph{*stráwą} yields *stræw* rather than expected OE *strēaw* ‘straw’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside a broad \emph{-en} failure set. One lower witness places apocope after long-diphthong formation; many reciprocal upper failures place it before secondary nasalization.

### \CAPRRuleHeading{SC048. Secondary nasalization before final \emph{*n}}{OESecondaryNasalization} {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

The broad \emph{-an}/\emph{-en} split fixes the lower boundary of final \emph{*a} nasalization before \emph{n}. Before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc \emph{*bákaną} yields *bacen* rather than expected OE *bacan*, and PGmc \emph{*bíndaną} yields *binden* rather than expected *bindan*. The upper boundary comes from back mutation. After [SC059 OEBackMutation](#rule-OEBackMutation), PGmc \emph{*stélaną} yields *steolan* rather than expected OE *stelan* ‘steal’, and PGmc \emph{*wébaną} yields *weofan* rather than expected *wefan* ‘weave’. Reciprocal nasal-tail failures place secondary nasalization after apocope, and the later mutation witnesses place it before back mutation; [SC046 OEARestoration](#rule-OEARestoration) retains the clearest independent historical support.

\newpage

## B allophony and Sievers-law syncope

### Historical discussion of B allophony

The first change is the positional alternation of Germanic \emph{*b}. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@Hogg1992, pp. 101--102]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

The distribution is narrow, but later changes presuppose the stop-fricative
alternation.

### \CAPRRuleHeading{SC049. Distribution of \emph{*b} after vowels and liquids}{PGmcBAllophony} {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

The handbooks describe \emph{*b}/\emph{*bb} as a positional alternation within the consonant system, and one compound supplies its chronological consequence. Before [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope), *reġnboga* ‘rainbow’ develops as *reġnfoga* rather than expected OE *reġnboga*; later placement creates no comparable failure. The witness places b-allophony after compound-linking syncope without turning the alternation into an independent sound law.

### Historical discussion of Sievers-law syncope

Sievers' Law concerns a different historical problem. It is a prosodic and
morphological adjustment in heavy stems, not a distributional allophone of a
stop consonant. Adamczyk treats the Old English reflexes of the law as
historical evidence from weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through
familiar forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15].

Sievers-law syncope is narrow in scope, but its relation to the following
palatalization is lexically secure. Its earlier limit is less sharply defined
than that of the preceding allophony rule.

### SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

The Sievers-law reduction \emph{*-CijV-*} > \emph{*-CjV-*}, including loss of \emph{*i} before \emph{*j}, must precede palatalization. If [SC050 SieversLawSyncope](#rule-SieversLawSyncope) follows [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*strákkijaną} yields *strecċan* rather than expected OE *streċċan* ‘stretch’; earlier placement creates no comparably precise error. The single cluster witness therefore places syncope before velar palatalization.

\newpage

## Palatalization of \emph{*sk} to \emph{*sc}

### Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, p. 278, §440]. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@Hogg1992, pp. 106--107, 111--112]. Ringe and Taylor make the same sequence
explicit when they distinguish the earlier palatalization of velars and \emph{*sk} from
the later diphthongization after already palatal consonants
[@RingeTaylor2014, pp. 213--216, §§6.4.1, 6.5.1].

Luick places the cluster change within a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
identity between the cluster change and the later umlautal developments.

### SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

```foma
define OESkPalatalization [
    {*s} {*k} -> {*ʃ} || .#. _
] .o. [
    {*s} {*k} -> {*ʃ} || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
] .o. [
    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
] .o. [
    {*s} {*k} -> {*ʃ} || _ {*j}
] .o. [
    {*s} {*k} -> {*ʃ} || {*j} _
];
```

The non-fronted vowels of *flasce* ‘flask’ and *wascan* ‘wash’ fix the lower boundary of \emph{*sk} > \emph{*sc}. Before [SC046 OEARestoration](#rule-OEARestoration), the forms are fronted too soon, yielding *flæsce* ‘flask’ and *wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This places [SC051 OESkPalatalization](#rule-OESkPalatalization) after restoration.

Five witnesses establish the upper boundary collectively. The palatal cluster must already underlie *sċeaft* ‘shaft’, *sċēar* ‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’ before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). The \emph{*sċea-*}/\emph{*sċie-*} set therefore places cluster palatalization before the West Saxon vowel change. The cluster change occupies the same palatalization zone as [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) while remaining distinct from plain-velar palatalization and the later vowel changes.

\newpage

## Velar palatalization before front vowels

### Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological sequence. The examples associated with that sequence, such as
*ceaster* ‘town’, *geaf* ‘gave’, *giefan* ‘give’, and *giest* ‘guest’, already
show that consonantal palatalization and later vowel effects stand close
together historically, even when they must be distinguished analytically
[@Luick1914, pp. 157--167, §§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as *cild* ‘child’, *dæg* ‘day’, *giefan* ‘give’, and *giest*
‘guest’, which show how palatalized velars, palatal influence, and later
umlautal outcomes meet in the same region of the lexicon without collapsing
into one process [@Campbell1959, pp. 69--72, 89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@Hogg1992, pp. 103--104]. This formulation
replaces a broad list of palatal outcomes with a phonological environment
defined by adjacency and syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and \emph{*sk} had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as \emph{weccan} ‘wake’, \emph{licgan} ‘lie’, \emph{lecgan} ‘lay’,
\emph{secg} ‘retainer’, \emph{ecg} ‘edge’, \emph{wicg} ‘horse’, and
\emph{brycg} ‘bridge’, illustrate the same point in lexical detail: front
vowels and `j` create the palatal environment in which plain `k` and `g` cease
to behave as plain velars [@RingeTaylor2014, pp. 213--214, §6.4.1].

Luick describes a broad early movement; Campbell distinguishes plain velars
from the `sk` complex; Hogg specifies the adjacency and syllable conditions;
and Ringe and Taylor order the plain-velar change before West-Saxon
diphthongization. Plain-velar palatalization thus forms part of a wider
palatalizing environment without being identical to its neighboring changes.

### \CAPRRuleHeading{SC052. Palatalization of \emph{*k} before front vowels and \emph{*j}}{OEVelarPalatalizationKFront} {#rule-OEVelarPalatalizationKFront}

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;
```

The *weccan* ‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’ set identifies front vowels and `j` as the environment for palatalization of `k` [@RingeTaylor2014, pp. 213--214, §6.4.1]. These forms establish the conditioning; different witnesses establish the chronology.

Applied before Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* rather than expected OE *streċċan* ‘stretch’. Applied after i-umlaut fronting, PGmc \emph{*kūi} and \emph{*lúnganjō} yield *ċȳ* ‘cows’ and *lunġen* ‘lungs’ rather than expected OE *cȳ* and *lungen*. The front-vowel `k` change therefore follows Sievers-law syncope and precedes i-umlaut fronting.

### \CAPRRuleHeading{SC052. Velar palatalization before front vowels}{OEVelarPalatalization} {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

Plain `k` and `g` palatalization in front-vocalic and `j`-adjacent environments follows `sk`-palatalization and occupies a sharply defined pre-umlaut interval. Applied before Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* rather than expected OE *streċċan* ‘stretch’. Applied after general i-umlaut, PGmc \emph{*kūi} yields *ċȳ* rather than expected *cȳ* ‘cows’, and PGmc \emph{*lúnganjō} yields *lunġen* rather than expected *lungen* ‘lungs’. These witnesses place velar palatalization after Sievers-law syncope and before umlaut.

Luick, Campbell, and Ringe and Taylor place *cild* ‘child’ and *dæg* ‘day’ in a consonantal palatalization that precedes later vowel fronting [@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1]. The umlautal developments therefore receive plain `k` and `g` already reshaped beside front vowels and `j`.

The `sk` change belongs to the same palatalizing region with a separate scope. The *streċċan* ‘stretch’ evidence establishes a specific dependency on earlier syncope; it does not merge the two changes into one process.

\newpage

## Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

### Historical discussion of early \emph{*w}-loss before umlaut

The first rule is a narrow loss of \emph{*w} after velars in the \emph{*ngw}
sequence. Ringe and Taylor derive PGmc \emph{*singwan} to Old English *singan*
‘sing’ [@RingeTaylor2014, p. 214, §6.4.2]. This comparative evidence establishes
the change, although no checked form fixes its order relative to a neighboring
rule.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The first rule is restricted to
the \emph{*ngw} sequence; the second has a specific lexical witness and defined
earlier and later limits.

### SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

The comparative development `*singwan > singan` establishes narrow post-velar \emph{*w}-loss in the \emph{*ngw} sequence, yielding *singan* ‘sing’. Moving [SC053 OEPostVelarWLoss](#rule-OEPostVelarWLoss) earlier or later leaves every checked output unchanged. Its pre-umlaut position therefore rests on comparative evidence, while the present lexicon supplies no neighboring boundary.

### SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

The history of *sǣ* ‘sea’ explains why non-initial \emph{*w} disappeared before final unstressed \emph{*i}. Campbell describes the loss, Ringe and Taylor derive the form from \emph{*saiwi-}/\emph{*sawi-}, and Luick gives the parallel trajectory [@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. Loss of the glide allowed the preceding vowel to undergo the later fronting and lengthening.

The same witness supplies two distant limits. Before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) or after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI) yields *sǣw* ‘sea’ rather than expected OE *sǣ*. The loss must therefore follow final \emph{z}-deletion and precede high-vowel apocope, while its exact position within that broad interval remains source-based.

\newpage

## The Old English i-umlaut and West Saxon palatal diphthongization

### Historical discussion of i-umlaut \CAPRHeadingBreak and West Saxon palatal diphthongization

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> [@Luick1914, pp. 166--167, §182]

Campbell gives the most compact classical formulation in English when he writes
that “the process known as i-umlaut or i-mutation operates on practically all
the sounds which it could theoretically affect in OE” [@Campbell1959, p. 69,
§190]. He immediately defines the core conditioning environment as a following
`i` or `j`, and he goes on to trace the consequences across much of the vowel
system, including forms such as *giest* ‘guest’, *giefan* ‘give’, *hierde*
‘shepherd’, and *ieldra* ‘older’ [@Campbell1959, pp. 69--72, §§190--197].

Hogg continues in the same vein: “we come now to a change which is almost as
uncontroversial as it is important” [@Hogg1992, p. 112]. His examples, such as
*bryd* ‘bride’, *trymman* ‘strengthen’, *bedd* ‘bed’, *ciest* ‘chest’, and
*wiersa* ‘worse’, likewise emphasize that the change is a broad redistribution
of vowel quality across the Old English vowel system [@Hogg1992,
pp. 112--114].

The narrower palatal-diphthongal material is described differently. Ringe and
Taylor treat West-Saxon diphthongization after initial palatals as a distinct
process [@RingeTaylor2014, p. 215, §6.5.1], and Fulk is even more explicit about
its chronological delicacy when he calls it “diphthongization by initial
palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13]. Ringe and Taylor’s examples such as *gieldan* ‘pay’,
*scield* ‘shield’, and *scieppan* ‘create’ show that this narrower process is
triggered by already palatal consonants and leads to specifically West-Saxon
diphthongal outputs [@RingeTaylor2014, pp. 215--216, §6.5.1].

Luick, Campbell, and Hogg treat i-umlaut as a system-wide change. Ringe and
Taylor and Fulk distinguish from it a narrower West-Saxon process affecting
words after initial palatals. The two changes act in different environments and
produce different lexical consequences.

### SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

```foma
define OEIUmlautFronting [
    {*a} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ā} -> {*ǣ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*e} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*o} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ō} -> {*ē} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*u} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ū} -> {*ȳ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*á} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*é} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ó} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ú} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

The breadth of i-umlaut appears in lexical classes that share only a following high front vocoid. The forms *fylgan* ‘follow’, *gylden* ‘golden’, *wyrm* ‘worm’, and *giest* ‘guest’ exemplify the same `i`- or `j`-conditioned fronting across different vowels [@RingeTaylor2014, p. 222, §6.6.1; @Campbell1959, pp. 69--72, §§190--191].

The cow and lung forms establish the lower boundary. If fronting precedes velar palatalization, PGmc \emph{*kūi} yields *ċȳ* ‘cows’ rather than expected OE *cȳ*, and \emph{*lúnganjō} yields *lunġen* ‘lungs’ rather than expected OE *lungen*. The consonantal change must therefore precede fronting.

The gift and sheath forms establish the upper boundary. If West Saxon palatal diphthongization precedes fronting, PGmc \emph{*géftiz} yields *ġieft* ‘gift’ rather than expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’ rather than expected *sċēaþ*. Fronting consequently follows velar palatalization and precedes the West Saxon change; the other components of i-umlaut share those bounds.

### SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Raising of umlauted `æ` to `e` continues the same assimilatory event as fronting and therefore shares the chronology of general i-umlaut.

The same four forms fix both boundaries. If raising precedes velar palatalization, \emph{*kūi} yields *ċȳ* instead of expected *cȳ* and \emph{*lúnganjō} yields *lunġen* instead of expected *lungen*. If West Saxon palatal diphthongization precedes raising, \emph{*géftiz} yields *ġieft* rather than expected *ġift*, and \emph{*skáiθiz} yields *sċǣþ* rather than expected *sċēaþ*. These forms place raising after velar palatalization and before West Saxon palatal diphthongization.

The sources do not describe umlaut as simple fronting alone. Campbell notes that
the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@Hogg1992, p. 112].

### SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

```foma
define OEIUmlautDiphthong [
    {*ea} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēa} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*io} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*īo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*eo} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éa} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éo} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ío} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Diphthongal outcomes belong to the same system-wide assimilation as simple-vowel fronting and raising. All three therefore belong to a single historical event.

The relevant examples are the recurring West-Saxon `ie` forms cited in the
handbooks, including *giest* ‘guest’, *giefan* ‘give’, and *hierde*
‘shepherd’ in Campbell and *ciest* ‘chest’ in Hogg
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @Hogg1992,
pp. 112--114]. These diphthongal outcomes form a distinct part of the general
umlautal development alongside simple fronting.

The chronology comes from the cow/lung and gift/sheath contrasts. Placed before velar palatalization, diphthongal mutation over-palatalizes \emph{*kūi} and \emph{*lúnganjō}; placed after West Saxon palatal diphthongization, it yields *ġieft* and *sċǣþ* instead of expected *ġift* and *sċēaþ*. These failures place diphthongal mutation after velar palatalization and before West Saxon palatal diphthongization.

### SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The lower boundary is consonantal. If general umlaut precedes velar palatalization, PGmc \emph{*kūi} yields *ċȳ* ‘cows’ rather than expected *cȳ*, and PGmc \emph{*lúnganjō} yields *lunġen* ‘lungs’ rather than expected *lungen*. These over-palatalized forms place general umlaut after velar palatalization.

The upper boundary separates general umlaut from the narrower West Saxon process. If West Saxon palatal diphthongization precedes umlaut, PGmc \emph{*géftiz} yields *ġieft* ‘gift’ rather than expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’ rather than expected *sċēaþ*. Together the two witness pairs place general umlaut after velar palatalization and before the West Saxon process.

### \CAPRRuleHeading{SC056. West Saxon palatal diphthongization}{OEWsPalatalDiphthongization} {#rule-OEWsPalatalDiphthongization}

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

West Saxon *gieldan* ‘pay’, *scield* ‘shield’, and *scieppan* ‘create’ show diphthongization after an already palatal consonant [@RingeTaylor2014, pp. 215--216, §6.5.1]. Their dialectal and phonological restriction separates this development from system-wide i-umlaut.

Hogg's *giefan* ‘give’ and *sceap* ‘sheep’ belong to the same palatal-consonant environment [@Hogg1992, pp. 108--109]. Fulk likewise assigns this diphthongization a place before front mutation and distinguishes the two processes [@Fulk2018, p. 74, §4.13].

The forms *ġift* ‘gift’ and *sċēaþ* ‘sheath’ fix the lower boundary. If West Saxon palatal diphthongization precedes general i-umlaut, PGmc \emph{*géftiz} yields *ġieft* ‘gift’ rather than expected *ġift*, and PGmc \emph{*skáiθiz} yields *sċǣþ* ‘sheath’ rather than expected *sċēaþ*. These witnesses place West Saxon palatal diphthongization after general umlaut; no tested lexical item supplies a later terminus ante quem.

The one-sided chronology reflects the difference in scale. General umlaut reorganizes the vowel system, whereas West Saxon palatal diphthongization affects a narrower dialectal class after palatal consonants. Its exact later placement remains undemonstrated by the present lexicon.

\newpage

## J-cluster coalescence

### Historical discussion

Only a small lexical group reveals the coalescence of velars with \emph{*j}.
Plain-velar and \emph{*sk} palatalization must already have run before
\emph{*gj} and \emph{*kj} acquire their later outcomes.
Campbell, Ringe and Taylor, and Fulk discuss the palatalized and fronted
outcomes in *bīeġan* ‘bend’ and *sēċan* ‘seek’ without assigning this later
cluster adjustment the status of a major sound law [@Campbell1959, pp. 89,
107--108, §§170, 248--251; @RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1,
6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13].

### SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

The forms *bīeġan* ‘bend’ and *sēċan* ‘seek’ determine the earlier boundary.
If coalescence precedes [SC052
OEVelarPalatalization](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related
forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc `*báugijaną` yields *bēaġan* ‘bend’ rather than expected OE *bīeġan*,
and PGmc `*sōkijaną` yields *sōċan* ‘seek’ rather than expected *sēċan*. This
demonstrates that velar palatalization preceded coalescence. Nothing in the
present lexicon supplies a terminus ante quem.

\newpage

## Nasal dissimilation

### Historical discussion

Most accounts introduce nasal dissimilation to explain individual forms rather
than as a regular sound law. Luick records *enetre* ‘yearling’ (spelled
*enitre* in his text) [@Luick1914, p. 166]; Campbell discusses *heofon*
‘heaven’ with suffixal variation [@Campbell1959, p. 155]; and Hogg encounters
the same form while treating back mutation [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The disagreement concerns scope. Fulk's formulation recognizes a recurrent but
irregular development in `mn`; the remaining discussions stay with particular
lexical outcomes. None warrants a sound law comparable in scope to the major
Old English vowel changes.

### \CAPRRuleHeading{SC058. Nasal dissimilation in short-vowel environments}{OENasalDissimilation} {#rule-OENasalDissimilation}

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

I adopt a narrower environment than the handbook observations might suggest.
Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “*heofon* is for
older *hefzen*” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind [@Campbell1959, p. 155;
@Hogg1992, p. 112]. The short-vowel environment adopted here covers a recurrent
subset of these outcomes, not every dissimilatory development involving nasals.

No witness word fixes the position of nasal dissimilation within the Old
English sequence. Reversing its order with any tested neighbor leaves every
checked output unchanged. A more precise relative chronology would therefore
require lexical evidence not represented here.

\newpage

## Back mutation

### Historical discussion

West Saxon *giefan* ‘give’ and *wefan* ‘weave’ stand against non-West-Saxon
*geofad* and *weofan*. Ringe and Taylor use this contrast to define the
dialectal profile of back mutation [@RingeTaylor2014, p. 319, §6.9.4].
Campbell's treatment of diphthongization before following back vowels includes
*heofon* ‘heaven’ [@Campbell1959, p. 86, §207], while Hogg draws the instructive
comparison with breaking [@Hogg1992, p. 112]. Fulk accordingly separates back
mutation from the earlier umlautal changes [@Fulk2018, p. 69, §4.8].

### SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
```

Three witness forms bracket the chronology. If back mutation precedes
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), forms such as
\emph{*gébaną} produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. \emph{*stélaną} likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. At the other edge, delaying
back mutation until after
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) makes
\emph{*wébaną} yield *weofan* ‘weave’; the expected form is *wefan* ‘weave’.
Thus back mutation follows secondary nasalization but precedes the weak-tail
reductions.

\newpage

## West Saxon palatal umlaut

### Historical discussion

The reflexes *miht* ‘might’ and *niht* ‘night’ place West Saxon palatal umlaut
after the principal umlautal developments. Campbell and Ringe and Taylor
describe the forms themselves; Fulk supplies the broader chronology of
palatal-vowel change [@Campbell1959, pp. 107--108, §§248--251;
@RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75,
§§4.7, 4.13].

### \CAPRRuleHeading{SC060. West Saxon palatal umlaut before \emph{*h}-clusters}{OEWsPalatalUmlaut} {#rule-OEWsPalatalUmlaut}

```foma
define OEWsPalatalUmlaut [
    {*eo} -> {*i} || _ OEHCluster .#.,
    {*io} -> {*i} || _ OEHCluster .#.,
    {*ie} -> {*i} || _ OEHCluster .#.,
    {*eo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*io} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ie} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*éo} -> {*i} || _ OEHCluster .#.,
    {*ío} -> {*i} || _ OEHCluster .#.,
    {*íe} -> {*i} || _ OEHCluster .#.,
    {*éo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ío} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*íe} -> {*i} || _ OEHCluster EnglishStarFrontVowel
];
```

The change to \emph{*i} before \emph{*h}-clusters can be ordered only on its
earlier side. If palatal umlaut precedes
[SC055 OEIUmlaut](#rule-OEIUmlaut),
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage *mieht* and *nieht* rather than expected OE *miht* and *niht*.
Consequently, i-umlaut precedes palatal umlaut. Reordering the latter against
any tested later change leaves both witness forms unchanged.

\newpage

## Weak-tail nasal loss

### Historical discussion

The pathway from \emph{*dōną} to *dōn* ‘do’ supplies the sole lexical thread
through this reduction. Campbell, Hogg, and Fulk place such weak-tail losses
among apocope and related late reductions [@Campbell1959, pp. 144--145,
§§345--349; @Hogg1992, pp. 120--121; @Fulk2018, p. 91, §5.6]. The witness,
however, ties the change to a much older development. Its immediate neighbors
remain untested.

### \CAPRRuleHeading{SC061. Reduction of final nasal weak-tail endings}{OEWeakTailNasalLoss} {#rule-OEWeakTailNasalLoss}

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

Final weak-tail \emph{*-ną} and \emph{*-mą} accordingly yield plain
\emph{*-n} and \emph{*-m}.

Only *dōn* ‘do’ constrains the relative order. Placing this loss before
the older n-stem loss makes the derivation record no output instead of expected
OE *dōn* ‘do’. The older loss must therefore precede weak-tail nasal loss.
Nothing in the current lexicon distinguishes among its possible later
positions, and one witness cannot establish a wider historical development.

\newpage

## High-vowel apocope

### Historical discussion

Final high vowels must survive long enough to condition umlaut before apocope
removes them after heavy syllables and in the relevant trisyllabic patterns.
Campbell, Hogg, Ringe and Taylor, and Fulk agree on this Old English
development, though they differ over the extent of the surrounding syncope
[@Campbell1959, pp. 144--145, §§345--349; @Hogg1992, p. 120;
@RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

### \CAPRRuleHeading{SC063. High-vowel apocope after heavy syllables and in trisyllables}{OEHighVowelApocope} {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

Final \emph{*i}, \emph{*u}, and \emph{*ų} cannot disappear before completing
their umlautal work. Applied before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*kūi} yields *cū* rather than
expected OE *cȳ* ‘cow’, and PGmc \emph{*brūdiz} yields *brūd* rather than
expected OE *brȳd* ‘bride’. Conversely, if apocope waits until after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
PGmc \emph{*fúrxtīnaz} yields *fyrht* rather than expected OE *fyrhte*
‘fright’. The three witnesses establish the sequence i-umlaut, high-vowel
apocope, unstressed long-vowel shortening.

\newpage

## Post-apocope \emph{*n}-loss and medial syncope

### Historical discussion of post-apocope \emph{*n}-loss and medial syncope

Evidence for post-apocope reduction is strikingly uneven. The inherited
\emph{*furht-} family makes the survival of one nasal diagnostic and fixes both
sides of stem-final n-loss [@Kroonen2013, p. 201]. No comparable witness orders
the medial syncope that follows. Hogg, Ringe and Taylor, and Fulk describe both
processes within the late history of weak syllables
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

### SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

```foma
define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];
```

Only final \emph{*n} after long \emph{*ī} is at issue, as in the inherited
family behind *fyrhte* ‘fright’.

The same proto-form fixes both edges. Before
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc
\emph{*fúrxtīnaz} yields *fyrhten* rather than expected OE *fyrhte* ‘fright’.
After [SC072
OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc
\emph{*fúrxtīnaz} again yields *fyrhten* rather than expected *fyrhte*. I
therefore order final bare-a loss, stem-final n-loss, and unstressed long-vowel
shortening in that sequence. Both boundaries are firm within the derivation,
but depend upon one lexical family.

### \CAPRRuleHeading{SC065. Medial syncope before dentals after heavy syllables}{OEMedialSyncope} {#rule-OEMedialSyncope}

Loss of medial \emph{*i} before dentals belongs to the late weak-tail history
described by Hogg, Ringe and Taylor, and Fulk
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

```foma
define OEMedialSyncope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
];
```

No diagnostic word establishes a local chronology. Moving medial syncope to
either end of the tested range leaves every checked output unchanged. Its
handbook placement after apocope and before later cluster simplification
therefore remains preferable, but the present lexicon cannot demonstrate it.

\newpage

## Late syncope and degemination

### Historical discussion of late syncope and degemination

Vowel loss creates the clusters upon which later assimilation and degemination
operate. Hogg and Ringe and Taylor describe this dependence, while Brunner's
*netle* ‘nettle’ beside later *netele* supplies a concrete lexical type
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2;
@SieversBrunner1965, pp. 144--145, §§158--159]. Fulk places this syncope after
i-umlaut [@Fulk2018, p. 91, §5.6].

The three relations are not equally secure. Lexical evidence orders syncope
and degemination; the intervening dental assimilation has no independent
ordering witness.

### \CAPRRuleHeading{SC066. L-adjacent syncope in medial syllables}{OELAdjacentSyncope} {#rule-OELAdjacentSyncope}

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

The loss of medial \emph{*i} before \emph{*l} is late enough to preserve
earlier umlaut, as *netle* ‘nettle’ and *spinl* ‘spindle’ demonstrate.

Placed before i-umlaut, PGmc \emph{*nátilōn} yields *nætle* rather than
expected OE *netle* ‘nettle’, and PGmc \emph{*spénnilō} yields *spenl* rather
than expected *spinl* ‘spindle’. Placed after preconsonantal degemination, PGmc
\emph{*spénnilō} yields *spinnl* rather than expected *spinl*. The witnesses
therefore establish the sequence i-umlaut, l-adjacent syncope, preconsonantal
degemination. The first relation separates two historical phases; the second is
a direct feeding relation, since syncope creates the cluster that degemination
simplifies.

### \CAPRRuleHeading{SC067. Dental assimilation in newly formed clusters}{OEDentalAssimilation} {#rule-OEDentalAssimilation}

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

Loss of \emph{*θ} after \emph{*t} resolves a dental cluster produced by syncope
[@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].
No witness distinguishes its position: moving dental assimilation across every
tested neighbor leaves the outputs unchanged. I nevertheless place it after
syncope, which supplies its input, and before the more general cluster
simplification described in the handbooks. This order is phonologically
motivated, not established by a lexical contrast.

### \CAPRRuleHeading{SC068. Preconsonantal degemination before sonorants}{OEPreconsonantalDegemination} {#rule-OEPreconsonantalDegemination}

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

Preconsonantal \emph{*tt} and \emph{*nn} simplify only after syncope has
created a following sonorant cluster, as in *spinl* ‘spindle’
[@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Placed before l-adjacent syncope, PGmc \emph{*spénnilō} yields *spinnl* rather
than expected OE *spinl* ‘spindle’. Syncope must therefore create the cluster
before degemination simplifies it. Reordering degemination against any tested
later change leaves the witness unchanged, so no terminus ante quem is known.

\newpage

## Early o-shortening

### Historical discussion

After the principal palatal and umlautal changes, unstressed vowels undergo
shortening, fronting, merger, and sometimes complete loss. Campbell describes
the early shortening of unaccented long vowels, while Hogg, Ringe and Taylor,
and Fulk relate it to apocope, syncope, and the later reductions
[@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening has only a distant earlier boundary. The rules that follow,
especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
have more closely defined relations.

### \CAPRRuleHeading{SC069. Early shortening of unstressed \emph{*ō} before nasals}{OEEarlyOShortening} {#rule-OEEarlyOShortening}

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

The rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Moving the rule before
[SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss), PGmc \emph{*nḗdrōn} yields
*nǣdran* rather than expected OE *nǣdre* ‘adder’, PGmc \emph{*érθōn} yields
*eorþan* rather than expected *eorþe* ‘earth’, and PGmc \emph{*fláskōn} yields
*flascan* rather than expected *flasce* ‘flask’. The same earlier shift also
disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of
failures requires [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening) to follow
[SC023 NWGmcNStemNLoss](#rule-NWGmcNStemNLoss).

If the rule is moved later within the tested sequence, no checked form yields a
form different from the expected one. The checked forms therefore do not
identify a corresponding later constraint. The sources place early
\emph{*ō}-shortening before the later weak-tail changes without fixing a closer
local order.

\newpage

## Early unstressed fronting and later o-shortening

### Historical discussion of early unstressed fronting and later o-shortening

Campbell distinguishes the shortening of unaccented long vowels, while Hogg,
Ringe and Taylor, and Fulk place fronting and shortening within a later history
of syncope and final-vowel adjustment [@Campbell1959, p. 148, §355;
@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7]. Earlier unstressed fronting precedes later
o-shortening.

[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) has both an
earlier and a later lexical breakpoint.
[SC071 OELateOShortening](#rule-OELateOShortening) confirms their reciprocal
order, but no checked form fixes its later boundary.

### \CAPRRuleHeading{SC070. Early fronting of unstressed \emph{*a}}{OEUnstressedFrontingEarly} {#rule-OEUnstressedFrontingEarly}

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

The rule fronts unstressed \emph{*a} to \emph{*æ} after the earlier shortening
has created a frontable vowel but before the later shortening of unstressed
\emph{*ō}. It produces endings such as OE \emph{-en} in *lungen* ‘lungs’.

If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc \emph{*lúnganjō} yields *lunġen* rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc \emph{*búrōθi} yields *boreþ* rather than expected OE *boraþ* ‘bears’, and PGmc \emph{*mḗnōθz} yields *mōneþ* rather than expected *mōnaþ* ‘month’. The witness forms require [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) to follow [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and precede [SC071 OELateOShortening](#rule-OELateOShortening).

The relation to [SC071 OELateOShortening](#rule-OELateOShortening) is local.
The earlier boundary at
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) places fronting after
the older palatal developments.

### SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting,
producing the later “stable a” endings in OE *boraþ* ‘bears’ and *liornaþ*
‘learns’.

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc \emph{*búrōθi} yield *boreþ* rather than expected OE *boraþ*, and PGmc \emph{*líznōθi} yield *liorneþ* rather than expected *liornaþ*. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly). Moving it later within the tested range creates no equally sharp failure.

\newpage

## Unstressed long-vowel shortening and ae-merger

### Historical discussion of unstressed long-vowel shortening and ae-merger

Campbell describes the shortening of unaccented long vowels, and Ringe and
Taylor place it among the last prehistoric Old English changes before the
merger of unstressed \emph{*æ} with \emph{*e}
[@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) have a reciprocal
ordering relation. [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) supplies
the earlier boundary of shortening, and [SC085 OEHLoss](#rule-OEHLoss) the
later boundary of the merger.

### \CAPRRuleHeading{SC072. Shortening of unstressed long vowels}{OEUnstressedLongVowelShortening} {#rule-OEUnstressedLongVowelShortening}

```foma
define OEUnstressedLongVowelShortening OEUnstressedLongVowelShortening1
    .o. OEUnstressedLongVowelShortening2
    .o. OEUnstressedLongVowelShortening3
    .o. OEUnstressedLongVowelShortening5
    .o. OEUnstressedLongVowelShortening6
    .o. OEUnstressedLongVowelShortening7
    .o. OEUnstressedLongVowelShortening8;
```

The rule shortens the remaining unstressed long vowels before weak final
syllables reach their later forms. A small group of lexical witnesses fixes its
chronology.

If the rule is moved before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), PGmc \emph{*fúrxtīnaz} yields *fyrhten* rather than expected OE *fyrhte* ‘fright’. If the rule is delayed until after [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre* ‘adder’, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder* ‘father’. These outputs require [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) to follow [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) and precede [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

Shortening therefore follows the earlier weak-tail preparation and immediately
precedes the merger.

### SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger OEWeakTailReduction3;
```

The rule merges unstressed \emph{*æ} with \emph{*e} after shortening has
produced the weak final vowels, yielding the ordinary OE \emph{-e} spellings.

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*nḗdrōn} yields *nǣdræ* rather than expected OE *nǣdre*, and PGmc \emph{*fádēr} yields *fædær* rather than expected *fæder*. If the rule is delayed until after [SC085 OEHLoss](#rule-OEHLoss), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. These failures show that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss).

The checked forms fix the local order after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and place the merger before the later h-loss and contraction.

\newpage

## Medial unstressed-i lowering

### Historical discussion of medial unstressed-i lowering and \emph{*ng} retention

Hogg and Ringe and Taylor treat the late weakening and merger of unstressed
vowels as a continuing history [@Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6].
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) lowers
medial unstressed \emph{i}; [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering)
preserves \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’
type.

General lowering precedes the restricted restoration before \emph{*ng}. The
evidence is narrower than that for
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

### \CAPRRuleHeading{SC074. First medial unstressed-\emph{i} lowering}{OEMedUnstressedILowering1} {#rule-OEMedUnstressedILowering1}

```foma
define OEMedUnstressedILowering1 [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

The rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding
vocalic syllable. The resulting \emph{e}-outcome is reversed before
\emph{*ng}.

If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc \emph{*fúrxtīnaz} yields *fyrhti* rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc \emph{*skíllingaz} yields *sċilleng* rather than expected *sċilling* ‘shilling’. The derivations require [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) to follow [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and precede [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side. The rule follows unstressed long-vowel
shortening and precedes the more specific \emph{*ng} preservation.

### \CAPRRuleHeading{SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng}}{OEMedUnstressedILowering} {#rule-OEMedUnstressedILowering}

The following rule reverses the lowering before \emph{*ng}.

```foma
define OEMedUnstressedILowering [
    {*e} -> {*i} || _ {*n} {*g}
];
```

The rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Moving the rule before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) makes PGmc \emph{*skíllingaz} yield *sċilleng* rather than expected OE *sċilling*. On this evidence, I take [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) to follow [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1). Moving it later within the tested range creates no equally sharp failure.

\newpage

## Prefix i-reduction

### Historical discussion

Late weak-tail reduction affects unstressed prefixes as well as inflectional
endings and medial vowels. Fulk's discussion of prefix vowels accounts for OE
\emph{*be-} and \emph{*ne-} [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and
Taylor place such weakening within the broader late history of unstressed
vowels [@Hogg1992, pp. 120--121; @RingeTaylor2014, pp. 298--332,
§§6.8.3--6.9.6].

The tested forms do not determine the rule's position relative to a neighboring
change.

### \CAPRRuleHeading{SC076. Reduction of prefixal \emph{*i} in unstressed position}{OEPrefixIReduction} {#rule-OEPrefixIReduction}

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

The rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the
\emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following
vowel. The development accounts for later prefix spellings such as OE
\emph{*be-} and \emph{*ne-}.

If the rule is moved earlier or later within the tested sequence, no checked form yields a form different from the expected one. The tested forms therefore do not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

The handbooks attest late prefix-vowel weakening, but the precise placement
remains approximate. No lexical failure fixes it.

\newpage

## Weak-tail reduction

### Historical discussion

Campbell, Hogg, Ringe and Taylor, and Fulk describe a late history in which
apocope, shortening, contraction, and further weak-tail reductions reshape
final syllables [@Campbell1959, p. 148, §355; @Hogg1992, pp. 120--121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--91, §5.6]. Lexical failures place the remaining weak-tail
reduction after unstressed fronting and before contraction.

### \CAPRRuleHeading{SC078. Reduction of remaining weak-tail vowels}{OEWeakTailReduction} {#rule-OEWeakTailReduction}

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

The rule reduces the remaining weak-tail vowels, preventing a broad class of
\emph{-en} and extra-vowel outcomes.

I place the change after [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and before [SC086 OEContraction](#rule-OEContraction). Moving it before
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc
\emph{*bákaną} yields *bacen* rather than expected OE *bacan* ‘bake’, and PGmc
\emph{*bíndaną} yields *binden* rather than expected *bindan* ‘bind’, alongside
a much wider set of comparable \emph{-en} failures. If the rule is delayed until
after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields
*flēoan* rather than expected OE *flēon* ‘flee’, and PGmc \emph{*sláxaną}
yields *sleaan* rather than expected *slēan* ‘slay’.

The earlier boundary spans a wide interval and does not establish a close
neighboring relation. The later boundary is narrower:
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) precedes
[SC086 OEContraction](#rule-OEContraction).

\newpage

## Final-j loss and final geminate simplification

### Historical discussion of final-j loss and final geminate simplification

After [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} in
heavy environments, forms such as *lungen* ‘lungs’ acquire a final geminate.
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification)
then removes the second nasal.

[SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) has a broad earlier boundary
at [SC055 OEIUmlaut](#rule-OEIUmlaut).
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is
fixed only by the final \emph{nn} outcome in the following derivation.

### SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

The rule removes \emph{*j} after the relevant heavy-syllable configurations,
after the earlier umlaut-sensitive vocalism has developed.
The affected glide is \emph{*j}.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*galáubijaną} yields *ġelēafan* rather than expected OE *ġelīefan* ‘believe’, PGmc \emph{*báugijaną} yields *bēaġan* rather than expected *bīeġan* ‘bow’, and PGmc \emph{*fúlgijaną} yields *fulġan* rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc \emph{*lúnganjō} yields *lungenn* rather than expected OE *lungen* ‘lungs’. I accordingly take [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The earlier boundary is broad, but the relation to final geminate
simplification is local.

### \CAPRRuleHeading{SC080. Simplification of final geminates}{OEFinalGeminateSimplification} {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

The rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Moving the rule before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) makes PGmc \emph{*lúnganjō} yield *lungenn* rather than expected OE *lungen*. These failures require [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) to follow [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

## J-strengthening, vocalization, and ei-contraction

### Historical discussion of j-strengthening, vocalization, and ei-contraction

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
vocalizes the remaining intervocalic \emph{*j}, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) removes the
resulting \emph{ei}-like sequence in weak verbal endings.

The output of each rule conditions the next.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) has local
lexical evidence on both sides;
[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
has a distant earlier boundary, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) has no
tested later boundary.

### \CAPRRuleHeading{SC081. Strengthening of \emph{*j} after front diphthongs}{OEJStrengtheningAfterFrontDiphthong} {#rule-OEJStrengtheningAfterFrontDiphthong}

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

After the relevant front diphthongs, \emph{*j} first strengthened to a consonantal outcome; otherwise it would have vocalized too early.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc \emph{*stráwjaną} yields *strēaġan* rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields *strīeian* rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

### \CAPRRuleHeading{SC082. Intervocalic vocalization of \emph{*j}}{OEIntervocalicJVocalization} {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule vocalizes intervocalic \emph{*j} to \emph{*i}, creating the
\emph{ei}-like sequence later removed by
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak
verb forms.

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc \emph{*stráwjaną} yield *strīeian* rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc \emph{*búrōjaną} yield *boreian* rather than expected OE *borian* ‘bore’, PGmc \emph{*xándlōjaną} yield *handleian* rather than expected *handlian* ‘handle’, and PGmc \emph{*mákōjaną} yield *maceian* rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.

### SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc \emph{*búrōjaną} yield *boreian* rather than expected OE *borian*, PGmc \emph{*líznōjaną} yield *liorneian* rather than expected *liornian*, and PGmc \emph{*líkkōjaną} yield *licceian* rather than expected *liccian*. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

## H-loss and contraction

### Historical discussion of h-loss and contraction

When [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, it creates
hiatus. [SC086 OEContraction](#rule-OEContraction) immediately resolves the
resulting vowel sequence.

Ringe and Taylor describe this late sequence of \emph{h}-loss and contraction
[@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk places the contracted
verbs in a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick
describes the corresponding West Germanic contractions [@Luick1914, p. 165].

### SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc \emph{*táixōn} yields *tāæ* rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc \emph{*fléuxaną} yields *flēoan* rather than expected OE *flēon* ‘flee’, PGmc \emph{*sláxaną} yields *sleaan* rather than expected *slēan* ‘slay’, PGmc \emph{*téxun} yields *teoon* rather than expected *tēon* ‘draw’, and PGmc \emph{*táixōn} yields *tāe* rather than expected *tā*. These outputs require [SC085 OEHLoss](#rule-OEHLoss) to follow [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) and precede [SC086 OEContraction](#rule-OEContraction).

The earlier boundary rests on one witness; the four later witnesses establish
the immediate relation to contraction.

### SC086. Contraction of the resulting hiatus (`OEContraction`) {#rule-OEContraction}

The following rule contracts the hiatus left by [SC085 OEHLoss](#rule-OEHLoss).

```foma
define OEContraction [
    {*a} {*a} -> {*ā},
    {*e} {*e} -> {*ē},
    {*i} {*i} -> {*ī},
    {*o} {*o} -> {*ō},
    {*u} {*u} -> {*ū},
    {*ea} {*a} -> {*ēa},
    {*ēa} {*a} -> {*ēa},
    {*eo} {*a} -> {*ēo},
    {*ēo} {*a} -> {*ēo},
    {*eo} {*o} -> {*ēo},
    {*ēo} {*o} -> {*ēo},
    {*éo} {*o} -> {*ḗo},
    {*ḗo} {*o} -> {*ḗo},
    {*ā} {*a} -> {*ā},
    {*ā} {*e} -> {*ā},
    {*ē} {*a} -> {*ē},
    {*ē} {*e} -> {*ē},
    {*ḗ} {*a} -> {*ḗ},
    {*ḗ} {*e} -> {*ḗ},
    {*ī} {*a} -> {*ī},
    {*ī} {*e} -> {*ī},
    {*ḯ} {*a} -> {*ḯ},
    {*ḯ} {*e} -> {*ḯ},
    {*ō} {*a} -> {*ō},
    {*ō} {*e} -> {*ō},
    {*ū} {*a} -> {*ū},
    {*ū} {*e} -> {*ū}
];
```

The rule contracts the vowel sequences created after \emph{h}-loss, producing
*flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Moving contraction before [SC085 OEHLoss](#rule-OEHLoss) makes PGmc \emph{*fléuxaną} yield *flēoan* rather than expected OE *flēon*, PGmc \emph{*sláxaną} yield *sleaan* rather than expected *slēan*, PGmc \emph{*téxun} yield *teoon* rather than expected *tēon*, and PGmc \emph{*táixōn} yield *tāe* rather than expected *tā*. The derivations require [SC086 OEContraction](#rule-OEContraction) to follow [SC085 OEHLoss](#rule-OEHLoss). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
The more distant [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
relation establishes only that weak-tail reduction precedes contraction.

\newpage

## R-metathesis

### Historical discussion

Sievers-Brunner describes r-metathesis in forms such as *berstan* ‘burst’,
*forst* ‘frost’, and *cærse* ‘cress’
[@SieversBrunner1965, p. 159, §179]. Luick likewise treats it as a later
rearrangement whose interaction with breaking remains variable
[@Luick1914, p. 201].

The evidence establishes that breaking precedes metathesis. It does not
establish an ordering relation between
[SC086 OEContraction](#rule-OEContraction) and
[SC087 OERMetathesis](#rule-OERMetathesis).

### \CAPRRuleHeading{SC087. Metathesis of \emph{*r} with a following short vowel}{OERMetathesis} {#rule-OERMetathesis}

```foma
define OERMetathesis [
    {*r} {*e} -> {*e} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*u} -> {*u} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*i} -> {*i} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*o} -> {*o} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*a} -> {*a} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*é} -> {*é} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*ó} -> {*ó} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*á} -> {*á} {*r} || EnglishStarConsonant _ {*s} {*t}
];
```

The rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Moving the rule before [SC044 OEBreaking](#rule-OEBreaking) makes PGmc \emph{*bréstaną} yield *beorstan* rather than expected OE *berstan* ‘burst’. On this evidence, I take [SC087 OERMetathesis](#rule-OERMetathesis) to follow [SC044 OEBreaking](#rule-OEBreaking). Moving it later within the tested sequence alters none of the checked outputs.

The checked forms fix the earlier relation but do not identify a corresponding
later constraint. The sources treat r-metathesis as a late rearrangement after
breaking without placing it immediately beside contraction.

\newpage

\part{Lexical derivations}

# Word-by-word derivations

## Introduction

The catalogue groups words by the kind of historical explanation they require.
Regular derivations establish the reach of the sound laws. The remaining
classes mark, without concealment, the places where attestation, morphology,
analogy, or an unresolved mismatch intervenes.

The catalogue proceeds from words; the preceding part proceeds from rules.
Together they allow each proposed sound law to be tested against its lexical
witnesses and each etymology against the complete ordered history.

## Data and sources

This volume assembles the lexical corpus from the aligned Germanic dataset and the compact derivation traces that accompany each entry. Comparative dictionaries, Old English dictionaries, and historical grammars are cited in the prose where they bear on particular lexical arguments.

The result is a lexical catalogue rather than a separate report on citation method or trace machinery.

## Transducer and derivation method

Four objects must be distinguished in every derivation: the citation reconstruction, the selected input, the transducer outcome, and the Old English target. The summary identifies them where they differ; the boxed trace then divides the changes into Earlier Germanic and Old English stages.

## Derivation classes

The lexical catalogue is ordered by seven derivation classes in the current manifest. Counts in this alpha are:

- Regular derivations: **70**
- Attested variants: **4**
- Early analogy: **35**
- Late analogy: **28**
- Reconstructed Old English comparators: **3**
- Known but unmodelled remodellings: **2**
- Unexplained or deliberately unmodelled exceptions: **5**

\clearpage

## Regular derivations

In these entries the selected Germanic input yields the Old English reflex by
regular sound change. They establish the standard against which the following
analogical and exceptional histories must be judged.

### adder — OE _nǣdre_

\index[oe]{naedre@\emph{nǣdre}}
\index[pgmc]{nedron@*nḗdrōn}

Derivation: _\*nḗdrōn_ > _nǣdre_ (regular).

#### Derivation trace

Proto input: _\*nḗdrōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*nḗdrǭ} \\
\mbox{NWGmc Long E Lowering} & \emph{*nǣdrǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*nǣdræ} \\
OE Unstressed AE Merger & \emph{*nǣdre} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nǣdre_

#### Reconstruction and comparative evidence

Kroonen distinguishes the masculine snake word [_\*nadra-_]{.iv lang=pgmc sort=nadra role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:98"} from a feminine
ablauting formation [_\*nēdrōn-_]{.iv lang=pgmc sort=nedron role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:99"}, and gives Old English [_nǣdre_]{.iv lang=oe sort=naedre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:99"}, [_næddre_]{.iv lang=oe sort=naeddre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:99"} under the
latter [@Kroonen2013, 426]. Orel likewise points from the masculine entry to a
feminine [_\*nēdrōn_]{.iv lang=pgmc sort=nedron role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:101"} ~ [_\*nadrōn_]{.iv lang=pgmc sort=nadron role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:101"} type [@Orel2003, 325].

The derivational input therefore is not a reshaped convenience form. It is the
comparative reconstruction that specifically underlies the Old English noun.

#### Old English evidence

The Old English word is securely represented by [_nǣdre_]{.iv lang=oe sort=naedre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:108"}, with [_næddre_]{.iv lang=oe sort=naeddre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:108"} as a
secondary variant. Clark Hall cross-references [_næddre_]{.iv lang=oe sort=naeddre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:109"} to [_nædre_]{.iv lang=oe sort=naedre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:109"}, and Fulk
treats [_næddre_]{.iv lang=oe sort=naeddre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:110"} as the later geminated form beside the older base [@ClarkHall1960,
225; @Fulk2018, 149].

#### Development to Old English

From [_\*nḗdrōn_]{.iv lang=pgmc sort=nedron role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:115"}, the stressed long mid vowel develops to Old English [_nǣdre_]{.iv lang=oe sort=naedre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:115"}, and
the weak feminine ending remains as final _-e_, giving [_nǣdre_]{.iv lang=oe sort=naedre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:116"}. The doubled
consonant of [_næddre_]{.iv lang=oe sort=naeddre source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:117"} is secondary and does not alter the inherited base form.

### bake — OE _bacan_

\index[oe]{bacan@\emph{bacan}}
\index[pgmc]{bakana@*bákaną}
\index[ohg]{backan@backan}
\index[ohg]{bahhan@bahhan}

Derivation: _\*bákaną_ > _bacan_ (regular).

#### Derivation trace

Proto input: _\*bákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bækaną} \\
OE A Restoration & \emph{*bakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bakan} \\
OE Secondary Nasalization & \emph{*bakąn} \\
OE Weak Tail Reduction & \emph{*bakan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bacan_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as [_\*bakanan_]{.iv lang=pgmc sort=bakanan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:171"} and cites Old English [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:171"} beside Old High German _backan, bahhan_ [@Orel2003]. Campbell gives [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:171"} as one of the standard examples of Old English A-restoration before a single consonant, and Ringe and Taylor state the same development from [_\*bakan_]{.iv lang=preoe sort=bakan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:171"} to Old English [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:171"} [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall both record [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:175"} as the ordinary Old English verb 'to bake' [@BosworthToller1898, 72; @ClarkHall1960]. The target in this entry is therefore the attested infinitive headword itself, not a selected oblique or finite paradigm cell.

#### Development to Old English

From [_\*bákaną_]{.iv lang=pgmc sort=bakana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:179"}, Anglo-Frisian brightening first gives _\*bækaną_. A-restoration then returns the stem vowel to _a_ before single _k_ plus the back-vocalic infinitive suffix, and later apocope and weak-tail reduction yield [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:179"} [@Campbell1959, 61; @RingeTaylor2014]. The development is therefore straightforward: [_\*bákaną_]{.iv lang=pgmc sort=bakana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:179"} > [_bacan_]{.iv lang=oe sort=bacan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:179"}.

### beech — OE _bōc_

\index[oe]{boc@\emph{bōc}}
\index[pgmc]{boko@*bōkō}

Derivation: _\*bōkō_ > _bōc_ (regular).

#### Derivation trace

Proto input: _\*bōkō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*bōku} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*bōk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bōc_

#### Reconstruction and comparative evidence

Kroonen gives the beech noun as _\*bōk(j)ō-_ and cites Old English _boc_, [_bēce_]{.iv lang=oe sort=bece source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:231"} among its reflexes [@Kroonen2013]. The form followed here, _\*bōkō_, is the nominative-singular shape of that family, which is the relevant comparison form here.

#### Old English evidence

Kroonen's Old English evidence already separates the paradigm material: _boc_ as the nominative form and [_bēce_]{.iv lang=oe sort=bece source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:235"} as an oblique form [@Kroonen2013]. The relevant comparator is therefore _bōc_; [_bēċe_]{.iv lang=oe sort=bece source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:235"} remains related paradigm evidence rather than the form chosen for this comparison.

#### Development to Old English

With nominative input _\*bōkō_, the development is compact. Northwest Germanic final long _ō_ raises to _u_, and later high-vowel apocope leaves _bōc_. The regular comparison is therefore _\*bōkō_ > _bōc_.

### begin — OE _beġinnan_

\index[oe]{beginnan@\emph{beġinnan}}
\index[pgmc]{biginnana@*bigínnaną}

Derivation: _\*bigínnaną_ > _beġinnan_ (regular).

#### Derivation trace

Proto input: _\*bigínnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*bigínnan} \\
OE Secondary Nasalization & \emph{*bigínnąn} \\
OE Velar Palatalization & \emph{*biʤínnąn} \\
OE Prefix I Reduction & \emph{*bĕʤínnąn} \\
OE Weak Tail Reduction & \emph{*bĕʤínnan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _beġinnan_

#### Reconstruction and comparative evidence

The verb is modeled here as inherited [_\*bigínnaną_]{.iv lang=pgmc sort=biginnana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:293"}. Ringe and Taylor state that intervocalic _\*g_ is palatalized between front vowels in Old English [@RingeTaylor2014], and Campbell lists [_ginnan_]{.iv lang=oe sort=ginnan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:293"} among familiar examples of palatal _g_ in this verb family [@Campbell1959, 174].

#### Old English evidence

Bosworth-Toller and Clark Hall lemmatize the verb as [_be-ginnan_]{.iv lang=oe sort=beginnan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:297"} / [_beginnan_]{.iv lang=oe sort=beginnan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:297"} [@BosworthToller1898, 84; @ClarkHall1960]. Those plain-_g_ dictionary spellings support the same verb that appears here in normalized form as [_beġinnan_]{.iv lang=oe sort=beginnan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:297"}.

#### Development note

The prefix deserves separate notice. Ringe and Taylor explicitly cite _bi- > be-_ as an Old English unstressed-prefix development [@RingeTaylor2014].

#### Development to Old English

From [_\*bigínnaną_]{.iv lang=pgmc sort=biginnana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:305"}, heavy-syllable nasal apocope yields _\*bigínnan_. Intervocalic _\*g_ between front vowels then palatalizes to _ġ_, and the unstressed prefix reduces _bi-_ to _be-_, giving [_beġinnan_]{.iv lang=oe sort=beginnan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:305"}.

### bier — OE _bǣr_

\index[oe]{baer@\emph{bǣr}}
\index[pgmc]{bero@*bḗrō}

Derivation: _\*bḗrō_ > _bǣr_ (regular).

#### Derivation trace

Proto input: _\*bḗrō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*bḗru} \\
\mbox{NWGmc Long E Lowering} & \emph{*bǣru} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*bǣr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bǣr_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as [_\*bērō-_]{.iv lang=pgmc sort=bero source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:358"} f. 'bier' and cites Old English [_bar_]{.iv lang=oe sort=bar source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:358"}, [_bær_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:358"} among the reflexes [@Kroonen2013, 717]. The derivational input [_\*bḗrō_]{.iv lang=pgmc sort=bero source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:358"} is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller lemmatize the noun as [_bær_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:362"}, and Kroonen also records [_bar_]{.iv lang=oe sort=bar source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:362"} beside it [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717]. The target [_bǣr_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:362"} is therefore a normalized long-vowel spelling of the same noun.

#### Source note

Lexicographic spellings vary between [_bær_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:366"} and [_bar_]{.iv lang=oe sort=bar source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:366"}. The normalized target [_bǣr_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:366"} represents the same long vowel [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717].

#### Development to Old English

From [_\*bḗrō_]{.iv lang=pgmc sort=bero source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:370"}, Northwest Germanic final long _ō_ raises to _u_, long _ē_ lowers to _ǣ_, and high-vowel apocope yields [_bǣr_]{.iv lang=oe sort=baer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:370"}. The resulting noun matches the normalized Old English target.

### birth — OE _byrd_

\index[oe]{byrd@\emph{byrd}}
\index[pgmc]{burdiz@*búrdiz}

Derivation: _\*búrdiz_ > _byrd_ (regular).

#### Derivation trace

Proto input: _\*búrdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*búrdi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*byrdi} \\
\mbox{OE High Vowel Apocope} & \emph{*byrd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _byrd_

#### Reconstruction and comparative evidence

Kroonen cites the noun under stem-level _\*burdi-_ and gives Old English _(ge-)byrd_ among the reflexes [@Kroonen2013]. The form followed here, _\*búrdiz_, is the nominative-style form that stands behind that stem label.

#### Old English evidence

Clark Hall and Bosworth-Toller both attest simplex _byrd_ as an Old English noun meaning 'birth' [@ClarkHall1960; @BosworthToller1898, 125]. The prefixed form _gebyrd_ is also well established in the tradition: Kroonen lists _(ge-)byrd_, Bosworth-Toller has a separate _ge-byrd_ entry, and Campbell cites _gebyrd_ and _gebyrdu_ in his grammatical discussion [@Kroonen2013; @BosworthToller1898, 125; @Campbell1959].

#### Form note

The relevant comparator here is the simplex noun _byrd_. The prefixed forms remain related attested material within the same lexical family, and Hogg's discussion of deverbal feminines provides the broader derivational setting [@Hogg1992].

#### Development to Old English

From _\*búrdiz_, loss of final _z_ gives _\*búrdi_. I-umlaut fronts _u_ to _y_, and high-vowel apocope then yields _byrd_. The result is the ordinary simplex Old English noun.

### bone — OE _bān_

\index[oe]{ban@\emph{bān}}
\index[pgmc]{baina@*báiną}

Derivation: _\*báiną_ > _bān_ (regular).

#### Derivation trace

Proto input: _\*báiną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*bāną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*bān} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bān_

#### Reconstruction and comparative evidence

Kroonen cites the noun as [_\*baina-_]{.iv lang=pgmc sort=baina source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:487"}, and Orel gives the same lexeme under [_\*bainan_]{.iv lang=pgmc sort=bainan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:487"} [@Kroonen2013; @Orel2003]. Both are comparative headword conventions for the same neuter noun whose Old English reflex is [_bān_]{.iv lang=oe sort=ban source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:487"}.

#### Old English evidence

Clark Hall and Bosworth-Toller record [_bān_]{.iv lang=oe sort=ban source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:491"} as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898]. Bright's glossary also distinguishes citation-form [_bān_]{.iv lang=oe sort=ban source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:491"} from oblique [_bāne_]{.iv lang=oe sort=bane source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:491"} [@BrightCassidyRingler1971].

#### Source note

The comparative headwords [_\*baina-_]{.iv lang=pgmc sort=baina source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:495"} and [_\*bainan_]{.iv lang=pgmc sort=bainan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:495"} provide lexeme background. The relevant comparison form here is the nominative-accusative singular [_\*báiną_]{.iv lang=pgmc sort=baina source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:495"}.

#### Development to Old English

West Germanic monophthongization turns stressed _\*ai_ into _ā_, giving _\*bāną_; heavy-syllable nasal apocope then yields [_bān_]{.iv lang=oe sort=ban source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:499"}. The resulting form matches the attested Old English citation noun.

### both — OE _bū_

\index[oe]{bu@\emph{bū}}
\index[pgmc]{bo@*bō}

Derivation: _\*bō_ > _bū_ (regular).

#### Derivation trace

Proto input: _\*bō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc Stressed Monosyllable O Raising & \emph{*bū} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bū_

#### Reconstruction and comparative evidence

Kroonen treats the Germanic numeral under _\*ba-_ and gives the inherited
paradigm _\*bai_, _\*bans_, _\*bōz_/_\*bōns_, _\*bō_, with Old English [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:550"}, [_bā_]{.iv lang=oe sort=ba role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:550"}, and
neuter [_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:551"} [@Kroonen2013, 47]. For the present entry, the relevant inherited
form is the unextended neuter dual [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:552"}.

The older explanation of [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:554"} derives it from _\*bō-jen-_, and Orel still
gives OE _bezen_ (< _\*bō-jenō)_ beside _ON_ [_báðir_]{.iv lang=on sort=badir role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:555"}, _OFris_ [_bēthe_]{.iv lang=ofris sort=bethe role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:555"}, _OS_ [_be-thia_]{.iv lang=os sort=bethia role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:555"},
and _OHG_ [_bēde_]{.iv lang=ohg sort=bede role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:556"} [@Orel2003, 65]. Fulk reports that explanation
cautiously and notes Seebold's preference for a _\*bō-þ-_ analysis instead
[@Fulk2018, §10.1]. That debate concerns [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:558"} and the extended forms
behind Modern English [_both_]{.iv lang=modeng sort=both role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:559"}, German [_beide_]{.iv lang=german sort=beide role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:559"}, and Dutch [_beide_]{.iv lang=dutch sort=beide role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:559"}; it does not
displace the inherited neuter [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:560"} > [_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:560"} treated here.

#### Old English evidence

The Old English dual paradigm is well established. Brunner gives masculine
[_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:565"}, feminine [_bā_]{.iv lang=oe sort=ba role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:565"}, and neuter [_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:565"} beside _bā_, with compounds such as
_bā_ _twā_, _bū_ _tū_, and _bām_ _twām_ [@SieversBrunner1965, §324 Anm. 2].
Campbell and Fulk present the same basic pattern: masculine [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:567"}, feminine
_bā_, neuter _bā_, _bū_, genitive _bēġra_, _bēġ(e)a_, and dative [_bǣm_]{.iv lang=oe sort=baem role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:568"}
[@Campbell1959, §683; @Fulk2018, §10.1].

[_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:571"} is therefore an attested neuter dual form, not a reconstruction. It is the
cleanest target for this entry because [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:572"} belongs to the historically more
contested _\*bō-jen-_ / analogical zone, while _bā_ remains a partner form
within the dual paradigm rather than the most straightforward monosyllabic
comparison.

#### Development to Old English

[_\*bō_]{.iv lang=pgmc sort=bo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:579"} is a stressed monosyllabic form. Campbell cites _cū_, _hū_, _tū_, and
[_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:580"} as examples of final accented _ō_ > _ū_ in the West Germanic stage leading
to Old English [@Campbell1959, §122]. Brunner states the same development more
directly: Auslautendes _ō_ erscheint als û in _bū_ ... cu ... _hū_, _tū_
[@SieversBrunner1965, §69].

The development is therefore straightforward: [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:585"} > [_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:585"}.

#### Form comparison

The comparison below sets the relevant forms side by side. It separates the inherited OE target from the
other forms that belong to the same broader lexical history.

| Form | Source / stage | Status | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| [_\*bō_]{.iv lang=pgmc sort=bo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:594"} > [_bū_]{.iv lang=oe sort=bu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:594"} | PGmc neuter dual > OE neuter dual | selected regular comparison | main line of the entry |
| [_bēġen_]{.iv lang=oe sort=begen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:595"} | OE masculine dual | attested, but historically contested and at least partly analogical in Kroonen | real OE evidence, not the Old English form here |
| [_bā_]{.iv lang=oe sort=ba role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:596"} | OE feminine dual; also neuter variant | attested partner form | part of the OE paradigm, but not the chosen monosyllabic comparator |
| [_báðir_]{.iv lang=on sort=badir role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:597"}, German [_beide_]{.iv lang=german sort=beide role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:597"}, Dutch [_beide_]{.iv lang=dutch sort=beide role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:597"}, Modern English [_both_]{.iv lang=modeng sort=both role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:597"} | Norse, continental West Germanic, Modern English extended forms | related but different formation | useful background, not the direct continuation of OE _bū_ |

### bow — OE _bīeġan_

\index[oe]{biegan@\emph{bīeġan}}
\index[pgmc]{baugijana@*báugijaną}

Derivation: _\*báugijaną_ > _bīeġan_ (regular).

#### Derivation trace

Proto input: _\*báugijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*báeugijaną} \\
OE Diphthong Leveling & \emph{*bēagijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bēagijan} \\
OE Secondary Nasalization & \emph{*bēagijąn} \\
Sievers Law Syncope & \emph{*bēagjąn} \\
OE Velar Palatalization & \emph{*bēaʤjąn} \\
OE I Umlaut & \emph{*bīeʤjąn} \\
OE Weak Tail Reduction & \emph{*bīeʤjan} \\
OE J Loss After Heavy & \emph{*bīeʤan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bīeġan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the weak verb as _\*baugjan-_ 'to (make) bend' and cites Old English _biegan_ among its reflexes [@Kroonen2013]. Ringe and Taylor give the northwest Germanic preform _\*baugijana_, with later _\*béagjan_ behind West Saxon Old English _biegan_ [@RingeTaylor2014]. The entry therefore concerns the weak causative member of the bend-family, alongside the related strong verb and noun.

#### Old English evidence

Clark Hall lemmatizes _biegan_, and Bosworth-Toller records _bigan_ with examples such as Ic _bēge_ _mīne_ _cneówa_ and Se ord _bīgde_ upp _tō_ _þām_ hiltum [@ClarkHall1960; @BosworthToller1898, 102]. The form _bīeġan_ used here is a normalized spelling of that attested Old English weak verb.

#### Development to Old English

From _\*báugijaną_, the stem reaches pre-Old-English _\*bēagjan_, after which palatalization of _\*gj_ and i-umlaut yield West Saxon _biegan_; Campbell lists _biegan_ among the regular _ie_ outcomes of _\*éa_ under i-umlaut [@RingeTaylor2014; @Campbell1959, 80]. The development is therefore straightforward: _\*báugijaną_ > _bīeġan_.

### breeches — OE _brēċ_

\index[oe]{brec@\emph{brēċ}}
\index[pgmc]{brokiz@*brōkiz}

Derivation: _\*brōkiz_ > _brēċ_ (regular).

#### Derivation trace

Proto input: _\*brōkiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*brōki} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Palatalization & \emph{*brōʧi} \\
OE I Umlaut & \emph{*brēʧi} \\
\mbox{OE High Vowel Apocope} & \emph{*brēʧ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brēċ_

#### Reconstruction and comparative evidence

Kroonen cites the noun under _\*brōk-_, with Old English _brōc_ and plural 'breeches' among its reflexes [@Kroonen2013]. Ringe and Taylor give the plural development directly as PNWGmc _\*brokiz_ > _\*breeci_ > OE _bréc_ [@RingeTaylor2014]. The deeper verbal base belongs to the noun's etymological background, while the derivational input here is the plural noun form _\*brōkiz_.

#### Old English evidence

Bright notes _brōc_ with plural _brēc_, and Clark Hall gives _brēc_ fp. breeches while also listing _broc_ as a feminine noun probably represented chiefly in the plural [@BrightCassidyRingler1971; @ClarkHall1960, 64]. I write _brēċ_ for the long vowel and palatal consonant; the attested plural is _brēc_.

#### Development to Old English

After loss of final _-z_, the stem ends in _-ki_, so the velar palatalizes and _ō_ undergoes i-umlaut to _ē_; final high-vowel apocope then yields _brēċ_ [@RingeTaylor2014]. The development is therefore regular: _\*brōkiz_ > _brēċ_.

### calf — OE _ċealf_

\index[oe]{cealf@\emph{ċealf}}
\index[pgmc]{kalbaz@*kálbaz}

Derivation: _\*kálbaz_ > _ċealf_ (regular).

#### Derivation trace

Proto input: _\*kálbaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kálba} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*kálb} \\
Anglo Frisian Brightening & \emph{*kælb} \\
OE Breaking & \emph{*kealb} \\
PGmc B Allophony & \emph{*kealβ} \\
OE Velar Palatalization & \emph{*ʧealβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ċealf_

#### Reconstruction and comparative evidence

Kroonen treats the noun under _\*kalbiz-_ and notes an older s-stem _\*kalbaz_, pl. _\*kalbizō_, while Orel cites _\*kalbaz_ as the citation form and Ringe and Taylor derive West Saxon _Cealf_ from _\*kalbaz_, _\*kalbiz-_ [@Kroonen2013; @Orel2003, 248; @RingeTaylor2014, 220]. The derivational input here is the singular _\*kálbaz_, since the entry concerns the citation-form noun.

#### Old English evidence

Clark Hall gives [_cealf_]{.iv lang=oe sort=cealf source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:785"} I. (æ, e) nm. (nap. [_cealfru_]{.iv lang=oe sort=cealfru source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:785"}), and Bosworth-Toller likewise records _Caelf_ / _Cealf_ beside plural forms such as _calfur_ and [_cealfru_]{.iv lang=oe sort=cealfru source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:785"} [@ClarkHall1960; @BosworthToller1898, 131]. Campbell and Fulk show the same singular-plus-_-r-_ plural pattern [@Campbell1959; @Fulk2018, 193]. I write _ċealf_ for the palatalized initial; the attested dictionary headword is [_cealf_]{.iv lang=oe sort=cealf source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:785"}.

#### Development to Old English

After loss of final _-z_ and bare _-a_, Anglo-Frisian brightening gives _\*kælb_, and breaking before _l_ plus consonant yields _\*kealb_. Ringe and Taylor's account of the lexeme and their rule for initial _k_ in front-vocalic environments support the West Saxon palatalized onset represented here as _ċ-_, so _\*kálbaz_ develops regularly to _ċealf_ [@RingeTaylor2014, 220].

### corn — OE _corn_

\index[oe]{corn@\emph{corn}}
\index[pgmc]{kurna@*kúrną}

Derivation: _\*kúrną_ > _corn_ (regular).

#### Derivation trace

Proto input: _\*kúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*kórną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*kórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _corn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*kurna-_, and Orel gives the citation form _\*kurnan_, both with Old English _corn_ among the reflexes [@Kroonen2013; @Orel2003, 264]. The singular form _\*kúrną_ is the nominative-accusative singular appropriate to the citation noun.

#### Old English evidence

Clark Hall gives _corn n. 'corn,' grain_, Bright's glossary lists _corn, n._ with genitive singular _cornes_, and Bosworth-Toller treats _corn_ as an ordinary noun headword [@ClarkHall1960; @BrightCassidyRingler1971, 347; @BosworthToller1898, 144]. The target is therefore an attested citation form, while forms such as _cornes_ simply provide paradigm background.

#### Development to Old English

With northwest Germanic lowering, _\*kúrną_ becomes _\*kórną_, and later loss of final nasal after a heavy syllable yields _\*kórn_, whence _corn_. The oblique form _\*kurnăn_ belongs to comparative background rather than to the derivational input of this entry.

### deed — OE _dǣd_

\index[oe]{daed@\emph{dǣd}}
\index[pgmc]{dediz@*dḗdiz}

Derivation: _\*dḗdiz_ > _dǣd_ (regular).

#### Derivation trace

Proto input: _\*dḗdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*dḗdi} \\
\mbox{NWGmc Long E Lowering} & \emph{*dǣdi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*dǣd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dǣd_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*dēdiz_, and Ringe and Taylor derive the same inherited i-stem from Proto-Germanic _\*dédiz_ through northwest Germanic _\*dadiz_ [@Orel2003; @RingeTaylor2014]. The acute accent in _\*dḗdiz_ marks stress on the same reconstructed long vowel.

#### Old English evidence

Campbell states that Primitive Germanic _ē_ appears as West Saxon _ǣ_ but in other Old English dialects mostly as _ē_, and Brunner gives the contrast explicitly as West Saxon _dǣd_ beside non-West-Saxon _dēd_ [@Campbell1959; @SieversBrunner1965]. Clark Hall likewise lists _dæd_ and cross-refers Anglian _dēd_ to it [@ClarkHall1960]. West Saxon _dǣd_ is therefore the relevant Old English form here, with Anglian _dēd_ as a dialectal doublet.

#### Development to Old English

From inherited _\*dēdiz_, loss of final _-z_ and the West Saxon lowering of stressed long _ē_ yield _dǣd_; Anglian _dēd_ preserves the non-West-Saxon outcome [@Campbell1959; @SieversBrunner1965]. The development treated here is therefore the regular West Saxon line.

### door — OE _dor_

\index[oe]{dor@\emph{dor}}
\index[pgmc]{dura@*dúrą}
\index[ohg]{tura@tura}
\index[ofris]{dore@dore}

Derivation: _\*dúrą_ > _dor_ (regular).

#### Derivation trace

Proto input: _\*dúrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*dórą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*dór} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dor_

#### Reconstruction and comparative evidence

Kroonen reconstructs a neuter _\*dura-_ 'gate, (single) door' and cites Old English _dor_ among its reflexes. In the same entry he separates Old English _duru_, Old Frisian _dore_, and Old High German _tura_ as reflexes of _\*durō-_ instead [@Kroonen2013].

#### Old English evidence

Clark Hall records _dor_ as a neuter noun and separately records feminine _duru_ with its own inflection [@ClarkHall1960]. Ringe and Taylor likewise treat _duru_ as an early Old English u-stem, originally a root noun shifted into that class [@RingeTaylor2014]. The Old English form here is therefore the attested neuter _dor_, while _duru_ remains a parallel Old English reflex from another stem history.

#### Development to Old English

From _\*dúrą_, Northwest Germanic u-lowering gives _\*dórą_, and heavy-syllable nasal apocope then yields _dor_. The regular development treated in this entry is therefore _\*dúrą_ > _dor_; the feminine _duru_ belongs to the separate line identified by Kroonen and Ringe-Taylor [@Kroonen2013; @RingeTaylor2014].

### fare — OE _faran_

\index[oe]{faran@\emph{faran}}
\index[pgmc]{farana@*fáraną}

Derivation: _\*fáraną_ > _faran_ (regular).

#### Derivation trace

Proto input: _\*fáraną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*færaną} \\
OE A Restoration & \emph{*faraną} \\
OE Heavy Syllable Nasal Apocope & \emph{*faran} \\
OE Secondary Nasalization & \emph{*farąn} \\
OE Weak Tail Reduction & \emph{*faran} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _faran_

#### Reconstruction and comparative evidence

Kroonen gives the inherited strong verb as _\*faran-_, and Orel gives the same lexeme as _\*faranan_, both with Old English _faran_ among the reflexes [@Kroonen2013; @Orel2003, 132]. Campbell also uses _faran_ as a standard example of Old English A-restoration [@Campbell1959, 61].

#### Old English evidence

Clark Hall lemmatizes the strong verb as _faran_ and separately records weak _færan_ 'to frighten'; [_fære_]{.iv lang=oe sort=faere source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:1028"}, [_færst_]{.iv lang=oe sort=faerst source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:1028"}, and [_færð_]{.iv lang=oe sort=faerd source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:1028"} belong to present-tense forms of _faran_ rather than to the infinitive itself [@ClarkHall1960]. Bosworth-Toller preserves the same distinction [@BosworthToller1898, 108]. The Old English form here is therefore the attested citation infinitive _faran_.

#### Development to Old English

From _\*fáraną_, Anglo-Frisian brightening first gives _\*færaną_, but A-restoration before single _r_ returns _\*faraną_; later apocope and weak-tail reduction yield _faran_ [@Campbell1959, 61]. Fulk's contrast with participial faren- < _\*faræn-_ < _\*faran-_ shows why fronting elsewhere in the paradigm does not alter the infinitive headword [@Fulk2018].

### fell — OE _fell_

\index[oe]{fell@\emph{fell}}
\index[pgmc]{fella@*féllą}

Derivation: _\*féllą_ > _fell_ (regular).

#### Derivation trace

Proto input: _\*féllą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*féll} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fell_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*fella-_ 'membrane, skin, hide' and cites Old English _fell_ beside Dutch _vel_ and German _Fell_ [@Kroonen2013]. The form followed here, _\*féllą_, is the derivable singular form of that same inherited noun.

#### Old English evidence

Clark Hall records _fell_ as the noun 'fell, skin, hide', and Bright's glossary likewise gives _fell_ with inflected forms such as accusative singular _fel_ and dative plural _fellum_ [@ClarkHall1960; @BrightCassidyRingler1971]. The target is therefore the attested noun _fell_, not the verb _fellan_ or the preterite _feoll_.

#### Development to Old English

With _\*féllą_, no special earlier reshaping is needed: heavy-syllable nasal apocope yields _\*féll_, surfacing as _fell_. The regular development treated here is therefore _\*féllą_ > _fell_.

### fern — OE _fearn_

\index[oe]{fearn@\emph{fearn}}
\index[pgmc]{farnaz@*fárnaz}

Derivation: _\*fárnaz_ > _fearn_ (regular).

#### Derivation trace

Proto input: _\*fárnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*fárna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fárn} \\
Anglo Frisian Brightening & \emph{*færn} \\
OE Breaking & \emph{*fearn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as masculine _\*farna-_ and gives Old English _fearn, fern_, while Orel gives the same lexeme as neuter _\*farnan_ with Old English _fearn_ [@Kroonen2013; @Orel2003, 133]. Those are comparative headword conventions rather than competing Old English outcomes; the modeled input here is the nominative-style _\*fárnaz_.

#### Old English evidence

Clark Hall gives _fearn_ as an Old English noun, and Bosworth-Toller records _fearn_ with inflected forms such as _fearnes_, _fearna_, and _fearne_ [@ClarkHall1960; @BosworthToller1898, 219]. Kroonen also records _fern_, but the local lexical sources give stronger support to _fearn_ as the citation target [@Kroonen2013].

#### Development to Old English

From _\*fárnaz_, loss of final _-z_ and final _-a_ gives _\*fárn_; Anglo-Frisian brightening then yields _\*færn_, and breaking before _r_ plus consonant gives _fearn_ [@Campbell1959; @RingeTaylor2014]. The development treated here is therefore the regular _rC_-breaking line.

### field — OE _feld_

\index[oe]{feld@\emph{feld}}
\index[pgmc]{felthuz@*félθuz}

Derivation: _\*félθuz_ > _feld_ (regular).

#### Derivation trace

Proto input: _\*félθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*félduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*féldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*féld} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _feld_

#### Reconstruction and comparative evidence

Ringe and Taylor treat Old English _feld_ as one of the cases where earlier _\*felþu-_ ~ _\*feldu-_ may reflect either inherited _\*þ_ ~ _\*d_ alternation or the regular West Germanic development _\*lþ_ > _ld_ [@RingeTaylor2014, 170]. The broader proto label _\*félθuz_ can remain as comparative background, while that narrower historical ambiguity does not affect the regular classification.

#### Old English evidence

Clark Hall records _feld_ with oblique forms such as _felda_ and _felde_, and Campbell notes early place-name spellings in _-felth_ beside the later standard form [@ClarkHall1960, 114; @Campbell1959, 169]. The Old English form here is therefore the attested citation noun _feld_, with the older _-felth_ spellings as historical support rather than as rival targets.

#### Development to Old English

In the modeled pathway, medial _\*lþ_ becomes _ld_, final _-z_ is lost, and high-vowel apocope then yields _feld_. Whether the voiced dental ultimately reflects inherited alternation or the regular _\*lþ_ > _ld_ development, both accounts converge on the same Old English form [@RingeTaylor2014, 170].

### fly — OE _flēogan_

\index[oe]{fleogan@\emph{flēogan}}
\index[pgmc]{fleugana@*fléuganą}

Derivation: _\*fléuganą_ > _flēogan_ (regular).

#### Derivation trace

Proto input: _\*fléuganą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*flēoganą} \\
OE Heavy Syllable Nasal Apocope & \emph{*flēogan} \\
OE Secondary Nasalization & \emph{*flēogąn} \\
OE Weak Tail Reduction & \emph{*flēogan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _flēogan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive the verb as _\*fleugana_ > OE _fléogan_ and elsewhere contrast West Saxon _fléogan_ with Anglian _flégan_, alongside related forms _fléoge_ / _flége_ [@RingeTaylor2014]. The form followed here, _\*fléuganą_, represents that inherited strong verb in the notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller record _flēogan_ as the ordinary Old English strong verb, and Bright gives the familiar paradigm _flēag_, flugon, flogen with present _fleogeð_ [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971]. The target in this entry is therefore the attested verbal infinitive itself.

#### Form note

Ringe and Taylor also list related _fléoge_ / _flége_ and Anglian _flégan_, which belong to the same family but do not replace the infinitive _flēogan_ treated here [@RingeTaylor2014].

#### Development to Old English

From _\*fléuganą_, Old English diphthong leveling gives _\*flēoganą_; heavy-syllable nasal apocope and weak-tail reduction then yield _flēogan_ [@RingeTaylor2014]. The development is therefore regular: _\*fléuganą_ > _flēogan_.

### forlorn — OE _lēosan_

\index[oe]{leosan@\emph{lēosan}}
\index[pgmc]{leusana@*léusaną}

Derivation: _\*léusaną_ > _lēosan_ (regular).

#### Derivation trace

Proto input: _\*léusaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*lēosaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēosan} \\
OE Secondary Nasalization & \emph{*lēosąn} \\
OE Weak Tail Reduction & \emph{*lēosan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lēosan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the verb under _\*leusan-_ and cites prefixed daughters such as Gothic _fra-liusan_ and Old English _for-lēosan_; Orel likewise gives Old English _for-leósan_ [@Kroonen2013; @Orel2003]. The inherited verbal base is therefore clear, though the daughter set often appears with the prefix.

#### Old English evidence

The direct Old English evidence behind English _forlorn_ lies in the prefixed verb _forlēosan_ and especially in the participle _forloren_, recorded by Ringe and Taylor and in the dictionaries [@RingeTaylor2014; @ClarkHall1960; @BosworthToller1898]. The simplex infinitive _lēosan_ represents the verbal base itself.

#### Form note

As a base-form comparison, the simplex infinitive is _lēosan_, while the English adjective continues the prefixed Old English family _forlēosan_ / _forloren_ [@RingeTaylor2014].

#### Development to Old English

From _\*léusaną_, Old English diphthong leveling gives _\*lēosaną_, and later nasal apocope and weak-tail reduction yield _lēosan_ [@RingeTaylor2014]. The prefixed forms follow the same verbal base with added _for-_.

### gang — OE _gang_

\index[oe]{gang@\emph{gang}}
\index[pgmc]{gangaz@*gángaz}
\index[on]{gangr@gangr}

Derivation: _\*gángaz_ > _gang_ (regular).

#### Derivation trace

Proto input: _\*gángaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*gánga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*gáng} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _gang_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*gangaz_ and cites Old English _gang_ beside Old Norse _gangr_, Old Frisian _gang_ / _gong_, Old Saxon _gang_, and Old High German _gang_ [@Orel2003]. The form followed here, _\*gángaz_, is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller both record _gang_ as the noun 'going, journey, way', and Bright's glossary gives _gong (gang), m., path, course_ [@ClarkHall1960; @BosworthToller1898, 159; @BrightCassidyRingler1971, 392]. The target is therefore the attested noun headword itself.

#### Form note

This entry concerns the noun _gang_, not the separate verb _gangan_ [@ClarkHall1960; @BosworthToller1898, 159].

#### Development to Old English

From _\*gángaz_, loss of final _-z_ gives _\*gánga_, and later loss of final bare _-a_ yields _gang_. The development is therefore regular: _\*gángaz_ > _gang_.

### give — OE _ġiefan_

\index[oe]{giefan@\emph{ġiefan}}
\index[pgmc]{gebana@*gébaną}

Derivation: _\*gébaną_ > _ġiefan_ (regular).

#### Derivation trace

Proto input: _\*gébaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*géban} \\
OE Secondary Nasalization & \emph{*gébąn} \\
PGmc B Allophony & \emph{*géβąn} \\
OE Velar Palatalization & \emph{*ʤéβąn} \\
OE Ws Palatal Diphthongization & \emph{*ʤíeβąn} \\
OE Weak Tail Reduction & \emph{*ʤíeβan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġiefan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*geban-_ and cites Old English _giefan_ among its reflexes [@Kroonen2013]. Ringe and Taylor contrast West Saxon _giefan_ with Mercian _for-geofan_ and Northumbrian _geafa_, showing that the inherited verb takes different later dialectal shapes [@RingeTaylor2014].

#### Old English evidence

Campbell gives _gefan_ (W-S _giefan_) among examples of initial palatalization, and Clark Hall records the verb under plain _giefan_ with forms such as _geaf_ and _giefen_ [@Campbell1959; @ClarkHall1960]. I write _ġiefan_ for the palatal initial.

#### Dialect note

West Saxon _ie_ here reflects palatal diphthongization after initial palatalization; non-West-Saxon forms such as _geafa_ or _for-geofan_ continue the same verb without the West Saxon vocalism [@RingeTaylor2014].

#### Development to Old English

From _\*gébaną_, initial _g_ palatalizes before _e_; West Saxon palatal diphthongization then yields _ie_, and later tail reduction gives _giefan_ [@Campbell1959; @RingeTaylor2014]. The result is therefore the regular West Saxon infinitive.

### gold — OE _gold_

\index[oe]{gold@\emph{gold}}
\index[pgmc]{gultha@*gúlθą}

Derivation: _\*gúlθą_ > _gold_ (regular).

#### Derivation trace

Proto input: _\*gúlθą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*gúldą} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*góldą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*góld} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _gold_

#### Reconstruction and comparative evidence

Ringe and Taylor cite the noun as _\*gulþa-_ / _\*gulda-_, and Kroonen gives the same pair [@RingeTaylor2014, 42; @Kroonen2013]. The form followed here, _\*gúlθą_, preserves the older consonantal form while leaving open whether the medial stop reflects inherited alternation or regular West Germanic development.

#### Old English evidence

Bosworth-Toller and Clark Hall both record _gold_ as the ordinary Old English neuter noun [@BosworthToller1898, 121; @ClarkHall1960, 152]. The target is therefore the attested citation form itself.

#### Development note

Ringe and Taylor note that the medial stop can be understood either as alternation _\*gulþa-_ / _\*gulda-_ or as the ordinary West Germanic change _\*lþ_ > _ld_; both routes lead to the same Old English consonantism [@RingeTaylor2014, 42].

#### Development to Old English

From _\*gúlθą_, the regular consonant development gives _\*gúldą_; Northwest Germanic / Old English lowering then yields _\*góldą_, and apocope gives _gold_ [@Campbell1959; @RingeTaylor2014, 42].

### grave — OE _grafan_

\index[oe]{grafan@\emph{grafan}}
\index[pgmc]{grabana@*grábaną}

Derivation: _\*grábaną_ > _grafan_ (regular).

#### Derivation trace

Proto input: _\*grábaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*græbaną} \\
OE A Restoration & \emph{*grabaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*graban} \\
OE Secondary Nasalization & \emph{*grabąn} \\
PGmc B Allophony & \emph{*graβąn} \\
OE Weak Tail Reduction & \emph{*graβan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _grafan_

#### Reconstruction and comparative evidence

Campbell gives _grafan_ among the standard examples of Old English a-restoration before a single consonant and a following back vowel, and Ringe and Taylor describe the same development for Class VI infinitives [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Clark Hall records _grafan_ as the verb 'to dig, grave' and separately records noun _græf_ 'grave, trench' [@ClarkHall1960]. The target here is the attested infinitive headword of the verb.

#### Development to Old English

From _\*grábaną_, Anglo-Frisian brightening first gives a fronted stem vowel. A-restoration then returns _a_ before single _b_ plus the back-vocalic infinitive ending, and later apocope and weak-tail reduction yield _grafan_ [@Campbell1959, 61; @RingeTaylor2014].

#### Form note

Noun _græf_ and verbal forms such as _græfð_ or past participial _græfen_ belong to other lexical or paradigm positions and do not replace the infinitive _grafan_ as the target here [@ClarkHall1960].

### guest — OE _ġiest_

\index[oe]{giest@\emph{ġiest}}
\index[pgmc]{gastiz@*gástiz}

Derivation: _\*gástiz_ > _ġiest_ (regular).

#### Derivation trace

Proto input: _\*gástiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*gásti} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gæsti} \\
OE Velar Palatalization & \emph{*ʤæsti} \\
OE I Umlaut & \emph{*ʤesti} \\
OE Ws Palatal Diphthongization & \emph{*ʤiesti} \\
\mbox{OE High Vowel Apocope} & \emph{*ʤiest} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġiest_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the noun as an ordinary i-stem whose West Saxon development shows palatal diphthongization, while non-West-Saxon evidence preserves forms of the _gest_ type [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record the word under forms such as _gist_, _gest_, _giest_, and _gyst_ [@BosworthToller1898; @ClarkHall1960]. The Old English form here, _ġiest_, is the normalized West Saxon form within that attested family.

#### Development to Old English

From _\*gástiz_, Anglo-Frisian brightening gives a _gæst-_ stage, and i-mutation affects the front vowel before the lost high-vocalic ending. In West Saxon the initial palatal environment then produces _ie_, so the regular outcome is _ġiest_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _ġiest_ is the Old English form here. Anglian _gest_ and related spellings remain real Old English comparators rather than corrections to that choice [@RingeTaylor2014; @BosworthToller1898].

### hair — OE _hǣr_

\index[oe]{haer@\emph{hǣr}}
\index[pgmc]{xera@*xḗrą}

Derivation: _\*xḗrą_ > _hǣr_ (regular).

#### Derivation trace

Proto input: _\*xḗrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*xǣrą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çǣrą} \\
OE Heavy Syllable Nasal Apocope & \emph{*çǣr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hǣr_

#### Reconstruction and comparative evidence

Kroonen cites the ordinary Proto-Germanic hair word as _\*hēra-_ [@Kroonen2013]. The form followed here, _\*xḗrą_, represents that same long-ē stem in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hær_ / _hǣr_ as the ordinary Old English noun 'hair' [@ClarkHall1960, 158; @BosworthToller1898, 510]. The target is therefore the attested headword itself.

#### Development to Old English

From _\*xḗrą_, Northwest Germanic lowering gives a long front vowel, and later loss of the final nasal leaves the Old English form _hǣr_. The development treated here is straightforward and does not require any special paradigm choice.

#### Form note

Older references to _\*xazwăz_ belong to a different lexeme, and the separate _haddr_ / _heordan_ / _hād-_ material does not displace the ordinary simplex _hǣr_ treated here [@Kroonen2013; @ClarkHall1960, 158].

### harvest — OE _hierfest_

\index[oe]{hierfest@\emph{hierfest}}
\index[pgmc]{xarbistuz@*xárbistuz}

Derivation: _\*xárbistuz_ > _hierfest_ (regular).

#### Derivation trace

Proto input: _\*xárbistuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*xárbistu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xærbistu} \\
OE Breaking & \emph{*xearbistu} \\
OE Velar Fricative Palatalization & \emph{*çearbistu} \\
PGmc B Allophony & \emph{*çearβistu} \\
OE I Umlaut & \emph{*çierβistu} \\
OE High Vowel Apocope & \emph{*çierβist} \\
OE Med Unstressed I Lowering1 & \emph{*çierβest} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hierfest_

#### Reconstruction and comparative evidence

Bammesberger and Ringe-Taylor treat _\*harbist-_ as the inherited base and explain that the regular native West Saxon development would be of the _hierfest_ / _hyrfest_ type [@Bammesberger1997; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record _hærfest_, with _herfest_ as a variant in the lexical tradition [@BosworthToller1898; @ClarkHall1960]. Those attested forms remain the main dictionary evidence for the noun.

#### Development to Old English

From _\*xárbistuz_, Anglo-Frisian brightening, breaking, and i-mutation produce a _hierbist-_ stage, and later lowering of unstressed medial _i_ to _e_ gives _hierfest_. That is the regular West Saxon development treated here [@RingeTaylor2014; @Campbell1959].

#### Source note

The Old English form here, _hierfest_, represents the regular native West Saxon outcome discussed by Bammesberger and Ringe-Taylor. The attested Old English lexical tradition, however, is chiefly _hærfest_ / _herfest_, commonly treated as non-West-Saxon or Anglian material in West Saxon transmission [@Bammesberger1997; @RingeTaylor2014].

### hedge — OE _heġġ_

\index[oe]{hegg@\emph{heġġ}}
\index[pgmc]{xagjaz@*xágjaz}

Derivation: _\*xágjaz_ > _heġġ_ (regular).

#### Derivation trace

Proto input: _\*xágjaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*xággjaz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xággja} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xággj} \\
Anglo Frisian Brightening & \emph{*xæggj} \\
OE Velar Fricative Palatalization & \emph{*çæggj} \\
OE Velar Palatalization & \emph{*çæʤʤj} \\
OE I Umlaut & \emph{*çeʤʤj} \\
OE J Loss After Heavy & \emph{*çeʤʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _heġġ_

#### Reconstruction and comparative evidence

The derivational input models a palatal _\*-gj-_ noun whose Old English development includes gemination, palatalization, and i-mutation. The current derivation therefore reaches a palatal-geminate outcome of the _heġġ_ type [@Campbell1959].

#### Old English evidence

Bosworth-Toller and Clark Hall record the noun under standard spellings _hecg_ / _heċġ_ [@BosworthToller1898; @ClarkHall1960]. The lexical item itself is therefore well attested even though the form compared here is normalized.

#### Development to Old English

From _\*xágjaz_, West Germanic j-gemination first yields a geminate stop, and later Old English palatalization and loss of final _j_ produce _heġġ_. The development is treated as regular rather than exceptional.

#### Form note

Standard dictionary spelling is _heċġ_ or _hecg_. Normalized _heġġ_ is the Old English form here, while the ordinary lexicographic forms remain the main Old English citation evidence [@BosworthToller1898; @ClarkHall1960].

### helm — OE _helm_

\index[oe]{helm@\emph{helm}}
\index[pgmc]{xelmaz@*xélmaz}

Derivation: _\*xélmaz_ > _helm_ (regular).

#### Derivation trace

Proto input: _\*xélmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xélma} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xélm} \\
OE Velar Fricative Palatalization & \emph{*çélm} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _helm_

#### Reconstruction and comparative evidence

Kroonen cites the helmet noun as _\*helma-_ and separately distinguishes a different lexeme _\*helman-_ 'rudder' [@Kroonen2013]. The form followed here, _\*xélmaz_, is the nominative-style form used for the helmet noun itself.

#### Old English evidence

Clark Hall and Bosworth-Toller record _helm_ as the ordinary Old English noun for 'helmet', while _helma_ belongs to a separate rudder lexeme [@ClarkHall1960; @BosworthToller1898, 542].

#### Development to Old English

From _\*xélmaz_, loss of final _z_ and later loss of the short final vowel yield _helm_. The development is therefore a straightforward citation-form match.

#### Form note

Comparative _\*helma-_ is headword notation for the helmet cognate set. It should not be confused with Old English _helma_, which is a different noun meaning 'helm, rudder' [@Kroonen2013; @ClarkHall1960].

### help — OE _helpan_

\index[oe]{helpan@\emph{helpan}}
\index[pgmc]{xelpana@*xélpaną}

Derivation: _\*xélpaną_ > _helpan_ (regular).

#### Derivation trace

Proto input: _\*xélpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çélpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çélpan} \\
OE Secondary Nasalization & \emph{*çélpąn} \\
OE Weak Tail Reduction & \emph{*çélpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _helpan_

#### Reconstruction and comparative evidence

The entry treats the strong verb itself rather than the separate noun _help_. Bright's principal parts _helpan, healp, hulpon, holpen_ show the ordinary Old English strong-verb family continued by this input [@BrightCassidyRingler1971].

#### Old English evidence

Clark Hall and Bosworth-Toller record _helpan_ as the verbal headword 'to help' [@ClarkHall1960; @BosworthToller1898, 542]. The target is therefore the attested infinitive citation form.

#### Development to Old English

From _\*xélpaną_, no special repair is needed beyond the ordinary reduction of the infinitive ending. The derivation therefore reaches _helpan_ directly.

#### Form note

Noun _help_ belongs to a separate lexical line and should not replace verbal _helpan_ as the target here [@ClarkHall1960; @BosworthToller1898, 542].

### hind — OE _hind_

\index[oe]{hind@\emph{hind}}
\index[pgmc]{xendjo@*xéndjō}

Derivation: _\*xéndjō_ > _hind_ (regular).

#### Derivation trace

Proto input: _\*xéndjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*xéndju} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Velar Fricative Palatalization & \emph{*çéndju} \\
OE I Umlaut & \emph{*çindju} \\
\mbox{OE High Vowel Apocope} & \emph{*çindj} \\
OE J Loss After Heavy & \emph{*çind} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hind_

#### Reconstruction and comparative evidence

Kroonen cites the animal name as _\*hindō-_ f. 'hind' [@Kroonen2013]. The form followed here, _\*xéndjō_, represents that same noun in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hind_ as the noun 'hind, female deer' [@ClarkHall1960; @BosworthToller1898, 554]. The target is therefore the attested lexical item itself.

#### Development to Old English

From _\*xéndjō_, i-mutation produces the front-vocalic Old English stem, and later apocope plus loss of final _j_ yield _hind_. The outcome is therefore a regular citation-form derivation.

#### Form note

_hindan_ 'from behind, behind' is a different Old English lexeme and does not belong to the noun history of _hind_ [@ClarkHall1960; @BosworthToller1898, 554].

### hold — OE _healdan_

\index[oe]{healdan@\emph{healdan}}
\index[pgmc]{xaldana@*xáldaną}

Derivation: _\*xáldaną_ > _healdan_ (regular).

#### Derivation trace

Proto input: _\*xáldaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xældaną} \\
OE Breaking & \emph{*xealdaną} \\
OE Velar Fricative Palatalization & \emph{*çealdaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çealdan} \\
OE Secondary Nasalization & \emph{*çealdąn} \\
OE Weak Tail Reduction & \emph{*çealdan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _healdan_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the verb as a regular _\*a_ + lC breaking case, with West Saxon _healdan_ opposed to Anglian and Mercian _haldan_ [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bright gives the ordinary strong-verb citation form and principal parts _healdan, heold, heoldon, healden_ [@BrightCassidyRingler1971]. The target is therefore the attested infinitive headword itself.

#### Development to Old English

From _\*xáldaną_, Anglo-Frisian brightening first yields a fronted vowel, and West Saxon breaking then produces _ea_ before _ld_. Later reduction of the infinitive ending gives _healdan_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _healdan_ is the Old English form here. Anglian and Mercian _haldan_ are genuine non-West-Saxon doublets rather than corrections to that choice [@Campbell1959; @RingeTaylor2014].

### horn — OE _horn_

\index[oe]{horn@\emph{horn}}
\index[pgmc]{xurna@*xúrną}

Derivation: _\*xúrną_ > _horn_ (regular).

#### Derivation trace

Proto input: _\*xúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*xórną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _horn_

#### Reconstruction and comparative evidence

Kroonen and Orel cite lemma-style Proto-Germanic headwords of the _\*hurna-_ / _\*xurnan_ type for this noun [@Kroonen2013; @Orel2003, 234]. The form followed here, _\*xúrną_, is the nominative-style form used in the derivation here.

#### Old English evidence

Clark Hall, Bosworth-Toller, and Bright all record _horn_ as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898, 108; @BrightCassidyRingler1971]. The target is therefore the attested citation form.

#### Development to Old English

From _\*xúrną_, Northwest Germanic u-lowering gives _\*xórną_, and later loss of the final nasal leaves _horn_. The development treated here is fully regular.

#### Form note

The note's oblique _\*xurnăn_ belongs to comparative stem background only. It does not replace the derivational input _\*xúrną_ as the derivational form used here [@Kroonen2013; @Orel2003, 234].

### lead — OE _lǣdan_

\index[oe]{laedan@\emph{lǣdan}}
\index[pgmc]{laidijana@*láidijaną}

Derivation: _\*láidijaną_ > _lǣdan_ (regular).

#### Derivation trace

Proto input: _\*láidijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*lādijaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*lādijan} \\
OE Secondary Nasalization & \emph{*lādijąn} \\
Sievers Law Syncope & \emph{*lādjąn} \\
OE I Umlaut & \emph{*lǣdjąn} \\
OE Weak Tail Reduction & \emph{*lǣdjan} \\
OE J Loss After Heavy & \emph{*lǣdan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lǣdan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive Old English _lǣdan_ from Proto-Germanic _\*laidijaną_, and Kroonen likewise cites a weak verb of the _\*laidjan-_ type for 'lead' [@RingeTaylor2014; @Kroonen2013, 363].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lædan_ / _lǣdan_ as the ordinary Old English verb 'to lead, guide, conduct' [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*láidijaną_, monophthongization of _\*ai_ first gives a _\*lād-_ stage. Later syncope, i-mutation, weak-tail reduction, and loss of _j_ after a heavy stem yield _lǣdan_, so the development represented here is fully regular [@RingeTaylor2014].

### learn — OE _liornian_

\index[oe]{liornian@\emph{liornian}}
\index[pgmc]{liznojana@*líznōjaną}

Derivation: _\*líznōjaną_ > _liornian_ (regular).

#### Derivation trace

Proto input: _\*líznōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*líornōjan} \\
OE Secondary Nasalization & \emph{*líornōjąn} \\
OE I Umlaut & \emph{*líornējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*líornejąn} \\
OE Weak Tail Reduction & \emph{*líornejan} \\
OE Intervocalic J Vocalization & \emph{*líorneian} \\
OE Unstressed EI Contraction & \emph{*líornian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liornian_

#### Reconstruction and comparative evidence

Ringe and Taylor place the verb in a class-II weak family of the _\*liznō-_
type [@RingeTaylor2014], and Kroonen keeps the same comparative base for the
Germanic lexeme [@Kroonen2013]. The derivational input therefore requires no change
of stem class or paradigm cell.

The non-obvious issue is dialectal. Campbell records Northumbrian _liornian_
beside _leornian_, and he states that the _eo_ of _leornian_ is secondary,
while Northumbrian preserves forms with _io_, where original _eo_ and _io_
remain distinct [@Campbell1959, §123 n. 2].

#### Old English evidence

The form modeled here is _liornian_, the Northumbrian member of the Old
English family. Dictionary practice more often privileges _leornian_ as the
ordinary headword [@ClarkHall1960; @BrightCassidyRingler1971], but Campbell's
dialect evidence shows that _liornian_ is a genuine Old English form
[@Campbell1959, §123 n. 2].

This entry therefore remains compact. The point is to state clearly that the
Old English form here belongs to the Northumbrian side of the OE evidence rather than
to the leveled _leornian_ headword tradition.

#### Development to Old English

From _\*líznōjaną_, the expected Old English developments include rhotacism of
_z_, followed by breaking before _r_ plus consonant, and the ordinary reduction
of the weak verbal ending. The result is _liornian_, preserving the _io_
spelling that Campbell associates with Northumbrian where original _eo_ and
_io_ remain distinct [@Campbell1959, §123 n. 2].

_Leornian_ reflects the later _eo_ development that Campbell treats as
secondary [@Campbell1959, §123 n. 2; §296]. The selected Northumbrian target is
therefore the regular comparison form for the _i_-grade member of the family.

#### Form comparison

The comparison below sets the relevant forms side by side. It distinguishes the regular Northumbrian form
modeled here from the better-known West Saxon headword.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*líznōjaną_ > _liornian_ | computed regular output; attested Northumbrian comparison form | selected comparison |
| _leornian_ | attested later _eo_ form and dictionary headword | useful control, but not the target of this entry |

### lid — OE _hlid_

\index[oe]{hlid@\emph{hlid}}
\index[pgmc]{xlida@*xlídą}
\index[on]{hlitho@hliþó}

Derivation: _\*xlídą_ > _hlid_ (regular).

#### Derivation trace

Proto input: _\*xlídą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xlíd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hlid_

#### Reconstruction and comparative evidence

Orel cites a neuter lexeme of the _\*xliđ-_ type with Old English _hlid_, and Lloyd includes OE _hlid_ beside ON _hliþó_ and OHG _(h)lit_ among forms that retain _i_ [@Orel2003; @Lloyd1966].

#### Old English evidence

Clark Hall and Bosworth-Toller record _hlid_ as the noun 'lid, cover, door, gate' [@ClarkHall1960; @BosworthToller1898, 563].

#### Development to Old English

The derivational input already represents the later Germanic _hliđ-_ stage used for the derivation here. From _\*xlídą_, heavy-syllable apocope yields _hlid_, and the form belongs to the retained-_i_ set noted by Lloyd rather than to the lowered _e_ type [@Lloyd1966].

#### Form note

An earlier etymological stage _\*liþuz_ belongs to comparative background only. The form represented here is the later _\*xlídą_ > _hlid_ line that matches the attested Old English noun [@Orel2003; @Lloyd1966].

### light — OE _līehtan_

\index[oe]{liehtan@\emph{līehtan}}
\index[pgmc]{leuxtijana@*léuxtijaną}

Derivation: _\*léuxtijaną_ > _līehtan_ (regular).

#### Derivation trace

Proto input: _\*léuxtijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*lēoxtijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēoxtijan} \\
OE Secondary Nasalization & \emph{*lēoxtijąn} \\
Sievers Law Syncope & \emph{*lēoxtjąn} \\
OE I Umlaut & \emph{*līextjąn} \\
OE Weak Tail Reduction & \emph{*līextjan} \\
OE J Loss After Heavy & \emph{*līextan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _līehtan_

#### Reconstruction and comparative evidence

Fulk gives Proto-Germanic _\*liuxtijanan_ with Old English _līehtan_ 'illuminate', and Ringe and Taylor likewise derive West Saxon _liehtan_ from the same weak-verb formation [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller preserve the verb family under spellings such as _liehtan_, _lihtan_, and _līhtan_, distinct from the related noun _lēoht_ and adjective _leoht_/_liht_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*léuxtijaną_, the regular verbal line preserves _\*xt_, passes through a West Saxon _liehtan_ stage, and is represented here by normalized _līehtan_. The word treated in this entry is therefore the verb 'to light, illuminate', not the related noun from _\*leuxtą_ [@Fulk2018; @RingeTaylor2014].

#### Dialect note

Ringe and Taylor and Campbell distinguish West Saxon _liehtan_ from Anglian _lihtan_, while later West Saxon also shows _lyhtan_ [@RingeTaylor2014; @Campbell1959].

### linden — OE _lind_

\index[oe]{lind@\emph{lind}}
\index[pgmc]{lindo@*líndō}

Derivation: _\*líndō_ > _lind_ (regular).

#### Derivation trace

Proto input: _\*líndō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*líndu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*línd} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lind_

#### Reconstruction and comparative evidence

Kroonen cites _\*lindō-_ 'lime tree' and gives Old English _lind_ as the relevant reflex [@Kroonen2013].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lind_ as the noun 'lime-tree, linden' [@ClarkHall1960; @BosworthToller1898, 630].

#### Development to Old English

From _\*líndō_, Northwest Germanic final _\*ō_ raising first gives a _\*líndu_ stage, and later high-vowel apocope yields _lind_. The development is therefore straightforward and regular.

#### Form note

The Old English noun represented here is _lind_. Clark Hall also has a separate adjectival _linden_ 'made of linden-wood', but that is not the noun counterpart for this entry [@ClarkHall1960].

### milk — OE _meoloc_

\index[oe]{meoloc@\emph{meoloc}}
\index[pgmc]{melukz@*mélukz}

Derivation: _\*mélukz_ > _meoloc_ (regular).

#### Derivation trace

Proto input: _\*mélukz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*méluk} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*mélok} \\
OE Back Mutation & \emph{*méolok} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _meoloc_

#### Reconstruction and comparative evidence

Kroonen and Orel reconstruct the noun as _\*meluk-_ / _\*melukz_, and the nominative-style input used here is _\*mélukz_ [@Kroonen2013; @Orel2003, 306].

#### Old English evidence

Old English preserves a mixed dossier for this noun. Ringe and Taylor describe West Saxon _meolc_ < _meoluc_ < _\*meluk_, Campbell likewise discusses _meoluc_ and _meoloc_, and Anglian shows _milc_ [@RingeTaylor2014; @Campbell1959].

#### Development to Old English

The unsyncopated line from _\*mélukz_ loses final _\*z_, lowers unstressed _u_ to _o_, and with back mutation yields _meoloc_. That fuller unsyncopated outcome is the form represented here [@RingeTaylor2014].

#### Form comparison

Syncopated _meolc_ and Anglian _milc_ belong to the competing leveled tradition associated with oblique forms, whereas _meoloc_ / _meoluc_ preserves the fuller nominal shape [@Campbell1959; @RingeTaylor2014].

### mother — OE _mōder_

\index[oe]{moder@\emph{mōder}}
\index[pgmc]{moder@*mōdēr}

Derivation: _\*mōdēr_ > _mōder_ (regular).

#### Derivation trace

Proto input: _\*mōdēr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*mōdǣr} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*mōdær} \\
OE Unstressed AE Merger & \emph{*mōder} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mōder_

#### Reconstruction and comparative evidence

Kroonen and Orel cite the Proto-Germanic r-stem kinship noun as _\*mōder-_ / _\*mōdēr_ [@Kroonen2013; @Orel2003].

#### Old English evidence

The transmitted Old English headword tradition is _mōdor_ / _modor_, with oblique _mēder_ in the paradigm. Clark Hall, Campbell, and Ringe and Taylor all preserve that contrast [@ClarkHall1960; @Campbell1959; @RingeTaylor2014].

#### Development to Old English

From _\*mōdēr_, the regular suffixal development yields _mōder_. That regular nominative reflex is the form represented here, while the more familiar citation form _mōdor_ reflects later levelling within the r-stem paradigm [@Campbell1959; @RingeTaylor2014].

#### Form comparison

The note therefore concerns inherited vocalism rather than a different lexeme: _mōder_ is the regularized nominative represented here, but dictionaries usually print _mōdor_ / _modor_, and the oblique evidence survives in _mēder_ [@ClarkHall1960; @RingeTaylor2014].

### net — OE _nett_

\index[oe]{nett@\emph{nett}}
\index[pgmc]{natja@*nátją}

Derivation: _\*nátją_ > _nett_ (regular).

#### Derivation trace

Proto input: _\*nátją_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*náttją} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*nættją} \\
OE Heavy Syllable Nasal Apocope & \emph{*nættj} \\
OE I Umlaut & \emph{*nettj} \\
OE J Loss After Heavy & \emph{*nett} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nett_

#### Reconstruction and comparative evidence

Orel gives _\*natjan_ with Old English _nett_, and Fulk's account of West Germanic gemination before _j_ explains the geminate outcome after a short vowel [@Orel2003; @Fulk2018].

#### Old English evidence

Clark Hall and Bosworth-Toller record _nett_ as the noun, and Campbell notes that final geminates are often graphically simplified in Old English spelling [@ClarkHall1960; @BosworthToller1898, 29; @Campbell1959].

#### Development to Old English

From _\*nátją_, West Germanic j-gemination first gives _\*náttją_. Later brightening, loss of the weak ending, and loss of final _j_ after a heavy stem yield _nett_, so the development represented here is regular [@Fulk2018].

#### Form note

Spellings in _net_ can therefore be graphic simplifications, but the lexical target supported by the dictionary evidence is _nett_ [@Campbell1959; @Orel2003].

### nightmare — OE _mare_

\index[oe]{mare@\emph{mare}}
\index[pgmc]{maron@*márōn}

Derivation: _\*márōn_ > _mare_ (regular).

#### Derivation trace

Proto input: _\*márōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*márǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mærǭ} \\
OE A Restoration & \emph{*marǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*maræ} \\
OE Unstressed AE Merger & \emph{*mare} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mare_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the lexeme as Proto-Germanic / Proto-Northwest-Germanic _\*marōn-_, with Old English _mare, maran_, and variant _mere_; Orel preserves the same comparative lemma though with a different Old English headword tradition [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _mare_ 'nightmare, monster' and also preserves related variant forms _mera_ / _mere_ [@ClarkHall1960, 213].

#### Development to Old English

The selected simplex input _\*márōn_ regularly gives _mare_ after brightening, A-restoration before the n-stem ending, and later reduction of the final vowel. The word represented here is the attested simplex noun, not an attested compound [@RingeTaylor2014].

#### Form note

The concept corresponds to an unattested compound _\*nihtmare_, but the Old English lexical evidence is for simplex _mare_, with oblique _maran_ and variant _mere_ / _mera_ [@RingeTaylor2014; @ClarkHall1960, 213].

### coat — OE _rocc_

\index[oe]{rocc@\emph{rocc}}
\index[pgmc]{rukkaz@*rúkkaz}

Derivation: _\*rúkkaz_ > _rocc_ (regular).

#### Derivation trace

Proto input: _\*rúkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*rókkaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*rókka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*rókk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _rocc_

#### Reconstruction and comparative evidence

Orel cites a masculine _\*rukkaz_ for the garment word, while Kroonen gives _\*hrukka-_. Both treat this as the garment lexeme and not as the separate stone word [@Orel2003; @Kroonen2013, 290].

#### Old English evidence

Clark Hall and Bosworth-Toller record _rocc_ as an over-garment or tunic and preserve compounds such as _bisceoprocc_ and _breóstrocc_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

With _\*rúkkaz_ as the derivational input, Northwest Germanic u-lowering and later loss of final _-a_ yield _rocc_ as a regular outcome.

#### Source note

This entry concerns the garment noun only. The stone word seen in _stānrocc_ belongs to a different lexical history [@ClarkHall1960; @BosworthToller1898].

### sheep — OE _sċēap_

\index[oe]{sceap@\emph{sċēap}}
\index[pgmc]{skepa@*skḗpą}

Derivation: _\*skḗpą_ > _sċēap_ (regular).

#### Derivation trace

Proto input: _\*skḗpą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*skǣpą} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*skǣp} \\
OE Sk Palatalization & \emph{*ʃǣp} \\
OE Ws Palatal Diphthongization & \emph{*ʃēap} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēap_

#### Reconstruction and comparative evidence

Ringe and Taylor cite a later West Germanic _\*skap_ > WS _scéap_, while Orel preserves a Proto-Germanic noun of the _\*skēp-_ type for the same lexeme [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _scēap_ with spelling variation, and Campbell likewise lists West Saxon _scéap_ among the palatal-diphthongized forms [@ClarkHall1960; @Campbell1959].

#### Development to Old English

From _\*skḗpą_, Northwest Germanic lowering gives _\*skǣpą_; after apocope and palatalization the West Saxon branch diphthongizes to _sċēap_. The development represented here is therefore fully regular.

#### Dialect note

Ringe and Taylor contrast West Saxon _scéap_ with Mercian and Kentish _scép_, and Campbell also notes Northumbrian _scip_. The form represented here is the West Saxon headword [@RingeTaylor2014; @Campbell1959].

### shilling — OE _sċilling_

\index[oe]{scilling@\emph{sċilling}}
\index[pgmc]{skillingaz@*skíllingaz}

Derivation: _\*skíllingaz_ > _sċilling_ (regular).

#### Derivation trace

Proto input: _\*skíllingaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*skíllinga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*skílling} \\
OE Sk Palatalization & \emph{*ʃílling} \\
OE Med Unstressed I Lowering1 & \emph{*ʃílleng} \\
OE Med Unstressed I Lowering & \emph{*ʃílling} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċilling_

#### Reconstruction and comparative evidence

Kroonen treats the cognate set under _\*skellinga-_ ~ _\*skillinga-_ and connects it with _\*skeld-linga-_, while Orel likewise gives the coin word with OE _scilling_ among the reflexes [@Kroonen2013; @Orel2003]. The form followed here, _\*skíllingaz_, is the nominative-style form used here to represent that inherited _\*-ing-_ derivative.

#### Old English evidence

Clark Hall records _scilling_, and Campbell cites it among nouns with unstressed _i_ in derivational _-ing_ [@ClarkHall1960; @Campbell1959]. The target is the ordinary OE citation form, normalized as _sċilling_.

#### Development to Old English

From _\*skíllingaz_, loss of final _-az_ yields _\*skílling_. Old English palatalization of initial _sk_ before front vocalism then gives _sċilling_. The _i_ of derivational _-ing-_ remains, so the regular outcome is _sċilling_, not _\*sċilleng_ [@Campbell1959; @Hogg1992].

#### Form note

Kroonen's _\*skellinga-_ ~ _\*skillinga-_ and his internal analysis _\*skeld-linga-_ belong to the etymological background of the cognate set. The form followed here, _\*skíllingaz_, is the specific form used for the derivation represented here [@Kroonen2013].

### show — OE _sċēawian_

\index[oe]{sceawian@\emph{sċēawian}}
\index[pgmc]{skawojana@*skáwōjaną}

Derivation: _\*skáwōjaną_ > _sċēawian_ (regular).

#### Derivation trace

Proto input: _\*skáwōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*skḗawōjan} \\
OE Secondary Nasalization & \emph{*skḗawōjąn} \\
OE Sk Palatalization & \emph{*ʃḗawōjąn} \\
OE I Umlaut & \emph{*ʃḗawējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawejąn} \\
OE Weak Tail Reduction & \emph{*ʃḗawejan} \\
OE Intervocalic J Vocalization & \emph{*ʃḗaweian} \\
OE Unstressed EI Contraction & \emph{*ʃḗawian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawian_

#### Reconstruction and comparative evidence

Orel and Kroonen cite a Class II verb of the type [_\*skawōjan-_]{.iv lang=pgmc sort=skawojan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3088"}, with OE [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3088"} among the reflexes [@Orel2003; @Kroonen2013, 482]. Brunner likewise records the Old English family as [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3088"}, [_scāwian_]{.iv lang=oe sort=scawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3088"}, confirming that it belongs to the ordinary show-verb set rather than to a special finite-cell formation [@SieversBrunner1965].

#### Old English evidence

Bright lists [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3092"} (W. II.) and also the related form [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3092"} [@BrightCassidyRingler1971]. The sources therefore use [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3092"}, while [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3092"} supplies a normalized spelling.

#### Development to Old English

From [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3096"}, Old English _aw_ before a following vowel yields _ēaw_, and _\*ō_ survives between _\*w_ and _\*j_ in the Class II suffix. The development therefore runs regularly to [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3096"}, without the direct _\*aw+j_ problem seen in other verb types [@Campbell1959; @Orel2003].

#### Form note

The difference between [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3100"} and [_sċēawian_]{.iv lang=oe sort=sceawian role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:3100"} is orthographic normalization of initial <_sc_>, not a difference of lexeme or paradigm cell [@Campbell1959; @Hogg1992].

### sleep — OE _slǣpan_

\index[oe]{slaepan@\emph{slǣpan}}
\index[pgmc]{slepana@*slḗpaną}

Derivation: _\*slḗpaną_ > _slǣpan_ (regular).

#### Derivation trace

Proto input: _\*slḗpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*slǣpaną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*slǣpan} \\
OE Secondary Nasalization & \emph{*slǣpąn} \\
OE Weak Tail Reduction & \emph{*slǣpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _slǣpan_

#### Reconstruction and comparative evidence

Kroonen preserves the comparative verb as _\*slēpan-_, and Fulk cites the same family under root _\*slēb-_ [@Kroonen2013; @Fulk2018, 120]. The form followed here, _\*slḗpaną_, is the infinitive-style form used here for that inherited sleep-verb.

#### Old English evidence

Clark Hall gives _slæpan_ with preterite _slēp_, _slēap_, and Bright likewise lists _slæpan_ _(slāpan)_, _slēp_ _slēpon_ _slēpen_ [@ClarkHall1960; @BrightCassidyRingler1971, 435]. The target represented here is therefore the normalized infinitive _slǣpan_, not the preterite forms and not the separate noun _slǣp_.

#### Development to Old English

From _\*slḗpaną_, Northwest Germanic lowering gives _\*slǣpaną_. The later OE tail developments then yield _slǣpan_ regularly. Brunner and Bülbring show that the OE tradition also has variant spellings such as West Saxon _slāpan_/_slæpan_ and Anglian or Kentish _slēpan_, but those do not displace the infinitive chosen here [@SieversBrunner1965; @Bulbring1902].

#### Form note

The note concerns lemma type rather than a special derivational problem: this row represents the verb _slǣpan_, whereas _slǣp_ belongs to noun or lookup background and _slēp_/_slēap_ are preterite forms [@ClarkHall1960; @BrightCassidyRingler1971, 435].

### smear — OE _smierwan_

\index[oe]{smierwan@\emph{smierwan}}
\index[pgmc]{smerwijana@*smérwijaną}

Derivation: _\*smérwijaną_ > _smierwan_ (regular).

#### Derivation trace

Proto input: _\*smérwijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*sméorwijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sméorwijan} \\
OE Secondary Nasalization & \emph{*sméorwijąn} \\
Sievers Law Syncope & \emph{*sméorwjąn} \\
OE I Umlaut & \emph{*smíerwjąn} \\
OE Weak Tail Reduction & \emph{*smíerwjan} \\
OE J Loss After Heavy & \emph{*smíerwan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _smierwan_

#### Reconstruction and comparative evidence

Kroonen gives the comparative headword as _\*smerwjan-_ [@Kroonen2013]. Ringe and Taylor instead cite a later-stage _\*smirwijana_, from which they derive West Saxon _smierwan_, Mercian _smirwan_, and Northumbrian _smiriga_ [@RingeTaylor2014]. The form followed here, _\*smérwijaną_, therefore represents the Kroonen-aligned PGmc layer, while the later-stage dialect split belongs to a different chronological level.

#### Old English evidence

The target represented here is the West Saxon citation form _smierwan_. Campbell's Anglian discussion explains the contrasting _smirwan_, and Clark Hall, Brunner, and Bright show that the same lexical family later also includes forms such as _smirian_, _smyrian_, and preterite _smyrode_ [@Campbell1959; @ClarkHall1960; @SieversBrunner1965; @BrightCassidyRingler1971].

#### Development to Old English

From _\*smérwijaną_, breaking before _r + consonant_ yields _eo_, and later i-umlaut produces _ie_. The result is West Saxon _smierwan_. Anglian _smirwan_ reflects the well-known failure of breaking in this environment, not a different lexeme [@Campbell1959; @RingeTaylor2014].

#### Dialect note

The entry therefore represents the West Saxon member of a broader OE family: _smierwan_ in West Saxon, _smirwan_ in Anglian or Mercian, and related later class-II forms such as _smirian_ or _smyrian_ in the same lexical field [@RingeTaylor2014; @ClarkHall1960].

### span — OE _spannan_

\index[oe]{spannan@\emph{spannan}}
\index[pgmc]{spannana@*spánnaną}

Derivation: _\*spánnaną_ > _spannan_ (regular).

#### Derivation trace

Proto input: _\*spánnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*spánnan} \\
OE Secondary Nasalization & \emph{*spánnąn} \\
OE Weak Tail Reduction & \emph{*spánnan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spannan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited verb as _\*spannan-_, with OE _spannan_ among the reflexes [@Kroonen2013]. The form followed here, _\*spánnaną_, is the infinitive-style form used here for that same verbal lexeme.

#### Old English evidence

Clark Hall lists noun _spann_ and verb _spannan_ as separate headwords, and Brunner likewise records _sponnan, spannan stv._ [@ClarkHall1960; @SieversBrunner1965]. The target is the strong-verb infinitive, not the noun.

#### Development to Old English

From _\*spánnaną_, the final nasal ending is lost and the regular OE weak-tail steps surface _spannan_. No paradigm-cell substitution is needed: the current derivation already lands on the infinitive directly.

#### Form note

English _span_ can also reach the noun _spann_ in local lookup material. The form represented here is the verb _spannan_, with the noun treated elsewhere [@ClarkHall1960].

### spar — OE _spearra_

\index[oe]{spearra@\emph{spearra}}
\index[pgmc]{sparro@*spárrô}

Derivation: _\*spárrô_ > _spearra_ (regular).

#### Derivation trace

Proto input: _\*spárrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*spærrô} \\
OE Breaking & \emph{*spearrô} \\
OE Unstressed Long Vowel Shortening & \emph{*spearra} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spearra_

#### Reconstruction and comparative evidence

Kroonen and Orel place this noun in the beam or rafter set _\*spar(r)an-_, with cognates such as Old Saxon and Old High German _sparro_ [@Kroonen2013; @Orel2003]. The form followed here, _\*spárrô_, is the OE-facing nominal form used here for that same lexeme.

#### Old English evidence

The noun is _spearra_. English gloss overlap also reaches the unrelated verb _sperran_ 'to bar', which does not belong to this row.

#### Development to Old English

From _\*spárrô_, Anglo-Frisian brightening gives _\*spærrô_, and OE breaking before geminate _rr_ yields _\*spearrô_, later _spearra_. The development is therefore regular for a breaking-conditioned noun of this type [@Luick1914].

#### Form note

This entry concerns the noun _spearra_ only. It should be kept separate from verb _sperran_, even though the Modern English glosses overlap [@Kroonen2013; @Orel2003].

### still — OE _stillan_

\index[oe]{stillan@\emph{stillan}}
\index[pgmc]{stellijana@*stéllijaną}

Derivation: _\*stéllijaną_ > _stillan_ (regular).

#### Derivation trace

Proto input: _\*stéllijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*stéllijan} \\
OE Secondary Nasalization & \emph{*stéllijąn} \\
Sievers Law Syncope & \emph{*stélljąn} \\
OE I Umlaut & \emph{*stilljąn} \\
OE Weak Tail Reduction & \emph{*stilljan} \\
OE J Loss After Heavy & \emph{*stillan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stillan_

#### Reconstruction and comparative evidence

The wider West Germanic family includes adjective _still_ and verb _stillen_ [@KlugeSeebold2011]. The form followed here, _\*stéllijaną_, represents the verbal j-formation used for the OE row.

#### Old English evidence

Clark Hall gives _stillan_ as the verb and separately _stille_ as the adjective [@ClarkHall1960]. Bosworth-Toller likewise preserves a substantial prefixed verbal family under _ge-stillan_ and related forms [@BosworthToller1898, 724]. The Old English form here is the verb _stillan_, not the adjective.

#### Development to Old English

As a heavy-stem Class I weak verb, _\*stéllijaną_ undergoes the expected syncope and i-umlaut, and later loss of _j_ after a heavy stem yields _stillan_. The development represented here is regular.

#### Form note

The note concerns lexical framing rather than sound law: _stillan_ is the verb represented here, while _stille_ belongs to the related adjectival branch of the family [@ClarkHall1960; @KlugeSeebold2011].

### summer — OE _sumer_

\index[oe]{sumer@\emph{sumer}}
\index[pgmc]{sumaraz@*súmaraz}

Derivation: _\*súmaraz_ > _sumer_ (regular).

#### Derivation trace

Proto input: _\*súmaraz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*súmara} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*súmar} \\
Anglo Frisian Brightening & \emph{*súmær} \\
OE Unstressed AE Merger & \emph{*súmer} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sumer_

#### Reconstruction and comparative evidence

Kroonen gives the lexeme as _\*sumara-_, and Ringe and Taylor likewise use _\*sumaraz_, while Orel preserves an alternate _\*sumeraz_ [@Kroonen2013; @RingeTaylor2014; @Orel2003, 425]. The form followed here, _\*súmaraz_, follows the _\*a_ vocalism that underlies the regular development represented here.

#### Old English evidence

Clark Hall gives _sumor m., gs. sumeres, ds. sumera, sumere_, and Bright likewise lists _sumor (sumer)_ with genitive _sumeres_ [@ClarkHall1960; @BrightCassidyRingler1971, 440]. The tradition therefore preserves both _sumor_ and _sumer_, with the oblique forms strongly supporting second-syllable _e_.

#### Development to Old English

From _\*súmaraz_, loss of final _-az_ is followed by fronting and merger in the unstressed second syllable, yielding _sumer_. The form compared here is the regularized _e_-form, while the common citation form _sumor_ remains part of the attested OE tradition [@RingeTaylor2014].

#### Form note

The entry does not deny _sumor_. It represents _sumer_ as the regular outcome chosen here, while _sumor_ remains a common headword spelling and _sumeres_/_sumere_ show that the _e_-vocalism was also real in Old English [@ClarkHall1960; @BrightCassidyRingler1971, 440].

### sunder — OE _sundrian_

\index[oe]{sundrian@\emph{sundrian}}
\index[pgmc]{sundrojana@*súndrōjaną}

Derivation: _\*súndrōjaną_ > _sundrian_ (regular).

#### Derivation trace

Proto input: _\*súndrōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*súndrōjan} \\
OE Secondary Nasalization & \emph{*súndrōjąn} \\
OE I Umlaut & \emph{*súndrējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*súndrejąn} \\
OE Weak Tail Reduction & \emph{*súndrejan} \\
OE Intervocalic J Vocalization & \emph{*súndreian} \\
OE Unstressed EI Contraction & \emph{*súndrian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sundrian_

#### Reconstruction and comparative evidence

Orel distinguishes three related formations: adverbial _\*sunþraz_ > _sundor_, Class I verbal _\*sunþrjanan_ > _syndrian_, and Class II verbal _\*sunþrōjanan_ > _sundrian_ [@Orel2003]. Kluge-Seebold aligns the cognate set with German _sondern_ and OE _gesundrian_, so this entry belongs with the Class II verb, not the adverb [@KlugeSeebold2011].

#### Old English evidence

Clark Hall and Bosworth-Toller list _sundrian_ and _syndrian_ separately from adverbial _sundor_; both also record the prefixed verbal family _ā-sundrian_ [@ClarkHall1960, 296; @BosworthToller1898]. The target is therefore the weak verb _sundrian_.

#### Development to Old English

From _\*súndrōjaną_, the Class II weak-verb suffix yields regular OE _-ian_, producing _sundrian_. Because this is the _\*-ōjan-_ verb and not the Class I _\*-jan-_ formation, the form represented here does not belong to the umlauted _syndrian_ branch.

#### Form note

The earlier confusion was lexical, not phonological: _sundor_ is the separate adverb, and _syndrian_ is a related but different verb. The verb treated here is the Class II verb _sundrian_ [@Orel2003; @ClarkHall1960, 296].

### swallow — OE _swealwe_

\index[oe]{swealwe@\emph{swealwe}}
\index[pgmc]{swalwon@*swálwōn}

Derivation: _\*swálwōn_ > _swealwe_ (regular).

#### Derivation trace

Proto input: _\*swálwōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*swálwǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*swælwǭ} \\
OE Breaking & \emph{*swealwǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*swealwæ} \\
OE Unstressed AE Merger & \emph{*swealwe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swealwe_

#### Reconstruction and comparative evidence

Kroonen gives the bird name as _\*swalwōn-_, and Ringe and Taylor cite the later West Germanic stage _\*swalwa_, from which West Saxon _swealwe_ and Mercian _swalwe_ develop [@Kroonen2013, 535; @RingeTaylor2014, 200]. The selected etymological comparison belongs to the swallow-bird family, not to the verb _swelgan_.

#### Old English evidence

Clark Hall records _swealwe (a, o)_ as the noun headword [@ClarkHall1960]. Campbell and Brunner also preserve later or oblique-family forms such as _swaluwe_, _swalewan_, and _swealuwe_, but those belong to wider variation around the noun rather than to the citation form represented here [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

From _\*swálwōn_, brightening yields _\*swælw-_, and breaking before _lw_ gives _\*swealw-_. The later noun ending develops regularly to _swealwe_. The relevant point is that the bird name has no inherited _\*g_: that consonant belongs to the separate verb _swelgan_ [@RingeTaylor2014, 200; @Kroonen2013, 535].

### swine — OE _swīn_

\index[oe]{swin@\emph{swīn}}
\index[pgmc]{swina@*swī́ną}
\index[pgmc]{swina@*swḯną}

Derivation: citation reconstruction _\*swī́ną_; form followed here _\*swī́ną_ > _swīn_ (regular).

#### Derivation trace

Proto input: _\*swī́ną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*swī́n} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swīn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*swina-_ 'pig' [@Kroonen2013]. The selected comparative form here is the bare neuter citation cell _\*swī́ną_, which matches the singular noun aimed at in Old English rather than an oblique stem form.

#### Old English evidence

Clark Hall records _swin (y)_ as the ordinary noun headword [@ClarkHall1960]. The target here is that singular citation form _swīn_, not a plural glossed in Modern English as *swine*.

#### Development to Old English

From _\*swī́ną_, loss of the final nasal vowel yields _swīn_. The outcome is therefore the regular monosyllabic noun with preserved long root _ī_.

#### Source note

The derivational input writes stressed long _ī_ as _\*ī́_, so comparative _\*swī́ną_ and derivational _\*swī́ną_ represent the same lexical form.

### think — OE _þenċan_

\index[oe]{thencan@\emph{þenċan}}
\index[pgmc]{thankijana@*θánkijaną}

Derivation: _\*θánkijaną_ > _þenċan_ (regular).

#### Derivation trace

Proto input: _\*θánkijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*θánkijan} \\
OE Secondary Nasalization & \emph{*θánkijąn} \\
Sievers Law Syncope & \emph{*θánkjąn} \\
OE Velar Palatalization & \emph{*θánʧjąn} \\
OE I Umlaut & \emph{*θenʧjąn} \\
OE Weak Tail Reduction & \emph{*θenʧjan} \\
OE J Loss After Heavy & \emph{*θenʧan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þenċan_

#### Reconstruction and comparative evidence

Kroonen gives the verb as _\*þankjan-_ 'to think', and Ringe and Taylor cite fully inflected _\*þankijaną_ beside OE _þenċan_ [@Kroonen2013; @RingeTaylor2014]. The noun _\*þankaz_ belongs only to the wider derivational background.

#### Old English evidence

Bosworth-Toller preserves the verb under _þencan_/_geþencan_, and the citation form here is the ordinary infinitive _þenċan_ [@BosworthToller1898].

#### Development to Old English

From _\*θánkijaną_, palatalization before _\*j_ and i-umlaut produce _þenċan_. The infinitive is therefore a straightforward weak-verb outcome.

#### Lexical note

Campbell's assibilation discussion uses the same verb _þencan_; the class-III relic _hycgan_ is a different lexeme [@Campbell1959; @Hogg1992].

### thorn — OE _þorn_

\index[oe]{thorn@\emph{þorn}}
\index[pgmc]{thurnaz@*θúrnaz}

Derivation: _\*θúrnaz_ > _þorn_ (regular).

#### Derivation trace

Proto input: _\*θúrnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*θórnaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*θórna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*θórn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þorn_

#### Reconstruction and comparative evidence

Kroonen gives _\*þurna-_ 'thorn, briar', while Orel preserves the masculine pair _\*þurnuz_ ~ _\*þurnaz_ [@Kroonen2013; @Orel2003]. The form followed here, _\*θúrnaz_, belongs to that same comparative family.

#### Old English evidence

Bright lists _þorn_, m., and Clark Hall likewise treats _þorn_ as the ordinary noun headword [@BrightCassidyRingler1971; @ClarkHall1960].

#### Development to Old English

The inherited stem shows regular lowering of _u_ to _o_ before _r_, and final loss yields _þorn_. The noun is therefore a regular Old English continuation of the Proto-Germanic thorn-family.

#### Source note

The comparative sources preserve more than one stem formation, but the Old English target itself is simply the citation form _þorn_.

### tide — OE _tīd_

\index[oe]{tid@\emph{tīd}}
\index[pgmc]{tidiz@*tī́diz}
\index[pgmc]{tidiz@*tḯdiz}

Derivation: citation reconstruction _\*tī́diz_; form followed here _\*tī́diz_ > _tīd_ (regular).

#### Derivation trace

Proto input: _\*tī́diz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*tī́di} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*tī́d} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tīd_

#### Reconstruction and comparative evidence

Kroonen gives _\*tīdi-_ 'time', and Orel's _\*tīđiz_ points to the same feminine noun [@Kroonen2013; @Orel2003]. The related verb _tīdan_ is separate.

#### Old English evidence

Bright records _tīd_ with singular _tīde_ and plural _tīda_, and Clark Hall treats _tīd_ as the ordinary noun 'time, period, season' [@BrightCassidyRingler1971; @ClarkHall1960, 309].

#### Development to Old English

From _\*tī́diz_, final _z_ is lost and the high final vowel drops, leaving _tīd_. The development is straightforward for a feminine i-stem.

#### Lexical note

English *tide* can also lead to the separate weak verb _tīdan_; the noun is _tīd_.

### token — OE _tācn_

\index[oe]{tacn@\emph{tācn}}
\index[pgmc]{taikna@*táikną}

Derivation: _\*táikną_ > _tācn_ (regular).

#### Derivation trace

Proto input: _\*táikną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*tākną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tākn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tācn_

#### Reconstruction and comparative evidence

Kroonen cites _\*taikna-_ and Orel _\*taiknan_ for the noun 'sign, token' [@Kroonen2013; @Orel2003, 438]. The form followed here, _\*táikną_, is the simple citation-form noun used for the derivation.

#### Old English evidence

Campbell and Sievers-Brunner preserve both unbroken _tācn_ and broken _tācen_, with oblique _tācnes_ remaining unbroken [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

Monophthongization of _ai_ yields _ā_, and loss of the final nasal vowel leaves _tācn_. The unbroken form is therefore a regular Old English outcome.

#### Form note

_tācn_ is the attested unbroken citation form selected here. Later West Saxon prose often prefers _tācen_, but that does not displace the older unbroken form [@Campbell1959; @SieversBrunner1965].

### town — OE _tūn_

\index[oe]{tun@\emph{tūn}}
\index[pgmc]{tuna@*tūną}

Derivation: _\*tūną_ > _tūn_ (regular).

#### Derivation trace

Proto input: _\*tūną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tūn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tūn_

#### Reconstruction and comparative evidence

Kroonen cites _\*tūna-_ 'fenced area', while Orel gives _\*tūnan_ ~ _\*tūnaz_ [@Kroonen2013; @Orel2003, 452]. The form followed here, _\*tūną_, is the simple citation-form noun used in the derivation.

#### Old English evidence

Clark Hall records _tūn_ as the ordinary headword 'enclosure, yard, village, town' [@ClarkHall1960].

#### Development to Old English

The inherited long _ū_ is preserved, and loss of the final nasal vowel yields _tūn_ regularly [@SieversBrunner1965].

#### Source note

The comparative headwords vary, but the Old English target here is the direct citation form _tūn_, not an oblique _\*tūnăn_.

### wade — OE _wadan_

\index[oe]{wadan@\emph{wadan}}
\index[pgmc]{wadana@*wádaną}

Derivation: _\*wádaną_ > _wadan_ (regular).

#### Derivation trace

Proto input: _\*wádaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wædaną} \\
OE A Restoration & \emph{*wadaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wadan} \\
OE Secondary Nasalization & \emph{*wadąn} \\
OE Weak Tail Reduction & \emph{*wadan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wadan_

#### Reconstruction and comparative evidence

Campbell and Ringe and Taylor describe A-restoration before a following back vowel, and Luick explicitly includes _wadan_ among the standard open-syllable examples [@Campbell1959; @RingeTaylor2014; @Luick1914, 239].

#### Old English evidence

Clark Hall gives _wadan_ as the verb 'to go, move, stride, advance', and Bright lists the same infinitive in the strong-verb paradigm [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wádaną_, Anglo-Frisian brightening first gives _\*wædaną_. A-restoration before the back-vocalic infinitive ending then returns _a_, and later reduction yields _wadan_ [@Campbell1959; @RingeTaylor2014].

#### Development note

The infinitive belongs to the A-restoration class. The citation form is therefore _wadan_, not a fronted _wæden_-type output.

### warp — OE _weorpan_

\index[oe]{weorpan@\emph{weorpan}}
\index[pgmc]{werpana@*wérpaną}

Derivation: _\*wérpaną_ > _weorpan_ (regular).

#### Derivation trace

Proto input: _\*wérpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*wéorpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wéorpan} \\
OE Secondary Nasalization & \emph{*wéorpąn} \\
OE Weak Tail Reduction & \emph{*wéorpan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weorpan_

#### Reconstruction and comparative evidence

Ringe and Taylor distinguish preterite _\*warp_ from infinitive _\*werpana_, and the derivational input here is the verbal form _\*wérpaną_ [@RingeTaylor2014].

#### Old English evidence

Clark Hall records _weorpan_ as the strong verb headword and separately lists _wearp_ as both noun and preterite. Bright gives the paradigm _weorpan, wearp, wurpon, worpen_ [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

Breaking before _r + C_ yields _weor-_, and the infinitive develops regularly to _weorpan_ [@Campbell1959; @Hogg1992].

#### Lexical note

English *warp* also points to related _wearp_ material. The target is the infinitive _weorpan_.

### wash — OE _wascan_

\index[oe]{wascan@\emph{wascan}}
\index[pgmc]{waskana@*wáskaną}

Derivation: _\*wáskaną_ > _wascan_ (regular).

#### Derivation trace

Proto input: _\*wáskaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wæskaną} \\
OE A Restoration & \emph{*waskaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*waskan} \\
OE Secondary Nasalization & \emph{*waskąn} \\
OE Weak Tail Reduction & \emph{*waskan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wascan_

#### Reconstruction and comparative evidence

Kroonen cites _\*waskan-_, Orel _\*waskanan_, and Ringe and Taylor likewise derive Old English _wascan_ from the same verb family [@Kroonen2013; @Orel2003, 489; @RingeTaylor2014, 142].

#### Old English evidence

Clark Hall heads the verb as _wascan_, while Sievers-Brunner also notes the variant _wæscan_ [@ClarkHall1960; @SieversBrunner1965].

#### Development to Old English

From _\*wáskaną_, brightening gives _\*wæskaną_. A-restoration before the _sC_ cluster restores _a_, and medial _sc_ remains unpalatalized before the following back vowel, yielding _wascan_ [@Campbell1959; @RingeTaylor2014, 142].

#### Form note

The conservative citation form _wascan_ is selected here. Spellings such as _wæscan_ or _wasċan_ belong to variant or normalized background rather than to the target of this entry.

### wax — OE _weaxan_

\index[oe]{weaxan@\emph{weaxan}}
\index[pgmc]{waxsana@*wáxsaną}

Derivation: _\*wáxsaną_ > _weaxan_ (regular).

#### Derivation trace

Proto input: _\*wáxsaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wæxsaną} \\
OE Breaking & \emph{*weaxsaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*weaxsan} \\
OE Secondary Nasalization & \emph{*weaxsąn} \\
OE Weak Tail Reduction & \emph{*weaxsan} \\
OE Xs Merge & \emph{*weaXSan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weaxan_

#### Reconstruction and comparative evidence

Kroonen cites the verb as _\*wahs(j)an-_, Orel as _\*waxsanan_, and Ringe and Taylor discuss the prehistory of Old English _weaxan_ within the same verbal family [@Kroonen2013; @Orel2003, 478; @RingeTaylor2014].

#### Old English evidence

Clark Hall gives _weaxan_ as the verb headword and separately records bare _wax_ as a preterite form; Bright likewise treats _weaxan_ as the infinitive [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wáxsaną_, brightening and breaking yield _weax-_, and the infinitive develops regularly to _weaxan_. The cluster is preserved here, since _xs_ > _s_ belongs to forms where another consonant follows, such as _wæstm_, not to the infinitive itself [@Campbell1959; @SieversBrunner1965].

#### Lexical note

The target here is the infinitive _weaxan_. Noun _weax_ and preterite _wax_/_wēox_ belong to different lexical or paradigm slots.

### way — OE _weġ_

\index[oe]{weg@\emph{weġ}}
\index[pgmc]{wegaz@*wégaz}

Derivation: _\*wégaz_ > _weġ_ (regular).

#### Derivation trace

Proto input: _\*wégaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wéga} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wég} \\
OE Velar Palatalization & \emph{*wéʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weġ_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*wega-_ 'way, road', while the selected derivational form here is nominative-singular _\*wégaz_ [@Kroonen2013]. Campbell, Hogg, and Ringe and Taylor use the same word as the standard contrast between singular palatal _weġ_ and inflected _wegas_/_wegum_ [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Old English evidence

The Old English singular is the ordinary noun _weg_, here normalized as _weġ_ to show the palatal final. The contrasting plural and oblique forms _wegas, wegum_ keep a velar stop before the following back vowel [@Campbell1959; @RingeTaylor2014, 341].

#### Development to Old English

From _\*wégaz_, final _\*z_ is lost and the weak tail apocopates, leaving word-final _\*g_ after a front vowel. In that environment Old English palatalization yields _weġ_, whereas _wegas_ remains velar because the following _a_ blocks the same outcome [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Form note

Normalized _weġ_ and dictionary _weg_ represent the same noun. _wē_ is not supported in the checked Old English evidence for 'way'.

### weapon — OE _wǣpn_

\index[oe]{waepn@\emph{wǣpn}}
\index[pgmc]{wepna@*wḗpną}

Derivation: _\*wḗpną_ > _wǣpn_ (regular).

#### Derivation trace

Proto input: _\*wḗpną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*wǣpną} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*wǣpn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wǣpn_

#### Reconstruction and comparative evidence

Kroonen reconstructs a double-stem noun _\*wēbna-_ ~ _\*wēpna-_ and cites OE _wæpn_ among its reflexes [@Kroonen2013, 617]. The form followed here, _\*wḗpną_, represents the unbroken citation-form noun rather than the later broken simplex.

#### Old English evidence

Campbell's cluster-noun discussion preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. Bright
contrasts broken nominative _wǣpen_/_wapen_ with unbroken oblique _wǣpnes_,
while Clark Hall lemmatizes the noun under _wapen_ and also preserves unbroken
forms in compounds and related spellings
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

#### Development to Old English

Northwest Germanic lowering gives _wǣpn_, and loss of the final nasal vowel leaves the unbroken cluster word-finally. The Old English form here is the attested unbroken form _wǣpn_.

#### Form note

The ordinary late West Saxon simplex headword is _wǣpen_, but Campbell's
noun-class discussion also preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. _wǣpnes_
remains the regular unbroken oblique comparator
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

### will — OE _willa_

\index[oe]{willa@\emph{willa}}
\index[pgmc]{weljo@*wéljô}

Derivation: _\*wéljô_ > _willa_ (regular).

#### Derivation trace

Proto input: _\*wéljô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*wélljô} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*willjô} \\
OE Unstressed Long Vowel Shortening & \emph{*willja} \\
OE J Loss After Heavy & \emph{*willa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _willa_

#### Reconstruction and comparative evidence

Kroonen separates noun _\*weljan-_ 2 'will, wish' from verb _\*weljan-_ 1 'to want', while Orel and Kluge represent the noun as _\*weljōn_ [@Kroonen2013; @Orel2003; @KlugeSeebold2011]. The selected derivational form _\*wéljô_ is the noun-side input used for this row.

#### Old English evidence

Clark Hall lemmatizes noun _willa m._ separately from verb _willan_ [@ClarkHall1960, 368]. The Old English form here is the noun citation form, not the related verb.

#### Development to Old English

From _\*wéljô_, j-gemination yields a heavy stem, i-umlaut gives _will-_, and later shortening plus j-loss produce _willa_. The noun is therefore a regular weak masculine outcome.

#### Lexical note

The target here is the noun _willa_ 'will, wish'. Related verb _willan_ belongs to a separate lexeme and should not be substituted for the noun row [@Kroonen2013; @ClarkHall1960, 368].

### wind — OE _windan_

\index[oe]{windan@\emph{windan}}
\index[pgmc]{windana@*wíndaną}

Derivation: _\*wíndaną_ > _windan_ (regular).

#### Derivation trace

Proto input: _\*wíndaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*wíndan} \\
OE Secondary Nasalization & \emph{*wíndąn} \\
OE Weak Tail Reduction & \emph{*wíndan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _windan_

#### Reconstruction and comparative evidence

Kroonen distinguishes noun _\*winda-_ from verb _\*windan-_, and the present row belongs to the verb [@Kroonen2013]. Fulk and Ringe and Taylor derive the dental directly from PIE _\*wendh-_, not from a Verner alternant [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller record _windan_ as the verb headword [@ClarkHall1960; @BosworthToller1898, 101]. The Old English form here is the ordinary infinitive of the strong verb.

#### Development to Old English

The form followed here, _\*wíndaną_, yields the regular infinitive _windan_ by ordinary heavy-syllable apocope and weak-tail reduction. The form is therefore a straightforward strong-verb outcome.

#### Lexical note

English *wind* also names the noun. This row represents the class-III verb, not the noun [@Kroonen2013; @ClarkHall1960].

### wold — OE _weald_

\index[oe]{weald@\emph{weald}}
\index[pgmc]{walthuz@*wálθuz}

Derivation: _\*wálθuz_ > _weald_ (regular).

#### Derivation trace

Proto input: _\*wálθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc L Th Voicing & \emph{*wálduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wáldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wældu} \\
OE Breaking & \emph{*wealdu} \\
\mbox{OE High Vowel Apocope} & \emph{*weald} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weald_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*walþu-_ and gives OE _weald_ beside other West Germanic _wald_ forms [@Kroonen2013]. The form followed here, _\*wálθuz_, is the nominative singular used for the derivation.

#### Old English evidence

Clark Hall makes _weald_ the main noun headword and cross-refers _wald_ and _wold_ to it [@ClarkHall1960]. The Anglian-looking _wald_ therefore remains variant background rather than the main target.

#### Development to Old English

_\*lþ_ voices to _ld_, Anglo-Frisian brightening yields _wæld-_, and breaking before the cluster gives _weald-_; apocope then yields _weald_. The noun is therefore a regular breaking outcome.

#### Dialect note

_wald_ survives as an Anglian-type variant in the same family. The Old English form here is normalized _weald_, not the variant form [@ClarkHall1960; @RingeTaylor2014].

### yarn — OE _ġearn_

\index[oe]{gearn@\emph{ġearn}}
\index[pgmc]{garna@*gárną}

Derivation: _\*gárną_ > _ġearn_ (regular).

#### Derivation trace

Proto input: _\*gárną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gærną} \\
OE Breaking & \emph{*gearną} \\
OE Heavy Syllable Nasal Apocope & \emph{*gearn} \\
OE Velar Palatalization & \emph{*ʤearn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*garna-_, and Ringe and Taylor give the early chain _\*garna_ > _\*geern_ > _\*gearn_ > OE _gearn_ [@Kroonen2013; @RingeTaylor2014, 220]. The form followed here, _\*gárną_, is the nominal citation form used here, while oblique _\*garnăn_ belongs only to comparative background.

#### Old English evidence

Clark Hall records _gearn (e) n._ 'yarn, spun wool', and Bosworth-Toller glosses _gearn_ as _filatum_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*gárną_, brightening and breaking before _rn_ yield _gearn_; palatalization of initial _g_ before the resulting front-vocalic sequence gives normalized _ġearn_. The derivation is regular.

#### Form note

Dictionary _gearn_ and normalized _ġearn_ refer to the same noun. The comparative stem _\*garna-_ and oblique _\*garnăn_ do not replace the derivational input _\*gárną_.

\clearpage

## Attested variants and comparison forms

Here the Old English comparator belongs to a documented set of variants. The
variation is part of the evidence and not an inconvenience to be normalized
away.

### cud — OE _cwedu_

\index[oe]{cwedu@\emph{cwedu}}
\index[pgmc]{kweduz@*kwéðuz}
\index[pgmc]{kwithuz@*kwíθuz}

Derivation: citation reconstruction _\*kwíθuz_; form followed here _\*kwéðuz_ > _cwedu_ (attested variant).

#### Derivation trace

Proto input: _\*kwéðuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*kwéduz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kwédu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cwedu_

#### Reconstruction and comparative evidence

Kroonen reconstructs the resin word as _\*kwedu-2_ and gives Old English
variants [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4737"}, [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4737"}, and [_c(w)udu_]{.iv lang=oe display=c(w)udu sort=cwudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4737"} [@Kroonen2013, 355]. Orel likewise
lists [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4738"} under the cognate set [@Orel2003, 266]. The derivational input
[_\*kwéðuz_]{.iv lang=pgmc sort=kweduz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4739"}
therefore represents the older e-grade, voiced-dental form behind the chosen
variant [_cwedu_]{.iv lang=oe sort=cwedu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4741"}.

#### Old English evidence

The Old English word survives in a wider variant set than one dictionary
headword suggests. Ringe and Taylor discuss [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4746"} > [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4746"} > [_cudu_]{.iv lang=oe sort=cudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4746"} and also
note late West Saxon [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4747"}; Clark Hall gives [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4747"}, [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4747"}, and [_cudu_]{.iv lang=oe sort=cudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4747"}
[@RingeTaylor2014, 338; @ClarkHall1960, 84]. Attested _cwedu_ is treated here
as the
conservative variant within that set.

#### Development to Old English

From [_\*kwéðuz_]{.iv lang=pgmc sort=kweduz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4754"}, the West Germanic voiced dental hardens in the expected way and
the regular Old English development yields [_cwedu_]{.iv lang=oe sort=cwedu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4755"}. The other Old English
spellings belong to the same lexical family, but reflect later leveling,
back-umlaut, or further reduction rather than a need to replace the selected
input.

#### Variant comparison

| Variant type | Old English form | Comment |
| :--- | :--- | :--- |
| conservative target | [_cwedu_]{.iv lang=oe sort=cwedu role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4764"} | selected attested variant represented here |
| leveled i-grade form | [_cwidu_]{.iv lang=oe sort=cwidu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4765"} | common lexical variant in the same family |
| back-umlauted forms | [_cweodu_]{.iv lang=oe sort=cweodu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4766"}, [_cwudu_]{.iv lang=oe sort=cwudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4766"} | later developments within the same OE tradition |
| reduced form | [_cudu_]{.iv lang=oe sort=cudu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4767"} | further reduced member of the same variant set |

### ten — OE _tēon_

\index[oe]{teon@\emph{tēon}}
\index[pgmc]{texun@*téxun}

Derivation: _\*téxun_ > _tēon_ (attested variant).

#### Derivation trace

Proto input: _\*téxun_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*téxon} \\
OE Breaking & \emph{*téoxon} \\
OE H Loss & \emph{*téoon} \\
OE Contraction & \emph{*tḗon} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _tēon_

#### Reconstruction and comparative evidence

Fulk states that Old English _tien_ shows umlaut from the inflected forms,
whereas the uninflected form without umlaut is reflected in
_hund-tēon-tig_ [@Fulk2018, §10.2]. Brunner gives the same contrast more
broadly: _tēon_ develops from _\*tëhun_, while West Saxon tien, _tȳn_ belong to
a different, umlauted branch of the numeral history [@SieversBrunner1965,
§§129.2, 129 Anm. 6, 234].

The comparison form _tēon_ therefore represents the bare cardinal's
un-umlauted line, not the later umlauted simplex tradition.

#### Old English evidence

The attested simplex forms are varied. Campbell gives _tien_, north-western
West Saxon _tēn_, and late Northumbrian _tēo_, _tēa_
[@Campbell1959, §682]. Brunner likewise lists West Saxon tien, _tȳn_ beside
_tēn_, _tēo_, _tēa_ in other dialects [@SieversBrunner1965, §325].

Exact simplex _tēon_ is weaker as a directly cited headword than those
spellings. The un-umlauted stem is, however, explicit in _tēoða_ and
_-tēontig_ [@SieversBrunner1965, §129.2; @Fulk2018, §10.2]. The comparison
form _tēon_ is therefore a normalized spelling of that un-umlauted base.

#### Development to Old English

From _\*téxun_, lowering of medial unstressed _u_ gives _\*téxon_,
breaking gives _\*téoxon_, loss of intervocalic _h_/_x_ yields _\*téoon_,
and contraction produces _\*tḗon_, written _tēon_. This is the regular
bare-cardinal path.

The umlauted forms _tien_ / _tīen_ belong to a different branch, created when
the numeral was levelled from inflected forms with a front-vocalic trigger
[@Fulk2018, §10.2; @SieversBrunner1965, §129 Anm. 6].

#### Variant comparison

The comparison below sets the relevant forms side by side. It distinguishes the normalized un-umlauted base
from the attested simplex variants.

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _tēon_ | normalized un-umlauted comparison form; trace-supported | Old English form here |
| _tien_ / _tīen_ | attested West Saxon umlauted simplex forms | genuine OE variants, but not the bare-cardinal line modeled here |
| _tēn_ / _tēo_ / _tēa_ | attested un-umlauted simplex variants in other dialects | support the same branch as the comparison form |

### three — OE _þrīe_

\index[oe]{thrie@\emph{þrīe}}
\index[pgmc]{threjez@*θréjez}

Derivation: _\*θréjez_ > _þrīe_ (attested variant).

#### Derivation trace

Proto input: _\*θréjez_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*θréje} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*θrije} \\
OE Intervocalic J Vocalization & \emph{*θriie} \\
OE Contraction & \emph{*θrīe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þrīe_

#### Reconstruction and comparative evidence

Kroonen cites the numeral under a broader stem-style reconstruction rather than
under one Old English-ready paradigm cell [@Kroonen2013, 586]. The input
[_\*θréjez_]{.iv lang=pgmc sort=threjez role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4918"} is therefore best understood as the inherited masculine
nominative-accusative singular.

The Old English numeral has no uniform citation form across the paradigm. The
masculine singular line must be
kept apart from feminine-neuter _þrēo_ and from later reduced spellings of
the masculine form.

#### Old English evidence

Campbell gives masculine nominative-accusative [_þrīe_]{.iv lang=oe sort=thrie role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4928"}, feminine and neuter
nominative-accusative [_þrēo_]{.iv lang=oe sort=threo role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4929"}, genitive [_þrēora_]{.iv lang=oe sort=threora role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4929"}, and dative
[_þrim_]{.iv lang=oe sort=thrim role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4930"}, adding that late West Saxon has _þry_, _þri_ for [_þrīe_]{.iv lang=oe sort=thrie role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4930"}
[@Campbell1959, §683]. Fulk presents the same masculine _þrīe_ beside the
wider numeral paradigm [@Fulk2018, §10.1].

The target is therefore an attested Old English paradigm cell. _þrī_
belongs to later reduction or headword-style citation, whereas _þrīe_ is
the conservative masculine nominative-accusative form.

#### Development to Old English

From _\*θréjez_, loss of final _-z_ leaves a form of the _\*θréje_
type. The following _j_ fronts the stem vowel, then vocalizes between
vowels, and contraction yields _þrīe_. The compact trace records the same
sequence as _\*θrije_ > _\*θriie_ > _þrīe_.

#### Variant comparison

The comparison below sets the relevant forms side by side. It separates the selected masculine cell from
the later reduced form and from the rest of the numeral paradigm.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| [_þrīe_]{.iv lang=oe sort=thrie role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4952"} | attested masculine nom./acc.; regular output | Old English form here |
| _þrī_ / _þry_ | later reduced masculine variant | genuine OE variant, but not the conservative comparison form |
| [_þrēo_]{.iv lang=oe sort=threo role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4954"} | attested feminine-neuter nom./acc. | same numeral, different paradigm cell |
| [_þrēora_]{.iv lang=oe sort=threora role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4955"}, [_þrim_]{.iv lang=oe sort=thrim role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:4955"} | attested genitive and dative forms | confirm the wider paradigm, not the cell compared here |

### wasp — OE _wæfs_

\index[oe]{waefs@\emph{wæfs}}
\index[pgmc]{wabsaz@*wábsaz}

Derivation: _\*wábsaz_ > _wæfs_ (attested variant).

#### Derivation trace

Proto input: _\*wábsaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*wábsa} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wábs} \\
Anglo Frisian Brightening & \emph{*wæbs} \\
PGmc B Allophony & \emph{*wæβs} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wæfs_

#### Reconstruction and comparative evidence

The Proto-Germanic form [_\*wábsaz_]{.iv lang=pgmc sort=wabsaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5009"} reaches Old English without any special
change of stem or paradigm cell. The question in this entry is instead which
attested Old English member of the variant set should serve as the comparison
form.

Fulk presents the Old English forms together as [_wæfs_]{.iv lang=oe sort=waefs role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5014"} with variants [_wæsp_]{.iv lang=oe sort=waesp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5014"} and
[_wæps_]{.iv lang=oe sort=waeps role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5015"} [@Fulk2018, §6.5]. Bülbring and Brunner then make the chronology more
explicit by deriving later _wæps_ and late West Saxon _wasp_ from earlier
_waefs_ / _wæfs_ through restricted metatheses [@Bulbring1902, §484 Anm. 3;
@SieversBrunner1965, §§193, 204].

#### Old English evidence

The earliest directly cited Old English form is [_wæfs_]{.iv lang=oe sort=waefs role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5022"}, written [_waefs_]{.iv lang=oe sort=waefs role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5022"} in
the Épinal-Corpus material discussed by Bülbring and Brunner
[@Bulbring1902, §484 Anm. 3; @SieversBrunner1965, §193]. Later Old English also
shows [_wæps_]{.iv lang=oe sort=waeps role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5025"} and [_wæsp_]{.iv lang=oe sort=waesp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5025"} / [_wasp_]{.iv lang=oe sort=wasp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5025"}, and dictionary practice often favors
[_wæps_]{.iv lang=oe sort=waeps role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5026"} or later spellings as headwords [@ClarkHall1960, 341].

This entry therefore distinguishes chronological priority from headword habit.
[_wæfs_]{.iv lang=oe sort=waefs role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5029"} is not a convenient reconstruction: it is an attested Old English form
and also the one that matches the regular development most closely.

#### Development to Old English

From [_\*wábsaz_]{.iv lang=pgmc sort=wabsaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5034"}, the regular Old English path passes through loss of final _z_,
Anglo-Frisian fronting, and the allophonic development of _b_ to a fricative
before _s_, yielding [_wæfs_]{.iv lang=oe sort=waefs role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5036"}.

The later forms [_wæps_]{.iv lang=oe sort=waeps role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5038"} and [_wæsp_]{.iv lang=oe sort=waesp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5038"} / [_wasp_]{.iv lang=oe sort=wasp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5038"} belong to subsequent, lexically
restricted metatheses. They are genuine Old English forms, but they are later
within the variant history.

#### Variant comparison

The comparison below sets the relevant forms side by side. It separates the earliest attested and regular
form from the later metathesized doublets.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| [_wæfs_]{.iv lang=oe sort=waefs role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5049"} | earliest attested OE form; regular output | Old English form here |
| [_wæps_]{.iv lang=oe sort=waeps role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5050"} | later attested metathesized variant | genuine OE doublet, but secondary |
| [_wæsp_]{.iv lang=oe sort=waesp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5051"} / [_wasp_]{.iv lang=oe sort=wasp role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5051"} | later West Saxon metathesized variant | genuine OE doublet, but not the form compared here |

\clearpage

## Early analogy and pre-Old-English input selection

Here an analogical change already separates the transducer input from the
lexeme's citation reconstruction before the specifically Old English changes
apply. Each entry must therefore justify the remodeled input independently of
the successful output.

### bottom — OE _botm_

\index[oe]{botm@\emph{botm}}
\index[pgmc]{budmaz@*búdmaz}
\index[pgmc]{buttmaz@*búttmaz}

Derivation: citation reconstruction _\*búdmaz_; form followed here _\*búttmaz_ > _botm_ (early analogy).

#### Derivation trace

Proto input: _\*búttmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bóttmaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*bóttma} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*bóttm} \\
OE Preconsonantal Degemination & \emph{*bótm} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _botm_

#### Reconstruction and comparative evidence

Kroonen reconstructs the word as a stem complex _\*budmō_, gen. _\*buttaz_,
summarized as _\*budman-_ ~ _\*buttman-_, and gives Old English _botm_ as the reflex
[@Kroonen2013, 120]. The comparative label _\*búdmaz_ names the lexeme-level stem
complex, while the derivational input _\*búttmaz_ represents the pre-Old-English
form with oblique _\*butt-_ generalized into the nominative formation.

Orel likewise preserves both sides of the comparison under _\*budmaz_ _\*butmaz_
[@Orel2003, 100]. The derivational input is thus a historical stem choice, not an
arbitrary respelling.

#### Old English evidence

The Old English noun itself is secure. Clark Hall gives _botm_
[@ClarkHall1960, 63]. Bosworth-Toller cross-references _bodan_ to _botm_,
showing the wider reflex family without weakening the attested lemma
[@BosworthToller1898, 112].

#### Development to Old English

Once the oblique _\*butt-_ stem has been generalized, the derivational input
_\*búttmaz_ develops regularly to _botm_. The analogical step is therefore early:
it belongs to pre-Old-English stem formation rather than to a later choice
among Old English paradigm cells.

### brand — OE _brandes_

\index[oe]{brandes@\emph{brandes}}
\index[pgmc]{brandas@*brándas}
\index[pgmc]{brandaz@*brándaz}

Derivation: citation reconstruction _\*brándaz_; form followed here _\*brándas_ > _brandes_ (early analogy).

#### Derivation trace

Proto input: _\*brándas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*brándæs} \\
OE Unstressed AE Merger & \emph{*brándes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brandes_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem [_\*brándaz_]{.iv lang=pgmc sort=brandaz source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5187"}, continued by Old English
[_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5188"} and its continental cognates [@Orel2003, 53]. The selected
input [_\*brándas_]{.iv lang=pgmc sort=brandas source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5189"} is not a different lexeme but the genitive singular of that
same a-stem noun.

Both forms belong to the same root and stem class but occupy different inherited
inflectional cells. The derivational input is the oblique cell.

#### Old English evidence

Old English dictionaries lemmatize the noun as [_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5197"} [@ClarkHall1960, 49;
@BosworthToller1898, 116]. Bosworth-Toller also records inflectional forms such as
[_brandas_]{.iv lang=oe sort=brandas source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5199"}, [_branda_]{.iv lang=oe sort=branda source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5199"}, and [_brandum_]{.iv lang=oe sort=brandum source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5199"} under the same entry [@BosworthToller1898, 116].

The specific comparison form in this entry, [_brandes_]{.iv lang=oe sort=brandes source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5201"}, is the expected
genitive singular of that a-stem noun. It is therefore an inferred Old English
paradigm form rather than the ordinary dictionary headword.

#### Development to Old English

From [_\*brándas_]{.iv lang=pgmc sort=brandas source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5207"}, the regular Old English development passes through the usual
unstressed-vowel weakening of the inflectional ending, yielding [_brandes_]{.iv lang=oe sort=brandes source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5208"}.
Nothing in the stem itself requires a special repair. The root consonants and
the stressed vowel are the same as in the citation lemma [_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5210"}.

The analytical weight of the entry lies in the ending. By choosing the oblique
singular rather than the nominative citation form, the entry presents the same
lexeme in a different inherited cell.

#### Form comparison

The comparison below sets the relevant forms side by side. It separates the citation lemma from the
selected oblique singular.

| Form / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*brándaz_]{.iv lang=pgmc sort=brandaz source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5223"} | expected OE lemma [_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5223"} | [_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5223"} | regular headword-level outcome |
| genitive singular | [_\*brándas_]{.iv lang=pgmc sort=brandas source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5224"} | regular output: [_brandes_]{.iv lang=oe sort=brandes source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5224"} | [_brandes_]{.iv lang=oe sort=brandes source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5224"} | exact match for the oblique cell |

The noun itself is straightforwardly inherited. The main point of the entry is
that [_brandes_]{.iv lang=oe sort=brandes source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5227"} belongs to the same regular a-stem paradigm as [_brand_]{.iv lang=oe sort=brand source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5227"}, even
though the citation lemma remains the nominative singular.

### breast — OE _brēost_

\index[oe]{breost@\emph{brēost}}
\index[pgmc]{breusta@*bréustą}
\index[pgmc]{brustz@*brústz}

Derivation: citation reconstruction _\*brústz_; form followed here _\*bréustą_ > _brēost_ (early analogy).

#### Derivation trace

Proto input: _\*bréustą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*brēostą} \\
OE Heavy Syllable Nasal Apocope & \emph{*brēost} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _brēost_

#### Reconstruction and comparative evidence

The word family shows two related but distinct Proto-Germanic formations. The
root noun [_\*brust-_]{.iv lang=pgmc sort=brust role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5280"} lies behind forms such as Gothic [_brusts_]{.iv lang=goth sort=brusts role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5280"}, whereas Old
English [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5281"} belongs to a thematic formation [_\*breusta-_]{.iv lang=pgmc sort=breusta role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5281"}, alongside Old
Norse [_brjóst_]{.iv lang=on sort=brjost role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5282"} and Old Saxon [_briost_]{.iv lang=os sort=briost role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5282"} [@Kroonen2013, 114; @Orel2003, 95;
@RingeTaylor2014, 43].

The derivational input [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5285"} therefore differs from the citation label
[_\*brústz_]{.iv lang=pgmc sort=brustz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5286"} because Old English reflects the thematic branch rather than the root
noun. The morphological choice comes before the Old English sound changes
themselves.

#### Old English evidence

Clark Hall records the noun as [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5292"} / [_breóst_]{.iv lang=oe sort=breost role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5292"}
[@ClarkHall1960, 65]. The form is an established Old English
lexeme, not a reconstructed target assembled from comparative evidence alone.

What requires explanation is not the Old English attestation but the relation
between that attested noun and the broader Germanic word family. The relevant
comparison form is therefore the thematic Old English noun [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5298"}.

#### Development to Old English

From [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5302"}, the regular Old English development gives [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5302"}, with the
expected _eu_ > _ēo_ vowel history [@Campbell1959, §115]. No special repair is needed
once the correct thematic formation is chosen.

The earlier mismatch arose only if the word was forced into the root-noun line.
The Old English noun itself continues the thematic branch cleanly and directly.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader root-noun family label
from the thematic formation actually continued in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader root-noun family | [_\*brústz_]{.iv lang=pgmc sort=brustz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5316"} | root-noun type outcomes outside OE | non-OE comparanda | useful family label, but not the direct source of _brēost_ |
| selected thematic formation | [_\*bréustą_]{.iv lang=pgmc sort=breusta role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5317"} | regular output: _brēost_ | [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5317"} | exact match between formation and attested OE noun |

The relevant point is the formation split. [_brēost_]{.iv lang=oe sort=breost role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5319"} is the regular Old English
outcome of the thematic [_\*breusta-_]{.iv lang=pgmc sort=breusta role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5320"} branch, not of the root noun [_\*brust-_]{.iv lang=pgmc sort=brust role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5320"}.

### craft — OE _cræft_

\index[oe]{craeft@\emph{cræft}}
\index[pgmc]{kraftaz@*kráftaz}
\index[pgmc]{kraftiz@*kráftiz}

Derivation: citation reconstruction _\*kráftiz_; form followed here _\*kráftaz_ > _cræft_ (early analogy).

#### Derivation trace

Proto input: _\*kráftaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*kráfta} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*kráft} \\
Anglo Frisian Brightening & \emph{*kræft} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cræft_

#### Reconstruction and comparative evidence

Comparative sources disagree about the older stem class. Kroonen gives a u-stem
_\*kraftu-_, while Orel prints _\*kraftiz_ ~ _\*kraftuz_ [@Kroonen2013, 340; @Orel2003,
259].
The comparative label _\*kráftiz_ remains in view as a lexeme-level shorthand,
while _\*kráftaz_ is the pre-Old-English form used for the Old English
derivation.

#### Old English evidence

The Old English noun itself is secure. Clark Hall and Bosworth-Toller both give
_cræft_ as the headword [@ClarkHall1960, 19; @BosworthToller1898, 145].

#### Development to Old English

The comparison is between possible pre-Old-English inputs. The i-stem
comparator _\*kráftiz_ gives _creft_, while the u-stem comparator _\*kráftuz_
gives _craft_. The a-stem-shaped input _\*kráftaz_ yields _cræft_ and is
therefore the form used for the Old English derivation. This does not require
treating the comparative dictionaries as identical; it shows the narrower point
that the Old English derivation needs a pre-Old-English form without the
i-umlaut trigger of _\*-iz_ and without the back-vowel outcome associated with
the u-stem comparator.

#### Form comparison

| Candidate input | OE output | Result |
| :--- | :--- | :--- |
| *kráftiz | _creft_ | non-match; i-stem comparator |
| *kráftuz | _craft_ | non-match; u-stem comparator |
| *kráftaz | _cræft_ | exact match; selected pre-OE input |

### dill — OE _dile_

\index[oe]{dile@\emph{dile}}
\index[pgmc]{deliz@*déliz}
\index[pgmc]{deljaz@*déljaz}

Derivation: citation reconstruction _\*déljaz_; form followed here _\*déliz_ > _dile_ (early analogy).

#### Derivation trace

Proto input: _\*déliz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*déli} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*dili} \\
OE Med Unstressed I Lowering1 & \emph{*dile} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _dile_

#### Reconstruction and comparative evidence

Comparative evidence preserves both an i-stem and a ja-stem formation, with Old
English [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5456"} on one side and continental forms such as Old Saxon [_dilli_]{.iv lang=os sort=dilli role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5456"} and
Old High German [_tilli_]{.iv lang=ohg sort=tilli role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5457"} on the other [@Fulk2018, 170]. The derivational input
[_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5458"} therefore represents the i-stem side of the paradigm,
whereas the citation label [_\*déljaz_]{.iv lang=pgmc sort=deljaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5459"} is a broader comparative headword.

The stem class determines the Old English consonant shape. A
ja-stem with _\*-lj-_ would be expected to produce gemination, but the Old
English noun shows a single _l_. Fulk's discussion of ja-stems transferred to
the i-stems provides the relevant morphological background for the OE side
[@Fulk2018, 170].

#### Old English evidence

Old English dictionaries record the plant name as [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5469"}, alongside the variant
[_dili_]{.iv lang=oe sort=dili role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5470"} [@BosworthToller1898, 164; @ClarkHall1960, 95]. The form discussed here is
therefore an attested Old English noun with single _l_.

The Old English evidence is the relevant point. Whatever broader comparative
headword is chosen for the family, the inherited form reflected in OE is the
i-stem type [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5475"}, not a geminated [_dill_]{.iv lang=oe sort=dill role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5475"} outcome.

#### Development to Old English

From [_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5479"}, regular loss of final _z_ and the later lowering of unstressed
_i_ yield [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5480"}. The stem itself remains ungeminated throughout that path.

The contrast is morphological rather than phonological. If the word were
forced through a ja-stem _\*-lj-_ pathway, the expected result would show _ll_.
The attested Old English noun instead matches the i-stem development.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the stem class actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative ja-stem label | [_\*déljaz_]{.iv lang=pgmc sort=deljaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5493"} | ja-stem type outcome with gemination | [_dill_]{.iv lang=oe sort=dill role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5493"}-type comparison | useful comparative label, but not the OE form |
| selected i-stem formation | [_\*déliz_]{.iv lang=pgmc sort=deliz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5494"} | regular output: [_dile_]{.iv lang=oe sort=dile role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5494"} | [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5494"} | exact match between formation and attested OE noun |

The single _l_ is the decisive diagnostic. It identifies [_dile_]{.iv lang=oe sort=dile role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5496"} with the i-stem
formation rather than with the continental ja-stem branch.

### fast — OE _festan_

\index[oe]{festan@\emph{festan}}
\index[pgmc]{fastena@*fastēną}
\index[pgmc]{fastijana@*fástijaną}

Derivation: citation reconstruction _\*fastēną_; form followed here _\*fástijaną_ > _festan_ (early analogy).

#### Derivation trace

Proto input: _\*fástijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*fæstijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*fæstijan} \\
OE Secondary Nasalization & \emph{*fæstijąn} \\
Sievers Law Syncope & \emph{*fæstjąn} \\
OE I Umlaut & \emph{*festjąn} \\
OE Weak Tail Reduction & \emph{*festjan} \\
OE J Loss After Heavy & \emph{*festan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _festan_

#### Reconstruction and comparative evidence

Kroonen places the verb within the wider [_\*fastu-_]{.iv lang=pgmc sort=fastu role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5553"} adjective family and its
derived [_\*fasten-_]{.iv lang=pgmc sort=fasten role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5554"} verbal line, the comparative background behind Old English
'to fast' [@Kroonen2013, 171]. Ringe and Taylor, however, distinguish the Old English verb
more closely: they treat OE 'to fast' as originally a class-I weak verb that
later acquired the stative meaning through lexical confusion [@RingeTaylor2014, 110].

The derivational input [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5559"} therefore represents the inherited class-I
formation reflected in Old English, whereas the citation label [_\*fastēną_]{.iv lang=pgmc sort=fastena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5560"}
belongs to the broader comparative presentation of the lexeme.

#### Old English evidence

Old English dictionaries record forms such as [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5565"}, alongside related
[_fæstan_]{.iv lang=oe sort=faestan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5566"} / [_fǣstan_]{.iv lang=oe sort=faestan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5566"} spellings and meanings [@BosworthToller1898, 213]. The form selected here is [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5566"}, which fits the regular
class-I phonological development.

The _æ_-forms remain relevant, but they do not control the entry. In the
present analysis they belong to a later analogical reshaping under the
adjective [_fæst_]{.iv lang=oe sort=faest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5571"}, whereas [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5571"} is the regular inherited class-I comparison
form.

#### Development to Old English

From [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5576"}, Anglo-Frisian brightening and subsequent i-umlaut produce the
fronted vowel seen in [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5577"}. The later weak-tail reductions and loss of _j_
after a heavy syllable complete the regular Old English outcome.

What makes the entry non-regular is not the phonology of [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5580"} itself, but
the choice of formation. Old English continues the class-I verb, even though
the comparative headword is often given under the parallel [_\*fastēn-_]{.iv lang=pgmc sort=fasten role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5582"} family.

#### Class comparison

The comparison below sets the relevant forms side by side. It distinguishes the comparative class-III
headword from the class-I formation actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative class-III headword | [_\*fastēną_]{.iv lang=pgmc sort=fastena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5591"} | class-III type outcome, not [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5591"} | wider family context | useful family label, but not the direct source of the target |
| selected class-I weak verb | [_\*fástijaną_]{.iv lang=pgmc sort=fastijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5592"} | regular output: [_festan_]{.iv lang=oe sort=festan role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5592"} | [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5592"} | exact match between formation and attested OE verb |
| later analogical reshaping | adjective-driven [_fæst_]{.iv lang=oe sort=faest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5593"} influence | [_fæstan_]{.iv lang=oe sort=faestan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5593"} / [_fǣstan_]{.iv lang=oe sort=faestan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5593"} type spellings | fæstan-type evidence | genuine later OE reshaping, but secondary to the Old English form here |

The relevant point is the class split. [_festan_]{.iv lang=oe sort=festan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5595"} is the regular Old English
outcome of the class-I formation, while the better-known _æ_-forms belong to a
later analogical layer.

### flask — OE _flasce_

\index[oe]{flasce@\emph{flasce}}
\index[pgmc]{flasko@*flaskō}
\index[pgmc]{flaskon@*fláskōn}

Derivation: citation reconstruction _\*flaskō_; form followed here _\*fláskōn_ > _flasce_ (early analogy).

#### Derivation trace

Proto input: _\*fláskōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc N Stem N Loss & \emph{*fláskǭ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*flæskǭ} \\
OE A Restoration & \emph{*flaskǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*flaskæ} \\
OE Unstressed AE Merger & \emph{*flaske} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _flasce_

#### Reconstruction and comparative evidence

The wider Germanic family is often cited under a form such as [_\*flaskō_]{.iv lang=pgmc sort=flasko role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5652"}, but
the evidence relevant for Old English points instead to a weak feminine
formation [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5654"} / [_\*flaskǭ_]{.iv lang=pgmc sort=flasko role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5654"} [@Orel2003, 104]. That distinction is
crucial for the suffixal history of the noun.

The derivational input therefore differs from the citation label in stem class. Old
English [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5658"} belongs with the weak feminine line, and the plural or oblique
forms [_flascan_]{.iv lang=oe sort=flascan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5659"} support that analysis [@RingeTaylor2014, 192].

#### Old English evidence

Old English dictionaries record the noun as [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5663"}, with inflectional support
from forms such as [_flascan_]{.iv lang=oe sort=flascan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5664"}; a later West Saxon [_flaxe_]{.iv lang=oe sort=flaxe role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5664"} is also noted as a
secondary variant [@BosworthToller1898, 235; @ClarkHall1960, 121].

The relevant comparison form is therefore the weak feminine noun [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5667"}.
The plural and oblique evidence helps explain why the vowel
and ending are preserved as they are in the singular.

#### Development to Old English

From [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5673"}, the weak feminine passes through the expected loss of _n_ and
the later Old English development of the unstressed ending, reaching [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5674"}.
Campbell cites restored _a_ in exactly this environment, including [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5675"}
after inflected [_flascan_]{.iv lang=oe sort=flascan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5676"} [@Campbell1959, §158]. Once the weak feminine
formation is chosen, the noun follows a regular path to its Old English shape.

The decisive issue is morphological rather than phonological. A simple strong
feminine citation form does not capture the OE weak noun as cleanly as the
selected _\*fláskōn_ does.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the weak feminine formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader comparative headword | [_\*flaskō_]{.iv lang=pgmc sort=flasko role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5690"} | broader family label | wider family context | useful lexeme label, but not the cleanest OE-facing derivation |
| selected weak feminine formation | [_\*fláskōn_]{.iv lang=pgmc sort=flaskon role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5691"} | regular output: [_flasce_]{.iv lang=oe sort=flasce role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5691"} | [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5691"} | exact match between formation and attested OE noun |

The weak feminine suffix is the relevant point. It aligns the inherited form
with attested [_flasce_]{.iv lang=oe sort=flasce role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5694"} and its supporting paradigm forms.

### follow — OE _fylġan_

\index[oe]{fylgan@\emph{fylġan}}
\index[pgmc]{fulgena@*fulgēną}
\index[pgmc]{fulgijana@*fúlgijaną}

Derivation: citation reconstruction _\*fulgēną_; form followed here _\*fúlgijaną_ > _fylġan_ (early analogy).

#### Derivation trace

Proto input: _\*fúlgijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*fúlgijan} \\
OE Secondary Nasalization & \emph{*fúlgijąn} \\
Sievers Law Syncope & \emph{*fúlgjąn} \\
OE Velar Palatalization & \emph{*fúlʤjąn} \\
OE I Umlaut & \emph{*fylʤjąn} \\
OE Weak Tail Reduction & \emph{*fylʤjan} \\
OE J Loss After Heavy & \emph{*fylʤan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fylġan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the verb as _\*fulgen-_ and gives Old English [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5750"}, [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5750"},
adding that Old Norse [_fylgja_]{.iv lang=on sort=fylgja role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5751"} and Old English [_fylg(e)an_]{.iv lang=oe display=fylg(e)an sort=fylgean role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5751"} continue a formation
_\*fulgjan-_ [@Kroonen2013, 159]. The comparative headword and the class-I formation
are therefore related but not identical.

Ringe and Taylor distinguish PNWGmc _\*fulgija-_ ~ _\*fulgai-_ > OE _fylgan_ ~ _folgian_ and describe it as a dual formation that probably reflects an
older alternation between j-present and e-stative [@RingeTaylor2014, 293-294].
This is a stem-class choice, not a spelling choice. The derivational input
[_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5758"} belongs to the class-I _\*fulgija-_ / _\*fulgjan-_ branch; the citation
form [_\*fulgēną_]{.iv lang=pgmc sort=fulgena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5759"} belongs to the parallel class-II history behind [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5759"}.

#### Old English evidence

The Old English evidence preserves both formations. Clark Hall lists [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5763"}
with variant spellings [_fylgian_]{.iv lang=oe sort=fylgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5764"} and [_fyligan_]{.iv lang=oe sort=fyligan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5764"} [@ClarkHall1960, 125].
Bosworth-Toller likewise has a separate [_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5765"} entry
[@BosworthToller1898, 275].

Bright notes traces of the older conjugation in [_fylg(e)an_]{.iv lang=oe display=fylg(e)an sort=fylgean role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5768"}
[@BrightCassidyRingler1971, 77] and lists [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5769"} ([_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5769"}) in the glossary
[@BrightCassidyRingler1971, 364]. The relevant comparison form in this entry is
therefore the class-I verb [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5771"} / [_fylgean_]{.iv lang=oe sort=fylgean role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5771"}, here normalized as [_fylġan_]{.iv lang=oe sort=fylgan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5771"}.
The spelling with ġ represents the palatalized velar before a front-vocalic
environment.

#### Development to Old English

[_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5777"} is a class-I weak-verb formation. In the class-I branch the _\*j_
blocks NWGmc lowering of _u_ to _o_, since Ringe and Taylor formulate that
lowering for environments in which no _\*j_ intervened [@RingeTaylor2014, 96].
The same front-vocalic environment then triggers i-umlaut, so _u_ becomes _y_
[@RingeTaylor2014, §6.6.2].

The subsequent Old English developments are palatalization of the velar,
weak-tail reduction, and loss of _j_ after a heavy syllable, yielding
[_fylġan_]{.iv lang=oe sort=fylgan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5785"}. This is the regular outcome of the class-I formation. The class-II
form [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5786"} belongs to the parallel _\*-ē-_ / _\*-ai-_ branch and is not the
form modeled here.

#### Class comparison

A class comparison identifies which inherited formation corresponds to the
established Old English form under discussion. The comparison below is manual;
no full automatic class probe is presented here.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation class-II formation | [_\*fulgēną_]{.iv lang=pgmc sort=fulgena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5797"} | probe output: [_folgon_]{.iv lang=oe sort=folgon role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5797"} | [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5797"} | mismatch: the regular output is not the remodeled infinitive _folgian_ |
| parallel class-II branch | PNWGmc _\*fulgai-_ | Ringe-Taylor: OE [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5798"} | [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5798"} | documents the separate class-II branch, but not the target of this entry |
| selected class-I formation | [_\*fúlgijaną_]{.iv lang=pgmc sort=fulgijana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5799"} | regular output: [_fylġan_]{.iv lang=oe sort=fylgan role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5799"} | [_fylġan_]{.iv lang=oe sort=fylgan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5799"} / [_fylgan_]{.iv lang=oe sort=fylgan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5799"} | exact match between input, output, and class |

The relevant point is the class split. [_fylġan_]{.iv lang=oe sort=fylgan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5801"} is the regular Old English
outcome of the class-I _\*fulgija-_ / _\*fulgjan-_ formation, whereas [_folgian_]{.iv lang=oe sort=folgian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5802"}
belongs to the parallel class-II branch.

### gall — OE _ġealla_

\index[oe]{gealla@\emph{ġealla}}
\index[pgmc]{galla@*gállą}
\index[pgmc]{gallo@*gállô}

Derivation: citation reconstruction _\*gállą_; form followed here _\*gállô_ > _ġealla_ (early analogy).

#### Derivation trace

Proto input: _\*gállô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*gællô} \\
OE Breaking & \emph{*geallô} \\
OE Velar Palatalization & \emph{*ʤeallô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʤealla} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġealla_

#### Reconstruction and comparative evidence

The wider cognate family can be presented under a form such as [_\*gállą_]{.iv lang=pgmc sort=galla role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5856"}, but
the Old English noun itself belongs with a weak noun _\*gallōn-_, cited here as
[_\*gállô_]{.iv lang=pgmc sort=gallo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5858"} [@Kroonen2013, 165]. The derivational input therefore differs from the broader
comparative headword in stem class.

The stem class determines the Old English shape. The weak
masculine pathway preserves the ending needed for _ġealla_, whereas a simple
strong-noun headword does not align as closely with the attested OE noun.

#### Old English evidence

Old English dictionaries record the noun as [_gealla_]{.iv lang=oe sort=gealla role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5867"}, and Bright also gives the
dative [_geallan_]{.iv lang=oe sort=geallan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5868"}, confirming a weak-noun paradigm [@BosworthToller1898, 297;
@ClarkHall1960, 145; @BrightCassidyRingler1971, 372]. The normalized spelling
[_ġealla_]{.iv lang=oe sort=gealla role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5870"} uses ġ for the palatal consonant.

Campbell also notes dialectal variation, contrasting West Saxon or Kentish
[_gealla_]{.iv lang=oe sort=gealla role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5873"} with Anglian [_galla_]{.iv lang=oe sort=galla role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5873"} [@Campbell1959, §486]. The target of this entry is the
West Saxon type [_ġealla_]{.iv lang=oe sort=gealla role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5874"}.

#### Development to Old English

From [_\*gállô_]{.iv lang=pgmc sort=gallo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5878"}, the weak noun develops through the expected Old English history
of the suffix and the regular breaking environment before _ll_, yielding
[_ġealla_]{.iv lang=oe sort=gealla role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5880"} [@Campbell1959, §486]. Once the weak masculine input is chosen, the noun
follows a regular path to its attested Old English form.

The decisive issue is therefore morphological. Old English reflects the weak
noun, while the broader family label belongs to a different way of presenting
the cognate set.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the weak noun formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader family label | [_\*gállą_]{.iv lang=pgmc sort=galla role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5894"} | broader cognate-set headword | wider family context | useful lexeme label, but not the direct source of _ġealla_ |
| selected weak noun | [_\*gállô_]{.iv lang=pgmc sort=gallo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5895"} | regular output: [_ġealla_]{.iv lang=oe sort=gealla role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5895"} | [_ġealla_]{.iv lang=oe sort=gealla role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5895"} | exact match between formation and attested OE noun |
| dialectal Anglian continuation | weak noun branch | Anglian [_galla_]{.iv lang=oe sort=galla role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5896"} type | [_galla_]{.iv lang=oe sort=galla role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5896"} | genuine OE variant, but not the West Saxon form used here |

The weak-noun stem class is the relevant point. It gives a direct route to
attested _ġealla_, while the broader comparative label serves only as a family
heading.

### knight — OE _cniht_

\index[oe]{cniht@\emph{cniht}}
\index[pgmc]{knextaz@*knéxtaz}
\index[pgmc]{knixtaz@*kníxtaz}

Derivation: citation reconstruction _\*kníxtaz_; form followed here _\*knéxtaz_ > _cniht_ (early analogy).

#### Derivation trace

Proto input: _\*knéxtaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*knéxta} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*knéxt} \\
OE Breaking & \emph{*knéoxt} \\
OE Ws Palatal Umlaut & \emph{*knixt} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cniht_

#### Reconstruction and comparative evidence

The comparative sources align on an _e_-grade reconstruction for this noun.
Ringe and Taylor cite _\*kneht_, and Orel gives [_\*knextaz_]{.iv lang=pgmc sort=knextaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5955"}
[@RingeTaylor2014, 142; @Orel2003, 256]. Kluge-Seebold likewise points to
_\*knehta-_ [@KlugeSeebold2011, 506]. The derivational input [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5957"} follows that
comparative evidence.

A competing citation reconstruction [_\*kníxtaz_]{.iv lang=pgmc sort=knixtaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5960"} remains possible as a label for
the word family, but it is not the reconstruction followed here. The Old
English development discussed below is based on [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5962"}.

#### Old English evidence

Old English dictionaries record the noun as [_cniht_]{.iv lang=oe sort=cniht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5966"} [@ClarkHall1960, 63;
@BosworthToller1898, 71]. Campbell cites plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5967"} among the broken
forms, showing the same vowel environment from another point in the paradigm
[@Campbell1959, §146].

The target is therefore an ordinary attested Old English noun. No reconstructed
OE comparator is needed here.

#### Development to Old English

From [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5976"}, the relevant Old English changes include breaking before the
velar cluster and then the later reduction that yields [_cniht_]{.iv lang=oe sort=cniht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5977"}. Campbell later
notes the early West-Saxon alternation [_cniht_]{.iv lang=oe sort=cniht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5978"} beside plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5978"}
[@Campbell1959, §305]. Sievers-Brunner gives the same contrast as _cniht ... cneohtas_ [@SieversBrunner1965, §122]. With that corrected input, the
derivation is straightforward.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the handbook-supported _e_-grade
input from a competing citation reconstruction.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing citation reconstruction | [_\*kníxtaz_]{.iv lang=pgmc sort=knixtaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5989"} | not the reconstruction followed here | broader citation tradition | useful as a competing label, but not the source-based choice used for the OE derivation |
| handbook-supported reconstruction | [_\*knéxtaz_]{.iv lang=pgmc sort=knextaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5990"} | regular output: [_cniht_]{.iv lang=oe sort=cniht role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5990"} | [_cniht_]{.iv lang=oe sort=cniht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5990"} | exact match between comparative reconstruction and attested OE noun |
| related plural evidence | same stem family | plural [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5991"} type background | [_cneohtas_]{.iv lang=oe sort=cneohtas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:5991"} | supports the vowel environment, but not the Old English form here cell |

### lade — OE _hladan_

\index[oe]{hladan@\emph{hladan}}
\index[pgmc]{lathojana@*laθōjaną}
\index[pgmc]{xladana@*xláðaną}

Derivation: citation reconstruction _\*laθōjaną_; form followed here _\*xláðaną_ > _hladan_ (early analogy).

#### Derivation trace

Proto input: _\*xláðaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*xládaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xlædaną} \\
OE A Restoration & \emph{*xladaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xladan} \\
OE Secondary Nasalization & \emph{*xladąn} \\
OE Weak Tail Reduction & \emph{*xladan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hladan_

#### Reconstruction and comparative evidence

Ringe and Taylor cite the strong verb _hladan_ directly [@RingeTaylor2014, 248].
The citation label _\*laθōjaną_ is used here only as a broader family heading,
not as the direct source of the OE derivation.

The derivational input therefore marks an early stem choice. The entry follows the
strong Verner-grade form that reaches Old English _hladan_ directly.

#### Old English evidence

Bosworth-Toller records the verb as _hladan_ and preserves the expected
strong-verb paradigm material around it [@BosworthToller1898, 559]. Clark Hall
likewise records _hladan_ [@ClarkHall1960, 159].
The target is an attested infinitive rather than a reconstructed paradigm cell.

For this entry the relevant comparison form is the infinitive _hladan_ itself.
The question is how that attested strong verb relates to the broader comparative
family.

#### Development to Old English

From _\*xláðaną_, the verb passes through the expected early voiced stop stage,
Anglo-Frisian brightening, and the later A-restoration that returns the root
vowel to _a_ before the full infinitival ending. Campbell treats verbs such as
_hladan_ as showing restored _a_ in the present system [@Campbell1959, §744].
Ringe and Taylor likewise derive _hladan_ from the voiced strong-verb line
[@RingeTaylor2014, 248]. The resulting Old English infinitive is _hladan_.

#### Class comparison

The comparison below sets the relevant forms side by side. It separates the wider weak-verb family label
from the strong verb actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative weak-verb label | *laθōjaną | wider family background | broader family context | useful family label, but not the direct source of _hladan_ |
| selected strong Verner-grade input | *xláðaną | regular output: _hladan_ | _hladan_ | exact match between formation and attested OE infinitive |

### lap — OE _lappa_

\index[oe]{lappa@\emph{lappa}}
\index[pgmc]{labbaz@*lábbaz}
\index[pgmc]{lappo@*láppô}

Derivation: citation reconstruction _\*lábbaz_; form followed here _\*láppô_ > _lappa_ (early analogy).

#### Derivation trace

Proto input: _\*láppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*læppô} \\
OE A Restoration & \emph{*lappô} \\
OE Unstressed Long Vowel Shortening & \emph{*lappa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lappa_

#### Reconstruction and comparative evidence

The comparative sources point to a weak noun with _pp_: Orel gives _\*lappōn_,
and the Old English dictionary tradition preserves variant _læppa_
[@Orel2003, 236; @ClarkHall1960, 180]. The derivational input _\*láppô_
follows that evidence.

A competing comparative label _\*lábbaz_ has also circulated for the word
family, but the cited handbooks do not make it the direct source of the Old
English weak noun. The form relevant to the OE development is the weak
masculine input _\*láppô_.

#### Old English evidence

Campbell cites _lappa_ as a case of restored _a_
[@Campbell1959, §158]. Sievers-Brunner records _lappa_ beside variant _læppa_
[@SieversBrunner1965, §10]. The dictionary tradition also preserves _læppa_
[@ClarkHall1960, 180; @BosworthToller1898, 613].

The target of this entry is the restored singular _lappa_. The variant _læppa_
and the oblique or plural _leappan_ remain part of the Old English record and
help frame the noun's vowel history.

#### Development to Old English

Campbell explicitly lists _lappa_ among the forms with restored _a_
[@Campbell1959, §158]. Sievers-Brunner records _lappa_ beside variant _læppa_
at the same Old English stage [@SieversBrunner1965, §10]. With the weak
masculine input chosen, the selected _lappa_ outcome is therefore the regular
Old English comparison.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the weak masculine formation from
a competing voiced comparative label.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing voiced comparative label | *lábbaz | not the form followed for the OE weak-noun derivation | broader comparative background | useful as a competing label, but not the source-based choice used here |
| selected weak masculine noun | *láppô | regular output: _lappa_ | _lappa_ | exact match between formation and attested OE noun |
| attested OE variant line | same noun family | _læppa_, _leappan_ | _læppa_ / _leappan_ | useful control forms within the same OE tradition |

### laugh — OE _hliehhan_

\index[oe]{hliehhan@\emph{hliehhan}}
\index[pgmc]{lakana@*lákaną}
\index[pgmc]{xlaxjana@*xláxjaną}

Derivation: citation reconstruction _\*lákaną_; form followed here _\*xláxjaną_ > _hliehhan_ (early analogy).

#### Derivation trace

Proto input: _\*xláxjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.470\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.470\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*xláxxjaną} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xlæxxjaną} \\
OE Breaking & \emph{*xleaxxjaną} \\
OE Velar Fricative Palatalization & \emph{*xleaxçjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xleaxçjan} \\
OE Secondary Nasalization & \emph{*xleaxçjąn} \\
OE I Umlaut & \emph{*xliexçjąn} \\
OE Weak Tail Reduction & \emph{*xliexçjan} \\
OE J Loss After Heavy & \emph{*xliexçan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hliehhan_

#### Reconstruction and comparative evidence

The wider Germanic family includes a non-j branch represented here by the
citation label _\*lákaną_, while the derivational input _\*xláxjaną_ reflects the
j-present line behind Old English _hliehhan_.

This branch supplies the geminate fricative and
the vowel development characteristic of the Old English verb. The comparative
family label and the OE-facing input are therefore related but not identical.

#### Old English evidence

Bosworth-Toller records _hlihhan_ as the verb 'to laugh'
[@BosworthToller1898, 551]. Clark Hall cross-references _hlæhan_,
_hlehhan_, and _hlihhan_ to _hliehhan_ [@ClarkHall1960, 160-161]. Bright's
glossary likewise gives _hlihhan (hliehhan, hlyhhan)_
[@BrightCassidyRingler1971, 315]. The target of this entry is the West Saxon
_hliehhan_.

The variants belong to the same background, but the attested lemma _hliehhan_
supplies the evidence followed here.

#### Development to Old English

From _\*xláxjaną_, West Germanic j-gemination yields the doubled consonant
[@Campbell1959, §407]. Ringe and Taylor derive Old English _hliehhan_ from the
j-present branch via breaking before the palatalized geminate
[@RingeTaylor2014, 240]. They separately compare the related noun _hleahtor_
as the outcome of _\*hlahtraz_ [@RingeTaylor2014, 328].

#### Branch comparison

The comparison below sets the relevant forms side by side. It separates the wider non-j family label from
the j-present branch actually reflected in Old English.

| Formation / branch | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| wider non-j family | *lákaną | comparative background outside the selected OE line | wider family context | useful family label, but not the direct source of _hliehhan_ |
| selected j-present branch | *xláxjaną | regular output: _hliehhan_ | _hliehhan_ | exact match between branch and attested OE lemma |
| attested OE variants | same OE verb line | _hlæhhan_, _hlehhan_ | _hlæhhan_ / _hlehhan_ | genuine variant evidence, but secondary to the form compared here |

### loam — OE _lām_

\index[oe]{lam@\emph{lām}}
\index[pgmc]{laima@*láimą}
\index[pgmc]{laimon@*laimōn}

Derivation: citation reconstruction _\*laimōn_; form followed here _\*láimą_ > _lām_ (early analogy).

#### Derivation trace

Proto input: _\*láimą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*lāmą} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*lām} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lām_

#### Reconstruction and comparative evidence

The inherited comparative noun is given as _\*laimōn_ or _\*laiman-_, and both
Orel and Kroonen identify Old English _lām_ as a neuter reflex of that family
[@Orel2003, 272; @Kroonen2013, 363]. The form followed here, _\*láimą_, differs from the
comparative headword because it represents the stem class that matches the Old
English noun most directly.

This is therefore a class shift within the history of the English branch rather
than a dispute about the OE target itself.

#### Old English evidence

Old English dictionaries record the noun as _lām_, a neuter word for 'loam,
clay, mud' [@BosworthToller1898, 604; @ClarkHall1960, 196]. The target is an attested
citation form rather than a reconstructed comparator.

The relevant question is not whether _lām_ is Old English, but which inherited
formation best accounts for that attested neuter noun.

#### Development to Old English

From _\*láimą_, regular monophthongization of _ai_ and the later loss of the
final nasal syllable yield _lām_. With that OE-facing input, the phonological
development is straightforward.

#### Class comparison

The comparison below sets the inherited comparative n-stem label beside the
OE-facing stem class used to derive the attested noun.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited comparative noun | *laimōn | comparative family background | wider family context | useful headword, but not the direct OE-facing input |
| OE-facing stem class followed here | *láimą | regular output: _lām_ | _lām_ | exact match between the form followed here and the attested OE noun |

### lung — OE _lungen_

\index[oe]{lungen@\emph{lungen}}
\index[pgmc]{lunganjo@*lúnganjō}
\index[pgmc]{lungo@*lungō}

Derivation: citation reconstruction _\*lungō_; form followed here _\*lúnganjō_ > _lungen_ (early analogy).

#### Derivation trace

Proto input: _\*lúnganjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.470\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.470\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
PWGmc J Gemination & \emph{*lúngannjō} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.24\linewidth}@{\hspace{0.25em}}}
NWGmc Final Long O Raising & \emph{*lúngannju} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*lúngennju} \\
OE High Vowel Apocope & \emph{*lúngennj} \\
OE J Loss After Heavy & \emph{*lúngenn} \\
OE Final Geminate Simplification & \emph{*lúngen} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lungen_

#### Reconstruction and comparative evidence

Kroonen treats the basic noun as _\*lungōn-_ and also cites an OE-facing
derivative _\*lungunjō-_, continued by Old English _lungen_ and close West
Germanic cognates [@Kroonen2013, 384]. The form followed here, _\*lúnganjō_, models that
derived feminine formation rather than the base noun. The notation differs
slightly from Kroonen's _\*lungunjō-_, but both point to the same derived
feminine line.

The difference between the citation label and the derivational input is therefore
derivational. Old English _lungen_ is not a direct reflex of the bare base noun
_\*lungō_; it belongs to an expanded feminine formation.

#### Old English evidence

Old English dictionaries record the noun as _lungen_, with inflected forms such
as _lungenne_ and _lungena_ [@BosworthToller1898, 634]. Clark Hall also preserves a
small family of compounds such as _lungenādl_, _lungensealf_, and _lungenwyrt_
[@ClarkHall1960, 191].

The target is an attested Old English lexeme with its own paradigm, not a
rescued inflectional cell.

#### Development to Old English

From the selected derived input, the expected derivational consonant and vowel
adjustments lead to _lungen_. Once the expanded feminine formation is chosen,
the Old English outcome is regular.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the base noun from the derived
feminine formation reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| base noun | *lungō | base-noun outcome without the OE derivative suffix | broader family context | useful headword, but not the direct source of _lungen_ |
| derived OE-facing formation | *lúnganjō | regular output: _lungen_ | _lungen_ | exact match between the derived formation and the attested OE noun |
| Kroonen's cited derivative | _\*lungunjō-_ | comparative support for the same OE-facing formation | _lungen_ and cognate set | supports the derived feminine formation, with notation differing from the normalized input form used here |

### navel — OE _nafola_

\index[oe]{nafola@\emph{nafola}}
\index[pgmc]{nablo@*nablô}
\index[pgmc]{nabulo@*nábulô}

Derivation: citation reconstruction _\*nablô_; form followed here _\*nábulô_ > _nafola_ (early analogy).

#### Derivation trace

Proto input: _\*nábulô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*nábolô} \\
Anglo Frisian Brightening & \emph{*næbolô} \\
OE A Restoration & \emph{*nabolô} \\
PGmc B Allophony & \emph{*naβolô} \\
OE Unstressed Long Vowel Shortening & \emph{*naβola} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nafola_

#### Reconstruction and comparative evidence

Kroonen instead gives a nasal-suffix navel formation with Old English [_nafela_]{.iv lang=oe sort=nafela role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6499"}
among its reflexes [@Kroonen2013, 420], while Ringe and Taylor give the
derivational pathway _\*nabulō_ > _\*næbula_ > _nafola_ [@RingeTaylor2014, 270]. The
difference is one of stage and notation rather than of lexeme identity: the
derivational input [_\*nábulô_]{.iv lang=pgmc sort=nabulo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6503"} is the pre-syncope form needed for the Old English
development.

For the Old English comparison, the crucial point is simply that the pre-OE form
still contains a medial vowel.

#### Old English evidence

Ringe and Taylor note the early West Saxon shift [_nafola_]{.iv lang=oe sort=nafola role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6511"} > [_nafela_]{.iv lang=oe sort=nafela role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6511"}
[@RingeTaylor2014, 336]. Campbell likewise records _nafela_ beside Corpus
[_nabula_]{.iv lang=oe sort=nabula role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6513"} [@Campbell1959, §159]. The target of this entry is the nominative
singular [_nafola_]{.iv lang=oe sort=nafola role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6514"}, the form that matches the selected derivational pathway
most directly.

[_nafela_]{.iv lang=oe sort=nafela role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6517"} is the better-known later West Saxon spelling, while [_nabula_]{.iv lang=oe sort=nabula role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6517"} preserves
a less reduced medial vowel. These forms belong to the same lexical history, but
this entry is centered on [_nafola_]{.iv lang=oe sort=nafola role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6519"}.

#### Development to Old English

Ringe and Taylor give the pre-OE line _\*nabulō_ > _\*næbula_ > OE _nafola_
[@RingeTaylor2014, 270]. The trace represents that same development with
stress-marked notation and explicit intermediate weakening. Intervocalic _b_
then surfaces as _f_, and final weak-tail shortening gives _nafola_.

The medial vowel is still present when A-restoration applies. That is why the
selected pre-syncope input differs from the syncopated comparative headword.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the comparative citation form from
the pre-syncope input and from the later OE spellings.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| syncopated comparative headword | [_\*nablô_]{.iv lang=pgmc sort=nablo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6538"} | reduced _næfla_-type outcome rather than [_nafola_]{.iv lang=oe sort=nafola role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6538"} | not the Old English form here | useful citation form, but too reduced for the pathway modeled here |
| selected pre-syncope input | [_\*nábulô_]{.iv lang=pgmc sort=nabulo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6539"} | regular output: [_nafola_]{.iv lang=oe sort=nafola role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6539"} | [_nafola_]{.iv lang=oe sort=nafola role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6539"} | exact match between derivational input and target |
| later OE reduction stages | same lexical history | attested [_nafela_]{.iv lang=oe sort=nafela role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6540"}; Corpus [_nabula_]{.iv lang=oe sort=nabula role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6540"} | [_nafela_]{.iv lang=oe sort=nafela role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6540"} / [_nabula_]{.iv lang=oe sort=nabula role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6540"} | related OE spellings, but not the chosen comparator |

### neck — OE _hnecca_

\index[oe]{hnecca@\emph{hnecca}}
\index[pgmc]{xnakkaz@*xnákkaz}
\index[pgmc]{xnekko@*xnékkô}

Derivation: citation reconstruction _\*xnákkaz_; form followed here _\*xnékkô_ > _hnecca_ (early analogy).

#### Derivation trace

Proto input: _\*xnékkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*xnékka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hnecca_

#### Reconstruction and comparative evidence

The noun belongs to an ablauting n-stem family. Kroonen reconstructs a paradigm
with nominative _\*hnekkō_, genitive _\*hnukkaz_, and accusative plural
_\*hnakkuns_, and he places Old English _hnecca_ among the e-grade descendants
[@Kroonen2011, 167]. Kluge-Seebold likewise identifies _ae. hnecca_ as an ablaut
partner of the a-grade _Nacken_ family [@KlugeSeebold2011, 347].

A competing comparative label [_\*xnákkaz_]{.iv lang=pgmc sort=xnakkaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6596"} belongs to the wider family, and Orel
also gives an a-grade headword line [@Orel2003, 218]. The derivational input
[_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6598"}, however, is the form that matches the Old English branch.

#### Old English evidence

Clark Hall records the weak masculine noun _hnecca_ [@ClarkHall1960, 162].
Bosworth-Toller likewise records _hnecca_ [@BosworthToller1898, 567]. The target is therefore an attested
citation form, not an oblique cell or a reconstructed lemma.

The phonological question is upstream of the Old English evidence. The attested
noun already shows that the branch continued an e-grade form rather than the
a-grade seen in much of the continental material.

#### Development to Old English

From [_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6612"}, the derivation is straightforward. The trace shortens the final
long vowel to _\*xnékka_, and Old English orthography gives [_hnecca_]{.iv lang=oe sort=hnecca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6613"}.

The derivation depends on the earlier selection of the e-grade weak-noun form
continued by Old English.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the wider a-grade family from the
selected e-grade Old English branch.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing comparative label | [_\*xnákkaz_]{.iv lang=pgmc sort=xnakkaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6625"} | broader a-grade family rather than the selected OE source | continental [_Nacken_]{.iv lang=german sort=nacken role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6625"} line | useful family label, but not the input followed for the Old English derivation |
| weak noun with a-grade | [_\*xnakkô_]{.iv lang=pgmc sort=xnakko role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6626"} | expected [_hnacca_]{.iv lang=oe sort=hnacca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6626"} type outcome | [_hnacca_]{.iv lang=oe sort=hnacca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6626"} | fixes the class, but not the vowel grade |
| selected e-grade nominative | [_\*xnékkô_]{.iv lang=pgmc sort=xnekko role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6627"} | regular output: [_hnecca_]{.iv lang=oe sort=hnecca role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6627"} | [_hnecca_]{.iv lang=oe sort=hnecca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6627"} | exact match between derivational input and attested OE noun |
| oblique paradigm background | [_\*hnukkaz_]{.iv lang=pgmc sort=hnukkaz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6628"}, [_\*hnakkuns_]{.iv lang=pgmc sort=hnakkuns role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6628"} | ON/OHG/German a-grade continuation | [_hnakki_]{.iv lang=on sort=hnakki role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6628"} / [_Nacken_]{.iv lang=german sort=nacken role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6628"} | shows the wider ablaut family, but not the chosen OE branch |

### needle — OE _nǣdl_

\index[oe]{naedl@\emph{nǣdl}}
\index[pgmc]{nedlo@*nḗðlō}
\index[pgmc]{nethlo@*nḗθlō}

Derivation: citation reconstruction _\*nḗθlō_; form followed here _\*nḗðlō_ > _nǣdl_ (early analogy).

#### Derivation trace

Proto input: _\*nḗðlō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*nḗdlō} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*nḗdlu} \\
\mbox{NWGmc Long E Lowering} & \emph{*nǣdlu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*nǣdl} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nǣdl_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the word as a voiced/voiceless alternant, citing
PGmc _\*nēþlō_, _\*nēdlō-_ 'needle' ... > OE _nédl_ [@RingeTaylor2014, 329]. The
form followed here, [_\*nḗðlō_]{.iv lang=pgmc sort=nedlo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6685"}, is the voiced Verner-grade form used for the Old
English comparison, while the citation form [_\*nḗθlō_]{.iv lang=pgmc sort=nethlo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6686"} remains the broader
lexeme label.

The development discussed here follows the Ringe-Taylor alternant framework.

#### Old English evidence

Clark Hall records the attested citation form _nǣdl_ [@ClarkHall1960, 210].
Campbell lists _nédl_ among the expected unbroken forms after _t_ and _d_
[@Campbell1959, §367]. Hogg also includes _nidi_ / _nǣdl_ in the same broader
cluster history [@Hogg1992, 95].

The target is therefore an attested citation form. No oblique-cell substitution
is involved in this entry.

#### Development to Old English

Ringe and Taylor give the historical line _\*nēþlō_, _\*nēdlō-_ ... > OE _nédl_
[@RingeTaylor2014, 329]. Campbell likewise lists _nédl_ among the expected
unbroken forms after _t_ and _d_ [@Campbell1959, §367]. The trace expresses the
same pathway with the voiced alternant followed here for the Old English comparison.

The essential choice lies in which Proto-Germanic alternant is taken as the
starting point. Once the voiced form is chosen, the rest of the pathway is
regular.

#### Alternant comparison

The comparison below sets the relevant forms side by side. It separates the broader citation headword from
the voiced alternant used for Old English.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative voiceless headword | [_\*nḗθlō_]{.iv lang=pgmc sort=nethlo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6719"} | broader word-family label rather than the OE-facing alternant | _\*nēþlō_ line | useful citation form, but not the derivational input for the Old English comparison |
| voiced Verner alternant followed here | [_\*nḗðlō_]{.iv lang=pgmc sort=nedlo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6720"} | regular output: [_nǣdl_]{.iv lang=oe sort=naedl role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6720"} | [_nǣdl_]{.iv lang=oe sort=naedl role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6720"} | exact match between the form followed here and the attested OE noun |
| later hardening stage | *nḗdlō | intermediate pre-OE stage in the same derivation | _nǣdl_ | genuine stage in the pathway, but not the Proto-Germanic form followed here |

### nose — OE _nosu_

\index[oe]{nosu@\emph{nosu}}
\index[pgmc]{naso@*nasō}
\index[pgmc]{nuso@*núsō}

Derivation: citation reconstruction _\*nasō_; form followed here _\*núsō_ > _nosu_ (early analogy).

#### Derivation trace

Proto input: _\*núsō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*nósō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*nósu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _nosu_

#### Reconstruction and comparative evidence

Kroonen reconstructs a Germanic ablaut pair _\*nasō-_ ~ _\*nusō-_ and adds that the
root _\*nus-_ is likely to have arisen as a secondary zero grade after a
remodeling of the older paradigm [@Kroonen2013, 423]. Campbell is more specific for
Old English, citing _nosu_ < _\*nusō_ [@Campbell1959, 44].

The citation reconstruction _\*nasō_ is therefore best treated as the full-grade
comparative headword, while the derivational input _\*núsō_ represents the remodeled
zero-grade line continued by the Old English form discussed here. Orel's _\*nasō_ ... OE _nasu_ preserves the competing full-grade notation and shows that the two
lines should not be collapsed without comment [@Orel2003, 320].

#### Old English evidence

_Nosu_ is an attested Old English noun. Ringe and Taylor list it among the few
surviving early Old English feminine u-stems [@RingeTaylor2014, 385]. Clark Hall
likewise gives _nosu f._, with genitive-dative singular _nosa_, and cross-refers
_nasu_ to _nosu_ [@ClarkHall1960, 810].

The selected OE target is therefore attested _nosu_, not a reconstructed
placeholder. The lexicographical record also gives _nasu_ for the full-grade
side of the tradition.

#### Development to Old English

From _\*núsō_, the regular path is the one documented by the current trace:
_\*núsō_ > _\*nósō_ > _\*nósu_ > _nosu_. The early special step lies in the choice of the
zero-grade input, not in any late Old English repair.

With that input chosen, the OE development is straightforward. The full-grade
line behind _\*nasō_ instead points toward _nasu_, not to the form treated here.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the full-grade comparative line
from the remodeled zero-grade input that yields the Old English form.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| full-grade comparative line | *nasō | expected full-grade continuation _nasu_ | _nasu_ | useful comparative background, but not the Old English-facing input |
| remodeled zero-grade line | *núsō | regular output: _nosu_ | _nosu_ | exact match between derivational input and attested OE noun |

### sap — OE _sæp_

\index[oe]{saep@\emph{sæp}}
\index[pgmc]{sapa@*sápą}
\index[pgmc]{sapon@*sapōn}

Derivation: citation reconstruction _\*sapōn_; form followed here _\*sápą_ > _sæp_ (early analogy).

#### Derivation trace

Proto input: _\*sápą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*sæpą} \\
OE Heavy Syllable Nasal Apocope & \emph{*sæp} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sæp_

#### Reconstruction and comparative evidence

The comparative sources do not give one uniform inherited stem. Kroonen
preserves the word family as _\*saf_/ppan-, with Old English _sæp_ m.
[@Kroonen2013, 420]. Orel preserves the comparative notation _\*sapōn_ ~ _\*sapan_
[@Orel2003, 319].

The derivational input [_\*sápą_]{.iv lang=pgmc sort=sapa role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6866"} therefore does not replace those comparative labels.
It identifies the OE-facing stem shape that yields the attested noun treated
here.

#### Old English evidence

Clark Hall records [_sæp_]{.iv lang=oe sort=saep role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6872"} (e) n. [@ClarkHall1960, 247]. The target is therefore
an attested neuter Old English noun. Orel's plain _sap_ notation belongs to
comparative normalization, not to the spelling adopted here for the Old English
form [@Orel2003, 319].

#### Development to Old English

From [_\*sápą_]{.iv lang=pgmc sort=sapa role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6879"}, Anglo-Frisian brightening yields _sæ_, and heavy-syllable nasal
apocope then produces [_sæp_]{.iv lang=oe sort=saep role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6880"}. That is the regular path documented by the current
trace.

The competing comparative lines do not give the same result. The inherited
n-stem notation [_\*sapōn_]{.iv lang=pgmc sort=sapon role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6884"} yields [_sape_]{.iv lang=oe sort=sape role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6884"}, while an i-stem continuation from the
[_\*sapi-_]{.iv lang=pgmc sort=sapi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6885"} line leads to [_sep_]{.iv lang=oe sort=sep role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6885"} / [_sepe_]{.iv lang=oe sort=sepe role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6885"} rather than to [_sæp_]{.iv lang=oe sort=saep role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6885"}. The special step in
this entry is therefore the early stem choice, not a late OE paradigm-cell
selection.

#### Stem comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative stem lines
from the Old English-facing input.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative n-stem line | [_\*sapōn_]{.iv lang=pgmc sort=sapon role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6896"} | local comparator output: [_sape_]{.iv lang=oe sort=sape role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6896"} | [_sape_]{.iv lang=oe sort=sape role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6896"} | useful comparative background, but not the source of attested _sæp_ |
| inferred i-stem comparator from _\*sapi-_ | [_\*sapiz_]{.iv lang=pgmc sort=sapiz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6897"} | local comparator output: [_sepe_]{.iv lang=oe sort=sepe role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6897"} | [_sepe_]{.iv lang=oe sort=sepe role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6897"} | confirms that an i-triggering stem does not reach the target |
| selected a-stem input | [_\*sápą_]{.iv lang=pgmc sort=sapa role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6898"} | regular output: [_sæp_]{.iv lang=oe sort=saep role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6898"} | [_sæp_]{.iv lang=oe sort=saep role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6898"} | exact match between derivational input and attested OE noun |

### sea — OE _sǣ_

\index[oe]{sae@\emph{sǣ}}
\index[pgmc]{sai@*sái}
\index[pgmc]{saiwiz@*sáiwiz}

Derivation: citation reconstruction _\*sái_; form followed here _\*sáiwiz_ > _sǣ_ (early analogy).

#### Derivation trace

Proto input: _\*sáiwiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*sāwiz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*sāwi} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE W Loss Before I & \emph{*sāi} \\
OE I Umlaut & \emph{*sǣi} \\
\mbox{OE High Vowel Apocope} & \emph{*sǣ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sǣ_

#### Reconstruction and comparative evidence

Kroonen gives the noun in stem notation as _\*saiwi-_, an i-stem whose English
reflex is cited as OE [_sæ_]{.iv lang=oe sort=sae role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6955"} [@Kroonen2013, 423]. Ringe and Taylor write the fuller
form [_\*saiwiz_]{.iv lang=pgmc sort=saiwiz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6956"} and derive it through _\*sawi_ > _\*sei_ > OE _sǣ_
[@RingeTaylor2014, §6.7.1]. The comparative headword is therefore shorter than
the form required for the English history: [_\*sái_]{.iv lang=pgmc sort=sai role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6958"} names the lexeme, but
[_\*sáiwiz_]{.iv lang=pgmc sort=saiwiz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6959"} preserves the medial _\*w_ and the final high vowel that control the
later development.

#### Old English evidence

The Old English noun is the ordinary word for ‘sea’. Kroonen cites it as [_sæ_]{.iv lang=oe sort=sae role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6964"};
the normalized form here is [_sǣ_]{.iv lang=oe sort=sae role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6965"} [@Kroonen2013, 423]. Campbell likewise treats
_sea_ as continuing the same _\*saiui-_ > _\*sǣi_ history, with loss of _u_/_w_
before _i_ [@Campbell1959, §406].

#### Development to Old English

Once the fuller i-stem input is chosen, the development is regular. After
Proto-West-Germanic monophthongization _\*sáiwiz_ > _\*sāwiz_ and final _\*-z_ loss
_\*sāwiz_ > _\*sāwi_, the non-initial _\*w_ disappears before unstressed _\*i_, and
the following high vowel fronts the root vowel before final apocope. The
documented chain is _\*sáiwiz_ > _\*sāwiz_ > _\*sāwi_ > _\*sāi_ > _\*sǣi_ > _sǣ_
[@RingeTaylor2014, §6.7.1; @Campbell1959, §406].

#### Stem and stage comparison

The comparison below sets the relevant forms side by side. It separates the abbreviated comparative
headword from the fuller i-stem input that yields the Old English form.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| abbreviated comparative headword | [_\*sái_]{.iv lang=pgmc sort=sai role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6985"} | too short to preserve the _\*w_ ... _\*i_ environment needed for the documented chronology | [_sǣ_]{.iv lang=oe sort=sae role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6985"} | useful comparative label, but not the Old English-facing input |
| selected i-stem input | [_\*sáiwiz_]{.iv lang=pgmc sort=saiwiz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6986"} | documented regular output: [_sǣ_]{.iv lang=oe sort=sae role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6986"} | [_sǣ_]{.iv lang=oe sort=sae role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:6986"} | exact match between derivational input and Old English target |

### sieve — OE _sife_

\index[oe]{sife@\emph{sife}}
\index[pgmc]{sibaz@*síbaz}
\index[pgmc]{sibi@*síbi}

Derivation: citation reconstruction _\*síbaz_; form followed here _\*síbi_ > _sife_ (early analogy).

#### Derivation trace

Proto input: _\*síbi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*síβi} \\
OE Med Unstressed I Lowering1 & \emph{*síβe} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sife_

#### Reconstruction and comparative evidence

Kluge-Seebold gives wg. _\*sibi-_ n. ... ae. _sife_, and Campbell groups [_sife_]{.iv lang=oe sort=sife role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7037"}
with short neuter i-stems such as _spere_ [@KlugeSeebold2011, 847;
@Campbell1959, §609]. The older morphological background is the s-stem
_\*sib-iz_, but the derivational input is the normalized i-stem form [_\*síbi_]{.iv lang=pgmc sort=sibi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7040"}.

Kroonen's nearby _\*sebjō-_ entry belongs to the separate kinship lexeme that
yields Old English [_sibb_]{.iv lang=oe sort=sibb role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7043"}, not to the sieve word. Orel's [_\*sibaz_]{.iv lang=pgmc sort=sibaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7043"} ... OE [_sife_]{.iv lang=oe sort=sife role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7043"}
preserves a broader handbook notation, but that a-stem shape does not fit the
Old English form treated here [@Orel2003, 328].

#### Old English evidence

Clark Hall gives [_sibi_]{.iv lang=oe sort=sibi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7049"} (GL) ... = [_sife_]{.iv lang=oe sort=sife role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7049"} and also [_sife_]{.iv lang=oe sort=sife role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7049"} n. ‘sieve’
[@ClarkHall1960, 263]. Campbell likewise cites Corpus Glossary _sibi_ and
treats _sife_ as a short neuter i-stem [@Campbell1959, §§444, 609]. The
normalized Old English target is therefore _sife_, while _sibi_ is an attested
earlier spelling rather than a separate lexeme.

#### Development to Old English

From [_\*síbi_]{.iv lang=pgmc sort=sibi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7057"}, the regular derivation gives _\*síβi_ > _\*síβe_ > [_sife_]{.iv lang=oe sort=sife role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7057"}. Medial _b_
is realized as a spirant and later written _f_, while the final unstressed _i_
lowers to _e_. The older s-stem background _\*sib-iz_ explains the morphology,
but the derivational input [_\*síbi_]{.iv lang=pgmc sort=sibi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7060"} is the immediate pre-Old-English form.

#### Stem comparison

The comparison below sets the relevant forms side by side. It distinguishes the accepted i-stem line from
its rejected competitors.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| ja-stem kinship line | Kroonen _\*sebjō-_ / comparator [_\*sibja_]{.iv lang=pgmc sort=sibja role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7069"} | OE [_sibb_]{.iv lang=oe sort=sibb role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7069"} | [_sibb_]{.iv lang=oe sort=sibb role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7069"} | separate lexeme, not the target treated here |
| a-stem handbook line | [_\*síbaz_]{.iv lang=pgmc sort=sibaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7070"} | expected [_sif_]{.iv lang=oe sort=sif role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7070"} | [_sif_]{.iv lang=oe sort=sif role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7070"} | wrong ending for the attested noun |
| selected i-stem line from older _\*sib-iz_ | [_\*síbi_]{.iv lang=pgmc sort=sibi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7071"} | documented regular output: [_sife_]{.iv lang=oe sort=sife role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7071"} | [_sife_]{.iv lang=oe sort=sife role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7071"}; early spelling [_sibi_]{.iv lang=oe sort=sibi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7071"} | exact match between derivational input and Old English evidence |

### spare — OE _sparian_

\index[oe]{sparian@\emph{sparian}}
\index[pgmc]{sparena@*sparēną}
\index[pgmc]{sparojana@*spárōjaną}

Derivation: citation reconstruction _\*sparēną_; form followed here _\*spárōjaną_ > _sparian_ (early analogy).

#### Derivation trace

Proto input: _\*spárōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*spærōjaną} \\
OE A Restoration & \emph{*sparōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sparōjan} \\
OE Secondary Nasalization & \emph{*sparōjąn} \\
OE I Umlaut & \emph{*sparējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*sparejąn} \\
OE Weak Tail Reduction & \emph{*sparejan} \\
OE Intervocalic J Vocalization & \emph{*spareian} \\
OE Unstressed EI Contraction & \emph{*sparian} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sparian_

#### Reconstruction and comparative evidence

Kroonen keeps the inherited verb under class-III [_\*sparēn-_]{.iv lang=pgmc sort=sparen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7129"}
[@Kroonen2013, 465]. Orel similarly preserves [_\*sparēnan_]{.iv lang=pgmc sort=sparenan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7130"} [@Orel2003, 362]. Ringe
and Taylor, however, reconstruct [_\*sparai-_]{.iv lang=preoe sort=sparai source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7131"} ~ [_\*sparja-_]{.iv lang=preoe sort=sparja source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7131"} for the English branch
and derive the citation verb from a class-II line [@RingeTaylor2014, 162, 191].
The derivational input [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7133"} therefore represents the refashioned class-II
formation behind Old English [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7134"}, while the citation reconstruction
[_\*sparēną_]{.iv lang=pgmc sort=sparena source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7135"} remains the inherited comparative headword.

#### Old English evidence

Campbell says that [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7139"} does not show the ordinary class-III
characteristics, but the Ritual forms, normalized here as [_spæria_]{.iv lang=oe sort=spaeria source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7140"}, [_spær_]{.iv lang=oe sort=spaer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7140"}, and
[_spærede_]{.iv lang=oe sort=spaerede source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7141"}, together with Vespasian Psalter [_spearad_]{.iv lang=oe sort=spearad source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7141"}, point to primitive Old
English forms both with and without back vowels [@Campbell1959, §764]. Brunner likewise records
Northumbrian [_spæria_]{.iv lang=oe sort=spaeria source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7143"}, [_spærede_]{.iv lang=oe sort=spaerede source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7143"} beside common Old English [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7143"} and
Vespasian Psalter [_spearad_]{.iv lang=oe sort=spearad source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7144"} [@SieversBrunner1965, §364 Anm. 11]. The citation
form treated here is [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7145"}; the Anglian forms are relics of the older
formation, not alternative headwords of equal status.

#### Development to Old English

Once the class-II formation [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7150"} is chosen, the remaining development is
regular. The regular derivation shows brightening, restoration of _a_ before the
back vocalism of the suffix, later i-mutation within the weak ending, weak-tail
reduction, and contraction to [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7153"}. By contrast, Brunner's rule against
further apocope of final _-e_ explains why Ritual [_spær_]{.iv lang=oe sort=spaer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7154"} cannot be the regular
continuation of inherited [_\*spárē_]{.iv lang=preoe sort=spare source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7155"} [@SieversBrunner1965, §150].

#### Formation comparison

The comparison below sets the relevant forms side by side. It contrasts the inherited class-III formation
with the refashioned class-II one that yields the citation verb.

| Formation / comparison | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited class-III infinitive | [_\*spárēną_]{.iv lang=pgmc sort=sparena source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7164"} | paradigm comparison / probe output: [_sparen_]{.iv lang=oe sort=sparen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7164"} | [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7164"} | wrong class and wrong ending for the citation verb |
| inherited class-III imperative singular | [_\*spárē_]{.iv lang=preoe sort=spare source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7165"} | paradigm comparison / probe output: [_spære_]{.iv lang=oe sort=spaere source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7165"} | Ritual [_spær_]{.iv lang=oe sort=spaer source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7165"} | loss of final _-e_ is not regular, so the relic form cannot control the entry |
| inherited class-III finite present | [_\*spárēθi_]{.iv lang=preoe sort=sparethi source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7166"} | paradigm comparison / probe output: [_spæreþ_]{.iv lang=oe sort=spaereth source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7166"} | [_spearad_]{.iv lang=oe sort=spearad source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7166"} | attested form is mixed, not a direct continuation of the inherited cell |
| selected class-II formation | [_\*spárōjaną_]{.iv lang=pgmc sort=sparojana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7167"} | documented regular output: [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7167"} | [_sparian_]{.iv lang=oe sort=sparian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7167"} | exact match between derivational input and Old English citation form |

### staff — OE _stæf_

\index[oe]{staef@\emph{stæf}}
\index[pgmc]{stabaz@*stábaz}
\index[pgmc]{stabiz@*stábiz}

Derivation: citation reconstruction _\*stábiz_; form followed here _\*stábaz_ > _stæf_ (early analogy).

#### Derivation trace

Proto input: _\*stábaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*stába} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*stáb} \\
Anglo Frisian Brightening & \emph{*stæb} \\
PGmc B Allophony & \emph{*stæβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stæf_

#### Reconstruction and comparative evidence

The comparative dictionaries do not give one uniform stem class. Kroonen
reconstructs an a-stem _\*staba-_ [@Kroonen2013, 471]. Orel writes [_\*stábiz_]{.iv lang=pgmc sort=stabiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7222"} ~
[_\*stábaz_]{.iv lang=pgmc sort=stabaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7223"} [@Orel2003, 368]. A direct i-stem input in
_\*-iz_ would predict i-mutation in Old English, whereas the attested noun keeps
_æ_.

#### Old English evidence

The Old English noun itself is the ordinary citation form [_stæf_]{.iv lang=oe sort=staef role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7229"}. Luick lists
[_stæf_]{.iv lang=oe sort=staef role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7230"} among closed monosyllables with _æ_ [@Luick1914, 176]. Ringe and Taylor
pair singular [_stæf_]{.iv lang=oe sort=staef role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7231"} with plural [_stafas_]{.iv lang=oe sort=stafas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7231"} [@RingeTaylor2014, 193]. The
normalized form here is therefore _stæf_; later English _staff_ with _a_
belongs to a later stage of the word's history.

#### Development to Old English

With the selected a-stem input, the development is regular. Final _\*-z_
disappears, bare final _-a_ is lost, Anglo-Frisian brightening gives _æ_ in the
closed monosyllable, and medial _b_ surfaces as a fricative written _f_. The
documented chain is _\*stábaz_ > _\*stába_ > _\*stáb_ > _\*stæb_ > _stæf_. A direct
continuation of _\*stábiz_, by contrast, would produce i-mutated _stefe_ rather
than the attested singular.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the rejected i-stem line from the
selected a-stem input.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative i-stem line | [_\*stábiz_]{.iv lang=pgmc sort=stabiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7251"} | expected [_stefe_]{.iv lang=oe sort=stefe role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7251"} after i-mutation | [_stæf_]{.iv lang=oe sort=staef role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7251"} | wrong vowel for the attested singular |
| mixed comparative notation | Orel _\*stabiz_ ~ _\*stabaz_; Kluge _\*stabi-_/a- | source-level stem-class uncertainty | _stæf_ | useful comparative background, but not a single OE-facing input |
| selected a-stem input | [_\*stábaz_]{.iv lang=pgmc sort=stabaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7253"} | documented regular output: [_stæf_]{.iv lang=oe sort=staef role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7253"} | [_stæf_]{.iv lang=oe sort=staef role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7253"} | exact match between derivational input and Old English target |

### stem — OE _stefn_

\index[oe]{stefn@\emph{stefn}}
\index[pgmc]{stamnaz@*stámnaz}
\index[pgmc]{stebno@*stébnō}

Derivation: citation reconstruction _\*stámnaz_; form followed here _\*stébnō_ > _stefn_ (early analogy).

#### Derivation trace

Proto input: _\*stébnō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Final Long O Raising} & \emph{*stébnu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*stéβnu} \\
\mbox{OE High Vowel Apocope} & \emph{*stéβn} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _stefn_

#### Reconstruction and comparative evidence

The source tradition behind [_stefn_]{.iv lang=oe sort=stefn role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7306"} is not the same as the comparative label
[_\*stámnaz_]{.iv lang=pgmc sort=stamnaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7307"}. Ringe and Taylor cite _\*stebnō_ for the noun continued by
Gothic [_stibna_]{.iv lang=goth sort=stibna role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7308"} and Old English _stebn_ > _stefn_ > _stemn_ [@RingeTaylor2014,
330]. Orel likewise gives _\*stebnō_ ~ _\*stemnō_, whereas Kroonen prefers
_\*stimnō-_, and Fulk describes the etymology of _stefn, stemn_ as insecure
[@Orel2003, 374; @Kroonen2013, 480; @Fulk2018, §6.11 n. 6].

These forms belong to the Old English noun [_stefn_]{.iv lang=oe sort=stefn role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7313"} 'voice, sound'. The
derivational input [_\*stébnō_]{.iv lang=pgmc sort=stebno role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7314"} is therefore best treated as the OE-facing
transponent supported by that source tradition. It does not settle the deeper
comparative reconstruction implied by the citation label [_\*stámnaz_]{.iv lang=pgmc sort=stamnaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7316"}.

#### Old English evidence

Clark Hall records [_stefn_]{.iv lang=oe sort=stefn role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7320"} as the noun 'voice, sound' and cross-refers
[_stemn_]{.iv lang=oe sort=stemn role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7321"} to the same word [@ClarkHall1960, 276]. Ringe and Taylor give the OE
chronology directly as _stebn_ > _stefn_ > _stemn_ [@RingeTaylor2014, 330].

Bülbring and Luick treat [_stemn_]{.iv lang=oe sort=stemn role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7324"} as a later West Saxon development from
older [_stefn_]{.iv lang=oe sort=stefn role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7325"}, produced by _fn_ > _mn_ only after the earlier period of nasal
influence on _e_ [@Bulbring1902, §§62 Anm. 3, 445; @Luick1914, §75 Anm. 1].
The relevant comparison form is therefore the conservative [_stefn_]{.iv lang=oe sort=stefn role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7327"}, not the
later West Saxon doublet [_stemn_]{.iv lang=oe sort=stemn role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7328"}.

#### Development to Old English

From _\*stébnō_, raising of final long _ō_ gives a _\*stébnu_ stage.
Regular fricativization of _b_ before _n_ then yields _\*stéβnu_, and loss
of the final high vowel leaves _\*stéβn_, written _stefn_ in Old English.
The later form _stemn_ belongs to a separate West Saxon assimilation after
this stage [@RingeTaylor2014, 330; @Bulbring1902, §445].

#### Source comparison

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| [_\*stámnaz_]{.iv lang=pgmc sort=stamnaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7342"} | comparative citation label for the broader stem/trunk family | does not itself control the _stefn_ derivation discussed here | broader lexical label only |
| [_\*stébnō_]{.iv lang=pgmc sort=stebno role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7343"} | voice-noun transponent | regular output: [_stefn_]{.iv lang=oe sort=stefn role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7343"} | Old English-facing input |
| [_stemn_]{.iv lang=oe sort=stemn role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7344"} | later attested West Saxon doublet | secondary form from _stefn_ by _fn_ > _mn_ | real OE variant, but not the selected comparator |

### swan — OE _swanes_

\index[oe]{swanes@\emph{swanes}}
\index[pgmc]{swanas@*swánas}
\index[pgmc]{swanaz@*swánaz}

Derivation: citation reconstruction _\*swánaz_; form followed here _\*swánas_ > _swanes_ (early analogy).

#### Derivation trace

Proto input: _\*swánas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*swánæs} \\
OE Unstressed AE Merger & \emph{*swánes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _swanes_

#### Reconstruction and comparative evidence

The Germanic noun is ordinarily cited as the masculine a-stem [_\*swánaz_]{.iv lang=pgmc sort=swanaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7395"}
[@Orel2003, 367]. The form followed here, _\*swánas_, is not a competing
lexeme reconstruction. It is the genitive singular [_\*swánas_]{.iv lang=pgmc sort=swanas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7397"} of the same paradigm.

The question here is therefore one of paradigm cell rather than stem history.
The citation form remains [_\*swánaz_]{.iv lang=pgmc sort=swanaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7400"} > [_swan_]{.iv lang=oe sort=swan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7400"}; the comparison form is the
genitive singular [_\*swánas_]{.iv lang=pgmc sort=swanas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7401"} > [_swanes_]{.iv lang=oe sort=swanes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7401"}.

#### Old English evidence

Bright's glossary records the ordinary noun as [_swan_]{.iv lang=oe sort=swan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7405"}, m. and also gives the
exact inflected form [_swanes_]{.iv lang=oe sort=swanes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7406"}, citing the phrase _swanes feðre_
[@BrightCassidyRingler1971, 441].

The target is therefore an attested Old English genitive singular, not a
reconstruction or the ordinary citation lemma.

#### Development to Old English

From _\*swánas_, Anglo-Frisian brightening gives _\*swánæs_, and
subsequent merger of unstressed _æ_ with _e_ yields _swanes_. The
comparison is straightforward once the genitive singular is chosen as the
relevant cell.

#### Paradigm-cell comparison

The comparison below sets the relevant forms side by side. It separates the ordinary citation form from the
selected inflected cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*swánaz_]{.iv lang=pgmc sort=swanaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7426"} | OE headword [_swan_]{.iv lang=oe sort=swan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7426"} | [_swan_]{.iv lang=oe sort=swan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7426"} | ordinary lexeme line |
| genitive singular | [_\*swánas_]{.iv lang=pgmc sort=swanas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7427"} | regular output: [_swanes_]{.iv lang=oe sort=swanes role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7427"} | [_swanes_]{.iv lang=oe sort=swanes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7427"} | attested cell |

### thousand — OE _þūsend_

\index[oe]{aerende@\emph{ærende}}
\index[oe]{thusend@\emph{þūsend}}
\index[pgmc]{thusendi@*θūs-èndi}
\index[pgmc]{thusendi@*θūsèndi}
\index[pgmc]{thusundi@*θūs-undī}

Derivation: citation reconstruction _\*θūs-undī_; form followed here _\*θūs-èndi_ > _þūsend_ (early analogy).

#### Derivation trace

Proto input: _\*θūsèndi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*θūsènd} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Strip Secondary Stress & \emph{*θūsend} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þūsend_

#### Reconstruction and comparative evidence

Kroonen reconstructs the Germanic numeral as [_\*þūsundī-_]{.iv lang=pgmc sort=thusundi role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7479"} and cites Old
English [_þūsend_]{.iv lang=oe sort=thusend role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7480"} among its continuations [@Kroonen2013, 554]. The
derivational input [_\*θūs-èndi_]{.iv lang=pgmc sort=thusendi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7481"} is not the same claim. It is an OE-oriented
transponent with the second-member vowel already resolved to _e_ and the final
high vowel already shortened for apocope.

The chronology must explain why Old English shows
[_þūsend_]{.iv lang=oe sort=thusend role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7486"} while related languages such as Old Saxon and Old High German keep
_u_ in the second syllable? [@Kroonen2013, 554].

#### Old English evidence

Old English _þūsend_ is an ordinary citation form, not a selected oblique or
paradigm cell. Campbell treats it as a neuter noun with normal case forms
[@Campbell1959, §689]. The problem lies in the internal history of the word, not
in its lexical status.

#### Development to Old English

If the old final _-ī_ had remained long enough to trigger ordinary double
umlaut, Campbell's rule would point toward a form of [_\*þȳsend_]{.iv lang=oe sort=thysend role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7499"} type rather
than attested [_þūsend_]{.iv lang=oe sort=thusend role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7500"} [@Campbell1959, §203]. Preserved root _ū_
therefore argues that the umlaut-triggering vowel was lost or neutralized before
the ordinary OE umlaut outcome could develop.

That early loss, however, does not by itself explain the medial _e_. Luick
compares the word with [_ærende_]{.iv lang=oe sort=aerende role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7505"} and later groups _thousand_ with forms
reshaped on that pattern [@Luick1914, §§198, 492]. Viredaz is more cautious,
arguing that Old English _e_ in this weak position may simply write schwa and so
need not prove a unique _ærende_-type analogy [@GermanicSlavicBaltic2025,
§2.1.4].

The selected transponent [_\*θūs-èndi_]{.iv lang=pgmc sort=thusendi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7511"} captures the OE-side state from which
the regular derivation reaches [_þūsend_]{.iv lang=oe sort=thusend role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7512"}.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the secure chronology from the more
interpretive account of the second-syllable vowel.

| Stage / interpretation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| surviving _-ī_ with ordinary double umlaut | [_\*þūsundī-_]{.iv lang=pgmc sort=thusundi role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7521"} treated as still umlaut-active in OE | would point toward [_\*þȳsend_]{.iv lang=oe sort=thysend role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7521"} | excluded by preserved _ū_ |
| early loss of the trigger without further reshaping | _\*þūsund-_ type | explains _ū_, but not why OE alone has medial _e_ | incomplete account |
| selected OE-oriented transponent | [_\*θūs-èndi_]{.iv lang=pgmc sort=thusendi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7523"} | regular output: [_þūsend_]{.iv lang=oe sort=thusend role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7523"} | selected modeling input |

### timber — OE _timber_

\index[oe]{timber@\emph{timber}}
\index[pgmc]{timbra@*tímbrą}
\index[pgmc]{timra@*tímrą}

Derivation: citation reconstruction _\*tímrą_; form followed here _\*tímbrą_ > _timber_ (early analogy).

#### Derivation trace

Proto input: _\*tímbrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*tímbr} \\
OE Epenthetic Vowel & \emph{*tímber} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _timber_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as [_\*timbra-_]{.iv lang=pgmc sort=timbra role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7574"} and cites Old English
[_timber_]{.iv lang=oe sort=timber role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7575"} among its continuations [@Kroonen2013, 517]. Ringe and Taylor
instead state the history from PGmc _\*timra_ through West Germanic
[_\*timbr_]{.iv lang=preoe sort=timbr role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7577"} to Old English [_timber_]{.iv lang=oe sort=timber role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7577"} [@RingeTaylor2014, 327].

The difference is therefore not over the Old English noun itself. It concerns
whether medial _b_ belongs in the comparative citation form or appears in an
early pre-Old-English stage of the cluster.

#### Old English evidence

Clark Hall lemmatizes the noun as [_timber_]{.iv lang=oe sort=timber role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7585"} and also records [_timbor_]{.iv lang=oe sort=timbor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7585"} as
a variant spelling [@ClarkHall1960, 294]. The Old English form is thus an ordinary
citation noun, not a selected oblique cell or a reconstructed convenience form.

#### Development to Old English

With the consonantal frame _timbr-_ in place, the rest of the development is
straightforward. Loss of final _-ą_ leaves _\*tímbr_, and epenthetic
_e_ in the final cluster yields _timber_. Ringe and Taylor's
_\*timra_ > _\*timbr_ > OE _timber_ and the handbook treatment of this epenthetic
vowel point to the same Old English result [@RingeTaylor2014, 327; @Campbell1959,
§§463-464].

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the comparative headword from the
OE-facing consonantal input.

| Formation or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Kroonen's comparative citation | [_\*timbra-_]{.iv lang=pgmc sort=timbra role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7605"} | already matches the consonantal frame of OE [_timber_]{.iv lang=oe sort=timber role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7605"} | closest comparative support for the derivational input |
| Ringe-Taylor citation line | [_\*timra_]{.iv lang=pgmc sort=timra role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7606"} > [_\*timbr_]{.iv lang=preoe sort=timbr role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7606"} | reaches the same OE noun through early cluster expansion | compatible comparative background |
| modeled input | [_\*tímbrą_]{.iv lang=pgmc sort=timbra role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7607"} | regular output: [_timber_]{.iv lang=oe sort=timber role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7607"} | Old English-facing input |

### wake — OE _wacan_

\index[oe]{wacan@\emph{wacan}}
\index[pgmc]{wakana@*wákaną}
\index[pgmc]{wakena@*wakēną}

Derivation: citation reconstruction _\*wakēną_; form followed here _\*wákaną_ > _wacan_ (early analogy).

#### Derivation trace

Proto input: _\*wákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wækaną} \\
OE A Restoration & \emph{*wakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wakan} \\
OE Secondary Nasalization & \emph{*wakąn} \\
OE Weak Tail Reduction & \emph{*wakan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wacan_

#### Reconstruction and comparative evidence

Kroonen gives the strong verb as _\*wakan-_ with Old English
[_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7662"} [@Kroonen2013, 568]. Ringe and Taylor separately derive Old English
[_wacian_]{.iv lang=oe sort=wacian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7663"} from weak _\*wakai-_ ~ _\*wakja-_ [@RingeTaylor2014, §3.3.2].

The difference is therefore lexical and class-based, not graphic. Strong
[_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7666"} 'wake up, arise' and weak [_wacian_]{.iv lang=oe sort=wacian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7666"} 'be awake, watch' belong to
related but distinct histories.

#### Old English evidence

Clark Hall lists [_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7671"} and [_wacian_]{.iv lang=oe sort=wacian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7671"} as separate headwords
[@ClarkHall1960, 338]. Bosworth-Toller cautions under
[_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7673"}: the simplex infinitive itself does not occur, its place seeming to
be taken by [_wæcnan_]{.iv lang=oe sort=waecnan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7674"} [@BosworthToller1898, 226].

The target [_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7676"} is therefore best understood as a normalized strong
headword for the verb family, not as a directly quoted simplex infinitive. It
still remains the correct Old English comparison form for the strong branch.

#### Development to Old English

With strong [_\*wákaną_]{.iv lang=pgmc sort=wakana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7682"}, Anglo-Frisian brightening first gives a form of the
_\*wækaną_ type. A-restoration then returns _a_, and the ordinary tail
reductions yield [_wacan_]{.iv lang=oe sort=wacan role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7684"}. The weak verb [_wacian_]{.iv lang=oe sort=wacian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7684"} belongs to a different
prehistory and is not the expected outcome of this input.

#### Class comparison

The comparison below sets the relevant forms side by side. It separates the strong and weak verb lines.

| Formation / class | Candidate input | OE outcome or comparison | Result |
| :--- | :--- | :--- | :--- |
| weak class-III / class-II branch | [_\*wakēną_]{.iv lang=pgmc sort=wakena role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7693"}, _\*wakai-_ ~ _\*wakja-_ | OE [_wacian_]{.iv lang=oe sort=wacian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7693"} and related weak forms | related lexeme, but not the target of this entry |
| strong class-VI branch | [_\*wákaną_]{.iv lang=pgmc sort=wakana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7694"} | regular output: [_wacan_]{.iv lang=oe sort=wacan role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7694"} | Old English-facing input |
| strong normalized headword | [_wacan_]{.iv lang=oe sort=wacan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7695"} | dictionary comparison form beside attested strong-family forms | correct Old English comparator, though not a directly quoted simplex infinitive |

### water — OE _wæter_

\index[oe]{waeter@\emph{wæter}}
\index[pgmc]{watna@*wátną}
\index[pgmc]{wator@*wátōr}

Derivation: citation reconstruction _\*wátną_; form followed here _\*wátōr_ > _wæter_ (early analogy).

#### Derivation trace

Proto input: _\*wátōr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Or Lowering & \emph{*wátar} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wætær} \\
OE Unstressed AE Merger & \emph{*wæter} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wæter_

#### Reconstruction and comparative evidence

Kroonen reconstructs a heteroclitic noun _\*watar-_ ~ _\*watan-_ and states that
the Proto-Germanic material points to _\*watōr_, _\*watenaz_
[@Kroonen2013, 616]. Ringe and Taylor likewise start from singular
_\*wator_ before the Old English branch [@RingeTaylor2014, §3.1.4].

The generalized comparative label is therefore broader than the singular
form that actually corresponds to Old English [_wæter_]{.iv lang=oe sort=waeter role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7754"}. The relevant
comparator is the inherited nominative-accusative singular [_\*wátōr_]{.iv lang=pgmc sort=wator role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7755"}.

#### Old English evidence

Bright gives the noun as [_wæter_]{.iv lang=oe sort=waeter role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7759"} with the regular paradigm
_wæteres_, _wætere_, _wæter(u)_, _wætera_, _wæterum_
[@BrightCassidyRingler1971, 29]. Ringe and Taylor add the dialectal contrast
between West Saxon _weeter_ and Mercian _weter_
[@RingeTaylor2014, §6.5.2].

The target is therefore an attested Old English citation form within a normal
paradigm. The complication lies on the comparative side of the lexeme, not in
Old English attestation.

#### Development to Old English

From [_\*wátōr_]{.iv lang=pgmc sort=wator role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7771"}, pre-final _\*ō_ becomes _a_ before final _r_,
yielding _\*watar_ [@RingeTaylor2014, §3.1.4]. Anglo-Frisian brightening then
gives _\*wætær_, and merger of unstressed _æ_/_e_ yields [_wæter_]{.iv lang=oe sort=waeter role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7773"}.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the generalized lexeme label from
the singular input that matches the Old English citation form.

| Stage or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| generalized comparative label | [_\*wátną_]{.iv lang=pgmc sort=watna role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7782"} | broader lexeme shorthand, not the singular that corresponds directly to [_wæter_]{.iv lang=oe sort=waeter role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7782"} | useful background only |
| heteroclitic stem notation | _\*watar-_ ~ _\*watan-_ | source-faithful comparative reconstruction | explains why a singular comparator is needed |
| inherited singular input | [_\*wátōr_]{.iv lang=pgmc sort=wator role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7784"} | regular output: [_wæter_]{.iv lang=oe sort=waeter role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7784"} | Old English-facing input |

### whale — OE _hwæl_

\index[oe]{hwael@\emph{hwæl}}
\index[pgmc]{walaz@*wálaz}
\index[pgmc]{xwalaz@*xwálaz}

Derivation: citation reconstruction _\*wálaz_; form followed here _\*xwálaz_ > _hwæl_ (early analogy).

#### Derivation trace

Proto input: _\*xwálaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*xwála} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*xwál} \\
Anglo Frisian Brightening & \emph{*xwæl} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hwæl_

#### Reconstruction and comparative evidence

The comparative sources are not uniform. Orel gives [_\*xwalaz_]{.iv lang=pgmc sort=xwalaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7837"} and notes some
mixed [_\*xwaliz_]{.iv lang=pgmc sort=xwaliz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7838"} evidence [@Orel2003, 197]. Kroonen instead cites
[_\*hwali-_]{.iv lang=pgmc sort=hwali role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7839"} [@Kroonen2013, 262].

Both notations agree on inherited initial _hw-/xw-_, but they differ in
stem label. The a-stem-like input followed here is closer to Orel's notation
than to Kroonen's citation form.

#### Old English evidence

Clark Hall lemmatizes the noun as [_hwal_]{.iv lang=oe sort=hwal role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7847"}, and Bosworth-Toller preserves the
plural [_hwalas_]{.iv lang=oe sort=hwalas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7848"} [@ClarkHall1960, 170; @BosworthToller1898, 326]. The comparison form
is normalized here as [_hwæl_]{.iv lang=oe sort=hwael role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7849"} for the singular citation form with Anglo-
Frisian fronting.

The plural [_hwalas_]{.iv lang=oe sort=hwalas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7852"} supplies control evidence. It shows the same
lexeme with _a_ in an open syllable, beside singular [_hwæl_]{.iv lang=oe sort=hwael role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7853"} in the
closed monosyllable.

#### Development to Old English

From _\*xwálaz_, final _-z_ disappears and bare final _-a_ is lost.
Anglo-Frisian fronting then yields _æ_ in the closed monosyllable, and Old
English orthography writes _hwæl_.

#### Formation comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative
notations from the normalized Old English singular.

| Comparative line | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Orel's citation | [_\*xwalaz_]{.iv lang=pgmc sort=xwalaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7869"} | same stem notation as the modeled singular line | closest comparative support for the derivational input |
| Kroonen's citation | [_\*hwali-_]{.iv lang=pgmc sort=hwali role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7870"} | same initial cluster, different stem label | important comparative rival, but not the notation followed here |
| modeled input | [_\*xwálaz_]{.iv lang=pgmc sort=xwalaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7871"} | regular output: [_hwæl_]{.iv lang=oe sort=hwael role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7871"} | Old English-facing input |
| plural control | [_hwalas_]{.iv lang=oe sort=hwalas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7872"} | attested open-syllable plural beside singular [_hwæl_]{.iv lang=oe sort=hwael role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7872"} | confirms that the lexeme also preserves an _a_-vocalism branch |

### whine — OE _hwīnan_

\index[oe]{hwinan@\emph{hwīnan}}
\index[pgmc]{wainojana@*wainōjaną}
\index[pgmc]{xwinana@*xwḯnaną}

Derivation: citation reconstruction _\*wainōjaną_; form followed here _\*xwī́naną_ > _hwīnan_ (early analogy).

#### Derivation trace

Proto input: _\*xwī́naną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Heavy Syllable Nasal Apocope & \emph{*xwī́nan} \\
OE Secondary Nasalization & \emph{*xwī́nąn} \\
OE Weak Tail Reduction & \emph{*xwī́nan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hwīnan_

#### Reconstruction and comparative evidence

The citation reconstruction preserved in the header belongs to the lament-family
verb seen in German [_weinen_]{.iv lang=german sort=weinen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7925"} and Old English [_wānian_]{.iv lang=oe sort=wanian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7925"}. Kroonen instead separates
Old English [_hwīnan_]{.iv lang=oe sort=hwinan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7926"} under _\*hwinan-_ [@Kroonen2013, 267]. Orel likewise
distinguishes strong [_\*xwinanan_]{.iv lang=pgmc sort=xwinanan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7927"} from weak [_\*wainōjanan_]{.iv lang=pgmc sort=wainojanan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7927"} [@Orel2003, 201]. Ringe and
Taylor make the same split at the Northwest Germanic level, linking Old Norse
[_hvina_]{.iv lang=on sort=hvina role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7929"} and Old English [_hwinan_]{.iv lang=oe sort=hwinan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7929"} to the same strong verb
[@RingeTaylor2014, 130].

The two families also differ phonologically and morphologically. The lament
family has initial _w-_, diphthongal _ai_, and weak-II morphology, whereas the
verb behind Old English _hwīnan_ has initial _hw-/xw-_, long _ī_, and
strong-verb inflection. The derivational input [_\*xwī́naną_]{.iv lang=pgmc sort=xwinana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7935"} therefore represents a
competing comparative identification rather than a hidden cell of _\*wainōjaną_.

#### Old English evidence

Clark Hall records [_hwinan_]{.iv lang=oe sort=hwinan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7940"} with the gloss 'to hiss, whizz, whistle'
[@ClarkHall1960, 171]. Seebold keeps the verb among the strong verbs and notes that
only a present-tense attestation is directly preserved [@Seebold1970, 280].

The Old English form is normalized here as [_hwīnan_]{.iv lang=oe sort=hwinan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7944"}. That normalization adds the
usual vowel length marking to the dictionary spelling [_hwinan_]{.iv lang=oe sort=hwinan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7945"}; it does not turn
an unattested verb into a reconstructed one.

#### Development to Old English

Once the strong-verb input [_\*xwī́naną_]{.iv lang=pgmc sort=xwinana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7950"} is selected, the path to Old English is
straightforward. The compact trace shows heavy-syllable nasal apocope,
secondary nasalization, and weak-tail reduction, after which the form surfaces
as [_hwīnan_]{.iv lang=oe sort=hwinan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7953"}.

No special paradigm maneuver is needed for this verb. The comparison is between
two different Germanic verb families: the Old English form belongs with the
strong verb _\*hwīnan-_, not with the weak lament verb.

#### Verb-family comparison

The comparison below sets the relevant forms side by side. It separates the competing comparative labels
that stand behind the inherited Old English forms.

| Verb family / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lament-family weak verb | [_\*wainōjaną_]{.iv lang=pgmc sort=wainojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7966"} | comparative continuation in OE [_wānian_]{.iv lang=oe sort=wanian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7966"} | [_wānian_]{.iv lang=oe sort=wanian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7966"} | competing citation reconstruction, but not the source of _hwīnan_ |
| selected strong verb | [_\*xwī́naną_]{.iv lang=pgmc sort=xwinana role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7967"} | regular output: [_hwīnan_]{.iv lang=oe sort=hwinan role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7967"} | [_hwīnan_]{.iv lang=oe sort=hwinan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7967"} | exact match between derivational input and OE verb |
| comparative North Germanic cognate | Northwest Germanic strong verb behind ON [_hvina_]{.iv lang=on sort=hvina role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7968"} / OE [_hwinan_]{.iv lang=oe sort=hwinan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7968"} | ON [_hvina_]{.iv lang=on sort=hvina role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7968"} / OE [_hwinan_]{.iv lang=oe sort=hwinan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7968"} | [_hwīnan_]{.iv lang=oe sort=hwinan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:7968"} | supports the strong-verb identification |

### withy — OE _wīþiġ_

\index[oe]{withig@\emph{wīþiġ}}
\index[pgmc]{waithiz@*wáiθiz}
\index[pgmc]{withaga@*wḯθagą}

Derivation: citation reconstruction _\*wáiθiz_; form followed here _\*wī́θagą_ > _wīþiġ_ (early analogy).

#### Derivation trace

Proto input: _\*wī́θagą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*wī́θægą} \\
OE Heavy Syllable Nasal Apocope & \emph{*wī́θæg} \\
OE Velar Palatalization & \emph{*wī́θæʤ} \\
OE Unstressed AE Merger & \emph{*wī́θeʤ} \\
OE Late Unstressed Ag Suffix & \emph{*wī́θiʤ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _wīþiġ_

#### Reconstruction and comparative evidence

The comparative evidence groups the word with Germanic forms of the
_\*wīþja_/_ō-_ or _\*wiþ-_ type [@Orel2003, 503]. These forms establish the
cognate set but do not by themselves explain the Old English suffix of
_wīþiġ_.

For Old English, the relevant point is the suffix history. Campbell's account
of OE _-ig_, including forms such as _hunig_, supports an analysis in which the
_-iġ_ of _wīþiġ_ continues a derivational _\*-ag-_ sequence rather than a heavy
ja-stem _\*-ij-_ [@Campbell1959, §§275, 376]. The derivational input [_\*wī́θagą_]{.iv lang=pgmc sort=withaga role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8030"} is
thus a formation choice rather than a mere respelling of the comparative
headword.

#### Old English evidence

Clark Hall records the noun as [_wiðig_]{.iv lang=oe sort=withig role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8036"} [@ClarkHall1960, 358]. The form used here,
[_wīþiġ_]{.iv lang=oe sort=withig role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8037"}, is a normalized Old English spelling with macrons and palatal ġ marked
explicitly.

The relevant comparison form is therefore not a reconstructed dictionary
convenience but an established Old English noun. What requires explanation is
why the selected Proto-Germanic input is [_\*wī́θagą_]{.iv lang=pgmc sort=withaga role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8042"} rather than a comparative
headword of the _\*wīþja-_ type.

#### Development to Old English

From [_\*wī́θagą_]{.iv lang=pgmc sort=withaga role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8047"}, Anglo-Frisian brightening gives a fronted vowel in the suffixal
syllable, and, on the Campbell analysis adopted here, the later Old English
development of _\*-ag-_ yields _-iġ_ [@Campbell1959, §§275, 376].
Palatalization supplies the final _ġ_, and the full development reaches
[_wīþiġ_]{.iv lang=oe sort=withig role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8051"}.

This derivation is regular for the form compared here. The central claim of the
entry is therefore morphological: Old English _wīþiġ_ belongs with an
_\*-ag-_ derivative, whereas the comparative _\*wīþja-_ label belongs to a
different way of presenting the cognate family.

#### Formation comparison

The comparison below sets the relevant formations side by side. It distinguishes the comparative headword from
the Old English-facing formation that actually yields the attested noun.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative family label | [_\*wáiθiz_]{.iv lang=pgmc sort=waithiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8065"} | broader cognate-set headword | OE family context | useful lexeme label, but not the direct source of _wīþiġ_ |
| heavy ja-stem analysis | _\*wīþja-_ type | Campbell/Adamczyk-style heavy ja-stem _-e_ / zero outcome | [_wīþiġ_]{.iv lang=oe sort=withig role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8066"} | does not account cleanly for the OE suffix |
| _\*-ag-_ derivative followed here | [_\*wī́θagą_]{.iv lang=pgmc sort=withaga role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8067"} | regular output: [_wīþiġ_]{.iv lang=oe sort=withig role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8067"} | [_wīþiġ_]{.iv lang=oe sort=withig role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8067"} | exact match between formation and target |

### world — OE _weorold_

\index[oe]{weorold@\emph{weorold}}
\index[pgmc]{wiraaldiz@*wíra-àldiz}
\index[pgmc]{wiraldu@*wír-àldu}
\index[pgmc]{wiraldu@*wíràldu}

Derivation: citation reconstruction _\*wíra-àldiz_; form followed here _\*wír-àldu_ > _weorold_ (early analogy).

#### Derivation trace

Proto input: _\*wíràldu_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
NWGmc I Lowering & \emph{*wéràldu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
OE Inter Stress Raising & \emph{*wéruldu} \\
OE Med Unstressed U Lowering & \emph{*wéroldu} \\
OE Back Mutation & \emph{*wéoroldu} \\
OE High Vowel Apocope & \emph{*wéorold} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _weorold_

#### Reconstruction and comparative evidence

The word is the old compound 'age of men'. Orel and the _\*wira-_ tradition
reconstruct the older _i_-vocalism, while Ringe and Taylor discuss the lowered form
_\*weraldiz_ and its pre-Old-English chain _\*weraldu_ > _\*weruld_
[@Orel2003, 501; @RingeTaylor2014, 341]. Kluge-Seebold likewise gives the
compound _\*wira-aldō_ and explicitly includes Old English _weorold_
[@KlugeSeebold2011, 981].


The derivational input [_\*wír-àldu_]{.iv lang=pgmc sort=wiraldu role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8130"} therefore combines the older _\*wir-_ vowel of the comparative headword with
the early shift of the compound into the ō-stems that Ringe and
Taylor note for this lexeme [@RingeTaylor2014, 341]. The early analogical step lies
in that stem-class reassignment; the later phonological developments can then run
regularly.

#### Old English evidence

Old English does not preserve a single isolated form. Ringe and Taylor give West
Saxon [_weorold_]{.iv lang=oe sort=weorold role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8139"} ~ [_worold_]{.iv lang=oe sort=worold role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8139"}, Mercian [_weoruld_]{.iv lang=oe sort=weoruld role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8139"}, Northumbrian
[_woruld_]{.iv lang=oe sort=woruld role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8140"}, and Kentish [_wiarald_]{.iv lang=oe sort=wiarald role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8140"} [@RingeTaylor2014, 341]. Sievers-Brunner and Bright present the same wider
set, including the syncopated [_world_]{.iv lang=oe sort=world role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8141"} and later rounded [_wurold_]{.iv lang=oe sort=wurold role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8141"}
[@SieversBrunner1965, §113; @BrightCassidyRingler1971, 465].

The Old English form used here is the West Saxon form [_weorold_]{.iv lang=oe sort=weorold role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8144"}. It is an attested Old
English form within that broader variant cluster, not the only form the lexeme
ever shows.

#### Development to Old English

From _\*wír-àldu_, Northwest Germanic _i_-lowering gives
_\*wér-àldu_. Inter-stress raising then changes the medial _a_ to _u_, producing
_\*wér-uldu_. In the Old English branch that unstressed _u_ lowers to _o_, and
back mutation yields _\*wéor-oldu_; final high-vowel apocope then gives
_weorold_.

This sequence matches the comparative background in Ringe and Taylor's
_\*weraldiz_ > _\*weraldu_ > _\*weruld_ chain while preserving the _\*wir-_ notation of
the comparative label [@RingeTaylor2014, 341]. The modeled Old English form
therefore stands at the meeting point of an early stem-class reshaping and later
regular sound change.

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the comparative headword from the
OE-facing stage chosen for the derivation.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| comparative compound with older first-element vowel | [_\*wíra-àldiz_]{.iv lang=pgmc sort=wiraaldiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8169"} | citation reconstruction / lexeme label | preserves the older _\*wir-_ tradition of the compound |
| literature-stage lowered compound after early stem-class shift | [_\*weraldiz_]{.iv lang=preoe sort=weraldiz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8170"} > [_\*weraldu_]{.iv lang=preoe sort=weraldu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8170"} > [_\*weruld_]{.iv lang=preoe sort=weruld role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8170"} | Ringe-Taylor background chain to OE [_weorold_]{.iv lang=oe sort=weorold role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8170"} ~ [_worold_]{.iv lang=oe sort=worold role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8170"} | explains the older comparative literature cited for the word |
| Old English-facing input | [_\*wír-àldu_]{.iv lang=pgmc sort=wiraldu role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8171"} | regular output: [_weorold_]{.iv lang=oe sort=weorold role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8171"} | exact match for the West Saxon form used here |
| broader OE variant cluster | — | [_worold_]{.iv lang=oe sort=worold role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8172"}, [_weoruld_]{.iv lang=oe sort=weoruld role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8172"}, [_woruld_]{.iv lang=oe sort=woruld role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8172"}, [_wiarald_]{.iv lang=oe sort=wiarald role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8172"}, [_world_]{.iv lang=oe sort=world role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8172"} | real attested comparanda that remain outside that West Saxon line |

### youth — OE _ġeoguþ_

\index[oe]{geoguth@\emph{ġeoguþ}}
\index[pgmc]{jugunth@*júgunθ}
\index[pgmc]{jugunthiz@*júgunθiz}

Derivation: citation reconstruction _\*júgunθiz_; form followed here _\*júgunθ_ > _ġeoguþ_ (early analogy).

#### Derivation trace

Proto input: _\*júgunθ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Ws Palatal Glide & \emph{*jéugunθ} \\
NWGmc Nasal Spirant Lengthening & \emph{*jéugūnθ} \\
NWGmc Nasal Spirant Loss & \emph{*jéugūθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Diphthong Leveling & \emph{*jéogūθ} \\
OE Unstressed Long Vowel Shortening & \emph{*jéoguθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ġeoguþ_

#### Reconstruction and comparative evidence

The wider etymological tradition reconstructs an earlier form of the word as
[_\*ju(w)unþi-_]{.iv lang=pgmc sort=juwunthi role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8228"} [@Kroonen2013, 316]. The comparative label
[_\*júgunθiz_]{.iv lang=pgmc sort=jugunthiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8229"} already stands at a later Germanic stage with _g_, and the
derivational input [_\*júgunθ_]{.iv lang=pgmc sort=jugunth role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8230"} is later again: it represents the form after final
_-i_ has been lost.

Ringe and Taylor explicitly give the sequence
_\*jugunþi_ > _\*juguþ_ > OE _geoguþ_ ~ _iuguþ_ [@RingeTaylor2014, 141]. The
derivational input therefore differs from the broader comparative headword
because the Old English development must begin after early loss of final _-i_.

#### Old English evidence

The Old English noun is attested with varying spellings. Ringe and Taylor cite
[_geoguþ_]{.iv lang=oe sort=geoguth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8241"} ~ [_iuguþ_]{.iv lang=oe sort=iuguth role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8241"} [@RingeTaylor2014, 141]. The form is normalized here as
[_ġeoguþ_]{.iv lang=oe sort=geoguth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8242"}: the initial palatal is written with _ġ_, and the attested spelling
variation is treated as orthographic rather than lexical.

Nothing in the source stack suggests that a different paradigm cell should be
chosen. The relevant Old English comparison form is the noun [_ġeoguþ_]{.iv lang=oe sort=geoguth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8246"} itself.

#### Development to Old English

The decisive early step is the loss of final _-i_ before the Old English umlaut
stage. If that high vowel remained, the word would develop an over-umlauted
_y_-type vowel instead of the attested form [@RingeTaylor2014, 141].

From the derivational input [_\*júgunθ_]{.iv lang=pgmc sort=jugunth role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8254"}, the later development is regular: palatal
fronting yields _\*jéugunθ_; nasal-spirant lengthening and loss give
_\*jéogūθ_ [@Fulk2018, 109]; unstressed long-vowel shortening then produces
_\*jéoguθ_, which surfaces as [_ġeoguþ_]{.iv lang=oe sort=geoguth role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8257"}. Campbell preserves _u_ after accented _u_ in forms such
as [_duguþ_]{.iv lang=oe sort=duguth role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8258"} and [_munuc_]{.iv lang=oe sort=munuc role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8258"} [@Campbell1959, §374]. Brunner likewise cites _iuzuð_
_Jugend_ and _munuc_ _Mönch_ in the same environment
[@SieversBrunner1965, §150.3].

#### Stage comparison

The comparison below sets the relevant forms side by side. It separates the broader comparative headword
from the later stages relevant to the Old English noun.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| earlier etymological headword | [_\*ju(w)unþi-_]{.iv lang=pgmc sort=juwunthi role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8269"} | comparative family background | older comparative reconstruction of the lexeme |
| later g-bearing comparative label | [_\*júgunθiz_]{.iv lang=pgmc sort=jugunthiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8270"} | citation reconstruction / lexeme label | preserves the later Germanic stage behind the selected entry |
| Old English-facing input | [_\*júgunθ_]{.iv lang=pgmc sort=jugunth role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8271"} | regular output: [_ġeoguþ_]{.iv lang=oe sort=geoguth role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8271"} | exact match for the Old English form used here |
| full _-i_ stage retained too long | [_\*jugunþi_]{.iv lang=pgmc sort=jugunthi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8272"} | expected over-umlauted _y_-type result | negative control showing why early _-i_ loss must precede the OE umlaut stage |

\clearpage

## Late analogy and paradigm-cell selection

These Old English forms continue a particular paradigm cell or a later
analogical remodeling, not the unaltered citation form. The phonology may be
regular once the proper morphological history has been identified.

### ban — OE _bannes_

\index[oe]{bannes@\emph{bannes}}
\index[pgmc]{banna@*bánną}
\index[pgmc]{bannas@*bánnas}

Derivation: citation reconstruction _\*bánną_; form followed here _\*bánnas_ > _bannes_ (late analogy).

#### Derivation trace

Proto input: _\*bánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bánnæs} \\
OE Unstressed AE Merger & \emph{*bánnes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bannes_

#### Reconstruction and comparative evidence

Orel cites a bann-noun under [_\*bannan_]{.iv lang=pgmc sort=bannan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8331"}, while Seebold distinguishes bann-stems
of both masculine and neuter type and gives Old English [_gebann_]{.iv lang=oe sort=gebann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8332"} as the noun
reflex [@Orel2003, 35; @Seebold1970, 89]. The citation reconstruction [_\*bánną_]{.iv lang=pgmc sort=banna role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8333"}
names the lexeme, but the comparison here turns on the genitive singular
[_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8335"}.

The analysis therefore depends on medial, not final, gemination.

#### Old English evidence

Old English lexicographic evidence securely supports the noun itself.
Bosworth-Toller records the noun under nominative [_ge-bann_]{.iv lang=oe sort=gebann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8342"}, with oblique
usage such as [_gebanne_]{.iv lang=oe sort=gebanne role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8343"} [@BosworthToller1898, 303]. The exact unprefixed
genitive [_bannes_]{.iv lang=oe sort=bannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8344"} is less directly cited in the dictionaries, so it is best
treated here as the regular genitive form used for comparison rather than as a
dictionary headword.

#### Development to Old English

From [_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8350"}, the geminate remains medial before the case ending and the
unstressed vowel develops regularly to give [_bannes_]{.iv lang=oe sort=bannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8351"}. The paradigm comparison
therefore sets the genitive against nominative [_ban_]{.iv lang=oe sort=ban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8352"}, the ordinary nominative
form of the same noun, rather than against a directly cited genitive headword.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows why the genitive singular is the
conservative cell used for the entry.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*bánną_]{.iv lang=pgmc sort=banna role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8362"} | regular output: [_ban_]{.iv lang=oe sort=ban role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8362"} | ban | regular nominative outcome, but not the Old English form here |
| genitive singular | [_\*bánnas_]{.iv lang=pgmc sort=bannas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8363"} | regular output: _bannes_ | [_bannes_]{.iv lang=oe sort=bannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8363"} | direct match for the conservative genitive |

### berry — OE _berġes_

\index[oe]{berges@\emph{berġes}}
\index[pgmc]{bazja@*bázją}
\index[pgmc]{bazjas@*bázjas}

Derivation: citation reconstruction _\*bázją_; form followed here _\*bázjas_ > _berġes_ (late analogy).

#### Derivation trace

Proto input: _\*bázjas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*bærjæs} \\
OE I Umlaut & \emph{*berjæs} \\
OE Unstressed AE Merger & \emph{*berjes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _berġes_

#### Reconstruction and comparative evidence

Kroonen reconstructs the berry noun as [_\*basja-_]{.iv lang=pgmc sort=basja role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8415"} ~ [_\*bazja-_]{.iv lang=pgmc sort=bazja role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8415"} [@Kroonen2013, 54]. The
derivational input [_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8416"} is therefore not a rival lexeme headword, but a
specific genitive singular cell drawn from that paradigm.

The relevant point is that _\*rj_ did not geminate in Proto-West Germanic.
Ringe and Taylor's [_here_]{.iv lang=oe sort=here role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8420"}, [_herges_]{.iv lang=oe sort=herges role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8420"} comparison shows the same _rj_ environment in
an Old English paradigm without any hidden gemination repair [@RingeTaylor2014, 181].

#### Old English evidence

Campbell cites feminine [_berige_]{.iv lang=oe sort=berige role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8425"} 'berry' and notes that _-j-_ is retained after
_r_ in this type [@Campbell1959, 250]. The reviewed evidence therefore supports the
citation form more directly than the exact genitive [_berġes_]{.iv lang=oe sort=berges role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8427"}, which is best read
here as the regular genitive comparison form rather than as a
dictionary headword.

#### Development to Old English

Citation [_\*bázją_]{.iv lang=pgmc sort=bazja role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8433"} gives [_bere_]{.iv lang=oe sort=bere role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8433"}, not the Old English form here. The genitive singular
[_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8434"}, however, gives [_berġes_]{.iv lang=oe sort=berges role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8434"}, with medial _-rġ-_ preserved in the same
way that Ringe and Taylor cite [_herges_]{.iv lang=oe sort=herges role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8435"} beside [_here_]{.iv lang=oe sort=here role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8435"} [@RingeTaylor2014, 181].
This points to paradigm choice rather than to an extra phonological rule.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows the contrast between the citation form
and the genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*bázją_]{.iv lang=pgmc sort=bazja role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8445"} | regular output: [_bere_]{.iv lang=oe sort=bere role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8445"} | [_berige_]{.iv lang=oe sort=berige role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8445"} / [_berġe_]{.iv lang=oe sort=berge role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8445"} | useful citation-form background, but not the Old English form here |
| genitive singular | [_\*bázjas_]{.iv lang=pgmc sort=bazjas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8446"} | regular output: _berġes_ | [_berġes_]{.iv lang=oe sort=berges role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8446"} | exact match for the conservative cell |

### bow — OE _bēag_

\index[oe]{beag@\emph{bēag}}
\index[pgmc]{baug@*báug}
\index[pgmc]{beugana@*béuganą}

Derivation: citation reconstruction _\*béuganą_; form followed here _\*báug_ > _bēag_ (late analogy).

#### Derivation trace

Proto input: _\*báug_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*báeug} \\
OE Diphthong Leveling & \emph{*bēag} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bēag_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-II strong-verb family [_\*béuganą_]{.iv lang=pgmc sort=beugana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8497"}
[@RingeTaylor2014, 55]. Within that paradigm, however, the infinitive and the
singular preterite continue different ablaut grades. The derivational input [_\*báug_]{.iv lang=pgmc sort=baug source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8499"}
is the singular preterite cell, whereas the citation form [_\*béuganą_]{.iv lang=pgmc sort=beugana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8500"} is the
infinitive.

Campbell's account of Old English class-II strong verbs treats the singular
preterite _au_ > _ēa_ development as regular in this environment
[@Campbell1959, 53].
That is the phonological path relevant for [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8506"}, whereas the analogical _ū_
of the present stem belongs to the separate history behind [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8507"}
[@RingeTaylor2014, 55].

#### Old English evidence

Bosworth-Toller and Clark Hall both record [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8512"} as a preterite form of
[_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8513"} [@BosworthToller1898, 122; @ClarkHall1960, 45]. The form discussed here is
therefore an attested Old English verbal form, not a reconstructed substitute
for the infinitive.

The ordinary dictionary headword remains [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8517"}, but the relevant comparison
form for this entry is the singular preterite [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8518"}. That is the paradigm
cell in which the inherited _\*au_ grade is preserved most directly.

#### Development to Old English

From [_\*báug_]{.iv lang=pgmc sort=baug source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8523"}, Anglo-Frisian fronting and the later leveling of the diphthong
produce [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8524"} [@Campbell1959, 53]. No special analogical repair is needed for that
cell. The form is the regular Old English outcome of the singular-preterite
grade.

The analogical element in the wider lexeme belongs instead to the present stem
seen in [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8529"}. The derivational input differs from the citation form because the
regular inherited pathway survives more transparently in the preterite than in
the infinitive.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the regular singular
preterite from the more familiar infinitival citation form.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | [_\*béuganą_]{.iv lang=pgmc sort=beugana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8540"} | inherited present-stem history behind [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8540"} | [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8540"} | establishes the lexeme, but not the Old English form here |
| singular preterite | [_\*báug_]{.iv lang=pgmc sort=baug source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8541"} | regular output: [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8541"} | [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8541"} | exact match between input, output, and attested cell |
| past participial branch | participial _\*bugan-_ type | later participial outcomes | bogen-type evidence | relevant to the paradigm, but not the clearest match for this entry |

The singular preterite is the relevant comparison form. It gives a direct
lautgesetzlich path to attested [_bēag_]{.iv lang=oe sort=beag source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8545"}, while the citation form [_būgan_]{.iv lang=oe sort=bugan source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8545"}
belongs to a paradigm whose present stem has already undergone later leveling.

### cow — OE _cȳ_

\index[oe]{cy@\emph{cȳ}}
\index[pgmc]{koz@*kōz}
\index[pgmc]{kui@*kūi}

Derivation: citation reconstruction _\*kōz_; form followed here _\*kūi_ > _cȳ_ (late analogy).

#### Derivation trace

Proto input: _\*kūi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*kȳi} \\
\mbox{OE High Vowel Apocope} & \emph{*kȳ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _cȳ_

#### Reconstruction and comparative evidence

Kroonen reconstructs a root noun with the inherited alternation
_\*kō-_ ~ _\*ku-_, explicitly nom. _\*kōz_, obl. _\*kū-_ [@Kroonen2013, 299].
The citation form therefore belongs to the nominative singular, whereas the
derivational input _\*kūi_ belongs to the oblique stem.

Ringe and Taylor also posit a later PNWGmc nominative _\*kūaz_ > _\*kūz_ behind Old
English _cū_ [@RingeTaylor2014, §3.1.3]. That nominative history accounts for
the headword, whereas the form _cȳ_ depends on the oblique _\*kū-_ stem and a
following _\*i_.

#### Old English evidence

Clark Hall lemmatizes the noun under _cū_ and records gen.sg. _cū(e)_, _cȳ_, _cūs_,
dat.sg. _cȳ_, nom.-acc.pl. _cȳ_, and dat.pl. _cūm_ [@ClarkHall1960, 67]. Ringe
and Taylor likewise state that the root-noun _cū_ exhibits dat.sg., nom.-acc.pl.
_cȳ_ < _\*cūi_, dat.pl. _cūm_ < _\*cūm_, and apparently gen.sg. _cā_ < _\*cūiz_
[@RingeTaylor2014, §6.6.1].

The dictionary headword is therefore _cū_, but _cȳ_ is an established Old
English paradigm form rather than a convenient reconstruction. It serves as
dative singular and also as nominative-accusative plural. The genitive
singular is less stable, with _cā_, _cȳ_, _cū(e)_, and _cūs_ all appearing in
the local source record.

#### Development to Old English

_\*kūi_ is the dative singular of the oblique _\*kū-_ stem. The following _\*i_
triggers i-umlaut, so _ū_ becomes _ȳ_, and loss of the final high vowel leaves
_cȳ_. The development is _\*kūi_ > _\*kȳi_ > _\*kȳ_ > _cȳ_.

This is the regular oblique-cell path recognized by Ringe and Taylor's paradigm
statement [@RingeTaylor2014, §6.6.1]. It also explains why _cȳ_ is the cleanest
comparison form for the present entry, even though the ordinary headword is
_cū_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that
corresponds to an established Old English paradigm form. The comparison below
sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *kōz | OE headword _cū_ belongs to the nominative history of the lexeme | _cū_ | useful background, but not the chosen comparison for _cȳ_ |
| later generalized nominative | PNWGmc *kūaz > *kūz | inferred nominative _cū_ | _cū_ | explains the leveled headword, not the oblique target |
| dative singular oblique | *kūi | regular output: _cȳ_ | _cȳ_ | exact match between input, output, and paradigm cell |
| genitive singular oblique | *kūiz | Ringe-Taylor: apparently _cā_; Hall: _cū(e)_, _cȳ_, _cūs_ | gen.sg. variable | too unstable to control the entry |

The dative singular is the relevant comparison form. It gives a regular path to
attested _cȳ_, while the broader Old English paradigm shows how far the oblique
_\*kū-_ grade spread beyond that one cell.

### find — OE _fundene_

\index[oe]{fundene@\emph{fundene}}
\index[pgmc]{finthana@*fínθaną}
\index[pgmc]{fundano@*fúnðanǭ}

Derivation: citation reconstruction _\*fínθaną_; form followed here _\*fúnðanǭ_ > _fundene_ (late analogy).

#### Derivation trace

Proto input: _\*fúnðanǭ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Dental Hardening & \emph{*fúndanǭ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Unstressed Fronting Early & \emph{*fúndænǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*fúndænæ} \\
OE Unstressed AE Merger & \emph{*fúndene} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fundene_

#### Reconstruction and comparative evidence

The inherited verb is the strong verb [_\*fínθaną_]{.iv lang=pgmc sort=finthana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8701"}, continued by Old English
[_findan_]{.iv lang=oe sort=findan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8702"} [@RingeTaylor2014, 344]. The form followed here, [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8702"},
belongs to the past-participial paradigm rather than to the infinitive. It
represents an oblique singular form of the participle.

The familiar dictionary form [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8706"} is not
the form compared here. The derivational input instead models an attested
participial form directly, rather than treating the infinitive or the ordinary
dictionary headword as primary. It therefore reaches [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8709"} in the form
where the trace and the attested evidence match directly.

#### Old English evidence

Bosworth-Toller records [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8714"} under [_findan_]{.iv lang=oe sort=findan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8714"}, citing the form in
_Beón þá herigeata swa fundene_ [@BosworthToller1898, 219]. Clark Hall likewise preserves the
participial stem in forms such as [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8716"} and _tō-fundennes_
[@ClarkHall1960, 124].

The ordinary dictionary headword for the participle is [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8719"}, but the
relevant comparison form for this entry is the attested oblique [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8720"}.
It is an Old English form in its own right, not a merely convenient probe.

#### Development to Old English

From [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8725"}, the participial oblique develops through regular loss and
weakening of the final ending, yielding [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8726"}. In that cell both the
consonantism and the medial vowel history remain regular.

The broader participial paradigm fixes the interpretation. The more
familiar nominative [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8730"} is the ordinary dictionary form, whereas the
oblique form [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8731"} is the attested form compared here.

#### Paradigm comparison

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | [_\*fínθaną_]{.iv lang=pgmc sort=finthana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8737"} | inherited verb [_findan_]{.iv lang=oe sort=findan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8737"} | [_findan_]{.iv lang=oe sort=findan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8737"} | establishes the lexeme, but not the form compared here |
| nominative participial line | [_\*fúnðanaz_]{.iv lang=pgmc sort=fundhanaz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8738"} | ordinary dictionary [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8738"} type | [_funden_]{.iv lang=oe sort=funden role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8738"} | important paradigm background, but not the form compared here |
| oblique participle compared here | [_\*fúnðanǭ_]{.iv lang=pgmc sort=fundhano role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8739"} | regular output: [_fundene_]{.iv lang=oe sort=fundene role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8739"} | [_fundene_]{.iv lang=oe sort=fundene role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8739"} | exact match between input, output, and attested cell |

The oblique participle is the relevant comparison form. It matches the
derivational input and Old English form directly, while the nominative participial headword remains a
different presentation cell within the same paradigm.

### fright — OE _fyrhte_

\index[oe]{fyrhte@\emph{fyrhte}}
\index[pgmc]{furxtin@*furxtīn}
\index[pgmc]{furxtinaz@*fúrxtīnaz}

Derivation: citation reconstruction _\*furxtīn_; form followed here _\*fúrxtīnaz_ > _fyrhte_ (late analogy).

#### Derivation trace

Proto input: _\*fúrxtīnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*fúrxtīna} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fúrxtīn} \\
OE I Umlaut & \emph{*fyrxtīn} \\
NWGmc In Stem N Loss & \emph{*fyrxtī} \\
OE Unstressed Long Vowel Shortening & \emph{*fyrxti} \\
OE Med Unstressed I Lowering1 & \emph{*fyrxte} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _fyrhte_

#### Reconstruction and comparative evidence

The noun belongs to the inherited in-stem abstract [_\*furxtīn_]{.iv lang=pgmc sort=furxtin role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8799"}, the same family
as Gothic [_faurhtei_]{.iv lang=goth sort=faurhtei role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8800"} [@Orel2003, 120]. The derivational input [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8800"} is not a
different lexeme but an oblique singular cell within that in-stem paradigm.

Ringe and Taylor treat the later nominative forms with _-u_ or _-o_ as
analogically remodeled [@RingeTaylor2014, 395-396]. I therefore use the oblique
in-stem form, which continues the older formation rather than the remodeled
nominative.

#### Old English evidence

Bosworth-Toller records [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8810"} with textual attestation, and it also
records nominative forms such as [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8811"} and [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8811"}
[@BosworthToller1898, 160]. Clark Hall lists adjective and verb material
separately under _fyrht_ / _fyrhtan_ [@ClarkHall1960, 141].


The relevant comparison form is therefore the attested oblique [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8816"}.
The nominative lemma forms remain part of the Old English evidence, but the
Old English form here of this entry is the oblique cell.

#### Development to Old English

From [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8822"}, the oblique in-stem develops through the loss and weakening
of the final ending, yielding [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8823"}. The form compared here therefore
follows the ordinary Old English reduction of the abstract ending in this
paradigm.

The later nominative forms with _-u_ or _-o_ belong to a subsequent analogical
reshaping of the paradigm. The Old English form here is earlier in that sense: it is
the attested OE cell in which the inherited in-stem development remains most
transparent.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the attested oblique form from the
later remodeled nominative line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation in-stem headword | [_\*furxtīn_]{.iv lang=pgmc sort=furxtin role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8839"} | broader noun-class label | wider family context | useful lexeme label, but not the cell compared here |
| remodeled nominative line | nominative in-stem forms | [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8840"} / [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8840"} type lemma forms | [_fyrhtu_]{.iv lang=oe sort=fyrhtu role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8840"} / [_fyrhto_]{.iv lang=oe sort=fyrhto role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8840"} | genuine OE evidence, but later remodeled |
| selected oblique singular | [_\*fúrxtīnaz_]{.iv lang=pgmc sort=furxtinaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8841"} | regular output: [_fyrhte_]{.iv lang=oe sort=fyrhte role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8841"} | [_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8841"} | exact match between input, output, and attested cell |

The oblique in-stem form is the relevant comparison form. It yields attested
[_fyrhte_]{.iv lang=oe sort=fyrhte role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8844"} directly, while the more familiar nominative forms belong to a later
analogical layer.

### hammer — OE _hameres_

\index[oe]{hameres@\emph{hameres}}
\index[pgmc]{xamaras@*xámaras}
\index[pgmc]{xamaraz@*xámaraz}

Derivation: citation reconstruction _\*xámaraz_; form followed here _\*xámaras_ > _hameres_ (late analogy).

#### Derivation trace

Proto input: _\*xámaras_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xámæræs} \\
OE Unstressed AE Merger & \emph{*xámeres} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hameres_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem [_\*xámaraz_]{.iv lang=pgmc sort=xamaraz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8896"}, reflected in Old English
citation forms such as [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8897"} and [_hamer_]{.iv lang=oe sort=hamer role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8897"} [@Kroonen2013, 206; @Orel2003, 197;
@ClarkHall1960, 160]. The derivational input [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8898"} is the genitive singular of that
same noun rather than a different lexeme.

The citation tradition is already mixed in its unstressed vowel, while the
genitive singular gives a closer comparison form.
This is a cell choice within one paradigm, not a change of stem class.

#### Old English evidence

Bosworth-Toller directly records [_hameres_]{.iv lang=oe sort=hameres role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8907"} in an Old English genitival
phrase [@BosworthToller1898, 78]. Clark Hall preserves the simplex headword as
[_hamer_]{.iv lang=oe sort=hamer role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8909"} / [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8909"} [@ClarkHall1960, 160].

Sievers-Brunner gives a paradigm line [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8911"} — [_hamores_]{.iv lang=oe sort=hamores role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8911"}, which shows that the
oblique tradition itself was not entirely uniform [@SieversBrunner1965, §245]. The
relevant comparison form here is the attested genitive singular [_hameres_]{.iv lang=oe sort=hameres role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8913"}.

#### Development to Old English

From [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8917"}, Anglo-Frisian brightening and the subsequent merger of
unstressed _æ_ with _e_ yield [_hameres_]{.iv lang=oe sort=hameres role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8918"}. The derivation of that oblique form is
straightforward once the genitive singular cell is selected.

The noun as a whole retains a mixed citation tradition in [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8921"} and [_hamer_]{.iv lang=oe sort=hamer role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8921"},
and the selected oblique cell avoids making that variation carry the argument of
the entry.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the attested genitive singular
from the less stable citation tradition.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*xámaraz_]{.iv lang=pgmc sort=xamaraz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8932"} | regular citation form [_hamer_]{.iv lang=oe sort=hamer role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8932"} / [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8932"} | [_hamor_]{.iv lang=oe sort=hamor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8932"} / [_hamer_]{.iv lang=oe sort=hamer role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8932"} | good lexical background, but not the Old English form here |
| genitive singular | [_\*xámaras_]{.iv lang=pgmc sort=xamaras role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8933"} | regular output: [_hameres_]{.iv lang=oe sort=hameres role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8933"} | [_hameres_]{.iv lang=oe sort=hameres role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8933"} | exact match between input, output, and attested cell |
| later oblique tradition | oblique a-stem forms | [_hamores_]{.iv lang=oe sort=hamores role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8934"} type evidence | [_hamores_]{.iv lang=oe sort=hamores role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8934"} | attested background variant, but not the chosen comparison form |

### have — OE _hæfeþ_

\index[oe]{haefeth@\emph{hæfeþ}}
\index[pgmc]{xabena@*xabēną}
\index[pgmc]{xabethi@*xábēθi}

Derivation: citation reconstruction _\*xabēną_; form followed here _\*xábēθi_ > _hæfeþ_ (late analogy).

#### Derivation trace

Proto input: _\*xábēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*xábēθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*xábǣθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*xæbǣθ} \\
OE Velar Fricative Palatalization & \emph{*çæbǣθ} \\
PGmc B Allophony & \emph{*çæβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*çæβæθ} \\
OE Unstressed AE Merger & \emph{*çæβeθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _hæfeþ_

#### Reconstruction and comparative evidence

The verb belongs to the inherited class-III weak paradigm usually cited under
[_\*xabēną_]{.iv lang=pgmc sort=xabena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8993"} and Old English [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8993"} [@Kroonen2013, 237; @RingeTaylor2014, 93]. Within
that paradigm, however, the infinitive and the singular present indicative do
not continue the same stem. Ringe and Taylor distinguish a _-ja-_ stem in the
infinitive from a non-geminating -ai- / _-ē-_ stem in the 2sg and 3sg present
forms [@RingeTaylor2014, 93].

The derivational input [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:8999"} is therefore the 3sg present cell rather than a
rephrasing of the infinitive. For the present analysis, that finite cell is the
cleaner comparator for the inherited non-geminating stem.

#### Old English evidence

The ordinary Old English headword is [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9005"} [@ClarkHall1960, 157].
Campbell's Anglian paradigm includes unsyncopated 3sg forms of the [_hæfed_]{.iv lang=oe sort=haefed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9006"} type,
and the present paradigm therefore shows forms of the _hæf-_ type that support
the normalized target [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9008"} [@Campbell1959, §762].

The target form is therefore a normalized finite cell rather than the ordinary
dictionary lemma. It represents the inherited non-geminating present stem more
directly than [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9012"} does.

#### Development to Old English

From [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9016"}, the finite form yields [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9016"} regularly. Ringe and Taylor
discuss this non-geminating present stem under [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9017"}
[@RingeTaylor2014, 364]. Campbell's Anglian paradigms include unsyncopated 3sg
forms of the [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9019"} / [_hæfed_]{.iv lang=oe sort=haefed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9019"} type [@Campbell1959, §762].

The wider lexeme is less straightforward only because the infinitive [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9021"}
shows later leveling. The 3sg present cell is therefore the closer comparison
form.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the analogically leveled citation
form from the regular 3sg present line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | _-ja-_ stem of [_\*xabēną_]{.iv lang=pgmc sort=xabena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9032"} | citation form [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9032"} | [_habban_]{.iv lang=oe sort=habban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9032"} | important headword, but shaped by later leveling |
| 3sg present | [_\*xábēθi_]{.iv lang=pgmc sort=xabethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9033"} | regular output: [_hæfeþ_]{.iv lang=oe sort=haefeth role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9033"} | [_hæfeþ_]{.iv lang=oe sort=haefeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9033"} | exact match between input, output, and finite form compared here |
| syncopated finite tradition | same present stem | [_hæfþ_]{.iv lang=oe sort=haefth role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9034"} type evidence | [_hæfþ_]{.iv lang=oe sort=haefth role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9034"} | genuine later OE finite form, but not the normalized target used here |

### heaven — OE _heofon_

\index[oe]{heofon@\emph{heofon}}
\index[pgmc]{xemenaz@*xémenaz}
\index[pgmc]{xemonu@*xémonų}

Derivation: citation reconstruction _\*xémenaz_; form followed here _\*xémonų_ > _heofon_ (late analogy).

#### Derivation trace

Proto input: _\*xémonų_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc Unstressed O Raising & \emph{*xémunų} \\
NWGmc Mn Dissimilation & \emph{*xéβunų} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Med Unstressed U Lowering & \emph{*xéβonų} \\
OE Velar Fricative Palatalization & \emph{*çéβonų} \\
OE Back Mutation & \emph{*çéoβonų} \\
\mbox{OE High Vowel Apocope} & \emph{*çéoβon} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _heofon_

#### Reconstruction and comparative evidence

The inherited noun belongs to the mn-stem family cited by Kroonen as
[_\*hemina-_]{.iv lang=pgmc sort=hemina source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9091"} ~ [_\*hemna-_]{.iv lang=pgmc sort=hemna source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9091"} [@Kroonen2013, 220]. The derivational input [_\*xémonų_]{.iv lang=pgmc sort=xemonu source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9091"} is an
oblique singular form within that paradigm rather than the lexeme-level
citation form [_\*xémenaz_]{.iv lang=pgmc sort=xemenaz source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9093"}.

The back-vocalic oblique stem accounts for the West Saxon target. Ringe and Taylor give
northern WGmc [_\*hebun_]{.iv lang=preoe sort=hebun source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9096"} > West Saxon and Northumbrian [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9096"}, Mercian
[_heofen_]{.iv lang=oe sort=heofen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9097"} [@RingeTaylor2014, 324]. Campbell likewise gives [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9097"} beside
[_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9098"} in the same West-Saxon _u_-umlaut environment [@Campbell1959, §210.1].

#### Old English evidence

Old English dictionaries record the standard West Saxon noun as [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9102"},
alongside Anglian or Mercian [_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9103"} material [@ClarkHall1960, 188;
@BosworthToller1898, 43]. Campbell also cites an earlier stage [_hefzen_]{.iv lang=oe sort=hefzen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9104"} in the
history of the word [@Campbell1959, §381].

The target of this entry is the West Saxon citation form [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9107"}. Its vowel
history points toward the oblique stem rather than the front-vocalic nominative
line.

#### Development to Old English

From [_\*xémonų_]{.iv lang=pgmc sort=xemonu source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9113"}, the West Saxon line passes through the oblique-stem type
reflected in northern WGmc [_\*hebun_]{.iv lang=preoe sort=hebun source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9114"} [@RingeTaylor2014, 324]. Campbell's
[_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9115"} beside [_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9115"} and earlier [_hefzen_]{.iv lang=oe sort=hefzen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9115"} show the later West-Saxon
back-mutation and suffix reshaping behind [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9116"}
[@Campbell1959, §210.1; @Campbell1959, §381].

The front-vocalic nominative line explains the dialectal [_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9119"}
type. West Saxon [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9120"} reflects the oblique
stem that was generalized into the nominative position.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the front-vocalic nominative
line from the oblique stem selected for West Saxon _heofon_.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*xémenaz_]{.iv lang=pgmc sort=xemenaz source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9130"} | front-vocalic [_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9130"} type outcome | [_hefen_]{.iv lang=oe sort=hefen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9130"} / [_heofen_]{.iv lang=oe sort=heofen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9130"} | useful control, but not the West Saxon form used here |
| selected oblique singular | [_\*xémonų_]{.iv lang=pgmc sort=xemonu source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9131"} | regular output: [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9131"} | [_heofon_]{.iv lang=oe sort=heofon source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9131"} | exact match between input, output, and target |
| older pre-OE stage | inherited oblique line | earlier [_hefzen_]{.iv lang=oe sort=hefzen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9132"} stage | [_hefzen_]{.iv lang=oe sort=hefzen source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9132"} | historical background for the same West Saxon development |

### live — OE _lifeþ_

\index[oe]{lifeth@\emph{lifeþ}}
\index[pgmc]{libena@*libēną}
\index[pgmc]{libethi@*líbēθi}

Derivation: citation reconstruction _\*libēną_; form followed here _\*líbēθi_ > _lifeþ_ (late analogy).

#### Derivation trace

Proto input: _\*líbēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*líbēθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc Long E Lowering} & \emph{*líbǣθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PGmc B Allophony & \emph{*líβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*líβæθ} \\
OE Unstressed AE Merger & \emph{*líβeθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _lifeþ_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-III weak family cited by Kroonen under
_\*libēn-_, reflected in Old English [_libban_]{.iv lang=oe sort=libban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9189"} [@Kroonen2013, 336]. Ringe and
Taylor show that the paradigm also contained a separate 3sg present stem,
continued in late Northumbrian [_lifed_]{.iv lang=oe sort=lifed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9191"}, which they treat as an archaism
[@RingeTaylor2014, 364].

The derivational input [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9194"} therefore represents a finite present cell rather
than the citation infinitive. The later lemma tradition also includes remodeled
forms such as [_lifian_]{.iv lang=oe sort=lifian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9196"}.

#### Old English evidence

The ordinary lemma tradition centers on [_libban_]{.iv lang=oe sort=libban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9200"} and, in later remodeling,
[_lifian_]{.iv lang=oe sort=lifian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9201"}. For this entry, however, the relevant comparison form is the archaic
3sg present attested as [_lifed_]{.iv lang=oe sort=lifed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9202"}, here
normalized as [_lifeþ_]{.iv lang=oe sort=lifeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9203"} [@RingeTaylor2014, 364; @Campbell1959, §762].

The target is thus a normalized finite form, not the ordinary dictionary lemma.
It preserves the older present-stem history more clearly than the remodeled
lemma tradition does.

#### Development to Old English

From [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9211"}, regular reduction of the final syllable and later weakening of
the unstressed vowel yield [_lifeþ_]{.iv lang=oe sort=lifeth role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9212"}. The attested spelling [_lifed_]{.iv lang=oe sort=lifed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9212"} belongs to the
same finite form in late Northumbrian orthography [@Campbell1959, §762;
@RingeTaylor2014, 364].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the archaic finite cell from the
ordinary infinitival and later remodeled lemma lines.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive line | [_\*libēną_]{.iv lang=pgmc sort=libena role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9223"} | OE [_libban_]{.iv lang=oe sort=libban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9223"} headword tradition | [_libban_]{.iv lang=oe sort=libban role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9223"} | establishes the lexeme, but not the Old English form here |
| 3sg present | [_\*líbēθi_]{.iv lang=pgmc sort=libethi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9224"} | regular output: [_lifeþ_]{.iv lang=oe sort=lifeth role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9224"}; attested [_lifed_]{.iv lang=oe sort=lifed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9224"} | [_lifed_]{.iv lang=oe sort=lifed role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9224"}, normalized here as [_lifeþ_]{.iv lang=oe sort=lifeth role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9224"} | selected archaic finite cell |
| later remodeled present tradition | later class-II-type forms | [_lifian_]{.iv lang=oe sort=lifian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9225"} and related finite remodeling | [_lifian_]{.iv lang=oe sort=lifian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9225"} | genuine OE development, but secondary to the cell compared here |

### man — OE _mannes_

\index[oe]{mannes@\emph{mannes}}
\index[pgmc]{mannas@*mánnas}
\index[pgmc]{mannaz@*mánnaz}

Derivation: citation reconstruction _\*mánnaz_; form followed here _\*mánnas_ > _mannes_ (late analogy).

#### Derivation trace

Proto input: _\*mánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mánnæs} \\
OE Unstressed AE Merger & \emph{*mánnes} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _mannes_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is not uniform. Kroonen cites _\*mannan-_, and
Orel has _\*mannz_ [@Kroonen2013, 354; @Orel2003, 299]. The derivational input [_\*mánnas_]{.iv lang=pgmc sort=mannas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9277"}
belongs to a different level: it is the genitive-singular cell chosen for the
Old English comparison.

The target is not the ordinary citation form. Its medial geminate precedes the
genitive ending.

#### Old English evidence

Campbell gives the paradigm [_mann_]{.iv lang=oe sort=mann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9286"}, [_man_]{.iv lang=oe sort=man role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9286"} / [_mannes_]{.iv lang=oe sort=mannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9286"} / _menn_
[@Campbell1959, §621].
Sievers-Brunner likewise cites [_man_]{.iv lang=oe sort=man role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9288"} [_mannes_]{.iv lang=oe sort=mannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9288"} [@SieversBrunner1965, §226]. He
also explains that word-final simplification underlies forms such as [_man_]{.iv lang=oe sort=man role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9289"}
beside inflected [_monnes_]{.iv lang=oe sort=monnes role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9290"} [@SieversBrunner1965, §231]. Clark Hall keeps the dictionary headword under [_mann_]{.iv lang=oe sort=mann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9290"}
[@ClarkHall1960, 197].

The relevant comparison form is therefore the attested genitive singular
[_mannes_]{.iv lang=oe sort=mannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9294"}, not the citation lemma [_mann_]{.iv lang=oe sort=mann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9294"}.

#### Development to Old English

Campbell's paradigm _mann_, _man_ / _mannes_ / _menn_ confirms the selected genitive
singular _mannes_ [@Campbell1959, §621]. In the present analysis, _\*mánnas_
develops through Anglo-Frisian brightening and later unstressed merger to
_mannes_. In this cell the geminate remains medial before _-es_. The citation
form behaves differently because word-final gemination was simplified in Old
English [@SieversBrunner1965, §231].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It separates the citation-form line from the
genitive singular.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*mannăz_]{.iv lang=pgmc sort=mannaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9312"} | expected citation-form outcome [_man_]{.iv lang=oe sort=man role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9312"} | [_mann_]{.iv lang=oe sort=mann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9312"} / [_monn_]{.iv lang=oe sort=monn role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9312"} | establishes the lexeme, but not the Old English form here |
| accusative singular | [_\*manną_]{.iv lang=pgmc sort=manna role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9313"} | expected [_man_]{.iv lang=oe sort=man role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9313"} | [_man_]{.iv lang=oe sort=man role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9313"} | same word-final simplification as the nominative |
| dative singular | [_\*mannăi_]{.iv lang=pgmc sort=mannai role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9314"} | expected [_manne_]{.iv lang=oe sort=manne role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9314"} | [_manne_]{.iv lang=oe sort=manne role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9314"} | preserves medial _nn_, but not the chosen cell |
| genitive singular | [_\*mánnas_]{.iv lang=pgmc sort=mannas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9315"} | regular output: [_mannes_]{.iv lang=oe sort=mannes role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9315"} | [_mannes_]{.iv lang=oe sort=mannes role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9315"} | exact match between input, output, and attested comparator |

### meed — OE _meorde_

\index[oe]{meorde@\emph{meorde}}
\index[pgmc]{mizdai@*mízdai}
\index[pgmc]{mizdo@*mizdō}

Derivation: citation reconstruction _\*mizdō_; form followed here _\*mízdai_ > _meorde_ (late analogy).

#### Derivation trace

Proto input: _\*mízdai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*mírdē} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
NWGmc I Lowering & \emph{*mérdē} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*méordē} \\
OE Unstressed Long Vowel Shortening & \emph{*méorde} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _meorde_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is [_\*mizdō_]{.iv lang=pgmc sort=mizdo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9370"}, but the derivational input [_\*mízdai_]{.iv lang=pgmc sort=mizdai role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9370"}
is a dative-singular cell rather than the citation form. The Old English
evidence for the _meord_ side is oblique.

The wider history of competing _mēd_ remains disputed. Kroonen and Fulk
explain it through some form of _z_-loss and compensatory lengthening
[@Kroonen2013, 410; @Fulk2018, 69], while Orel keeps
a doublet analysis [@Orel2003, 311]. The comparison here concerns the
attested oblique line _meorde_.

#### Old English evidence

The directly attested forms are obliques: [_meorde_]{.iv lang=oe sort=meorde role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9382"} as a dative singular and
[_meorda_]{.iv lang=oe sort=meorda role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9383"} as a genitive plural [@BrightCassidyRingler1971, 328; @BosworthToller1898, 647].
Lexicographers reconstruct a bare nominative [_meord_]{.iv lang=oe sort=meord role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9384"} from those obliques, while
West Saxon prose more commonly shows the competing doublet _mēd_
[@ClarkHall1960, 214; @BosworthToller1898, 647].

The target of this entry is therefore the attested oblique [_meorde_]{.iv lang=oe sort=meorde role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9388"}, not the
reconstructed lemma [_meord_]{.iv lang=oe sort=meord role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9389"} and not the better-known West Saxon citation form
_mēd_.

#### Development to Old English

Ringe and Taylor give the broader noun history as PGmc _\*mizdo_ > PWGmce _\*mizdu_ > OE _meord_ ~ _méd_ [@RingeTaylor2014, 99]. The fuller oblique-cell path modeled
here spells out the intermediate rhotacism, monophthongization, lowering,
breaking, and unstressed-shortening steps needed for the selected dative-singular
comparison.

This entry therefore follows the attested oblique line within the broader
development. It does not depend on a full decision about the history of the
competing _mēd_ tradition.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the attested oblique target from
the broader lemma history.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*mizdō_]{.iv lang=pgmc sort=mizdo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9410"} | inferred lemma outcome [_meord_]{.iv lang=oe sort=meord role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9410"} | [_meord_]{.iv lang=oe sort=meord role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9410"} | useful background, but the bare lemma is reconstructed rather than directly attested |
| selected dative singular | [_\*mízdai_]{.iv lang=pgmc sort=mizdai role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9411"} | regular output: [_meorde_]{.iv lang=oe sort=meorde role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9411"} | [_meorde_]{.iv lang=oe sort=meorde role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9411"} | exact match between derivational input and attested target |
| genitive singular | [_\*mizdōz_]{.iv lang=pgmc sort=mizdoz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9412"} | regular output: [_meorde_]{.iv lang=oe sort=meorde role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9412"} | [_meorde_]{.iv lang=oe sort=meorde role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9412"} | converges on the same attested string, but the dat.sg. has the clearest direct support |
| genitive plural control | plural oblique line | attested [_meorda_]{.iv lang=oe sort=meorda role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9413"} | [_meorda_]{.iv lang=oe sort=meorda role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9413"} | confirms the broader oblique tradition, but not the chosen singular target |

### night — OE _niht_

\index[oe]{niht@\emph{niht}}
\index[pgmc]{naxti@*náxti}
\index[pgmc]{naxtz@*náxtz}

Derivation: citation reconstruction _\*náxtz_; form followed here _\*náxti_ > _niht_ (late analogy).

#### Derivation trace

Proto input: _\*náxti_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*næxti} \\
OE Breaking & \emph{*neaxti} \\
OE I Umlaut & \emph{*niexti} \\
OE Ws Palatal Umlaut & \emph{*nixti} \\
\mbox{OE High Vowel Apocope} & \emph{*nixt} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _niht_

#### Reconstruction and comparative evidence

Ringe and Taylor cite gen.sg. _\*nahtiz_, dat.sg. _\*nahti_, and nom.pl. _\*nahtiz_ for the high-vowel side of the paradigm, and derive West Saxon [_niht_]{.iv lang=oe sort=niht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9467"}
from that side [@RingeTaylor2014, 240]. The citation reconstruction [_\*náxtz_]{.iv lang=pgmc sort=naxtz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9468"}
therefore belongs to the nominative-like headword, while the derivational input
[_\*náxti_]{.iv lang=pgmc sort=naxti role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9470"} represents the dative-singular cell.

The word later became the model for endingless datives. Ringe and Taylor
explicitly explain forms such as [_dæg_]{.iv lang=oe sort=daeg role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9473"} by analogy
with dat. sg. _niht_ < _\*nahti_ [@RingeTaylor2014, 380].

#### Old English evidence

Clark Hall lemmatizes [_niht_]{.iv lang=oe sort=niht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9478"} and cross-references forms such as [_neaht_]{.iv lang=oe sort=neaht role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9478"},
[_neht_]{.iv lang=oe sort=neht role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9479"}, and [_nieht_]{.iv lang=oe sort=nieht role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9479"} [@ClarkHall1960, 215]. Campbell likewise preserves the
fluctuation between [_neaht_]{.iv lang=oe sort=neaht role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9480"} and [_niht_]{.iv lang=oe sort=niht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9480"}, giving genitive _nihte, nihtes_,
dative _niht, nihte_, nominative plural _niht_, and the contrasting
plural-side forms represented by [_neahtas_]{.iv lang=oe sort=neahtas role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9482"} [@Campbell1959, §628.3].

The comparison form used here is therefore an attested Old English _niht_, not a
reconstructed substitute. The broader lexical record still preserves the
non-umlauted side of the paradigm in _neaht_-type forms.

#### Development to Old English

Ringe and Taylor derive West Saxon _niht_ from _\*nahti_ via _\*nehti_ and
_\*neahti_ [@RingeTaylor2014, 240]. Campbell and Brunner preserve the
contrasting non-umlauted _neaht_-type forms elsewhere in the paradigm
[@Campbell1959, §628.3; @SieversBrunner1965, §284].

The modeled path is therefore _\*náxti_ > _\*næxti_ > _\*neaxti_ > _\*niexti_ > _\*nixti_ > _niht_.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It identifies the inherited cell that matches the
attested Old English form.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*náxtz_]{.iv lang=pgmc sort=naxtz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9504"} | expected non-umlauted outcome [_neaht_]{.iv lang=oe sort=neaht role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9504"} | [_neaht_]{.iv lang=oe sort=neaht role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9504"} | useful background, but not the comparison used for _niht_ |
| selected dative singular | [_\*náxti_]{.iv lang=pgmc sort=naxti role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9505"} | regular output: [_niht_]{.iv lang=oe sort=niht role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9505"} | [_niht_]{.iv lang=oe sort=niht role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9505"} | exact match between input, output, and paradigm cell |

### rest — OE _ræste_

\index[oe]{raeste@\emph{ræste}}
\index[pgmc]{rasto@*rastō}
\index[pgmc]{rastoz@*rástōz}

Derivation: citation reconstruction _\*rastō_; form followed here _\*rástōz_ > _ræste_ (late analogy).

#### Derivation trace

Proto input: _\*rástōz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*rástō} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Surviving Bimoric O Unrounding & \emph{*rástā} \\
Anglo Frisian Brightening & \emph{*ræstǣ} \\
OE Unstressed Long Vowel Shortening & \emph{*ræstæ} \\
OE Unstressed AE Merger & \emph{*ræste} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _ræste_

#### Reconstruction and comparative evidence

Kroonen treats the noun as a feminine ō-stem [_\*rastō-_]{.iv lang=pgmc sort=rasto role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9560"}, continued by Old English
[_ræst_]{.iv lang=oe sort=raest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9561"} [@Kroonen2013, 445]. The derivational input [_\*rástōz_]{.iv lang=pgmc sort=rastoz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9561"} therefore does not replace
the lexeme-level headword. It identifies one oblique singular cell on the side of
the paradigm that yields _ræste_.

The source tradition used here labels that cell specifically as genitive
singular, but the broader local synthesis of the ō-stem paradigm shows that the
oblique singulars converge on the same front-vocalic _ræste_ side, in contrast
to a nominative singular that would remain _rast_.

#### Old English evidence

The ordinary Old English citation form is [_ræst_]{.iv lang=oe sort=raest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9572"} [@Kroonen2013, 445]. Clark
Hall likewise gives [_ræst_]{.iv lang=oe sort=raest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9573"} [@ClarkHall1960, 239]. Bosworth-Toller also preserves oblique uses of [_ræste_]{.iv lang=oe sort=raeste role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9573"}, including prepositional
examples such as on _ræste_ and _tó_ _ræste_ [@BosworthToller1898, 121].

The comparison form used here is therefore an attested oblique [_ræste_]{.iv lang=oe sort=raeste role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9576"}, not a
reconstructed surrogate. The dictionary headword [_ræst_]{.iv lang=oe sort=raest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9577"} remains an equally real
part of the Old English record.

#### Development to Old English

Once final _\*z_ is lost, the derivational input moves through the front-vocalic
oblique side of the paradigm rather than the back-vocalic nominative side. In
the modeled derivation, the surviving final long vowel is first exposed,
unrounded, fronted, shortened, and then reduced to the final _-e_ of _ræste_.

The key point is the paradigm split. Nominative _\*rastō_ yields a regular _rast_,
whereas the selected oblique input yields _ræste_. The later citation form _ræst_
is best explained as leveling from that oblique _ræst-_ stem.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the nominative citation form
from the oblique singular chosen here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*rastō_]{.iv lang=pgmc sort=rasto role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9598"} | expected regular outcome _rast_ | [_ræst_]{.iv lang=oe sort=raest role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9598"} | useful background, but not the cell that matches attested oblique _ræste_ |
| selected oblique singular | [_\*rástōz_]{.iv lang=pgmc sort=rastoz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9599"} | regular output: [_ræste_]{.iv lang=oe sort=raeste role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9599"} | [_ræste_]{.iv lang=oe sort=raeste role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9599"} | exact match between derivational input and attested OE oblique form |

### shoulder — OE _sċuldrum_

\index[oe]{sculdrum@\emph{sċuldrum}}
\index[pgmc]{skuldramiz@*skúldramiz}
\index[pgmc]{skuldro@*skuldrō}

Derivation: citation reconstruction _\*skuldrō_; form followed here _\*skúldramiz_ > _sċuldrum_ (late analogy).

#### Derivation trace

Proto input: _\*skúldramiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.560\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.280\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
NWGmc A To U Before M & \emph{*skúldrumiz} \\
PWGmc Early I Apocope & \emph{*skúldrumz} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.26\linewidth}@{\hspace{0.25em}}}
PGmc Final Z Deletion & \emph{*skúldrum} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Sk Palatalization & \emph{*ʃúldrum} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċuldrum_

#### Reconstruction and comparative evidence

The handbooks do not agree on the reconstruction of the Germanic word. Orel gives [_\*skuldr(j)ō_]{.iv lang=pgmc sort=skuldrjo role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"}, a feminine ō-/jō-stem, and explicitly notes that Old English [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"} is masculine beside OFrisian [_skulder_]{.iv lang=ofris sort=skulder role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"}, Middle Low German _schulder_, and Old High German [_scultra_]{.iv lang=ohg sort=scultra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"}, [_scultirra_]{.iv lang=ohg sort=scultirra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"} [@Orel2003, 345]. Kroonen reconstructs [_\*skuldra-_]{.iv lang=pgmc sort=skuldra role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"}, a masculine a-stem, and derives the Old High German feminine forms from [_\*skuldrjōn-_]{.iv lang=pgmc sort=skuldrjon role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"} [@Kroonen2013, 478]. Ringe and Taylor cite PWGmc [_\*skuldru_]{.iv lang=pwgmc sort=skuldru role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9654"} for the Old English branch [@RingeTaylor2014, 142].

These forms imply different stem classes and different expectations for the Old English inflection. The question is which inflectional cell best aligns with the Old English evidence.

A dative/instrumental plural form [_\*skúldramiz_]{.iv lang=pgmc sort=skuldramiz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9658"} aligns with the inherited plural ending that later yields Old English _-um_, and it corresponds directly to the attested dative plural discussed below.

#### Old English evidence

The ordinary Old English headword is [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9662"}. Clark Hall lemmatizes [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9662"} as the normal dictionary form [@ClarkHall1960, 257]. Bosworth-Toller also preserves the dative plural [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9662"} [@BosworthToller1898, 85].

Bosworth-Toller's Supplement records a weak-feminine [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9664"}, an [@BosworthToller1898, 699], so [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9664"} belongs to the Old English record beside the stronger masculine paradigm headed by [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9664"}. Brunner and Luick also record later spellings such as [_sceoldor_]{.iv lang=oe sort=sceoldor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9664"} and the i-mutated dative plural [_scyldrum_]{.iv lang=oe sort=scyldrum role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9664"}, which reflect secondary phonological and analogical reshaping within Old English [@SieversBrunner1965, §92.2.a; @Luick1914, 230].

The singular and plural evidence point to different parts of the paradigm. The relevant comparison form here is the attested dative plural [_sċuldrum_]{.iv lang=oe sort=sculdrum role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9666"}. The spelling with _sċ-_ is a normalized representation of the same Old English initial cluster.

#### Development to Old English

Proto-Germanic _\*skúldramiz_ can be interpreted as a dative/instrumental plural form. In this environment the post-tonic _a_ before _m_ is raised to _u_, giving a form of the _\*skúldrumiz_ type. Unstressed _u_ is regularly preserved before _m_, especially in the dative plural ending _-um_: Campbell states this explicitly, and Hogg formulates the same condition for the dative plural inflexion [@Campbell1959, §373; @Hogg1992, §3.3.1.3]. Brunner points in the same direction by excluding _m_ from the environments in which medial _o_ became general in West Saxon [@SieversBrunner1965, §44 Anm. 7].

Subsequent reduction of the ending removes the final _\*i_ and _\*z_, so that the inflectional ending appears in Old English as _-um_. The initial cluster is written here as _sċ-_, and the development is _\*skúldramiz_ > _\*skúldrumiz_ > _\*skúldrum_ > _sċuldrum_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that corresponds to an established Old English paradigm form. The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| singular-oriented citation input | [_\*skúldrō_]{.iv lang=pgmc sort=skuldro role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9680"} | probe output: [_sċoldor_]{.iv lang=oe sort=scoldor role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9680"} | [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9680"} | fails: the singular output has root _o_, not the attested _u_ |
| serious plural-based singular alternative | [_\*skúldru_]{.iv lang=pwgmc sort=skuldru role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9681"} | probe output: [_sċuldor_]{.iv lang=oe sort=sculdor role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9681"} | [_sculdor_]{.iv lang=oe sort=sculdor role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9681"} | close formally, but it compares a plural-stage input with a singular form |
| dat./inst.pl. input | [_\*skúldramiz_]{.iv lang=pgmc sort=skuldramiz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9682"} | regular output: [_sċuldrum_]{.iv lang=oe sort=sculdrum role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9682"} | [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9682"} | matches both the output and the dative plural comparison form |
| later weak-feminine singular | — | OE [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9683"} | [_sculdra_]{.iv lang=oe sort=sculdra role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9683"} | secondary doublet, useful as a control rather than the inherited target |

The dative plural line is decisive because it matches both the output and the paradigm cell of Old English [_sculdrum_]{.iv lang=oe sort=sculdrum role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9685"}. Singular-oriented candidates either lower the root vowel or compare unlike cells.

### shove — OE _sċēaf_

\index[oe]{sceaf@\emph{sċēaf}}
\index[pgmc]{skaub@*skáub}
\index[pgmc]{skeubana@*skéubaną}

Derivation: citation reconstruction _\*skéubaną_; form followed here _\*skáub_ > _sċēaf_ (late analogy).

#### Derivation trace

Proto input: _\*skáub_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*skáeub} \\
OE Diphthong Leveling & \emph{*skēab} \\
PGmc B Allophony & \emph{*skēaβ} \\
OE Sk Palatalization & \emph{*ʃēaβ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēaf_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*skeuban-_ ~ _\*skūban-_ and cites Old
English present forms [_scēofan_]{.iv lang=oe sort=sceofan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9739"}, [_scūfan_]{.iv lang=oe sort=scufan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9739"} [@Kroonen2013, 444]. Those
present-system forms belong to the same verb family, but the comparison here
uses the singular preterite [_\*skáub_]{.iv lang=pgmc sort=skaub role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9741"}, not the infinitive.

#### Old English evidence

The ordinary dictionary verb is [_scūfan_]{.iv lang=oe sort=scufan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9745"}/[_scēofan_]{.iv lang=oe sort=sceofan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9745"}, but the preterite itself is
well attested. Bright gives the principal parts [_scufan_]{.iv lang=oe sort=scufan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9746"}, [_sceaf_]{.iv lang=oe sort=sceaf role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9746"}, [_scufon_]{.iv lang=oe sort=scufon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9746"}, [_scofen_]{.iv lang=oe sort=scofen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9746"}
[@BrightCassidyRingler1971, 347]. Sweet gives the same paradigm [@Sweet1953, 29].
The normalized form here is [_sċēaf_]{.iv lang=oe sort=sceaf role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9748"},
regularizing the attested spellings [_sceaf_]{.iv lang=oe sort=sceaf role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9749"} and prefixed [_āsceaf_]{.iv lang=oe sort=asceaf role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9749"}.

#### Development to Old English

From _\*skáub_, the development is straightforward. _\*au_ fronts and levels to
_ēa_, final _\*b_ becomes a fricative and is written _f_, and initial _\*sk-_
undergoes the usual Old English palatalized spelling in this environment. The
derivation therefore gives _\*skáub_ > _\*skáeub_ > _\*skēab_ > _\*skēaβ_ > _sċēaf_.

#### Paradigm comparison

A paradigm comparison is needed here because the ordinary citation verb and
_sċēaf_ belong to different cells of the same strong paradigm. The comparison
below is manual.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | [_\*skéubaną_]{.iv lang=pgmc sort=skeubana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9766"} | inherited infinitive line [_sċēofan_]{.iv lang=oe sort=sceofan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9766"}; present system also leveled [_scūfan_]{.iv lang=oe sort=scufan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9766"} | [_scēofan_]{.iv lang=oe sort=sceofan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9766"} / [_scūfan_]{.iv lang=oe sort=scufan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9766"} | necessary background, but not the comparison used for _sċēaf_ |
| 1/3 sg. preterite | [_\*skáub_]{.iv lang=pgmc sort=skaub role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9767"} | documented regular output: [_sċēaf_]{.iv lang=oe sort=sceaf role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9767"} | [_sċēaf_]{.iv lang=oe sort=sceaf role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9767"} | direct match for the singular preterite |
| preterite plural | [_\*skúbun_]{.iv lang=pgmc sort=skubun role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9768"} | later leveled plural [_scufon_]{.iv lang=oe sort=scufon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9768"} beside expected [_sċufun_]{.iv lang=oe sort=scufun role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9768"} under the corrected cascade | [_scufon_]{.iv lang=oe sort=scufon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9768"} | poorer comparison for the singular-preterite target |
| past participle | [_\*skúbanaz_]{.iv lang=pgmc sort=skubanaz role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9769"} | attested participial line [_scofen_]{.iv lang=oe sort=scofen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9769"} | [_scofen_]{.iv lang=oe sort=scofen role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9769"} | valid alternative cell, but not the form compared here |

### span — OE _spanne_

\index[oe]{spanne@\emph{spanne}}
\index[pgmc]{spannai@*spánnai}
\index[pgmc]{spanno@*spannō}

Derivation: citation reconstruction _\*spannō_; form followed here _\*spánnai_ > _spanne_ (late analogy).

#### Derivation trace

Proto input: _\*spánnai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Ai Monophthongization & \emph{*spánnē} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*spánne} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _spanne_

#### Reconstruction and comparative evidence

Seebold gives Old English [_spann_]{.iv lang=oe sort=spann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9821"} under this noun family [@Seebold1970, 450].
The form followed here, [_\*spánnai_]{.iv lang=pgmc sort=spannai role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9822"}, is therefore not a rival headword, but the
specific dative singular form compared on the model of the feminine ō-stem
paradigm [@SieversBrunner1965, §252; @SieversBrunner1965, §255.2].

#### Old English evidence

The reviewed lexicographic evidence more directly supports the citation noun
[_spann_]{.iv lang=oe sort=spann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9829"} than the exact form [_spanne_]{.iv lang=oe sort=spanne role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9829"}. Clark Hall gives [_spann_]{.iv lang=oe sort=spann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9829"}
[@ClarkHall1960, 286], and [_spanne_]{.iv lang=oe sort=spanne role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9830"} is accordingly treated as the regular
dative singular form compared here rather than as a dictionary headword.

#### Development to Old English

Citation [_\*spannō_]{.iv lang=pgmc sort=spanno role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9835"} yields [_span_]{.iv lang=oe sort=span role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9835"}. The oblique cell [_\*spánnai_]{.iv lang=pgmc sort=spannai role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9835"} therefore
supplies the conservative comparison form: it preserves the medial geminate and
yields [_spanne_]{.iv lang=oe sort=spanne role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9837"}, while citation [_\*spannō_]{.iv lang=pgmc sort=spanno role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9837"} gives the nominative background form.

#### Paradigm comparison

The comparison below sets the citation form beside the dative singular form
compared here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*spannō_]{.iv lang=pgmc sort=spanno role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9846"} | regular output: [_span_]{.iv lang=oe sort=span role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9846"} | [_spann_]{.iv lang=oe sort=spann role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9846"} | useful citation-form background, but not the form compared here |
| dative singular compared here | [_\*spánnai_]{.iv lang=pgmc sort=spannai role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9847"} | regular output: [_spanne_]{.iv lang=oe sort=spanne role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9847"} | [_spanne_]{.iv lang=oe sort=spanne role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9847"} | exact match for that conservative form |

### thistle — OE _þistles_

\index[oe]{thistles@\emph{þistles}}
\index[pgmc]{thestilaz@*θéstilaz}
\index[pgmc]{thistilas@*θístilas}

Derivation: citation reconstruction _\*θéstilaz_; form followed here _\*θístilas_ > _þistles_ (late analogy).

#### Derivation trace

Proto input: _\*θístilas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.66\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.22\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*θístilæs} \\
OE L Adjacent Syncope & \emph{*θístlæs} \\
OE Unstressed AE Merger & \emph{*θístles} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _þistles_

#### Reconstruction and comparative evidence

Orel prints _\*þe(x)stilaz_ for the lexeme [@Orel2003, 458]. The comparative
label [_\*θéstilaz_]{.iv lang=pgmc sort=thestilaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9900"} therefore remains in view as the lexeme-level headword, while
the derivational input [_\*θístilas_]{.iv lang=pgmc sort=thistilas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9901"} is a specific genitive singular cell.

#### Old English evidence

The ordinary simplex headword tradition is broken [_þistel_]{.iv lang=oe sort=thistel role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9905"} / [_ðistel_]{.iv lang=oe sort=thistel role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9905"}. Clark
Hall gives [_ðistel_]{.iv lang=oe sort=thistel role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9906"} as the noun headword [@ClarkHall1960, 326]. The Old English form here
here is the genitive singular [_þistles_]{.iv lang=oe sort=thistles role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9907"}, which preserves the same stem in an
oblique form where the cluster is medial.

#### Development to Old English

Campbell's discussion of cluster nouns shows the contrast clearly. Simplex forms
often develop a parasite vowel in word-final obstruent + sonorant clusters,
while comparable medial clusters remain unbroken; his examples include _hrefn_,
_tacn_, _wépn_, and _botm_ beside forms with parasitic vowels elsewhere in the
same lexical class [@Campbell1959, 151]. The genitive singular [_\*θístilas_]{.iv lang=pgmc sort=thistilas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9916"}
therefore supplies the conservative comparison form: the cluster is medial and
the regular development yields [_þistles_]{.iv lang=oe sort=thistles role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9918"}, while the simplex nominative belongs
to the broken headword tradition [_þistel_]{.iv lang=oe sort=thistel role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9919"}.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It shows the contrast between the citation form
and the genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | [_\*θéstilaz_]{.iv lang=pgmc sort=thestilaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9928"} | computed output: [_þistl_]{.iv lang=oe sort=thistl role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9928"} | [_þistel_]{.iv lang=oe sort=thistel role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9928"} | useful citation-form background, but not the Old English form here |
| genitive singular | [_\*θístilas_]{.iv lang=pgmc sort=thistilas role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9929"} | computed output: [_þistles_]{.iv lang=oe sort=thistles role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9929"} | [_þistles_]{.iv lang=oe sort=thistles role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9929"} | exact match for the conservative cell |

### make (iptv.2sg) — OE _maca_

\index[oe]{maca@\emph{maca}}
\index[pgmc]{mako@*mákô}
\index[pgmc]{makona@*makōną}

Derivation: citation reconstruction _\*makōną_; form followed here _\*mákô_ > _maca_ (late analogy).

#### Derivation trace

Proto input: _\*mákô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mækô} \\
OE A Restoration & \emph{*makô} \\
OE Unstressed Long Vowel Shortening & \emph{*maka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _maca_

#### Reconstruction and comparative evidence

The make-family belongs to the Old English class-II weak verbs. Campbell cites
_lapian,_ [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9982"} among verbs with restored _a_ [@Campbell1959, §159]. Ringe and
Taylor place the Germanic verb in the same class, comparing West Germanic
continuants such as Old Frisian [_makia_]{.iv lang=ofris sort=makia role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9984"}, Old Saxon [_makon_]{.iv lang=os sort=makon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9984"}, and Old High German
[_mahhon_]{.iv lang=ohg sort=mahhon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9985"} [@RingeTaylor2014, 191].

The derivational input [_\*mákô_]{.iv lang=pgmc sort=mako role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9987"} is not the citation form of the lexeme but a finite
paradigm cell. Ringe and Taylor give the class-II weak imperative singular as
-a < _\*-ō_, which makes this cell the relevant comparison point for the Old
English form treated here [@RingeTaylor2014, 314].

#### Old English evidence

The dictionary headword is [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9994"} [@ClarkHall1960, 193]. The form compared here in this
entry is therefore not the lemma but the imperative singular [_maca_]{.iv lang=oe sort=maca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9995"}, chosen as a
paradigm form beside the headword [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9996"} and the related finite form [_macaþ_]{.iv lang=oe sort=macath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:9996"}.

The lexical history is still that of _macian_, but the finite cell isolates the regular outcome
of trimoric _\*ō_ more cleanly than the citation form does.

#### Development to Old English

From _\*mákô_, Anglo-Frisian brightening first gives _\*mækô_. Campbell cites
_macian_ among the class-II verbs with restored _a_ [@Campbell1959, §159].
Ringe and Taylor's class-II weak imperative singular -a < _\*-ō_ then supports
the later finite ending [@RingeTaylor2014, 314].

The same development explains why earlier fronted forms of the _mæċa_ type do
not control the entry. Once trimoric _\*ô_ is treated as a back-vocalic trigger
for restoration, the imperative singular falls into line with the broader
_macian_ family.

#### Paradigm comparison

A paradigm comparison identifies which finite cell of the make-family matches
the Old English form chosen here. The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*mákōjaną_]{.iv lang=pgmc sort=makojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10020"} | comparative continuation [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10020"} | [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10020"} | ordinary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*mákô_]{.iv lang=pgmc sort=mako role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10021"} | regular output: [_maca_]{.iv lang=oe sort=maca role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10021"} | [_maca_]{.iv lang=oe sort=maca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10021"} | exact match between input, output, and selected paradigm form |
| present third singular companion | [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10022"} | comparative companion [_macaþ_]{.iv lang=oe sort=macath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10022"} | [_macaþ_]{.iv lang=oe sort=macath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10022"} | useful family control, but not the target of this entry |

### make (3sg) — OE _macaþ_

\index[oe]{macath@\emph{macaþ}}
\index[pgmc]{makona@*makōną}
\index[pgmc]{makothi@*mákōθi}

Derivation: citation reconstruction _\*makōną_; form followed here _\*mákōθi_ > _macaþ_ (late analogy).

#### Derivation trace

Proto input: _\*mákōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*mákōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*mækōθ} \\
OE A Restoration & \emph{*makōθ} \\
OE Late O Shortening & \emph{*makaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _macaþ_

#### Reconstruction and comparative evidence

Kroonen derives the Old English verb from [_\*makōjan-_]{.iv lang=pgmc sort=makojan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10076"} on the make-family base _\*maka-_ [@Kroonen2013, 350]. Ringe and Taylor likewise derive Old English [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10076"} from PWGmc [_\*makon_]{.iv lang=os sort=makon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10076"} through _\*mekojan_ [@RingeTaylor2014, 191].

The derivational input [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10078"} is therefore a finite 3sg cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10082"} [@ClarkHall1960, 193]. The relevant comparison form here is the normalized present-third-singular [_macaþ_]{.iv lang=oe sort=macath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10082"}, set beside the dictionary headword and the related imperative singular [_maca_]{.iv lang=oe sort=maca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10082"}.

Campbell's class-II paradigm makes the ordinary 3sg ending _-aþ_, while his dialect survey allows secondary _-e-_ spellings in some traditions [@Campbell1959, §356.4; @Campbell1959, §757]. _Macaþ_ is thus the regular comparison form for the non-_j_ 3sg cell.

#### Development to Old English

After early loss of final _-i_, _\*mákōθi_ yields _\*mákōθ_. Anglo-Frisian brightening gives _\*mækōθ_, but Campbell lists _macian_ among the class-II verbs with restored _a_, so the stem returns to _mak-_ before the ending is reduced [@Campbell1959, §159].

The ending then follows the ordinary class-II 3sg development. Campbell's lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells point to _\*makōθ_ > _\*makaθ_ > _macaþ_ [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the make-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*makōjaną_]{.iv lang=pgmc sort=makojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10098"} | dictionary headword [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10098"} | [_macian_]{.iv lang=oe sort=macian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10098"} | family background, but not the cell compared here |
| 3sg present | [_\*mákōθi_]{.iv lang=pgmc sort=makothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10099"} | regular output [_macaþ_]{.iv lang=oe sort=macath role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10099"} | [_macaþ_]{.iv lang=oe sort=macath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10099"} | exact match |
| imperative singular companion | [_\*mákô_]{.iv lang=pgmc sort=mako role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10100"} | related finite form [_maca_]{.iv lang=oe sort=maca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10100"} | [_maca_]{.iv lang=oe sort=maca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10100"} | useful control, but not the target |

### bore (iptv.2sg) — OE _bora_

\index[oe]{bora@\emph{bora}}
\index[pgmc]{buro@*búrô}
\index[pgmc]{burona@*burōną}

Derivation: citation reconstruction _\*burōną_; form followed here _\*búrô_ > _bora_ (late analogy).

#### Derivation trace

Proto input: _\*búrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bórô} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*bóra} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _bora_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its continuants [@Kroonen2013, 85]. Ringe and Taylor give the class-II weak imperative singular as -a < _\*-ō_ [@RingeTaylor2014, 314].

The form followed here, _\*búrô_, is therefore an imperative cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960, 48]. The comparison form here is the normalized imperative singular _bora_, used beside the headword and the related 3sg form _boraþ_.

The imperative is thus a paradigm form rather than a replacement for the dictionary lemma. It is the most direct Old English comparator for the non-_j_ finite cell represented by _\*búrô_.

#### Development to Old English

Northwest Germanic lowering first gives _\*bórô_ from _\*búrô_, and late shortening of the unstressed long vowel then yields _\*bóra_, whence _bora_.

Ringe and Taylor's class-II imperative singular -a < _\*-ō_ points to exactly this type of outcome [@RingeTaylor2014, 314]. The form compared here therefore isolates the regular finite-cell development more cleanly than the remodelled infinitive does.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected imperative cell from the bore-family lemma and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*burōjaną_]{.iv lang=pgmc sort=burojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10174"} | dictionary headword [_borian_]{.iv lang=oe sort=borian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10174"} | [_borian_]{.iv lang=oe sort=borian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10174"} | family background, but not the cell compared here |
| imperative singular | [_\*búrô_]{.iv lang=pgmc sort=buro role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10175"} | regular output [_bora_]{.iv lang=oe sort=bora role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10175"} | [_bora_]{.iv lang=oe sort=bora role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10175"} | exact match |
| 3sg present companion | [_\*búrōθi_]{.iv lang=pgmc sort=burothi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10176"} | related finite form [_boraþ_]{.iv lang=oe sort=borath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10176"} | [_boraþ_]{.iv lang=oe sort=borath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10176"} | useful control, but not the target |

### bore (3sg) — OE _boraþ_

\index[oe]{borath@\emph{boraþ}}
\index[pgmc]{burona@*burōną}
\index[pgmc]{burothi@*búrōθi}

Derivation: citation reconstruction _\*burōną_; form followed here _\*búrōθi_ > _boraþ_ (late analogy).

#### Derivation trace

Proto input: _\*búrōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*búrōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bórōθ} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Late O Shortening & \emph{*bóraθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _boraþ_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its reflexes [@Kroonen2013, 85]. The form compared here isolates the finite 3sg cell _\*búrōθi_ rather than the infinitive.

Campbell's class-II pattern lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's account of stable _a_ in the class-II 2sg and 3sg make this finite cell the relevant comparison form for the ending [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960, 48]. The relevant comparison form here is the normalized present-third-singular _boraþ_, used beside the headword and the imperative singular _bora_.

Campbell's dialect survey allows secondary _-e-_ and _-o-_ spellings in 2sg and 3sg class-II forms, but the basic ending remains _-aþ_ [@Campbell1959, §757]. _Boraþ_ is therefore the regular comparison form for this non-_j_ 3sg cell.

#### Development to Old English

Early loss of final _-i_ first gives _\*búrōθ_ from _\*búrōθi_. Northwest Germanic lowering then produces _\*bórōθ_, and late shortening of unstressed _ō_ yields _\*bóraθ_, whence _boraþ_.

Campbell's class-II ending evidence and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells support exactly this sequence [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the bore-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*burōjaną_]{.iv lang=pgmc sort=burojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10252"} | dictionary headword [_borian_]{.iv lang=oe sort=borian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10252"} | [_borian_]{.iv lang=oe sort=borian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10252"} | family background, but not the cell compared here |
| 3sg present | [_\*búrōθi_]{.iv lang=pgmc sort=burothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10253"} | regular output [_boraþ_]{.iv lang=oe sort=borath role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10253"} | [_boraþ_]{.iv lang=oe sort=borath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10253"} | exact match |
| imperative singular companion | [_\*búrô_]{.iv lang=pgmc sort=buro role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10254"} | related finite form [_bora_]{.iv lang=oe sort=bora role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10254"} | [_bora_]{.iv lang=oe sort=bora role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10254"} | useful control, but not the target |

### learn (iptv.2sg) — OE _liorna_

\index[oe]{liorna@\emph{liorna}}
\index[pgmc]{lizno@*líznô}
\index[pgmc]{liznojana@*liznōjaną}

Derivation: citation reconstruction _\*liznōjaną_; form followed here _\*líznô_ > _liorna_ (late analogy).

#### Derivation trace

Proto input: _\*líznô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornô} \\
OE Unstressed Long Vowel Shortening & \emph{*líorna} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liorna_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10305"} ~ [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10305"} from a learn-family base of the _\*lizn-_ type [@RingeTaylor2014, 38], and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@Kroonen2013, 380]. Fulk cites the same Old English family from _\*liznō-_ [@Fulk2018, 127].

The derivational input [_\*líznô_]{.iv lang=pgmc sort=lizno role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10307"} is a finite imperative cell of that family, not the citation form of the verb.

#### Old English evidence

Clark Hall gives the ordinary headword as _leornian_ [@ClarkHall1960, 186]. Brunner, however, explicitly records _leornian, nordh. auch liorna_, and Campbell notes that beside _leornian_ Northumbrian forms with _io_ occur where original _eo_ and _io_ remain distinct [@SieversBrunner1965, §417 Anm. 10; @Campbell1959, §123 n. 2].

[_Liorna_]{.iv lang=oe sort=liorna role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10313"} can therefore be treated as an attested Northumbrian finite form, while [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10313"} remains the better-known dictionary headword.

#### Development to Old English

The form compared here develops regularly as _\*líznô_ > _\*lírnô_ by rhotacism, then _\*líornô_ by breaking before _rn_, and finally _\*líorna_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's explicit statement that no form of _liornian_ stood in an i-umlauting environment support this stem shape [@Campbell1959, §123 n. 2; @RingeTaylor2014, 247]. The West-Saxon-looking _eo_ forms belong to a different dialectal presentation of the same family.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected imperative cell from the learn-family infinitive and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*liznōjaną_]{.iv lang=pgmc sort=liznojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10327"} | Northumbrian [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10327"}; dictionary headword often [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10327"} | [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10327"} / [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10327"} | family background, but not the cell compared here |
| imperative singular | [_\*líznô_]{.iv lang=pgmc sort=lizno role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10328"} | regular output and Brunner's Northumbrian [_liorna_]{.iv lang=oe sort=liorna role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10328"} | [_liorna_]{.iv lang=oe sort=liorna role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10328"} | exact match |
| 3sg present companion | [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10329"} | related finite form [_liornaþ_]{.iv lang=oe sort=liornath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10329"} | [_liornaþ_]{.iv lang=oe sort=liornath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10329"} | useful control, but not the target |

### learn (3sg) — OE _liornaþ_

\index[oe]{liornath@\emph{liornaþ}}
\index[pgmc]{liznojana@*liznōjaną}
\index[pgmc]{liznothi@*líznōθi}

Derivation: citation reconstruction _\*liznōjaną_; form followed here _\*líznōθi_ > _liornaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líznōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*lírnōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Breaking & \emph{*líornōθ} \\
OE Late O Shortening & \emph{*líornaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liornaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10382"} ~ [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10382"} from a learn-family base of the _\*lizn-_ type [@RingeTaylor2014, 38], and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@Kroonen2013, 380]. The derivational input [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10382"} is the finite 3sg cell of that family, not the citation form of the verb.

For the ending, Campbell's lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the class-II 2sg and 3sg make the non-_j_ 3sg cell the relevant comparison point [@Campbell1959, §356.4; @RingeTaylor2014, 80].

#### Old English evidence

Clark Hall gives the ordinary headword as [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10388"} [@ClarkHall1960, 186]. Brunner records Northumbrian finite forms in _liorn-_, including [_liorna_]{.iv lang=oe sort=liorna role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10388"} and the 3sg [_liornes_]{.iv lang=oe sort=liornes role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10388"}, beside the West-Saxon-looking [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10388"} tradition [@SieversBrunner1965, §417 Anm. 10]. Campbell likewise notes Northumbrian forms with _io_ beside [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10388"} [@Campbell1959, §123 n. 2].

The relevant comparison form here is the normalized 3sg [_liornaþ_]{.iv lang=oe sort=liornath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10390"}. The directly cited Old English evidence supports the finite stem _liorn-_; the exact _-aþ_ ending follows the regular class-II 3sg pattern.

#### Development to Old English

The form compared here develops as _\*líznōθi_ > _\*lírnōθi_ by rhotacism, then _\*lírnōθ_ after early apocope of final _-i_, then _\*líornōθ_ by breaking before _rn_, and finally _\*líornaθ_ > _liornaþ_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's statement that no form of _liornian_ stood in an i-umlauting environment support the stem, while Campbell's class-II ending evidence supports the final _-aþ_ [@Campbell1959, §123 n. 2; @Campbell1959, §356.4; @RingeTaylor2014, 247].

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the selected 3sg cell from the learn-family infinitive and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*liznōjaną_]{.iv lang=pgmc sort=liznojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10404"} | Northumbrian [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10404"}; dictionary headword often [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10404"} | [_liornian_]{.iv lang=oe sort=liornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10404"} / [_leornian_]{.iv lang=oe sort=leornian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10404"} | family background, but not the cell compared here |
| 3sg present | [_\*líznōθi_]{.iv lang=pgmc sort=liznothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10405"} | regular output [_liornaþ_]{.iv lang=oe sort=liornath role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10405"} | [_liornaþ_]{.iv lang=oe sort=liornath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10405"} | exact match |
| imperative singular companion | [_\*líznô_]{.iv lang=pgmc sort=lizno role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10406"} | regular output and Brunner's Northumbrian [_liorna_]{.iv lang=oe sort=liorna role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10406"} | [_liorna_]{.iv lang=oe sort=liorna role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10406"} | useful control, but not the target |

### lick (iptv.2sg) — OE _licca_

\index[oe]{licca@\emph{licca}}
\index[pgmc]{likko@*líkkô}
\index[pgmc]{likkona@*likkōną}

Derivation: citation reconstruction _\*likkōną_; form followed here _\*líkkô_ > _licca_ (late analogy).

#### Derivation trace

Proto input: _\*líkkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*líkka} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _licca_

#### Reconstruction and comparative evidence

Ringe and Taylor give PWGmc _\*li_/_ekkōn_ continuing as Old English [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10456"}, Old Saxon [_likkon_]{.iv lang=os sort=likkon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10456"}, and Old High German [_lecchon_]{.iv lang=ohg sort=lecchon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10456"} [@RingeTaylor2014, 50]. Orel gives the fuller weak-verb reconstruction [_\*likkōjanan_]{.iv lang=pgmc sort=likkojanan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10456"} with the same Old English continuation [@Orel2003, 285].

Campbell's weak class-II discussion gives present forms such as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80]. The form treated here is therefore not that remodeled infinitive but a finite cell in bare trimoric _\*-ō_.

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_ [@BosworthToller1898, 614]. Campbell cites _liccian_ among Old English forms with preserved geminate _cc_ [@Campbell1959, §398.1]. Brunner likewise cites _liccian_ [@SieversBrunner1965, §45 Anm. 3]. The Old English evidence therefore establishes the verbal headword and its consonantal frame securely.

The Old English form here in this entry is the imperative singular [_licca_]{.iv lang=oe sort=licca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10464"}. It is a paradigm form chosen beside the headword [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10464"} and the related present [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10464"}, not a separately lemmatized citation word.

#### Development to Old English

With the stem _licc-_ established, the remaining development is brief. Campbell's class-II present endings lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ support late _-a_ in this finite cell [@Campbell1959, §356.4]. Ringe and Taylor likewise note stable _a_ in the class-II 2sg and 3sg [@RingeTaylor2014, 80]. The same stem consonantism that appears in _liccian_ is preserved here, giving _cc_ throughout the finite form.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*líkkōjaną_]{.iv lang=pgmc sort=likkojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10476"} | regular output [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10476"} | [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10476"} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*líkkô_]{.iv lang=pgmc sort=likko role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10477"} | regular output [_licca_]{.iv lang=oe sort=licca role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10477"} | [_licca_]{.iv lang=oe sort=licca role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10477"} | exact match between the derivational input and the Old English form here |
| present third singular companion | [_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10478"} | regular output [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10478"} | [_liccaþ_]{.iv lang=oe sort=liccath role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10478"} | useful family control, but not the target of this entry |

### lick (3sg) — OE _liccaþ_

\index[oe]{liccath@\emph{liccaþ}}
\index[pgmc]{likkona@*likkōną}
\index[pgmc]{likkothi@*líkkōθi}

Derivation: citation reconstruction _\*likkōną_; form followed here _\*líkkōθi_ > _liccaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líkkōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*líkkōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Late O Shortening & \emph{*líkkaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _liccaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor give PWGmc _\*li_/_ekkōn_ continuing as Old English [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10530"}, Old Saxon [_likkon_]{.iv lang=os sort=likkon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10530"}, and Old High German [_lecchon_]{.iv lang=ohg sort=lecchon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10530"} [@RingeTaylor2014, 50]. Orel gives the fuller weak-verb reconstruction [_\*likkōjanan_]{.iv lang=pgmc sort=likkojanan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10530"} with the same Old English continuation [@Orel2003, 285].

The form compared here in this entry is the non-_j_ present third singular _\*líkkōθi_, not the remodeled infinitive. Campbell states the class-II present endings as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80].

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_ [@BosworthToller1898, 614]. The same consonantal frame appears in Campbell's and Brunner's grammatical citations of _liccian_ [@Campbell1959, §398.1; @SieversBrunner1965, §45 Anm. 3]. The Old English headword is therefore clear even though the entry here is not about the citation form.

The form treated here is the present third singular [_liccaþ_]{.iv lang=oe sort=liccath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10538"}. It is a selected paradigm form beside the lemma [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10538"} and the related imperative [_licca_]{.iv lang=oe sort=licca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10538"}, not a separately lemmatized headword.

#### Development to Old English

[_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10542"} first loses final _-i_, giving _\*líkkōθ_. Campbell's class-II present endings lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ support the regular 3sg outcome _-aþ_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note stable _a_ in the class-II 2sg and 3sg [@RingeTaylor2014, 80]. Because this ending never contains _-j-_, the form does not pass through an i-umlauted _-eþ_ stage.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*líkkōjaną_]{.iv lang=pgmc sort=likkojana role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10550"} | regular output [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10550"} | [_liccian_]{.iv lang=oe sort=liccian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10550"} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular companion | [_\*líkkô_]{.iv lang=pgmc sort=likko role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10551"} | regular output [_licca_]{.iv lang=oe sort=licca role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10551"} | [_licca_]{.iv lang=oe sort=licca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10551"} | useful family control, but not the target of this entry |
| present third singular | [_\*líkkōθi_]{.iv lang=pgmc sort=likkothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10552"} | regular output [_liccaþ_]{.iv lang=oe sort=liccath role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10552"} | [_liccaþ_]{.iv lang=oe sort=liccath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10552"} | exact match between the derivational input and the Old English form here |

### show (iptv.2sg) — OE _sċēawa_

\index[oe]{sceawa@\emph{sċēawa}}
\index[pgmc]{skawo@*skáwô}
\index[pgmc]{skawona@*skawōną}
\index[ohg]{scouwon@scouwōn}
\index[ofris]{skawia@skawia}
\index[os]{skawon@skawōn}

Derivation: citation reconstruction _\*skawōną_; form followed here _\*skáwô_ > _sċēawa_ (late analogy).

#### Derivation trace

Proto input: _\*skáwô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawô} \\
OE Sk Palatalization & \emph{*ʃḗawô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawa_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as _\*skawōjanan_ and cites Old English _sceáwian_ beside Old Frisian _skawia_, Old Saxon _skawōn_, and Old High German _scouwōn_ [@Orel2003, 337]. The derivational input in this entry is not that infinitive but the imperative singular _\*skáwô_, a finite class-II cell with imperative -a < _\*-ō_ [@RingeTaylor2014, 314].

The imperative singular provides the direct comparison with the Old English form. The lexical history still belongs to the _sceáwian_ verb, but the cell compared here isolates the finite _-a_ outcome more clearly than the citation form does.

#### Old English evidence

Bright lists _scēawian_ and explicitly gives the imperative singular _scēawa_ under that headword [@BrightCassidyRingler1971, 346]. The form treated here is therefore an attested finite paradigm form, not a reconstructed convenience form.

The spelling used in this entry is normalized _sċēawa_, while Bright's glossary gives source spelling _scēawa_. The ordinary Old English headword remains _scēawian_; _sċēawa_ is the imperative singular chosen beside it.

#### Development to Old English

Campbell lists _scéawian_ under the West Germanic _\*auw_ developments [@Campbell1959, §120]. Ringe and Taylor's class-II weak imperative singular -a < _\*-ō_ supports the late finite ending that yields _sċēawa_ [@RingeTaylor2014, 314]. The result is therefore the expected finite singular form of the _scēawian_ family rather than an analogical replacement of the headword.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10624"} | regular output [_sċēawian_]{.iv lang=oe sort=sceawian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10624"} | [_scēawian_]{.iv lang=oe sort=sceawian source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10624"} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular | [_\*skáwô_]{.iv lang=pgmc sort=skawo source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10625"} | regular output [_sċēawa_]{.iv lang=oe sort=sceawa source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10625"} | [_scēawa_]{.iv lang=oe sort=sceawa source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10625"} / normalized [_sċēawa_]{.iv lang=oe sort=sceawa source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10625"} | exact match between the derivational input and the Old English form here |
| present third singular companion | [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10626"} | regular output [_sċēawaþ_]{.iv lang=oe sort=sceawath source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10626"} | [_sċēawaþ_]{.iv lang=oe sort=sceawath source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10626"} | useful family control, but not the target of this entry |

### show (3sg) — OE _sċēawaþ_

\index[oe]{sceawath@\emph{sċēawaþ}}
\index[pgmc]{skawona@*skawōną}
\index[pgmc]{skawothi@*skáwōθi}

Derivation: citation reconstruction _\*skawōną_; form followed here _\*skáwōθi_ > _sċēawaþ_ (late analogy).

#### Derivation trace

Proto input: _\*skáwōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.64\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Early I Apocope & \emph{*skáwōθ} \\
\end{tabular}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.68\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.20\linewidth}@{\hspace{0.25em}}}
OE Aw Long Diphthong & \emph{*skḗawōθ} \\
OE Sk Palatalization & \emph{*ʃḗawōθ} \\
OE Late O Shortening & \emph{*ʃḗawaθ} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _sċēawaþ_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as [_\*skawōjanan_]{.iv lang=pgmc sort=skawojanan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"} and cites Old English [_sceáwian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"} beside Old Frisian [_skawia_]{.iv lang=ofris sort=skawia role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"}, Old Saxon [_skawōn_]{.iv lang=os sort=skawon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"}, and Old High German [_scouwōn_]{.iv lang=ohg sort=scouwon role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"} [@Orel2003, 337]. The derivational input in this entry is the present third singular [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10680"}, a finite class-II cell with stable _a_ in the 3sg ending [@RingeTaylor2014, 80].

Campbell states the class-II present endings as lufas, _-aþ_ (< _-ōsi_, _-ōþi)_ [@Campbell1959, §356.4]. Ringe and Taylor likewise note that class-II weak present 2sg. _-as(t)_ and 3sg. _-aþ_ have stable _a_ [@RingeTaylor2014, 80]. The relevant comparison is therefore the 3sg cell itself, not an i-umlauted alternative.

#### Old English evidence

Bright lists the simplex headword [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10686"} and the imperative [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10686"}, and under _geond-scēawian_ also records a third singular _sceawað_ [@BrightCassidyRingler1971, 383]. The evidence thus establishes the _scēaw-_ / _sceawað_ finite-cell pattern directly.

The form written here as [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10688"} is the normalized simplex comparison form for that weak class-II pattern. It is therefore not a dictionary headword but a finite comparison form aligned with the attested _scēaw-_ evidence and the directly cited _sceawað_ ending pattern.

#### Development to Old English

Campbell lists [_scéawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10692"} under the same West Germanic _\*auw_ development [@Campbell1959, §120]. [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10692"} therefore belongs to the _scēaw-_ family before the class-II 3sg ending is applied. Campbell's chronology and Ringe and Taylor's stable-_a_ discussion show that the class-II 3sg ending gives _-aþ_, not _-eþ_ [@Campbell1959, §356.4; @RingeTaylor2014, 80]. Because the ending never contains _-j-_, no i-umlaut applies.

#### Paradigm comparison

The comparison below sets the relevant forms side by side.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | [_\*skáwōjaną_]{.iv lang=pgmc sort=skawojana role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10700"} | regular output [_sċēawian_]{.iv lang=oe sort=sceawian role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10700"} | [_scēawian_]{.iv lang=oe sort=sceawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10700"} | ordinary dictionary headword of the verb, but not the finite form compared here |
| imperative singular companion | [_\*skáwô_]{.iv lang=pgmc sort=skawo role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10701"} | regular output [_sċēawa_]{.iv lang=oe sort=sceawa role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10701"} | [_scēawa_]{.iv lang=oe sort=sceawa role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10701"} | useful family control, but not the target of this entry |
| present third singular | [_\*skáwōθi_]{.iv lang=pgmc sort=skawothi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10702"} | regular output [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10702"} | normalized [_sċēawaþ_]{.iv lang=oe sort=sceawath role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10702"}; source-side pattern _sceawað_ | exact match for the finite form compared here |

\clearpage

## Reconstructed Old English comparators

Direct attestation does not supply the required comparator in these entries.
The target is an explicitly reconstructed Old English form and carries the
corresponding evidential burden.

### knob — OE _\*cnobba_

\index[oe]{cnobba@\emph{*cnobba}}
\index[pgmc]{knubbo@*knúbbô}
\index[pgmc]{knuppaz@*knúppaz}

Derivation: citation reconstruction _\*knúppaz_; form followed here _\*knúbbô_ > _\*cnobba_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*knúbbô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*knóbbô} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Unstressed Long Vowel Shortening & \emph{*knóbba} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*cnobba_

#### Reconstruction and comparative evidence

The wider knob-family is not uniform. Kroonen's discussion of the Germanic
n-stems points to related voiced and voiceless branches within this group
[@Kroonen2011, 297]. The citation reconstruction _\*knúppaz_ represents the broader
cognate-set headword, while the form followed here, _\*knúbbô_, represents the voiced
weak-noun branch treated here.

The Old English record is uneven. The better
attested OE material belongs to the voiceless branch, but the present entry
represents the reconstructed OE form that would continue the voiced branch
behind later English knob.

#### Old English evidence

Clark Hall preserves Old English evidence of the _cnoppa_ type
[@ClarkHall1960, 79]. Those forms are genuine Old English evidence, but they
belong to the voiceless branch of the family.

The target _\*cnobba_ is a **reconstructed Old English form**, not a directly
attested one. I use it for the voiced branch because attested _cnoppa_ continues
the voiceless branch and therefore represents a different prehistory.

#### Development to Old English

From the weak-noun form followed here, _\*knúbbô_, the regular Old English outcome is
_\*cnobba_, with Proto-Germanic _kn-_ represented in Old English as _cn-_ and
with the expected weak-noun ending.

The entry therefore does not claim that _\*cnobba_ is attested. Its claim is
different: if the voiced weak-noun branch is the one to be represented, then
_\*cnobba_ is the regular Old English form corresponding to that branch.

#### Reconstruction status

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| [_\*knúbbô_ > _\*cnobba_]{.iv lang=oe display=*cnobba sort=cnobba source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10797"} | reconstructed OE form; regular derivation | reconstructed Old English form compared here |
| [_cnopp_]{.iv lang=oe sort=cnopp source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10798"} / [_cnoppa_]{.iv lang=oe sort=cnoppa source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10798"} | attested OE branch | important control form, but belongs to the voiceless branch |
| [_cnæp_]{.iv lang=oe sort=cnaep source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10799"} | attested OE form from another family | not part of the present lexeme line |

This remains the most review-sensitive item here, because the choice between
reconstructed _\*cnobba_ and attested _cnoppa_ is still a comparator-policy
question rather than a settled point of OE attestation.

### reek — OE _\*rēac_

\index[oe]{reac@\emph{*rēac}}
\index[pgmc]{raukaz@*ráukaz}
\index[pgmc]{raukiz@*ráukiz}

Derivation: citation reconstruction _\*ráukiz_; form followed here _\*ráukaz_ > _\*rēac_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*ráukaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.320\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.520\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{PGmc Final Z Deletion} & \emph{*ráuka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE Au Fronting & \emph{*ráeuka} \\
OE Diphthong Leveling & \emph{*rēaka} \\
PWGmc Final Bare A Loss & \emph{*rēak} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*rēac_

#### Reconstruction and comparative evidence

The wider noun family is represented by [_\*ráukiz_]{.iv lang=pgmc sort=raukiz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10857"} / [_\*rauki-_]{.iv lang=pgmc sort=rauki role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10857"}, with Old English
[_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10858"} as the attested noun reflex in the comparative dictionaries
[@Kroonen2013, 446; @Orel2003, 338]. The derivational input [_\*ráukaz_]{.iv lang=pgmc sort=raukaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10859"} is therefore not the
lexeme-level headword, but the form used here for the Old English derivation.

#### Old English evidence

The attested noun is [_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10864"}, not [_\*rēac_]{.iv lang=oe sort=reac role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10864"}. Clark Hall records [_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10864"} as the noun
and also preserves related forms such as [_rēcels_]{.iv lang=oe sort=recels role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10865"}; Kroonen likewise gives OE
[_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10866"} under the noun family [@ClarkHall1960, 255; @Kroonen2013, 446]. Clark
Hall and Seebold also record verbal [_rēac_]{.iv lang=oe sort=reac role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10867"} as the preterite of [_rēocan_]{.iv lang=oe sort=reocan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10867"}, but
that verbal form is separate from the noun treated here [@ClarkHall1960, 254;
@Seebold1970, 380].

The Old English form here [_\*rēac_]{.iv lang=oe sort=reac role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10871"} is therefore a reconstructed West Saxon noun form,
not a directly attested manuscript headword.

#### Development to Old English

From [_\*ráukaz_]{.iv lang=pgmc sort=raukaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10876"}, the regular West Saxon development gives [_\*rēac_]{.iv lang=oe sort=reac role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10876"}. The attested
noun [_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10877"} belongs to the same lexical family, but reflects a later smoothed
surface form rather than the regular noun target represented here.

#### Form note

The distinction here is between an attested noun headword [_rēc_]{.iv lang=oe sort=rec role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10882"} and a
reconstructed regular West Saxon target [_\*rēac_]{.iv lang=oe sort=reac role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10883"}. The latter is treated as the
modelling target, while the former remains philological background.

### strew — OE _\*strīeġan_

\index[oe]{striegan@\emph{*strīeġan}}
\index[pgmc]{strawjana@*stráwjaną}

Derivation: _\*stráwjaną_ > _\*strīeġan_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*stráwjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\footnotesize
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.280\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.560\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.62\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.28\linewidth}@{\hspace{0.25em}}}
OE Awj Glide Formation & \emph{*stráujaną} \\
OE Au Fronting & \emph{*stráeujaną} \\
OE Diphthong Leveling & \emph{*strēajaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*strēajan} \\
OE Secondary Nasalization & \emph{*strēająn} \\
OE I Umlaut & \emph{*strīejąn} \\
OE Weak Tail Reduction & \emph{*strīejan} \\
OE J Strengthening After Front Diphthong & \emph{*strīeʒan} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Old English form: _\*strīeġan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited weak verb as [_\*straujan-_]{.iv lang=pgmc sort=straujan role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10941"} and gives Old English
[_streowian_]{.iv lang=oe sort=streowian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10942"} as its dictionary continuation [@Kroonen2013, 483]. Ringe and
Taylor distinguish the two Old English formations: the inherited class-I verb is
continued by Anglian [_strēgan_]{.iv lang=oe sort=stregan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10944"}, while West Saxon [_streowian_]{.iv lang=oe sort=streowian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10944"} is a
remodelled class-II verb [@RingeTaylor2014, §6.1 n. 27].

Luick groups _\*strauwjan_ with the same set as _\*hauwja-_ and _\*kauwjan_,
yielding Anglian _strēzan_ beside West
Saxon forms of the _hīez_, ciezan type [@Luick1914, §98]. Fulk likewise allows
an early West Saxon _\*striegan_ directly from Proto-Germanic _\*straujana_
[@Fulk2018, §4.10 n. 1].

#### Old English evidence

The attested inherited Old English form is _strēgan_ in Anglian. The
attested West Saxon citation forms are _strewian_, _streowian_, and
_strēawian_, which belong to the remodelled class-II branch
[@RingeTaylor2014, §6.1 n. 27; @Campbell1959, §753.7].

The target [_\*strīeġan_]{.iv lang=oe sort=striegan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10960"} is therefore a **reconstructed Old English form**, not
an attested manuscript lemma. It is the inferred West Saxon reflex of the
inherited class-I verb; the attested West Saxon lemma belongs to the remodelled
class-II formation.

#### Development to Old English

From _\*stráwjaną_, the inherited West Saxon development passes through
_\*straujaną_, fronting and leveling to a _\*strēajan-_ stage, i-umlaut to
_\*strīejan_, and retention or strengthening of the glide after the front
diphthong, written here as _ġ_. The resulting form is _\*strīeġan_.

This differs from Anglian _strēgan_, where smoothing removes the diphthongal
sequence, and from West Saxon _strewian_ / _streowian_ / _strēawian_, where the
verb has already been remodelled into class II [@Fulk2018, §4.10 n. 1;
@Campbell1959, §753.7].

#### Reconstruction status

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| [_strēgan_]{.iv lang=oe sort=stregan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10981"} | attested Anglian inherited class-I form | proves that the inherited verb survived into Old English |
| [_\*strīeġan_]{.iv lang=oe sort=striegan role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10982"} | reconstructed West Saxon inherited class-I form; trace-supported | Old English form here |
| [_strewian_]{.iv lang=oe sort=strewian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10983"} / [_streowian_]{.iv lang=oe sort=streowian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10983"} / [_strēawian_]{.iv lang=oe sort=streawian role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:10983"} | attested remodelled West Saxon class-II forms | genuine OE evidence, but not the inherited branch modeled here |

\clearpage

## Known but unmodelled remodellings

The historical remodeling is known, but it cannot be derived by sound change
alone. Naming the process explains the mismatch without pretending that the
attested form is phonologically regular.

### fire — OE _fȳre_

\index[oe]{fyre@\emph{fȳre}}
\index[pgmc]{furi@*fūri}

Derivation: _\*fūri_ yields regular _fȳr_; the Old English form here is _fȳre_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*fūri_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
OE I Umlaut & \emph{*fȳri} \\
\mbox{OE High Vowel Apocope} & \emph{*fȳr} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _fȳr_

Old English form: _fȳre_

#### Reconstruction and comparative evidence

Kroonen places the lexeme in a heteroclitic family _\*fōr_ ~ _\*fun-_ and explains
the front-mutated West Germanic forms from an oblique form of the
_\*fu(w)eri_ type [@Kroonen2013, 151]. The derivational input [_\*fūri_]{.iv lang=pgmc sort=furi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11046"} therefore does not
function as an arbitrary substitute for the headword: it represents the
specific inherited cell that supplies the _i_ needed for i-umlaut.

The Old English target combines a regular inherited form
[_fȳr_]{.iv lang=oe sort=fyr role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11051"} with an attested analogical surface form [_fȳre_]{.iv lang=oe sort=fyre role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11051"}.

#### Old English evidence

Bosworth-Toller records [_fyr_]{.iv lang=oe sort=fyr role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11055"} as the noun 'fire' and also preserves oblique
[_fyre_]{.iv lang=oe sort=fyre role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11056"} in the Old English record [@BosworthToller1898, 288]. The first is the
regular inherited outcome of the phonological development from the selected
input; the second shows the later restoration of a final _-e_ within the
paradigm.

The entry therefore concerns the relation between a regular inherited oblique
input and an attested Old English surface form that has undergone later
morphological remodeling.

#### Development to Old English

From [_\*fūri_]{.iv lang=pgmc sort=furi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11067"}, i-umlaut changes _ū_ to _ȳ_ [@Hogg1992, §3.3.3.1]. Subsequent
loss of the final high vowel after a heavy syllable yields [_fȳr_]{.iv lang=oe sort=fyr role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11068"}
[@Campbell1959, §345]. The inherited phonology is complete at that point.

[_fȳre_]{.iv lang=oe sort=fyre role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11071"} is later than that inherited output. Its final _-e_ belongs to
analogical restoration in the Old English paradigm rather than to the original
Proto-Germanic ending. The form therefore remains a known but unmodelled
remodelling: the deterministic phonology is regular, but the attested surface
form includes later morphological rebuilding.

#### Paradigm comparison

The comparison below sets the relevant forms side by side. It distinguishes the lexeme-level etymological
background from the inherited cell that actually produces the front-mutated
form and from the later analogical surface result.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level heteroclitic headword | _\*fōr_ ~ _\*fun-_ | comparative background only | fire family | explains the wider lexeme, but not the selected oblique input |
| inherited oblique cell | [_\*fūri_]{.iv lang=pgmc sort=furi role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11086"} | regular output: [_fȳr_]{.iv lang=oe sort=fyr role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11086"} | [_fȳr_]{.iv lang=oe sort=fyr role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11086"} | regular inherited output from the derivational input |
| later analogical surface form | — | attested [_fȳre_]{.iv lang=oe sort=fyre role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11087"} with restored _-e_ | [_fȳre_]{.iv lang=oe sort=fyre role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11087"} | genuine OE target, but not the direct phonological output |

### tap — OE _tæppa_

\index[oe]{taeppa@\emph{tæppa}}
\index[pgmc]{tappo@*táppô}

Derivation: _\*táppô_ yields regular _tappa_; the Old English form here is _tæppa_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*táppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.300\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.540\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
Anglo Frisian Brightening & \emph{*tæppô} \\
OE A Restoration & \emph{*tappô} \\
OE Unstressed Long Vowel Shortening & \emph{*tappa} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _tappa_

Old English form: _tæppa_

#### Reconstruction and comparative evidence

Orel gives the noun under _\*tappòn_ and already connects it with Old English
[_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11142"} [@Orel2003, 402]. The derivational input [_\*táppô_]{.iv lang=pgmc sort=tappo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11142"} is therefore the inherited noun itself;
the entry does not depend on a different lexeme-level proto or a different
inherited noun cell.

#### Old English evidence

The Old English noun family is well attested. Orel gives [_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11148"}, and Clark
Hall records [_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11149"} together with derivatives _tæppere_ and _tæppestre_
[@Orel2003, 402; @ClarkHall1960, 305]. The target is therefore a real Old English noun
form, not a reconstructed convenience spelling.

#### Development to Old English

From [_\*táppô_]{.iv lang=pgmc sort=tappo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11155"}, the regular inherited noun path gives [_tappa_]{.iv lang=oe sort=tappa role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11155"}. The attested
target [_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11156"} therefore stands outside that regular phonological development.

The mismatch is historically intelligible, but it is not solved here by a new
inherited input. A related j-verb pathway would give [_teppan_]{.iv lang=oe sort=teppan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11159"}, not the noun
target [_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11160"}. The entry accordingly remains a known but unmodelled case.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | [_\*táppô_]{.iv lang=pgmc sort=tappo role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11166"} | regular output: [_tappa_]{.iv lang=oe sort=tappa role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11166"} | regular output, but not the target |
| attested OE target | — | [_tæppa_]{.iv lang=oe sort=taeppa role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11167"} | genuine target form, but analogically remodelled in the present classification |
| related j-verb background | [_\*táppjaną_]{.iv lang=pgmc sort=tappjana role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11168"} | [_teppan_]{.iv lang=oe sort=teppan role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11168"} | related formation, but not the noun target |

\clearpage

## Unexplained or deliberately unmodelled exceptions

No sufficiently supported account yet reconciles the regular output with the
Old English form. An ad hoc sound law would conceal rather than explain the
mismatch.

### buck — OE _bucc_

\index[oe]{bucc@\emph{bucc}}
\index[pgmc]{bukkaz@*búkkaz}

Derivation: _\*búkkaz_ yields regular _bocc_; the Old English form here is _bucc_ (unexplained exception).

#### Derivation trace

Proto input: _\*búkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*bókkaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*bókka} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*bókk} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _bocc_

Old English form: _bucc_

#### Reconstruction and comparative evidence

Kroonen and Orel both reconstruct the word with a geminate stop, [_\*bukkaz_]{.iv lang=pgmc sort=bukkaz role=source_protoform source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11231"}
[@Kroonen2013, 121; @Orel2003, 61]. Orel also preserves parallel n-stem
material behind Old English [_bucca_]{.iv lang=oe sort=bucca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11233"} [@Orel2003, 62]. The derivational input
therefore remains identical with the lexeme label: no alternative inherited
cell accounts for the form.

#### Old English evidence

Old English preserves a mixed lexical picture. Campbell cites [_bucca_]{.iv lang=oe sort=bucca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11239"} in the
exception set for this phonological environment [@Campbell1959, §115]. Clark
Hall and Bosworth-Toller show that Old English has both [_bucca_]{.iv lang=oe sort=bucca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11241"} and [_bucc_]{.iv lang=oe sort=bucc role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11241"}
[@ClarkHall1960, 53; @BosworthToller1898, 122]. The a-stem citation form [_bucc_]{.iv lang=oe sort=bucc role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11242"}
is the target treated here; [_bucca_]{.iv lang=oe sort=bucca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11243"} supplies genuine philological
background from the same lexical family.

#### Development to Old English

From [_\*búkkaz_]{.iv lang=pgmc sort=bukkaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11248"}, the regular inherited path gives [_bocc_]{.iv lang=oe sort=bocc role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11248"}. That is the form
expected under the ordinary lowering pattern in this environment. [_bucc_]{.iv lang=oe sort=bucc role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11249"}
therefore remains outside the deterministic phonology.

No accepted inherited cell repairs the mismatch. A high-vowel alternative would
introduce i-umlaut and produce a [_byċċ_]{.iv lang=oe sort=bycc role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11253"}-type form rather than the target.
[_bucc_]{.iv lang=oe sort=bucc role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11254"} is therefore best treated as a documented exception, not as a regular
paradigm-cell survival.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | [_\*búkkaz_]{.iv lang=pgmc sort=bukkaz role=selected_input source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11261"} | regular output: [_bocc_]{.iv lang=oe sort=bocc role=regular_output source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11261"} | regular output, but not the target |
| attested OE target | — | [_bucc_]{.iv lang=oe sort=bucc role=target_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11262"} | genuine target form, but unexplained in the present classification |
| parallel OE lexical background | — | [_bucca_]{.iv lang=oe sort=bucca role=comparison_form source_ref="Germanic/docs/assembly/lexical_volume_alpha_01.md:11263"} | related n-stem form, not the present target |

### fowl — OE _fugol_

\index[oe]{fugol@\emph{fugol}}
\index[pgmc]{fuglaz@*fúglaz}
\index[on]{fugl@fugl}
\index[ohg]{fogal@fogal}

Derivation: _\*fúglaz_ yields regular _fogol_; the Old English form here is _fugol_ (unexplained exception).

#### Derivation trace

Proto input: _\*fúglaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.440\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.440\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*fóglaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*fógla} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*fógl} \\
OE Epenthetic Vowel & \emph{*fógol} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _fogol_

Old English form: _fugol_

#### Reconstruction and comparative evidence

The noun is the ordinary Germanic a-stem _\*fúglaz_, continued by forms such as
Old Norse _fugl_ and Old High German _fogal_ [@Kroonen2013, 197; @Orel2003,
155]. There
is no stem-class or paradigm-cell dispute behind this entry. The comparative
headword and the derivational input are the same.

The difficulty lies instead in the stressed root vowel. Under the regular West
Germanic and Old English development, that _u_ should lower before the following
non-high vowel, yielding an _o_-vocalism
[@RingeTaylor2014, 42–43; @Campbell1959, 43].

#### Old English evidence

Old English dictionaries record the noun as _fugol_, with variant spelling
_fugel_ [@BosworthToller1898, 282; @ClarkHall1960, 138]. The target is therefore an
attested ordinary Old English noun, not a reconstructed or selectively chosen
paradigm form.

The attested word already contains the crucial problem. Its medial _-o-_ is the
ordinary parasite vowel of Old English cluster phonology, but the root _fu-_
retains _u_ where the regular history predicts _fo-_ [@Campbell1959, 150].

#### Development to Old English

From _\*fúglaz_, the regular cascade yields _fogol_: the root vowel lowers before
the following non-high vowel [@RingeTaylor2014, 42–43; @Campbell1959, 43],
final _z_ is lost, and the cluster is resolved by the usual medial vowel
[@RingeTaylor2014, 345; @Campbell1959, 150]. That is the expected inherited
outcome.

The attested Old English noun is _fugol_, not _fogol_. Luick and later
handbooks treat this preservation of _u_ as a small inherited residue, not as a
categorical sound law [@Luick1914, 148; @RingeTaylor2014, 47]. The item
therefore remains a genuine lexical exception rather than
the output of a recoverable regular mechanism.

#### Expected and attested forms

The comparison below sets the relevant forms side by side. It distinguishes the regular prediction from the
attested Old English noun.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _fogol_ | computed regular output from _\*fúglaz_ | establishes the expected inherited outcome |
| _fugol_ | attested Old English form | Old English form here; preserves unexplained root _u_ |
| _fugel_ | attested variant spelling | secondary spelling variant of the attested noun |

The unresolved point lies only in the root vowel. The medial _-o-_ is regular,
but no accepted lautgesetzlich pathway has been found from _\*fúglaz_ to
attested _fugol_.

### rust — OE _rust_

\index[oe]{rust@\emph{rust}}
\index[pgmc]{rusto@*rústō}

Derivation: _\*rústō_ yields regular _rost_; the Old English form here is _rust_ (unexplained exception).

#### Derivation trace

Proto input: _\*rústō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*róstō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*róstu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*róst} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _rost_

Old English form: _rust_

#### Reconstruction and comparative evidence

The comparative dictionaries do not support a single citation reconstruction
uniformly. Orel cites _\*rustaz_ sb.m./f. with Old English _rust_ and Old Saxon
and Old High German _rost_ [@Orel2003, 308]. The form _\*rústō_ therefore stands here
as a competing citation reconstruction rather than as the best-supported
inherited headword.

That disagreement does not remove the central problem. Whether one starts from
_\*rústō_ or from source-supported _\*rustaz_, the regular citation-form history
points toward _rost_, not toward the attested Old English noun.

#### Old English evidence

The Old English noun is attested, not reconstructed. Clark Hall gives _rūst_ m.
[@ClarkHall1960, 245], and Bosworth-Toller records _rúst_ (? and rust)
[@BosworthToller1898, 677]. The form is normalized here as _rust_ from that attested
record.

Those dictionary entries identify a masculine noun, which aligns better with
Orel's _\*rustaz_ than with the competing _\*rústō_
preserved in the header.

#### Development to Old English

Under Campbell's regular lowering of stressed _u_ before a following mid or low
vowel, the citation-form input gives _rost_, not _rust_ [@Campbell1959, §115].
The same lowering would also affect comparative citation-form reconstructions
such as _\*rustaz_.

A high-vowel comparator such as instrumental-type _\*rústu_ would yield _rust_
regularly, but that does not explain the attested citation form of the noun. No
accepted regular pathway from the citation form to attested _rust_ has been
established.

#### Expected and attested forms

The comparison below sets the regular inherited outcomes beside the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*rústō_ > _rost_ | computed regular output from one competing citation reconstruction | shows that this citation reconstruction does not reach attested _rust_ |
| _\*rustaz_ > _rost_ | expected regular output from the source-supported citation reconstruction | shows that correcting the stem class does not solve the vowel problem |
| _\*rústu_ > _rust_ | regular high-vowel comparator | useful negative control, but not a defensible citation-form solution |
| _rust_ | attested Old English noun, normalized from _rūst_ / _rúst_ / _rust_ | attested Old English form; the citation-form development remains unexplained |

### wolf — OE _wulf_

\index[oe]{wulf@\emph{wulf}}
\index[pgmc]{wulfaz@*wúlfaz}

Derivation: _\*wúlfaz_ yields regular _wolf_; the Old English form here is _wulf_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúlfaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.540\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.300\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*wólfaz} \\
\mbox{PGmc Final Z Deletion} & \emph{*wólfa} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.70\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
PWGmc Final Bare A Loss & \emph{*wólf} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _wolf_

Old English form: _wulf_

#### Reconstruction and comparative evidence

The inherited noun is an a-stem: Kroonen gives _\*wulfa-_, and Ringe and Taylor
list PGmc _\*wulfaz_ among the inherited words that preserve _u_ in Old English
beside Old High German _wolf_ [@Kroonen2013, 638; @RingeTaylor2014, 47]. Campbell
accordingly names Old English _wulf_ as an exception to the regular lowering of
stressed _u_ before a following non-high vowel [@Campbell1959, §115].

The older literature often notices that the exceptional words cluster near
labials. Bülbring lists _full_, _wulle_, and _wulf_ together, but he also says
that the ordinary rule still gives _o_ in comparable forms such as _folc_ and
_bolt_ [@Bulbring1902, §116]. Luick rejects a categorical labial blocker on the
same grounds and prefers a lexical or analogical account instead
[@Luick1914, 148].

#### Old English evidence

Campbell treats _wulf_ as part of the exceptional _u_ set
[@Campbell1959, §115]. Sievers-Brunner notes that oblique _wulfe_ continues
_wulfi_ or older _wulfai_ [@SieversBrunner1965, §160].

The surviving oblique forms do not supply a regular route back to bare _wulf_.
They belong to the same lexeme, but they do
not remove the explanatory problem presented by the citation form.

#### Development to Old English

Under the ordinary Northwest Germanic lowering of stressed _u_ before a
following non-high vowel, the citation-form input would point toward
_o_-vocalism [@RingeTaylor2014, 42-44]. The compact trace shows exactly that
path: _\*wúlfaz_ > _\*wólfaz_ > _\*wólfa_ > _wolf_.

A high-vowel oblique input would behave differently. There the following high
vowel would block the lowering of _u_, but the same environment
would also trigger i-umlaut, so the regular control result would be _wylf_ or
_wylfe_, not bare _wulf_. The attested noun therefore remains unexplained at
the citation-form level.

#### Expected and attested forms

The comparison below sets the regular inherited outcomes beside the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúlfaz_ > _wolf_ | computed regular output from the citation form | shows the regular development expected from the inherited a-stem |
| _OHG wolf_ | comparative regular cognate | confirms that the _o_-vocalism is the ordinary outcome |
| _\*wúlfi_ / _\*wúlfis_ > _wylf_ / _wylfe_ | expected high-vowel control forms | shows why oblique high-vowel cells do not solve the noun's vowel history |
| _wulf_ | attested Old English noun | attested Old English form; the preservation of _u_ remains unexplained |

### wool — OE _wull_

\index[oe]{wull@\emph{wull}}
\index[pgmc]{wullo@*wúllō}

Derivation: _\*wúllō_ yields regular _woll_; the Old English form here is _wull_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúllō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}p{0.460\linewidth}>{\centering\arraybackslash}X>{\raggedright\arraybackslash}p{0.460\linewidth}@{}}
\begin{minipage}[t]{\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{NWGmc U Lowering} & \emph{*wóllō} \\
\mbox{NWGmc Final Long O Raising} & \emph{*wóllu} \\
\end{tabular}
\end{minipage}
&
&
\begin{minipage}[t]{\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.74\linewidth}@{\hspace{0.55em}}>{\raggedright\arraybackslash}p{0.16\linewidth}@{\hspace{0.25em}}}
\mbox{OE High Vowel Apocope} & \emph{*wóll} \\
\end{tabular}
\end{minipage}
\\
\end{tabularx}
\end{minipage}%
}
\endgroup

Regular outcome: _woll_

Old English form: _wull_

#### Reconstruction and comparative evidence

The inherited form is a feminine ō-stem _\*wúllō_. In the ordinary phonological
history of West Germanic, stressed _u_ lowers before a following non-high vowel,
so the regular Old English outcome is an _o_-form. Campbell's discussion of the
parallel adjective _full_, with OHG _foll_ as the regular comparator, shows that
the handbooks treat this as a genuine exception cluster rather than as a place
where the rule itself is doubtful [@Campbell1959, §115].

Bülbring likewise lists _wulle_ among the traditional _u_-preserving
exceptions [@Bulbring1902, §116]. The comparative evidence therefore establishes
two things at once: the regular result should be _woll_, and Old English still
has a lexical exception of the _wull_ / _wulle_ type.

#### Old English evidence

The Old English target is given here as _wull_, a normalized lexeme form.
Handbook discussion often cites _wulle_, the feminine weak form of the noun
[@Bulbring1902, §116]. Both point to the same lexical item and to the same
exceptional preservation of root _u_.

The OE evidence therefore does not remove the problem. It confirms that the
language has a _u_-form where the regular phonology would have produced _o_.

#### Development to Old English

From _\*wúllō_, the regular sequence is lowering of stressed _u_ before a
non-high vowel, followed by the ordinary later reductions of the ending. The
regular outcome is therefore _woll_.

That regular derivation is not the attested Old English form. Luick rejects a
simple phonological rule that would protect this word alone, and Ringe and
Taylor state the larger problem plainly: we do not really know why _\*u_ failed
to lower in forms of this sort [@Luick1914, 148; @RingeTaylor2014, §2.3.1].

#### What remains unexplained

The comparison below sets the regular result beside the attested lexical exception.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúllō_ > _woll_ | regular output | shows what the deterministic sound laws produce |
| _wull_ / _wulle_ | attested OE exception | attested Old English form to be recorded |
| high-vowel escape from another paradigm cell | unsupported for this noun | rejected because the feminine ō-stem paradigm supplies no suitable escape cell |

\clearpage

## References

\backmatter

# References



::: {#refs}

:::



\part*{Index verborum}

\addcontentsline{toc}{part}{Index verborum}

\printindex[oe]

\printindex[pgmc]

\printindex[pwgmc]

\printindex[on]

\printindex[ohg]

\printindex[ofris]

\printindex[goth]

\printindex[os]

\printindex[dutch]

\printindex[german]

\printindex[modeng]
