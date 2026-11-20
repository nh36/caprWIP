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

An early-loss experiment can delete the ending first and then apply
a separately tested final \emph{aw > au} companion at this same
position. It restores reconstructed \emph{*strēa}, with no change to
the selected target *strēaw* 'straw'. Matched suffixed, long-vowel and
consonant-plus-w controls do not undergo that added operation.
The old matcher is therefore an executable dependency, not an
independent argument that historical apocope must follow this
fragment. The companion is not installed while
[SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope)
retains its present production position; the regular-versus-analogical
distinction remains the source's distinction
[@RingeTaylor2014, pp. 172--173, 387].
