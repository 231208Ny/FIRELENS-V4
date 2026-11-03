import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "regional_detections_exploratory.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

# Load data
df = pd.read_csv(DATA_FILE)

# Satellite order and region labels
satellites = ["Aqua", "Terra", "N20"]

regions = {
    "Central_Kalimantan_approx": "Central Kalimantan",
    "Riau_approx": "Riau"
}

# Ensure FRP is numeric
df["frp"] = pd.to_numeric(df["frp"], errors="coerce")
df = df.dropna(subset=["frp"])

# Create one histogram and one boxplot for each region
for region_code, region_name in regions.items():

    regional_data = df[df["study_region"] == region_code]

    # Histogram
    plt.figure(figsize=(10, 6))

    for satellite in satellites:
        values = regional_data.loc[
            regional_data["satellite"] == satellite, "frp"
        ]

        if not values.empty:
            plt.hist(
                values,
                bins=40,
                alpha=0.45,
                label=satellite
            )

    plt.title(f"FRP Distribution - {region_name}")
    plt.xlabel("Fire Radiative Power (MW)")
    plt.ylabel("Detection Records")
    plt.legend(title="Satellite")
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()

    histogram_path = OUTPUT_DIR / (
        f"frp_histogram_{region_code}.png"
    )
    plt.savefig(histogram_path, dpi=300)
    plt.close()

    # Boxplot
    box_data = [
        regional_data.loc[
            regional_data["satellite"] == satellite, "frp"
        ].dropna()
        for satellite in satellites
    ]

    plt.figure(figsize=(9, 6))

    plt.boxplot(
        box_data,
        tick_labels=satellites,
        showfliers=True
    )

    plt.title(f"FRP Boxplot - {region_name}")
    plt.xlabel("Satellite")
    plt.ylabel("Fire Radiative Power (MW)")
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()

    boxplot_path = OUTPUT_DIR / (
        f"frp_boxplot_{region_code}.png"
    )
    plt.savefig(boxplot_path, dpi=300)
    plt.close()

    print(f"Completed visualization for {region_name}")

print("\nAll FRP visualizations completed.")
print(f"Output folder: {OUTPUT_DIR}")

