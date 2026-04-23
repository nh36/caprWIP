# Skill: FST Build and Tokenize

**Invocation:** "fst build and tokenize" (or just "build the FST", "rebuild
bins", "why is this PROTOFORM not tokenising")

This skill exists because a recurring class of self-inflicted slowdown is:
edit a TSV row or grammar fragment, then thrash for half an hour because
(a) the bin wasn't rebuilt, (b) the bin was rebuilt in the wrong place,
(c) `flookup` returns `+?` and the assumption is "phonology bug" when in
fact the input was rejected by `pgrmWord` at the tokeniser, or (d) the
PROTOFORM uses a character (`þ`, `ǣ`, plain `*ą` instead of `*á̧`, …)
that the grammar doesn't list. Read this skill **before** any of:
adding a new PROTOFORM with an unfamiliar shape, editing
`Germanic/fsts/germanic.txt`, debugging a `+?` from `flookup`, or
debugging an `oe_full_trace_report.py` showing `[carry]` everywhere.

Closely related skills:

- `skills/sync-trace-report.md` — when the *tracer* is out of sync with
  the real pipeline (covers the **40-character foma name limit**, do
  not duplicate that here — cross-reference it).
- `skills/be-lautgesetzlich.md` — when the question is *which* PROTOFORM
  to put in the TSV in the first place.

---

## 1. Where the FST actually lives

There are **three** copies of `old_english.bin` on disk and you must
keep them straight:

| path                                  | what it is                                       | who writes it           |
|---------------------------------------|--------------------------------------------------|-------------------------|
| `/usr/app/old_english.bin` (in container) | foma's actual output | `foma -f fsts/germanic.txt`     |
| `backend/old_english.bin` (host repo) | the bin used by the backend service & most tools | `rebuild_oe_bins.sh` syncs it |
| `Germanic/fsts/old_english.bin`       | mirrored copy for in-repo browsing               | `rebuild_oe_bins.sh` syncs it |

`backend/old_english.bin` is the one read by `oe_mismatch_report.py`,
`oe_full_trace_report.py`, the backend HTTP service, and any
`flookup -i backend/old_english.bin` invocation from the host. The
`Germanic/fsts/old_english.bin` copy is for browsing convenience only;
**do not** rely on it being in sync if you didn't run the rebuild
script.

The same pattern applies to the per-stage sandbox bins
(`old_english_sandbox_after_*.bin`) — foma writes them to
`/usr/app/`, the rebuild script syncs to `backend/`, and the tracer
reads from `backend/`.

## 2. The build command

There is exactly one supported way to build:

```bash
bash Germanic/tools/rebuild_oe_bins.sh
```

This:

1. `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/germanic.txt"`
   → builds `old_english.bin` (and a few others) in `/usr/app/`.
2. `docker compose exec backend bash -lc "cd /usr/app && foma -f fsts/old_english_sandbox.txt"`
   → builds the per-stage sandbox bins.
3. `cp /usr/app/old_english.bin /usr/app/fsts/old_english.bin`
4. If `/usr/app/backend/` exists, `cp /usr/app/old_english.bin /usr/app/backend/old_english.bin`.

Takes a few minutes. **Do not** try to build with a host-side `foma`
binary — the container has the exact toolchain the project expects,
and host-side builds will produce inconsistent or unbuildable bins.

**Prerequisite**: Docker containers must be up. Check with
`docker compose ps`; if `backend` is not running, `docker compose up -d`.

**Post-build sanity check** (cribbed from `sync-trace-report.md`):

```bash
bash Germanic/tools/rebuild_oe_bins.sh 2>&1 | tee /tmp/build.log
grep -iE "should consist of at most 40 character" /tmp/build.log   # must be empty
ls -la backend/old_english_sandbox_after_*.bin | awk '{print $5, $NF}' | sort -n | head
```

Sub-200-byte stage bins ⇒ a foma name-limit collapse, see
`sync-trace-report.md`.

## 3. flookup invocation

Apply-down (PGmc → OE):

```bash
echo 'fúnðanǭ' | flookup -i backend/old_english.bin
# fúnðanǭ	fundene
```

Or inside the container:

```bash
docker compose exec -T backend bash -lc 'cd /usr/app && echo "fúnðanǭ" | flookup -i old_english.bin'
```

Notes:

- The `-i` flag is **inverse**, i.e. apply-down (PGmc → OE). Without
  it, `flookup` does apply-up (OE → PGmc).
- The input on the left of the tab is what you fed in; the right is
  the FST output. `+?` = no path through the network = **rejection**,
  not a phonology error (see §5).
- `echo` in modern shells handles UTF-8 fine. If you ever need to feed
  a literal control character or have shell-escaping doubts, use
  `printf '%s\n' '...'` instead.

## 4. Tokenisation: PROTOFORM ↔ FST input

The PROTOFORM column in `Germanic/data/germanic-aligned-final.tsv`
uses the human-readable convention `*xyz` with a leading asterisk and
special characters (`ǭ`, `ð`, `ú`, `θ` etc.). Tools normalise this
before feeding it to `flookup`.

`oe_full_trace_report.py` and `oe_mismatch_report.py` both call
`normalize_proto`:

```python
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")
def normalize_proto(raw: str) -> str:
    normalized = PROTO_STRIP_RE.sub("", raw or "")
    # Proto inventory uses θ; normalize þ to avoid false no_output buckets.
    return normalized.replace("þ", "θ")
```

So:

- Leading `*` is stripped.
- Whitespace, `{}`, `/`, `(`, `)` are stripped.
- `þ` → `θ` (the grammar uses Greek theta, not Latin thorn — easy to
  mix up).

Other gotchas:

- Use precomposed `ą` (U+0105), not `a` + combining ogonek. Same for
  `ǭ`, `ę`, etc. Foma matches by codepoint.
- Acute accents (`ú`, `ó`) similarly must be precomposed.
- Do **not** use `*ă` (a-breve) and `*a` interchangeably — the grammar
  treats them as distinct symbols. The breve historically marked
  unaccented vowels; the project no longer uses two ways of marking
  unaccentedness (see `skills/be-lautgesetzlich.md` §"notational
  redundancy"). Existing `ă` clauses are legacy.

## 5. The `+?` and `[carry]` symptoms — what they mean

| symptom | meaning |
|---------|---------|
| `flookup` returns `INPUT\t+?` | no path through the FST = the input is not in the language of the network. **Almost always a tokenisation problem at `pgrmWord`**, not a phonology bug. |
| `oe_full_trace_report.py` shows `[carry]` at every stage | identical: the input was rejected at ProtoInput (`pgrmWord`), so every downstream stage just carries the literal input through. |
| `[carry]` at *some* stages but not others | a downstream rule failed on a form the previous stage did produce. This *is* a phonology bug — investigate the first stage that carries. |
| `flookup` returns `INPUT\tOUTPUT` where OUTPUT differs from expected | normal phonology debugging. Use `oe_full_trace_report.py` to find the stage where it diverges. |

## 6. `pgrmWord` — the explicit-suffix-list design

`Germanic/fsts/germanic.txt` defines `pgrmWord` (line 469) as
roughly: `pgrmInitSimple pgrmStressedNucleus pgrmCoda pgrmMedial*
pgrmWeakTailVowel`. The crucial component is **`pgrmWeakTailVowel`**
(lines ~365-438), which is an **explicit list** of accepted PGmc
suffix shapes. If the suffix of your PROTOFORM is not in this list,
`pgrmWord` rejects the whole word and `flookup` returns `+?`.

This is by design — keeping the PGmc input space narrow lets the
grammar make confident assumptions downstream. But it means **any
new paradigm cell or unusual derivational suffix needs an explicit
new clause here**.

### Adding a new suffix clause

1. Locate `pgrmWeakTailVowel` (search for `define pgrmWeakTailVowel`).
2. Each clause is a sequence of `surface:{tag}` mappings separated by
   `|`. Example (current line for strong adj/ptc acc.sg.m.):
   ```foma
   a:{*a} n:{*n} ǭ:{*ǭ} |
   ```
   Surface chars on the left, starred tag (kept by upstream stages,
   stripped by `OldEnglishRemoveStars`) on the right.
3. Add your clause **before** the closing `;` of the `pgrmWeakTailVowel`
   definition. Match the indentation of neighbouring lines.
4. Add a comment **above** the clause stating: which paradigm cell or
   suffix it represents, the citation (R/T, Campbell, Fulk, etc.),
   and a reference to the DEV_NOTES section that justifies it.
   Existing precedent: lines 430-437 ("Class III weak paradigm cells").
5. Rebuild (§2). Re-test with `flookup` (§3).

### Don't put characters here that aren't in the PGmc inventory

The right-hand `{*X}` tags must use symbols the downstream stages
already handle. If you invent a new tag, every rule that mentions
`OEAnyVowel`, `pgrmStressedNucleus` etc. probably doesn't know about
it and will silently leave it stranded.

## 7. Editing `germanic.txt` safely

- It is one big file (~6000 lines). Use line numbers and unique
  context when applying patches.
- `define` order is significant — definitions reference earlier
  ones. Adding a new `define` after the rule that uses it will
  silently break.
- The composite at the bottom (`define EnglishProtoToOE …`) is the
  authoritative rule sequence; if you add a new rule, add it both
  here and in `Germanic/fsts/old_english_sandbox.txt` in the same
  position (see `skills/sync-trace-report.md`).
- Watch for the **40-character `define` name limit** — covered in
  `skills/sync-trace-report.md` §"Procedure" step 3. foma silently
  truncates, producing a poisoned bin.

## 8. Quick post-edit checklist

After any edit to a TSV PROTOFORM, `germanic.txt`, or
`old_english_sandbox.txt`:

```bash
# 1. Rebuild
bash Germanic/tools/rebuild_oe_bins.sh 2>&1 | tee /tmp/build.log
grep -iE "should consist of at most 40 character" /tmp/build.log   # must be empty

# 2. Spot-check the affected word
echo 'YOUR_PROTOFORM_SANS_LEADING_STAR' | docker compose exec -T backend \
    bash -lc 'cd /usr/app && flookup -i old_english.bin'

# 3. Mismatch report (regenerate, then read total)
python3 Germanic/tools/oe_mismatch_report.py
head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt

# 4. Stage trace if anything looks off
python3 Germanic/tools/oe_full_trace_report.py
grep -A 30 'YOUR_WORD' Germanic/docs/debug_snapshots/oe_full_trace_report.txt
```

If the count went **up**, you have a regression — investigate before
committing.

## 9. Common failure modes (cheat sheet)

| What you see | Probable cause | Fix |
|--------------|----------------|-----|
| `+?` from flookup | suffix not in `pgrmWeakTailVowel` | §6 — add a clause |
| `+?` from flookup, suffix *is* listed | special char mismatch (`þ` vs `θ`, decomposed vs precomposed) | §4 — normalise |
| `[carry]` everywhere in trace | same as above; tokenisation rejected | §6 |
| `[carry]` at one specific stage | rule failure at that stage | normal phonology debugging |
| flookup output unchanged after edit | bin not rebuilt, or built in wrong place | §2 — `rebuild_oe_bins.sh` |
| `Network name 'X' should consist of at most 40 characters` warning | foma name-limit collapse | `sync-trace-report.md` step 3 |
| Sub-200-byte stage bin | name-limit collapse poisoned the bin | `sync-trace-report.md` step 8 |
| `docker compose exec backend …: No such container` | container not up | `docker compose up -d` |
| Edit looks right but trace shows old behaviour | reading `Germanic/fsts/old_english.bin` instead of `backend/old_english.bin` | use `backend/` for tooling, or rebuild to sync |

## 10. Key invariants

- **Build only via `Germanic/tools/rebuild_oe_bins.sh`.** Never invoke
  `foma` directly on the host.
- **The bin used by tools is `backend/old_english.bin`.** Trust no other
  copy.
- **`pgrmWeakTailVowel` is an explicit allow-list.** New paradigm cell
  ⇒ new clause, with comment + citation.
- **`+?` ≠ phonology bug.** It means tokenisation failed.
- **Special characters are codepoint-exact.** `þ ≠ θ`, `ą ≠ a + ̨`.
- **40-char `define` name limit applies everywhere in foma.** Cross-ref
  `sync-trace-report.md`.
