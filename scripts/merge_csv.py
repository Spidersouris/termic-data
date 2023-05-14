import pandas as pd
import glob

lang = "fr-FR" # Put your language code here
csv_files = glob.glob(f"../csv_to_merge/{lang}/*.csv")

for i, csv_file in enumerate(csv_files):
    print(f"Reading file {csv_file}… ({i+1}/{len(csv_files)})")
    try:
        df = pd.read_csv(csv_file, skiprows=13, delimiter=",", encoding="utf-8", on_bad_lines="warn")
        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
        df.to_csv(f"../data/{lang}/merged_exc_{lang}.csv", mode="a", sep="\t", index=False)
    except Exception as e:
        print(e)
        raise
    print(f"File {csv_file} has been read successfully.")