# *eorþcund* 'earthly': comparative morphology and candidate cells

This file follows the reasoning headings of
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md` so that it
can be read against the same checklist as a real SC dossier, but it is
**not** a Registry adjudication: no SC id exists for *eorþcund*, no
Foma rule is being judged, and no row is allocated or reserved. Per
task scope, this document ends with a recommended *grammatical cell*
and its reconstructed PGmc/pre-OE input, not a RETAIN/REFORMULATE/etc.
verdict.

## Identity

- **SC id:** n/a — lexical research, SC n/a.
- **Executable identifier:** n/a (no Foma rule proposed, defined, or run
  by this research).
- **Date / branch / base commit:** 2026-11-01, `research/earthly-regular-cell`,
  pinned `8f7713c39f26a7f81ef04d29d54070f1b83ab0e0`.

## Question

- **Hypothesis or suspected problem (falsifiable):** at least one
  grammatical cell of *eorþcund* 'earthly' (OE reflex of PGmc
  compound *\*erþa-kunþaz*, Orel 2003: 85, cf. Goth. *airþakunds*) can
  be shown, from independently checked comparative-grammar sources, to
  have a historically regular inherited (or, for pronominal-origin
  endings, regularly remodelled) ending, distinguishable from a
  dictionary's generated/normalized citation form.
- **What would confirm/refute it:** confirmation = an attested surface
  form whose ending is independently attested, in a standard
  comparative grammar's own paradigm table, as the regular reflex for
  that cell in other adjectives (ideally cross-confirmed in ≥2
  grammars); refutation = every attested surface form's ending turning
  out to depend on a disputed sound change or unexplained remodelling
  not independently attested elsewhere.

## Current state (before this research)

- **Existing historical characterization:** `rainbow-earthly-secondary-stress/adjudication.md`
  and `lexical-witnesses-2335-2336/gate-adjudication.md` record an
  existing, **not adopted**, experimental input-gate extension modelling
  strong masc./neut. genitive *\*-as(a)/\*-es(a)* and feminine genitive
  *\*-(a)izōz* endings for this lexeme, with the *-(a)izōz* → *eorþcundre*
  derivation explicitly left open pending a syncope-timing question
  (now the subject of the parent's SC065/066/068 experiments).
- **Existing executable behavior:** none specific to this lexeme is
  final/selected; per the parent's most recent status report, the
  production TSV (390 selected rows) has no *eorþcund* row, and no ID is
  reserved for one.
- **Selected-input assumptions:** none — this lexeme has no selected
  row. The prior audits' experimental replay used ad hoc PGmc inputs for
  the genitive and the feminine genitive only; this research adds
  the Genesis weak-neuter cell and the newly recovered Rule-of-Benedict
  dative-plural cell, neither previously modelled.
- **Existing verdicts/dossiers consulted:** both named audit directories
  (`rainbow-earthly-secondary-stress/`, `lexical-witnesses-2335-2336/`)
  read in full and left unmodified, per task instruction.

## Diagnosis

- **Complete firing census:** n/a in the SC sense (no rule). The lexical
  census is `attestation-census.md` in this directory: three
  independently verified attested cells (Gen. 1627 weak neut. acc.sg;
  An. Ox. 691 strong fem. gen.sg; R. Ben. 139,27 strong dat.pl), one
  reconstructed-but-unattested cell under consideration (masc./neut.
  gen.sg), and two excluded near-homographs (*eardcundes*,
  *eorþcundlic*).
- **Principal witness traces:** for each attested cell, this section
  gives the OE surface form, its PGmc input as printed in Fulk's and
  Campbell's own paradigm tables (verified by direct image inspection of
  Fulk's printed page, not just OCR — see Technical note below), and the
  comparandum within this compound's own family (*godcund*, *eardcund*).
- **Witness role classification:** all three attested cells are "live
  application" witnesses for their respective regular endings (i.e. the
  ending itself is not in dispute as the regular synchronic OE
  reflex); what is **not** settled for the feminine genitive is the
  *diachronic derivation* of that ending from PGmc (see below) — a
  question about sound-law chronology, which is explicitly out of this
  research's scope and belongs to the parent's SC065/066/068 work.

### Technical note: Fulk's superscript-ⁿ notation (resolves parent's nasalization query)

Fulk (2018) prints two visually similar but historically different
things in his paradigm tables, legible only in the actual page image
(`docs/references/fulk_comparative_grammar_early_germanic.pdf`, scan
page 226 = printed p.209; rendered at 200dpi and visually inspected,
then discarded — not retained as a deliverable):

- masc. acc.sg PGmc = **⁠*-anōⁿ*** — a real consonant *-an-* followed by
  a long ō marked with a superscript ⁿ for **nasalization** (not a
  second written *n*). OE reflex in the same row: **langne**.
- neut. nom./acc.sg PGmc = **⁠*-aⁿ*** — a nasalized **short vowel only**,
  with no real consonant at all. OE reflex: **lang**. (This research
  does not assert a specific account of how the OE reflex surfaces from
  the nasalized vowel; no compensatory-lengthening/rounding claim is
  made here, and the OE form *lang* alone does not by itself demonstrate
  any particular derivation — see the Verification note below on the
  parent's v5 replay, which found this correction does not by itself
  yield a regular derivation.)
- Fulk's own prose (§7.8, printed pp.146–147; OCR at
  `fulk_comparative_grammar_early_germanic.vision.txt:8518-8533`)
  glosses this explicitly: "PGmc. *-a [nasalized] < *-an < PIE *-o-m",
  i.e. Fulk's own convention is that a plain, non-superscripted "-an" in
  his prose always names the **earlier**, pre-PGmc stage with a real
  consonant, while the superscript-ⁿ forms in his paradigm tables are
  the **actual PGmc reflexes** he reconstructs, already nasalized vowels
  (for the neuter) or a real consonant plus a nasalized vowel (for the
  masculine accusative).
- **Table-alignment correction (this document's own earlier draft had
  an error here, now fixed by re-inspecting a higher-resolution render
  of the same page):** the printed table's masc./neut. gen.sg row is
  *\*-as(a)* for masc., and **both** *\*-as(a)* **and** *\*-es(a)* for
  neut. (i.e. the *-es(a)* variant belongs to the **genitive** row, as
  an alternate neuter form, not to the dative). The masc./neut. dat.sg
  row is *\*-azmai* for **both** genders — there is no *-es(a)* dative
  form in Fulk's table at all. An earlier draft of this document
  mis-stated "neut. dat.sg also *-es(a)*", conflating the genitive and
  dative rows; that was an OCR/alignment misreading on this document's
  part, not something Fulk's table actually shows, and is corrected
  throughout this document.
- **Consequence for any prior/future experimental input using this
  cell:** an experimental PGmc input written as literal "*-an*" (full
  consonant) for the neuter nom/acc.sg, or literal "*-anōn*" (two
  written n's) for the masc. acc.sg, does **not** correctly represent
  Fulk's own reconstruction; it reads his table's superscript marker as
  if it were plain text. In CAPR's own feature notation (which already
  has first-class short/long nasal vowels **ą**/**ǭ**), the
  table-accurate inputs would use a nasalized vowel, not a bare *-an-*
  sequence, e.g. neut. nom/acc.sg *-ąⁿ* → written with CAPR's **ą**;
  masc. acc.sg *-anōⁿ* → *-an-* (real) + **ǭ** (nasalized long ō). This
  question does **not** touch the masc./neut. genitive *\*-as(a)/\*-es(a)*
  reconstruction or the dat.pl *\*-aimiz* reconstruction, neither of
  which carries a nasalization marker in Fulk's table (verified in the
  same image). It is reported here purely as a **notation** correction,
  not a claim that correcting the notation yields a regular or complete
  historical derivation for either cell.
- **Verification note (parent's v5 replay, reported 2026-11-01, not
  independently re-run by this research — out of scope):** the parent
  reports that testing the corrected nasal-vowel inputs through the
  existing phonology does **not** straightforwardly derive the expected
  OE forms without further qualification: the corrected neut. nom/acc.sg
  input *\*-ą* (nasalized short vowel, no consonant) yields *eorþcond*
  under ordinary prominence assignment, and reaches *eorþcund* only
  under a separate final-overheavy *sensitivity* hypothesis (not a
  demonstrated regular rule); and the corrected masc. acc.sg input
  *\*-anǭ* yields *eorþcundene* (paralleling *godcundene*), which is not
  an attested *eorþcund* form at all. **This research therefore does not
  characterize either the neuter nom/acc.sg or the masc. acc.sg
  nasal-vowel-corrected inputs as regular or historically complete
  derivations for this lexeme; the notation correction resolves what
  Fulk's table says, not whether that input derives an attested OE
  outcome by ordinary phonology.** Consistent with this research's
  original recommendation, no attested *eorþcund* token of either cell
  exists in any case, so neither cell is put forward as a candidate
  here regardless of this phonological question.

### Technical note: a sourced PGmc candidate for the Genesis weak-neuter ending (not merely citing synchronic OE *-e*)

The earlier draft of this document cited the OE weak neuter nom./acc.sg
ending *-e* (Fulk 2018: 217; Campbell 1959: §656) as the "regular
inherited ending" for the Genesis cell, but Fulk's weak-adjective table
itself (§9.8, p.217) gives **only OE forms, with no PGmc column** — so
that citation establishes the ending is regular **synchronically within
OE**, not that a specific "fully regular, complete inherited PGmc
derivation" for it has been independently sourced. That stronger claim
was premature and is corrected here.

An independently sourced PGmc candidate can be built, but only as an
**inference bridging two separate, explicit statements in Fulk**, not as
a single directly-tabulated form:

1. Fulk states explicitly that weak adjectives are n-stem nouns:
   "These are commonly referred to as 'weak' nouns, just as with weak
   adjectives, which are also n-stems (see §9.7)" (§7.29 n.1, printed
   p.168; OCR `fulk_comparative_grammar_early_germanic.vision.txt:10103-10105`).
2. For n-stem (*an-stem*) **neuter** nouns specifically, Fulk's exact
   printed sentence (§7.31, printed pp.169–170) spans a page break and
   uses **two distinct diacritics that must not be conflated**, confirmed
   by direct pixel-level re-render at 260dpi (scan pp.186–187,
   2026-11-01 correction pass; glyph shapes cross-checked against
   unambiguous nearby circumflex/macron tokens on the same page, e.g.
   *"-ē, *-ê, or *-êⁿ"* in an adjacent sentence, which prints macron and
   circumflex side-by-side in clearly different shapes):

   > "...Only *\*-ô* or *\*-ôⁿ* will account for the WGmc. masc. forms
   > ..., and the origin of the trimoric vowel in these, as elsewhere
   > among the *n*-stems, is perplexing. Likewise, *\*-ô* is required to
   > explain Go. neuter *-ō*, whereas the neuter endings in the other
   > languages require *\*-ōⁿ*; PIE neuter *\*-ōn*, however, is to be
   > derived from *\*-on-h₂*..."

   Parsed cell-by-cell, this sentence gives **three different
   reconstructions for what look superficially like "the same" ending**,
   and they do **not** all carry the same vowel quantity:
   - WGmc **masc.** nom.sg: *\*-ô* or *\*-ôⁿ* — **circumflex**
     (Fulk's trimoric notation), explicitly called "perplexing" in
     origin by Fulk himself. This is the **masculine** cell, not the
     neuter cell at issue here.
   - **Gothic** neuter nom./acc.sg (the PGmc-level form needed to
     explain the attested Gothic reflex *-ō*, itself printed with a
     plain macron as an ordinary attested spelling, not a quantity
     claim): *\*-ô* — **circumflex** (trimoric).
   - **WGmc/ON** ("the other languages") neuter nom./acc.sg — i.e. the
     branch that actually includes OE — is explicitly printed as
     *\*-ōⁿ* with a **macron**, not a circumflex. This is the ending
     relevant to the Genesis weak-neuter candidate.

   **Correction to an earlier draft of this document:** an earlier
   version of this file misquoted the WGmc/ON neuter ending as
   circumflex *\*-ôⁿ*, apparently by analogical contamination from the
   immediately preceding (genuinely circumflex) masculine and
   Gothic-neuter clauses in the same sentence. On renewed pixel-level
   comparison this was this research's own transcription error, not a
   property of the source: Fulk's print for the WGmc/ON neuter cell is
   **macron *-ōⁿ* (bimoric nasalized)**, which **matches** CAPR's
   bimoric **ǭ** notation directly — i.e. the earlier (pre-correction)
   candidate *\*érθa-kùnðǭ* was not a bimoric/trimoric notation
   conflation after all; it faithfully transcribes the specific printed
   form Fulk gives for the WGmc/ON branch of this cell. This is
   corrected here to avoid two different errors cancelling out by
   accident: the candidate below is retained, but for the *right*
   documented reason (matches Fulk's own macron) rather than the wrong
   one (an uncorrected circumflex-to-macron conflation).

   Final source check: the reported paragraph image was independently
   inspected during synthesis. The macron in the OE-relevant neuter
   *-ōⁿ* is clear. Fulk's “perplexing” explicitly qualifies the origin
   of the preceding WGmc masculine trimoric vowel, not this bimoric
   neuter reconstruction. Requiring settlement of that separate
   masculine/Gothic corner would improperly make the whole paradigm a
   prerequisite for one OE cell. Fulk connects the neuter ending with
   inherited PIE *-ōn* < *-on-h₂* (Jasanoff 2002: 33, cited by Fulk);
   he also records Boutkan's alternative analogical extension from the
   neuter plural (1995b: 285–286). Preserve that origin alternative:
   the successful FST does not decide it. The preferred regular
   inherited account is Fulk's, not an invented analogy or an
   unmotivated trimoric-to-bimoric operation.
3. **Critically, this *-ō/-ōⁿ* ending attaches directly to the bare
   (unaugmented) stem in the nom./acc.sg, not to an oblique *-an-*-suffixed
   stem.** Fulk's own paradigm table for *guma* 'man' (masc. n-stem,
   printed p.168) shows the *-n-* element **absent from the nominative
   singular** (*guma*) and present only from the **accusative singular
   onward** (*guman*, gen. *guman*, dat. *guman*) — i.e. *-an-* is an
   oblique-case formative, not part of the bare stem. The neuter
   paradigm (*augō* 'eye') shows the identical pattern for number: the
   **singular** nom./acc. row has no *-n-* at all in any reflex (Go.
   *augō*, OIcel. *auga*, OE *ēage*, OS *ōga*, OHG *ouga*); the *-n-*
   is visible in the **plural nominative/accusative examples**
   (*áugōna*, *ēagan*, etc.), which are not the cell in question.
   This is not a claim that every singular oblique lacks *n*.
   **This means the weak-neuter candidate must
   NOT insert *-an-* between the compound stem and the ending:** the
   correct parallel to *augō* > *ēage* is bare stem + *-ōⁿ* directly, not
   stem + *-an-* + *-ōⁿ*. An earlier draft of this document (and the
   reply that accompanied it) instead gave **PGmc *\*erþa-kunþan-ōⁿ***,
   inserting an *-an-* element before the ending "merely from the class
   name" (n-stem) without checking this specific row of the table; that
   was an error, now corrected. The corrected candidate input is:

   **PGmc *\*erþa-kunþ-ōⁿ*** (CAPR inference notation: *\*érθa-kùnðǭ*,
   using CAPR's own nasalized-long-ō symbol, bare compound stem + ending,
   no inserted *-an-*).

   This has the **same final syllable** that an earlier literal,
   pre-nasalization-correction *-ōn* experimental input already used
   successfully for this lexeme, per the parent's report — i.e. once the
   nasalization correction is applied without the extraneous *-an-*
   insertion, the resulting serialization is the direct nasalized
   counterpart of that earlier form, not a new structure. **This is this
   research's own inference, assembled from Fulk's explicit statements
   cited above (points 1–3); it is not a form Fulk himself prints for a
   weak adjective, and is presented here as CAPR-side comparative
   reconstruction, not an author's printed word.** It is distinct in
   structure from the masc. acc.sg PGmc *\*-anōⁿ* (printed p.209, table),
   which genuinely does contain *-an-* in the printed strong-adjective
   ending. That is not permission to insert the same sequence in the
   weak neuter. No independent second-grammar cross-check of
   this specific inferential step (weak adjective = n-stem noun ending
   equation, and the bare-stem-vs-oblique-stem distinction) was performed
   in this research beyond Fulk's own two passages; Campbell (1959) was
   checked only for the OE-internal ending and poetic-license statement,
   not for a PGmc-level n-stem equation.




- **Existing CAPR dossiers checked:** `rainbow-earthly-secondary-stress/{lexical-evidence,literature,adjudication}.md`,
  `lexical-witnesses-2335-2336/gate-adjudication.md` (both preserved
  unchanged).
- **Sources checked, with page numbers:**
  - Fulk, R.D. 2018. *A Comparative Grammar of the Early Germanic
    Languages*. Amsterdam: Benjamins.
    - §9.2, printed pp.209–211 (strong/indefinite adjective paradigm;
      masc. gen.sg *\*-as(a)*, neut. gen.sg *\*-as(a)*/*\*-es(a)*;
      masc./neut. dat.sg *\*-azmai*; all dat.pl, all genders,
      *\*-aimiz*; fem. gen.sg *\*-(a)izōz*). Scan pages 226–228;
      re-verified at 220dpi render, printed p.209/scan 226, 2026-11-01.
    - §7.8, printed pp.146–147 (nasalization notation gloss). OCR lines
      8518–8533.
    - §9.7, printed p.216 (weak/definite adjective syntax: "In WGmc.
      poetry the definite [weak] form may appear even without a
      specifier, especially when the adj. is used as a substantive, as
      is the rule in Gothic."). Scan page ~233.
    - §9.8, printed p.217 (weak adjective paradigm table: neut.
      nom./acc.sg *lange*, ending *-e*, identical in shape to masc.
      nom.sg *-a* mutatis mutandis — table gives OE forms directly, no
      separate PGmc column for this sub-paradigm). Scan page ~234.
    - §7.29–7.31, printed pp.168–170 (the n-stem noun chapter; see new
      section below on the weak-neuter PGmc ending).
  - Campbell, A. 1959. *Old English Grammar*. Oxford: Clarendon.
    - §656 (p.272 by this copy's OCR page markers): weak adjective
      paradigm of *blind*, confirming neut. nom./acc.sg = **blinde**
      (ending *-e*), independently cross-confirming Fulk's *lange*.
    - §638 (p.260–261 by this copy's OCR page markers, between page
      markers "259" and "263"): "OE verse admits a freer use of the
      weak adjective than prose" — independent second-grammar
      confirmation of Fulk's §9.7 poetic-license statement.
  - Orel, Vladimir. 2003. *A Handbook of Germanic Etymology*. Leiden:
    Brill. p.85: "*\*erpa-kunđaz* adj.: Goth *airpa-kunds* 'of earthly
    birth', OE *eorð-cund* 'earthly, terrestrial'." No stress/accent
    marks given by Orel on this entry; any accentuation (e.g.
    "*érθa-kùnðaz*") in prior CAPR documents is CAPR's own addition, not
    Orel's.
  - Bosworth, J. & T.N. Toller. *An Anglo-Saxon Dictionary* (1898) and
    *Supplement* (1921), consulted both via bosworthtoller.com (live,
    2026-11-01) and via the two held OCR texts in `docs/references/`
    (see attestation-census.md for exact line numbers per citation).
  - Clark Hall, J.R. *A Concise Anglo-Saxon Dictionary*, consulted via
    the held OCR text, used only as a cross-reference lead (its "(CP)"
    tag), not as primary evidence for any grammatical cell.
  - Thorpe, Benjamin. 1832. *Cædmon's Metrical Paraphrase*. Consulted
    directly via archive.org (public domain), page "98", for the
    Genesis locus — see attestation-census.md.
- **Source-supported historical phenomenon (exactly what the sources
  demonstrate):**
  1. The OE weak adjective neuter nom./acc.sg ending *-e* is the regular,
     cross-grammar-confirmed reflex for this cell in the entire weak
     adjective class **synchronically within OE** (not a form special to
     *eorþcund*). A PGmc-level derivation of that ending is only
     available as an inference (see the technical note above), not as a
     directly sourced tabulated form.
  2. OE verse licenses a weak (definite-form) adjective attributively
     without an overt determiner, used substantively — stated
     explicitly by two independent grammars (Fulk 2018: 216; Campbell
     1959: §638), not inferred solely from the Genesis example itself.
  3. The strong adjective dat.pl ending *-um* (PGmc *\*-aimiz*) is
     syncretic across all three genders and is independently already
     attested within the same compound family at *godcundum* (Gú. 501;
     Cri. 638, per the prior audit's documentary table).
  4. The strong masc./neut. gen.sg ending *-es* (PGmc *\*-as(a)*, neut.
     also *\*-es(a)*) is likewise the regular strong adjective reflex,
     independently attested within the family at *godcundes*
     (per the prior audit's godcund-control citations).
  5. The strong fem. gen.sg ending printed in Fulk's table is PGmc
     *\*-(a)izōz*, i.e. Fulk himself presents the form with the
     pronominal *a*- as optional/bracketed, reflecting exactly the same
     *-izōz* vs. *-aizōz* uncertainty already flagged in the prior
     audits — this is **not** a new resolution of that question, merely
     an independent confirmation that the ambiguity is native to Fulk's
     own table notation, not an artifact of how a prior CAPR document
     paraphrased it.
- **CAPR modelling decisions (explicitly NOT source claims):** none
  proposed by this research. This document recommends a cell and gives
  its comparative-grammar-sourced reconstructed input; it does not
  propose Foma rule text, environment, or cascade placement — that
  remains the parent's and the registry's responsibility.

## Historical analysis

- **Historical stage:** this research did not independently verify the
  etymology of the *-cund* suffix itself (e.g. any relation to *kunnan*
  'to know' or to being '(be)gotten/born of'); an earlier draft of this
  document asserted such a derivation without a located source, and that
  claim is **withdrawn** as unsupported by the sources actually checked.
  What is directly sourced is only the compound's attestation: Orel
  (2003: 85) lists PGmc *\*erþa-kunþaz* with the Gothic cognate
  *airþa-kunds* and the OE reflex *eorð-cund*, without further
  etymological commentary on the suffix.
- **Historical scope (geographical/genealogical):** the three attested
  OE loci are West Saxon (Genesis), a glossary text (An. Ox. 691), and a
  West Saxon prose translation (R. Ben.) respectively — see
  attestation-census.md for the genre of each individual locus; "poetic"
  applies only to the Genesis locus, not to the Oxford glossary entry.
  The Gothic cognate *airþa-kunds* shows that this specific compound
  (not any individual OE inflectional ending) existed as a formation in
  at least one other Germanic language; this research does not treat
  that cognate as independently proving a PGmc date or an unbroken
  inheritance chain for the compound (that would require comparative
  sound-correspondence argumentation beyond this research's bounded
  scope), only as evidence that the *erþa-* + *-kund-* compounding
  pattern itself is not an OE-internal innovation unique to the three OE
  loci.
- **Regular phonological conditioning:** the complete weak-neuter
  input now succeeds under the same general weight-sensitive medial
  prominence projection as the genitive. Its bimoric nasal ending
  undergoes the existing final shortening/merger; no new ending law or
  quantity transition is required. The new dative instead predicts
  *-em*, not *-um*, even with correct diphthong parsing. Its documentary
  ending is secure but its complete history remains separate and
  unresolved. Neither operation is conditioned on the identity of
  *-cund*, a grammatical case or the lexeme.
- **Counterexamples and falsification:** none found for the weak neut.
  acc.sg or strong dat.pl cells **at the OE-synchronic level** — both
  are maximally regular, paradigm-wide endings with multiple independent
  controls already in the existing documentary table (`godcundum`,
  `godcundes`). The feminine gen.sg cell (*eorþcundre*) remains the one
  genuinely disputed case, precisely because its PGmc source ending is
  itself ambiguous in the primary grammar (*\*-(a)izōz*), independent of
  any CAPR syncope question.
- **Positive evidence for analogy:** none asserted for the two
  recommended cells (no analogy is needed to explain them). For the
  feminine genitive, Ringe & Taylor (2014: 22–23, cited in the prior
  audit's literature.md but not independently re-read in this session —
  **not independently re-verified here**, flagged as an existing
  citation carried over, not new evidence) and Fulk's bracketed
  *\*-(a)izōz* both describe pronominal-inflection encroachment on the
  original nominal *-izōz*, i.e. documented analogical remodelling in
  the broader adjective paradigm, not invented for this lexeme — but
  whether that remodelling had **already** happened by the time of the
  relevant OE sound changes (the parent's SC065/066/068 syncope-timing
  question) is a chronology question this research does not and cannot
  resolve from the morphological sources alone.
- **Relationship between historical phenomenon and executable proxy:**
  n/a — no executable proxy is proposed here.
- **Chronology evidence:** n/a for the two recommended cells (no
  disputed chronology). For the feminine genitive, the chronology
  question (pronominal remodelling timing vs. syncope/shortening
  ordering) is explicitly the parent's SC065/066/068 scope, not this
  research's; this document takes no position on it beyond reporting
  that Fulk's own table bracket shows the *a*- as optional/uncertain
  rather than firmly attested as pre-syncope.

## Recommendation (in place of a Verdict — no Registry-verdict issued)

Three attestation loci are documented; synchronic regularity and a complete
inherited derivation are assessed separately.

1. **eorþcunde** — weak neuter acc.sg, *-e*. Attested (Gen. 1627).
   Regular, cross-confirmed ending (Fulk 2018: 217; Campbell 1959:
   §656). Syntax (determiner-less weak adjective) independently
   confirmed as a recognized, non-anomalous OE poetic construction
   (Fulk 2018: 216; Campbell 1959: §638), **not** merely posited to
   rescue this one example. Fulk's weak paradigm table gives no separate
   PGmc reconstruction for this sub-paradigm directly; a PGmc candidate
   input, **PGmc *\*erþa-kunþ-ōⁿ*** (bare compound stem + nasalized
   neut. nom/acc.sg ending, **no inserted *-an-***), is obtainable only
   by the inference set out in the technical note above (weak adjective
   = n-stem noun, whose WGmc neut. nom/acc.sg ending Fulk separately
   reconstructs as nasalized *\*-ōⁿ* attached to the bare, unaugmented
   stem — not the oblique *-an-*-suffixed stem, which belongs only to
   the masculine accusative singular and the displayed plural cells,
   per the *guma*/*augō*
   paradigm tables). Report this as a comparative inference, not a
   directly tabulated whole adjective. The final v11 assay accepts the
   correctly bimoric `*érθa-kùnðǭ` in the production parser and derives
   *eorþcunde* under every tested prominence sensitivity. Current
   unmodified lowering instead gives *eorþconde*. The complete inherited
   cell is therefore supported under Fulk's regular n-stem account,
   with only the same general prominence correction needed by the
   genitive. It is the preferred attested witness. (An
   earlier draft of this document erroneously inserted *-an-*, giving
   *\*erþa-kunþan-ōⁿ* — structurally identical to the already-tested
   masc. acc.sg serialization and not actually a correct parallel to the
   neuter cell; that error is corrected here.)
2. **eorþcundum** — strong dative plural, masculine by agreement with
   *lustum* (surface ending *-um* is gender-syncretic in OE), surface
   *-um* conventionally traced to PGmc *\*-aimiz*. Attested (R. Ben.
   139, 27/28 — **newly recovered in this research**, prose text,
   independent of the Genesis (poetic) and An. Ox. (glossary) loci).
   The OE spelling itself is regular and independently attested within
   the same compound family at *godcundum*, so **this cell's attested
   synchronic status is the most straightforward of the three**.
   However, per the parent's own experimental replay, a diphthong-coded
   PGmc input *\*-aimiz* does **not** derive the attested *-um* spelling
   under the current system (it yields *eorþcundem*/*godcundem*
   instead); this document's earlier characterization of the ending's
   "regular development" as "already effectively modelled by the
   existing *godcund-* control pair" is withdrawn as premature. The
   *-um* ~ *-aimiz* correspondence remains the standard comparative
   claim in the literature consulted (attested spelling, regular
   paradigm cell), but its complete PGmc-to-OE phonological derivation
   is **not a complete successful history** in the current replay —
   unlike the now correctly represented Genesis weak-neuter cell.
   Only the attested OE form and its
   textual/grammatical regularity (gender-syncretic dat.pl, documented
   compound-family control) are claimed here. Full input as cited in
   the literature: the compound stem cited as PGmc *\*erþa-kunþaz*,
   with nominative *-az* replaced by dative plural *\*-aimiz*; its
   phonological fate is the parent's experimental concern, not an
   adjudicated result of this research.
3. **eorþcundre** — strong fem. gen.sg. Attested (An. Ox. 691, a
   glossary text; exact edition/manuscript not independently
   established — see attestation-census.md).
   Regular only in the weaker sense that *some* historically continuous
   ending underlies it; which PGmc ending (*\*-izōz* vs. *\*-aizōz*) and
   at what relative chronology the pronominal remodelling and any
   syncope applied is **not settled** by the sources read in this
   research. **This research does not recommend treating the
   *-aizōz*-plus-late-syncope account as established enough to displace
   a simpler cell**. The preferred simpler attested cell is Genesis's
   weak neuter, not the dative with an unresolved complete ending.

The previously framed fallback — reconstructed, unattested masc./neut.
gen.sg *eorþcundes* (the same compound stem, with citation *-az*
replaced by *\*-as(a)*) — remains valid
as a documented, regular, but **unattested** fallback; its ending is
independently attested within the family at *godcundes*. No attested OE
*eorþcundes*/*eorðcundes* token was found by this research (consistent
with the prior audit's identical negative result). Its continuing
success is independent of the preferred attested-cell choice, not
superseded evidence or a demonstration of the whole paradigm.

**No Registry-verdict line is issued.** This is lexical research, SC
n/a; selection of a cell, registry row allocation, and any Foma
implementation remain the parent's and the Registry's responsibility.

## Propagation

- **Affected files/registries:** none. No production, registry, Foma,
  corpus, or baseline file was read for modification or written to by
  this research; only `docs/references/*` (main worktree, explicitly
  authorized read-only) and this worktree's own new audit directory
  were touched.
- **Regression tests added/updated:** none (out of this research's
  bounded scope; parent owns experimental replay).
- **Baseline/fingerprint effect:** none — expected and actual.
