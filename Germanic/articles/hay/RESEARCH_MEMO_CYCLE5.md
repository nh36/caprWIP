# Hay source intake and targeted philological investigation: cycle 5

> **Historical calibration status:** Cycle 7 expanded the long-V+glide
> panel to include independently long *stīgan* forms and corrected the
> short-HL sensitivity result: the old 6/135 count below is superseded by
> 6/147. The current bounded results are in
> `FARMAN_ACCENT_CALIBRATION.tsv` and `RESEARCH_MEMO_CYCLE7.md`.

Date: 2026-11-24. Status: provisional evidence memorandum. This cycle
verifies supplied publications, the charter and gospel witnesses, and the
specific lexical/phonological implications requested. It does not adjudicate
the production cascades or settle the article's historical argument.

## Holdings, identification, and extraction

Eight distinct new works were registered in the general CAPR library.
Versloot (2026) was already held and registered as `Versloot2025`, so the
existing item was reused. The two supplied Trousdale PDFs are byte-identical;
one private copy is retained. The nine works are listed with source IDs,
bibliographic keys, hashes, page counts, page maps, and extraction status in
[`docs/references/hay-article-literature-2026-11-24/holdings.tsv`](../../../docs/references/hay-article-literature-2026-11-24/holdings.tsv).
Full PDFs and searchable texts are private under the corresponding
Git-ignored `docs/references/local/` directory. They are not duplicated in
this article directory. Downloads were not moved or deleted.

The catalogue's November cleanup did not establish a cross-worktree private
library: its documented shared-root/symlink design remains a recommendation,
and `docs/references/local/` is checkout-specific. All nine registered
publications are accessible in this checkout; their next-worktree
availability must be rechecked. The reference-library validator confirms
that private holdings remain ignored. No hay-relevant publication was found
in Downloads, and no further general acquisition was pursued.

Pagination audit: Trousdale 2005 pp. 59–76 occupy PDF sheets 1–18
(printed page = sheet + 58); cited pp. 60–65 are sheets 2–7. The existing
Versloot article has 39 PDF sheets, with pp. 103–141 on sheets 1–39
(printed page = sheet + 102). The holdings, catalogue and page map now agree.

The Wallenberg discrepancy is resolved bibliographically: the required
1931 *Kentish Place-Names: A Topographical and Etymological Study of the
Place-Name Material in Kentish Charters Dated Before the Conquest* (378 pp.)
and the 1934 *The Place-Names of Kent* (626 pp.) are different books. The
1931 work, pp. 203–205, is not held; Electronic Sawyer cites Wallenberg,
KPN, pp. 205–207 on S 327 place-names, so those pages may clarify the
charter's toponymic segmentation, not independently establish the identity
of *heiweg*. The 1934 book is not a substitute. Dal's 1934 article was
reprinted in *Untersuchungen zur germanischen und deutschen
Sprachgeschichte* (Universitetsforlaget, 1971), pp. 65–73. The reprint is
not held; catalogues disagree between 1971 and [1972]. The original remains
on the existing ILL record; no new request was initiated. Brooks and Kelly's
2013 *Charters of Christ Church Canterbury* is also unheld and could provide
authoritative texts and commentary for S 1196 and the scribe-7 comparisons.

Bryan's native text layer is searchable but corrupts historical type and
diacritics; Tesseract search aids were generated for the cited pages and the
page images were checked for `heiweg`, `dei`, `meihanda`, and `meghond`.
Skeat's old scan text layer is badly distorted in the gospel columns; the
relevant sheets were separately OCRed, but the readings below rest on the
page images and edition apparatus, not OCR. The remaining article sources
have usable page-separated native or OCR text, with originals authoritative.
OCR aids and complete extracts remain private.

## Literature verified

### Bryan 1915, pp. 8, 23, 25

