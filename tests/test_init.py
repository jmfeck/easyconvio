import pytest
from unittest.mock import patch, MagicMock

import easyconvio as ec
from easyconvio.image import ImageFile
from easyconvio.audio import AudioFile
from easyconvio.video import VideoFile
from easyconvio.document import DocumentFile
from easyconvio.ebook import EbookFile
from easyconvio.archive import ArchiveFile


@patch.object(ImageFile, "_load")
def test_read_jpg(mock_load):
    result = ec.read_jpg("photo.jpg")
    assert isinstance(result, ImageFile)


@patch.object(ImageFile, "_load")
def test_read_png(mock_load):
    result = ec.read_png("photo.png")
    assert isinstance(result, ImageFile)


@patch.object(ImageFile, "_load")
def test_read_webp(mock_load):
    result = ec.read_webp("photo.webp")
    assert isinstance(result, ImageFile)


@patch.object(AudioFile, "_load")
def test_read_mp3(mock_load):
    result = ec.read_mp3("song.mp3")
    assert isinstance(result, AudioFile)


@patch.object(AudioFile, "_load")
def test_read_wav(mock_load):
    result = ec.read_wav("song.wav")
    assert isinstance(result, AudioFile)


@patch.object(VideoFile, "_load")
def test_read_mp4(mock_load):
    result = ec.read_mp4("clip.mp4")
    assert isinstance(result, VideoFile)


@patch.object(DocumentFile, "_load")
def test_read_docx(mock_load):
    result = ec.read_docx("report.docx")
    assert isinstance(result, DocumentFile)


@patch.object(DocumentFile, "_load")
def test_read_pdf(mock_load):
    result = ec.read_pdf("report.pdf")
    assert isinstance(result, DocumentFile)


@patch.object(EbookFile, "_load")
def test_read_epub(mock_load):
    result = ec.read_epub("book.epub")
    assert isinstance(result, EbookFile)


@patch.object(ArchiveFile, "_load")
def test_read_zip(mock_load):
    result = ec.read_zip("files.zip")
    assert isinstance(result, ArchiveFile)
