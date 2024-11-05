import pypandoc

def convert_to_epub(input_path, output_path=None):
    """
    Converts a document (e.g., PDF, DOCX) to EPUB format.
    """
    output_path = output_path or input_path.replace(".pdf", ".epub").replace(".docx", ".epub")
    pypandoc.convert_file(input_path, 'epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_to_pdf(input_path, output_path=None):
    """
    Converts an EPUB document to PDF format.
    """
    output_path = output_path or input_path.replace(".epub", ".pdf")
    pypandoc.convert_file(input_path, 'pdf', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_to_mobi(input_path, output_path=None):
    """
    Converts an EPUB document to MOBI format.
    """
    output_path = output_path or input_path.replace(".epub", ".mobi")
    pypandoc.convert_file(input_path, 'mobi', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path