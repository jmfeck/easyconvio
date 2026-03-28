from __future__ import annotations

from typing import Optional, Dict, Any

from .base import BaseFile


class FontFile(BaseFile):
    """Font file with conversion and inspection methods."""

    def _load(self) -> None:
        try:
            from fontTools.ttLib import TTFont
        except ImportError:
            raise ImportError(
                "FontFile requires fonttools. "
                "Install with: pip install easyconvio[fonts]"
            )
        self._font = TTFont(self.path)

    # --- Properties ---

    @property
    def family_name(self) -> Optional[str]:
        """Font family name (e.g. 'Roboto')."""
        name_table = self._font["name"]
        for record in name_table.names:
            if record.nameID == 1:
                return record.toUnicode()
        return None

    @property
    def style(self) -> Optional[str]:
        """Font style (e.g. 'Regular', 'Bold')."""
        name_table = self._font["name"]
        for record in name_table.names:
            if record.nameID == 2:
                return record.toUnicode()
        return None

    @property
    def glyph_count(self) -> int:
        """Number of glyphs in the font."""
        return len(self._font.getGlyphOrder())

    @property
    def units_per_em(self) -> int:
        """Units per em."""
        return self._font["head"].unitsPerEm

    # --- Operations ---

    def info(self) -> Dict[str, Any]:
        """Return a summary dict with font metadata."""
        return {
            "family_name": self.family_name,
            "style": self.style,
            "glyph_count": self.glyph_count,
            "units_per_em": self.units_per_em,
        }

    def subset(self, characters: str) -> FontFile:
        """Subset the font to only include glyphs for the given characters."""
        from fontTools import subset as ft_subset
        subsetter = ft_subset.Subsetter()
        subsetter.populate(text=characters)
        subsetter.subset(self._font)
        return self

    # --- Export ---

    def _save_with_flavor(self, flavor: Optional[str], output_path: str) -> str:
        self._font.flavor = flavor
        self._font.save(output_path)
        return output_path

    def to_ttf(self, output_path: Optional[str] = None) -> str:
        """Export as TrueType (.ttf)."""
        output_path = self._output_path("ttf", output_path)
        return self._save_with_flavor(None, output_path)

    def to_otf(self, output_path: Optional[str] = None) -> str:
        """Export as OpenType (.otf)."""
        output_path = self._output_path("otf", output_path)
        return self._save_with_flavor(None, output_path)

    def to_woff(self, output_path: Optional[str] = None) -> str:
        """Export as WOFF."""
        output_path = self._output_path("woff", output_path)
        return self._save_with_flavor("woff", output_path)

    def to_woff2(self, output_path: Optional[str] = None) -> str:
        """Export as WOFF2."""
        output_path = self._output_path("woff2", output_path)
        return self._save_with_flavor("woff2", output_path)
