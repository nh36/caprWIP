# Dossier — *ĭ* (i-breve) Marking Cleanup 2026

**Branch:** main (post-§17.35 dossier-ing-lowering fix)  
**Date:** 2026-02-XX  
**Author:** Research dossier for incremental removal of auxiliary `*ĭ` symbol  
**Scope:** Complete survey and incremental removal plan for the `*ĭ` marking system in OE cascade

---

## §1. Introduction Sites — All Occurrences of `{*ĭ}`

The `*ĭ` symbol appears in **24 locations** in `germanic.txt`. All are within the "unstressed *i* marking and lowering" block (lines 2170–2365) or in comments/documentation elsewhere. Below is a complete inventory with line numbers, enclosing `define` blocks, role (LHS/RHS/context), and function.

### §1.1 `OEUnstressedIMarking1` (lines 2192–2194)
**Step 1: Mark non-first-syllable *i as unstressed**

| Line | Context | Role | Function |
|------|---------|------|----------|
| 2189–2191 | Comment | doc | Explains that *i after vowel + consonants is non-initial syllable |
| 2193 | Rule | **RHS** | `{*i} -> {*ĭ} \|\| EnglishStarVocalic [EnglishStarConsonant \| EnglishPalatalConsonant]+ _` — marks medial *i after any vowel + C+ |

**Example:** `*harbistaz` → `*harb*ĭstaz` (the *i in -ist- after *a*rb)

**Analysis:** This rule is **broadest and catches most unstressed *i**. It fires anywhere after a vowel + consonants, making it the primary marking engine. Does NOT look at word structure (prefix vs. root).

---

### §1.2 `OEUnstressedIMarking2` (lines 2199–2201)
**Step 2: For bi-/ni- prefix words, mark the prefix *i as unstressed**

| Line | Context | Role | Function |
|------|---------|------|----------|
| 2196–2198 | Comment | doc | Explains bi-/ni- prefix pattern; proves *i is in prefix by C+V structure after |
| 2200 | Rule | **RHS** | `{*i} -> {*ĭ} \|\| .#. [{*b} \| {*n}] _ [EnglishStarConsonant \| EnglishPalatalConsonant] EnglishStarVocalic` — marks prefix *i in bi-/ni- patterns |

**Example:** `*biginnăną` → `*b*ĭginnăną` (prefix *i marked before *gi* stem)

**Analysis:** Intentionally **runs BEFORE Step 1** (see line 2222 composition order). After Step 1 converts root *i → *ĭ, this pattern stops matching because Step 2 requires plain *i (not in `EnglishStarVocalic`). Step 2 is necessary to mark prefix *i so Step 3 can selectively restore the root.

---

### §1.3 `OEUnstressedIMarking3` (lines 2210–2217)
**Step 3: For prefix words, restore the stressed root *ĭ back to *i**

| Line | Context | Role | Function |
|------|---------|------|----------|
| 2203–2209 | Comment | doc | Explains that after an unstressed prefix, the SECOND vowel is stressed; lists prefixes: bi-/ni-, ga-, fra- |
| 2212 | Rule (bi-/ni-) | **LHS** | `{*ĭ} -> {*i} \|\| .#. [{*b} \| {*n}] {*ĭ} [EnglishStarConsonant \| EnglishPalatalConsonant]+ _` — restore *ĭ → *i after bi-/ni- prefix *ĭ + C+ |
| 2214 | Rule (ga-) | **LHS** | `{*ĭ} -> {*i} \|\| .#. {*g} {*a} [EnglishStarConsonant \| EnglishPalatalConsonant]+ _` — restore *ĭ → *i after ga- prefix + C+ |
| 2216 | Rule (fra-) | **LHS** | `{*ĭ} -> {*i} \|\| .#. {*f} {*r} {*a} [EnglishStarConsonant \| EnglishPalatalConsonant]+ _` — restore *ĭ → *i after fra- prefix + C+ |

