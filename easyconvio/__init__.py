from .image import ImageFile
from .audio import AudioFile
from .video import VideoFile
from .document import DocumentFile
from .ebook import EbookFile
from .archive import ArchiveFile
from .presentation import PresentationFile
from .vector import VectorFile
from .font import FontFile
from .cad import CADFile


# ============================================================
# Image readers
# ============================================================

def read_jpg(path):
    return ImageFile(path)

def read_jpeg(path):
    return ImageFile(path)

def read_png(path):
    return ImageFile(path)

def read_gif(path):
    return ImageFile(path)

def read_bmp(path):
    return ImageFile(path)

def read_tiff(path):
    return ImageFile(path)

def read_tif(path):
    return ImageFile(path)

def read_webp(path):
    return ImageFile(path)

def read_ico(path):
    return ImageFile(path)

def read_tga(path):
    return ImageFile(path)

def read_ppm(path):
    return ImageFile(path)

def read_pcx(path):
    return ImageFile(path)

def read_dds(path):
    return ImageFile(path)

def read_heic(path):
    return ImageFile(path)

def read_heif(path):
    return ImageFile(path)


# ============================================================
# Audio readers
# ============================================================

def read_mp3(path):
    return AudioFile(path)

def read_wav(path):
    return AudioFile(path)

def read_ogg(path):
    return AudioFile(path)

def read_flac(path):
    return AudioFile(path)

def read_aac(path):
    return AudioFile(path)

def read_wma(path):
    return AudioFile(path)

def read_m4a(path):
    return AudioFile(path)

def read_aiff(path):
    return AudioFile(path)

def read_ac3(path):
    return AudioFile(path)

def read_opus(path):
    return AudioFile(path)

def read_amr(path):
    return AudioFile(path)

def read_au(path):
    return AudioFile(path)


# ============================================================
# Video readers
# ============================================================

def read_mp4(path):
    return VideoFile(path)

def read_avi(path):
    return VideoFile(path)

def read_mov(path):
    return VideoFile(path)

def read_mkv(path):
    return VideoFile(path)

def read_webm(path):
    return VideoFile(path)

def read_flv(path):
    return VideoFile(path)

def read_ogv(path):
    return VideoFile(path)

def read_wmv(path):
    return VideoFile(path)

def read_3gp(path):
    return VideoFile(path)

def read_ts(path):
    return VideoFile(path)

def read_mpeg(path):
    return VideoFile(path)

def read_mpg(path):
    return VideoFile(path)


# ============================================================
# Document readers
# ============================================================

def read_pdf(path):
    return DocumentFile(path)

def read_docx(path):
    return DocumentFile(path)

def read_doc(path):
    return DocumentFile(path)

def read_odt(path):
    return DocumentFile(path)

def read_rtf(path):
    return DocumentFile(path)

def read_txt(path):
    return DocumentFile(path)

def read_html(path):
    return DocumentFile(path)

def read_md(path):
    return DocumentFile(path)

def read_latex(path):
    return DocumentFile(path)

def read_csv(path):
    return DocumentFile(path)


# ============================================================
# Ebook readers
# ============================================================

def read_epub(path):
    return EbookFile(path)

def read_mobi(path):
    return EbookFile(path)

def read_azw3(path):
    return EbookFile(path)

def read_fb2(path):
    return EbookFile(path)

def read_lrf(path):
    return EbookFile(path)

def read_pdb(path):
    return EbookFile(path)

def read_snb(path):
    return EbookFile(path)


# ============================================================
# Archive readers
# ============================================================

def read_zip(path):
    return ArchiveFile(path)

def read_tar(path):
    return ArchiveFile(path)

def read_gz(path):
    return ArchiveFile(path)

def read_tgz(path):
    return ArchiveFile(path)

def read_bz2(path):
    return ArchiveFile(path)

def read_xz(path):
    return ArchiveFile(path)

def read_7z(path):
    return ArchiveFile(path)

def read_rar(path):
    return ArchiveFile(path)


# ============================================================
# Presentation readers
# ============================================================

def read_pptx(path):
    return PresentationFile(path)

def read_ppt(path):
    return PresentationFile(path)

def read_odp(path):
    return PresentationFile(path)


# ============================================================
# Vector readers
# ============================================================

def read_svg(path):
    return VectorFile(path)

def read_eps(path):
    return VectorFile(path)

def read_ai(path):
    return VectorFile(path)

def read_wmf(path):
    return VectorFile(path)

def read_emf(path):
    return VectorFile(path)

def read_cdr(path):
    return VectorFile(path)


# ============================================================
# Font readers
# ============================================================

def read_ttf(path):
    return FontFile(path)

def read_otf(path):
    return FontFile(path)

def read_woff(path):
    return FontFile(path)

def read_woff2(path):
    return FontFile(path)


# ============================================================
# CAD readers
# ============================================================

def read_dxf(path):
    return CADFile(path)
