# Hay research unresolved evidence

## External evidence

- Ritt 2000: acquired as a restricted ILL scan and consulted; the local
  PDF and article-only OCR are Git-ignored. Its findings concern Aldred,
  not Farman.
- Dal 1934: original article remains on the existing ILL request; its 1971
  reprint is identified (pp. 65–73) but not held. It may clarify the
  original early-loss/inflection argument.
- Approaches to Old Frisian Philology 1998: pp. 21 and the tail after 329
  remain unavailable, while Fulk 1998 is complete.
- Goetz 1971: p. 121 and entire-work completeness beyond the four tranches
  remain unknown.
- Sehrt festschrift: pp. 33--34 and 255 remain unavailable in the local variants.

## Current status after cycle 6

- Cooper (2003) knew of S 1196 and excluded it from his highway chronology
  because he suspected corruption (p. 61 nn. 151, 155). The bounded
  fourteen-charter corpus is in `COOPER_CHARTER_CORPUS.tsv`; it includes
  *higi wegge* (S 508), *heige weye* (S 727), and later-copy *hig weg(e)*
  forms, but their lexical identity and the source of ⟨i⟩ are unresolved.
  S 1338 *heahstræt*, S 1361 *hæhstræte*, and S 911 *hehstræte* are
  different compounds. The bounded corpus supplies no secure independent
  derivation of S 1196 *heiweg* from *hēah*.
- Farman's matched calibration is complete within its stated limits.
  Correct totals are 1/53 short-V+glide tokens, 1/2 *stīg* tokens, and
  5/133 short-HL tokens; the structure, surface-type, and lexical-type
  counts and short-HL sensitivity analyses are in
  `FARMAN_ACCENT_CALIBRATION.tsv`. The one long-control lexeme does not
  support a precise probability or likelihood ratio.
- The only direct edition ⟨hieg⟩ readings found are Eadwine Psalter PPs
  71.16 and 146.8 (Harsley 1889: 72, 241), Trinity College Cambridge
  MS R.17.1, c. 1150. The manuscript readings and dialect are unverified.
  Normalized *hīeġ* must not be treated as a manuscript form or secure
  West Saxon evidence. Hogg (2006: 400) describes three distinct sources
  of West Saxon ⟨ie⟩; their applicability to ‘hay’ remains unsettled.
- The remaining requested publications are Dal (1934) / its identified
  1971 reprint, Wallenberg (1931: 203–205), and Brooks and Kelly (2013).
  They are being pursued separately; no other acquisitions are planned.

## Bounded specialist questions

- ~~Establish the exact literal Minkova p. 178 form~~ **Resolved 22 Nov 2026:**
  400 dpi image verification shows Minkova prints *hēġ* ‘hay’, also spelled
  `<heig>`; the earlier *hæg* reading was erroneous.
- ~~Separate OE short, long and diphthongal quantity evidence from later
  spelling and glide developments.~~ **Addressed 23 Nov 2026** in
  `QUANTITY_EVIDENCE.md` and updated cycle 5: no decisive independent
  quantity evidence establishes the long vowel. Farman's printed acutes
  are suggestive of his own practice, but the bounded matched calibration
  is small and not a population rate; it does not support a ninth-century
  inference. The earlier claim that West Saxon ⟨ie/i/y⟩ securely requires
  an ēa-type stem is not established by the current word-attestations;
  Harsley's direct ⟨hieg⟩ readings have unassigned dialect.
- ~~Determine whether Lindisfarne *heig*/*heg* supports independent
  diphthongization or is best explained by the palatal /j/ environment.~~
  **Locus resolved 23 Nov 2026 (cycle 2):** the tokens are Li Mt 6:30
  *heg*, Mt 14:19 *hehg*, Jn 6:10 *heig*, all double-glossed with
  *gers/gærs* over *faenum*; plus Ru1 *hóeg* ×2 and Ru2 *heg*
  (LINDISFARNE_EVIDENCE.md, CONCORDANCE.tsv ids 26–32). The
  diphthongization-vs-orthography question remains open. Farman's
  cycle-5 calibration concerns his own Mercian practice and does not
  resolve Lindisfarne; Ritt 2000 is now available as an alternative
  analysis of Aldred's practice.
- ~~Compare Jones, Minkova, Mokrowiecki and Goering without importing
  conclusions from later phonological models.~~ **Addressed 23 Nov 2026**
  in `LITERATURE_MATRIX.md` and `QUANTITY_EVIDENCE.md`.
- Preserve the distinction between WS *hīeġ* and extra-WS *hēg*/*hēje*.
  (Maintained throughout the cycle-1 artifacts.)

