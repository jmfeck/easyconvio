from __future__ import annotations

from typing import Optional, Any, Tuple

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

from .base import BaseFile


_HEIF_REGISTERED = False


def _ensure_heif_support() -> None:
    """Register pillow-heif as a PIL plugin so Image.open accepts HEIC/HEIF."""
    global _HEIF_REGISTERED
    if _HEIF_REGISTERED:
        return
    try:
        from pillow_heif import register_heif_opener
    except ImportError:
        raise ImportError(
            "HEIC/HEIF support requires pillow-heif. "
            "Install with: pip install easyconvio[images]"
        )
    register_heif_opener()
    _HEIF_REGISTERED = True


PIL_FORMAT_MAP = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "bmp": "BMP",
    "tiff": "TIFF",
    "tif": "TIFF",
    "webp": "WEBP",
    "ico": "ICO",
    "ppm": "PPM",
    "pgm": "PPM",
    "pbm": "PPM",
    "tga": "TGA",
    "pcx": "PCX",
    "dds": "DDS",
    "heic": "HEIF",
    "heif": "HEIF",
}


class ImageFile(BaseFile):
    """Image file with conversion and manipulation methods."""

    def _load(self) -> None:
        if self.format in ("heic", "heif"):
            _ensure_heif_support()
        self._img = Image.open(self.path)

    # --- Properties ---

    @property
    def size(self) -> Tuple[int, int]:
        """Width and height in pixels."""
        return self._img.size

    @property
    def width(self) -> int:
        """Width in pixels."""
        return self._img.size[0]

    @property
    def height(self) -> int:
        """Height in pixels."""
        return self._img.size[1]

    @property
    def mode(self) -> str:
        """Color mode (e.g. RGB, RGBA, L)."""
        return self._img.mode

    # --- Geometric transforms ---

    def resize(self, width: int, height: int) -> ImageFile:
        """Resize to exact dimensions."""
        self._img = self._img.resize((width, height))
        return self

    def crop(self, left: int, top: int, right: int, bottom: int) -> ImageFile:
        """Crop to the given bounding box."""
        self._img = self._img.crop((left, top, right, bottom))
        return self

    def rotate(self, degrees: float) -> ImageFile:
        """Rotate by the given degrees (counterclockwise)."""
        self._img = self._img.rotate(degrees, expand=True)
        return self

    def flip_horizontal(self) -> ImageFile:
        """Mirror horizontally."""
        self._img = self._img.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def flip_vertical(self) -> ImageFile:
        """Mirror vertically."""
        self._img = self._img.transpose(Image.FLIP_TOP_BOTTOM)
        return self

    def thumbnail(self, max_width: int, max_height: int) -> ImageFile:
        """Resize to fit within the given bounds, preserving aspect ratio."""
        self._img.thumbnail((max_width, max_height))
        return self

    # --- Color adjustments ---

    def grayscale(self) -> ImageFile:
        """Convert to grayscale."""
        self._img = self._img.convert("L")
        return self

    def brightness(self, factor: float) -> ImageFile:
        """Adjust brightness. 1.0 = original, >1 brighter, <1 darker."""
        self._img = ImageEnhance.Brightness(self._img).enhance(factor)
        return self

    def contrast(self, factor: float) -> ImageFile:
        """Adjust contrast. 1.0 = original."""
        self._img = ImageEnhance.Contrast(self._img).enhance(factor)
        return self

    def sharpness(self, factor: float) -> ImageFile:
        """Adjust sharpness. 1.0 = original."""
        self._img = ImageEnhance.Sharpness(self._img).enhance(factor)
        return self

    def saturation(self, factor: float) -> ImageFile:
        """Adjust color saturation. 1.0 = original, 0 = grayscale."""
        self._img = ImageEnhance.Color(self._img).enhance(factor)
        return self

    def invert(self) -> ImageFile:
        """Invert all colors."""
        self._img = ImageOps.invert(self._img.convert("RGB"))
        return self

    def auto_contrast(self) -> ImageFile:
        """Normalize contrast by stretching the histogram."""
        self._img = ImageOps.autocontrast(self._img)
        return self

    def equalize(self) -> ImageFile:
        """Equalize the image histogram."""
        self._img = ImageOps.equalize(self._img)
        return self

    def sepia(self) -> ImageFile:
        """Apply a sepia tone filter."""
        gray = self._img.convert("L")
        sepia_img = Image.merge("RGB", (
            gray.point(lambda x: min(int(x * 1.2), 255)),
            gray.point(lambda x: min(int(x * 1.0), 255)),
            gray.point(lambda x: min(int(x * 0.8), 255)),
        ))
        self._img = sepia_img
        return self

    def opacity(self, alpha: float) -> ImageFile:
        """Set opacity. 1.0 = fully opaque, 0.0 = fully transparent."""
        self._img = self._img.convert("RGBA")
        r, g, b, a = self._img.split()
        a = a.point(lambda x: int(x * alpha))
        self._img = Image.merge("RGBA", (r, g, b, a))
        return self

    # --- Filters ---

    def blur(self, radius: float = 2) -> ImageFile:
        """Apply Gaussian blur."""
        self._img = self._img.filter(ImageFilter.GaussianBlur(radius))
        return self

    # --- Compositing ---

    def paste(self, other_path: str, x: int, y: int) -> ImageFile:
        """Paste another image on top at the given position."""
        other = Image.open(other_path)
        self._img.paste(other, (x, y))
        return self

    def add_border(self, width: int, color: str = "black") -> ImageFile:
        """Add a solid-color border around the image."""
        self._img = ImageOps.expand(self._img, border=width, fill=color)
        return self

    # --- Export ---

    def _save_as(
        self,
        pil_format: str,
        output_path: Optional[str] = None,
        ext: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        if ext is None:
            ext = pil_format.lower()
            if ext == "jpeg":
                ext = "jpg"
        output_path = self._output_path(ext, output_path)
        if pil_format == "HEIF":
            _ensure_heif_support()
        img = self._img.convert("RGB") if pil_format in ("JPEG", "BMP") else self._img
        img.save(output_path, pil_format, **kwargs)
        return output_path

    def to_jpg(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as JPEG."""
        return self._save_as("JPEG", output_path, **kwargs)

    def to_png(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PNG."""
        return self._save_as("PNG", output_path, **kwargs)

    def to_gif(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as GIF."""
        return self._save_as("GIF", output_path, **kwargs)

    def to_bmp(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as BMP."""
        return self._save_as("BMP", output_path, **kwargs)

    def to_tiff(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as TIFF."""
        return self._save_as("TIFF", output_path, **kwargs)

    def to_webp(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as WebP."""
        return self._save_as("WEBP", output_path, **kwargs)

    def to_ico(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as ICO."""
        return self._save_as("ICO", output_path, **kwargs)

    def to_tga(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as TGA."""
        return self._save_as("TGA", output_path, **kwargs)

    def to_ppm(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PPM."""
        return self._save_as("PPM", output_path, **kwargs)

    def to_pcx(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as PCX."""
        return self._save_as("PCX", output_path, **kwargs)

    def to_dds(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as DDS."""
        return self._save_as("DDS", output_path, **kwargs)

    def to_heic(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as HEIC. Requires pillow-heif (pip install easyconvio[images])."""
        return self._save_as("HEIF", output_path, ext="heic", **kwargs)

    def to_heif(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Export as HEIF. Requires pillow-heif (pip install easyconvio[images])."""
        return self._save_as("HEIF", output_path, ext="heif", **kwargs)

    def save(self, output_path: Optional[str] = None, **kwargs: Any) -> str:
        """Save in the original format."""
        output_path = output_path or self.path
        pil_format = PIL_FORMAT_MAP.get(self.format, self.format.upper())
        self._img.save(output_path, pil_format, **kwargs)
        return output_path