Bryan prints *hei < *hauja-* in a note on p. 8 and elsewhere identifies
*heiweg* as the charter's spelling; on p. 23 he records *meihanda* beside
*meghond* and describes ⟨ei⟩ from ⟨eg⟩. On p. 25 he distinguishes the
⟨ei⟩ of *heiweg* from *dei* ‘day’, whose ⟨ei⟩ he derives from short ⟨eg⟩.
This establishes that Bryan recognized both short- and long-vowel histories
behind ⟨ei⟩; ⟨ei⟩ itself is not a quantity mark. His quantity for ‘hay’
is not independently demonstrated by metrical, accentual, or manuscript
evidence: it follows from the historical reconstruction he assumes in
*hauja-*. His note immediately attributes the comparison of the Kentish
element with Gothic *gawi* to Miller and Chadwick, so the lexical
identification is not shown to be independent of that earlier etymological
discussion. It does, however, predate Dahl. Bryan's p. 8 list labels
*heiweg* charter XXVI; his p. 25 discussion correctly identifies it as
XXIV. The discrepancy is suitable for a source-critical footnote.

### Lowe 2001, pp. 76–78, 85–86; Trousdale 2005, pp. 60–65

Lowe calls S 1196 `? 859`, not an unqualified original dated and written in
859. Æthelwulf appears in the witness list although he died in 858.
Campbell suggests a slightly later copy with a date slip; Keynes notes the
smaller witness script may indicate a separate addition; Lapidge considers
the scribe to have copied a charter he did not understand (Lowe, pp. 85–86).
The surviving single sheet is Cotton Augustus ii.16, s. ix med.; the
transaction/date convention remains 859. The article should retain the
conventional date but qualify the document's transmission.

Lowe's p. 77 n. 19 places S 316, S 328, S 332, S 344, S 1195, S 1196, and
the confirmation in S 1197 among Brooks scribe 7's work. The initial grant
in S 1197 is separately assigned to scribe 6. Lowe's appendix distinguishes
dates and manuscript witnesses; the references and relevant hand-specific
segments are recorded in `SAME_SCRIBE_CONCORDANCE.tsv`. Trousdale (pp. 60–65)
adds that Brooks regarded scribe 7's Latin and orthographic practice as
uncontrolled and “particularly unattractive”; this is a reason to document
his examples, not to infer a sound law from an isolated spelling.

### Langlands 2019, pp. 45–46, 109, 126; primary charter checks

Langlands favors ‘hay-way’ for S 445 *higweges* on topographical grounds:
the route passes through enclosed meadowland, and a nineteenth-century map
calls the route through the meadow Mower's Lane (p. 109). S 445's transaction
is dated 939, but its surviving witness is a fifteenth-century copy, BL
Harley 61, ff. 15v–16v. At Meavy, S 963 (transaction 1031; Cotton Augustus
ii.69, s. xi 1), *boc sætena hig wege* is disputed: Finberg favors ‘high
way’, Hooke ‘hay-way’. Langlands does not turn the spelling into a secure
hay identification. The Edington bounds in S 765 (transaction 968) have
*hegweige*; the surviving witness is a fourteenth-century copy, and
Langlands leaves the interpretation open (pp. 45–46, 126). These examples
establish that a ‘hay-way’ compound is a credible lexical possibility, not
that Kentish S 1196 has that meaning.

### Wager 2017, pp. 169–174

Wager distinguishes fodder hay from enclosure vocabulary represented by
*hege*, *haga*, and *(ge)hæg* (especially pp. 170–174). S 296 (845) calls a
river meadow near Canterbury *be norðan hege*; Reculver S 546 (949) has
*ealden hege* and *Gata gehægge*. The S 546 charter's authenticity and
transmission are disputed, as Wager notes. S 328's *hegforde* is therefore
not automatically fodder ‘hay’; its local context is *Stocmed healf be
norðan hegforde* (a meadow to the north of Hegford). If the first element is
the feminine *hege*, loss of its final vowel in the compound needs a
morphological explanation; a consonant-final member of the *(ge)hæg* family
could avoid that particular issue. The available evidence does not establish
which base, if either, is present. The same morphology prevents treating
enclosure as an impossible third etymology.

