# FIRELENS: Satellite-Based Wildfire Detection Analysis in Riau and Central Kalimantan, Indonesia

## Final Research Report

**Research Period:** 1 August – 31 October 2024  
**Project Version:** FIRELENS V3

---

## Abstract

This study presents an exploratory analysis of satellite-based wildfire detection records in Riau and Central Kalimantan, Indonesia, during August–October 2024.

Using 12,809 detection records associated with MODIS and VIIRS satellite observations, the study examines geographical distribution, temporal patterns, Fire Radiative Power (FRP), sensor-based differences, and selected data quality indicators.

The results show that Central Kalimantan contributed 10,030 records, while Riau contributed 2,779 records. VIIRS accounted for 10,109 records, compared with 2,700 from MODIS.

The analysis also identified regional differences in temporal patterns and FRP distributions. An interactive dashboard, developed using Python and Streamlit, was created to support data exploration and visualization.

The findings provide descriptive insights into satellite fire detection patterns. However, detection records should not be interpreted as counts of unique wildfire events.

**Keywords:** Wildfire Detection, NASA FIRMS, MODIS, VIIRS, Fire Radiative Power, Indonesia, Exploratory Data Analysis.

---

## 1. Introduction

Wildfires are an important environmental concern in Indonesia because of their potential impacts on ecosystems, air quality, biodiversity, and surrounding communities.

Satellite-based fire detection systems provide valuable observations for examining the spatial and temporal distribution of detected thermal anomalies.

This research introduces FIRELENS, an exploratory analytical platform designed to investigate satellite-based fire detection records in Riau and Central Kalimantan.

### 1.1 Research Objectives

The study aims to:

1. Examine geographical patterns of satellite fire detections.
2. Identify temporal variations during the research period.
3. Analyze Fire Radiative Power distributions.
4. Compare MODIS and VIIRS detection records.
5. Assess selected data quality indicators.
6. Develop an interactive analytical dashboard.

### 1.2 Research Questions

1. How are satellite fire detections distributed across the selected study regions?
2. What temporal patterns can be observed between August and October 2024?
3. How does FRP vary between the two study regions?
4. What differences are observed between MODIS and VIIRS records?
5. What data quality characteristics can be identified?

---

## 2. Data and Methodology

### 2.1 Data Source

The research uses satellite fire detection records associated with NASA FIRMS MODIS and VIIRS observations.

### 2.2 Study Period and Regions

The observation period covers 1 August to 31 October 2024.

The selected study regions are Riau and Central Kalimantan. The regional selections use approximate bounding boxes and should not be interpreted as official administrative boundaries.

### 2.3 Dataset Profile

| Study region | Records |
|---|---:|
| Central Kalimantan | 10,030 |
| Riau | 2,779 |
| Total | 12,809 |

### 2.4 Sensor Distribution

| Sensor | Records |
|---|---:|
| VIIRS | 10,109 |
| MODIS | 2,700 |
| Total | 12,809 |

### 2.5 Analytical Procedures

The study applies the following procedures:

- Data preprocessing and harmonization.
- Geographical distribution analysis.
- Daily and monthly temporal analysis.
- FRP descriptive statistical analysis.
- Sensor comparison.
- Data quality assessment.
- Interactive visualization using Streamlit and Plotly.

---

## 3. Results

### 3.1 Geographical Distribution

Central Kalimantan accounted for 10,030 detection records, while Riau accounted for 2,779 records.

These figures describe the distribution of records within the selected study areas and observation period.

### 3.2 Temporal Analysis

September 2024 was the peak month in Central Kalimantan, with 6,911 records.

In Riau, the monthly counts were:

- August: 1,054 records.
- September: 687 records.
- October: 1,038 records.

The highest daily count in Central Kalimantan occurred on 14 September 2024, with 762 records.

In Riau, the highest daily count occurred on 27 October 2024, with 223 records.

### 3.3 Fire Radiative Power Analysis

The mean FRP values were:

| Region | Mean FRP |
|---|---:|
| Central Kalimantan | 14.03 MW |
| Riau | 11.09 MW |

The median FRP values were:

| Region | Median FRP |
|---|---:|
| Central Kalimantan | 8.09 MW |
| Riau | 5.43 MW |

The distributions were right-skewed, suggesting that a relatively small number of observations had substantially higher FRP values.

### 3.4 Sensor Comparison

VIIRS contributed the largest number of records, with 10,109 observations.

MODIS contributed 2,700 observations.

MODIS Aqua recorded the highest mean FRP among the compared sensors in both study regions.

These differences are descriptive and may reflect sensor characteristics, observation conditions, and sampling differences.

### 3.5 Data Quality Assessment

The previous research assessment reported seven checks passed, zero flagged, and no automatic data removals.

The latest system check confirmed:

- Dataset readability.
- 12,809 records.
- Zero missing values.
- Zero exact duplicate rows.
- Successful generation of the system test report.

---

## 4. Discussion

The results indicate differences in the number and temporal distribution of satellite detection records between the two study regions.

Central Kalimantan contributed a larger proportion of the dataset and experienced a pronounced detection peak in September 2024. Riau showed a different temporal pattern, with relatively higher monthly counts in August and October than in September.

The FRP analysis also revealed differences in descriptive averages and medians between the regions. However, these statistics should not be treated as direct evidence of differences in total wildfire impact or burned area.

Sensor comparisons require additional caution because MODIS and VIIRS differ in their observation characteristics and detection methodologies.

Overall, FIRELENS provides an integrated framework for exploring satellite detection records through geographical, temporal, radiative power, and sensor-based perspectives.

---

## 5. Limitations

The research has several limitations:

1. Satellite detection records do not necessarily correspond to unique wildfire events.
2. Cross-sensor deduplication has not been fully performed.
3. The selected regional boundaries are approximate bounding boxes.
4. MODIS and VIIRS use different sensor characteristics and confidence schemes.
5. FRP values should not be interpreted as direct measurements of total burned area.
6. Temporal and spatial proximity alone cannot establish that detections belong to the same fire event.
7. The study is exploratory and does not establish causal relationships.

---

## 6. Conclusion

This study developed FIRELENS V3, an interactive analytical platform for exploring satellite-based wildfire detection records in Riau and Central Kalimantan during August–October 2024.

The analysis examined geographical distribution, temporal patterns, Fire Radiative Power, sensor comparisons, and selected data quality indicators.

The findings demonstrate the value of integrating satellite detection data with interactive analytical visualization.

FIRELENS provides a foundation for further exploratory research and future development involving more detailed spatial analysis, additional environmental variables, and validated fire event identification methods.

---

## 7. Recommendations for Future Research

Future research could:

1. Integrate official administrative boundaries.
2. Extend the observation period.
3. Investigate meteorological and environmental variables.
4. Develop validated methods for identifying individual fire events.
5. Improve cross-sensor comparison and harmonization.
6. Evaluate the relationship between satellite observations and independent ground-based information.

---

**End of Report — FIRELENS V3**