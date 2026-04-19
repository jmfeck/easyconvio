# Changelog

## 1.0.0 (2026-04-18)

### Added
- **Spreadsheet module** — read/write XLSX, XLS, ODS, CSV, TSV via openpyxl/odfpy/xlrd, with multi-sheet manipulation (`add_sheet`, `rename_sheet`, `remove_sheet`, `iter_rows`).
- **HEIC/HEIF support** — register pillow-heif as a PIL plugin; `to_heic()` / `to_heif()` methods; new `[images]` extra.
- **JAR archives** — read and write Java `.jar` (zip-format) archives.
- **PPS/PPSX presentations** — `to_pps()` / `to_ppsx()` PowerPoint Show variants; non-PPTX formats (PPT/ODP) read via LibreOffice round-trip.
- **CSV document export** — `DocumentFile.to_csv()` for tabular sources.
- **Calibre integration** — `EbookFile.to_mobi()` and `to_azw3()` now correctly route to Calibre's `ebook-convert` (pandoc has no native MOBI/AZW3 writer).
- **`read_jar`, `read_xlsx`, `read_xls`, `read_ods`, `read_csv`, `read_tsv`, `read_pps`, `read_ppsx`, `read_heic`, `read_heif`** added to the public API.
- **Runtime dependency table** in README listing ffmpeg, pandoc, LibreOffice, Inkscape, and Calibre with install commands.
- **CI** now installs all runtime binaries on Ubuntu (ffmpeg, pandoc, libreoffice, inkscape, calibre, unrar, libheif).

### Fixed
- **CAD rendering** — `to_png/svg/pdf` used the removed `qfigure` API; now uses `ezdxf.addons.drawing.matplotlib.qsave`.
- **Audio export** — AAC, WMA, M4A, AMR, Opus exports were silently broken because pydub/ffmpeg need explicit muxer + codec for these. Format map now carries (muxer, codec) tuples; AMR auto-coerces to 8 kHz mono.

### Removed
- **Unimplementable formats dropped from the public API**: `read_ai`, `read_cdr` (proprietary, no Python writer); `read_lrf`, `read_pdb`, `read_snb` (dead ebook formats with no maintained writers); `to_rar` was never implemented (no Python lib writes RAR).
- README format table is now a Read/Write split — every cell reflects what actually works.

### Tests
- **Replaced ~120 mock-heavy tests with 199 real-file tests** using a shared `conftest.py` that synthesizes fixtures (HEIC, MP4 with audio, DOCX, ODS, TTF built via fontTools, DXF, etc.) via the same libraries production uses.
- Tests gracefully skip when an optional binary (LibreOffice, Inkscape, Calibre, pandoc) is missing.

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
