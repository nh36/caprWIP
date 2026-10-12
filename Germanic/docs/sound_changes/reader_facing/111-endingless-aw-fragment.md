# Endingless \emph{aw}: the regular straw branch

## Historical discussion

The inherited nominative/accusative \emph{*stráwą} loses its final
ending and vocalizes resulting final \emph{w}, giving \emph{*strau}.
Ordinary English diphthong development then produces reconstructed
\emph{*strēa}. Attested *strēaw* 'straw' instead combines that long
diphthong with \emph{w} restored from inflected forms; the long nucleus
also spreads into those forms. The regular free simplex and short
obliques are explicitly unattested. The compound *strēaberige*
'strawberry' preserves the endingless branch, but is not substituted
for an attested free noun
[@Campbell1959, pp. 46--47, 232--233;
@SieversBrunner1965, pp. 49, 110, 204--205;
@RingeTaylor2014, pp. 172--173, 387].

The model keeps attested *strēaw* 'straw' as its comparison and produces
regular reconstructed \emph{*strēa}: this is an explicit mismatch.
The fragment below combines final-vowel loss and ensuing vocalization.
Its narrow matcher does not make general final-vowel loss
\emph{w}-conditioned.

## SC111. Endingless \emph{aw} fragment (`PWGmcEndinglessAw`) {#rule-PWGmcEndinglessAw}

```foma
define PWGmcEndinglessAw [
    {*a} {*w} {*ą} -> {*au} || _ .#. ,
    {*á} {*w} {*ą} -> {*áu} || _ .#.
];
```

The ordinary \emph{au} product feeds
[SC030 OEAuBrightening](#rule-OEAuBrightening) and
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), not the retained
show proxy [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong).
The early holding site is compatible with the source's West Germanic
history, not evidence for strict relative order against unrelated
dental hardening [@RingeTaylor2014, pp. 172--173].
