# The Lindisfarne *heig/heg* problem (research cycle 2)

Cycle 1 verified that Jones (1989: 21) reports a Lindisfarne alternation
⟨heig⟩ ~ ⟨heg⟩ but could not identify the manuscript locus; the
concordance carried the report as an unverified secondary claim (old
id 26). This file records the cycle-2 investigation and its result.

**Result: the tokens were identified and independently verified in
nineteenth-century diplomatic editions (not yet in manuscript images),
and they do belong to the noun 'hay'.** Jones's report is genuine, and
richer than he indicates.

## 1. Tracing Jones's sources

Jones gives no citation at p. 21. His Table 2.29 (p. 55) sources its
Lindisfarne data to "Ross and Stanley 1956: Bk. 2" — the commentary
volume of the *Evangeliorum Quattuor Codex Lindisfarnensis* facsimile —
and to an index verborum; the facsimile volume is not held here. The
locus was instead recovered through Cook's glossary of the Lindisfarne
gloss, which has a dedicated entry [@Cook1894, s.v. *heg*]:

> **heg** sn. *fœnum*, ns. heg Mt. 6,30; heig J. 6,10; as. heg Mt. 14,19.

Cook identifies the lemma as a strong neuter glossing Latin *faenum*
'hay' — the lexical identification Jones's 'meadow' gloss (Table 2.29)
obscured.

## 2. Independent verification in the editions

Each of Cook's three loci, plus the two further *faenum* verses
(Mk 6:39, Lk 12:28), was checked directly in the Cambridge synoptic
editions, with the relevant printed page images inspected (edition page
images, not manuscript facsimiles):

| Verse | Latin | Lindisfarne gloss | Edition, page | Image checked |
|---|---|---|---|---|
| Mt 6:30 | faenum | **gers ɫ heg** | @KembleHardwick1858, p. 55; @Skeat1887, p. 59 | yes (both) |
| Mt 14:19 | super fœnum | ofer **hehg ɫ gers** (1858); ofer **heg\* ɫ gers**, apparatus "\*hehg, *alt. to* heg" (1887) | @KembleHardwick1858, p. 117; @Skeat1887, p. 123 | yes (both) |
| Mk 6:39 | super uiride faenum | ofer groene **gers** | @Skeat1871, OCR text | OCR only |
| Lk 12:28 | faenum quod hodie in agro est | ðæt **gærs** | @Skeat1874, pp. 130–131 | OCR only |
| Jn 6:10 | faenum multum | **gærs ɫ heig** micil | @Skeat1878, p. 55 | yes |

The Rushworth glosses on the same verses supply further tokens:

| Verse | Glossator | Form | Edition, page | Image checked |
|---|---|---|---|---|
| Mt 6:30 | Farman (Ru1, Mercian) | londes **hóeg** | @KembleHardwick1858, p. 55; @Skeat1887, p. 59; @Tamoto2013, p. 19 | yes (all three) |
| Mt 14:19 | Farman (Ru1, Mercian) | gesittan on **hóeg** | @KembleHardwick1858, p. 117; @Skeat1887, p. 123; @Tamoto2013, p. 47 | yes (all three) |
| Jn 6:10 | Owun (Ru2, Northumbrian) | **heg** ɫ gers micel | @Skeat1878, p. 55 | yes |

Findings of note:

1. **Every Lindisfarne hay token is one member of a double gloss with
   *gers/gærs* 'grass'.** Cook's entry silently normalizes this away
   (he lists bare "heg Mt. 6,30" etc.). Aldred treats *faenum* as
   needing both renderings; at Mk 6:39 and Lk 12:28 he uses *gers* alone.
2. **The Mt 14:19 discrepancy is resolved (cycle 3): the manuscript
   wrote ⟨hehg⟩ and altered it to ⟨heg⟩.** Skeat's re-edition prints
   *ofer heg\* ɫ gers* with the apparatus note "\*hehg, *alt. to* heg"
   [@Skeat1887, p. 123, page image verified]. Kemble–Hardwick printed
   the original spelling, Skeat (followed by Cook and the DOE) the
   corrected one; both are genuine readings of the same gloss at
   different moments of its production. ⟨hehg⟩ thus joins the
   Northumbrian redundant-⟨h⟩ spellings before consonants as a scribal
   first attempt, corrected in situ, and says nothing direct about
   quantity.
