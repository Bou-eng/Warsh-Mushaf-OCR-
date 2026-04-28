import json
import re
import sys
from pathlib import Path

SURAH_NAMES = [
    "001_al_fatihah", "002_al_bakarah", "003_al_imran", "004_al_nisa",
    "005_al_maida", "006_al_an'am", "007_al_araf", "008_al_anfal",
    "009_al_tawba", "010_yunus", "011_hud", "012_yusuf",
    "013_al_ra'd", "014_ibrahim", "015_al_hijr", "016_al_nahl",
    "017_al_israa", "018_al_kahf", "019_maryem", "020_taha",
    "021_al_anbiya", "022_al_hajj", "023_al_muminun", "024_al_nur",
    "025_al_furkan", "026_al_shu'ara", "027_al_naml", "028_al_qasas",
    "029_al_ankabut", "030_al_rum", "031_lukman", "032_al_sajda",
    "033_al_ahzab", "034_saba'", "035_fatir", "036_yasin",
    "037_al_saffat", "038_sad", "039_al_zumar", "040_gafir",
    "041_fussilet", "042_al_shura", "043_al_zukhruf", "044_al_dukhan",
    "045_al_jathiya", "046_al_ahkaf", "047_muhammed", "048_al_fetih",
    "049_al_hujurat", "050_kaf", "051_al_thariyat", "052_al_tour",
    "053_al_najm", "054_al_qamar", "055_al_rahman", "056_al_waqi'a",
    "057_al_hadid", "058_al_mujadele", "059_al_hashr", "060_al_mumtahina",
    "061_al_saf", "062_al_jumu'a", "063_al_munafikun", "064_al_tagabun",
    "065_al_talaq", "066_al_tahrim", "067_al_mulk", "068_nun",
    "069_al_hakka", "070_alma'arij", "071_nuh", "072_al_jinn",
    "073_al_muzzamil", "074_al_muddathir", "075_al_qiyamah", "076_al_insan",
    "077_al_mursalat", "078_al_naba'", "079_al_nazi'at", "080_abese",
    "081_al_takwir", "082_al_infitar", "083_al_mutaffifin", "084_al_inshikak",
    "085_al_buruj", "086_al_tariq", "087_al_a'la", "088_al_gashiya",
    "089_al_fajr", "090_al_balad", "091_al_shams", "092_al_leyl",
    "093_al_duha", "094_al_inshirah", "095_al_tin", "096_alaq",
    "097_al_qadr", "098_al_bayinah", "099_al_zalzalah", "100_al_adiyat",
    "101_al_qari'a", "102_al_takathur", "103_al_asr", "104_al_humaza",
    "105_al_fil", "106_quraysh", "107_al_ma'un", "108_al_kawthar",
    "109_al_kafirun", "110_al_nasr", "111_al_masad", "112_al_ikhlas",
    "113_al_falaq", "114_al_nas"
]

ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")

def convert_arabic_number(number_text):
    return int(number_text.translate(ARABIC_DIGITS))

def split_ayahs(input_path, output_folder):
    text = input_path.read_text(encoding="utf-8")

    pattern = re.compile(r"(.*?)[۝]\s*([٠-٩]+)", re.DOTALL)

    ayahs = []

    for match in pattern.finditer(text):
        ayah_text = match.group(1).strip()
        ayah_number = convert_arabic_number(match.group(2))

        ayahs.append({
            "ayah": ayah_number,
            "text": ayah_text
        })

    if not ayahs:
        print(f"❌ No ayahs found in: {input_path.name}")
        return

    output_path = output_folder / f"{input_path.stem}.json"

    output_path.write_text(
        json.dumps(ayahs, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"✅ {input_path.name} -> {output_path.name} | {len(ayahs)} ayahs")

def process_all_surahs(folder_path):
    input_folder = Path(folder_path)

    if not input_folder.exists():
        print("Folder does not exist.")
        return

    script_folder = Path(__file__).parent
    output_folder = script_folder / "json_output"
    output_folder.mkdir(exist_ok=True)

    for surah_name in SURAH_NAMES:
        txt_file = input_folder / f"{surah_name}.txt"

        if not txt_file.exists():
            print(f"⚠️ Missing file: {txt_file.name}")
            continue

        split_ayahs(txt_file, output_folder)

    print("\nDone.")
    print(f"JSON files saved in: {output_folder}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print('python split_all.py "/path/to/Warsh txts"')
        sys.exit(1)

    process_all_surahs(sys.argv[1])
