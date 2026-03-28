from setuptools import setup, find_packages

setup(
    name="easyconvio",
    version="0.2.0",
    description="A universal file conversion library for Python with a fluent API",
    author="Joao Feck",
    author_email="joaomfeck@gmail.com",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "pydub",
        "pypandoc",
        "moviepy",
    ],
    extras_require={
        "presentations": ["python-pptx"],
        "vectors": ["cairosvg"],
        "fonts": ["fonttools", "brotli"],
        "archives": ["py7zr", "rarfile"],
        "cad": ["ezdxf", "matplotlib"],
        "all": [
            "python-pptx",
            "cairosvg",
            "fonttools",
            "brotli",
            "py7zr",
            "rarfile",
            "ezdxf",
            "matplotlib",
        ],
    },
)