3. **Jones's alternation is real but cross-verse**: ⟨heig⟩ is the
   John 6:10 token, ⟨heg⟩ the Matthew ones. It is not a single-passage
   variation.
4. **Farman writes ⟨hóeg⟩ twice, with an acute accent**, in both the
   nominative (Mt 6:30) and the accusative (Mt 14:19) context. Farman's
   Matthew gloss is independent of Lindisfarne, so this is a distinct
   Mercian witness.    Cycle-3 status of the two caveats: (i) the acute is
   printed by three editors working independently on the manuscript
   (1858, 1887, 2013), which makes an editorial invention very unlikely;
   direct manuscript confirmation remains impossible online, since
   Digital Bodleian's Auct. D. 2. 19 digitization is a 49-folio
   selection that omits both relevant pages. **Cycle 5 census; cycle 6
   control audit:** the corrected
   extraction census (FARMAN_ACCENTS.tsv; `extract_farman_accents.py`)
   contains 196 non-target types (299 tokens) plus *hóeg* (one type/two
   tokens), 197 types and 301 Old English tokens total. The old range mixed
   LF line numbers and `splitlines()` indices; the old 327-token figure is
   withdrawn. The cycle-6 audit adds unaccented *weig* ‘way’ at Mark 1:3
   (fol. 52v) to the short-V+glide panel as a closed monosyllable. The
   bounded matched calibration
   (FARMAN_ACCENT_CALIBRATION.tsv) includes unaccented occurrences:
   *weg/dæg* 1/53 tokens (1/9 surface types; 1/2 lexical types), *stīg*
   1/2 tokens (1/2 surface types; one lexical type), and the separate
   short-HL panel 5/133 tokens (5/23 surface types; 4/5 lexical types).
   Short-V+glide closed monosyllables are 1/26 accented and forms with
   following vowel graphs 0/27. Both *stīg* forms have following vowel
   graphs; *stígas* at Mt 3:3, fol. 4v, is supported as accusative plural
   by Latin *semitas eius*, while *stige* on fol. 52v is an uncertain
   alternative beside *gongas*. Treating short-HL as short gives 6/186
   tokens (6/32 surface types; 5/7 lexical types); treating it as
   lengthened gives 6/135 (6/25; 5/6). These selected controls are
   descriptive, not a population-wide accentuation rate, and the single
   long-control lexeme cannot yield a likelihood ratio. They support
   only a cautious statement about Farman's own late tenth-century
   practice, not a ninth-century quantity claim. Eight uncertain
   *gang*-family tokens and one *dægne* are listed separately and
   excluded. (ii) The
   ⟨oe⟩ digraph is a point about **quality and spelling convention, not
   length** (cycle 4, correcting the earlier "/eː/" shorthand): Kuhn
   [-@Kuhn1945, p. 646] discusses *oele* as i-umlaut of **short** Latin
   *o* kept rounded under Northumbrian influence. Farman's ⟨oe⟩ attaches
   to etymological œ̄ < \*ō + i (boéc, foérde, gemoéted), to ē of other
   origins as an inverted spelling — crucially the *hēran* < \*hauzjan
   class (gehóerde, gehóerað), structurally parallel to *hēġ* <
   \*hauj- — and to short œ (*oele*). Since no short control (*wég*,
   *stéfn*, *mónige*) is ever written ⟨oe⟩, the digraph independently
   groups *hóeg* with the ē/œ̄ class; the length evidence itself is
   carried by the acute.
5. **Owun's Jn 6:10 reverses the gloss order and the spelling**
   (*heg ɫ gers* against Li *gærs ɫ heig*). Ru2's John is textually very
   close to Li, but Kotake [-@Kotake2016, pp. 377–396] shows the premise
   of direct copying from the Lindisfarne manuscript itself is not
   established: the non-R–Y readings in Owun's portions may instead
   point to a common source or to intervening copies (his Type 1/Type 2
   distinction, pp. 381–382). For the phonology the consequence is
   limited either way: whether Owun copied Li directly or a close
   congener, his ⟨heg⟩ for ⟨heig⟩ is a respelling within one textual
   tradition, not a fully independent lexical witness — though the
   respelling itself is his own orthographic act and retains that much
   dialectal value.

