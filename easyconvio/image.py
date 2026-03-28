from PIL import Image, ImageEnhance, ImageFilter, ImageOps

from .base import BaseFile


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
}


class ImageFile(BaseFile):
    """Image file with conversion and manipulation methods."""

    def _load(self):
        self._img = Image.open(self.path)

    # --- Properties ---

    @property
    def size(self):
        return self._img.size

    @property
    def width(self):
        return self._img.size[0]

    @property
    def height(self):
        return self._img.size[1]

    @property
    def mode(self):
        return self._img.mode

    # --- Geometric transforms ---

    def resize(self, width, height):
        self._img = self._img.resize((width, height))
        return self

    def crop(self, left, top, right, bottom):
        self._img = self._img.crop((left, top, right, bottom))
        return self

    def rotate(self, degrees):
        self._img = self._img.rotate(degrees, expand=True)
        return self

    def flip_horizontal(self):
        self._img = self._img.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def flip_vertical(self):
        self._img = self._img.transpose(Image.FLIP_TOP_BOTTOM)
        return self

    def thumbnail(self, max_width, max_height):
        self._img.thumbnail((max_width, max_height))
        return self

    # --- Color adjustments ---

    def grayscale(self):
        self._img = self._img.convert("L")
        return self

    def brightness(self, factor):
        self._img = ImageEnhance.Brightness(self._img).enhance(factor)
        return self

    def contrast(self, factor):
        self._img = ImageEnhance.Contrast(self._img).enhance(factor)
        return self

    def sharpness(self, factor):
        self._img = ImageEnhance.Sharpness(self._img).enhance(factor)
        return self

    def saturation(self, factor):
        self._img = ImageEnhance.Color(self._img).enhance(factor)
        return self

    def invert(self):
        self._img = ImageOps.invert(self._img.convert("RGB"))
        return self

    def auto_contrast(self):
        self._img = ImageOps.autocontrast(self._img)
        return self

    def equalize(self):
        self._img = ImageOps.equalize(self._img)
        return self

    def sepia(self):
        gray = self._img.convert("L")
        sepia_img = Image.merge("RGB", (
            gray.point(lambda x: min(int(x * 1.2), 255)),
            gray.point(lambda x: min(int(x * 1.0), 255)),
            gray.point(lambda x: min(int(x * 0.8), 255)),
        ))
        self._img = sepia_img
        return self

    def opacity(self, alpha):
        self._img = self._img.convert("RGBA")
        r, g, b, a = self._img.split()
        a = a.point(lambda x: int(x * alpha))
        self._img = Image.merge("RGBA", (r, g, b, a))
        return self

    # --- Filters ---

    def blur(self, radius=2):
        self._img = self._img.filter(ImageFilter.GaussianBlur(radius))
        return self

    # --- Compositing ---

    def paste(self, other_path, x, y):
        other = Image.open(other_path)
        self._img.paste(other, (x, y))
        return self

    def add_border(self, width, color="black"):
        self._img = ImageOps.expand(self._img, border=width, fill=color)
        return self

    # --- Export ---

    def _save_as(self, pil_format, output_path=None, **kwargs):
        ext = pil_format.lower()
        if ext == "jpeg":
            ext = "jpg"
        output_path = self._output_path(ext, output_path)
        img = self._img.convert("RGB") if pil_format in ("JPEG", "BMP") else self._img
        img.save(output_path, pil_format, **kwargs)
        return output_path

    def to_jpg(self, output_path=None, **kwargs):
        return self._save_as("JPEG", output_path, **kwargs)

    def to_png(self, output_path=None, **kwargs):
        return self._save_as("PNG", output_path, **kwargs)

    def to_gif(self, output_path=None, **kwargs):
        return self._save_as("GIF", output_path, **kwargs)

    def to_bmp(self, output_path=None, **kwargs):
        return self._save_as("BMP", output_path, **kwargs)

    def to_tiff(self, output_path=None, **kwargs):
        return self._save_as("TIFF", output_path, **kwargs)

    def to_webp(self, output_path=None, **kwargs):
        return self._save_as("WEBP", output_path, **kwargs)

    def to_ico(self, output_path=None, **kwargs):
        return self._save_as("ICO", output_path, **kwargs)

    def to_tga(self, output_path=None, **kwargs):
        return self._save_as("TGA", output_path, **kwargs)

    def to_ppm(self, output_path=None, **kwargs):
        return self._save_as("PPM", output_path, **kwargs)

    def to_pcx(self, output_path=None, **kwargs):
        return self._save_as("PCX", output_path, **kwargs)

    def to_dds(self, output_path=None, **kwargs):
        return self._save_as("DDS", output_path, **kwargs)

    def save(self, output_path=None, **kwargs):
        output_path = output_path or self.path
        pil_format = PIL_FORMAT_MAP.get(self.format, self.format.upper())
        self._img.save(output_path, pil_format, **kwargs)
        return output_path
