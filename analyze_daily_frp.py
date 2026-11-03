import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = (
    BASE_DIR / "data" / "processed"
    / "regional_detections_exploratory.csv"
)
OUTPUT_DIR = BASE_DIR / "data" / "processed"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Prepare columns
df["acquisition_date"] = pd.to_datetime(
    df["acquisition_date"], errors="coerce"
)
df["frp"] = pd.to_numeric(df["frp"], errors="coerce")

df = df.dropna(
    subset=["acquisition_date", "frp", "study_region"]
)

# Calculate daily FRP statistics
daily_summary = (
    df.groupby(["study_region", "acquisition_date"])
    .agg(
        detection_records=("frp", "count"),
        mean_frp=("frp", "mean"),
        median_frp=("frp", "median"),
        total_frp=("frp", "sum")
    )
    .reset_index()
)

# Save daily summary
csv_path = OUTPUT_DIR / "daily_frp_temporal_summary.csv"
daily_summary.to_csv(csv_path, index=False)

regions = {
    "Central_Kalimantan_approx": "Central Kalimantan",
    "Riau_approx": "Riau"
}

# Generate daily FRP trend charts
for region_code, region_name in regions.items():

    regional_data = daily_summary[
        daily_summary["study_region"] == region_code
    ].sort_values("acquisition_date")

    plt.figure(figsize=(12, 6))

    plt.plot(
        regional_data["acquisition_date"],
        regional_data["mean_frp"],
        label="Daily Mean FRP",
        linewidth=1.5
    )

    plt.plot(
        regional_data["acquisition_date"],
        regional_data["median_frp"],
        label="Daily Median FRP",
        linewidth=1.5
    )

    plt.title(f"Daily FRP Trends - {region_name}")
    plt.xlabel("Date")
    plt.ylabel("Fire Radiative Power (MW)")

    plt.gca().xaxis.set_major_locator(
        mdates.MonthLocator()
    )
    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter("%b %Y")
    )

    plt.legend()
    plt.grid(alpha=0.25)
    plt.tight_layout()

    output_path = OUTPUT_DIR / (
        f"daily_frp_trend_{region_code}.png"
    )

    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Completed: {region_name}")

print("\nDaily FRP analysis completed.")
print("CSV:", csv_path)
print("Output folder:", OUTPUT_DIR)
