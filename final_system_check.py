from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent

files = [
    "app.py",
    "app_v2_backup.py",
    "pages/2_Geographic_Analysis.py",
    "pages/3_Advanced_Analytics.py",
    "pages/4_Data_Quality.py",
    "pages/5_Research_Insights.py",
]

print("=" * 50)
print("FIRELENS V3 SYSTEM CHECK")
print("=" * 50)

for file in files:
    status = "PASS" if (root / file).is_file() else "REVIEW"
    print(f"[{status}] {file}")

dataset = root / "data" / "processed" / "regional_detections_exploratory.csv"

if dataset.is_file():
    df = pd.read_csv(dataset)

    print("\n[PASS] Dataset ditemukan")
    print("Total records:", len(df))
    print("\nRegion distribution:")
    print(df["study_region_label"].value_counts())
    print("\nSensor distribution:")
    print(df["sensor"].value_counts())
    print("\nMissing values:", df.isna().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())

    report = pd.DataFrame({
        "column": df.columns,
        "missing_values": [
            df[col].isna().sum() for col in df.columns
        ]
    })

    report.to_csv(
        root / "FIRELENS_V3_system_test_report.csv",
        index=False
    )

    print("\n[PASS] System report berhasil dibuat")
else:
    print("\n[REVIEW] Dataset tidak ditemukan")

print("\nSYSTEM CHECK SELESAI")