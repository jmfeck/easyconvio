# Changelog

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
