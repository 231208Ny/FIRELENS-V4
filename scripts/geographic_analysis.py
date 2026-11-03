"""
FIRELENS — Exploratory Geographic Analysis
Run from the FIRELENS project root:
    python scripts/geographic_analysis.py

Input:
    data/processed/fire_events_harmonized.csv

Outputs:
    data/processed/regional_detections_exploratory.csv
    data/processed/daily_activity_by_region_sensor.csv
    data/processed/regional_sensor_summary.csv
    data/processed/regional_summary_exploratory.csv
    data/processed/regional_sensor_comparison.png
    data/processed/daily_activity_trends.png

IMPORTANT:
The study areas below are approximate bounding boxes, NOT official province
boundaries. Do not report their counts as official provincial totals.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "processed" / "fire_events_harmonized.csv"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

REGIONS = {
    "Riau_approx": {
        "label": "Riau (approximate bounding box)",
        "lat_min": -1.5, "lat_max": 2.0,
        "lon_min": 100.0, "lon_max": 104.5,
    },
    "Central_Kalimantan_approx": {
        "label": "Central Kalimantan (approximate bounding box)",
        "lat_min": -3.5, "lat_max": -0.5,
        "lon_min": 110.0, "lon_max": 115.5,
    },
}

if not INPUT.exists():
    raise FileNotFoundError(
        f"Input not found: {INPUT}\n"
        "Place fire_events_harmonized.csv in data/processed/ first."
    )

df = pd.read_csv(INPUT)
required = {"latitude", "longitude", "acquisition_date", "sensor",
            "satellite", "frp", "detection_record_id"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Input is missing required columns: {sorted(missing)}")

parts = []
for key, cfg in REGIONS.items():
    mask = (
        df["latitude"].between(cfg["lat_min"], cfg["lat_max"]) &
        df["longitude"].between(cfg["lon_min"], cfg["lon_max"])
    )
    part = df.loc[mask].copy()
    part["study_region"] = key
    part["study_region_label"] = cfg["label"]
    parts.append(part)

regional = pd.concat(parts, ignore_index=True)
regional.to_csv(OUT / "regional_detections_exploratory.csv", index=False)

daily = (
    regional.groupby(["study_region", "acquisition_date", "sensor"], dropna=False)
    .size().reset_index(name="detection_records")
)
daily.to_csv(OUT / "daily_activity_by_region_sensor.csv", index=False)

sensor_summary = (
    regional.groupby(["study_region", "sensor", "satellite"], dropna=False)
    .size().reset_index(name="detection_records")
)
sensor_summary.to_csv(OUT / "regional_sensor_summary.csv", index=False)

region_summary = (
    regional.groupby(["study_region", "study_region_label"], dropna=False)
    .agg(
        detection_records=("detection_record_id", "count"),
        first_date=("acquisition_date", "min"),
        last_date=("acquisition_date", "max"),
        mean_frp=("frp", "mean"),
        median_frp=("frp", "median"),
    ).reset_index()
)
region_summary.to_csv(OUT / "regional_summary_exploratory.csv", index=False)

# Chart 1: total detection records by region and sensor.
pivot = regional.groupby(["study_region", "sensor"]).size().unstack(fill_value=0)
ax = pivot.plot(kind="bar", figsize=(9, 5))
ax.set_title("FIRELENS — Detection records by study area and sensor")
ax.set_xlabel("Exploratory study area")
ax.set_ylabel("Detection records")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig(OUT / "regional_sensor_comparison.png", dpi=180)
plt.close()

# Chart 2: daily detection records by region, with sensor lines.
for region, group in daily.groupby("study_region"):
    wide = group.pivot(index="acquisition_date", columns="sensor",
                       values="detection_records").fillna(0).sort_index()
    ax = wide.plot(figsize=(11, 5), marker=".", linewidth=1)
    ax.set_title(f"FIRELENS — Daily activity: {region}")
    ax.set_xlabel("Acquisition date")
    ax.set_ylabel("Detection records")
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    safe_name = region.lower()
    plt.savefig(OUT / f"daily_activity_{safe_name}.png", dpi=180)
    plt.close()

print("Geographic analysis completed.")
print(f"Input records: {len(df):,}")
print(f"Regional records: {len(regional):,}")
print("\nRegional summary:")
print(region_summary.to_string(index=False))
print("\nSensor summary:")
print(sensor_summary.to_string(index=False))
print(f"\nOutputs saved in: {OUT}")
