# stem — OE stefn

PROTO: *stámnaz
PROTOFORM: *stámnaz
COUNTERPART: stefn
DERIVATION_CLASS: known_unmodelled

### Transducer input and output

| Item | Value |
| :--- | :--- |
| lexical item | stem, trunk, prow |
| citation reconstruction / lexeme label | *stámnaz |
| selected input form | *stámnaz (OE-facing transponent pending; see Development note) |
| Old English target | stefn |
| classification | known_unmodelled |
| documented output | *stámnaz -> stefn (via pre-OE cluster change, not yet modeled in FST) |

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
Old Saxon [`stamn`]{.iv lang=os sort=stamn role=comparison_form} 'stem' and Middle English `stam` — from the
separate OE voice/sound word ([stefn]{.lex lang=oe} 'voice, sound' / [stemn]{.lex lang=oe} 'voice, sound') treated in §75 [@Luick1914, §211]. Brunner §205 lists
`stefn, stemn Stamm` among words showing the `fn`/`mn` alternation [@SieversBrunner1965, §205].

The primary comparison form used here is [`stefn`]{.iv lang=oe sort=stefn role=target_form} 'stem, trunk, root, prow', the form attested most directly in the semantic range
relevant to English `stem`. The n-stem [`stefna`]{.iv lang=oe sort=stefna role=comparison_form}
'prow/stern' is a closely related but more narrowly attested nautical specialization.

### Development to Old English

The derivation of OE [`stefn`]{.iv lang=oe sort=stefn role=comparison_form} 'stem, trunk'
from [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem, trunk'
involves a cluster change `mn → fn` that is attested comparatively: Old Norse
[`stafn`]{.iv lang=on sort=stafn role=comparison_form} 'stem of a ship' and Old Saxon
[`stamn`]{.iv lang=os sort=stamn role=comparison_form} 'stem' preserve the `fn`/`mn` variants
expected from this family. The precise phonological dating and domain of this change —
whether it belongs to a North-West Germanic stage, an early West Germanic stage, or is
reconstructed separately in each branch — is not definitively resolved by the cited
scholarship. The handbooks treat it as a pre-Old-English development (Luick §211;
Brunner §205), but the term "North-West Germanic coda dissimilation" should be taken
as descriptive rather than technically established. This coda environment
(`[C]mn → [C]fn`) is distinct from the cross-syllable `m → β` change (as in
[xémonų]{.recon} 'heaven' → [heofon]{.lex lang=oe} 'heaven') handled by the `NWGmcMnDissimilation` rule;
it is currently not modeled in the FST.

The correct OE-facing transponent has not yet been established for the FST pipeline.
The classification `known_unmodelled` reflects that the derivation involves a historically
real development not yet represented in the FST cascade. The derivation is attested
comparatively; the FST work remains to be done.

### Homonym note

Old English `stefn`/`stemn` is a surface homonym for two etymologically unrelated words:

1. **`stefn/stemn` 'voice, sound'**: from PGmc `*stebnō` (Ringe-Taylor, Orel); via `bn → fn` (b-allophony), giving [stefn]{.lex lang=oe} 'voice, sound'. This is a **different row** from 2216.
2. **`stefn/stefna/stofn/stemn` 'stem, trunk, prow'**: from PGmc [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem/trunk' (Orel); via the pre-OE cluster change `mn → fn`. **This is row 2216.**

The selected input `*stébnō` used in earlier versions of this entry was the wrong homonym's transponent and must not be used here.

### Source comparison

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| [stámnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform} 'stem, trunk' | Orel's PGmc citation for stem/trunk/prow family | controls this derivation | selected comparative citation |
| [`stefn`]{.iv lang=oe sort=stefn role=target_form} III 'stem, trunk, root, prow' | primary OE target (strong masc.) | stem/trunk sense per Clark Hall | target form |
| [`stefna`]{.iv lang=oe sort=stefna role=comparison_form} 'prow/stern' | OE n-stem specialization | nautical sense per Clark Hall | comparison form |
| [`stofn`]{.iv lang=oe sort=stofn role=comparison_form} 'trunk' | OE `o`-grade variant or earlier stage | trunk/stem sense | comparison form |
| [`stemn`]{.iv lang=oe sort=stemn role=comparison_form} 'trunk' | late West Saxon `fn → mn` doublet | secondary form | comparison form |
| `*stébnō` (voice word) | **wrong homonym** — belongs to voice/sound dossier | no relation to stem/trunk sense | **must not appear in this entry** |
