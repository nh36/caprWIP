#!/usr/bin/env python3
"""Local-only asset reconciliation; publish metadata, never source contents."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[3]
HOME = Path.home()
KINDS = {".pdf", ".txt", ".djvu", ".epub", ".xml"}


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def display(path):
    return str(path).replace(str(HOME), "$HOME", 1)


def bibliography():
    text = (ROOT / "docs/refs.bib").read_text()
    entries = {}
    for match in re.finditer(r"^@\w+\{([^,]+),(.*?)(?=^@|\Z)", text, re.M | re.S):
        body = match[2]
        fields = {}
        for field in re.finditer(r"^\s*(\w+)\s*=\s*\{", body, re.M):
            start = field.end()
            level, end = 1, start
            while level and end < len(body):
                if body[end] in "{}" and body[end - 1] != "\\":
                    level += 1 if body[end] == "{" else -1
                end += 1
            fields[field[1]] = body[start:end - 1]
        entries[match[1]] = dict(citation_key=match[1], bibliography=fields,
                                assets=[], source_records=[])
    return entries


def run(main, output):
    output.mkdir(parents=True, exist_ok=True)
    entries = bibliography()
    associations = {}
    declared_hashes = {}

    def associate(key, path, evidence, coverage="not_established", method="not_established"):
        associations.setdefault(path, []).append(
            dict(citation_key=key, evidence=evidence, coverage=coverage, method=method))

    for key, entry in entries.items():
        path = entry["bibliography"].get("file")
        if path:
            for part in path.split(";"):
                part = part.strip()
                if (ROOT / part).is_dir():
                    for asset in (ROOT / part).rglob("*.txt"):
                        associate(key, str(asset.relative_to(ROOT)),
                                  "docs/refs.bib: page-extraction directory",
                                  "partial/page-level OCR; not a separate source")
                else:
                    associate(key, part, "docs/refs.bib: file field")
                    if part.endswith(".txt"):
                        stem = part[:-4].removesuffix(".vision")
                        if key != "KlugeSeebold2002" and (main / (stem + ".pdf")).is_file():
                            associate(key, stem + ".pdf",
                                      "existing extraction and same-stem source file; "
                                      "edition qualifications remain in README_resources.md",
                                      "PDF held; completeness not inferred from filename")
                    elif part.endswith(".pdf"):
                        stem = part[:-4]
                        texts = ([stem + ".txt", stem + ".vision.txt"]
                                 if key != "KlugeSeebold2011" else
                                 ["docs/references/kluge_seebold_2011_25th.txt"])
                        for text in texts:
                            if (main / text).is_file():
                                associate(key, text,
                                          "existing source/extraction pair; edition qualifications "
                                          "remain in README_resources.md",
                                          "searchable derivative; completeness not newly certified")
    for path in ("docs/references/bosworth_toller_anglo_saxon_dictionary.txt",
                 "docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt"):
        associate("BosworthToller1898", path, "README_resources.md: main dictionary",
                  "existing searchable text; original scan not located")
    associate("Stiles1985", "docs/references/stiles_1985_four_part1_nowele6.pdf",
              "existing article source; selected text is explicitly pp.89–94 only",
              "article PDF, distinct from partial text")
    for key in ("HoggIntroduction1992", "Bammesberger1992", "HoggPhonology1992",
                "Traugott1992", "Kastovsky1992", "Clark1992"):
        associate(key, "docs/references/hogg_chel_1992_volume1.pdf",
                  "chapter in newly preserved Cambridge History volume I",
                  "whole-volume container, not independent chapter edition")
    for path in (main / "docs/references").glob("bremmer_2009_introduction_old_frisian_part_*.pdf"):
        associate("Bremmer2009", str(path.relative_to(main)),
                  "existing split source PDFs", "part of source; aggregate completeness not certified")
    for manifest in (ROOT / "docs/references").rglob("holdings.tsv"):
        for row in csv.DictReader(manifest.open(), delimiter="\t"):
            for kind in ("pdf", "text"):
                if row.get(kind + "_path"):
                    associate(row["citation_key"], row[kind + "_path"],
                              str(manifest.relative_to(ROOT)),
                              row.get("coverage", "complete per intake manifest"),
                              row.get("extraction", row.get("method", "original")))
                    declared_hashes[row[kind + "_path"]] = row.get(kind + "_sha256")
    for key, paths in {
        "Colman2011": ["docs/references/local/colman-2011/complete.txt"],
        "LloydSpringer1988": ["docs/references/ewa_band1_lloyd_springer.pdf",
                             "docs/references/local/lloyd-springer-1988/original.djvu"],
    }.items():
        for path in paths:
            associate(key, path, "2026-11-04 local title/hash inspection",
                      "complete335-sheet OCR; not diplomatic" if path.endswith(".txt")
                      else "original; completeness not inferred from filename")
    decisions = json.loads(Path(__file__).with_name("intake-decisions.json").read_text())
    for decision in decisions.values():
        if decision.get("citation_key") and decision.get("target"):
            associate(decision["citation_key"], decision["target"],
                      "holdings_audit_2026-11-04/intake-decisions.json",
                      "source file retained; consultation scope recorded separately",
                      decision["inspection"])
    for filename in ("preservation.json", "research-supplement.json", "seiler-supplement.json"):
        preservation_path = Path(__file__).with_name(filename)
        preservation = json.loads(preservation_path.read_text()) if preservation_path.exists() else {}
        for record in preservation.get("records", []):
            declared_hashes[record["target"]] = record["sha256"]
            if record.get("text", {}).get("path"):
                declared_hashes[record["text"]["path"]] = record["text"]["sha256"]
            if record.get("citation_key"):
                associate(record["citation_key"], record["target"],
                          f"holdings_audit_2026-11-04/{filename}",
                          "original acquired file", record["inspection"])
                if record.get("text", {}).get("path"):
                    associate(record["citation_key"], record["text"]["path"],
                              f"holdings_audit_2026-11-04/{filename}",
                              record["text"]["coverage"], record["text"]["method"])
    for path in (main / "docs/references").glob("herren_et_al_epinal_erfurt_revised_*.pdf"):
        associate("HerrenEtAl2026", str(path.relative_to(main)),
                  "README_resources.md: five explicitly targeted letter/introduction files",
                  "partial selection of revised edition; not complete glossary", "original PDFs")
    associate("LloydSpringer1988", "docs/references/ewa_band1_lloyd_springer.txt",
              "1988 title/copyright plus 335 legacy formfeeds and final bezzisto endpoint",
              "335-sheet legacy OCR; glyph accuracy not globally checked", "existing OCR")
    associate("Colman2011", "docs/references/local/colman-2011/complete.txt",
              "four-cell closeout exact SHA256 verified in main and research worktrees",
              "complete per preserved closeout", "existing searchable extraction; no replacement")
    declared_hashes.update({
        "docs/references/colman_2011_moneyers_buga_boia.pdf":
            "0af5841706ba5a00007acc5fa027b0faf4263b1287199430cb212a21326f3c9d",
        "docs/references/local/colman-2011/complete.txt":
            "36b5aecf61225a39c09299e3695bf0c02b8389b7e8e195e277b4352e1f0e0e7c",
    })

    worktrees = [Path(line.split(" ", 1)[1]) for line in subprocess.check_output(
        ["git", "-C", str(ROOT), "worktree", "list", "--porcelain"], text=True).splitlines()
        if line.startswith("worktree ")]
    roots = list(dict.fromkeys([main] + worktrees))
    assets, by_hash = [], {}
    for root in roots:
        library = root / "docs/references"
        if not library.exists():
            continue
        for path in sorted(library.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in KINDS or path.is_symlink():
                continue
            relative = str(path.relative_to(root))
            item = dict(path=display(path), project_relative=relative,
                        bytes=path.stat().st_size, sha256=digest(path),
                        representation=path.suffix.lower().lstrip("."),
                        associations=associations.get(relative, []),
                        root_role="durable_main_project" if root == main else
                        "same_disk_worktree_not_independent_backup",
                        preservation_copies=[])
            if declared_hashes.get(relative):
                item["registered_hash_matches"] = item["sha256"] == declared_hashes[relative]
            assets.append(item)
            by_hash.setdefault(item["sha256"], []).append(item)
    for copies in by_hash.values():
        links = {json.dumps(link, sort_keys=True): link
                 for item in copies for link in item["associations"]}
        for item in copies:
            item["associations"] = list(links.values())
            item["source_representation_status"] = (
                "OCR-derived PDF; not substituted for an original scan"
                if item["representation"] == "pdf" and "_ocr" in item["project_relative"]
                else "searchable derivative; see coverage/method records"
                if item["representation"] == "txt"
                else "acquired file; edition and derivative qualifications remain applicable")

    bundles = list((main / "docs/references/local/backups").glob("*.tar.gz"))
    bundle_records = []
    for bundle in bundles:
        record = dict(path=display(bundle), sha256=digest(bundle),
                      role="same_disk_restoration_bundle_not_disaster_recovery",
                      verified_matching_members=0)
        with tarfile.open(bundle) as archive:
            for member in archive:
                if not member.isfile():
                    continue
                h = hashlib.sha256()
                stream = archive.extractfile(member)
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(block)
                matches = by_hash.get(h.hexdigest(), [])
                for item in matches:
                    item["preservation_copies"].append(display(bundle) + ":" + member.name)
                if matches:
                    record["verified_matching_members"] += 1
        bundle_records.append(record)

    external_roots = [HOME / "Downloads" / name for name in (
        "Germanic", "New CAPR resources", "New to OCR", "New new to OCR",
        "Books2/German stuff")]
    external, seen = [], set()
    for root in external_roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".pdf", ".djvu", ".epub"}:
                continue
            if path in seen:
                continue
            seen.add(path)
            identity = digest(path)
            matches = by_hash.get(identity, [])
            decision = decisions.get(identity[:12], {})
            external.append(dict(path=display(path), sha256=identity,
                                 bytes=path.stat().st_size,
                                 project_copies=[item["path"] for item in matches],
                                 status="excluded_project_manuscript" if decision.get("exclude")
                                 else "exact_bytes_preserved" if matches else
                                 "stranded_candidate_identity_or_scope_to_review"))
    for root in roots:
        cache = root / ".capr-work/source-readings"
        if cache.exists():
            external_roots.append(cache)
            for path in sorted(cache.glob("*.pdf")):
                identity = digest(path)
                matches = by_hash.get(identity, [])
                external.append(dict(path=display(path), sha256=identity,
                                     bytes=path.stat().st_size,
                                     project_copies=[item["path"] for item in matches],
                                     status="exact_bytes_preserved" if matches else
                                     "stranded_research_original"))
    seiler = HOME / "Downloads/master-gdc-gdcebookspublic-20-21-75-85-04-2021758504-2021758504.pdf"
    if seiler.exists():
        identity = digest(seiler)
        matches = by_hash.get(identity, [])
        external.append(dict(path=display(seiler), sha256=identity,
                             bytes=seiler.stat().st_size,
                             project_copies=[item["path"] for item in matches],
                             status="exact_bytes_preserved" if matches else "stranded_OA_volume"))
    desktop_record = ROOT / "docs/references/desktop_2026-11-04/originals.json"
    desktop_files = []
    if desktop_record.exists():
        for record in json.loads(desktop_record.read_text()):
            path = Path(record["origin"].replace("$HOME", str(HOME), 1))
            if not path.exists():
                continue
            desktop_files.append(display(path))
            identity = digest(path)
            matches = by_hash.get(identity, [])
            external.append(dict(path=display(path), sha256=identity,
                                 bytes=path.stat().st_size,
                                 project_copies=[item["path"] for item in matches],
                                 status="exact_bytes_preserved" if matches else "stranded_Desktop_source"))

    grouped = {}
    for item in assets:
        identity = item["project_relative"], item["sha256"]
        if identity not in grouped:
            grouped[identity] = dict(item, copy_locations=[item["path"]])
        else:
            grouped[identity]["copy_locations"].append(item["path"])
    asset_file_count = len(assets)
    assets = list(grouped.values())
    for item in assets:
        for association in item["associations"]:
            key = association["citation_key"]
            if key in entries:
                entries[key]["assets"].append(item["path"])
    records = list((ROOT / "Germanic/docs/lexeme_reports").rglob("*.md"))
    records += list((ROOT / "Germanic/docs/sound_changes/literature_dossiers").rglob("*.md"))
    records += list((ROOT / "Germanic/docs/sound_changes/audits").rglob("*.md"))
    records += list((ROOT / "docs/references").glob("*/README.md"))
    for path in records:
        text = path.read_text(errors="replace")
        for key in entries:
            if re.search(r"(?<!\w)" + re.escape(key) + r"(?!\w)", text):
                entries[key]["source_records"].append(str(path.relative_to(ROOT)))
    for entry in entries.values():
        entry["inspection_status"] = (
            "consultation_records_linked_not_a_new_direct_reading_certification"
            if entry["source_records"] else "not_established_by_this_holdings_audit")
        entry["holding_status"] = "held" if entry["assets"] else "no_exact_registered_asset_located"
        entry["independent_off_machine_backup"] = "not_verified"
        selected = [a for a in assets if a["path"] in entry["assets"]]
        entry["original_source_files"] = [
            dict(path=a["path"], sha256=a["sha256"], format=a["representation"],
                 representation_status=a["source_representation_status"])
            for a in selected if a["representation"] != "txt"]
        entry["searchable_texts"] = [
            dict(path=a["path"], sha256=a["sha256"],
                 coverage_and_method=[link for link in a["associations"]
                                      if link["citation_key"] == entry["citation_key"]])
            for a in selected if a["representation"] == "txt"]
        entry["verified_local_restoration_copies"] = sorted({
            copy for a in selected for copy in a["preservation_copies"]})
        entry["acquisition_origin"] = [
            dict(origin=row["path"], sha256=row["sha256"])
            for row in external if any(a["sha256"] == row["sha256"] for a in selected)]
        entry["stranded_acquisition_status"] = (
            "none in searched candidate set; not a claim about unsearched files")

    archive = HOME / "CAPR-local-archive-2026-08-11"
    named_missing = [
        dict(requested_key="Bennett1968", identity="The Accentuation of Gothic ga-, pp.53–60",
             status="unacquired; Bennett1950 is not a substitute",
             evidence="docs/references/ga_prefix_2026-10-25/corrections.md"),
        dict(requested_key="Stiles1995", identity="Remarks on the Anglo-Frisian Thesis, pp.177–220",
             status="unacquired; original known through explicitly attributed reports",
             evidence="Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/missing-direct-sources.md"),
        dict(requested_key="Hock1973",
             identity="On the Phonemic Status of Germanic e and i, Issues in Linguistics, pp.319–351",
             status="unacquired; known only through Hill2017/Fulk2018 reports",
             evidence="Germanic/docs/sound_changes/audits/sc015-a-ablaut-investigation/INGESTION_MANIFEST.md"),
    ]
    result = dict(schema=1, audit_date="2026-11-04", main_project=display(main),
                  bibliography_owner="docs/refs.bib", sources=list(entries.values()),
                  assets=assets, checked_asset_file_copies=asset_file_count,
                  external_candidates=external,
                  restoration_bundles=bundle_records, named_unacquired=named_missing,
                  old_archive=dict(path=display(archive), exists=archive.exists(),
                                   git_bundles=[display(p) for p in (archive / "bundles").glob("*")],
                                   limitation="same disk; Git bundles do not imply ignored PDF preservation"),
                  searched_external_roots=[display(p) for p in external_roots],
                  explicitly_checked_external_files=desktop_files + (
                      [display(seiler)] if seiler.exists() else []))
    (output / "inventory.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    stranded = [r for r in external if r["status"].startswith("stranded")]
    print(json.dumps(dict(sources=len(entries), asset_files=len(assets),
                          external=len(external), stranded=len(stranded))))
    for row in stranded:
        print(row["sha256"][:12], row["path"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run(args.main.resolve(), args.output.resolve())
