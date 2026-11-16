# Breaking

## Historical discussion

Breaking is a family of conditioned developments of stressed front
vowels, not one identical environment for every vowel. In the conventional
account short \emph{æ}, \emph{e} and \emph{i} acquire short diphthongs;
inherited long front vowels have a separate long outcome before \emph{h}.
The low-vowel history of *slēan* 'slay' is
\emph{*slæxan-} → \emph{*sleaxan-}, with length arising only in the
subsequent loss-and-contraction history. A following weak ending does not
itself justify making short \emph{a} directly into long \emph{ēa}
[@Campbell1959, pp.54--59, §§139--154; p.98, §234;
@HoggGrammar2011, pp.81--88, §§5.15--25;
@RingeTaylor2014, pp.177--178, 186--188;
@Fulk2018, pp.73--75, §4.13 and n.5].

The southern covered-\emph{l} outcomes, such as *healf* 'half' and
*eall* 'all', must be distinguished from Anglian *half* and *all*.
Hogg permits failure of the first fronting in that environment, whereas
Ringe and Taylor defend fronting followed by retraction. Supplying back
\emph{*a} rather than front \emph{*æ} to a breaking rule does not decide
between those accounts. The palatal \emph{ll} of *hell* 'hell' and
*sellan* 'give, sell' is a different contrast: it does not trigger the
ordinary southern breaking. The earlier gemination retains the following
\emph{j} needed to express that contrast here. Neither gemination in
general nor the mere spelling \emph{ll} is an exclusion
[@Campbell1959, pp.54--56, §§139, 143--145;
@HoggGrammar2011, pp.81--85, §§5.15--20;
@RingeTaylor2014, pp.184--186; @Fulk1998, pp.145--146].

## SC044. Vowel-specific breaking (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking FootCtx(OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI
    .o. OEBreakingLong
    .o. [{*ǽ} -> {*æ},
    {*à} -> {*a},
    {*è} -> {*e}]);
