# Awj glide formation and au-fronting

## Historical discussion of awj glide formation and au-fronting

The *hay* and *strew* material undergoes both changes. Glide formation reshapes the older \emph{awj} sequence, and fronting then affects the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

Glide formation creates the input to fronting; diphthong leveling follows both.

## Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

The sources establish glide formation, while the witness forms supply only a later boundary.

## SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

The *hīeġ* and *strīeġan* derivations show that \emph{awj} reshaping prepared the input to fronting. If fronting is applied first, PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. Earlier placement of glide formation changes no checked output, so these forms supply an upper boundary without a corresponding lower one.

## Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted
diphthongal outcomes of the broader West Saxon vowel history. Campbell
describes \emph{au} > \emph{ēa} [@Campbell1959, pp. 53--54, §135].

Fronting must follow glide formation and precede diphthong leveling, which applies to a wider set of derivations.

## SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Two distinct failure sets confine fronting. Placed before glide formation, it produces the wrong forms: PGmc \emph{*xáwwją} yields *hauġ* rather than expected OE *hīeġ* ‘hay’, and PGmc \emph{*stráwjaną} yields *strauian* rather than expected *strīeġan* ‘strew’. Placed after diphthong leveling, PGmc \emph{*galáubijaną}, \emph{*bráudą}, and \emph{*dráugmaz}, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. The lexical errors require fronting to follow glide formation, while the failed derivations require it to precede diphthong leveling.

The later failure set consists of failed derivations, not competing Old English
surface forms.
