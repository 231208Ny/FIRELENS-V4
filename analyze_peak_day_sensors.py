import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)

df = pd.read_csv(FILE)

df["acquisition_date"] = pd.to_datetime(
    df["acquisition_date"], errors="coerce"
)

df["frp"] = pd.to_numeric(
    df["frp"], errors="coerce"
)

peak_dates = [
    ("Central_Kalimantan_approx", "2024-09-14"),
    ("Central_Kalimantan_approx", "2024-08-06"),
    ("Central_Kalimantan_approx", "2024-10-15"),
    ("Riau_approx", "2024-10-27"),
    ("Riau_approx", "2024-08-26")
]

for region, date in peak_dates:

    selected = df[
        (df["study_region"] == region) &
        (df["acquisition_date"] == pd.Timestamp(date))
    ].copy()

    print("\n====================================")
    print("REGION:", region)
    print("DATE:", date)
    print("====================================")

    summary = (
        selected.groupby("satellite")
        .agg(
            detection_records=("frp", "count"),
            mean_frp=("frp", "mean"),
            median_frp=("frp", "median"),
            total_frp=("frp", "sum"),
            maximum_frp=("frp", "max")
        )
        .round(2)
    )

    print(summary.to_string())

    print("\nTotal records:", len(selected))