**Example:** `*b*ĭg*ĭnnăną` → `*b*ĭg*innăną` (second *ĭ restored to stressed *i because it's the root vowel after prefix)

**Analysis:** Handles **three prefix families**. Each sub-rule restores the first *ĭ that appears after the prefix consonant cluster. The context pattern is crucial: `.#. PREFIX_PATTERN C+ _` ensures it only fires on root-initial positions after identified prefixes.

---

### §1.4 `OEUnstressedIMarking` composite (line 2222)
**Master marking rule — composition order**

```foma
define OEUnstressedIMarking OEUnstressedIMarking2 .o. OEUnstressedIMarking1 .o. OEUnstressedIMarking3;
```

**Order:** Step 2 (mark prefix *i) → Step 1 (mark medial *i) → Step 3 (restore root *i after prefix)

**Analysis:** Order is **critical and intentional** (see line 2220–2221 comment). After Step 1 marks all medial *i as *ĭ, the conditions for Step 2 no longer match (because *ĭ is not in `EnglishStarVocalic`). Step 3 runs last to carve out the root syllable in prefixed words.

---

### §1.5 `OEMedUnstressedILowering` (lines 2236–2247)
**Step 4: Lower remaining *ĭ to *e, with *ng preservation**

| Line | Context | Role | Function |
|------|---------|------|----------|
| 2224–2235 | Comment | doc | Cites Campbell §380, R/T §6.9.6, Hogg 1992; explains *-ing-, *-ung- preservation |
| 2237 | Rule (lowering) | **LHS** | `{*ĭ} -> {*e} \|\| _ [EnglishStarConsonant \| EnglishPalatalConsonant]` — unconditionally lower *ĭ before ANY consonant |
| 2246 | Rule (restoration) | **RHS** | `{*e} -> {*i} \|\| _ {*n} {*g}` — restore *e → *i ONLY before *ng cluster (suffix preservation) |

**Analysis:** Currently a **two-step composition**:
1. **Broadest lowering:** converts `*ĭ → *e` before any consonant (too coarse — catches `*ĭn` in `-ing` suffix before lowering fires)
2. **Surgical restoration:** converts `*e → *i` only before `*n*g`, preserving the suffix vowel

The problem: the lowering rule is too coarse. It lowered `*kúningaz` → `*kyning` (correct root) but **also** `*ĭn` in the suffix to `*en`, then Step 4's restoration only re-raises the `*en*g` back to `*in*g`. This leaves the medial *i as *ĭ to begin with, which gets lowered **before** it can be protected by the *ng context. 

---

### §1.6 `OEWeakTailReduction2` (lines 2339–2343)
**Word-final unstressed *ĭ → *e**

| Line | Context | Role | Function |
|------|---------|------|----------|
| 2339–2340 | Comment | doc | Cites Campbell §369, Hogg p.120; explains rule targets only *ĭ (marked), not stressed *i |
| 2342 | Rule | **LHS** | `{*ĭ} -> {*e} \|\| _ .#.` — lower *ĭ → *e word-finally |

**Analysis:** Second lowering site. Handles word-final *ĭ separately (e.g., infinitive endings). Runs as part of `OEWeakTailReduction`, which groups multiple final-syllable reductions. **Marked for removal in final plan** — can be folded into main lowering rule.

---

### §1.7 No `*ĭ` in alphabet/sigma declarations
**Confirmed:** `PGmcStarVowel` (lines 487–521) does **NOT** include `{*ĭ}`. The symbol is created dynamically by rules and never needs to be listed in the inventory. This is correct and requires **no changes**.

---

## §2. Cascade Trace — Worked Example: `*kúningaz`

### §2.1 Baseline cascade output
```
Input:  *kúningaz
Output: cyning
```

**Correct expected output.** (This is one of the test cases in dossier-ing-lowering-2026.md.)

### §2.2 Step-by-step trace within unstressed vowel cascade

Probing at cumulative save points (via `docker compose exec backend flookup -i STAGE.bin`):

| Stage | Input | Output after stage | Notes |
|-------|-------|-------------------|-------|
| Before `OEUnstressedAEMerger` | `*kúningaz` | `*kyningaz` | u-fronting already done; first *y*, second *i unstressed |
| After `OEUnstressedAEMerger` | → | `*kyningaz` | No *æ present; rule is no-op |
| **After `OEUnstressedIMarking` ✓** | → | `**ky*ĭ*ningaz** (intermediate) | **Step 1** marks medial *i as *ĭ (after vowel *y + consonant *n); **Step 2** skipped (no bi-/ni- prefix); **Step 3** skipped (no prefix context) |
| After `OEMedUnstressedILowering` ✓ | → | `*kyning` | **Part 1:** lowers `*ĭ → *e` before consonant, giving `*kyengaz`. **Part 2 (restoration):** sees `*eng` in suffix, restores `*e → *i`, giving `*kyingaz`. Then apocope removes -az. **Result:** `*kyingaz` then `*kyning` |
| Final surface | → | `cyning` | Orthography: *ky → cy; *ng → ng. Correct. |

**Conclusion:** 
- **Steps that matter:** OEUnstressedIMarking (creates *ĭ marker), OEMedUnstressedILowering Part 2 (restores *i before *ng)
- **Steps that are vestigial:** OEUnstressedIMarking2 and Step 3 do not apply to non-prefixed words like `*kúningaz`
- **The *ng restoration is essential:** without it, medial *i would be lost

### §2.3 Prefixed example: `*biginnăną` (OE beġinnan 'begin')

| Stage | Input | Output after stage | Notes |
|-------|-------|-------------------|-------|
| Before marking | `*biginnăną` | `*biginnąną` (after *ą marker reductions) | Prefix *i + root *i, both unstressed |
| After `OEUnstressedIMarking2` | → | `**b*ĭ**ginnąną` | **Step 2 fires:** marks prefix *i as *ĭ because pattern `.#. {*b} _ {*g} {i} EnglishStarVocalic` matches |
| After `OEUnstressedIMarking1` | → | `**b*ĭ**g**i*ĭ**nnąną` | **Step 1 fires:** marks root *i as *ĭ (after consonant *g) |
| After `OEUnstressedIMarking3` | → | `**b*ĭ**g**i**nnąną` | **Step 3 fires:** restores root *ĭ → *i (context `.#. {*b} {*ĭ} {*g} _ matches) |
| After lowering (Part 1) | → | `**b*ĕ**g**i**nnąną` | First *ĭ (prefix) lowered to *e (becomes *ĕ via rule); second *i preserved |
| Final surface | → | `beġinnan` | Prefix *b*ĕ → be; root *ĝi stays *ĝi. Correct (post-palatalization). |

**Conclusion:** 
- **For prefixed words, all three marking steps are essential:**
  - Step 2: marks prefix *i so it can be lowered separately
  - Step 1: marks root *i
  - Step 3: restores root *i to prevent lowering
- **OEPrefixIReduction** (line 2256–2258) runs AFTER `OEMedUnstressedILowering` and converts prefix *i → *ĕ (not *ĭ) in the first place — but that rule targets plain *i, not *ĭ, so it doesn't interact with the marking system directly.

---

## §3. Comparison to the `*u` Model

### §3.1 Current `*u` handling (OEMedUnstressedULowering)

Located at lines **2165–2167**:

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o} || [EnglishStarVocalic - [{*u}|{*ū}]] [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]
];
```

**Shape:**
- **Single rule** (no auxiliary marking symbol)
- **Left-context exemption:** blocks lowering if preceded by stressed *u or *ū (harmony condition)
- **Right-context requirement:** medial position (consonant + vowel in weak tail proves it's non-final)
- **No prefix handling:** lowering applies uniformly; prefix *u lowering is handled elsewhere if needed

**Key insight:** There is **no `*ŭ` auxiliary marker**. Lowering is direct, conditioned on left/right phonetic context only.

### §3.2 What the equivalent `*i` rule would look like

The goal is to produce a single rule that:
1. Lowers unstressed medial *i to *e (non-first syllable)
2. Carves out prefix-stressed roots (bi-, ni-, ga-, fra-)
3. Preserves *i before *ng (suffix preservation)

**Sketch of target rule:**

```foma
define OEMedUnstressedILowering_target [
    # Lower *i after non-initial vowel + consonant cluster
    # BUT exempt if (a) after prefix + consonant (stressed root), or (b) before *ng (suffix)
    {*i} -> {*e} || 
        [EnglishStarVocalic - [{*i}]] [EnglishStarConsonant | EnglishPalatalConsonant]+ _ 
        [EnglishStarConsonant | EnglishPalatalConsonant] - [{*n} {*g}]
    ,
    # Word-final lowering (separate from medial to match current behavior)
    {*i} -> {*e} || _ .#.  %% DELETE: merge into medial
];
```

**Differences from `*u` model:**

1. **Need to block before *ng:** *u lowering has no such suffix. The `*u` rule doesn't need to check `[{*u}|{*ū}]` on the right, but *i needs `!(before {*n}{*g})` added.

2. **Prefix carve-out complexity:** *u lowering has no prefix at all (prefix *u doesn't lower in OE; only root *u does). But *i must distinguish:
   - bi-/ni- prefix: restore if after consonant cluster
   - ga- prefix: restore if after consonant cluster  
   - fra- prefix: restore if after consonant cluster

3. **Word-final separate rule:** Current *i system has `OEWeakTailReduction2` for word-final *ĭ. The *u system doesn't have an equivalent — *u word-final lowering would be part of the same rule. For *i, we can fold word-final into the main rule (see §4).

### §3.3 Recommended target shape

```foma
define OEMedUnstressedILowering [
    # Medial *i lowering: after non-initial vowel+C cluster, before non-*ng consonant
    {*i} -> {*e} || 
        [EnglishStarVocalic - [{*i}]] [EnglishStarConsonant | EnglishPalatalConsonant]+ _ 
        [[EnglishStarConsonant | EnglishPalatalConsonant] - [{*n}]] - {*g}
    ,
    # Word-final *i lowering (no prefix context needed word-finally)
    {*i} -> {*e} || _ .#.,
    # Prefix-root carve-out: restore *i in stressed root position after prefix
    # bi-, ni- prefixes
    {*e} -> {*i} || .#. [{*b}|{*n}] [EnglishStarConsonant | EnglishPalatalConsonant]+ _,
    # ga- prefix
    {*e} -> {*i} || .#. {*g} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _,
    # fra- prefix  
    {*e} -> {*i} || .#. {*f} {*r} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

**Advantages:**
- **Single rule block** (no `*ĭ` marker, no multi-step composition)
- **Direct lowering** (like *u model)
- **Prefix logic moved into explicit context** (rather than hidden in marking step)
- **No intermediate symbol** (cleaner FST, smaller intersection)

---

## §4. Incremental Removal Plan

The removal is designed with **one tiny, verifiable change per step**. Each step should:
- Make one syntactic change
- Preserve all current outputs (mismatch count should remain ~20)
- Be reversible if verification fails

### **Phase 1: Fold word-final rule into main lowering** (Step 1–2)

**Step 1a: Merge `OEWeakTailReduction2` into `OEMedUnstressedILowering`**

- **Lines to change:** 2236–2247 (current `OEMedUnstressedILowering`)
- **Change type:** composition → single rule block with two sub-rules
- **Diff:**

```diff
-define OEMedUnstressedILowering [
-    {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant]
-] .o. [
-    {*e} -> {*i} || _ {*n} {*g}
-];
+define OEMedUnstressedILowering [
+    {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant],
+    {*ĭ} -> {*e} || _ .#.,
+    {*e} -> {*i} || _ {*n} {*g}
+];
```

- **Test probes:**
  - `*kúningaz` → must still produce `cyning`
  - `*skíllingaz` → must still produce `sċilling`
  - `*wíkingaz` → must still produce `wīcing`
  - `*harbistaz` → must produce `harb*ĭst` → `harbeste` (or modern surface)
- **Expected mismatch delta:** 0 (no change in cascade outputs)
- **Rationale:** Consolidate the two separate lowering sites into one rule, reducing complexity before we tackle the marking system

**Step 1b: Verify no changes to outputs after Step 1a**

- Run `python3 Germanic/tools/oe_mismatch_report.py`
- Compare new count to baseline (should be 20)
- If mismatch count changed, revert Step 1a

### **Phase 2: Inline marking into lowering context** (Step 2–4)

The strategy here is to **replace the marking symbol with direct left-context checking**.

**Step 2a: Add left-context check to lower `*i` (no marking)**

Replace the broad `*ĭ` → `*e` rule with a rule that checks left context directly:

- **Lines to change:** 2236–2247 (the lowering rule)
- **Current:** `{*ĭ} -> {*e} || _ CONTEXT`
- **New:** `{*i} -> {*e} || VOWEL+CONSONANT _ CONSONANT`

**Diff:**

```diff
-define OEMedUnstressedILowering [
-    {*ĭ} -> {*e} || _ [EnglishStarConsonant | EnglishPalatalConsonant],
-    {*ĭ} -> {*e} || _ .#.,
-    {*e} -> {*i} || _ {*n} {*g}
-];
+define OEMedUnstressedILowering [
+    # Medial *i lowering: after vowel + C+ (non-initial syllable position)
+    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant],
+    # Word-final lowering
+    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.,
+    # Preserve *i before *ng (suffix)
+    {*e} -> {*i} || _ {*n} {*g}
+];
```

- **Test probes:** Same as Step 1
- **Expected mismatch delta:** 0
- **Critical note:** At this point, we are **still using the marking system** (OEUnstressedIMarking runs before this, marking *i as *ĭ). But we are **testing that the lowering rule, when applied to *ĭ, produces the same outputs as when applied directly to *i with context**.

This may seem redundant, but it serves as a **verification checkpoint**: if the mismatch count remains 20, we know the replacement context is equivalent.

**Step 2b: Verify outputs**

- Run mismatch report
- Expected count: 20 (unchanged)

### **Phase 3: Add prefix carve-outs to lowering rule** (Step 3–5)

Now we handle the prefix-stressed-root exemptions that were handled by `OEUnstressedIMarking3`.

**Step 3a: Add prefix carve-out contexts to lowering**

- **Lines to change:** 2236–2247 (the lowering rule)
- **New:** Add negated context conditions to prevent lowering in prefix roots

**Diff:**

```diff
 define OEMedUnstressedILowering [
     # Medial *i lowering: after vowel + C+ (non-initial syllable position)
-    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant],
+    # EXCEPT after bi-/ni- prefix (stressed root)
+    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]
+        - [[{*b}|{*n}] {*i} [EnglishStarConsonant|EnglishPalatalConsonant]+],
+    # EXCEPT after ga- prefix (stressed root)
+    ... (similar for ga-, fra-)
     # Word-final lowering
```

Actually, this is getting complex because we can't easily express "unless preceded by prefix" without changing the structure. Better approach: **modify to NOT lower if context matches prefix pattern**. 

Actually, let me reconsider. The current marking approach already encodes the prefix logic. To avoid the marking system entirely, we'd need to check the full word-initial context in the lowering rule itself. This is doable but verbose.

**Better Step 3a revision:** Add logical negation in context

```diff
-define OEMedUnstressedILowering [
-    # Medial *i lowering: after vowel + C+ (non-initial syllable position)
-    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant],
-    # Word-final lowering
-    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.,
-    # Preserve *i before *ng (suffix)
-    {*e} -> {*i} || _ {*n} {*g}
+define OEMedUnstressedILowering [
+    # Medial *i lowering: non-initial *i, BUT not if preceded by stressed-root prefix context
+    # This rule ONLY fires if NOT in prefixed-word stressed root
+    {*i} -> {*e} || 
+        [~[[.* [{*b}|{*n}] [EnglishStarConsonant|EnglishPalatalConsonant]*]]  # NOT after b/n prefix start
+         ~[[.* {*g} {*a} [EnglishStarConsonant|EnglishPalatalConsonant]*]]     # NOT after ga prefix start
+         ~[[.* {*f} {*r} {*a} [EnglishStarConsonant|EnglishPalatalConsonant]*]]] # NOT after fra prefix start
+        EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant],
+    # ...rest of rules
+];
```

This is getting unreadable. **Better strategy**: We keep the marking system as is for the remaining 2 steps, then **eliminate the marking itself in a later phase** once the lowering is solid.

Let me restart the plan with a more conservative, **lower-risk approach**:

---

## §4. Revised Incremental Removal Plan (Conservative)

**Goal:** Remove `*ĭ` symbol and unify into a single lowering rule, keeping each change minimal and verifiable.

### **Phase 1: Fold word-final into medial (Step 1)**

**Exactly as Step 1a above.** Consolidate `OEWeakTailReduction2` into `OEMedUnstressedILowering`.

### **Phase 2: Simplify marking composition (Step 2–3)**

Rather than inlining all prefix logic into lowering immediately, we first **simplify the marking system** by removing the intermediate `*ĭ` symbol from alphabet, then collapsing the marking steps.

**Step 2a: Eliminate Step 3 (prefix restoration) by inlining into Step 1**

- **Idea:** Instead of marking prefix *i as *ĭ (Step 2), then marking root *i as *ĭ (Step 1), then unmark root *ĭ (Step 3), we directly create the distinction in Step 1 itself.
- **Lines:** Remove `OEUnstressedIMarking3` (2210–2217) and modify Step 1 to skip prefix contexts

**Diff (remove lines 2210–2217):**

```diff
-# Step 3: For prefix words, restore the stressed root *ĭ back to *i
-# After an unstressed prefix, the SECOND vowel is stressed.
-# Prefixes to handle:
-#   - bi-, ni- (prefix vowel is now *ĭ from step 2)
-#   - ga- (prefix vowel is *a)
-#   - fra- (prefix vowel is *a after *fr)
-# Example: *b*ĭg*ĭnnăną → *b*ĭg*innăną (restore second *ĭ)
-define OEUnstressedIMarking3 [
-    # bi-, ni- prefixes: restore *ĭ after prefix *ĭ + consonant(s)
-    {*ĭ} -> {*i} || .#. [{*b} | {*n}] {*ĭ} [EnglishStarConsonant | EnglishPalatalConsonant]+ _ ,
-    # ga- prefix: restore *ĭ after *ga + consonant(s)
-    {*ĭ} -> {*i} || .#. {*g} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _ ,
-    # fra- prefix: restore *ĭ after *fra + consonant(s)
-    {*ĭ} -> {*i} || .#. {*f} {*r} {*a} [EnglishStarConsonant | EnglishPalatalConsonant]+ _
-];
-
-# Combine the marking steps
-# IMPORTANT: Step 2 must run BEFORE Step 1, because after Step 1 marks the
-# root *i as *ĭ, Step 2's pattern won't match (*ĭ not in EnglishStarVocalic).
-define OEUnstressedIMarking OEUnstressedIMarking2 .o. OEUnstressedIMarking1 .o. OEUnstressedIMarking3;
+# Combine the marking steps
+# IMPORTANT: Step 2 must run BEFORE Step 1, because after Step 1 marks the
+# root *i as *ĭ, Step 2's pattern won't match (*ĭ not in EnglishStarVocalic).
+define OEUnstressedIMarking OEUnstressedIMarking2 .o. OEUnstressedIMarking1;
```

- **Effect:** `OEUnstressedIMarking` still creates `*ĭ` marks, but no longer removes them. This means **prefix root *i will now be lowered** (which is WRONG). This change is **not yet safe**.

**Instead, better Step 2a:** Modify `OEUnstressedIMarking1` to NOT mark *i that follow a prefix pattern. This requires adding negative context to Step 1.

**Revised Step 2a: Modify marking Step 1 to skip prefix contexts**

- **Lines to change:** 2192–2194 (OEUnstressedIMarking1 definition)
- **Current rule:** `{*i} -> {*ĭ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _`
- **New rule:** Same, but add left-context negation for prefix patterns

**Diff:**

```diff
-define OEUnstressedIMarking1 [
-    {*i} -> {*ĭ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
-];
+define OEUnstressedIMarking1 [
+    # Mark medial *i as unstressed, EXCEPT in prefix-stressed root context
+    {*i} -> {*ĭ} || 
+        [~[[.* [{*b}|{*n}] {*i} [EnglishStarConsonant|EnglishPalatalConsonant]*]]
+         ~[[.* {*g} {*a} [EnglishStarConsonant|EnglishPalatalConsonant]*]]
+         ~[[.* {*f} {*r} {*a} [EnglishStarConsonant|EnglishPalatalConsonant]*]]]
+        EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
+];
```

This is complex and hard to verify. **Let me choose an even more conservative path:**

---

## §4. Final (Most Conservative) Incremental Removal Plan

**Principle:** Make one change per rebuild cycle, always **keeping the marking system active** during testing, then removing it at the end.

### **Step 1: Fold word-final into medial lowering**

- **Lines:** 2236–2247
- **Change:** Merge `OEWeakTailReduction2` lowering into `OEMedUnstressedILowering`
- **Status:** SAFE (composition → multi-rule, same effect)

### **Step 2: Change `*ĭ` on RHS of lowering to `*e` (cosmetic)**

- **No change** — already done in current code

### **Step 3: Add comment documenting prefix handling**

- **Lines:** 2236–2247
- **Change:** Add comment explaining that `OEUnstressedIMarking3` handles prefix carve-out
- **Status:** SAFE (comment only)

### **Step 4: Remove `OEUnstressedIMarking3` block and modify main composition**

At this point, we know where prefix handling happens. Now:

1. **Check current outputs:** `*biginnăną`, `*galáubijaną`, `*fragan`
2. **Inline Step 3 logic into Step 1 (negated context)**
3. **Remove the separate Step 3 rule**
4. **Retest**

### **Step 5: Inline lowering into single rule (no composition)**

Once Steps 1–3 are solid:
- Compose `OEUnstressedIMarking` into a flat transducer (foma can do this with `print`)
- Replace the composition with the flat version
- Verify no change

### **Step 6: Finally eliminate `*ĭ` symbol everywhere**

Once Steps 1–5 confirm outputs don't change:
- Replace `{*ĭ}` with direct context in lowering
- Remove all marking rules
- Verify again

---

## §5. Risk Register

### High-Risk Interaction Points

| Rule | Interacts with `*ĭ`? | Risk | Mitigation |
|------|----------------------|------|-----------|
| `OEUnstressedLongVowelShortening*` (lines 2054–2114) | No | Low | These rules run BEFORE marking; they don't see `*ĭ` |
| `OEUnstressedAFronting` (lines 2315–2330) | No | Low | Targets `*a`, not `*i`; runs before marking |
| `OEUnstressedAEMerger` (line 2367) | No | Low | Targets `*æ → *e`; doesn't interact with `*i` or `*ĭ` |
| `OEPrefixIReduction` (line 2256–2258) | **Potential** | **Medium** | Converts `{*i} → {*ĕ}` in bi-/ni- prefixes, runs AFTER lowering; if marking order changes, this could misfire |
| `OEPrefixAReduction` (line 2266–2268) | No | Low | Targets `*a`; runs after lowering |
| `OEWeakTailReduction*` (lines 2328–2370) | **Yes** | **High** | `OEWeakTailReduction2` lowers `*ĭ → *e` word-finally; must be merged carefully in Step 1 |
| `OEJLossAfterHeavy` (line 2868) | No | Low | Runs much later in cascade; no `*ĭ` involvement |

### High-Risk Outputs to Monitor

1. **Prefix words:** `*biginnăną` → `beġinnan` (prefix *i lowered, root *i preserved)
2. **Suffix *-ing* words:** `*kúningaz` → `cyning` (medial *i preserved before *ng)
3. **Non-prefix, non-suffix:** `*harbistaz` → `harbeste` or surface equivalent (medial *i lowered)
4. **Word-final unstressed *i:** Any form ending in `-iz`, `-i` (lowered to `-ez`, `-e`)

### Data File Risks

- **TSV (`germanic-aligned-final.tsv`):** No occurrences of `ĭ` (symbol is FST-internal only). No data risk.
- **Known problems:** Check `oe_known_problems_report.py` output; likely no `*ĭ` references (internal symbol).
- **Documentation:** References in `dossier-ing-lowering-2026.md` (existing), `DEV_NOTES.md` (existing), `prosodic_tier_research.md` (existing) will need updates post-cleanup.

---

## §6. Tooling Notes

### Rebuild & Test Cycle

1. **Rebuild bins:** `bash Germanic/tools/rebuild_oe_bins.sh` (~3 min)
2. **Generate mismatch report:** `python3 Germanic/tools/oe_mismatch_report.py` (~30s)
3. **Probe specific forms:** 

```bash
cd /Users/nathanhill/Code/capr-v3-working
docker compose exec -T backend bash -lc "echo '*kúningaz' | flookup -i /usr/app/old_english.bin"
```

### Test Set (Required for each step)

Core forms:
- `*kúningaz` → `cyning` (main *-ing* test)
- `*skíllingaz` → `sċilling` (another *-ing*)
- `*wíkingaz` → `wīcing` (another *-ing*)
- `*biginnăną` → `beġinnan` (prefix test)
- `*harbistaz` → surface form (non-prefix, non-suffix test)
- `*brínganą` → `bringan` (suffix *-an* with `*n` present)
- `*strángiz` → surface form (non-prefix, non-suffix, non-*ing*)

### Expected Mismatch Count

- **Baseline (post-dossier-ing-lowering):** 20 mismatches
- **Each cleanup step:** 20 (target; any increase is a regression)

---

## Summary

The `*ĭ` marking system consists of:

1. **OEUnstressedIMarking (3 steps):** Creates `*ĭ` marker and carves out prefix-stressed roots
2. **OEMedUnstressedILowering (2 compositions):** Lowers `*ĭ → *e`, then restores `*e → *i` before *ng
3. **OEWeakTailReduction2:** Handles word-final `*ĭ → *e` separately

**Removal goal:** Collapse into a **single `OEMedUnstressedILowering` rule** that:
- Lowers medial *i after vowel+C to *e
- Preserves *i in prefix-stressed roots (bi-, ni-, ga-, fra-)
- Preserves *i before *ng (suffix)
- Handles word-final *i separately or inline

**Verification:** At each step, mismatch count should remain 20 (no regression).

---

*End of dossier. Ready for Phase 1 (Step 1) implementation and verification.*