### Skeat 1871, Mark 6:39, pp. 48–49

The printed edition image gives the West Saxon base text CCCC 140 *hig*,
Hatton 38 *haig*, and Royal 1 A.xiv *heig* in the context corresponding
to Latin *super uiride faenum*; the Old English phrase is *sæte ofer þæt
grene hig*. Rushworth has *hegge* alongside *grese*, not a compound
`heggetgrese`. This is a hay/grass glossing context; its exact lexical
segmentation should not be used to claim an independent short direct stem.
The Rushworth Mark 6:39 gloss is Owun's, since Farman's contribution ends at
Mark 2:15. It is not a Farman accent-calibration token.
In the hay-bearing West Saxon clause, *hig/haig/heig* is syntactically
accusative singular after *ofer*; Latin *super uiride faenum* independently
identifies the referent. The Lindisfarne *grese* is ‘grass’, not a hay form.
For Rushworth, the edition layout does not securely assign case or
word-for-word alignment to *hegge* and *grese*.

The edition's column witnesses are not four independent lexical traditions:
the base and later West Saxon copies are related gospel witnesses; Rushworth
is its own gloss tradition. The spellings have no written accent or
quantity mark. For *hig/heig/haig*, the graphemes do not independently
establish vowel quality or quantity beyond conventional front-vowel reading.
The doubling in Rushworth *hegge* belongs to its spelling and/or lexical
segmentation; with no manuscript image or contrastive local evidence
established here, it cannot be treated as proof of a geminate or of the
noun's independent nominative shape. Skeat's introduction identifies
Rushworth's two glossators; manuscript-hand and edition limits are retained
in the revised attestation dossier.

## Same-scribe concordance and lexical controls

The reproducible concordance is `SAME_SCRIBE_CONCORDANCE.tsv`; its source
scope is the seven documents identified by Lowe, with the S 1197 grant and
scribe-7 confirmation distinguished. The complete searchable English
texts were reviewed for the listed spelling families, including negative
results: no independently identifiable ‘high’ token or non-target
long-vowel + palatal-glide control was found; S 344 has no secure diagnostic
occurrence. These are corpus-specific non-attestations, not evidence of
phonotactic prohibition. The principal positive comparanda are
S 1195 *dei* ‘day’, a spelling of a short-vowel + palatal-glide word, and
the compound *heiweg* in S 1196. The latter is the target and is excluded
as evidence for the sound development that would identify it as ‘high’.
S 328 *hegforde* is a secure spelling but its lexical identity is unresolved.
S 316 *bromteag* is an enclosure comparator, not a hay-form. S 1195 and
S 332 *higum* and the S 1197 confirmation *hiawum* mean ‘household/community’,
not ‘hay’; the S 1197 main grant's *higum* is excluded from scribe 7 because
Lowe attributes that section to scribe 6. S 344 provides no secure diagnostic
opportunity. No independently secure instance of ‘high’ or a same-corpus
long-vowel + palatal-g control was found. These absences do not establish a
phonotactic prohibition.

S 1196's witnesses and *Deimund* cannot be uncritically used as
same-scribe controls: Lowe notes their smaller script and possible separate
addition. The non-target corpus does not settle whether *heiweg* means
‘hay-way’, ‘highway’, or an enclosure-related compound.

## Expanded Lowe charter search

The bounded extension searched the relevant spelling families in
Lowe-catalogued Kentish charters, then inspected the candidate records and
English bounds. Electronic Sawyer's text search is not fully reliable, so
this is a documented targeted search, not an exhaustive searchable-database
claim.

- **S 332**: transaction 863; Canterbury D.C. M 14, s. ix med.; Lowe
  Appendix II.17; Earle, pp. 133–136. *Heahmund* is a Latin witness-name,
  not an English lexical token of ‘high’; English grant (b) has *higum*
  ‘community/household’ from *hīw*.
