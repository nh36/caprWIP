## OE A-restoration debug notes (2026-02-03) - **RESOLVED 2026-02-06**

**STATUS**: A-restoration is now working correctly. The issue was fixed by repairing the rule context (removing outer parentheses that made the context optional). See `DEV_NOTES.md` line 51-59 for fix details.

Purpose: capture what we already learned about OldEnglishARestoration so we don't re-run the same checks.

### Where the rule is
- Definition: `server/fsts/germanic.txt` in the Old English block.
- Key pieces (names as in file):
  - `OldEnglishARestorationIntervening` = single consonant | geminate | sC.
  - `OldEnglishARestorationBackVowel` = {*a, *ā, *o, *ō, *u, *ū, *au, *eu}.
  - `OldEnglishARestorationContext` = Intervening + BackVowel + EnglishStarConsonantSeq.
  - `OldEnglishARestorationWeakTailContext` = Intervening + OldEnglishARestorationWeakTailVowelStar + EnglishStarConsonantSeq.
  - A‑restoration: `{*æ} -> {*a} || _ (Context - WeakTailContext)`.

### Weak‑tail mechanics that matter
- Weak‑tail reduction happens **after** A‑restoration in the stack.
- `OldEnglishWeakTailReduction` maps `*ą -> *ɔ̆` and `*ă -> *a` (among others).
- Because `*ɔ̆` only appears **after** A‑restoration, adding `*ɔ̆` to a weak‑tail exclusion will not affect A‑restoration itself.

### Trace tool is in sync with sandbox bins
- `server/tools/trace_old_english_sandbox.py` traces **sandbox stage bins** (e.g. `old_english_sandbox_after_*.bin`).
- It does **not** feed outputs between stages; each stage runs from the same proto input.
- That means the trace is appropriate for checking whether the **rule exists** and whether its **context** matches the input at that stage.

### Evidence that weak‑tail exclusion is not matching
These were the key probes used in the last round of checks:

```bash
docker compose exec backend sh -lc "cd /usr/app && python3 tools/trace_old_english_sandbox.py --bin-dir /usr/app --lexeme '*b*a*s*t*ą'"
```
- `*b*a*s*t*ą` **does** A‑restore to `*a`, even though `*ą` should be weak‑tail.  
  This indicates `OldEnglishARestorationWeakTailContext` is not matching a weak‑tail shape that should exclude A‑restoration.

```bash
docker compose exec backend sh -lc "cd /usr/app && python3 tools/trace_old_english_sandbox.py --bin-dir /usr/app --lexeme '*n*a*d*r*ō'"
```
- `*n*a*d*r*ō` fronts to `*æ`, then A‑restoration flips it back to `*a` (expected behavior given the back‑vowel trigger).

```bash
docker compose exec backend sh -lc "cd /usr/app && python3 tools/trace_old_english_sandbox.py --bin-dir /usr/app --lexeme '*s*t*ą'"
```
- `*s*t*ą` shows no A‑restoration; weak‑tail reduction later yields `*ɔ̆`.

```bash
docker compose exec backend sh -lc "cd /usr/app && python3 tools/trace_old_english_sandbox.py --bin-dir /usr/app --lexeme '*d*ă*l'"
```
- `*d*ă*l` fails at ProtoInput (`+?`). Use `*d*a*l` for valid testing.

### Literature cross‑check (local)
- Ringe/Taylor (vol. 2, §6.3.1) describes **retraction of *æ** after breaking and **before** later changes, in contexts with
  **single/geminate or sC** followed by a **back vowel**.  
  This aligns with our `OldEnglishARestorationIntervening` + `BackVowel` design.
- Hogg’s volume is less explicit about formal contexts in the scanned sections, but does not contradict this environment.

### Current working hypothesis
- The weak‑tail exclusion is built from an **explicit suffix list** (`EnglishWeakTailVowelStar`) that does not cover all weak‑tail shapes,
  so `OldEnglishARestorationWeakTailContext` fails to match strings like `*b*a*s*t*ą`.
- A more robust exclusion should be **class‑based** (e.g., keyed to `EnglishWeakTailVowel`) or otherwise broadened so the
  A‑restoration context reliably rejects weak‑tail vowels.

### Next step when returning to fixes
1) Confirm that `OldEnglishARestorationContext` matches `*b*æ*s*t*ą` but `OldEnglishARestorationWeakTailContext` does not.  
2) Adjust weak‑tail exclusion to match the intended class, then rerun the same traces.  
3) Only if the traces improve, rerun mismatch + full trace reports.
