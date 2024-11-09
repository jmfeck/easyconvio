import pandas as pd
import yaml

# CSV Conversions
def convert_csv_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".feather")
    df = pd.read_csv(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".csv", ".h5")
    df = pd.read_csv(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".json")
    df = pd.read_csv(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".orc")
    df = pd.read_csv(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".parquet")
    df = pd.read_csv(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".sas7bdat")
    df = pd.read_csv(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".sav")
    df = pd.read_csv(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".dta")
    df = pd.read_csv(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".xlsx")
    df = pd.read_csv(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".xml")
    df = pd.read_csv(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_csv_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".csv", ".yaml")
    df = pd.read_csv(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# Feather Conversions
def convert_feather_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".csv")
    df = pd.read_feather(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".feather", ".h5")
    df = pd.read_feather(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".json")
    df = pd.read_feather(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".orc")
    df = pd.read_feather(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".parquet")
    df = pd.read_feather(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".sas7bdat")
    df = pd.read_feather(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".sav")
    df = pd.read_feather(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".dta")
    df = pd.read_feather(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".xlsx")
    df = pd.read_feather(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".xml")
    df = pd.read_feather(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_feather_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".feather", ".yaml")
    df = pd.read_feather(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# HDF Conversions
def convert_hdf_to_csv(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".csv")
    df = pd.read_hdf(input_path, key=key)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_feather(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".feather")
    df = pd.read_hdf(input_path, key=key)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_json(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".json")
    df = pd.read_hdf(input_path, key=key)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_orc(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".orc")
    df = pd.read_hdf(input_path, key=key)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_parquet(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".parquet")
    df = pd.read_hdf(input_path, key=key)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_sas(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".sas7bdat")
    df = pd.read_hdf(input_path, key=key)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_spss(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".sav")
    df = pd.read_hdf(input_path, key=key)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_stata(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".dta")
    df = pd.read_hdf(input_path, key=key)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_xlsx(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".xlsx")
    df = pd.read_hdf(input_path, key=key)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_xml(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".xml")
    df = pd.read_hdf(input_path, key=key)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_hdf_to_yaml(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".h5", ".yaml")
    df = pd.read_hdf(input_path, key=key)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# JSON Conversions
def convert_json_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".csv")
    df = pd.read_json(input_path, lines=True)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".feather")
    df = pd.read_json(input_path, lines=True)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".json", ".h5")
    df = pd.read_json(input_path, lines=True)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".orc")
    df = pd.read_json(input_path, lines=True)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".parquet")
    df = pd.read_json(input_path, lines=True)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".sas7bdat")
    df = pd.read_json(input_path, lines=True)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".sav")
    df = pd.read_json(input_path, lines=True)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".dta")
    df = pd.read_json(input_path, lines=True)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".xlsx")
    df = pd.read_json(input_path, lines=True)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".xml")
    df = pd.read_json(input_path, lines=True)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_json_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".json", ".yaml")
    df = pd.read_json(input_path, lines=True)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# ORC Conversions
