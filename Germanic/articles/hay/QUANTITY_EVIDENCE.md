# Vowel quantity and syllabification in OE 'hay' (artifact D)

**Cycle 5 extraction-boundary correction:** `FARMAN_ACCENTS.tsv` now
contains 197 types and 301 Old English tokens total: 196 non-target
types/299 tokens plus one target type (*hóeg*)/two tokens. The former
range mixed LF line numbers with Python `splitlines()` indices, including
pre-corpus matter and omitting the end of Farman's stint. The old 327-token
total and its Latin-token subtraction are withdrawn.

**Cycle 6 control audit:** the short-V+glide matching script now includes
the unaccented spelling *weig* ‘way’ in the Mark 1:3 gloss (fol. 52v),
previously omitted from the *weg* controls. It is counted as a closed
monosyllable; the calibration table and rates below reflect the correction.

Question: what does the surviving evidence actually establish about the
direct singular — short /e/ + syllabic /i/ (CAPR Model A's *hei*), /ej/,
/eːj/ (conventional *hēġ*/*hīeġ*), or a diphthong /ei̯/?

The controls are restricted to palatal/glide codas of comparable structure
and chronology: *weġ* 'way' (short e + /j/ by general consent), *dæġ*
'day' (short), *clǣg* 'clay' (conventionally long), *reġn* 'rain', *þeġn*
'thane' (short V + /j/ + C), *ēg/īeg* 'island' (long, same \*-awj-/-auj-
class), *glīg/glēo* 'glee' (\*gliwą/\*gliwi, same structure with i-grade).

| # | Evidence | Bears on | Finding | Decisive? |
|---|---|---|---|---|
| 1 | OE spellings ⟨heg, heig, hig, hyg, hieg, haig, hei⟩ | all | ⟨g⟩ normally spells /j/ (Hogg §2.76); no OE spelling distinguishes /e/ from /eː/ before /j/; ⟨ei⟩ can spell e+j, diphthong, or ē+glide | No |
| 2 | Accent marks | /eː/ | The Ru1 (Farman, Mercian) tokens print ⟨hóeg⟩ with an acute at Mt 6:30 and 14:19 in three independent editions (Kemble–Hardwick 1858: 55, 117; Skeat 1887: 59, 123; Tamoto 2013: 19, 47; page images checked); the manuscript leaves are not digitized. The corrected `FARMAN_ACCENTS.tsv` census has 196 non-target types/299 tokens plus target *hóeg* (one type/two tokens), 197 types/301 Old English tokens total. The matched panel includes unaccented tokens: short-V+glide *weg/dæg* 1/53 tokens, 1/9 surface types, 1/2 lexical types (10 exact spellings); closed monosyllables 1/26, forms with following vowel graphs 0/27. The sole long-V+glide control *stīg* is 1/2 tokens, 1/2 surface types, 1/1 lexical type; both forms have following vowel graphs, and are not a closed-monosyllable match. Its *stígas* (Mt 3:3, fol. 4v) is supported as accusative plural by Latin *semitas eius*; *stige* (fol. 52v) is an uncertain alternative beside *gongas*. Short-HL controls are separately 5/133 tokens, 5/23 surface types, 4/5 lexical types; eight uncertain *gang*-family tokens and one *dægne* are excluded. Treating short-HL as short gives 6/186 tokens, 6/32 surface types, 5/7 lexical types; treating it as lengthened gives 6/135, 6/25, 5/6. These selected controls are descriptive, not a population estimate; repeated tokens are not independent, and no likelihood ratio is inferred from one long-control lexeme. Farman's acutes are evidence about his own practice, not a ninth-century quantity fact. Ritt's completed analysis concerns Aldred, not Farman. | No (bounded descriptive sample; no precise rate or cross-period inference) |
| 3 | ME reflexes: *hei/hai* merging with *wei/wai* 'way' | /eː/ vs /e/ | Minkova 2014: 178 (image-verified): expected /eːj/ 'hay' vs /ej/ 'way' "should not have been preserved" — the merger shows length was neutralized before /j/; therefore ME and ModE *hay* cannot recover OE quantity | No — positively excludes this route |
| 4 | Jones's transcriptions | /e/ vs /eː/ | Internally mixed: [hej]/[heij] (pp. 149, 152) short; Table 3.17 [heej̆]/[hiij̆] long; Table 2.29 puts ⟨heg⟩ in the short [ɛ] class (but glosses it 'meadow', possibly the hedge word); his [klæj̆] 'clay' short against conventional *clǣg* shows his quantity assignments are analysis-dependent | No |
| 5 | Poetic metre | /eː/, syllable count | **Updated cycle 4 (scansions supplied):** verse tokens exist — Paris Psalter 71.16 *heg*, 101.4/101.9/102.14 *hege* (dat.), 105.17 *hig*, and Andreas 38 *hig* (146.9 *hig* is Krapp's emendation of MS ⟨hio⟩). They cannot discriminate: (i) the monosyllabic direct forms stand in lifts, where a closed monosyllable (CVC) is heavy by position whether its vowel is long or short; (ii) the dative lines scan both ways — *ic eom hege gelic* (101.4) and *and ic hege gelic* (101.9) are type-B verses (dip + lift + dip + lift) in which *hege* supplies the first lift either as resolved short *hĕge* or as long *hē-* with *-ge* in the medial dip; both are metrically unexceptionable, so the scansion makes no discriminating prediction, and in 102.14 (*mawenum hege … anlice*) the word's position admits the same two parses; (iii) a resolution-based test would in any case be unsafe here: Fulk (1992: 410–414) shows the Psalter's metre is too degenerate — late, formulaically padded, metrically irregular, dialectally mixed in transmission — to sustain quantitative inference, and Minkova (2003: 23–25) warns independently that resolution is the metrical equivalence least straightforwardly grounded in the ambient language. A negative result, now demonstrated line by line rather than asserted | No — demonstrated unusable, not merely absent |
| 6 | Normalized West Saxon ⟨ie⟩ and direct ⟨hieg⟩ readings | stem identity | *hīeġ* is a normalized citation form, not a uniform manuscript reading. The only direct edition readings ⟨hieg⟩ located are Eadwine Psalter PPs 71.16 and 146.8 (Harsley 1889: 72, 241), Trinity College Cambridge MS R.17.1, c. 1150; images were not checked and the gloss dialect is unassigned. Inspected West Saxon witnesses have ⟨hig/hyg⟩, while later gospel copies have ⟨heig/haig⟩. Hogg (2006: 400) lists palatalization of earlier /eː/, i-umlaut of earlier diphthongs, and hiatus resolution /i+e/ as distinct sources of West Saxon ⟨ie⟩; the first is conditioned by a preceding palatal consonant (Hogg–Fulk 2011 §§5.49, 5.53), the second is treated in §§5.82–84, and the third in §§5.146–147, with the analysis there uncertain; Campbell §234 also documents /i+e/ contraction. None is thereby established for ‘hay’. | No; the attestation, dialect, and applicable historical source remain open |
| 7 | Anglian ⟨heg⟩ (VP ×11, VH, Bede), Kentish ⟨hei-⟩ (S 1196, conventionally 859) | stem identity | Ninth-century Kentish charters write *dæġ* as **dei** (OET Ct. 39, 831; Ct. 42, 837); scribe 7's S 1195 also has *dei*. The expanded Lowe sample adds S 350 *bradan weg* (transaction 898; Canterbury D.C. F 150, s. ix/x; Earle, pp. 157–158; Lowe, App. II.23), a short-vowel control whose language date is debated. S 1196's **Deimund** is in a witness list Lowe says may have been added separately. No diagnostic long-vowel + palatal-glide control was found in the screened Kentish witnesses. Cooper's fourteen-charter corpus includes *higi wegge* (S 508), *heige weye* (S 727), and later-copy *hig weg(e)* variants; their lexical identity and the source of ⟨i⟩ are unresolved. S 1338 *heahstræt*, S 1361 *hæhstræte*, and S 911 *hehstræte* are different compounds and do not independently establish a development of *hēah* to ⟨hei-⟩. Neither S 1196 ⟨hei⟩ nor Anglian ⟨heg⟩ establishes quantity or stem identity. VP *heg* beside *deg* shows a separate short-vowel spelling control. Anglian smoothing of geminate-route \*ēaj gives ēġ; early-apocope \*hewi > \*hei would be orthographically compatible | No |
| 8 | Class parallels *ēg/īeg* 'island' < \*awjō-, *strēgan*, *cīegan* | /eː/ | These show long nuclei from \*auj/\*aujj contraction — but all derive from geminate/protected or heavy structures; they confirm the geminate route's output, not the inherited direct cell | No |
| 9 | *glīg* ~ *glēo* 'glee' < \*gliwą (direct) | fate of \*-wi/\*-wą | Campbell §579(4): \*gliwi "undisturbed" would be ungeminated; attested *glīg* he calls re-formation (§411); *glēo* shows w-retention with back reflex. The one possible regular witness of the ungeminated type is itself disputed | No |
| 10 | OHG *hewi*, Goth. *hawi* | existence of ungeminated direct cell in Gmc | Real and uncontested outside English (R&T p. 53); but Dahl doubts \*hewi ever existed in English ("no recorded w-forms" in OE \*-awj- nouns) | Supports the *possibility*, not the OE fact |
| 11 | Colloquy *mid hig* (dative syntax, no ending) | syllabicity of final i | The endingless Colloquy phrase is not an overt inflection. The late Paris Psalter supplies manuscript-verified dative *hege* ×3 (101.4, 101.9, 102.14), but this eleventh-century evidence cannot establish the date of the donor stem postulated for pre-i-umlaut analogy. The early-cell argument from silence is therefore reduced, not eliminated. | No |
| 12 | WW I.547 *hei* (Worcester F.174, s. xiii) | spelling of final segment | Exact match for Model A's serialization, but **demonstrably discontinuous** (cycle 4): F.174 (Tremulous Hand, s. xiii, Early Middle English — WW's "c. 1150" superseded) abridges the 11th-c. glossary WW no. X, whose parallel entry reads *Foenum, hig, oðde gærs*; and the same F.174 glossary writes *Uia, wei* and *weibreode* for short *weġ*. Its ⟨hei⟩ is a 13th-c. ⟨ei⟩-respelling of exemplar ⟨hig⟩, not a relic | No — positively excluded as continuity evidence |
| 13 | Lindisfarne accents (Aldred) | accentual interpretation | Ritt (2000: 498–501, 505–508) proposes preferential marking of long vowels where spelling does not already predict length. He reports 426 Matthew accents (318 graphically closed, 108 open); his table explains 328/376 non-ambiguous occurrences (87.3%), with 48 exceptions. This is Ritt's analysis, not an observed fact about quantity and not evidence for Farman. His p. 509 100-item CVC sample has an arithmetic inconsistency, so its reported 98% predictive accuracy is not reproduced. | Methodologically relevant to Aldred only; no direct inference for Farman |

## Assessment

- **No independent, decisive evidence identified in the sources examined establishes a long vowel in the OE
  direct singular of 'hay'.** The conventional /eːj/ of *hēġ*/*hīeġ* is
  theory-internal: it is the regular output of the geminate-route stem
  (\*awwj > \*auj > ēa > īe), and the handbooks' length marks are editorial.
- **Cycle-2 qualification:** the absence of decisive independent evidence
  should not be stated as route-specific. All three live derivations of
  the WS/Anglian forms — geminate resolution (B2), levelling before
  umlaut (A2), and Dahl's inherited diphthong — converge on a long
  nucleus; only the consonantal-w route (A0/A1) predicts short /e/, and
  that route fails independently against the WS vocalism. A long nucleus
  is therefore the shared prediction of every account that survives, even
  though no manuscript datum yet confirms it directly.
- The prior claim that West Saxon ⟨ie/i/y⟩ supplies a decisive stem
  constraint is not established by the current word-attestations.
  Normalized *hīeġ* is not a manuscript form; the direct-edition
  ⟨hieg⟩ readings are in an Eadwine Psalter witness of unassigned
  dialect. Hogg's three possible sources of West Saxon ⟨ie⟩ have
  distinct conditions, and their application to ‘hay’ needs independent
  argument. Farman's calibrated acute is a separate, defeasible
  observation about his own practice.
- The evidence that could in principle decide quantity independently has
  now been pursued to its current limits: Farman's two *hóeg* acutes have
  a bounded matched calibration (FARMAN_ACCENTS.tsv and
  FARMAN_ACCENT_CALIBRATION.tsv). The small selected panel is descriptive,
  not a population rate; the acutes are suggestive of Farman's own
  quantity practice, not decisive or transferable to ninth-century
  quantity. Manuscript confirmation is blocked by selective Bodleian
  digitization; Ritt 2000 is now held and concerns Aldred's neighbouring
  Lindisfarne practice, not Farman. The metre is demonstrated unusable (row 5). The
  orthographic lead is now stated more carefully (cycle 4, correcting
  cycle 3): Kuhn (1945: 646) discusses *oele* as i-umlaut of **short**
  Latin *o* retaining a rounded spelling under Northumbrian influence —
  ⟨oe⟩ per se is evidence about vowel **quality and spelling convention,
  not length**. Farman's ⟨oe⟩ words divide into etymological œ̄ < \*ō + i
  (boéc, foérde, gemoéted, gedróefed — all long), inverted spellings of
  ē from other sources — crucially the *hēran* < \*hauzjan class
  (gehóerde, gehóerað, gehóære), the exact structural parallel to *hēġ*
  < \*hauj- — and short œ (*oele*). What ⟨oe⟩ in *hóeg* shows is that
  Farman classed the word's vowel with his ē/œ̄ interchange set (no short
  control — *wég*, *stéfn*, *mónige* — is ever written ⟨oe⟩); the
  **length** evidence is carried by the acute, not the digraph
  (LINDISFARNE_EVIDENCE.md §5).
- Syllabicity: nothing in the record distinguishes /hej/ from /he.i/ for
  the early, non-WS spellings; ⟨heig⟩ is compatible with /ej/, /eij/, /eːj/
  and a diphthong (Jones's own readings span three of these).
