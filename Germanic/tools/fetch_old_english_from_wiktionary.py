#!/usr/bin/env python3
"""Fetch Old English etymologies for English lemmas via the Wiktionary API."""
from __future__ import annotations
import argparse
import csv
import json
import re
import ssl
import time
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import certifi  # type: ignore
except ImportError:  # pragma: no cover
    certifi = None

CACHE_DIR = Path("server/tmp/wiktionary_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)
API_ENDPOINT = "https://en.wiktionary.org/w/api.php"
USER_AGENT = "CAPR-OE-fetcher/0.1 (https://github.com/capr)"
TEMPLATE_NAMES = {"inh", "der", "bor", "etyl", "derived", "inherit"}
OLD_ENGLISH_LABEL = "old english"

if certifi is not None:
    SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
else:  # pragma: no cover
    SSL_CONTEXT = ssl.create_default_context()


def slugify(title: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", title)


def read_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    with path.open() as handle:
        return json.load(handle)


def write_json(path: Path, data: dict) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("w") as handle:
        json.dump(data, handle)
    tmp.replace(path)


def fetch_page(title: str, delay: float = 0.5) -> dict:
    slug = slugify(title)
    cache_path = CACHE_DIR / f"{slug}.json"
    cached = read_json(cache_path)
    if cached:
        return cached
    params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "rvslots": "main",
        "rvprop": "content",
        "titles": title,
    }
    url = f"{API_ENDPOINT}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, context=SSL_CONTEXT) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    write_json(cache_path, data)
    time.sleep(delay)
    return data


def extract_wikitext(api_payload: dict) -> tuple[str, str] | tuple[None, None]:
    pages = api_payload.get("query", {}).get("pages", {})
    for page_id, page in pages.items():
        if int(page_id) < 0:
            continue
        revisions = page.get("revisions")
        if not revisions:
            continue
        content = revisions[0].get("slots", {}).get("main", {}).get("*")
        if content:
            return page.get("title", ""), content
    return None, None


def strip_markup(text: str) -> str:
    text = text.strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2]
        if "|" in text:
            text = text.split("|", 1)[1]
        if "#" in text:
            text = text.split("#", 1)[0]
    while text.startswith("{{") and text.endswith("}}"):
        inner = text[2:-2]
        parts = inner.split("|")
        if len(parts) >= 3 and parts[0] in {"l", "m", "link"}:
            text = parts[2]
        elif len(parts) >= 2:
            text = parts[-1]
        else:
            break
    return text.strip()


def parse_template(raw: str) -> tuple[str, list[str]]:
    parts = raw.split("|")
    name = parts[0].strip().lower()
    params = [p.strip() for p in parts[1:]]
    return name, params


def extract_templates(wikitext: str) -> list[tuple[str, list[str]]]:
    templates: list[tuple[str, list[str]]] = []
    i = 0
    length = len(wikitext)
    while i < length:
        if wikitext.startswith("{{", i):
            depth = 1
            j = i + 2
            while j < length and depth > 0:
                if wikitext.startswith("{{", j):
                    depth += 1
                    j += 2
                elif wikitext.startswith("}}", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            content = wikitext[i + 2 : j - 2]
            name, params = parse_template(content)
            templates.append((name, params))
            i = j
        else:
            i += 1
    return templates


def extract_from_templates(wikitext: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for name, params in extract_templates(wikitext):
        if name not in TEMPLATE_NAMES:
            continue
        if len(params) < 3:
            continue
        lang = params[0].lower()
        source_lang = params[1].lower()
        if lang != "en" or source_lang != "ang":
            continue
        lemma = ""
        for param in params[2:]:
            if param.startswith("1="):
                lemma = param.split("=", 1)[1]
                break
        if not lemma and len(params) >= 3:
            lemma = params[2]
        lemma = strip_markup(lemma)
        if not lemma:
            continue
        results.append({"lemma": lemma, "source": name, "detail": f"template:{name}"})
    return results


def extract_from_text(wikitext: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    pattern = re.compile(r"Old English[^\[]*\[\[([^\]|#]+)", re.IGNORECASE)
    for match in pattern.finditer(wikitext):
        lemma = strip_markup(match.group(1))
        if lemma:
            results.append({"lemma": lemma, "source": "text", "detail": "Old English link"})
    return results


def gather_lemmas(wikitext: str) -> list[dict[str, str]]:
    lemmas: list[dict[str, str]] = []
    seen: set[str] = set()
    for entry in extract_from_templates(wikitext) + extract_from_text(wikitext):
        lemma = entry["lemma"]
        if lemma.lower() in seen:
            continue
        seen.add(lemma.lower())
        lemmas.append(entry)
    return lemmas


def load_english_words(tsv_path: Path) -> list[str]:
    seen = set()
    words: list[str] = []
    with tsv_path.open() as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "English":
                continue
            word = row.get("COUNTERPART", "").strip()
            if not word or word in seen:
                continue
            seen.add(word)
            words.append(word)
    return words


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tsv", type=Path, help="Output TSV with columns ENGLISH,OE_FORM,SOURCE,DETAIL,PAGE")
    parser.add_argument("data", type=Path, help="Path to germanic-aligned-final TSV to pull English lemmas")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of words for debugging")
    args = parser.parse_args()

    words = load_english_words(args.data)
    if args.limit:
        words = words[: args.limit]
    rows = []
    for word in words:
        try:
            payload = fetch_page(word)
        except Exception as exc:
            print(f"[WARN] Failed to fetch {word}: {exc}")
            continue
        title, wikitext = extract_wikitext(payload)
        if not wikitext:
            print(f"[WARN] No wikitext for {word}")
            continue
        lemmas = gather_lemmas(wikitext)
        if not lemmas:
            print(f"[INFO] No Old English lemma found for {word}")
            continue
        best = lemmas[0]
        rows.append(
            {
                "ENGLISH": word,
                "OE_FORM": best["lemma"],
                "SOURCE": best["source"],
                "DETAIL": best["detail"],
                "PAGE": title or word,
            }
        )
    args.tsv.parent.mkdir(parents=True, exist_ok=True)
    with args.tsv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["ENGLISH", "OE_FORM", "SOURCE", "DETAIL", "PAGE"], delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print(f"Wrote {len(rows)} entries to {args.tsv}")


if __name__ == "__main__":
    main()
