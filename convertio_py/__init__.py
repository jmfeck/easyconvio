import os

# Importing conversion functions from each module
from .images import *
from .audio import *
from .video import *
from .documents import *
from .ebooks import *

def convert(input_path, target_format, output_path=None):
    """
    Main conversion function that routes to the correct module and conversion function
    based on the target format.
    """
    ext = os.path.splitext(input_path)[1].lower()
    
    # Image conversions
    if target_format == "png":
        return convert_to_png(input_path, output_path)
    elif target_format == "jpg":
        return convert_to_jpg(input_path, output_path)
    elif target_format == "webp":
        return convert_to_webp(input_path, output_path)
    
    # Audio conversions
    elif target_format == "mp3":
        return convert_to_mp3(input_path, output_path)
    elif target_format == "wav":
        return convert_to_wav(input_path, output_path)
    
    # Video conversions
    elif target_format == "mp4":
        return convert_to_mp4(input_path, output_path)
    elif target_format == "avi":
        return convert_to_avi(input_path, output_path)
    elif target_format == "webm":
        return convert_to_webm(input_path, output_path)
    
    # Document conversions
    elif target_format == "pdf":
        return convert_to_pdf(input_path, output_path)
    elif target_format == "docx":
        return convert_to_docx(input_path, output_path)
    
    # eBook conversions
    elif target_format == "epub":
        return convert_to_epub(input_path, output_path)
    elif target_format == "mobi":
        return convert_to_mobi(input_path, output_path)
    
    else:
        raise ValueError(f"Conversion to {target_format} is not supported.")