## 3. Lexical identity

The identity of these forms with the noun 'hay' is secure on three
independent grounds: the glossed Latin is *faenum* in every instance;
Cook's lexicographical identification (*sn. fœnum*) separates the word
from *heh/hēh* 'high' and from *hege* 'hedge' (which Cook lemmatizes
separately); and the semantics of the feeding narratives (sitting down
*super faenum*) suit 'hay/dried grass', not 'hedge' or 'meadow'. Jones's
Table 2.29 gloss 'meadow' is his own loose rendering, not evidence of a
different lexeme. The cycle-1 worry of conflation with *hege* is
resolved for these tokens.

## 4. Grammatical cells

All six new tokens are direct-case (nominative or accusative) with no
overt ending: nominatives at Mt 6:30 ("londes hóeg þæt to dæge is",
"gers ɫ heg") and Jn 6:10 ("gærs ɫ heig micil ... wæs"), accusatives
after *ofer/on* at Mt 14:19. **The cycle-1 finding that no overtly
inflected Old English token has been identified in the sources examined
was accurate for the gospel glosses and remains so; cycle 3 has since
identified overt dative singulars elsewhere (Paris Psalter *hege* ×3 —
see PARADIGM.md), so the claim no longer holds of the language as a
whole.**

## 5. Quantity and accentuation

- No accent is printed on any Lindisfarne or Ru2 token (the editions
  print accents where their manuscripts have them — cf. ⟨hóeg⟩ on the
  same pages — so the absence is meaningful at the edition level).
- Ritt (2000) is now held and consulted. He proposes that Aldred may
  preferentially mark long vowels where length is not predictable from
  spelling; this is an alternative interpretation of the accent
  distribution, not an observation that all accents encode quantity.
  His Matthew count is 426 accents (318 graphically closed, 108 open);
  his p. 508 table accounts for 328/376 non-ambiguous occurrences
  (87.3%), leaving 48 exceptions. His p. 509 CVC sample has an
  arithmetic inconsistency, so its reported predictive accuracy is not
  reproduced. These findings concern Aldred, not Farman.
- The two Ru1 ⟨hóeg⟩ tokens carry acutes in all three editions
  (Kemble–Hardwick, Skeat 1887, Tamoto). With the cycle-3 calibration of
  Farman's practice (finding 4 above and QUANTITY_EVIDENCE.md §2) they
  are probabilistic evidence about Farman's own practice in a Mercian
  witness. The bounded controls do not establish a precise rate or
  discriminate among historical derivations.
- ⟨heig⟩ (Jn 6:10) remains orthographically ambiguous among /ej/,
  /eːj/, /eij/ and a diphthong, exactly as cycle 1 concluded for the
  late West Saxon ⟨heig⟩ spellings.

## 6. Consequences for the article

- CONCORDANCE.tsv: old id 26 (unverified secondary report) replaced by
  verified ids 26–31; negative control Lk 12:28 added as id 32.
- The Northumbrian/Mercian evidence base grows from zero verified
  gospel-gloss tokens to six, with three distinct spellings ⟨heg, hehg,
  heig⟩ in Lindisfarne alone and Mercian ⟨hóeg⟩ in Rushworth1.
- All new tokens show e-type (or ⟨oe⟩) vocalism, consistent with
  Anglian *hēġ* (smoothing of the geminate-route stem) and equally with
  an ungeminated reflex; they do not decide the stem question, but they
  materially broaden the dialect distribution in §3.3 of the draft.
- Verification rests on edition page images for the readings, plus the
  Skeat 1887 apparatus for the ⟨hehg⟩→⟨heg⟩ alteration. Manuscript
  images remain unexamined for these pages: Nero D.iv was not consulted
  directly, and the Digital Bodleian digitization of Auct. D.2.19 omits
  the two Rushworth hay pages, so the Farman acutes cannot at present be
  checked against the manuscript online.
