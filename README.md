# Warsh-Mushaf-OCR-

Usage

This project provides two scripts to convert Warsh Qur’an text files into structured JSON format.
__________________________________________________________________________________________________________
1. Process a single surah

Use this if you want to process one file or fix errors manually:

python split_one_surah.py path/to/surah.txt

Splits ayahs using the ۝ separator

Extracts ayah numbers (Arabic digits → normal digits)

Outputs a .json file with the same name

____________________________________________________________________________________________________________
2. Process all surahs at once

Use this to convert the full dataset automatically:

python split_all.py path/to/folder

Expects all surah .txt files in the folder

Processes all 114 surahs in one run

Skips missing files and continues

Saves results in a json_output/ folder

!! Notes
The script preserves all original text exactly (harakat, imala, small letters, etc.)
If a surah fails during batch processing, you can process it individually using the first script
