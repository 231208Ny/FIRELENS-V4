import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILE = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)

df = pd.read_csv(FILE)

df["frp"] = pd.to_numeric(df["frp"], errors="coerce")

# Select high-FRP observations in Riau
selected = df[
    (df["study_region"] == "Riau_approx") &
    (df["acquisition_date"] == "2024-08-26") &
    (df["satellite"] == "Aqua")
].copy()

columns = [
    "acquisition_date",
    "acquisition_time_hhmm",
    "latitude",
    "longitude",
    "frp",
    "brightness",
    "bright_t31",
    "confidence_raw",
    "confidence_scheme",
    "daynight",
    "source_file"
]

print("\nEXTREME FRP RECORD INSPECTION")
print("Region: Riau")
print("Date: 2024-08-26")
print("Satellite: Aqua")
print("\nNumber of records:", len(selected))

print(
    selected[columns]
    .sort_values("frp", ascending=False)
    .to_string(index=False)
)

# Save inspection output
output_file = (
    BASE_DIR / "data" / "processed"
    / "extreme_frp_riau_aqua_20240826.csv"
)

selected[columns].to_csv(output_file, index=False)

print("\nInspection file saved:", output_file)
