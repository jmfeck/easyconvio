"""Shared fixtures for easyconvio tests.

All fixtures generate REAL files at test time using the same libraries the
production code uses. This proves end-to-end behavior, not just import paths.
"""
from __future__ import annotations

import os
import shutil
import struct
import wave
from pathlib import Path

import pytest
from PIL import Image


# --- helpers ---


def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def _have_module(name: str) -> bool:
    """True if the module imports without error.

    Catches a broad Exception because some optional libs (e.g. cairosvg)
    raise OSError at import time when their native deps are missing.
    """
    try:
        __import__(name)
        return True
    except Exception:
        return False


# --- markers ---


needs_ffmpeg = pytest.mark.skipif(not _have("ffmpeg"), reason="ffmpeg not installed")
needs_pandoc = pytest.mark.skipif(not _have("pandoc"), reason="pandoc not installed")
needs_libreoffice = pytest.mark.skipif(
    not _have("libreoffice") and not _have("soffice"),
    reason="LibreOffice not installed",
)
needs_inkscape = pytest.mark.skipif(not _have("inkscape"), reason="Inkscape not installed")
needs_calibre = pytest.mark.skipif(
    not _have("ebook-convert"), reason="Calibre (ebook-convert) not installed"
)
needs_unrar = pytest.mark.skipif(not _have("unrar"), reason="unrar not installed")
needs_pillow_heif = pytest.mark.skipif(
    not _have_module("pillow_heif"), reason="pillow-heif not installed"
)
needs_openpyxl = pytest.mark.skipif(not _have_module("openpyxl"), reason="openpyxl not installed")
needs_odfpy = pytest.mark.skipif(not _have_module("odf"), reason="odfpy not installed")
needs_xlrd = pytest.mark.skipif(not _have_module("xlrd"), reason="xlrd not installed")
needs_python_pptx = pytest.mark.skipif(
    not _have_module("pptx"), reason="python-pptx not installed"
)
needs_fonttools = pytest.mark.skipif(
    not _have_module("fontTools"), reason="fontTools not installed"
)
needs_ezdxf = pytest.mark.skipif(not _have_module("ezdxf"), reason="ezdxf not installed")
needs_cairosvg = pytest.mark.skipif(
    not _have_module("cairosvg"), reason="cairosvg not installed"
)
needs_py7zr = pytest.mark.skipif(not _have_module("py7zr"), reason="py7zr not installed")


# --- image fixtures ---


@pytest.fixture
def jpg_path(tmp_path) -> str:
    p = tmp_path / "photo.jpg"
    Image.new("RGB", (120, 80), color="red").save(p)
    return str(p)


@pytest.fixture
def png_path(tmp_path) -> str:
    p = tmp_path / "photo.png"
    Image.new("RGBA", (60, 40), color=(0, 128, 255, 200)).save(p)
    return str(p)


@pytest.fixture
def heic_path(tmp_path) -> str:
    """Build a real HEIC file via pillow-heif."""
    pytest.importorskip("pillow_heif")
    from pillow_heif import register_heif_opener
    register_heif_opener()
    p = tmp_path / "photo.heic"
    Image.new("RGB", (40, 30), color="green").save(p, "HEIF")
    return str(p)


# --- audio fixtures ---


def _write_wav(path: str, duration_s: float = 0.5, freq: int = 440, rate: int = 16000) -> None:
    """Pure-stdlib WAV writer — produces a real signal even without ffmpeg."""
    import math
    n = int(rate * duration_s)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        for i in range(n):
            sample = int(32767 * 0.3 * math.sin(2 * math.pi * freq * i / rate))
            wf.writeframes(struct.pack("<h", sample))


@pytest.fixture
def wav_path(tmp_path) -> str:
    p = tmp_path / "tone.wav"
    _write_wav(str(p))
    return str(p)


@pytest.fixture
def mp3_path(tmp_path, wav_path) -> str:
    """Real mp3 built from a wav via pydub (requires ffmpeg)."""
    if not _have("ffmpeg"):
        pytest.skip("ffmpeg required to make mp3 fixture")
    from pydub import AudioSegment
    p = tmp_path / "tone.mp3"
    AudioSegment.from_wav(wav_path).export(p, format="mp3")
    return str(p)