def convert_orc_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".csv")
    df = pd.read_orc(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".feather")
    df = pd.read_orc(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".orc", ".h5")
    df = pd.read_orc(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".json")
    df = pd.read_orc(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".parquet")
    df = pd.read_orc(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".sas7bdat")
    df = pd.read_orc(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".sav")
    df = pd.read_orc(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".dta")
    df = pd.read_orc(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".xlsx")
    df = pd.read_orc(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".xml")
    df = pd.read_orc(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_orc_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".orc", ".yaml")
    df = pd.read_orc(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# Parquet Conversions
def convert_parquet_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".csv")
    df = pd.read_parquet(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".feather")
    df = pd.read_parquet(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".parquet", ".h5")
    df = pd.read_parquet(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".json")
    df = pd.read_parquet(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".orc")
    df = pd.read_parquet(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".sas7bdat")
    df = pd.read_parquet(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".sav")
    df = pd.read_parquet(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".dta")
    df = pd.read_parquet(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".xlsx")
    df = pd.read_parquet(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".xml")
    df = pd.read_parquet(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_parquet_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".parquet", ".yaml")
    df = pd.read_parquet(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# SAS Conversions
def convert_sas_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".csv")
    df = pd.read_sas(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".feather")
    df = pd.read_sas(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".sas7bdat", ".h5")
    df = pd.read_sas(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".json")
    df = pd.read_sas(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".orc")
    df = pd.read_sas(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".parquet")
    df = pd.read_sas(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".sav")
    df = pd.read_sas(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".dta")
    df = pd.read_sas(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".xlsx")
    df = pd.read_sas(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".xml")
    df = pd.read_sas(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_sas_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sas7bdat", ".yaml")
    df = pd.read_sas(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# SPSS Conversions
def convert_spss_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".csv")
    df = pd.read_spss(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".feather")
    df = pd.read_spss(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".sav", ".h5")
    df = pd.read_spss(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".json")
    df = pd.read_spss(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".orc")
    df = pd.read_spss(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".parquet")
    df = pd.read_spss(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".sas7bdat")
    df = pd.read_spss(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".dta")
    df = pd.read_spss(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".xlsx")
    df = pd.read_spss(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".xml")
    df = pd.read_spss(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_spss_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".sav", ".yaml")
    df = pd.read_spss(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path


# Stata Conversions
def convert_stata_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".csv")
    df = pd.read_stata(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".feather")
    df = pd.read_stata(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".dta", ".h5")
    df = pd.read_stata(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".json")
    df = pd.read_stata(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".orc")
    df = pd.read_stata(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".parquet")
    df = pd.read_stata(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".sas7bdat")
    df = pd.read_stata(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".sav")
    df = pd.read_stata(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".xlsx")
    df = pd.read_stata(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".xml")
    df = pd.read_stata(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_stata_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".dta", ".yaml")
    df = pd.read_stata(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path


# XLSX Conversions
def convert_xlsx_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".csv")
    df = pd.read_excel(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".feather")
    df = pd.read_excel(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".xlsx", ".h5")
    df = pd.read_excel(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".json")
    df = pd.read_excel(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".orc")
    df = pd.read_excel(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".parquet")
    df = pd.read_excel(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".sas7bdat")
    df = pd.read_excel(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".sav")
    df = pd.read_excel(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".dta")
    df = pd.read_excel(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".xml")
    df = pd.read_excel(input_path)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xlsx_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xlsx", ".yaml")
    df = pd.read_excel(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path


# XML Conversions
def convert_xml_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".csv")
    df = pd.read_xml(input_path)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".feather")
    df = pd.read_xml(input_path)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".xml", ".h5")
    df = pd.read_xml(input_path)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".json")
    df = pd.read_xml(input_path)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".orc")
    df = pd.read_xml(input_path)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".parquet")
    df = pd.read_xml(input_path)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".sas7bdat")
    df = pd.read_xml(input_path)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".sav")
    df = pd.read_xml(input_path)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".dta")
    df = pd.read_xml(input_path)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".xlsx")
    df = pd.read_xml(input_path)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_xml_to_yaml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".xml", ".yaml")
    df = pd.read_xml(input_path)
    with open(output_path, 'w') as file:
        yaml.dump(df.to_dict(orient="records"), file)
    print(f"Converted {input_path} to {output_path}")
    return output_path

# YAML Conversions
def convert_yaml_to_csv(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".csv")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_feather(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".feather")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_feather(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_hdf(input_path, output_path=None, key='df'):
    output_path = output_path or input_path.replace(".yaml", ".h5")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_hdf(output_path, key=key, mode='w')
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_json(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".json")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_json(output_path, orient="records", lines=True)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_orc(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".orc")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_orc(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_parquet(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".parquet")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_parquet(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_sas(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".sas7bdat")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_sas(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_spss(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".sav")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_spss(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_stata(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".dta")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_stata(output_path)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_xlsx(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".xlsx")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path

def convert_yaml_to_xml(input_path, output_path=None):
    output_path = output_path or input_path.replace(".yaml", ".xml")
    with open(input_path, 'r') as file:
        data = yaml.safe_load(file)
    df = pd.DataFrame(data)
    df.to_xml(output_path, index=False)
    print(f"Converted {input_path} to {output_path}")
    return output_path
