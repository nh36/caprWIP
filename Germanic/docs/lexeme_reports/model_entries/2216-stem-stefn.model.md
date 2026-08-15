# stem — OE stefn

PROTO: *stámnaz
PROTOFORM: *stámniz
COUNTERPART: stefn
DERIVATION_CLASS: early_analogy

### Transducer input and output

| Item | Value |
| :--- | :--- |
| lexical item | stem, trunk, prow |
| citation reconstruction / lexeme label | *stámnaz |
| selected input form | *stámniz (Orel's i-stem variant; citation reconstruction *stámnaz) |
| Old English target | stefn |
| classification | early_analogy |
| documented output | *stámniz -> stefn (multiplicity 1, exact match) |

### Reconstruction and comparative evidence

Orel reconstructs the Proto-Germanic source as [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform}
'stem, trunk' (also variant [stamniz]{.recon} 'stem, trunk'), citing Old Norse
[`stafn`]{.iv lang=on sort=stafn role=comparison_form} 'stem of a ship',
Old Frisian [`stevene`]{.iv lang=ofris sort=stevene role=comparison_form} 'stem of a ship' (fem.),
and Old Saxon [`stamn`]{.iv lang=os sort=stamn role=comparison_form} 'stem' as its
main continuants [@Orel2003, 371].

This word is etymologically unrelated to the Old English homonym
[stefn]{.lex lang=oe} 'voice, sound' / [stemn]{.lex lang=oe} 'voice, sound',
which descends from a distinct Proto-Germanic
[stebnō]{.recon} 'voice, sound' / [stemnō]{.recon} 'voice, sound' etymon.
The two OE lexemes are distinguished in Clark Hall, Bosworth-Toller, Brunner, and
Luick; they collide on the surface forms `stefn` and `stemn` through historically
independent developments.

Kroonen relates the 'stem' family to the `stam(m)` 'stem, trunk' group attested in
Old High German, Dutch, and German, without reconstructing a separate 'prow'
proto-form [@Kroonen2013, 479–480].

### Old English evidence

Clark Hall records [`stefn`]{.iv lang=oe sort=stefn role=target_form} 'stem, trunk, root, prow, foundation', the weak n-stem
[`stefna`]{.iv lang=oe sort=stefna role=comparison_form} 'prow or stern of a ship',
and the related [`stofn`]{.iv lang=oe sort=stofn role=comparison_form} 'trunk, stem, branch, shoot' [@ClarkHall1960, 276, 341].

Luick §211 explicitly distinguishes OE [stefn]{.lex lang=oe} 'stem, trunk' / [stemn]{.lex lang=oe} 'stem, trunk' — noting cognates with
Old Saxon [`stamn`]{.iv lang=os sort=stamn role=comparison_form} 'stem' and Middle English [`stam`]{.iv lang=me sort=stam role=comparison_form} 'stem' — from the
separate OE voice/sound word ([stefn]{.lex lang=oe} 'voice, sound' / [stemn]{.lex lang=oe} 'voice, sound') treated in §75 [@Luick1914, §211]. Brunner §205 lists
`stefn, stemn Stamm` among words showing the `fn`/`mn` alternation [@SieversBrunner1965, §205].

The primary comparison form used here is [`stefn`]{.iv lang=oe sort=stefn role=target_form} 'stem, trunk, root, prow', the form attested most directly in the semantic range
relevant to English `stem`. The n-stem [`stefna`]{.iv lang=oe sort=stefna role=comparison_form}
'prow/stern' is a closely related but more narrowly attested nautical specialization.

### Development to Old English

The derivation of OE [`stefn`]{.iv lang=oe sort=stefn role=comparison_form} 'stem, trunk'
from the i-stem input [stámniz]{.recon .iv lang=pgmc sort=stamniz role=source_protoform} 'stem, trunk'
(Orel's attested i-stem variant; the citation reconstruction remains
[stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem, trunk') is now **regular and
modelled**, with multiplicity 1. Live trace under the corrected literal
adjacent-`mn` SC022:

| step | form |
| :--- | :--- |
| proto input | `*stámniz` |
| EAF Final Z Deletion | `*stámni` |
| PNWGmc Mn Dissimilation (adjacent mn > βn) | `*stáβni` |
| EAF Brightening (á > æ) | `*stæβni` |
| OE i-Umlaut (æ > e, from the i-stem ending) | `*steβni` |
| OE High Vowel Apocope | `*steβn` |
| Old English Orthography (β > f) | `stefn` |

The consonantal change `mn → βn/fn` is attested comparatively: Old Norse
[`stafn`]{.iv lang=on sort=stafn role=comparison_form} 'stem of a ship' and Old Saxon
[`stamn`]{.iv lang=os sort=stamn role=comparison_form} 'stem' preserve the `fn`/`mn`
variants expected from this family. The handbooks treat the change as a pre-Old-English
development (Luick §211; Brunner §205), and the FST now encodes it as the historical
**adjacent** `mn > βn` (the rule `PNWGmcMnDissimilation` / SC022). The `e` of `stefn`
is regular from `á` via brightening (`á > æ`) plus i-umlaut triggered by the i-stem
ending (`æ > e`), so both the vowel and the consonant follow by regular sound change
once the i-stem input is selected.

Note the contrast with *heaven*. Here SC022 (`PNWGmcMnDissimilation`) **fires
directly inside** the selected derivation, deriving the labial of `stefn` from
the adjacent `-mn-` cluster of `*stámniz`. In *heaven*, by contrast, the **same
historical change** `mn > βn/fn` operated only in the deeper **cluster-bearing
oblique prehistory**; the resulting labial was then **generalized** into the
vowel-bearing `*hebun-` stem, so the selected CAPR path `*xébun -> heofon` begins
*after* that analogy and does **not** itself contain SC022 (see
`dossier-heaven-paradigm-history-2026.md` §§13–15 and
`audits/heaven-sc022-implementation-2026.md`). The earlier cross-syllable
`mV…n` proxy — which had formerly fabricated a labial from an intervocalic *m* —
has been **retired** in favour of this literal adjacent `mn > βn`. Selecting the
i-stem input `*stámniz` over the a-stem citation `*stámnaz` is a **pre-OE input
selection**; once selected, the Old English development is regular. Hence the
classification `early_analogy` (analogy separates the input from the citation
reconstruction before the specifically Old English changes apply), not
`known_unmodelled`.

### Homonym note

Old English `stefn`/`stemn` is a surface homonym for two etymologically unrelated words:

1. `stefn/stemn` 'voice, sound': from PGmc `*stebnō` (Ringe-Taylor, Orel); via `bn → fn` (b-allophony), giving [stefn]{.lex lang=oe} 'voice, sound'. This is a different row from 2216.
2. `stefn/stefna/stofn/stemn` 'stem, trunk, prow': from PGmc [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem/trunk' (Orel); via the pre-OE cluster change `mn → fn`. This is row 2216.

The selected input `*stébnō` used in earlier versions of this entry was the wrong homonym's transponent and must not be used here.

### Source comparison

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem, trunk' | Orel's PGmc a-stem citation for the stem/trunk/prow family | lexeme-level citation | retained as PROTO (citation) |
| [stámniz]{.recon .iv lang=pgmc sort=stamniz role=source_protoform} 'stem, trunk' | Orel's attested i-stem variant | **selected derivational input** | regular OE output `stefn` (mult 1) |
| [`stefn`]{.iv lang=oe sort=stefn role=target_form} III 'stem, trunk, root, prow' | primary OE target (strong masc.) | stem/trunk sense per Clark Hall | target form |
| [`stefna`]{.iv lang=oe sort=stefna role=comparison_form} 'prow/stern' | OE n-stem specialization | nautical sense per Clark Hall | comparison form |
| [`stofn`]{.iv lang=oe sort=stofn role=comparison_form} 'trunk' | OE `o`-grade variant or earlier stage | trunk/stem sense | comparison form |
| [`stemn`]{.iv lang=oe sort=stemn role=comparison_form} 'trunk' | late West Saxon `fn → mn` doublet | secondary form | comparison form |
| `*stébnō` (voice word) | **wrong homonym** — belongs to voice/sound dossier | no relation to stem/trunk sense | **must not be used as row 2216's derivational input** |
