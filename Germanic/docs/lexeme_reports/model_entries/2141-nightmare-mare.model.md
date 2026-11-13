# nightmare — OE mære

PROTO: *márōn
PROTOFORM: *márōn
COUNTERPART: mære
DERIVATION_CLASS: regular
OUTPUT_STATUS: implementation_gap

### Transducer input and output

| Item | Value |
| :--- | :--- |
| lexical item | nightmare |
| citation reconstruction / lexeme label | *marōn- |
| selected input form | *márōn |
| Old English target | mære |
| classification | regular |
| documented output | *márōn -> mare |

### Old English evidence and selected form

The selected form is the weak feminine nominative singular *mære* 'nightmare'. The Corpus Glossary gives *maere* under Latin *incuba*; normalizing the spelling *ae* as *æ* gives *mære* [@Lindsay1921, 96, I225]. Hall distinguishes this weak noun from the strong noun *mær*. Both have a short root vowel and are distinct from the adjective *mǣre* 'famous' [@Hall2007, 301–302, §2].

The variant [*mare*]{.iv lang=oe sort=mare role=comparison_form} 'nightmare' is also attested: *Bald's Leechbook* has the expression *Gif mon mare ride*. Oblique [*maran*]{.iv lang=oe sort=maran role=comparison_form} 'nightmare' occurs in *Leechbook III*. Hall's table separates these contexts from the related glossary copies, which do not constitute independent attestations of one gloss [@Hall2007, 313–314, table 1].

### Reconstruction and the variant

Ringe and Taylor reconstruct a nominative \emph{*marā} beside an oblique stem \emph{*marōn-}, followed by the front-root forms \emph{*mærǣ} and \emph{*mærōn-}. Their printed list includes *mare*, *maran*, and *mære*, not merely *mare* and *mere* [@RingeTaylor2014, 192]. Hall explicitly explains *mare* as levelling of the nominative root vowel to that of oblique forms such as *maran*, in which retraction had applied. This is a paradigmatic development, not evidence that the nominative itself regularly underwent the same restoration [@Hall2007, 301, §2].

### Current derivation and implementation gap

The selected input remains \emph{*márōn}. The unchanged cascade produces *mare*, not the selected *mære*. In the current implementation, the retained nasal ending triggers root-vowel restoration; its output matches an attested variant but does not implement the cited front-root nominative history. The unadopted Model B research experiment yields *mære*. Selecting that attested nominative does not adopt the experiment or change any production sound rule.

The English concept label 'nightmare' indexes the Old English simplex, not an attested compound. The regular classification describes the selected nominative history; the later levelled variant is retained as comparison, not substituted for the selected form to obtain a computational match.
