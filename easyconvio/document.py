import pypandoc

from .base import BaseFile


class DocumentFile(BaseFile):
    """Document file with conversion methods."""

    def _load(self):
        pass

    def _convert_to(self, fmt, output_path=None, **kwargs):
        output_path = self._output_path(fmt, output_path)
        pypandoc.convert_file(self.path, fmt, outputfile=output_path, **kwargs)
        return output_path

    def to_pdf(self, output_path=None, **kwargs):
        return self._convert_to("pdf", output_path, **kwargs)

    def to_docx(self, output_path=None, **kwargs):
        return self._convert_to("docx", output_path, **kwargs)

    def to_html(self, output_path=None, **kwargs):
        return self._convert_to("html", output_path, **kwargs)

    def to_md(self, output_path=None, **kwargs):
        return self._convert_to("md", output_path, **kwargs)

    def to_txt(self, output_path=None, **kwargs):
        return self._convert_to("plain", output_path, **kwargs)

    def to_odt(self, output_path=None, **kwargs):
        return self._convert_to("odt", output_path, **kwargs)

    def to_rtf(self, output_path=None, **kwargs):
        return self._convert_to("rtf", output_path, **kwargs)

    def to_latex(self, output_path=None, **kwargs):
        return self._convert_to("latex", output_path, **kwargs)

    def to_rst(self, output_path=None, **kwargs):
        return self._convert_to("rst", output_path, **kwargs)

    def to_asciidoc(self, output_path=None, **kwargs):
        return self._convert_to("asciidoc", output_path, **kwargs)

    def to_mediawiki(self, output_path=None, **kwargs):
        return self._convert_to("mediawiki", output_path, **kwargs)

    def to_org(self, output_path=None, **kwargs):
        return self._convert_to("org", output_path, **kwargs)

    def to_xml(self, output_path=None, **kwargs):
        return self._convert_to("docbook", output_path, **kwargs)

    def to_pptx(self, output_path=None, **kwargs):
        return self._convert_to("pptx", output_path, **kwargs)

    def to_epub(self, output_path=None, **kwargs):
        return self._convert_to("epub", output_path, **kwargs)
