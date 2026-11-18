#!/usr/bin/env python3
"""Preserve the supplied EPUB locally and map its retained printed pagination."""
import argparse
import csv
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
LOCAL = ROOT / "docs/references/local/dresher-1985"


class Pages(HTMLParser):
    def __init__(self, member, pages):
        super().__init__()
        self.member, self.pages, self.current = member, pages, None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        anchor = attrs.get("id", "")
        if anchor.startswith("pg_"):
            label = anchor[3:]
            if label in self.pages:
                raise ValueError(f"duplicate printed-page anchor: {label}")
            self.current = {"member": self.member, "anchor": anchor, "text": [], "images": []}
            self.pages[label] = self.current
        if self.current and tag == "img":
            name = str(Path(self.member).parent / attrs["src"])
            self.current["images"].append(name)
            self.current["text"].append(f"\n[IMAGE {name}]\n")
        if self.current and tag in {"p", "h1", "h2", "h3", "br", "li"}:
            self.current["text"].append("\n")

    def handle_data(self, data):
        if self.current:
            self.current["text"].append(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("epub", type=Path)
    args = parser.parse_args()
    LOCAL.mkdir(parents=True, exist_ok=True)
    installed = LOCAL / "original.epub"
    payload = args.epub.read_bytes()
    if installed.exists() and installed.read_bytes() != payload:
        raise RuntimeError("different holding already installed; preserve it before replacement")
    shutil.copyfile(args.epub, installed)
    pages = {}
    with zipfile.ZipFile(installed) as archive:
        opf = ET.fromstring(archive.read("OPS/content.opf"))
        ns = {"o": "http://www.idpf.org/2007/opf"}
        items = {e.attrib["id"]: e.attrib["href"] for e in opf.findall("o:manifest/o:item", ns)}
        for item in opf.findall("o:spine/o:itemref", ns):
            member = "OPS/" + items[item.attrib["idref"]]
            Pages(member, pages).feed(archive.read(member).decode("utf-8"))
        for name in archive.namelist():
            path = LOCAL / "epub" / name
            if not path.resolve().is_relative_to((LOCAL / "epub").resolve()):
                raise ValueError(f"unsafe EPUB member: {name}")
        archive.extractall(LOCAL / "epub")
    text = "\n\n".join(f"=== PRINTED {label}: {p['member']}#{p['anchor']} ===\n"
                       + "".join(p["text"]) for label, p in pages.items())
    (LOCAL / "complete.txt").write_text(text)
    with (HERE / "page_map.tsv").open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["printed_page", "epub_member", "anchor", "image_members"])
        writer.writerows((label, p["member"], p["anchor"], ";".join(p["images"]))
                        for label, p in pages.items())
    with (HERE / "holdings.tsv").open("w") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["citation_key", "format", "original_path", "original_sha256",
                         "text_path", "text_sha256", "access", "edition"])
        writer.writerow(["Dresher1985", "EPUB",
                         str(installed.relative_to(ROOT)), hashlib.sha256(payload).hexdigest(),
                         str((LOCAL / "complete.txt").relative_to(ROOT)),
                         hashlib.sha256(text.encode()).hexdigest(), "local_only",
                         "1985 Garland text; Routledge reissue imprint2019; OPF date2018"])
    print("Installed unchanged EPUB; retained page anchors:", len(pages))


if __name__ == "__main__":
    main()
