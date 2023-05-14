# termic-data

This repository contains Microsoft's translation memory and glossary files used by [termic](https://github.com/Spidersouris/termic). Check the termic repo for more information on data collection.

## Structure

- **/csv_to_merge**: seperate .csv translation memory files for each language,
- **/data**: merged .csv translation memory files (see merge_csv.py) and .xslx glossary files for each language,
- **/feather**: examples of pandas feather file (for local data),
- **/scripts**:
  - **convert_to_feather.py**: use this script to convert .csv and .xlsx files to the [feather format](https://arrow.apache.org/docs/python/feather.html),
  - **merge_csv.py**: use this script to merge the .csv files in the **csv_to_merge** folder into one .csv file.
