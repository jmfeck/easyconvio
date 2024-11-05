import pandas as pd
import json
import yaml

# CSV Conversions
def convert_csv_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".json")
    df = pd.read_csv(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".xml")
    df = pd.read_csv(input_path)
    with open(output_path, "w") as file:
        file.write(df.to_xml(root_name="data", row_name="record"))
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".yaml")
    df = pd.read_csv(input_path)
    data = df.to_dict(orient="records")
    with open(output_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_excel(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".xlsx")
    df = pd.read_csv(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".parquet")
    df = pd.read_csv(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".feather")
    df = pd.read_csv(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".dta")
    df = pd.read_csv(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

#validated until here
# JSON Conversions
def convert_json_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".csv")
    df = pd.read_json(input_path, lines=True)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".yaml")
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    with open(output_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_excel(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".xlsx")
    df = pd.read_json(input_path, lines=True)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".parquet")
    df = pd.read_json(input_path, lines=True)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# YAML Conversions
def convert_yaml_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".json")
    with open(input_path, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(output_path, "w") as json_file:
        json.dump(data, json_file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".csv")
    with open(input_path, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# XML Conversions
def convert_xml_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".csv")
    df = pd.read_xml(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".json")
    df = pd.read_xml(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# Parquet Conversions
def convert_parquet_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".csv")
    df = pd.read_parquet(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".json")
    df = pd.read_parquet(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path



def convert_json_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".csv")
    df = pd.read_json(input_path, lines=True)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path



def convert_excel_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".csv")
    df = pd.read_excel(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path



def convert_parquet_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".csv")
    df = pd.read_parquet(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path



def convert_xml_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".csv")
    df = pd.read_xml(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".yaml")
    with open(input_path, "r") as json_file:
        data = json.load(json_file)
    with open(output_path, "w") as yaml_file:
        yaml.dump(data, yaml_file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".json")
    with open(input_path, "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(output_path, "w") as json_file:
        json.dump(data, json_file)
    print(f"Converted {input_path} to {output_path}")
    return output_path



def convert_feather_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".csv")
    df = pd.read_feather(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path


def convert_stata_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".csv")
    df = pd.read_stata(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path