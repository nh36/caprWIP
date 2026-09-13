# Long \emph{ēow} before following vowels

## Historical discussion

Four distinct developments shape the West Saxon diphthongal field. Campbell
discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered
diphthongization, and later Anglian smoothing in connected but separate parts
of the vowel history; Hogg likewise distinguishes the palatal-diphthongal
developments [@Campbell1959, pp. 46, 53--54, 65--70, 95--96,
§§120, 135--136, 170--176, 185, 223--227; @Hogg1992, pp. 106--107, 111--112].

The closest interaction joins \emph{ww}-simplification and long-\emph{aw} diphthongization, which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. Diphthong leveling regularizes a wider field, while long-\emph{ew} diphthongization carries \emph{ēow} into the later environment of breaking.

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from chew,
four, and knee [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The only boundary established by the lexical evidence for
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) lies ahead at
[SC044 OEBreaking](#rule-OEBreaking).

## SC033. Long \emph{ēow} before following vowels and weak endings (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The long \emph{ēow} of *ċēowan* 'chew', *fēower* 'four', and *cnēow* 'knee' supplies only a terminus ante quem. If [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) follows [SC044 OEBreaking](#rule-OEBreaking), PGmc [kéwwaną]{.recon} ‘chew’ yields [*ċeowan*]{.pred} rather than expected OE *ċēowan* ‘chew’, PGmc [fédwōr]{.recon} ‘four’ yields [*feower*]{.pred} rather than expected *fēower* ‘four’, and PGmc [knéwą]{.recon} ‘knee’ yields [*cneow*]{.pred} rather than expected *cnēow* ‘knee’. Earlier placement changes no output. The sources associate \emph{ew} and \emph{iw} with the same diphthongal history but furnish no lower boundary.
