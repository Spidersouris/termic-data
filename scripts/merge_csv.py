#!/usr/bin/env python3

from argparse import ArgumentParser
import glob
import os

import pandas as pd

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("lang", help="language code for directory containing .csv files to merge")
    parser.add_argument("--csv-path", help="path to the dir containing the .csv files")
    parser.add_argument("--data-path", default="data/", help="path to where the merged csv will be written")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.csv_path is None:
        csv_path = os.path.join("csv_to_merge", args.lang)
    else:
        csv_path = args.csv_path
    csv_glob = os.path.join(csv_path, "*.csv")
    csv_files = glob.glob(csv_glob)

    if args.data_path is None:
        data_path = os.path.join("data", args.lang)
    else:
        data_path = os.path.join(args.data_path, args.lang)
    print(f"Writing merged CSV files to '{data_path}'")
    os.makedirs(data_path, exist_ok=True)


    try:
        for i, csv_file in enumerate(csv_files):
            print(f"Reading file {csv_file}… ({i+1}/{len(csv_files)})")

            df = pd.read_csv(csv_file, skiprows=13, delimiter=",", encoding="utf-8", on_bad_lines="warn")
            df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

            merged_path = os.path.join(data_path, f"merged_exc_{args.lang}.csv")
            df.to_csv(merged_path, mode="a", sep="\t", index=False)

            print(f"Parsed {csv_file} successfully.")
        else:
            raise SystemExit(f"No csv files found in '{csv_path}'")

    except (OSError, IOError) as e:
        print(f"{type(e).__name__}: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
