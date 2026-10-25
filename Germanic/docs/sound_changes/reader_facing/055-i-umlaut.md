# Old English i-umlaut

## SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

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

The selected cow and lung inputs are negative controls on the present
palatalization rule. Moving the composite umlaut rule before that rule yields
[*ċȳ*]{.pred} and [*lunġen*]{.pred} instead of *cȳ* 'cow' and *lungen* 'lung'. This
constrains the current rule's productive domain; it does not assign every
consonantal layer the same date. In particular the selected *cȳ* is a
dative-singular input, not evidence from an assumed generic plural.

The stored gift and sheath displacement failures constrain the current
serialization, not a universal historical upper boundary. The former gift input
left an earlier raising to this late rule; sheath represents the later
*sċ* treatment of a mutation product. Moving the entire palatal-diphthongization
bundle earlier strands sheath and diphthongizes the model's still-unraised
gift vowel. Neither failure overturns the independently supported ordinary
palatal-diphthongization-before-mutation account.

## SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Raising of umlauted `æ` to `e` continues the same assimilatory event as fronting and therefore shares the chronology of general i-umlaut.

The four displacement controls concern the composite rule. They are not
independent tests of this raising component: for example, the cow vowel
changes in the fronting component, not in this \emph{*æ}-raising clause.
Component chronology must follow the source-supported assimilatory event,
with ordinary palatal diphthongization and the later *sċ* extension kept
distinct.

The sources do not describe umlaut as simple fronting alone. Campbell notes that
the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@HoggPhonology1992, p. 113].

## SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

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
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @HoggPhonology1992, pp. 113--114]. These diphthongal outcomes form a distinct part of the general
umlautal development alongside simple fronting.

Those composite displacement controls do not isolate diphthongal mutation:
neither the cow input nor the gift input has a diphthong here. In the
conventional history, diphthongs produced by ordinary palatal diphthongization
can be mutated, as in the source derivation of *ġiest* 'guest'
[@RingeTaylor2014, p. 216]. The adopted derivation now follows that ea-to-ie source path. The former
simple-vowel route converged on the same final form, showing why final
agreement alone could not establish the relative chronology.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut FootCtx(OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong);
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The cow/lung displacement results require the present productive
palatalization rule not to consume those mutation-created environments.
The historical interpretation still depends on the relevant consonantal
layer and inherited versus secondary front-vowel conditions.

There is no single source-supported upper boundary at the entire West
Saxon bundle. Ordinary palatal diphthongization precedes mutation in the
handbook account; the later *sċ* treatment of some mutation products follows
it. The former gift input and sheath's later layer explained the old bundled
serialization, not a date for every historical palatal process.
