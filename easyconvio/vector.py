import os
import shutil
import subprocess

from .base import BaseFile


def _require_command(cmd, install_hint):
    if shutil.which(cmd) is None:
        raise RuntimeError(f"'{cmd}' not found. {install_hint}")


class VectorFile(BaseFile):
    """Vector graphics file with conversion methods."""

    def _load(self):
        self._is_svg = self.format in ("svg",)

    # --- Properties ---

    @property
    def is_svg(self):
        return self._is_svg

    # --- Manipulation (SVG only) ---

    def scale(self, factor):
        if not self._is_svg:
            raise NotImplementedError("scale() is only supported for SVG files")
        with open(self.path, "r") as f:
            content = f.read()
        import re
        width_match = re.search(r'width="([\d.]+)', content)
        height_match = re.search(r'height="([\d.]+)', content)
        if width_match:
            new_w = float(width_match.group(1)) * factor
            content = content.replace(
                f'width="{width_match.group(1)}',
                f'width="{new_w}',
            )
        if height_match:
            new_h = float(height_match.group(1)) * factor
            content = content.replace(
                f'height="{height_match.group(1)}',
                f'height="{new_h}',
            )
        with open(self.path, "w") as f:
            f.write(content)
        return self

    # --- Export via cairosvg (SVG input) ---

    def _cairosvg_convert(self, method_name, output_path):
        try:
            import cairosvg
        except ImportError:
            raise ImportError(
                "VectorFile requires cairosvg for SVG conversion. "
                "Install with: pip install cairosvg"
            )
        method = getattr(cairosvg, method_name)
        method(url=self.path, write_to=output_path)
        return output_path

    def _inkscape_convert(self, fmt, output_path):
        _require_command(
            "inkscape",
            "Install Inkscape for vector conversion: https://inkscape.org/",
        )
        subprocess.run(
            ["inkscape", self.path, "--export-type", fmt, "--export-filename", output_path],
            check=True,
            capture_output=True,
        )
        return output_path

    # --- Export ---

    def to_svg(self, output_path=None):
        output_path = self._output_path("svg", output_path)
        if self._is_svg:
            import shutil as sh
            sh.copy2(self.path, output_path)
        else:
            self._inkscape_convert("svg", output_path)
        return output_path

    def to_png(self, output_path=None, **kwargs):
        output_path = self._output_path("png", output_path)
        if self._is_svg:
            try:
                return self._cairosvg_convert("svg2png", output_path)
            except ImportError:
                return self._inkscape_convert("png", output_path)
        return self._inkscape_convert("png", output_path)

    def to_pdf(self, output_path=None):
        output_path = self._output_path("pdf", output_path)
        if self._is_svg:
            try:
                return self._cairosvg_convert("svg2pdf", output_path)
            except ImportError:
                return self._inkscape_convert("pdf", output_path)
        return self._inkscape_convert("pdf", output_path)

    def to_eps(self, output_path=None):
        output_path = self._output_path("eps", output_path)
        if self._is_svg:
            try:
                return self._cairosvg_convert("svg2ps", output_path)
            except ImportError:
                return self._inkscape_convert("eps", output_path)
        return self._inkscape_convert("eps", output_path)

    def to_emf(self, output_path=None):
        output_path = self._output_path("emf", output_path)
        return self._inkscape_convert("emf", output_path)

    def to_wmf(self, output_path=None):
        output_path = self._output_path("wmf", output_path)
        return self._inkscape_convert("wmf", output_path)

    def to_dxf(self, output_path=None):
        output_path = self._output_path("dxf", output_path)
        return self._inkscape_convert("dxf", output_path)