- **S 1203**: transaction 875; BL Cotton Augustus ii.89, s. ix 2
  (BM Facs. ii.40); Lowe Appendix III.60; Earle, pp. 141–144. *Heahulf*
  is a Latin witness-name, not a lexical token. The manuscript is usually
  dated s. ix 2, but whether it was copied at the 890–923 Plegmund
  confirmation is disputed; transaction and manuscript dates are distinct.
- **S 327**: transaction ?860, with the date altered to 790; BL Cotton
  Charter viii.29 (Sawyer dates the witness s. ix 2; its older-text
  description gives s. x 2 [?]); Lowe Appendix II.15; Campbell,
  *Rochester*, no. 24. Its bounds include *Meodowæge*, not an independent
  occurrence of ‘high’.
- **S 331**: transaction 862; BL Cotton Charter viii.32, s. ix 2; Lowe
  Appendix II.16; Campbell, *Rochester*, no. 25. No secure lexical ‘high’
  token occurs in the inspected bounds. S 344 (transaction 873; BL Stowe
  Charters 19, s. ix 2; Lowe Appendix II.21; Sweet, OET no. 32, p. 440)
  likewise supplies no diagnostic token.
- **S 350**: transaction 898, a grant of land at Farleigh, Kent, issued at
  Wulfamere; Canterbury D.C. F 150, s. ix/x; Lowe Appendix II.23; Earle,
  pp. 157–158. *Bradan weg* is a short-vowel *weg* ‘way’ control. The date
  of the language is disputed (Stevenson 1904, pp. 151 n. 2, 290 n. 1;
  Brooks 1984, pp. 169, 359 n. 67, 361 n. 72). *Medewæge* is not counted
  as a ‘meadow-way’ control: Sawyer translates the boundary as the Medway.
- False positives were excluded: S 339 (transaction 868) survives only in
  Textus Roffensis, s. xii 1; its *Heahmund* is a witness-name. Search-hit
  S 403 contains *heagam* in Sussex bounds (transaction 930; Barker 1948,
  pp. 139–145, no. 26), but its copies are s. xiii med. and s. xiv, so it
  is neither Kentish nor a contemporary ninth-century witness.

**Result:** no securely identified lexical *hēah* token or independent
⟨i⟩ spelling of its relevant consonantal reflex was found in the targeted
contemporary Kentish charter witnesses. The secure short-vowel controls
include *dei* in S 1195 and *bradan weg* in S 350; no diagnostic
long-vowel-plus-palatal-glide charter control was found. The proper names,
compound *heiweg*, non-Kentish *heagam*, and *hīw* forms are not evidence
for the missing regular sound correspondence. This negative result is
limited to the inspected witnesses and spellings.

## Three-way assessment of *heiweg*

1. **‘High’ from *hēah*.** The expected first member would be a
   *hēah-/hēa-* stem in *hēahweg* or a regularly reduced compound
   allomorph. To explain ⟨hei-⟩, the account needs an independently
   regular development by which the historical final consonantal segment
   of *hēah* is lost or represented by ⟨i⟩ as /j/ in ninth-century
   Kentish. No parallel establishing that outcome in this environment
   was found in the charter corpus or the consulted literature. A
   compound-specific reduction introduced only for *heiweg* would be
   hypothetical, not an established sound change. Nor may *heiweg* itself
   be used to prove the process that makes it mean ‘high-way’. This
   remains a historically proposed lexical reading, but its phonology is
   presently the least independently supported.