# --- video fixtures ---


@pytest.fixture
def mp4_path(tmp_path) -> str:
    """Real mp4 built via moviepy (requires ffmpeg)."""
    if not _have("ffmpeg"):
        pytest.skip("ffmpeg required to make mp4 fixture")
    try:
        from moviepy import ColorClip
    except ImportError:
        from moviepy.editor import ColorClip
    p = tmp_path / "clip.mp4"
    clip = ColorClip(size=(64, 48), color=(255, 0, 0), duration=1.0).with_fps(10)
    clip.write_videofile(str(p), codec="libx264", audio=False, logger=None)
    clip.close()
    return str(p)


# --- document fixtures ---


@pytest.fixture
def md_path(tmp_path) -> str:
    p = tmp_path / "doc.md"
    p.write_text(
        "# Hello\n\nThis is a **test** document.\n\n"
        "| col1 | col2 |\n|------|------|\n| 1    | 2    |\n",
        encoding="utf-8",
    )
    return str(p)


@pytest.fixture
def html_path(tmp_path) -> str:
    p = tmp_path / "doc.html"
    p.write_text(
        "<html><body><h1>Hello</h1><p>Test</p>"
        "<table><tr><th>a</th><th>b</th></tr><tr><td>1</td><td>2</td></tr></table>"
        "</body></html>",
        encoding="utf-8",
    )
    return str(p)


@pytest.fixture
def docx_path(tmp_path, md_path) -> str:
    """Build a real .docx by converting md via pandoc."""
    if not _have("pandoc"):
        pytest.skip("pandoc required to build docx fixture")
    import pypandoc
    p = tmp_path / "doc.docx"
    pypandoc.convert_file(md_path, "docx", outputfile=str(p))
    return str(p)


@pytest.fixture
def csv_doc_path(tmp_path) -> str:
    p = tmp_path / "data.csv"
    p.write_text("a,b,c\n1,2,3\n4,5,6\n", encoding="utf-8")
    return str(p)


# --- ebook fixtures ---


@pytest.fixture
def epub_path(tmp_path, md_path) -> str:
    """Build a real .epub via pandoc."""
    if not _have("pandoc"):
        pytest.skip("pandoc required to build epub fixture")
    import pypandoc
    p = tmp_path / "book.epub"
    pypandoc.convert_file(md_path, "epub", outputfile=str(p))
    return str(p)


# --- archive fixtures ---


@pytest.fixture
def src_dir(tmp_path) -> str:
    """A small source directory used for all archive tests."""
    d = tmp_path / "src"
    d.mkdir()
    (d / "a.txt").write_text("hello", encoding="utf-8")
    (d / "b.txt").write_text("world", encoding="utf-8")
    sub = d / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("nested", encoding="utf-8")
    return str(d)


@pytest.fixture
def zip_path(tmp_path, src_dir) -> str:
    import zipfile
    p = tmp_path / "files.zip"
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(src_dir):
            for f in files:
                full = os.path.join(root, f)
                zf.write(full, os.path.relpath(full, src_dir))
    return str(p)


@pytest.fixture
def tar_path(tmp_path, src_dir) -> str:
    import tarfile
    p = tmp_path / "files.tar"
    with tarfile.open(p, "w") as tf:
        for root, _, files in os.walk(src_dir):
            for f in files:
                full = os.path.join(root, f)
                tf.add(full, os.path.relpath(full, src_dir))
    return str(p)


@pytest.fixture
def gz_path(tmp_path, src_dir) -> str:
    import tarfile
    p = tmp_path / "files.tar.gz"
    with tarfile.open(p, "w:gz") as tf:
        for root, _, files in os.walk(src_dir):
            for f in files:
                full = os.path.join(root, f)
                tf.add(full, os.path.relpath(full, src_dir))
    return str(p)


@pytest.fixture
def sevenz_path(tmp_path, src_dir) -> str:
    py7zr = pytest.importorskip("py7zr")
    p = tmp_path / "files.7z"
    with py7zr.SevenZipFile(str(p), "w") as sz:
        for root, _, files in os.walk(src_dir):
            for f in files:
                full = os.path.join(root, f)
                sz.write(full, os.path.relpath(full, src_dir))
    return str(p)


