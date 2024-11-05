from setuptools import setup, find_packages

setup(
    name="ConvertIOPy",
    version="0.1.0",
    description="A universal file conversion library for Python",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "Pillow", "pydub", "pypandoc", "moviepy", "ebooklib"
    ],
)