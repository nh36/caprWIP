# Barrack (1975) census quality-control report

Second-pass review of the 231-row rule census against fresh 300 dpi
renders of printed pp. 38–127 (and 600 dpi for p. 136), performed after
the first integration (commits `d58f8c86`, `493b4ec7`). Every census
row was re-read against its page image; the two known problem rules
(NWG 331.6a, WG 404b) were re-transcribed by the lead reviewer directly
from the print.

## 1. Substantive description errors corrected

These census rows previously misdescribed what Barrack proposes. All
were re-verified against the printed page before correction.

| Rule | Pages | Old census claim | Verified reading |
| --- | --- | --- | --- |
| NWG 331.6a | 81 | "Final *m becomes ū" | Raising of unstressed rounded *o → *u before *m* (*om → um*); the `-mV` restriction is declared unnecessary because final *m* has already become *n* by 331.1z. Witness *tungōmiz* → OE *tungum*. Genuine rival input-value account to CAPR SC005. |
| WG 404b | 101–102 | change "producing m" | Loss of R before voiced dentals (*đ, d, n*) with compensatory lengthening of the preceding vowel; "evidence … very sporadic"; PG *mizdō* → *mēd* 'reward, meed'; the *meord* development is a separate path at 139zc(IIIA). Distinct from 404a (rhotacism feed) and 404c (final R-loss). |
| WG 404c | 102 | conflated with 404b | Word-final R-loss after an unaccented vowel ([∼(ac 1)][—]#); *dę̄diz* → WS *dǣd*; formally ordered before 404e and 331.4b. |
| WG 404d | 102 | under-described | *Rn* → *nn* after an accented vowel, "very sporadic"; *razn-* → *ærn* 'house' (derivation also passes 459.1 and 476); ordered before 404e. |
| PG 400z | 100 | *hrā* misattached to 404b | *hrā* 'corpse' belongs to 400z (w-loss family), not to 404b. |
| WG 406 | 104 | deletion direction inverted | Deletes *w* before *i* (not *i* after *w*). |
| WG 409 | 105–106 | output garbled | *đ* → *d* (dental hardening). |
| 422 | 108 | feature sign flipped | [+cnt] misread for printed [−cnt]. |
| 475b | 122 | "nasal deleted" | Deletes *r* in *rn(C)#*, not the nasal. |
| 480.1 | 124 | voicing direction inverted | Devoices *d* → *t* (not voicing). |
| PG 311.4a (printed) | 77 | treated as OCR error | The print itself reads "PG 311.4a"; this is the book's own misprint for 331.4a (unrounding [α low +rou] → [+low −rou]). Recorded as `VERIFIED_PRINT_MISPRINT`. |

In addition ~45 rows received glyph-level corrections (breve vs.
macron, *đ* vs. *d*, arrows, feature-matrix signs) found by the
six-tranche page-by-page re-read: 12 on pp. 38–52, 7 on pp. 53–67,
8 on pp. 68–82, 9 on pp. 83–97, 11 on pp. 98–112, 6 on pp. 113–127.
Rules 459.1 and 459.3 (r-metathesis, pp. 115–117) were exhaustively
re-transcribed, including all (III) derivations and ordering remarks,
as input to the SC087 adjudication.

## 2. Propagation audit

The corrected 404b/404c readings had leaked into reader-facing prose
and the crosswalk. Fixed:

- `reader_facing/003-west-germanic-rhotacism.md` (404b sentence).
- `reader_facing/chap2-pnwgmc-to-pwgmc-intro.md` (404b sentence).
- `capr_crosswalk.tsv` rows SC003 and SC097 (`conditioning_comparison`).
- `ocr_reconciliation.tsv` row 311.4a → `VERIFIED_PRINT_MISPRINT`.

No other reader-facing file cited 404b/404c/331.6a content.

## 3. p. 136 ordering chart re-read (600 dpi)

The "Chart of Principal Transitive Relationships" was re-rendered at
600 dpi in quadrants. Findings:

- The perimeter rule labels are now fully legible (clockwise sequence
  includes 120.1z, 128, 130a, 130b, 131, 134, 135a, 135z, 136, 139zb,
  139zc, 142, 143a, 143b, 146a–d, 157, 162, 170a, 171a, 179, 185z/b/c,
  190a/b, 193(d), 194, 200, 202, 210, 212, 241, 285, 333a/b, 335,
  339a/b, 341, 345, 347, 348, 351, 355.1, 355.5, 358, 365, 398.4b,
  428, 433b, 434, 440a, …).
- Short rim-adjacent arcs between neighbouring labels are legible
  (e.g. 162 → 170a → 171a; 142 → 143a → 143b; 131 → 134; 335 → 333b).
  These corroborate ordering statements already printed in the rule
  texts (`x > NNN`); they add nothing new.
- The interior straight chords remain too dense and unlabelled to
  attach endpoints securely even at 600 dpi.

Accordingly **no ordering edge has been inferred from the chart**;
the census records only the per-rule printed `x > NNN` statements, and
those remain formal, not chronological (Barrack p. 34).

## 4. Remaining uncertainty

- 38 reverse-index rows are classified `UNRESOLVED` and 55 carry
  disposition `VERIFY_SOURCE`: mostly feature-matrix internals on
  pp. 38–47 (dense matrices, PARTIAL legibility) and late orthographic
  rules whose CAPR relevance cannot be decided without per-SC study.
  They are visibly open in `barrack_to_capr.tsv`, not silently
  classified.
- The agent transcription of 459.1's (I)-statement vowel-length
  marking will be re-verified from print during the SC087
  adjudication before any scientific use.

## 5. Materially changed backlog items

- 331.6a is a genuine *input-value* rival to SC005 (rounded *o* vs
  CAPR *a* before nasal), not an unconditioned final-m change; the
  early-vowel research item (SC005/SC015/SC017) must include it.
- 404c (final R-loss after unaccented vowel) is a rival *accentual*
  conditioning account relevant to the z-loss family
  (SC020/SC096/SC097/SC098), not a duplicate of 404b.
- 404d (Rn → nn) is explicitly "very sporadic" in Barrack and is
  classified `HISTORICALLY_DOUBTFUL`; it is not a missing CAPR law.