# --- presentation fixtures ---


@pytest.fixture
def pptx_path(tmp_path) -> str:
    pptx_mod = pytest.importorskip("pptx")
    Presentation = pptx_mod.Presentation
    p = tmp_path / "slides.pptx"
    prs = Presentation()
    blank_layout = prs.slide_layouts[5]
    for i in range(2):
        slide = prs.slides.add_slide(blank_layout)
        slide.shapes.title.text = f"Slide {i + 1}"
    prs.save(str(p))
    return str(p)


# --- spreadsheet fixtures ---


@pytest.fixture
def xlsx_path(tmp_path) -> str:
    openpyxl = pytest.importorskip("openpyxl")
    p = tmp_path / "data.xlsx"
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["a", "b", "c"])
    ws.append([1, 2, 3])
    ws.append([4, 5, 6])
    ws2 = wb.create_sheet("Summary")
    ws2.append(["total", 21])
    wb.save(p)
    return str(p)


@pytest.fixture
def ods_path(tmp_path) -> str:
    odf_mod = pytest.importorskip("odf.opendocument")
    from odf.opendocument import OpenDocumentSpreadsheet
    from odf.table import Table, TableRow, TableCell
    from odf.text import P
    p = tmp_path / "data.ods"
    doc = OpenDocumentSpreadsheet()
    table = Table(name="Data")
    for row in [["a", "b"], ["1", "2"], ["3", "4"]]:
        tr = TableRow()
        for v in row:
            cell = TableCell()
            cell.addElement(P(text=v))
            tr.addElement(cell)
        table.addElement(tr)
    doc.spreadsheet.addElement(table)
    doc.save(p)
    return str(p)


@pytest.fixture
def csv_sheet_path(tmp_path) -> str:
    p = tmp_path / "data.csv"
    p.write_text("a,b,c\n1,2,3\n4,5,6\n", encoding="utf-8")
    return str(p)


@pytest.fixture
def tsv_path(tmp_path) -> str:
    p = tmp_path / "data.tsv"
    p.write_text("a\tb\tc\n1\t2\t3\n4\t5\t6\n", encoding="utf-8")
    return str(p)


# --- vector fixtures ---


@pytest.fixture
def svg_path(tmp_path) -> str:
    p = tmp_path / "logo.svg"
    p.write_text(
        '<?xml version="1.0"?>'
        '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50" viewBox="0 0 100 50">'
        '<rect width="100" height="50" fill="blue"/>'
        '<circle cx="50" cy="25" r="20" fill="yellow"/>'
        '</svg>',
        encoding="utf-8",
    )
    return str(p)


# --- font fixtures ---


@pytest.fixture
def ttf_path(tmp_path) -> str:
    """Build a minimal real TTF using fontTools."""
    fontTools = pytest.importorskip("fontTools")
    from fontTools.fontBuilder import FontBuilder
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    p = tmp_path / "tiny.ttf"
    fb = FontBuilder(1024, isTTF=True)
    glyph_order = [".notdef", "A", "B"]
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap({ord("A"): "A", ord("B"): "B"})
    pen = TTGlyphPen(None)
    pen.moveTo((0, 0))
    pen.lineTo((500, 0))
    pen.lineTo((500, 500))
    pen.lineTo((0, 500))
    pen.closePath()
    glyph = pen.glyph()
    glyphs = {".notdef": glyph, "A": glyph, "B": glyph}
    fb.setupGlyf(glyphs)
    metrics = {name: (600, 0) for name in glyph_order}
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    fb.setupNameTable({"familyName": "Tiny", "styleName": "Regular"})
    fb.setupOS2(sTypoAscender=800, usWinAscent=800, usWinDescent=200)
    fb.setupPost()
    fb.save(str(p))
    return str(p)


# --- CAD fixtures ---


@pytest.fixture
def dxf_path(tmp_path) -> str:
    ezdxf = pytest.importorskip("ezdxf")
    p = tmp_path / "drawing.dxf"
    doc = ezdxf.new(dxfversion="R2010")
    msp = doc.modelspace()
    msp.add_line((0, 0), (10, 10))
    msp.add_circle((5, 5), 3)
    doc.layers.add(name="Walls")
    doc.saveas(str(p))
    return str(p)
