"""easyconvio - Simple file conversion and transformation for Python."""


def __getattr__(name):
    """Lazy-load reader functions only when accessed."""
    _READERS = {
        # Image
        "read_jpg": ".image", "read_jpeg": ".image", "read_png": ".image",
        "read_gif": ".image", "read_bmp": ".image", "read_tiff": ".image",
        "read_tif": ".image", "read_webp": ".image", "read_ico": ".image",
        "read_tga": ".image", "read_ppm": ".image", "read_pcx": ".image",
        "read_dds": ".image", "read_heic": ".image", "read_heif": ".image",
        # Audio
        "read_mp3": ".audio", "read_wav": ".audio", "read_ogg": ".audio",
        "read_flac": ".audio", "read_aac": ".audio", "read_wma": ".audio",
        "read_m4a": ".audio", "read_aiff": ".audio", "read_ac3": ".audio",
        "read_opus": ".audio", "read_amr": ".audio", "read_au": ".audio",
        # Video
        "read_mp4": ".video", "read_avi": ".video", "read_mov": ".video",
        "read_mkv": ".video", "read_webm": ".video", "read_flv": ".video",
        "read_ogv": ".video", "read_wmv": ".video", "read_3gp": ".video",
        "read_ts": ".video", "read_mpeg": ".video", "read_mpg": ".video",
        # Document
        "read_pdf": ".document", "read_docx": ".document", "read_doc": ".document",
        "read_odt": ".document", "read_rtf": ".document", "read_txt": ".document",
        "read_html": ".document", "read_md": ".document", "read_latex": ".document",
        # Ebook
        "read_epub": ".ebook", "read_mobi": ".ebook", "read_azw3": ".ebook",
        "read_fb2": ".ebook",
        # Archive
        "read_zip": ".archive", "read_jar": ".archive", "read_tar": ".archive",
        "read_gz": ".archive", "read_tgz": ".archive", "read_bz2": ".archive",
        "read_xz": ".archive", "read_7z": ".archive", "read_rar": ".archive",
        # Presentation
        "read_pptx": ".presentation", "read_ppt": ".presentation",
        "read_odp": ".presentation", "read_pps": ".presentation",
        "read_ppsx": ".presentation",
        # Spreadsheet
        "read_xlsx": ".spreadsheet", "read_xls": ".spreadsheet",
        "read_ods": ".spreadsheet", "read_csv": ".spreadsheet",
        "read_tsv": ".spreadsheet",
        # Vector
        "read_svg": ".vector", "read_eps": ".vector",
        "read_wmf": ".vector", "read_emf": ".vector",
        # Font
        "read_ttf": ".font", "read_otf": ".font", "read_woff": ".font",
        "read_woff2": ".font",
        # CAD
        "read_dxf": ".cad",
    }

    _CLASSES = {
        "ImageFile": ".image", "AudioFile": ".audio", "VideoFile": ".video",
        "DocumentFile": ".document", "EbookFile": ".ebook",
        "ArchiveFile": ".archive", "PresentationFile": ".presentation",
        "SpreadsheetFile": ".spreadsheet",
        "VectorFile": ".vector", "FontFile": ".font", "CADFile": ".cad",
    }

    if name in _READERS:
        module_path = _READERS[name]
        import importlib
        mod = importlib.import_module(module_path, __name__)
        cls_name = mod.__all__[0] if hasattr(mod, "__all__") else None

        # Map module to file class
        _MOD_CLASS = {
            ".image": "ImageFile", ".audio": "AudioFile", ".video": "VideoFile",
            ".document": "DocumentFile", ".ebook": "EbookFile",
            ".archive": "ArchiveFile", ".presentation": "PresentationFile",
            ".spreadsheet": "SpreadsheetFile",
            ".vector": "VectorFile", ".font": "FontFile", ".cad": "CADFile",
        }
        cls = getattr(mod, _MOD_CLASS[module_path])

        def reader(path, _cls=cls):
            return _cls(path)

        reader.__name__ = name
        reader.__qualname__ = name
        globals()[name] = reader
        return reader

    if name in _CLASSES:
        import importlib
        mod = importlib.import_module(_CLASSES[name], __name__)
        cls = getattr(mod, name)
        globals()[name] = cls
        return cls

    raise AttributeError(f"module 'easyconvio' has no attribute {name!r}")


__all__ = [
    # Classes
    "ImageFile", "AudioFile", "VideoFile", "DocumentFile", "EbookFile",
    "ArchiveFile", "PresentationFile", "SpreadsheetFile",
    "VectorFile", "FontFile", "CADFile",
    # Image readers
    "read_jpg", "read_jpeg", "read_png", "read_gif", "read_bmp", "read_tiff",
    "read_tif", "read_webp", "read_ico", "read_tga", "read_ppm", "read_pcx",
    "read_dds", "read_heic", "read_heif",
    # Audio readers
    "read_mp3", "read_wav", "read_ogg", "read_flac", "read_aac", "read_wma",
    "read_m4a", "read_aiff", "read_ac3", "read_opus", "read_amr", "read_au",
    # Video readers
    "read_mp4", "read_avi", "read_mov", "read_mkv", "read_webm", "read_flv",
    "read_ogv", "read_wmv", "read_3gp", "read_ts", "read_mpeg", "read_mpg",
    # Document readers
    "read_pdf", "read_docx", "read_doc", "read_odt", "read_rtf", "read_txt",
    "read_html", "read_md", "read_latex",
    # Ebook readers
    "read_epub", "read_mobi", "read_azw3", "read_fb2",
    # Archive readers
    "read_zip", "read_jar", "read_tar", "read_gz", "read_tgz", "read_bz2",
    "read_xz", "read_7z", "read_rar",
    # Presentation readers
    "read_pptx", "read_ppt", "read_odp", "read_pps", "read_ppsx",
    # Spreadsheet readers
    "read_xlsx", "read_xls", "read_ods", "read_csv", "read_tsv",
    # Vector readers
    "read_svg", "read_eps", "read_wmf", "read_emf",
    # Font readers
    "read_ttf", "read_otf", "read_woff", "read_woff2",
    # CAD readers
    "read_dxf",
]
