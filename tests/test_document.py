import os

import pytest

from easyconvio.document import DocumentFile

from .conftest import needs_pandoc

pytestmark = needs_pandoc


@pytest.fixture
def doc_file(md_path):
    return DocumentFile(md_path)


@pytest.mark.parametrize(
    "method, ext",
    [
        ("to_html", "html"),
        ("to_md", "md"),
        ("to_txt", "txt"),
        ("to_latex", "tex"),
        ("to_rst", "rst"),
        ("to_docx", "docx"),
        ("to_odt", "odt"),
        ("to_rtf", "rtf"),
        ("to_asciidoc", "adoc"),
        ("to_mediawiki", "wiki"),
        ("to_org", "org"),
        ("to_xml", "xml"),
        ("to_epub", "epub"),
    ],
)
def test_export_format(doc_file, tmp_path, method, ext):
    out = str(tmp_path / f"out.{ext}")
    result = getattr(doc_file, method)(out)
    assert result == out
    assert os.path.exists(out)
    assert os.path.getsize(out) > 0


def test_to_pdf_via_html(html_path, tmp_path):
    """PDF requires a PDF engine; pandoc bundles weasyprint or wkhtmltopdf paths.
    Fall back to writing via the HTML path which always works.
    """
    doc = DocumentFile(html_path)
    out = str(tmp_path / "out.pdf")
    try:
        doc.to_pdf(out)
    except (RuntimeError, OSError):
        pytest.skip("No PDF engine (latex/wkhtmltopdf/weasyprint) available")
    assert os.path.exists(out)


def test_to_csv_from_csv(csv_doc_path, tmp_path):
    """CSV→CSV is a fast-path copy."""
    doc = DocumentFile(csv_doc_path)
    out = str(tmp_path / "out.csv")
    doc.to_csv(out)
    assert open(out, encoding="utf-8").read() == "a,b,c\n1,2,3\n4,5,6\n"


def test_to_generic(doc_file, tmp_path):
    out = str(tmp_path / "out.rst")
    result = doc_file.to("rst", out)
    assert result == out
    assert os.path.exists(out)
