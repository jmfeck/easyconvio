import pypandoc

# AZW3 Conversions

def convert_azw3_to_epub(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".epub")
    pypandoc.convert_file(input_path, 'epub', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_azw3_to_fb2(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".fb2")
    pypandoc.convert_file(input_path, 'fb2', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_azw3_to_lrf(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".lrf")
    pypandoc.convert_file(input_path, 'lrf', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_azw3_to_mobi(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".mobi")
    pypandoc.convert_file(input_path, 'mobi', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_azw3_to_pdb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".pdb")
    pypandoc.convert_file(input_path, 'pdb', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_azw3_to_snb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".azw3", ".snb")
    pypandoc.convert_file(input_path, 'snb', format='azw3', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# EPUB Conversions

def convert_epub_to_azw3(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".azw3")
    pypandoc.convert_file(input_path, 'azw3', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_epub_to_fb2(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".fb2")
    pypandoc.convert_file(input_path, 'fb2', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_epub_to_lrf(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".lrf")
    pypandoc.convert_file(input_path, 'lrf', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_epub_to_mobi(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".mobi")
    pypandoc.convert_file(input_path, 'mobi', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_epub_to_pdb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".pdb")
    pypandoc.convert_file(input_path, 'pdb', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_epub_to_snb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".epub", ".snb")
    pypandoc.convert_file(input_path, 'snb', format='epub', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path


# FB2 Conversions

def convert_fb2_to_azw3(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".azw3")
    pypandoc.convert_file(input_path, 'azw3', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_fb2_to_epub(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".epub")
    pypandoc.convert_file(input_path, 'epub', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_fb2_to_lrf(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".lrf")
    pypandoc.convert_file(input_path, 'lrf', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_fb2_to_mobi(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".mobi")
    pypandoc.convert_file(input_path, 'mobi', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_fb2_to_pdb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".pdb")
    pypandoc.convert_file(input_path, 'pdb', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_fb2_to_snb(input_path, output_path=None):
    output_path = output_path or input_path.replace(".fb2", ".snb")
    pypandoc.convert_file(input_path, 'snb', format='fb2', outputfile=output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path
