# West Saxon palatal umlaut

## Historical discussion

The reflexes *miht* ‘might’ and *niht* ‘night’ place West Saxon palatal umlaut
after the principal umlautal developments. Campbell and Ringe and Taylor
describe the forms themselves; Fulk supplies the broader chronology of
palatal-vowel change [@Campbell1959, pp. 107--108, §§248--251;
@RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75,
§§4.7, 4.13].

## SC060. West Saxon palatal umlaut before \emph{*h}-clusters (`OEWsPalatalUmlaut`) {#rule-OEWsPalatalUmlaut}

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
stage [*mieht*]{.pred} and [*nieht*]{.pred} rather than expected OE *miht* and *niht*.
Consequently, i-umlaut precedes palatal umlaut. Reordering the latter against
any tested later change leaves both witness forms unchanged.
