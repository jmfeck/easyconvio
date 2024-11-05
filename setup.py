from setuptools import setup, find_packages

setup(
    name="convertio-py",
    version="0.1.0",
    description="A universal file conversion library for Python",
    author="Joao Feck",
    author_email="joaomfeck@gmail.com",
    description="A generic library for file conversion",

    packages=find_packages(),
    install_requires=[
        "Pillow", "pydub", "pypandoc", "moviepy", "ebooklib"
    ]
    
)