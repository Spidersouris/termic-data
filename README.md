# termic-data

> **Warning** <br>
> **This repo has been archived as termic data is now stored on [Dropbox](https://www.dropbox.com/sh/5oh21rhlmrp7rip/AAB_F2Q9wboJlopMZVTMKD5Ya?dl=0). Scripts are now available in the main [termic](https://github.com/Spidersouris/termic) repo.**

___

This repository contained Microsoft's translation memory and glossary files used by [termic](https://github.com/Spidersouris/termic). Check the termic repo for more information on data collection.

## Structure

- **/csv_to_merge**: seperate .csv translation memory files for each language,
- **/data**: merged .csv translation memory files (see merge_csv.py) and .xslx glossary files for each language,
- **/feather**: examples of pandas feather file (for local data),
- **/scripts**:
  - **convert_to_feather.py**: use this script to convert .csv and .xlsx files to the [feather format](https://arrow.apache.org/docs/python/feather.html),
  - **merge_csv.py**: use this script to merge the .csv files in the **csv_to_merge** folder into one .csv file.

## Usage

_NOTE_: was written specifically for `merge_csv.py`.

Set up a virtualenv:

```
mkdir -p ~/.cache/virtualenvs
python3 -m venv ~/.cache/virtualenvs/termic-data
source ~/.cache/virtualenvs/termic-data/bin/activate
python3 -m pip install -r ./scripts/requirements.txt
```

## Contributors

- [benediktkr](https://github.com/benediktkr)
