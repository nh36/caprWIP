# stem — OE stefna, stefn

PROTO: *stámnaz
PROTOFORM: *stámnaz
COUNTERPART: stefna
DERIVATION_CLASS: early_analogy

### Transducer input and output

| Item | Value |
| :--- | :--- |
| lexical item | stem, trunk, prow of a ship |
| citation reconstruction / lexeme label | *stámnaz |
| selected input form | *stámnaz (transponent pending: see note) |
| Old English target | stefna |
| classification | early_analogy |
| documented output | *stámnaz -> stefna (via coda mn → fn, not yet modeled in FST) |

### Reconstruction and comparative evidence

Orel reconstructs the Proto-Germanic source as [`*stamnaz`]{.iv lang=pgmc sort=stamnaz role=source_protoform}
'stem, trunk' (also `*stamniz`), citing Old Norse [`stafn`]{.iv lang=on sort=stafn role=comparison_form}
'stem of a ship', Old Frisian [`stevene`]{.iv lang=ofris sort=stevene role=comparison_form} fem.
'id.', and Old Saxon [`stamn`]{.iv lang=os sort=stamn role=comparison_form} as its
main continuants [@Orel2003, 371].

This word is etymologically unrelated to the Old English homonym `stefn/stemn` 'voice,
sound', which descends from a distinct Proto-Germanic `*stebnō/*stemnō`-type noun.
The two OE lexemes are distinguished in Clark Hall, Bosworth-Toller, Brunner, and
Luick; they collide on the surface forms `stefn` and `stemn` through historically
independent developments.

Kroonen does not separate a distinct 'prow' proto-form but relates the 'stem'
family to the `stam(m)` 'stem, trunk' group attested in Old High German, Dutch,
and German [@Kroonen2013, 479–480].

### Old English evidence

Clark Hall distinguishes three OE lexemes under `stefn`: a weak masculine
[`stefna`]{.iv lang=oe sort=stefna role=target_form} 'prow or stern of a ship' (n-stem),
and [`stefn`]{.iv lang=oe sort=stefn role=comparison_form} III m. 'stem, trunk, root,
prow, foundation' [@ClarkHall1960, 276]. The related form
[`stofn`]{.iv lang=oe sort=stofn role=comparison_form} m. 'trunk, stem, branch, shoot'
is also recorded [@ClarkHall1960, 341].

Luick §211 notes that `stemn` 'Stamm (trunk/stem)' derives from `*stofn`, cognate with
Old Saxon `stamn`, distinguishing it explicitly from the voice word's development in
§75 [@Luick1914, §211]. Brunner §205 lists `stefn, stemn Stamm` among the words
showing the `fn/mn` alternation [@SieversBrunner1965, §205].

The comparison form used here is [`stefna`]{.iv lang=oe sort=stefna role=target_form}
'prow or stern of a ship', as the most specifically attested n-stem form for this
sense. The form [`stofn`]{.iv lang=oe sort=stofn role=comparison_form} 'trunk' represents
either a distinct `*o`-grade Germanic variant or an earlier OE stage before further
vowel development, following Luick's proposal.

### Development to Old English

The derivation of OE [`stefna`]{.iv lang=oe sort=stefna role=regular_output} 'prow/stern'
from [`*stámnaz`]{.iv lang=pgmc sort=stamnaz role=source_protoform} 'stem/trunk' involves
a North-West Germanic coda dissimilation `mn → fn` in the consonant cluster. This
is distinct from the cross-syllable `m → β` change (as in `*heβonų → heofon`) handled
by the `NWGmcMnDissimilation` rule; the coda environment (`Cmn → Cfn`) is currently
not modeled in the FST.

The scholarly pathway is: [`*stámnaz`]{.iv lang=pgmc sort=stamnaz role=source_protoform}
'stem/trunk' → NWGmc coda `mn → fn` (unmodeled) → `*stáfnaz`/`*stéfnô` → OE
[`stefna`]{.iv lang=oe sort=stefna role=regular_output} 'prow'. Late West Saxon `fn → mn`
(the same change documented for the voice word) then yields the variant
[`stemn`]{.iv lang=oe sort=stemn role=comparison_form} 'trunk/stem' (Luick §211,
Brunner §205).

The correct OE-facing transponent has not yet been established for the FST pipeline.
The classification `early_analogy` reflects that the derivation requires an intermediate
stage whose modeling is pending. The derivation is real and well-attested; the FST
work remains to be done.

### Homonym note

Old English `stefn`/`stemn` is a surface homonym for two etymologically unrelated words:

1. **`stefn/stemn` 'voice, sound'**: from PGmc `*stebnō` (Ringe-Taylor, Orel); via `bn → fn` BAllophony, giving `stefn`. This is a **different row** from 2216.
2. **`stefna/stefn/stofn` 'prow, trunk, stem'**: from PGmc [`*stámnaz`]{.iv lang=pgmc sort=stamnaz role=source_protoform} (Orel); via coda `mn → fn`. **This is row 2216.**

Do not conflate the two. The selected input `*stébnō` used in earlier versions of this entry was the wrong homonym's transponent.

### Source comparison

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| [`*stámnaz`]{.iv lang=pgmc sort=stamnaz role=source_protoform} | Orel's PGmc citation for prow/stem/trunk family | controls this derivation | selected comparative citation |
| [`stefna`]{.iv lang=oe sort=stefna role=target_form} 'prow' | primary OE target (n-stem masc.) | prow/stern sense per Clark Hall | target form |
| [`stofn`]{.iv lang=oe sort=stofn role=comparison_form} 'trunk' | OE `o`-grade variant or earlier stage | trunk/stem sense | comparison form |
| [`stemn`]{.iv lang=oe sort=stemn role=comparison_form} 'trunk' | late West Saxon `fn → mn` doublet | secondary form | comparison form |
| `*stébnō` (voice word) | **wrong homonym** — belongs to voice/sound dossier | no relation to prow/trunk sense | **must not appear in this entry** |
