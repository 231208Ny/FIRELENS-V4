
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "processed" / "regional_detections_exploratory.csv"

required_files = [
    "app.py",
    "app_v2_backup.py",
    "pages/2_Geographic_Analysis.py",
    "pages/3_Advanced_Analytics.py",
    "pages/4_Data_Quality.py",
    "pages/5_Research_Insights.py",
]

print("=" * 55)
print("FIRELENS V3 - SYSTEM CHECK")
print("=" * 55)

passed = 0
review = 0

for filename in required_files:
    exists = (ROOT / filename).is_file()
    print(f"[{'PASS' if exists else 'REVIEW'}] {filename}")
    passed += int(exists)
    review += int(not exists)

print("\n[DATASET CHECK]")

if DATA.is_file():
    try:
        df = pd.read_csv(DATA)
        print("[PASS] Dataset ditemukan dan berhasil dibaca")
        print(f"[INFO] Total records: {len(df):,}")

        required_columns = [
            "study_region_label",
            "sensor",
            "acquisition_date",
            "latitude",
            "longitude",
            "frp",
        ]

        missing = [c for c in required_columns if c not in df.columns]

        if not missing:
            print("[PASS] Semua kolom wajib tersedia")
            passed += 1
        else:
            print("[REVIEW] Kolom tidak ditemukan:", missing)
            review += 1

        print("\n[REGION DISTRIBUTION]")
        print(df["study_region_label"].value_counts(dropna=False))

        print("\n[SENSOR DISTRIBUTION]")
        print(df["sensor"].value_counts(dropna=False))

        print("\n[DATE RANGE]")
        dates = pd.to_datetime(
            df["acquisition_date"], errors="coerce"
        )
        print("Start:", dates.min())
        print("End:", dates.max())

        print("\n[DATA QUALITY]")
        print("Missing values:", int(df.isna().sum().sum()))
        print("Exact duplicate rows:", int(df.duplicated().sum()))

        report = pd.DataFrame({
            "column": df.columns,
            "missing_values": [
                int(df[col].isna().sum()) for col in df.columns
            ],
        })
        report.to_csv(
            ROOT / "FIRELENS_V3_system_test_report.csv",
            index=False
        )
        print("\n[PASS] System test report berhasil dibuat")
        passed += 1

    except Exception as e:
        print("[REVIEW] Dataset gagal diproses:", e)
        review += 1
else:
    print("[REVIEW] Dataset tidak ditemukan:", DATA)
    review += 1

print("\n" + "=" * 55)
print("FINAL SUMMARY")
print("=" * 55)
print("PASS:", passed)
print("REVIEW:", review)
print("Pemeriksaan selesai. Tidak ada data yang dihapus.")
