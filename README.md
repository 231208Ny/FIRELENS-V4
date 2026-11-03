# FIRELENS
## Satellite-Based Wildfire Detection Analysis in Riau and Central Kalimantan, Indonesia

**Research Period:** 1 August – 31 October 2024  
**Project Version:** FIRELENS V3  
**Project Type:** Exploratory Data Analysis and Interactive Visualization

---

## 1. Project Overview

FIRELENS is an exploratory satellite-based wildfire detection analysis platform designed to examine fire detection patterns in Riau and Central Kalimantan, Indonesia.

The project processes and analyzes satellite fire detection records to explore their geographical distribution, temporal patterns, Fire Radiative Power (FRP), and differences between satellite sensors.

FIRELENS also provides an interactive dashboard that allows users to explore the analytical results through visualizations and descriptive statistics.

## 2. Research Objectives

The objectives of FIRELENS are:

1. To examine the geographical distribution of satellite fire detections in the selected study regions.
2. To identify temporal patterns in fire detections during August–October 2024.
3. To analyze the distribution and characteristics of Fire Radiative Power.
4. To compare detection records from MODIS and VIIRS sensors.
5. To assess selected data quality indicators.
6. To present the analytical results through an interactive dashboard.

## 3. Dataset Description

The research dataset contains 12,809 satellite fire detection records.

| Study region | Detection records |
|---|---:|
| Central Kalimantan (approximate bounding box) | 10,030 |
| Riau (approximate bounding box) | 2,779 |
| **Total** | **12,809** |

The dataset uses satellite detection records associated with NASA FIRMS MODIS and VIIRS observations.

### Sensor distribution

| Sensor | Records |
|---|---:|
| VIIRS | 10,109 |
| MODIS | 2,700 |
| **Total** | **12,809** |

### Main analytical variables

- Study region label
- Satellite sensor
- Acquisition date
- Latitude and longitude
- Fire Radiative Power (FRP)

## 4. Research Methodology

The FIRELENS analytical workflow consists of:

1. Data preparation and harmonization.
2. Geographical distribution analysis.
3. Temporal pattern analysis.
4. Fire Radiative Power analysis.
5. Satellite sensor comparison.
6. Data quality assessment.
7. Interactive dashboard development.

The analysis is exploratory and descriptive. Satellite detection records are treated as observations rather than confirmed counts of unique wildfire events.

## 5. Preliminary Research Findings

### 5.1 Geographical Findings

Central Kalimantan accounts for 10,030 records, while Riau accounts for 2,779 records within the selected study areas and research period.

### 5.2 Temporal Findings

September 2024 was the peak month for Central Kalimantan, with 6,911 detection records.

Riau recorded 1,054 detections in August, 687 in September, and 1,038 in October.

The highest daily detection count in Central Kalimantan occurred on 14 September 2024, with 762 records. In Riau, the highest daily count occurred on 27 October 2024, with 223 records.

### 5.3 Fire Radiative Power Findings

The mean FRP was:

- Central Kalimantan: 14.03 MW.
- Riau: 11.09 MW.

The median FRP was:

- Central Kalimantan: 8.09 MW.
- Riau: 5.43 MW.

The FRP distributions were right-skewed, indicating that a relatively small number of observations had substantially higher FRP values.

### 5.4 Sensor Comparison

VIIRS contributed the largest number of detection records.

MODIS Aqua had the highest mean FRP among the compared sensors in both study regions.

These comparisons are descriptive and should not be interpreted as direct proof that one sensor detects more actual fires or measures fire intensity more accurately.

### 5.5 Data Quality

The previous data quality assessment reported seven checks passed, zero flagged, and no automatic record removals.

The latest system check also found:

- 0 missing values.
- 0 exact duplicate rows.
- 12,809 readable dataset records.
- All six expected application files present.

## 6. System Architecture

FIRELENS V3 is developed using Python and Streamlit.

The dashboard contains five main analytical sections:

1. Main Dashboard
2. Geographic Analysis
3. Advanced Analytics
4. Data Quality
5. Research Insights and Methodology

The platform uses interactive charts, geographical visualizations, filters, statistical summaries, and downloadable analytical outputs.

## 7. Research Limitations

Several limitations must be considered:

1. Satellite detections do not necessarily represent unique wildfire events.
2. Cross-sensor duplicate detections have not been fully resolved.
3. Study regions use approximate bounding boxes rather than official administrative boundaries.
4. MODIS and VIIRS have different sensor characteristics and confidence schemes.
5. FRP differences should be interpreted cautiously.
6. High FRP observations are not automatically data errors.
7. Spatial and temporal proximity alone cannot establish that two detections belong to the same fire event.

## 8. Future Development

Potential future improvements include:

- Integration of additional satellite observation periods.
- More detailed spatial analysis using official administrative boundaries.
- Advanced fire event clustering.
- Improved cross-sensor comparison.
- Integration of weather and environmental variables.
- Additional model-based analytical approaches, subject to suitable data and validation.

## 9. Conclusion

FIRELENS V3 provides an exploratory analytical platform for examining satellite fire detection patterns in Riau and Central Kalimantan during August–October 2024.

By combining geographical, temporal, FRP, sensor, and data quality analyses in an interactive dashboard, the project provides a structured way to explore satellite-based wildfire observations.

Its findings should be interpreted within the limitations of satellite detection data and the exploratory scope of the research.

---

**FIRELENS V3 — Satellite-Based Wildfire Detection Analysis**