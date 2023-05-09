import pandas as pd
import glob
import os

lang = "fr-FR" # Put your language code here
csv_files = glob.glob(f"../data/{lang}/*.csv")
xlsx_files = glob.glob(f"../data/{lang}/*.xlsx")

for csv_file in csv_files:
    csv_file = os.path.basename(csv_file)
    file_name = csv_file[:-4]
    if os.path.isfile(f"../feather/{file_name}.ft"):
        print(f"Existing feather file found for CSV {csv_file}: {file_name}.ft")
    else:
        df = pd.read_csv(f"../data/{lang}/{csv_file}", sep="\t")
        df.to_feather(f"../feather/{file_name}.ft")
        print(f"CSV {csv_file} successfully converted to feather file as {file_name}.ft")

for xlsx_file in xlsx_files:
    xlsx_file = os.path.basename(xlsx_file)
    file_name = xlsx_file[:-5]
    if os.path.isfile(f"../feather/{file_name}.ft"):
        print(f"Existing feather file found for XLSX {xlsx_file}: {file_name}.ft")
    else:
        df = pd.read_excel(f"../data/{lang}/{xlsx_file}")
        df.to_feather(f"../feather/{file_name}.ft")
        print(f"XLSX {xlsx_file} successfully converted to feather file as {file_name}.ft")