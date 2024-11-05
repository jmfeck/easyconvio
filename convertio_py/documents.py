import pypandoc

def convert_to_pdf(input_path, output_path=None):
    output_path = output_path or input_path.replace(os.path.splitext(input_path)[1], ".pdf")
    pypandoc.convert_file(input_path, 'pdf', outputfile=output_path)
    return output_path

def convert_to_docx(input_path, output_path=None):
    output_path = output_path or input_path.replace(os.path.splitext(input_path)[1], ".docx")
    pypandoc.convert_file(input_path, 'docx', outputfile=output_path)
    return output_path