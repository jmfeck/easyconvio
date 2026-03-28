import os
import subprocess
import shutil

from .base import BaseFile


def _require_command(cmd, install_hint):
    if shutil.which(cmd) is None:
        raise RuntimeError(f"'{cmd}' not found. {install_hint}")


class PresentationFile(BaseFile):
    """Presentation file with manipulation and conversion methods."""

    def _load(self):
        try:
            from pptx import Presentation
            self._prs = Presentation(self.path)
        except ImportError:
            raise ImportError(
                "PresentationFile requires python-pptx. "
                "Install with: pip install python-pptx"
            )

    # --- Properties ---

    @property
    def slide_count(self):
        return len(self._prs.slides)

    @property
    def slide_width(self):
        return self._prs.slide_width

    @property
    def slide_height(self):
        return self._prs.slide_height

    # --- Operations ---

    def extract_text(self):
        texts = []
        for slide in self._prs.slides:
            slide_text = []
            for shape in slide.shapes:
                if shape.has_text_frame:
                    for paragraph in shape.text_frame.paragraphs:
                        slide_text.append(paragraph.text)
            texts.append("\n".join(slide_text))
        return texts

    def extract_images(self, output_dir="."):
        os.makedirs(output_dir, exist_ok=True)
        paths = []
        img_count = 0
        for slide in self._prs.slides:
            for shape in slide.shapes:
                if shape.shape_type == 13:  # Picture
                    img = shape.image
                    ext = img.content_type.split("/")[-1]
                    img_count += 1
                    filename = f"image_{img_count}.{ext}"
                    filepath = os.path.join(output_dir, filename)
                    with open(filepath, "wb") as f:
                        f.write(img.blob)
                    paths.append(filepath)
        return paths

    def remove_slide(self, index):
        rId = self._prs.slides._sldIdLst[index].rId
        self._prs.part.drop_rel(rId)
        del self._prs.slides._sldIdLst[index]
        return self

    # --- Export ---

    def to_pptx(self, output_path=None):
        output_path = self._output_path("pptx", output_path)
        self._prs.save(output_path)
        return output_path

    def _libreoffice_convert(self, fmt, output_path=None):
        _require_command(
            "libreoffice",
            "Install LibreOffice for document conversion: https://www.libreoffice.org/",
        )
        output_path = self._output_path(fmt, output_path)
        out_dir = os.path.dirname(os.path.abspath(output_path))
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", fmt, "--outdir", out_dir, self.path],
            check=True,
            capture_output=True,
        )
        base = os.path.splitext(os.path.basename(self.path))[0]
        generated = os.path.join(out_dir, f"{base}.{fmt}")
        if generated != os.path.abspath(output_path):
            os.rename(generated, output_path)
        return output_path

    def to_pdf(self, output_path=None):
        return self._libreoffice_convert("pdf", output_path)

    def to_odp(self, output_path=None):
        return self._libreoffice_convert("odp", output_path)

    def to_ppt(self, output_path=None):
        return self._libreoffice_convert("ppt", output_path)

    def to_html(self, output_path=None):
        return self._libreoffice_convert("html", output_path)
