# R9: Revised matched stacks and wider firing census

**Source correction.** The short ‘flock’ probe is conditional, not the
published reconstruction ([Q1a](../hiatus-cycle4/FLOCK_QUANTITY.md)).
The [Q1b replay](../hiatus-cycle4/H_LOSS_QUANTITY.md) supersedes the
source interpretation of the original ‘receive’, ‘cover’ and ‘rug’
entries; the R9 receipt records their originally supplied inputs.

## Identity and controls

The run uses `113101ac5f169b589e1a9647cdf24d32cdd4d919`, the frozen canonical/A/B2 orders and the [R8 freeze](ENVIRONMENTS.md) at `23c9621a`. `revised-traces.json.gz` contains the exact orders, input strings, entry points, placements, definitions, changing stages and before/after anchors. The full-panel entries do not silently substitute protected or later local forms for failed early inputs.

The common stack retains the S1 `StFoot` form of the weak contraction, early back-vowel incorporation, `HwMed`, the prior shared post-loss treatments, and separate experimental broken-front and marked-identical treatments. It does not resolve short unlike front hiatus. The original frozen stage deletes a plain *e* in the tested prefixed root, whereas S1 leaves it and still reduces a genuinely weak sequence. Both leave the exact unprefixed local ‘strew’ input syllabically separate. [The corrected R4 replay](CHRONOLOGY.md) explains why an earlier report of automatic atomization was spurious. The extended back-vowel changes run as independent adverse probes, not as conditions that differentiate the front arms.

| Arm | Matched change |
|---|---|
| Late D/J/N | Apply in the same post-*h*-loss window, before the same stage, and only before *d, þ/ð, n*. |
| Two-window D/J/N | Apply also immediately after HVD, before the prefixed root loses its foot marker. Retain the same later window for newly created post-*h*-loss inputs. |
| Late D/J/N with edge | Add a separate absolute-edge operation to the late medial arm. No first-member or prevocalic extension is licensed. The late full pipeline rejects the synthetic `*⊕` member marker at the weak-contraction stage; that is an admission limit, not a negative historical firing. R1's isolated, explicitly marked first-member and prevocalic controls remain distinct. |

D coalesces directly. J makes a consonantal *j* with a temporary provenance marker consumed by the next step. N makes `*ėi` or acute `*éi`; its second step cannot consume an older `*ei`. The marker is bookkeeping, not a reconstruction of another phoneme. It does not survive beyond the adjacent matched pair, so this run does not demonstrate long-term survival of a marked consonant or nucleus through intermediate rules. The N edge arm records private nuclear formation before converting to the available display token; both hiatus and a nucleus can render ⟨ei⟩. Independent old *j*, secondary *ʝ*, old atomic *ei*, weak material and explicit accent are all checked. Serial timing between nonadjacent first and second steps is covered by corrected R4 and the private weight controls in R2; these are not silently assumed to be equivalent to the late adjacent pairs.

## Local results

- **Independent later matches:** In all three orders, common yields *sēon*, preserves five exercised initial-*hw* outputs, and gives *fēo* in the reconstructed dative. Under any of the nine matched arms, local short-final ‘flock’ gives *ēde* and raised ‘strike’ *slēþ*. Local ‘couch’ gives *strēne*; the full history does so in A/B2, but not canonical, which has a different earlier vocalism. All arms retain both key controls.
- **Timing:** The strictly late arms miss the plain prefixed ‘call’ root after loss of the foot marker; the two-window arms reach it in the local probe and in full A/B2, with no change to the canonical full long/broken input. This is a distinction between executable placement and the available stress representation, not independent evidence that ‘call’ had to resolve before *h*-loss.
- **Adverse ‘strew’:** On the same short input, all arms with nonfinal resolution change local *streide* to *strēde* in all three orders and the full A/B2 participle from *streid* to *strēd*. Canonical has *strēad* without the same precursor. These outcomes conflict with the preferred two-position scansion if it preserves historical hiatus; alternatively the glossary spellings may represent a different lexeme and the verse may preserve an older performance option.
- **Independent out-of-domain examples:** ‘Higher’ and ‘nearest’ resolve from long nuclei without licensing short *e.i* before *r/s*. ‘Receive’ stays *fæiþ* rather than the normalized long vowel, ‘rug’ retains the front spelling *rye* but the back probe ends *ryan* rather than *rēon*, and the later-entered ‘cow’ probe yields *cū* rather than *cȳ*. None is silently turned into a successful test of *e.i*. All retain their distinct vowels and historical evidence grades. The early written ‘fringe’ intermediate corresponds to *wlōum*, not an unattested contracted endpoint.
- **Edge:** When there is genuinely short *e.i* (full A and the conditional local history in every order), common and medial arms leave *he.i*; D edge gives *hē*, J edge *heġ* and N edge a short nuclear projection spelled *hei*. Canonical and B2 full histories supply no such precursor. For the conditional short ‘river’ oblique, D edge yields *ē* and J edge *eġ*, while the N edge remains an atomic *ei* with the same rendering as common hiatus. This is adverse to uniform edge J if the short inherited ‘river’ input is correct. The tested shared arms do not independently lengthen the short nucleus and then restore a palatal.

## Wider census

Each order replays all 394 archived and 396 active identities, with the original frozen surface outputs verified, and 231 additional panel traces per arm. The original benchmark and new frozen panel retain five written-only entries between them; the receipt names them rather than scoring them. Archived and active rows with a shared lexical identity are separate records, not independent historical witnesses.

| Arm or probe | Difference in the 790-row panels |
|---|---|
| Common vs. frozen | Four internal-only records in each order (archived and active 2019 and 2195, shared `HLBroken`), no surface changes. |
| Medial-only D/J/N vs. common | No added corpus changes, at either timing. The experimental local witnesses do change; the wide panel is sparse in genuinely matched inputs. |
| Edge D/J/N vs. common | Canonical and B2: none. A: D and J each change the two `2061` rows from *hei* to *hē/heġ* respectively. N changes the internal nucleus in the same two records with no surface difference. These records duplicate one lexical identity: ‘hay’, not an independent positive. |
| Back-realization probe vs. common | Four surface changes in each model: the archived and active copies of 2033 and 2326 yield *frīond* and *īow* for *frēond* and *ēow*. The realization of local ‘three’ as *þrīo* does not justify this indiscriminate `*iu` change. |
| Transient back-bridge probe vs. common | 32 internal-only records per order, plus 12 surface changes (canonical/B2) or 10 (A). The bridge also turns established earlier *æu* paths into long *ēa*; canonical/B2 ‘hay’ becomes *hēaġ* instead of *hīeġ*, and other fronted outputs change. The bridge is a useful token diagnosis, not a general repair. |

## Replay

```sh
set -o pipefail
cycle=Germanic/articles/hay/research/hiatus-cycle3
bash "$cycle/run-container.sh" --revised --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 | cmp "$cycle/revised-traces.json.gz" -
```
