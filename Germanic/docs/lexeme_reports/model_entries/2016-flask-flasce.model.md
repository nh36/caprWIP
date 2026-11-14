# flask — OE flasce

PROTO: *flaskō
PROTOFORM: *fláskōn
COUNTERPART: flasce
DERIVATION_CLASS: early_analogy
OUTPUT_STATUS: implementation_gap

### Transducer input and output

| Item | Value |
| :--- | :--- |
| lexical item | flask |
| citation reconstruction / lexeme label | *flaskō |
| selected input form | *fláskōn |
| Old English comparator | flasce |
| classification | early_analogy |
| current cascade output | *fláskōn -> flæsċe |

### Reconstruction and comparative evidence

The wider Germanic family is often cited under a form such as
[flaskō]{.iv .recon lang=pgmc sort=flasko role=source_protoform} 'flask',
whereas the formation relevant to Old English is weak feminine
[fláskōn]{.iv .recon lang=pgmc sort=flaskon role=selected_input} 'flask'
[@Orel2003, p. 104]. Choosing the weak formation identifies the relevant
ending history; it does not make the attested nominative's root vowel
the outcome of an uninterrupted sequence of sound changes.

Ringe and Taylor reconstruct a nominative \emph{*flaskā}, later
\emph{*flæskǣ}, beside the oblique stem \emph{*flaskōn-}, later
\emph{*flæskōn-}. Their final arrow to *flasċe* 'flask' and *flascan*
is explicitly marked as involving development beyond ordinary sound
change [@RingeTaylor2014, p. 192]. The stem followed by a hyphen is not
a complete genitive or accusative reconstruction.

### Old English evidence

The dictionaries give [*flasce*]{.iv lang=oe sort=flasce role=target_form}
'flask', with [*flaxe*]{.iv lang=oe sort=flaxe role=comparison_form} 'flask'
as a variant [@BosworthToller1898, p. 235; @ClarkHall1960, p. 121].
Ringe and Taylor identify *flaxe* and *flaxan* as late West Saxon
[@RingeTaylor2014, p. 192].

The inflected forms must be identified from their syntax. In Gregory's
*Dialogues*, *āne trȳwene flascan wīnes fulle* 'one wooden flask full of
wine' makes [*flascan*]{.iv lang=oe sort=flascan role=comparison_form} 'flask'
accusative singular, the direct object of *sealde*; *flaxan* stands in
the parallel recension [@Hecht1900, p. 66, lines 8--10].
At another occurrence, *twā fatu ... flascan gehātene* 'two vessels
called flasks' has nominative plural *flascan*, whereas *ōðre þāra
flascena* 'one of the flasks' contains genitive plural
[*flascena*]{.iv lang=oe sort=flascena role=comparison_form} 'flasks'
[@Hecht1900, p. 141, lines 25--30; @Toller1921, p. 223].
The following *be þǣre flascan* is dative singular, not evidence for a
genitive singular [@Hecht1900, p. 142, lines 2--4].
These passages establish the weak paradigm but do not supply a securely
identified genitive singular.

### Development to Old English

Campbell explicitly explains singular *flasce* after inflected *flascan*;
Luick likewise derives the singular's root vowel from the plural
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161].
This is positive evidence for root-vowel levelling, not a licence to let
the nominative retain an obsolete back ending until restoration.
The early final-vowel merger removes that trigger: final \emph{*ǭ}
joins \emph{*ō} in \emph{*ā}, which fronts to \emph{*ǣ}.
The nominative consequently keeps its front root and subsequently
undergoes palatalization of \emph{*sk}. The cascade produces
\emph{*flæsċe}, not selected *flasce*.

The oblique root provides an independently identified analogical donor,
but the consonantal history needs separate care. Ringe and Taylor print
palatal *flasċe*. Campbell also discusses *flasce* and *flaxe* among
the forms associated with retained \emph{sk} and later \emph{ks}
[@RingeTaylor2014, p. 192; @Campbell1959, p. 178, §§440--441].
Plain written *sc* does not by itself decide its pronunciation, and
root-vowel levelling alone does not demonstrate when a consonantal
alternation was levelled.

### Formation and cell comparison

| Formation or cell | Reconstructed input | Evidential status |
| :--- | :--- | :--- |
| comparative headword | \emph{*flaskō} | Family label, not the selected weak nominative history |
| selected weak nominative | \emph{*fláskōn} | Current cascade gives front-root \emph{*flæsċe}; attested comparator *flasce* has an explicitly sourced levelled root |
| weak accusative singular | \emph{*flaskōnų} | Ending reconstructed by applying the weak-feminine paradigm to the stem; not a complete form quoted by Ringe and Taylor |

The generic inherited accusative ending is supported by Ringe's
\emph{*tungōnų} paradigm, and its West Germanic erosion is discussed
separately [@Ringe2017, p. 312, §4.3.4(ii);
@RingeTaylor2014, pp. 55--58]. That evidence warrants testing a complete
oblique, not adding an ending solely to obtain a back root. Inflectional
remodelling and the distinct consonantal question prevent an automatic
replacement of the selected nominative by an oblique. Both complete raw
inputs \emph{*fláskōnų} and dative \emph{*fláskōni} are rejected by the
current tokenizer. Diagnostic entry after tokenization instead gives
\emph{*flasconu} and \emph{*flæsċe}, respectively, not attested
*flascan*. This is a modelling limit, not a demonstration that the
inherited endings or the attestations are wrong. The comparator
remains *flasce*; the computational mismatch is disclosed rather than
removed by changing the target.
