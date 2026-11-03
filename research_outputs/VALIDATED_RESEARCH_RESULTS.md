# FIRELENS — Validated Research Results

## 1. Dataset Overview

The analysis contains **12,809 satellite detection records**
covering Riau and Central Kalimantan, Indonesia, from
1 August to 31 October 2024.

The regional study areas use approximate bounding boxes.
The records represent satellite detections, not necessarily
unique wildfire events.

## 2. Regional Distribution

Central Kalimantan recorded 10,030
detections (78.3%).

Riau recorded 2,779
detections (21.7%).

| study_region_label | detection_records | percentage |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 10030 | 78.3 |
| Riau (approximate bounding box) | 2779 | 21.7 |

## 3. Satellite Sensor Distribution

VIIRS contributed 10,109
records, while MODIS contributed
2,700.

| sensor | detection_records | percentage |
| --- | --- | --- |
| MODIS | 2700 | 21.08 |
| VIIRS | 10109 | 78.92 |

## 4. Monthly Distribution

September recorded the highest monthly detection count
in both study regions.

| study_region_label | month | detection_records |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 2024-08 | 1332 |
| Central Kalimantan (approximate bounding box) | 2024-09 | 6911 |
| Central Kalimantan (approximate bounding box) | 2024-10 | 1787 |
| Riau (approximate bounding box) | 2024-08 | 1054 |
| Riau (approximate bounding box) | 2024-09 | 687 |
| Riau (approximate bounding box) | 2024-10 | 1038 |

## 5. Fire Radiative Power (FRP)

Central Kalimantan had a mean FRP of
14.031 MW and a median of
8.09 MW.

Riau had a mean FRP of 11.095 MW
and a median of 5.43 MW.

The difference between the mean and median suggests
right-skewed FRP distributions. High maximum values should
be interpreted cautiously and are not automatically data errors.

| study_region_label | count | mean | median | std | minimum | maximum |
| --- | --- | --- | --- | --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 10030 | 14.031 | 8.09 | 19.602 | 0.19 | 463.0 |
| Riau (approximate bounding box) | 2779 | 11.095 | 5.43 | 26.325 | 0.14 | 479.2 |

## 6. Daily Detection Peaks

The highest daily detection count in Central Kalimantan
occurred on 2024-09-14, with
762 records.

In Riau, the highest daily count occurred on
2024-10-27, with
223 records.

| study_region_label | date | detection_records |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 2024-09-14 | 762 |
| Central Kalimantan (approximate bounding box) | 2024-09-03 | 758 |
| Central Kalimantan (approximate bounding box) | 2024-09-19 | 679 |
| Central Kalimantan (approximate bounding box) | 2024-09-17 | 569 |
| Central Kalimantan (approximate bounding box) | 2024-09-02 | 542 |
| Central Kalimantan (approximate bounding box) | 2024-09-04 | 490 |
| Central Kalimantan (approximate bounding box) | 2024-09-13 | 488 |
| Central Kalimantan (approximate bounding box) | 2024-09-16 | 456 |
| Central Kalimantan (approximate bounding box) | 2024-10-24 | 327 |
| Central Kalimantan (approximate bounding box) | 2024-09-12 | 312 |
| Riau (approximate bounding box) | 2024-10-27 | 223 |
| Riau (approximate bounding box) | 2024-09-07 | 156 |
| Riau (approximate bounding box) | 2024-10-26 | 139 |
| Riau (approximate bounding box) | 2024-10-28 | 138 |
| Riau (approximate bounding box) | 2024-08-19 | 128 |
| Riau (approximate bounding box) | 2024-10-22 | 108 |
| Riau (approximate bounding box) | 2024-09-08 | 83 |
| Riau (approximate bounding box) | 2024-08-27 | 78 |
| Riau (approximate bounding box) | 2024-09-03 | 78 |
| Riau (approximate bounding box) | 2024-08-05 | 75 |

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
