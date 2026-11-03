# FIRELENS – Final Analytical Synthesis

## 1. Research Overview

FIRELENS is an exploratory wildfire-detection analysis based on NASA FIRMS MODIS and VIIRS satellite detection records. This analysis focuses on two study areas in Indonesia: Riau and Central Kalimantan.

The observation period covers 1 August to 31 October 2024. The regional exploratory dataset contains 12,809 satellite detection records.

The study regions were defined using approximate geographic bounding boxes rather than official provincial boundaries.

## 2. Geographic Findings

Central Kalimantan recorded 10,030 satellite detections, while Riau recorded 2,779 detections.

These figures represent satellite detection records rather than unique wildfire events. Cross-sensor deduplication has not been performed.

## 3. Temporal Findings

Central Kalimantan recorded its highest monthly detection count in September 2024, with 6,911 records.

Riau recorded 1,054 detections in August, 687 in September, and 1,038 in October.

The highest daily detection count occurred on 14 September 2024 in Central Kalimantan, with 762 records. In Riau, the highest daily count occurred on 27 October 2024, with 223 records.

These patterns describe the temporal distribution of satellite observations and do not independently establish the causes of wildfire activity.

## 4. Fire Radiative Power Findings

The mean FRP was 14.03 for Central Kalimantan and 11.09 for Riau. The corresponding median FRP values were 8.09 and 5.43.

The FRP distributions were right-skewed, with some observations substantially higher than the central values.

MODIS Aqua had the highest mean FRP among the evaluated satellite groups in both study regions. VIIRS N20 contributed the largest number of detection records.

Differences in FRP across sensors should be interpreted cautiously because of differences in instrument characteristics, spatial resolution, observation timing, and detection sensitivity.

## 5. Sensor Analysis

VIIRS N20 contributed the majority of detection records in both regions.

The analysis also identified differences in FRP distributions among MODIS Aqua, MODIS Terra, and VIIRS N20.

These differences are descriptive findings and should not be interpreted as evidence of sensor accuracy or superiority.

## 6. Data Quality Assessment

A final data quality assessment was conducted on all 12,809 regional detection records.

Seven checks were performed:
- Duplicate detection IDs
- Geographic coordinate validity
- Missing FRP values
- Non-positive FRP values
- Acquisition date validity
- Acquisition time validity
- Sensor-satellite consistency

All seven checks passed, with zero flagged records.

No records were automatically removed.

## 7. Limitations

The analysis has several limitations:

1. Detection records do not necessarily represent unique wildfire events.
2. Cross-sensor deduplication has not been performed.
3. Study regions use approximate bounding boxes rather than official administrative boundaries.
4. MODIS and VIIRS confidence values use different confidence schemes and are not directly comparable.
5. FRP differences across sensors require cautious interpretation.
6. Statistical FRP outliers are not necessarily erroneous observations.
7. Spatial proximity and acquisition time alone cannot establish whether detections represent the same fire.

## 8. Overall Conclusion

The exploratory analysis identified distinct geographic, temporal, and FRP patterns in satellite fire detection records across Riau and Central Kalimantan during August–October 2024.

Central Kalimantan contributed a substantially larger number of detection records, with a pronounced peak in September. Riau showed a different monthly pattern, with higher detection counts in August and October.

The results demonstrate the analytical potential of combining MODIS and VIIRS detection records for exploratory wildfire monitoring. However, the findings should be interpreted as patterns in satellite observations rather than definitive measurements of unique wildfire events or official provincial fire totals.