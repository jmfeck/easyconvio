import os
import zipfile
import tarfile
import pytest

from easyconvio.archive import ArchiveFile


@pytest.fixture
def zip_file(tmp_path):
    zip_path = tmp_path / "test.zip"
    with zipfile.ZipFile(str(zip_path), "w") as zf:
        zf.writestr("hello.txt", "hello world")
        zf.writestr("sub/nested.txt", "nested content")
    return ArchiveFile(str(zip_path))


@pytest.fixture
def tar_file(tmp_path):
    # create a file to add
    f1 = tmp_path / "a.txt"
    f1.write_text("aaa")
    tar_path = tmp_path / "test.tar"
    with tarfile.open(str(tar_path), "w") as tf:
        tf.add(str(f1), arcname="a.txt")
    return ArchiveFile(str(tar_path))


def test_zip_list_files(zip_file):
    files = zip_file.list_files()
    assert "hello.txt" in files
    assert "sub/nested.txt" in files


def test_zip_file_count(zip_file):
    assert zip_file.file_count == 2


def test_zip_extract(zip_file, tmp_path):
    out_dir = str(tmp_path / "extracted")
    zip_file.extract(out_dir)
    assert os.path.exists(os.path.join(out_dir, "hello.txt"))
    assert os.path.exists(os.path.join(out_dir, "sub", "nested.txt"))


def test_zip_extract_file(zip_file, tmp_path):
    out_dir = str(tmp_path / "single")
    result = zip_file.extract_file("hello.txt", out_dir)
    assert os.path.exists(result)
    with open(result) as f:
        assert f.read() == "hello world"


def test_zip_to_tar(zip_file, tmp_path):
    out = str(tmp_path / "converted.tar")
    result = zip_file.to_tar(out)
    assert result == out
    assert os.path.exists(out)
    with tarfile.open(out, "r") as tf:
        names = tf.getnames()
    assert "hello.txt" in names


def test_zip_to_gz(zip_file, tmp_path):
    out = str(tmp_path / "converted.tar.gz")
    result = zip_file.to_gz(out)
    assert result == out
    assert os.path.exists(out)


def test_tar_list_files(tar_file):
    assert "a.txt" in tar_file.list_files()


def test_tar_to_zip(tar_file, tmp_path):
    out = str(tmp_path / "converted.zip")
    result = tar_file.to_zip(out)
    assert result == out
    assert os.path.exists(out)
    with zipfile.ZipFile(out, "r") as zf:
        assert "a.txt" in zf.namelist()


def test_to_generic(zip_file, tmp_path):
    out = str(tmp_path / "generic.tar")
    result = zip_file.to("tar", out)
    assert result == out
    assert os.path.exists(out)
