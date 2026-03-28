import pytest
from unittest.mock import patch, MagicMock

from easyconvio.document import DocumentFile


@pytest.fixture
def doc_file():
    with patch.object(DocumentFile, "_load"):
        f = DocumentFile("report.docx")
    return f


@patch("easyconvio.document.pypandoc")
def test_to_pdf(mock_pandoc, doc_file):
    result = doc_file.to_pdf("out.pdf")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "pdf", outputfile="out.pdf"
    )
    assert result == "out.pdf"


@patch("easyconvio.document.pypandoc")
def test_to_html(mock_pandoc, doc_file):
    result = doc_file.to_html("out.html")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "html", outputfile="out.html"
    )
    assert result == "out.html"


@patch("easyconvio.document.pypandoc")
def test_to_md(mock_pandoc, doc_file):
    result = doc_file.to_md("out.md")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "md", outputfile="out.md"
    )


@patch("easyconvio.document.pypandoc")
def test_to_txt(mock_pandoc, doc_file):
    result = doc_file.to_txt("out.txt")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "plain", outputfile="out.txt"
    )


@patch("easyconvio.document.pypandoc")
def test_to_latex(mock_pandoc, doc_file):
    result = doc_file.to_latex("out.tex")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "latex", outputfile="out.tex"
    )


@patch("easyconvio.document.pypandoc")
def test_to_generic(mock_pandoc, doc_file):
    doc_file.to("rst", "out.rst")
    mock_pandoc.convert_file.assert_called_once_with(
        doc_file.path, "rst", outputfile="out.rst"
    )
