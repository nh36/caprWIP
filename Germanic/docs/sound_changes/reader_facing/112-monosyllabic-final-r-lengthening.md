# Monosyllabic lengthening before final \emph{r}

The model admits Old English *þǣr* ‘there’ and *hwǣr* ‘where’ from
source-supported short-*a* antecedents. Their quantity and the date of the
lengthening remain qualified: the forms do not establish a Proto-Germanic
date, and they do not determine the order of
[SC015 PNWGmcILowering](#rule-PNWGmcILowering).

## SC112. Stressed monosyllabic lengthening before inherited final \emph{r} (`PNWGmcMonosyllabicFinalRLengthening`) {#rule-PNWGmcMonosyllabicFinalRLengthening}

```foma
define PNWGmcMonosyllabicFinalRLengthening [
    [
        {*á} -> {*ā},
        {*é} -> {*ē},
        {*í} -> {*ī},
        {*ó} -> {*ō},
        {*ú} -> {*ū}
        || .#. EnglishStarConsonant* _ {*r} .#.
    ]
];
```

The early working placement preserves inherited final \emph{r} before
rhotacism, so secondary \emph{r} does not trigger the rule. The guard also
excludes disyllabic forms. This is a general formalization of the two
admitted witnesses, not a lexical exception list or a claim of strict
relative chronology against
[SC015 PNWGmcILowering](#rule-PNWGmcILowering) or
[SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering).

Hill's comparison of monosyllabic local with longer directional
forms supplies a broader phonological argument than the two selected
adverbs alone; the pan-Germanic extension additionally involves his
Scandinavian levelling analysis. Ringe and Taylor allow deictic stress
or reanalysis involving *hēr* 'here'. The long adverbs therefore
motivate the working generalization without uniquely deciding its
cause or date [@Hill2017, pp. 142--148;
@RingeTaylor2014, p. 65; @Stiles2013, pp. 15--16].

The short neuter *dor* 'door', compared with OS *dor* and OHG *tor*,
is distinct from feminine *duru* 'door'; the selected direct cell
must not be replaced by the latter paradigm
[@Fulk2018, pp. 56--57, §4.3; @RingeTaylor2014, p. 385].
In the controlled early-apocope experiment, placing this unchanged
rule before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope)
makes it see still-suffixed \emph{*dorą}. No lengthening occurs,
and subsequent loss gives short *dor*. The same two there/where
applications survive, while z has not yet supplied secondary r.
This establishes a viable executable prerequisite for that candidate,
not a newly proved historical edge. The production order is unchanged.
