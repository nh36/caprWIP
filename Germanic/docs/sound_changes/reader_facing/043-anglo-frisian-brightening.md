# Ordinary English fronting

## Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

Wright and Wright (§57) explain the root vowel of *flasce* 'flask' by
retention of Germanic \emph{*a} before \emph{*sk} when the following
syllable originally contained a back vowel. Their formulation also covers
\emph{*st} and most geminates. Two of their examples, *wascan* 'wash' and
*masc/max* 'net, mesh', allow the same root vowel through fronting followed
by restoration. In the infinitive the following \emph{*a} is still present
at restoration. In the reconstructed neuter plural of 'net', \emph{*u}
can trigger restoration before its loss. The front-vowel infinitive
*wæscan* 'wash' remains unexplained by either derivation. Applying the wider
retention condition at first fronting also gives predicted [raste]{.pred}
for the selected input of *ræste* 'rest'. The historical force of that
comparison depends on the reconstruction of the stem. Wright and Wright
discuss *rest* under i-umlaut in §56
[@Wright1908, pp. 37--38, §§56--57;
@HoggGrammar2011, pp. 93--96, §§5.35--5.38].

The model therefore retains first fronting followed by restoration.
A restriction on fronting before final \emph{*skā} gives the back vowel
of *flasce* and *asce* 'ashes', but the comparisons provide no independent
evidence for that restriction. CAPR declines to adopt the retention rule;
the evidence leaves the historical possibility open. The working
explanation of singular *flasce* is extension of the back vowel from
inflected forms such as *flascan*, as proposed by Campbell and Luick.
The selected nominative plural now follows regular restoration and
late ending reduction, without adopting root retention. Its history is discussed in
[Chapter 3](#weak-n-paradigms-after-apocope)
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161].

The traditional name does not itself establish one inherited event.
Under Campbell's premise that the daughter contractions precede ordinary
fronting, comparable English and Frisian outcomes require separate
daughter frontings in the strict tree. Chapter 3 develops that conditional
argument without removing the ancestral node
[@Campbell1939, pp. 90–91].
The model adopts the completed ordinary English stressed component on the
English daughter under this conventional working account. This is not a
claim that every author proves contraction before ordinary fronting:
Ringe and Taylor explicitly question whether diphthong nuclei must behave
like the plain short vowel [@RingeTaylor2014, pp. 170--175].
Earlier restricted ancestral fronting remains possible.

Fulk's surviving fronted \emph{*æi} and proposed paradigmatic levelling
provide a competing account, discussed in Chapter 3, rather than direct
confirmation of contraction before ordinary fronting
[@Fulk1998, pp. 143--145]. No shared fronting is demonstrated merely
by making that alternative compatible with the daughter outcomes.

The separately retained unstressed and final-vowel components are not dated
by that argument. The first supplies an earlier nonnasal contribution;
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) separately
implements the broader unstressed domain, including the contrast between
coda and heterosyllabic nasals [@Campbell1959, pp. 140--141, §§333--334].
The second carries the model's preserved final-vowel quantity into later
shortening and merger. Its long intermediate is a representation choice,
not independent evidence for a historical long-vowel fronting
[@RingeTaylor2014, pp. 58--59, 299--300].

## SC043. Fronting of low \emph{*a} outside nasal environments (`EAFBrightening`) {#rule-EAFBrightening}

```foma
define EAFBrightening Ctx([ EAFBrighteningStressed ]);
```

### Stressed component

The secondary-stressed short vowel is kept distinct until breaking. The
precomposed \emph{ǽ} carries fronted secondary \emph{à}; it is short and
is not a new primary accent or a long vowel. Decoding the annotation is
not a claim about the historical loss of subordinate stress
[@HoggGrammar2011, pp.217--218, §§6.7--8; @Russom2001, pp.39--64].

```foma
define EAFBrighteningStressed [ {*á} -> {*æ} || _ [EnglishStarConsonant -
    EnglishStarNasal | .#.] ]
    .o. [ {*à} -> {*ǽ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.] ];
```

Slay requires breaking to receive the fronted root vowel:
\emph{*sláxan-} → \emph{*slæxan-} → \emph{*sleaxan-}. With the
back-vowel fallback excluded, moving
[SC044 OEBreaking](#rule-OEBreaking) before this stressed contribution
leaves predicted [slæan]{.pred}, rather than *slēan* 'slay'.
The older whole-bundle trial's \emph{sleaan | slēaan} additionally
activated an unsupported quantity shortcut; it was not a clean
measurement of the fronting feeder alone.
Rest involves two different changes, root fronting and the separately
retained final-vowel representation. Its final-vowel dependency must not
be used to date this stressed rule.
