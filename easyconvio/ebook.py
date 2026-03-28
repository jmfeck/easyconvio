from __future__ import annotations

from typing import Optional, Any

import pypandoc

from .base import BaseFile


class EbookFile(BaseFile):
    """Ebook file with conversion methods via pandoc."""

    def _load(self) -> None:
        pass

    def _convert_to(self, fmt: str, output_path: Optional[str] = None, **kwargs: Any) -> str:
        output_path = self._output_path(fmt, output_path)
        pypandoc.convert_file(self.path, fmt, outputfile=output_path, **kwargs)
        return output_path

    def to_epub(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as EPUB."""
        return self._convert_to("epub", output_path, **kwargs)

    def to_mobi(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as MOBI."""
        return self._convert_to("mobi", output_path, **kwargs)

    def to_azw3(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as AZW3."""
        return self._convert_to("azw3", output_path, **kwargs)

    def to_fb2(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as FB2."""
        return self._convert_to("fb2", output_path, **kwargs)

    def to_pdf(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PDF."""
        return self._convert_to("pdf", output_path, **kwargs)

    def to_html(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as HTML."""
        return self._convert_to("html", output_path, **kwargs)

    def to_txt(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as plain text."""
        return self._convert_to("plain", output_path, **kwargs)

    def to_docx(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as DOCX."""
        return self._convert_to("docx", output_path, **kwargs)
