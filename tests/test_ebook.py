import os

import pytest

from easyconvio.ebook import EbookFile

from .conftest import needs_pandoc, needs_calibre

pytestmark = needs_pandoc


@pytest.fixture
def ebook_file(epub_path):
    return EbookFile(epub_path)


@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_epub", "epub"),
        ("to_html", "html"),
        ("to_txt", "txt"),
        ("to_docx", "docx"),
        ("to_fb2", "fb2"),
    ],
)
def test_export_format(ebook_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(ebook_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


@needs_calibre
def test_to_mobi(ebook_file, tmp_path):
    out = str(tmp_path / "out.mobi")
    ebook_file.to_mobi(out)
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


@needs_calibre
def test_to_azw3(ebook_file, tmp_path):
    out = str(tmp_path / "out.azw3")
    ebook_file.to_azw3(out)
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_to_pdf(ebook_file, tmp_path):
    out = str(tmp_path / "out.pdf")
    try:
        ebook_file.to_pdf(out)
    except (RuntimeError, OSError):
        pytest.skip("No PDF engine available")
    assert os.path.exists(out)


def test_to_generic(ebook_file, tmp_path):
    out = str(tmp_path / "out.html")
    result = ebook_file.to("html", out)
    assert os.path.exists(out)
