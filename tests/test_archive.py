import os
import tarfile
import zipfile

import pytest

from easyconvio.archive import ArchiveFile

from .conftest import needs_py7zr


# --- listing & extraction (zip) ---


def test_zip_list_count(zip_path):
    arc = ArchiveFile(zip_path)
    files = arc.list_files()
    assert "a.txt" in files
    assert "b.txt" in files
    assert any("c.txt" in f for f in files)
    assert arc.file_count == 3


def test_zip_extract(zip_path, tmp_path):
    out = str(tmp_path / "out")
    ArchiveFile(zip_path).extract(out)
    assert os.path.exists(os.path.join(out, "a.txt"))
    assert os.path.exists(os.path.join(out, "sub", "c.txt"))


def test_zip_extract_file(zip_path, tmp_path):
    out = str(tmp_path / "one")
    result = ArchiveFile(zip_path).extract_file("a.txt", out)
    assert os.path.exists(result)
    assert open(result, encoding="utf-8").read() == "hello"


# --- listing (tar/gz) ---


def test_tar_list(tar_path):
    arc = ArchiveFile(tar_path)
    assert arc.file_count == 3


def test_gz_list(gz_path):
    arc = ArchiveFile(gz_path)
    assert arc.file_count == 3


# --- write conversions: every claimed format ---


@pytest.mark.parametrize(
    "method, ext, opener",
    [
        ("to_zip", "zip", lambda p: zipfile.ZipFile(p, "r").namelist()),
        ("to_jar", "jar", lambda p: zipfile.ZipFile(p, "r").namelist()),
        ("to_tar", "tar", lambda p: tarfile.open(p, "r").getnames()),
        ("to_gz", "tar.gz", lambda p: tarfile.open(p, "r:gz").getnames()),
        ("to_tgz", "tgz", lambda p: tarfile.open(p, "r:gz").getnames()),
        ("to_bz2", "tar.bz2", lambda p: tarfile.open(p, "r:bz2").getnames()),
        ("to_xz", "tar.xz", lambda p: tarfile.open(p, "r:xz").getnames()),
    ],
)
def test_write_format(zip_path, tmp_path, method, ext, opener):
    arc = ArchiveFile(zip_path)
    out = str(tmp_path / f"out.{ext}")
    result = getattr(arc, method)(out)
    assert result == out
    assert os.path.exists(out)
    names = opener(out)
    assert any("a.txt" in n for n in names)


@needs_py7zr
def test_to_7z(zip_path, tmp_path):
    import py7zr
    arc = ArchiveFile(zip_path)
    out = str(tmp_path / "out.7z")
    arc.to_7z(out)
    assert os.path.exists(out)
    with py7zr.SevenZipFile(out, "r") as sz:
        assert any("a.txt" in n for n in sz.getnames())


@needs_py7zr
def test_read_7z(sevenz_path):
    arc = ArchiveFile(sevenz_path)
    assert arc.file_count == 3


def test_to_generic(zip_path, tmp_path):
    out = str(tmp_path / "generic.tar")
    ArchiveFile(zip_path).to("tar", out)
    assert os.path.exists(out)
