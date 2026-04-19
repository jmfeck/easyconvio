from __future__ import annotations

import shutil
import subprocess
from typing import Optional, Any

import pypandoc

from .base import BaseFile


def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def _ebook_convert(src: str, dst: str) -> str:
    if not _have("ebook-convert"):
        raise RuntimeError(
            "MOBI/AZW3 conversion requires Calibre's 'ebook-convert'. "
            "Install Calibre: https://calibre-ebook.com/download"
        )
    subprocess.run(["ebook-convert", src, dst], check=True, capture_output=True)
    return dst


class EbookFile(BaseFile):
    """Ebook file with conversion methods.

    EPUB, HTML, TXT, DOCX, FB2 conversions go through pandoc. MOBI and AZW3
    are not supported by pandoc — they require Calibre's ebook-convert.
    """

    def _load(self) -> None:
        pass

    def _convert_to(self, fmt: str, output_path: Optional[str] = None, **kwargs: Any) -> str:
        output_path = self._output_path(fmt, output_path)
        pypandoc.convert_file(self.path, fmt, outputfile=output_path, **kwargs)
        return output_path

    def to_epub(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as EPUB (via pandoc)."""
        return self._convert_to("epub", output_path, **kwargs)

    def to_fb2(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as FB2 (via pandoc)."""
        return self._convert_to("fb2", output_path, **kwargs)

    def to_pdf(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PDF (via pandoc; requires a PDF engine)."""
        return self._convert_to("pdf", output_path, **kwargs)

    def to_html(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as HTML (via pandoc)."""
        return self._convert_to("html", output_path, **kwargs)

    def to_txt(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as plain text (via pandoc)."""
        return self._convert_to("plain", output_path, **kwargs)

    def to_docx(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as DOCX (via pandoc)."""
        return self._convert_to("docx", output_path, **kwargs)

    def to_mobi(self, output_path: Optional[str] = None) -> str:
        """Export as MOBI (requires Calibre's ebook-convert)."""
        output_path = self._output_path("mobi", output_path)
        return _ebook_convert(self.path, output_path)

    def to_azw3(self, output_path: Optional[str] = None) -> str:
        """Export as AZW3 (requires Calibre's ebook-convert)."""
        output_path = self._output_path("azw3", output_path)
        return _ebook_convert(self.path, output_path)
