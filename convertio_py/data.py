import pandas as pd

def convert_data(input_path, from_format, to_format, output_path=None, key='df'):
    # Read the file based on `from_format`
    if from_format == "csv":
        df = pd.read_csv(input_path)
    elif from_format == "json":
        df = pd.read_json(input_path, lines=True)
    elif from_format == "xlsx":
        df = pd.read_excel(input_path)
    elif from_format == "parquet":
        df = pd.read_parquet(input_path)
    elif from_format == "xml":
        df = pd.read_xml(input_path)
    elif from_format == "yaml":
        import yaml
        with open(input_path, 'r') as file:
            data = yaml.safe_load(file)
        df = pd.DataFrame(data)
    elif from_format == "hdf":
        df = pd.read_hdf(input_path, key=key)
    elif from_format == "feather":
        df = pd.read_feather(input_path)
    elif from_format == "orc":
        df = pd.read_orc(input_path)
    elif from_format == "stata":
        df = pd.read_stata(input_path)
    elif from_format == "spss":
        df = pd.read_spss(input_path)
    elif from_format == "sas":
        df = pd.read_sas(input_path)
    else:
        raise ValueError(f"Unsupported input format: {from_format}")

    # Set the default output path if not provided
    output_path = output_path or input_path.replace(f".{from_format}", f".{to_format}")

    # Write the file based on `to_format`
    if to_format == "csv":
        df.to_csv(output_path, index=False)
    elif to_format == "json":
        df.to_json(output_path, orient="records", lines=True)
    elif to_format == "xlsx":
        df.to_excel(output_path, index=False)
    elif to_format == "parquet":
        df.to_parquet(output_path)
    elif to_format == "xml":
        df.to_xml(output_path, index=False)
    elif to_format == "yaml":
        import yaml
        with open(output_path, 'w') as file:
            yaml.dump(df.to_dict(orient="records"), file)
    elif to_format == "hdf":
        df.to_hdf(output_path, key=key, mode='w')
    elif to_format == "feather":
        df.to_feather(output_path)
    elif to_format == "orc":
        df.to_orc(output_path)
    elif to_format == "stata":
        df.to_stata(output_path)
    elif to_format == "spss":
        df.to_spss(output_path)
    elif to_format == "sas":
        df.to_sas(output_path)
    else:
        raise ValueError(f"Unsupported output format: {to_format}")

    print(f"Converted {input_path} from {from_format} to {to_format}")
    return output_path