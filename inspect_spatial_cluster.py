import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILE = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)

df = pd.read_csv(FILE)

# Convert numeric columns
for col in ["latitude", "longitude", "frp"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Reference point: center of the five Aqua detections
reference_lat = -1.3461
reference_lon = 103.9131

# Select detections on the same date and region
data = df[
    (df["study_region"] == "Riau_approx") &
    (df["acquisition_date"] == "2024-08-26")
].copy()

# Haversine distance in kilometers
lat1 = np.radians(reference_lat)
lon1 = np.radians(reference_lon)
lat2 = np.radians(data["latitude"])
lon2 = np.radians(data["longitude"])

dlat = lat2 - lat1
dlon = lon2 - lon1

a = (
    np.sin(dlat / 2) ** 2
    + np.cos(lat1) * np.cos(lat2)
    * np.sin(dlon / 2) ** 2
)

data["distance_km"] = (
    6371 * 2 * np.arcsin(np.sqrt(a))
)

# Select detections within 5 km
nearby = data[data["distance_km"] <= 5].copy()

print("\nSPATIAL CLUSTER INSPECTION")
print("Date: 2024-08-26")
print("Radius: 5 km")
print("Total nearby records:", len(nearby))

print("\nSUMMARY BY SATELLITE")

summary = (
    nearby.groupby("satellite")
    .agg(
        detection_records=("frp", "count"),
        mean_frp=("frp", "mean"),
        median_frp=("frp", "median"),
        maximum_frp=("frp", "max")
    )
    .round(2)
)

print(summary.to_string())

print("\nDETECTION DETAILS")

columns = [
    "satellite",
    "acquisition_time_hhmm",
    "latitude",
    "longitude",
    "distance_km",
    "frp",
    "confidence_raw",
    "confidence_scheme"
]

print(
    nearby[columns]
    .sort_values("distance_km")
    .to_string(index=False)
)

# Save results
output = (
    BASE_DIR / "data" / "processed"
    / "spatial_cluster_riau_20240826.csv"
)

nearby.to_csv(output, index=False)

print("\nSaved:", output)