## New open questions (cycle 1, 23 Nov 2026)

- ~~Verify the Lindisfarne heig/heg locus cited by Jones (p. 21) against a
  held edition or facsimile.~~ **Resolved cycle 2** (edition level):
  see LINDISFARNE_EVIDENCE.md. **Cycle 3:** the ⟨hehg⟩ question is
  resolved (MS spelling altered to ⟨heg⟩, Skeat 1887: 123 apparatus);
  the Ru1 ⟨hóeg⟩ acutes are confirmed in three editions but cannot be
  checked online against the manuscript (see register below).
- On access to Dal 1934 or the 1971 reprint, reconstruct the original
  early-loss argument and test it against Dahl's objections.
- ~~Test Dahl's "no recorded w-forms of OE \*-awj- nouns" claim against the
  full lexicon.~~ **Addressed cycle 2** against the collated record
  (DAHL_REASSESSMENT.md §3): no counterexample found; remains a bounded
  corpus observation (no exhaustive DOE corpus query was possible).
- ~~Source-critical treatment of the *glīg*/*glēo* doublet as the only
  candidate regular witness of the ungeminated type.~~ **Addressed
  cycle 2** (COMPARATIVE_CONTROLS.md §1): consistent with both Dahl and
  re-formation, decisive for neither; a manuscript-level collation of
  the doublet's cells is a remaining desideratum.
- Article Sections 4–8 remain to be written (see RESEARCH_MEMO.md).
  **Cycle 2: Sections 4–7 and a provisional conclusion drafted; see
  RESEARCH_MEMO_CYCLE2.md.**

## New open questions (cycle 2, 23 Nov 2026)

- ~~Manuscript-facsimile check of Li ⟨hehg⟩ (Mt 14:19) against Cook's
  normalized ⟨heg⟩.~~ **Resolved cycle 3 at apparatus level:** Skeat
  (1887: 123) prints *heg\** with the note "\*hehg, *alt. to* heg" —
  the manuscript wrote ⟨hehg⟩ and corrected it to ⟨heg⟩; both editions
  report genuine stages of one gloss.
- ~~Manuscript check of the Ru1 ⟨hóeg⟩ acutes (Mt 6:30, 14:19) in
  Bodleian Auct. D.2.19.~~ **Limit recorded cycle 3:** Digital
  Bodleian's digitization is a 49-folio selection omitting both pages;
  no online check is possible. The acute is printed by three independent
  editions (Kemble–Hardwick 1858, Skeat 1887, Tamoto 2013).
- ~~Interpretation of Farman's ⟨oe⟩ in *hóeg*.~~ **Addressed cycle 3**
  (LINDISFARNE_EVIDENCE.md §5): best read as an inverted spelling of
  /eː/ given Kuhn 1945's demonstration that unrounding was complete in
  Farman's dialect (⟨oele⟩-type inverted spellings; ~140 plain-⟨e⟩
  spellings of the \*au+i class).
- ~~Calibration of Farman's accentual practice.~~ **Bounded calibration
  completed cycle 5** (`FARMAN_ACCENT_CALIBRATION.tsv`): short V+glide
  controls *weg/dæg* 1/53 tokens accented; long V+glide *stīg* 1/2;
  short-HL controls 5/133, with separate sensitivity analyses. This
  selected panel is descriptive, not a population estimate; see
  `QUANTITY_EVIDENCE.md` §2.
- Whether Ross & Stanley 1956 (Bk. 2), Jones's actual source, adds
  manuscript detail beyond the editions used here.

## Outstanding-evidence register (cycle 3, 24 Nov 2026)

Questions not settled by cycle 3; current status is noted below:

1. **Farman's acutes in the manuscript.** Resolvable only by direct
   inspection (or new digitization) of Bodleian Auct. D. 2. 19, fols.
   containing Mt 6:30 and Mt 14:19; the online selection excludes them.
2. **Aldred's accent practice as a control.** Ritt 2000 is now acquired
   and consulted; see `LINDISFARNE_EVIDENCE.md`.
3. **Dal's original 1934 early-loss argument.** The original article
   remains on the existing ILL request; the 1971 reprint, pp. 65–73, is
   registered but unheld. The argument is presently known through Dahl's
   and Hogg–Fulk's reports.
4. **The pre-umlaut dating of the levelled oblique stem.** No attestation
   can reach it: the earliest overt oblique (PPs *hege*, s. xi) postdates
   i-umlaut by centuries. Only comparative evidence (the status of OHG
   *hewi* as inheritance or remodelling) bears on it.
5. **Direct-case quantity.** Farman's two printed *hóeg* acutes have
   bounded, selected calibration and suggest his own practice only; they
   do not establish ninth-century quantity. The metre is demonstrated
   unusable (Fulk 1992: 410–414) and ME reflexes are neutralized
   (Minkova 2014: 178).
6. **Ru2's exact exemplar.** Kotake 2016 leaves direct copying from Li
   unproven; a full collation of Owun's non-R–Y readings against the
   Aldredian manuscripts would be needed, and does not affect the hay
   evidence materially.

These are substantive research questions, not metadata or ingestion failures.

## Cycle-4 adjudications (24 Nov 2026)

- ~~Whether Model A's regular output *hei* survives in the attested
  record.~~ **Adjudicated** (RESEARCH_MEMO_CYCLE4.md): the spelling is
  attested (S 1196 compound, 859; F.174 independent noun, s. xiii) but
  not as an OE independent noun, and not demonstrably in continuity with
  the early-apocope output — F.174's ⟨hei⟩ is positively excluded
  (respelling of exemplar ⟨hig⟩). WS = Outcome C, manuscript-grounded;
  a dialect-differentiated relic (Outcome B) remains **unfalsified but
  undemonstrated and orthographically untestable** (ninth-century
  ⟨ei⟩/⟨eg⟩ spell /Vj/ regardless of quantity: dei/deg controls).
- ~~Date of the *heiweg* charter.~~ **Qualified:** S 1196 is conventionally
  dated 859 (?859 in Lowe); its surviving single sheet is BL Cotton
  Augustus ii.16, s. ix med., and the witness list and possible later copy
  require qualification. Dahl's "839" is a slip (he dates the same charter
  859 at *Scufelingforde*). See `RESEARCH_MEMO_CYCLE5.md`.
- **Bounded Farman calibration completed; no full-corpus rate claimed**
  (`FARMAN_ACCENT_CALIBRATION.tsv` and `calibrate_farman_accents.py`).
  The corrected accented census has 196 non-target types/299 tokens plus
  *hóeg* (one type/two tokens); its boundary now uses `splitlines()` indices
  anchored to fol. 1r and Mk 2:15. In the matched sample, *weg/dæg* are
  1/53 tokens accented, *stīg* 1/2, and short-HL controls 5/133. The
  short-HL sensitivity treatments produce 6/186 if counted as short and
  6/135 if counted as lengthened. These small, selected counts describe
  Farman's printed late tenth-century practice only; Ritt's analysis
  concerns Aldred's practice, not Farman's.
- ~~Interpretation of Farman's ⟨oe⟩ (refined).~~ **Revised cycle 4:**
  ⟨oe⟩ is quality/convention evidence, not length (Kuhn 1945: 646 on
  *oele* < short o); it groups *hóeg* with Farman's ē/œ̄ class
  (gehóerde < \*hauzjan = structural parallel), while the acute alone
  carries the quantity evidence. Supersedes the cycle-3 "inverted
  spelling of /eː/" shorthand.
- Remaining open: direct manuscript confirmation of the Farman acutes,
  Aldred's accent practice, access to Dal, pre-i-umlaut donor timing,
  the exact historical inference from the quantity evidence, and Ru2's
  exemplar. The bounded Kentish charter search and Farman calibration
  are complete; neither supplies a diagnostic result for ninth-century
  quantity.
