# Investigation: *deljăz "dill" — i-stem vs ja-stem

## Current TSV state

- **IDs**: 894 (German), 895 (English), 896 (Dutch), 1990 (Old English)
- **PROTO**: `*deljăz` (all 4 rows)
- **OE target**: `dile`
- **Pipeline result**: `deljăz → dill` (wrong — expected `dile`)
- **Pipeline with i-stem**: `deliz → dile` ✓

## Kroonen's reconstruction (*deli- ~ *delja-)

Kroonen (p. 93, line 7232):

> *deli- ~ *delja- m. 'dill' — OE dile, dyle m. 'id.', E dill, OS dilli m. 'id.', Du. dille c. 'id.', OHG tilli m. 'id.', MHG tille, tülle m. 'id.'
>
> The material offers evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli). Perhaps the forms with rounded vowels (OE dyle, MHG tülle) can be adduced to reconstruct an additional ablauting pair *duli- ~ *dulja-. If so, the original paradigm probably had ablaut of the root, viz. nom. *deliz, gen. *duljaz < *dhél-i-s, *dhl̥-i-ós.

## The linguistic problem

The daughter languages point in two directions:

| Language | Form | Points to | Evidence |
|----------|------|-----------|----------|
| OE | dile | i-stem *deliz | No gemination (WGmc *j-gemination would give **dille*) |
| OS | dilli | ja-stem *deljaz | Gemination before *j |
| OHG | tilli | ja-stem *deljaz | Gemination before *j |
| Du | dille | ja-stem *deljaz | Gemination before *j |
| E | dill | ja-stem *deljaz | Gemination (from OS/Scandinavian?) |

### Scenario 1: Original i-stem, remodeled to ja-stem in continental WGmc

PGmc *deliz (i-stem) → OE dile (regular), but continental languages remodeled to ja-stem *deljaz, causing WGmc gemination → OS dilli, OHG tilli.

The i-stem → ja-stem remodeling is well-known in WGmc. Many originally proterokinetic i-stems were remodeled to ja-stems by extension of the oblique *-j- to the nominative, triggering gemination.

### Scenario 2: Original ja-stem, OE escaped gemination

PGmc *deljaz (ja-stem) → OS dilli, OHG tilli (regular), but OE lost the gemination or was remodeled to an i-stem.

This is less likely because:
- WGmc gemination before *j is one of the most regular sound changes
- There's no known mechanism for "degemination" in OE that would undo it
- If OE had *deljaz, we'd expect **dille*, not dile

### Scenario 3: Kroonen's proterokinetic ablaut

Kroonen suggests an originally ablauting paradigm:
- nom. *deliz (e-grade, i-stem) → OE dile
- gen. *duljaz (zero-grade, ja-stem) → forms with *u and gemination

This is the most sophisticated reconstruction. It explains:
- Why some forms have *e and no gemination (nom.-stem)
- Why some forms have *u and gemination (obl.-stem)
- Why rounded vowels appear in some daughters (OE dyle, MHG tülle < *duljaz)

## User's position

The user is skeptical of two co-existing proto-forms as "not elegant" and wants specialized literature consulted before any change. The user's instinct is that there was likely ONE original stem that was remodeled in some daughters.

Kroonen's proterokinetic analysis actually SUPPORTS a single original paradigm — it's one word with two stem shapes depending on the case form, not two competing words. The daughters then generalized one stem or the other.

## What the pipeline needs

For OE dile, the correct proto form for our pipeline would be `*deliz` (i-stem nom.sg.):
- `deliz → dile` ✓ (tested, works)
- `deljăz → dill` ✗ (current, wrong — ja-stem gives gemination)

The change would be: PROTO `*deljăz` → `*deliz` for the OE row (and possibly all rows).

## Literature to consult (waiting for user)

1. **Kluge, F.** *Etymologisches Wörterbuch der deutschen Sprache*. 24th ed. (2002). s.v. Dill.
   - Will show what stem is reconstructed for the German form
2. **EWAhd** (*Etymologisches Wörterbuch des Althochdeutschen*). s.v. tilli.
   - May have detailed discussion of the stem class question
3. **Krahe, H. & W. Meid.** *Germanische Sprachwissenschaft III: Wortbildungslehre*.
   - General treatment of i-stem / ja-stem interchange in Germanic
4. **Seebold, E.** *Vergleichendes und etymologisches Wörterbuch der germanischen starken Verben*.
   - General reference on Germanic ablaut patterns
5. **Casaretto, A.** *Nominale Wortbildung der gotischen Sprache* (2004).
   - Discussion of proterokinetic i-stems in Germanic

### Key question for the literature
Was i-stem → ja-stem remodeling or ja-stem → i-stem simplification more common in WGmc? If i→ja was the productive direction (as is generally believed), then *deliz (i-stem) is likely original and OE preserves the archaic form.

## Status

**Blocked**: Waiting for user to locate specialized literature. No TSV changes until research is complete.

## References

- Kroonen, Guus. *Etymological Dictionary of Proto-Germanic*. Leiden: Brill, 2013. s.v. *deli- ~ *delja-.
