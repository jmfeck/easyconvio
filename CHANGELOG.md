# Changelog

## 0.3.0 (2026-03-28)

- Type hints on all public methods
- Docstrings on all public methods
- Lazy imports — `import easyconvio` no longer loads all dependencies eagerly
- Context manager support (`with ec.read_mp4("x") as video:`)
- `py.typed` marker (PEP 561)
- Clear error messages for missing external tools (ffmpeg, LibreOffice, Inkscape) and optional packages
- 134 tests covering all modules
- CI/CD with GitHub Actions (tests on Ubuntu + Windows, auto-publish on release)
- Target Python 3.13+
- Full moviepy 2.x compatibility (PascalCase effects API)

## 0.2.2 (2026-03-28)

- Fix project URLs in package metadata

## 0.2.1 (2026-03-28)

- New README with full usage examples
- Replace `setup.py` with `pyproject.toml`
- Fix moviepy 2.x import (`moviepy.editor` -> `moviepy`)

## 0.2.0 (2026-03-28)

- Full rewrite with fluent API (`ec.read_jpg("x").resize(800,600).to_png("y")`)
- Rename package from `convertio_py` to `easyconvio`
- 10 file categories: images, audio, video, documents, ebooks, archives, presentations, vectors, fonts, CAD
- Optional extras for heavy dependencies (presentations, vectors, fonts, archives, cad)

## 0.1.0

- Initial release as `convertio_py`
- Basic document and ebook conversion
