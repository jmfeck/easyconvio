# easyconvio

A universal file conversion and manipulation library for Python with a fluent API.

## Installation

```bash
pip install easyconvio
```

With optional extras:

```bash
pip install easyconvio[all]            # everything
pip install easyconvio[presentations]  # PowerPoint support
pip install easyconvio[vectors]        # SVG conversion via cairosvg
pip install easyconvio[fonts]          # font conversion via fonttools
pip install easyconvio[archives]       # 7z and RAR support
pip install easyconvio[cad]            # DXF support via ezdxf
```

## Usage

### Images

```python
import easyconvio as ec

img = ec.read_jpg("photo.jpg")
print(img)       # <ImageFile 'photo.jpg' (jpg)>
print(img.size)  # (1920, 1080)
print(img.mode)  # RGB

# Geometric transforms
img = img.resize(800, 600)
img = img.crop(0, 0, 400, 300)
img = img.rotate(90)
img = img.flip_horizontal()
img = img.thumbnail(200, 200)

# Color adjustments
img = ec.read_jpg("photo.jpg")
img = img.brightness(1.2)
img = img.contrast(1.5)
img = img.sharpness(2.0)
img = img.saturation(0.8)
img = img.grayscale()
img = img.sepia()
img = img.invert()
img = img.auto_contrast()
img = img.equalize()
img = img.opacity(0.5)

# Filters and compositing
img = ec.read_jpg("photo.jpg")
img = img.blur(radius=3)
img = img.add_border(10, color="red")
img = img.paste("overlay.png", 50, 50)

# Convert
img.to_png("photo.png")
img.to_webp("photo.webp", quality=80)
img.to("gif", "photo.gif")  # generic .to() also works
```

### Audio

```python
audio = ec.read_mp3("song.mp3")
print(audio.duration)     # 180.5 (seconds)
print(audio.channels)     # 2
print(audio.sample_rate)  # 44100

# Editing
audio = audio.trim(start=10, end=60)
audio = audio.append("outro.mp3")
audio = audio.overlay("effect.wav", position=5)
audio = audio.repeat(2)
audio = audio.reverse()
audio = audio.silence(3)

# Effects
audio = ec.read_mp3("song.mp3")
audio = audio.volume(6)
audio = audio.normalize()
audio = audio.fade_in(2)
audio = audio.fade_out(3)
audio = audio.low_pass_filter(3000)
audio = audio.high_pass_filter(200)
audio = audio.speed(1.5)

# Format settings
audio = audio.set_channels(1)  # mono
audio = audio.set_frame_rate(22050)

# Convert
audio.to_wav("song.wav")
audio.to_flac("song.flac")
audio.to("ogg", "song.ogg")
```

### Video

```python
video = ec.read_mp4("clip.mp4")
print(video.duration)  # 120.0 (seconds)
print(video.size)      # (1920, 1080)
print(video.fps)       # 30.0

# Editing
video = video.clip(0, 30)
video = video.resize(1280, 720)
video = video.crop(0, 0, 640, 360)
video = video.concatenate("clip2.mp4")
video = video.loop(3)

# Speed and time
video = ec.read_mp4("clip.mp4")
video = video.speed(2.0)
video = video.reverse()
video = video.set_fps(24)

# Visual effects
video = ec.read_mp4("clip.mp4")
video = video.rotate(90)
video = video.flip_horizontal()
video = video.grayscale()
video = video.brightness(1.3)
video = video.fade_in(2)
video = video.fade_out(2)

# Audio
video = ec.read_mp4("clip.mp4")
video = video.mute()
video = video.add_audio("music.mp3")
video = video.volume(0.5)

# Extract
video = ec.read_mp4("clip.mp4")
video.extract_audio("clip_audio.mp3")
video.snapshot(5.0, "frame_5s.png")

# Convert
video = ec.read_mp4("clip.mp4")
video.to_webm("clip.webm")
video.to("avi", "clip.avi")
```

### Documents

```python
doc = ec.read_docx("report.docx")
doc.to_pdf("report.pdf")
doc.to_html("report.html")
doc.to_md("report.md")
doc.to_latex("report.tex")
doc.to_rst("report.rst")
doc.to("odt", "report.odt")
```

### Ebooks

```python
ebook = ec.read_epub("book.epub")
ebook.to_mobi("book.mobi")
ebook.to_pdf("book.pdf")
ebook.to_html("book.html")
ebook.to("docx", "book.docx")
```

### Archives

```python
archive = ec.read_zip("files.zip")
print(archive.file_count)    # 42
print(archive.list_files())  # ['file1.txt', 'dir/file2.txt', ...]

archive.extract("output_dir/")
archive.extract_file("file1.txt", "output_dir/")

# Convert between archive formats
archive.to_tar("files.tar")
archive.to_gz("files.tar.gz")
archive.to_7z("files.7z")
archive.to("bz2", "files.tar.bz2")
```

### Presentations

```python
pres = ec.read_pptx("slides.pptx")
print(pres.slide_count)       # 15
print(pres.extract_text())    # ['Slide 1 text...', 'Slide 2 text...']

pres.extract_images("slides_images/")
pres = pres.remove_slide(0)

pres.to_pdf("slides.pdf")
pres.to_pptx("slides_copy.pptx")
pres.to("odp", "slides.odp")
```

### Vectors

```python
svg = ec.read_svg("logo.svg")
svg = svg.scale(2.0)

svg.to_png("logo.png")
svg.to_pdf("logo.pdf")
svg.to_eps("logo.eps")
svg.to("emf", "logo.emf")
```

### Fonts

```python
font = ec.read_ttf("font.ttf")
print(font.family_name)   # 'Roboto'
print(font.style)         # 'Regular'
print(font.glyph_count)   # 1294
print(font.info())

font = font.subset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
font.to_woff2("font_subset.woff2")
font.to_woff("font.woff")
font.to("otf", "font.otf")
```

### CAD

```python
cad = ec.read_dxf("drawing.dxf")
print(cad.layers)          # ['0', 'Walls', 'Doors', ...]
print(cad.entity_count)    # 256

cad.to_png("drawing.png", dpi=300)
cad.to_svg("drawing.svg")
cad.to_pdf("drawing.pdf")
```

## Supported Formats

| Category      | Formats                                                              |
|---------------|----------------------------------------------------------------------|
| Images        | jpg, png, gif, bmp, tiff, webp, ico, tga, ppm, pcx, dds, heic, heif |
| Audio         | mp3, wav, ogg, flac, aac, wma, m4a, aiff, ac3, opus, amr, au        |
| Video         | mp4, avi, mov, mkv, webm, flv, ogv, wmv, 3gp, ts, mpeg, mpg        |
| Documents     | pdf, docx, doc, odt, rtf, txt, html, md, latex, csv                  |
| Ebooks        | epub, mobi, azw3, fb2, lrf, pdb, snb                                |
| Archives      | zip, tar, gz, tgz, bz2, xz, 7z, rar                                |
| Presentations | pptx, ppt, odp                                                      |
| Vectors       | svg, eps, ai, wmf, emf, cdr                                         |
| Fonts         | ttf, otf, woff, woff2                                                |
| CAD           | dxf                                                                  |

## License

BSD 3-Clause
