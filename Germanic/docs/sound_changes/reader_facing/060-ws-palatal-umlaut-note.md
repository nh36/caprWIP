# West Saxon palatal umlaut

## Historical discussion

The evidence is narrow enough that the discussion can stay brief. Campbell and Ringe and Taylor both support the
development behind forms such as *miht* ‘might’ and *niht* ‘night’, while Fulk's
broader chronology makes clear that this material belongs beside the umlaut and
palatal-vowel region as a subordinate note beside it
[@Campbell1959, pp. 107--108, §§248--251; @RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4;
@Fulk2018, pp. 65, 75, §§4.7, 4.13].

That is why the note belongs here after back mutation even though its clearest
historical tie still reaches back to the earlier umlautal chapter. The
phenomenon is real, yet its place in the sequence is one-sided. The evidence is
clear enough to state and narrow enough to remain brief.

## SC060. West Saxon palatal umlaut before \emph{*h}-clusters (`OEWsPalatalUmlaut`) {#rule-OEWsPalatalUmlaut}

The implementation treats the West Saxon change as one explicit rule.

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

In prose, the rule reduces short diphthongs to \emph{*i} before the relevant \emph{*h}
clusters.

The crucial point is its earlier dependency. The rule must follow
[SC055 OEIUmlaut](#rule-OEIUmlaut), because if it is moved too early
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage *mieht* and *nieht* rather than expected OE *miht* and *niht*. No comparably sharp later lexical breakpoint emerges
within the remainder of the section. The note therefore belongs here as a short
afterpiece to the umlaut chapter, not as the start of a new larger unit.

This shows that [SC055 OEIUmlaut](#rule-OEIUmlaut) must come before
[SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut). No comparably sharp later
boundary is available.
