import hashlib
from pathlib import Path
import subprocess
import sys

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from bootstrap_references import provision, registered


def test_registered_private_pdf_can_be_copied_from_cache_into_worktree(tmp_path):
    checkout = tmp_path / "checkout"
    checkout.mkdir()
    subprocess.run(["git", "init", "-q", checkout], check=True)
    (checkout / ".gitignore").write_text("docs/references/*.pdf\n")
    relative = Path("docs/references/registered.pdf")
    original = b"exact original"
    sha = hashlib.sha256(original).hexdigest()
    ledger = checkout / "docs/references/intake/holdings.tsv"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(f"citation_key\tpdf_path\tpdf_sha256\nExample\t{relative}\t{sha}\n")
    cache = tmp_path / "cache"
    (cache / relative).parent.mkdir(parents=True)
    (cache / relative).write_bytes(original)

    assert registered(checkout, ["Example"], False) == {relative: sha}
    assert provision(checkout, relative, sha, (tmp_path / "main", cache))
    assert not (checkout / relative).is_symlink()
    assert (checkout / relative).read_bytes() == original


def test_provision_refuses_unpinned_bytes_and_does_not_replace_existing_file(tmp_path):
    checkout = tmp_path / "checkout"
    checkout.mkdir()
    subprocess.run(["git", "init", "-q", checkout], check=True)
    (checkout / ".gitignore").write_text("docs/references/*.pdf\n")
    relative = Path("docs/references/registered.pdf")
    source = tmp_path / "main" / relative
    source.parent.mkdir(parents=True)
    source.write_bytes(b"different scan")
    target = checkout / relative
    sha = hashlib.sha256(b"registered scan").hexdigest()

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        provision(checkout, relative, sha, (source.parents[2],))
    assert not target.exists()
    target.write_bytes(b"existing file")
    with pytest.raises(ValueError, match="destination is not the registered file"):
        provision(checkout, relative, sha, (source.parents[2],))
    assert target.read_bytes() == b"existing file"
