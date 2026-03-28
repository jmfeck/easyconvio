import pytest
from unittest.mock import patch

from easyconvio.ebook import EbookFile


@pytest.fixture
def ebook_file():
    with patch.object(EbookFile, "_load"):
        f = EbookFile("book.epub")
    return f


@patch("easyconvio.ebook.pypandoc")
def test_to_pdf(mock_pandoc, ebook_file):
    result = ebook_file.to_pdf("out.pdf")
    mock_pandoc.convert_file.assert_called_once_with(
        ebook_file.path, "pdf", outputfile="out.pdf"
    )
    assert result == "out.pdf"


@patch("easyconvio.ebook.pypandoc")
def test_to_html(mock_pandoc, ebook_file):
    ebook_file.to_html("out.html")
    mock_pandoc.convert_file.assert_called_once_with(
        ebook_file.path, "html", outputfile="out.html"
    )


@patch("easyconvio.ebook.pypandoc")
def test_to_epub(mock_pandoc, ebook_file):
    ebook_file.to_epub("out.epub")
    mock_pandoc.convert_file.assert_called_once_with(
        ebook_file.path, "epub", outputfile="out.epub"
    )


@patch("easyconvio.ebook.pypandoc")
def test_to_txt(mock_pandoc, ebook_file):
    ebook_file.to_txt("out.txt")
    mock_pandoc.convert_file.assert_called_once_with(
        ebook_file.path, "plain", outputfile="out.txt"
    )


@patch("easyconvio.ebook.pypandoc")
def test_to_generic(mock_pandoc, ebook_file):
    ebook_file.to("docx", "out.docx")
    mock_pandoc.convert_file.assert_called_once_with(
        ebook_file.path, "docx", outputfile="out.docx"
    )
