import os

def validate_file(input_path, supported_formats):
    ext = os.path.splitext(input_path)[1].lower()
    if ext not in supported_formats:
        raise ValueError(f"Unsupported file format: {ext}")
    return True