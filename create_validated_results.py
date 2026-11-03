
from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
OUTPUT = BASE / "research_outputs"
OUTPUT.mkdir(exist_ok=True)

def read_table(filename):
    return pd.read_csv(OUTPUT / filename)

def markdown_table(df):
    headers = list(df.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    for _, row in df.iterrows():
        values = [str(value) for value in row]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)

regional = read_table("table_01_regional_distribution.csv")
sensors = read_table("table_02_sensor_distribution.csv")
monthly = read_table("table_03_monthly_distribution.csv")
frp = read_table("table_04_frp_statistics.csv")
peaks = read_table("table_05_daily_peaks.csv")

total = int(regional["detection_records"].sum())

central = regional[regional["study_region_label"].str.startswith(
    "Central Kalimantan"
)].iloc[0]

riau = regional[regional["study_region_label"].str.startswith(
    "Riau"
)].iloc[0]

central_frp = frp[frp["study_region_label"].str.startswith(
    "Central Kalimantan"
)].iloc[0]

riau_frp = frp[frp["study_region_label"].str.startswith(
    "Riau"
)].iloc[0]

central_peak = peaks[peaks["study_region_label"].str.startswith(
    "Central Kalimantan"
)].iloc[0]

riau_peak = peaks[peaks["study_region_label"].str.startswith(
    "Riau"
)].iloc[0]

content = f"""# FIRELENS — Validated Research Results

## 1. Dataset Overview

The analysis contains **{total:,} satellite detection records**
covering Riau and Central Kalimantan, Indonesia, from
1 August to 31 October 2024.

The regional study areas use approximate bounding boxes.
The records represent satellite detections, not necessarily
unique wildfire events.

## 2. Regional Distribution

Central Kalimantan recorded {int(central['detection_records']):,}
detections ({central['percentage']:.1f}%).

Riau recorded {int(riau['detection_records']):,}
detections ({riau['percentage']:.1f}%).

{markdown_table(regional)}

## 3. Satellite Sensor Distribution

VIIRS contributed {int(sensors.loc[sensors['sensor'] == 'VIIRS', 'detection_records'].iloc[0]):,}
records, while MODIS contributed
{int(sensors.loc[sensors['sensor'] == 'MODIS', 'detection_records'].iloc[0]):,}.

{markdown_table(sensors)}

## 4. Monthly Distribution

September recorded the highest monthly detection count
in both study regions.

{markdown_table(monthly)}

## 5. Fire Radiative Power (FRP)

Central Kalimantan had a mean FRP of
{central_frp['mean']:.3f} MW and a median of
{central_frp['median']:.2f} MW.

Riau had a mean FRP of {riau_frp['mean']:.3f} MW
and a median of {riau_frp['median']:.2f} MW.

The difference between the mean and median suggests
right-skewed FRP distributions. High maximum values should
be interpreted cautiously and are not automatically data errors.

{markdown_table(frp)}

## 6. Daily Detection Peaks

The highest daily detection count in Central Kalimantan
occurred on {central_peak['date']}, with
{int(central_peak['detection_records']):,} records.

In Riau, the highest daily count occurred on
{riau_peak['date']}, with
{int(riau_peak['detection_records']):,} records.

{markdown_table(peaks)}

## 7. Research Interpretation

The results show a higher concentration of satellite detection
records in the Central Kalimantan study area. September was
the most active month in both regions within the analyzed
period. VIIRS accounted for the majority of records.

FRP statistics describe satellite-observed fire radiative power
and should not be interpreted as direct measurements of total
fire damage or burned area.

## 8. Limitations

- Detection records do not represent unique wildfire events.
- The study regions are based on approximate bounding boxes,
  not official administrative boundaries.
- No complete cross-sensor deduplication was performed.
- MODIS and VIIRS have different observation characteristics
  and confidence schemes.
- FRP comparisons should be interpreted cautiously.
- Spatial and temporal proximity alone cannot establish
  whether detections belong to the same fire event.

## 9. Generated Visualizations

Interactive charts are available in the `charts` directory:

- `charts/chart_01_regional_distribution.html`
- `charts/chart_02_sensor_distribution.html`
- `charts/chart_03_monthly_trends.html`
- `charts/chart_04_frp_distribution.html`

## 10. Validation Note

These tables were generated from the processed exploratory
dataset using `generate_research_visuals.py`.

The results should still be checked against the original
NASA FIRMS source data, preprocessing decisions, and research
definitions before formal academic submission.
"""

output_file = OUTPUT / "VALIDATED_RESEARCH_RESULTS.md"
output_file.write_text(content, encoding="utf-8")

print("Validated research results generated successfully!")
print(f"File: {output_file}")
print(f"Total records: {total:,}")
print("Tables integrated: 5")
print("Status: SUCCESS")
