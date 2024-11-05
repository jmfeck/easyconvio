from PIL import Image
import pyheif

def convert_jpg_to_png(input_path, output_path=None):
    output_path = output_path or input_path.replace(".jpg", ".png")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "PNG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_png_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".png", ".jpg")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_jpg_to_gif(input_path, output_path=None):
    output_path = output_path or input_path.replace(".jpg", ".gif")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "GIF")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_gif_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".gif", ".jpg")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_bmp_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".bmp", ".jpg")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_tiff_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".tiff", ".jpg")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_jpg_to_tiff(input_path, output_path=None):
    output_path = output_path or input_path.replace(".jpg", ".tiff")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "TIFF")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_webp_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".webp", ".jpg")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_png_to_gif(input_path, output_path=None):
    output_path = output_path or input_path.replace(".png", ".gif")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "GIF")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_tiff_to_png(input_path, output_path=None):
    output_path = output_path or input_path.replace(".tiff", ".png")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "PNG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_heic_to_jpg(input_path, output_path=None):
    output_path = output_path or input_path.replace(".heic", ".jpg")
    heif_file = pyheif.read(input_path)
    img = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data, 
        "raw", 
        heif_file.mode, 
        heif_file.stride
    )
    img.convert("RGB").save(output_path, "JPEG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_heic_to_png(input_path, output_path=None):
    output_path = output_path or input_path.replace(".heic", ".png")
    heif_file = pyheif.read(input_path)
    img = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data, 
        "raw", 
        heif_file.mode, 
        heif_file.stride
    )
    img.convert("RGB").save(output_path, "PNG")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_jpg_to_heic(input_path, output_path=None):
    output_path = output_path or input_path.replace(".jpg", ".heic")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "HEIC")
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_png_to_heic(input_path, output_path=None):
    output_path = output_path or input_path.replace(".png", ".heic")
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, "HEIC")
    print(f"Converted {input_path} to {output_path}")
    return output_path

