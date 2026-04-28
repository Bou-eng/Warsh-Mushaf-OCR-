import json
import re
from pathlib import Path
import sys

ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

def convert_arabic_number(number_text):
    return int(number_text.translate(ARABIC_DIGITS))

def split_ayahs(input_file):
    input_path = Path(input_file)

    text = input_path.read_text(encoding="utf-8")

    # Output will be created inside the script/project folder
    script_folder = Path(__file__).parent
    output_path = script_folder / f"{input_path.stem}.json"

    # Matches: ayah text + ۝ + ayah number
    pattern = re.compile(r"(.*?)[۝]\s*([٠-٩]+)", re.DOTALL)

    ayahs = []
    last_end = 0

    for match in pattern.finditer(text):
        ayah_text = match.group(1).strip()
        ayah_number = convert_arabic_number(match.group(2))

        ayahs.append({
            "ayah": ayah_number,
            "text": ayah_text
        })

        last_end = match.end()

    if not ayahs:
        print("No ayahs found.")
        print("Make sure the ayah separator looks like this: ۝١")
        return

    output_path.write_text(
        json.dumps(ayahs, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Created JSON: {output_path}")
    print(f"Total ayahs: {len(ayahs)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("python split_one_surah.py path/to/surah.txt")
        sys.exit(1)

    split_ayahs(sys.argv[1])