2. **Fodder ‘hay’.** The expected inherited neuter ja-stem is
   Proto-Germanic *hawją*, with an inherited *w*-bearing direct stem;
   Bryan writes the comparative form *hauja-*. Under Model A, the
   relevant expected sequence is *hawją > hawi > hæwi > hewi*, followed
   by the unresolved hiatus development /he.i/ > /hej/ versus contraction
   to *hē*. A compound formed with the ungeminated stem could therefore
   be ⟨heiweg⟩ only if that proposed development and stem use are correct;
   the charter does not establish them independently. A competing
   geminate/protected-stem history has a different expected compound
   shape. The meaning has direct support from the *faenum* gospel glosses
   and independent plausibility from Langlands's compounds. Bryan's
   ‘hay’ identification predates Dahl, but his vowel quantity is
   reconstructed rather than independently evidenced. A compound stem
   may preserve a shape not found in the simplex paradigm; even a secure
   ‘hay’ reading of *heiweg* would establish neither vowel quantity nor
   survival of independent nominative–accusative singular *hei*.
3. **Enclosure family (*hege, haga, (ge)hæg*).** This is contextually
   credible in charter boundary vocabulary: S 316's *bromteag* is
   translated ‘broom enclosure’, S 296 has *be norðan hege*, and the
   S 1196 clause concerns a boundary beside meadows. For S 328
   *Hegforde*, a consonant-final *(ge)hæg* compound stem could yield
   *heg-* without an added linking vowel; identifying the first element
   with inflected *hege* instead would require explaining the missing
   final vowel. For *heiweg*, an enclosure derivation would additionally
   need to establish how the family yields ⟨hei-⟩ in this dialect and
   compound environment; no independent same-scribe development has been
   found. Agricultural context alone does not decide between fodder and
   enclosure.

**Provisional ranking:** ‘hay’ has the strongest positive lexical support
from the later glossing and independent hay-way compounds; the same
meaning is plausible, but not proven, for S 1196. The ‘high’ analysis lacks
an independently demonstrated final-consonant development. Enclosure
remains a live competing possibility, especially for *Hegforde*, and cannot
be excluded for *heiweg*. Expert adjudication is still needed on the
Kentish morphology and the exact boundary-term lexicon.

## Model A and the independent direct stem

The secure S 1196 reading *heiweg* is compound-internal. It is orthographically
compatible with the predicted direct stem *hei*, but equally compatible
with a levelled long-vowel stem under the local ⟨ei⟩ conventions and with
non-hay lexical analyses. It supplies no independent nominative–accusative
singular token. The other known secure OE ‘hay’ attestations do not positively
identify the short ungeminated direct stem; the late Farman acutes instead
offer defeasible evidence for a long nucleus in that witness.

The corrected Farman census contains 196 non-target accented types
representing 299 tokens, plus target *hóeg* (one type, two tokens): 197
types and 301 Old English tokens total. The former bounds were LF line
numbers applied to a `splitlines()` slice; the corrected indices begin at
the fol. 1r marker and include the final *hleonadun* at Mk 2:15. The older
327-token statement and its purported Latin subtraction are withdrawn.

The reproducible matched sample in `FARMAN_ACCENT_CALIBRATION.tsv` counts
all tokens, accented or not, in selected glide and cluster-control words.
Short-V+glide *weg/dæg*: 1/53 tokens accented, 1/9 surface forms and 1/2
lexical types with an accent. Long-V+glide *stīg*: 1/2 tokens, 1/2 surface
forms, one lexical type. Potential short-HL controls (*gangan* clear verbal
forms, *lond*, *word*, *hond*, *cild*): 5/133 tokens, 5/23 surface forms,
4/5 lexical types. Eight ambiguous *gang*-family forms are separately
listed and excluded. Treating the short-HL panel as short yields 6/186
accented tokens in the combined short class; treating it as lengthened
yields 6/135 in the long-like class. These small, deliberately selected
controls are descriptive and not a population-wide accentuation estimate;
token repetitions are not independent, and the long-V+glide control is one
lexeme with two occurrences. The full census has 162 accented long-vowel
types, 14 short-HL types, 13 short types, and 7 uncertain types. This
calibration describes Farman's printed late tenth-century practice only
and does not establish ninth-century Old English quantity. It does not
alter the regular Model A derivation, the hiatus question, the West Saxon
controls, or the distinction between generating a reconstructed cell and
demonstrating its survival.