```

### Short low front vowel {#rule-OEBreakingA}

```foma
define OEBreakingA [ {*æ} -> {*ea} || .#. OEAnyConsonant* _ EnglishBreakingRContext,
    {*æ} -> {*ea} || .#. OEAnyConsonant* _ EnglishBreakingLContext,
    {*æ} -> {*ea} || .#. OEAnyConsonant* _ EnglishBreakingHContext ]
    .o. [ {*ǽ} -> {*ea} || _ EnglishBreakingRContext,
    {*ǽ} -> {*ea} || _ EnglishBreakingLContext,
    {*ǽ} -> {*ea} || _ EnglishBreakingHContext ];
```

The ordinary stressed fronting in
[SC043 EAFBrightening](#rule-EAFBrightening) supplies the short
\emph{æ}. The right contexts are \emph{h}, covered \emph{r} other than
\emph{rj}, and the nonpalatal covered-\emph{l} environment:

```foma
define EnglishBreakingLContext [ {*l} [EnglishStarConsonant - [{*l}|{*j}]] | {*l} {*l}
    [[ContextSegments - {*j}] | .#.] ];
```

The initial-nucleus restriction is an executable proxy for stress after
the primary accent has been consumed. It excludes genuinely weak medial
vowels. Secondary short front \emph{ǽ} is carried separately from earlier
\emph{à}; it can break in a noninitial root. The annotation is decoded
only after its breaking consumer, not at an invented historical date of
general destressing. *erian* 'plough' independently protects the
unbroken \emph{rj} history [@RingeTaylor2014, p.182;
@HoggGrammar2011, pp.217--218, §§6.7--8].

### Short e and the lateral distinctions {#rule-OEBreakingE}

```foma
define EnglishBreakingLContextE [{*l} [{*x} | {*w}]];
```

*seolh* 'seal' and *eolh* 'elk' support breaking before \emph{lh}.
*āseolcan* 'languish' does not license a general \emph{lk} rule:
*melcan* 'milk' remains unbroken and rules out obligatory breaking in
this environment. Wright and Wright list *meolcan* 'milk' beside Anglian
*melcan*, but give no manuscript locator there; their listing alone does
not verify an attestation or establish its dialectal distribution
[@Wright1908, p.46, §84]. The model keeps only the narrower
preceding-\emph{s} proxy for that exceptional comparison; its ultimate
historical explanation and dialectal reach are less secure than
\emph{lh}. No independently verified \emph{lg} witness supports the old
generalization. Non-West-Saxon *seolf* 'self' is not a reason to change
early West Saxon *self* or *delfan* 'dig'
[@Campbell1959, pp.56--57, §§146--147;
@HoggGrammar2011, pp.85--86, §5.22; @RingeTaylor2014, pp.186--188].

Hogg and Ringe and Taylor defend direct breaking before \emph{lw},
including *ġeolwe* 'yellow' and genitive *meolwes* 'meal, flour'.
The alternative derives the diphthongs in nominative *ġeolu* 'yellow' and *meolu* 'meal, flour'
by back mutation and transfers them into inflected forms. Hogg argues
against treating that transfer as the established explanation, particularly
given the distribution of *ġeolu*. The model adopts the regular
\emph{lw} account while retaining the alternative. A later rule can
already supply these surface diphthongs in the executable cascade;
surface agreement therefore does not independently date the change
[@HoggGrammar2011, p.86, §5.22 n.3;
@RingeTaylor2014, pp.187--188].

```foma
define OEBreakingE [ {*e} -> {*eo} || .#. OEAnyConsonant* _ EnglishBreakingRContext,
    {*e} -> {*eo} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*e} -> {*eo} || .#. OEAnyConsonant* _ EnglishBreakingWContext,
    {*e} -> {*eo} || .#. OEAnyConsonant* _ EnglishBreakingLContextE,
    {*e} -> {*eo} || .#. OEAnyConsonant* {*s} _ {*l} {*k} ]
    .o. [ {*é} -> {*éo} || _ EnglishBreakingRContext,
    {*é} -> {*éo} || _ EnglishBreakingHContext,
    {*é} -> {*éo} || _ EnglishBreakingWContext,
    {*é} -> {*éo} || _ EnglishBreakingLContextE,
    {*é} -> {*éo} || {*s} _ {*l} {*k} ]
    .o. [ {*è} -> {*eo} || _ EnglishBreakingRContext,
    {*è} -> {*eo} || _ EnglishBreakingHContext,
    {*è} -> {*eo} || _ EnglishBreakingWContext,
    {*è} -> {*eo} || _ EnglishBreakingLContextE,
    {*è} -> {*eo} || {*s} _ {*l} {*k} ];
```

Short \emph{e} and \emph{i} also break before singleton \emph{w},
except when a high front vowel or \emph{j} follows it. Dative
*cneowe* 'knee' is the short-vowel comparison, not long-diphthong
promotion [@Luick1914, p.139, §134; @HoggGrammar2011, p.86, §5.22;
@RingeTaylor2014, pp.187--188]:

```foma
define EnglishBreakingWContext [ {*w} [[EnglishStarVocalic | EnglishStarConsonant] -
    [{*i} | {*ì} | {*í} | {*ī} | {*ḯ} | {*j}]] | {*w} .#. ];
```

Long endingless *cnēo* 'knee' and the restored \emph{w} of *cnēow*
'knee' have separate histories, discussed under
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong).

### Short i and stress {#rule-OEBreakingI}

*meox* 'manure' and *Peohtas* 'Picts' independently support short
\emph{i}-breaking before \emph{h}. Their short \emph{io} may develop
later \emph{eo}; it is not born long. The three selected learn forms
already have \emph{e} at breaking and cannot witness this component.
Hogg's \emph{*filhiþ} comparison supplies the narrow \emph{lh}
environment, not every covered lateral. West Saxon and Kentish
breaking before covered \emph{r} must also be distinguished from the
Anglian following-\emph{i/j} exclusions
[@Campbell1959, pp.57--59, §§148--154;
@HoggGrammar2011, pp.87--88, §§5.24--25;
@RingeTaylor2014, pp.177--178, 187--188].

```foma
define EnglishBreakingLContextI [{*l} {*x}];
```

```foma
define OEBreakingI [ {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingRContext,
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingLContextI,
    {*i} -> {*io} || .#. OEAnyConsonant* _ EnglishBreakingWContext ]
    .o. [ {*í} -> {*ío} || _ EnglishBreakingRContext,
    {*í} -> {*ío} || _ EnglishBreakingHContext,
    {*í} -> {*ío} || _ EnglishBreakingLContextI,
    {*í} -> {*ío} || _ EnglishBreakingWContext,
    {*ì} -> {*io} || _ EnglishBreakingRContext,
    {*ì} -> {*io} || _ EnglishBreakingHContext,
    {*ì} -> {*io} || _ EnglishBreakingLContextI,
    {*ì} -> {*io} || _ EnglishBreakingWContext ];
```

Breaking is not an ordinary unstressed-vowel development. *fulwiht*
'baptism' and *nawiht* 'nothing' retain weak \emph{i} or undergo the
separately described retraction beside \emph{w}; the existence of
retracted alternatives does not make them stressed breaking positives.
A no-\emph{w} comparison isolates the stress condition. Plain initial
nuclei, explicit primary \emph{í} and preserved subordinate \emph{ì}
are distinguished from plain weak medial \emph{i}. In the conditional
*seleweard* history, medial \emph{i} causes mutation without breaking
and later lowers, while the subordinate root independently breaks to
\emph{weard}. The regular weight-conditioned reduction of a secondary
low vowel remains available in the separate *weorold* 'world' history. The date at which an annotation is removed is not a
date for obligatory historical destressing
[@HoggGrammar2011, pp.217--218, §§6.7--8; @Russom2001, pp.39--64].

### Inherited long quantity {#rule-OEBreakingLong}

```foma
define OEBreakingLong [ {*ǣ} -> {*ēa} || .#. OEAnyConsonant* _
    EnglishBreakingHContext,
    {*ē} -> {*ēo} || .#. OEAnyConsonant* _ EnglishBreakingHContext,
    {*ī} -> {*īo} || .#. OEAnyConsonant* _ EnglishBreakingHContext ]
    .o. [ {*ḗ} -> {*ḗo} || _ EnglishBreakingHContext,
    {*ḯ} -> {*īo} || _ EnglishBreakingHContext ];
```

West Saxon *nēah* 'near' continues long front \emph{ǣ}; the corresponding
non-West-Saxon input is long \emph{ē}. In *lēoht* 'light in weight', with earlier *līoht* 'light in weight',
the vowel has become long before breaking. These
histories are distinct from short breaking followed by contraction in
*slēan* 'slay'. The long component models the breaking intermediate; it is not
a claim to supply every later dialect-specific merger or loss
[@HoggGrammar2011, pp.85--88, §§5.21, 5.23, 5.25;
@RingeTaylor2014, pp.177--178].

### What the chronology witnesses establish

Under the conventional account the stressed low-vowel contribution of
[SC043 EAFBrightening](#rule-EAFBrightening) feeds breaking. The older
whole-rule displacement also activated a back-\emph{a} fallback and
therefore was not, by itself, a clean test of that history. The
[26-row front-only intervention](../audits/sc044-adjudication.md#front-only-brightening-displacement)
records each changed endpoint when the fallback-free rule is moved
before stressed brightening. This is not the 29-row ambiguous
whole-bundle intervention.

In *feoh* 'cattle' and *feohtan* 'fight', breaking removes the front-vowel
environment while preserving \emph{x}. They do not undergo a subsequent
live [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization)
change. Premature effective palatalization would instead remove the
velar breaking trigger. *hliehhan* 'laugh' contributes something different:
the second fricative of the geminate remains next to \emph{j} and does
undergo the following rule. The
[12-row fricative-palatalization intervention](../audits/sc044-adjudication.md#breaking-after-fricative-palatalization)
records the separate displacement of breaking after that rule.
Hogg's *feoh* argument concerns effective
\emph{h}-palatalization, while Fulk correctly distinguishes that evidence
from the dating of all \emph{k/g} articulation. Neither argument proves
that English and later Frisian breaking were one inherited event
[@Hogg1979, pp.90--92; @Fulk1998, pp.145--146, 152].

The West Saxon comparison with
[SC055 OEIUmlaut](#rule-OEIUmlaut) concerns a different contrast.
In live *bielġ* 'belly, bag', \emph{*bálgiz} has \emph{æ} after
brightening, \emph{ea} after breaking and \emph{ie} after mutation.
At the same prebreaking state, with consonants and surviving \emph{i}
held constant, reversing the vowel operations gives \emph{æ > e},
not \emph{ea > ie}: revised \emph{e}-breaking leaves \emph{e}
before \emph{lg}. The live remainder gives predicted [*belġ*]{.pred},
not *bielġ*. This supports the conventional West Saxon sequence for
this covered-lateral witness [@RingeTaylor2014, p.243, §6.6.3].

For *hliehhan*, the corresponding local comparison is \emph{æ > ea > ie}
against \emph{æ > e > eo}, with both fricatives and \emph{j} unchanged
inside that comparison. Moving mutation early while retaining breaking
before fricative palatalization gives predicted [*hleohhan*]{.pred}.
Moving the entire breaking rule later also lets both fricatives
palatalize first and instead gives predicted [*hlehhan*]{.pred}.
Neither reversed remainder restores \emph{ie}. Ringe and Taylor's
reconstruction already marks a palatalized geminate before breaking;
CAPR's explicit \emph{j}-adjacent consonantal rewrite follows it.
These are not interchangeable consonantal histories
[@RingeTaylor2014, pp.240--244, §6.6.3]. The
[paired West Saxon intervention record](../audits/sc044-adjudication.md#west-saxon-vowel-order-follow-up)
preserves the exact forms and both displacement definitions. It supports
the two selected West Saxon histories, not a universal date for every
component or dialect.

### The early Anglian alternative

Versloot's late Anglian \emph{rC} analysis makes a different prediction
for mutation-created \emph{e}. Given \emph{*farmjan-}, an early-breaking
account gives fronting, breaking and mutation, with final short
\emph{e}; post-mutation breaking restricted to \emph{rm} instead gives
\emph{eo}. Épinal *feormat* 'fosters, nourishes', a third-person singular
present, favours the latter only under that reconstruction. Pheifer's
§70 identifies the Old English inflection. The text and apparatus to
no.402 give Latin *fouit* in Épinal and Erfurt, but *fouet* in Corpus;
the Latin variants do not change the Old English parse. Pheifer
separately records Erfurt *caeormad* and the Corpus parallel; one
manuscript's spelling must not be silently substituted for another
[@Pheifer1974, p.lxxxii, §70, p.22, no.402;
@Versloot2025, pp.130--132, §§5.4--5.5].

The input premise is substantive. Lloyd and Lühr also consider an
original-\emph{e} analysis, deriving the verbs from North-West-Germanic
\emph{*ferma(n)-}, while leaving the deeper etymology problematic.
On that alternative either Anglian ordering can yield \emph{eo};
*feormat* is then not an independent date for breaking after mutation.
Their proposal is an alternative, not a verified replacement for every
part of the \emph{*farmjan-} history
[@LloydLuhr2007, cols.492--493, s.v. \emph{formôn}].

An original-front-vowel analysis of *geormantlab* 'mallow' can give
\emph{eo} in both orders; its complete etymology remains qualified by
Pheifer. The \emph{gard}~\emph{geard} comparison concerns the low vowel
supplied to breaking, not by itself the date of mutation-created
\emph{e}. A bounded late \emph{rm} account must also be distinguished
from unrestricted breaking before every \emph{rC}: *uuerci* 'works',
*smeruui* 'fat' and *teru* 'tar' constrain its scope. Published levelling
from *smeru* is a competing explanation of *smeruui*. For *teru* the
presence or prior vocalization of inherited consonantal \emph{w} matters
to whether there was a covered-\emph{r} environment at all
[@Pheifer1974, p.103, no.656; @HoggGrammar2011, p.86, §5.22 n.6;
@Versloot2025, pp.114--116, 130--132, 138--140, §§3.3, 5.4--5.5, 7].

The discriminating result is a reason to retain the late Anglian account
as a substantive alternative, not to replace the West Saxon sequence
globally. Establishing the relevant reconstruction and a wider regular
Anglian distribution would determine its extension. Later Frisian
breaking is a comparative check, not a shared inherited date.
