"""
FIRELENS — NASA FIRMS MODIS + VIIRS harmonization
Run from the FIRELENS project root:
    python scripts/harmonize_firms.py

This standardizes shared fields but does NOT merge detections into unique fire
events or remove cross-sensor matches. Confidence schemes differ by sensor.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

REQUIRED = [
    "latitude", "longitude", "brightness", "scan", "track", "acq_date",
    "acq_time", "satellite", "instrument", "confidence", "version",
    "bright_t31", "frp", "daynight", "type"
]

def load_and_standardize(filename, sensor_name, product_name):
    path = RAW / filename
    df = pd.read_csv(path)
    missing = [col for col in REQUIRED if col not in df.columns]
    if missing:
        raise ValueError(f"{filename}: missing columns: {missing}")

    time_digits = (
        df["acq_time"].astype("string")
        .str.replace(r"\.0$", "", regex=True)
        .str.zfill(4)
    )

    out = pd.DataFrame({
        "latitude": pd.to_numeric(df["latitude"], errors="coerce"),
        "longitude": pd.to_numeric(df["longitude"], errors="coerce"),
        "acquisition_date": pd.to_datetime(df["acq_date"], errors="coerce").dt.strftime("%Y-%m-%d"),
        "acquisition_time_hhmm": time_digits.where(time_digits.str.fullmatch(r"\d{4}")),
        "sensor": sensor_name,
        "satellite": df["satellite"].astype("string"),
        "product": product_name,
        "brightness": pd.to_numeric(df["brightness"], errors="coerce"),
        "frp": pd.to_numeric(df["frp"], errors="coerce"),
        "scan": pd.to_numeric(df["scan"], errors="coerce"),
        "track": pd.to_numeric(df["track"], errors="coerce"),
        "bright_t31": pd.to_numeric(df["bright_t31"], errors="coerce"),
        "confidence_raw": df["confidence"].astype("string"),
        "confidence_scheme": "MODIS_numeric_0_100" if sensor_name == "MODIS" else "VIIRS_categorical_l_n_h",
        "daynight": df["daynight"].astype("string"),
        "type_code_raw": df["type"].astype("string"),
        "version": df["version"].astype("string"),
        "source_file": filename,
    })
    out.insert(
        0, "detection_record_id",
        sensor_name.lower() + "_" + pd.Series(range(1, len(out) + 1)).astype(str).str.zfill(7)
    )
    out["coordinate_valid"] = (
        out["latitude"].between(-90, 90) &
        out["longitude"].between(-180, 180)
    )
    duplicate_count = int(df.duplicated().sum())
    return out, duplicate_count

modis, modis_duplicates = load_and_standardize("modis.csv", "MODIS", "MODIS_C6.1")
viirs, viirs_duplicates = load_and_standardize("viirs.csv", "VIIRS", "J1_VIIRS_C2_375m")

combined = pd.concat([modis, viirs], ignore_index=True)
combined = combined.sort_values(
    ["acquisition_date", "acquisition_time_hhmm", "sensor", "satellite"],
    na_position="last"
).reset_index(drop=True)

# Do not deduplicate across sensors: a single event can be observed by both.
combined.to_csv(OUT / "fire_events_harmonized.csv", index=False)

quality = pd.DataFrame([
    {
        "sensor": "MODIS", "satellite": "Terra + Aqua", "product": "MODIS_C6.1",
        "records": len(modis), "missing_latitude": int(modis["latitude"].isna().sum()),
        "missing_longitude": int(modis["longitude"].isna().sum()),
        "invalid_coordinates": int((~modis["coordinate_valid"]).sum()),
        "missing_date": int(modis["acquisition_date"].isna().sum()),
        "duplicate_rows_in_source": modis_duplicates,
    },
    {
        "sensor": "VIIRS", "satellite": "N20", "product": "J1_VIIRS_C2_375m",
        "records": len(viirs), "missing_latitude": int(viirs["latitude"].isna().sum()),
        "missing_longitude": int(viirs["longitude"].isna().sum()),
        "invalid_coordinates": int((~viirs["coordinate_valid"]).sum()),
        "missing_date": int(viirs["acquisition_date"].isna().sum()),
        "duplicate_rows_in_source": viirs_duplicates,
    },
])
quality.to_csv(OUT / "data_quality_summary.csv", index=False)
print(f"Saved {len(combined):,} records to {OUT / 'fire_events_harmonized.csv'}")
print(quality.to_string(index=False))
