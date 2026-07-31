# West Saxon palatal glide before back vowels

## Historical discussion

West Saxon spellings such as *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ*
'youth' reflect an early Old English development before back vowels. Campbell gives the
most direct handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

The sources establish [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), although the checked forms provide only a later boundary. The rule is computationally
positioned before [SC017 NWGmcULowering](#rule-NWGmcULowering) because the
derivation of *ġeoc* 'yoke' requires glide insertion before u-lowering applies. That
computational dependency places [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) in the Old English section of the cascade
even though the cascade position precedes many Northwest Germanic changes.

## SC016. West Saxon palatal glide before back vowels (`OEWsPalatalGlide`) {#rule-OEWsPalatalGlide}

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

OE *ġeoc* 'yoke' fixes the close relation between glide insertion before back-vocalic \emph{u} and the following change.

If glide insertion follows [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [júką]{.recon} 'yoke' yields [*ġoc*]{.pred} rather than expected OE *ġeoc* 'yoke'; earlier placement changes no checked output. The witness therefore dates [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) before u-lowering without supplying an earlier boundary. The *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ* 'youth' material establishes the lexical scope of the West Saxon development.
