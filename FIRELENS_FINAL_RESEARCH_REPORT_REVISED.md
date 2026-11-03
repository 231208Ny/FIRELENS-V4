# FIRELENS: Satellite-Based Wildfire Detection Analysis in Riau and Central Kalimantan, Indonesia

## Revised Final Research Report

**Research Period:** 1 August - 31 October 2024  
**Project Version:** FIRELENS V3  
**Research Type:** Exploratory Satellite Detection Analysis

---

## Abstract

This study presents an exploratory analysis of satellite-based wildfire detection records in Riau and Central Kalimantan, Indonesia, during August-October 2024.

The processed dataset contains **12,809 detection records** associated with NASA FIRMS MODIS and VIIRS observations. The analysis examines geographical distribution, temporal patterns, Fire Radiative Power (FRP), sensor distribution, and selected data quality indicators.

Central Kalimantan contributed 10,030 records (78.3%), while Riau contributed 2,779 records (21.7%). VIIRS accounted for 10,109 records, compared with 2,700 MODIS records.

September 2024 recorded the highest monthly detection count in both study regions. The highest daily counts were 762 records in Central Kalimantan and 223 records in Riau.

The analysis also identified differences in regional FRP distributions. An interactive dashboard developed with Python and Streamlit supports the exploration of these observations.

The findings describe satellite detection records and should not be interpreted as counts of unique wildfire events or direct measurements of total burned area.

**Keywords:** Wildfire Detection, NASA FIRMS, MODIS, VIIRS, Fire Radiative Power, Indonesia, Exploratory Data Analysis.

---

## 1. Introduction

Wildfires are an important environmental concern in Indonesia because of their potential impacts on ecosystems, air quality, biodiversity, and surrounding communities.

Satellite-based fire detection systems provide observations that can be used to examine the spatial and temporal distribution of detected thermal anomalies.

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
4. What differences are observed in the number of MODIS and VIIRS records?
5. What data quality characteristics can be identified?

---

## 2. Data and Methodology

### 2.1 Data Source

The research uses satellite fire detection records associated with NASA FIRMS MODIS and VIIRS observations.

### 2.2 Study Period and Regions

The observation period covers 1 August to 31 October 2024.

The selected study regions are Riau and Central Kalimantan. The regional selections use approximate bounding boxes and should not be interpreted as official administrative boundaries.

### 2.3 Dataset Profile

The processed dataset contains **12,809 detection records**.

| study_region_label | detection_records | percentage |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 10030 | 78.30 |
| Riau (approximate bounding box) | 2779 | 21.70 |

The regional records sum to 12,809.

### 2.4 Sensor Distribution

| sensor | detection_records | percentage |
| --- | --- | --- |
| MODIS | 2700 | 21.08 |
| VIIRS | 10109 | 78.92 |

VIIRS represents the larger share of records in the processed dataset. This difference in record counts does not, by itself, demonstrate that one sensor is more accurate than the other.

### 2.5 Analytical Procedures

The study applies the following procedures:

- Data preprocessing and harmonization.
- Geographical distribution analysis.
- Daily and monthly temporal analysis.
- FRP descriptive statistical analysis.
- Sensor distribution analysis.
- Selected data quality assessment.
- Interactive visualization using Streamlit and Plotly.

### 2.6 Analytical Scope

The analysis focuses on detection records within the selected approximate study areas and observation period. The results are descriptive and exploratory.

---

## 3. Results

### 3.1 Geographical Distribution

Central Kalimantan accounted for 10,030 records (78.3%), while Riau accounted for 2,779 records (21.7%).

The Central Kalimantan study area therefore contributed the larger proportion of records in the processed dataset.

| study_region_label | detection_records | percentage |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 10030 | 78.30 |
| Riau (approximate bounding box) | 2779 | 21.70 |

### 3.2 Monthly Temporal Analysis

The monthly distribution shows that September 2024 was the peak month in both regions.

Central Kalimantan recorded 6,911 detections in September, while Riau recorded 687.

| study_region_label | month | detection_records |
| --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 2024-08 | 1332 |
| Central Kalimantan (approximate bounding box) | 2024-09 | 6911 |
| Central Kalimantan (approximate bounding box) | 2024-10 | 1787 |
| Riau (approximate bounding box) | 2024-08 | 1054 |
| Riau (approximate bounding box) | 2024-09 | 687 |
| Riau (approximate bounding box) | 2024-10 | 1038 |

The monthly pattern differs between the regions. Central Kalimantan shows a pronounced September peak, whereas Riau recorded higher counts in August and October than in September.

### 3.3 Daily Detection Peaks

The highest daily detection count in Central Kalimantan occurred on 2024-09-14, with 762 records.

In Riau, the highest daily count occurred on 2024-10-27, with 223 records.

The following table presents the ten highest daily counts identified for each study region.

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

These values represent daily satellite detection records, not verified counts of separate fire events.

### 3.4 Fire Radiative Power Analysis

FRP provides an indication of the radiative energy observed from detected fires by satellite instruments. The following statistics summarize the available FRP observations.

| study_region_label | count | mean | median | std | minimum | maximum |
| --- | --- | --- | --- | --- | --- | --- |
| Central Kalimantan (approximate bounding box) | 10030 | 14.03 | 8.09 | 19.60 | 0.19 | 463.00 |
| Riau (approximate bounding box) | 2779 | 11.10 | 5.43 | 26.32 | 0.14 | 479.20 |

Central Kalimantan had a mean FRP of 14.031 MW and a median of 8.09 MW.

Riau had a mean FRP of 11.095 MW and a median of 5.43 MW.

In both regions, the mean exceeds the median, which is consistent with right-skewed FRP distributions. The maximum values are substantially higher than the medians, indicating the presence of high-FRP observations.

These maximum observations should not automatically be classified as errors. Their interpretation requires consideration of sensor characteristics, observation conditions, and the underlying data.

### 3.5 Sensor Distribution

VIIRS contributed the largest number of records, with 10,109 observations (78.92%). MODIS contributed 2,700 observations (21.08%).

| sensor | detection_records | percentage |
| --- | --- | --- |
| MODIS | 2700 | 21.08 |
| VIIRS | 10109 | 78.92 |

The difference in record counts may reflect differences in sensor characteristics, spatial resolution, observation timing, and sampling. Record counts alone cannot establish comparative sensor accuracy.

A previous sensor-level analysis identified MODIS Aqua as having the highest mean FRP among the compared sensors in both study regions. This finding should be checked against the corresponding sensor-by-region FRP statistics before being treated as a confirmed result in a formal publication.

### 3.6 Data Quality and System Validation

The previous research assessment reported seven checks passed, zero flagged, and no automatic data removals.

The latest system check confirmed:

- Dataset readability.
- 12,809 records.
- Zero missing values in the checked dataset.
- Zero exact duplicate rows.
- Successful generation of the system test report.

These checks describe the tested dataset and software workflow. They do not establish that every satellite detection is independently verified or free from all possible errors.

---

## 4. Discussion

The results indicate differences in the number and temporal distribution of satellite detection records between the two study regions.

Central Kalimantan contributed 78.3% of the records and experienced a pronounced detection peak in September 2024. Riau contributed 21.7% and showed a different monthly pattern, with relatively higher counts in August and October than in September.

The FRP analysis revealed differences in descriptive averages and medians between the regions. The mean FRP was higher in Central Kalimantan, while both regions showed distributions in which the mean exceeded the median.

These statistics should not be interpreted as direct evidence of differences in total wildfire impact, burned area, or ecological damage. Such conclusions would require additional data and appropriate validation.

VIIRS accounted for most records in the processed dataset. However, differences in observation characteristics and sampling mean that record counts should not be treated as a direct measure of sensor performance or accuracy.

Overall, FIRELENS provides an integrated framework for exploring satellite detection records through geographical, temporal, radiative power, and sensor-based perspectives.

---

## 5. Limitations

The research has several limitations:

1. Satellite detection records do not necessarily correspond to unique wildfire events.
2. Cross-sensor deduplication has not been fully performed.
3. The selected regional boundaries are approximate bounding boxes, not official administrative boundaries.
4. MODIS and VIIRS have different sensor characteristics and confidence schemes.
5. FRP values should not be interpreted as direct measurements of total burned area.
6. Spatial and temporal proximity alone cannot establish that detections belong to the same fire event.
7. High FRP observations require contextual interpretation and are not automatically data errors.
8. The study is exploratory and does not establish causal relationships.
9. The results depend on the coverage, quality, and characteristics of the processed satellite detection dataset.

---

## 6. Conclusion

This study developed FIRELENS V3, an interactive analytical platform for exploring satellite-based wildfire detection records in Riau and Central Kalimantan during August-October 2024.

The analysis examined 12,809 records and identified differences in geographical distribution, monthly and daily detection patterns, FRP statistics, and sensor record counts.

Central Kalimantan contributed the larger share of records, while September was the peak month in both study regions. VIIRS accounted for the majority of records in the processed dataset.

The FRP results showed higher mean and median values in Central Kalimantan than in Riau. However, these descriptive differences should not be interpreted as direct measurements of total wildfire impact.

FIRELENS demonstrates the value of integrating satellite detection data with interactive analytical visualization. It provides a foundation for further exploratory research and future development involving more detailed spatial analysis, additional environmental variables, and validated fire event identification methods.

---

## 7. Recommendations for Future Research

Future research could:

1. Integrate official administrative boundaries.
2. Extend the observation period.
3. Investigate meteorological and environmental variables.
4. Develop validated methods for identifying individual fire events.
5. Improve cross-sensor comparison and harmonization.
6. Evaluate relationships between satellite observations and independent ground-based information.
7. Conduct further validation of FRP observations and sensor-level statistics.

---

## 8. Research Tables and Visualizations

The following files were generated from the processed exploratory dataset.

### 8.1 Statistical Tables

- [Regional distribution](research_outputs/table_01_regional_distribution.csv)
- [Sensor distribution](research_outputs/table_02_sensor_distribution.csv)
- [Monthly distribution](research_outputs/table_03_monthly_distribution.csv)
- [FRP statistics](research_outputs/table_04_frp_statistics.csv)
- [Daily detection peaks](research_outputs/table_05_daily_peaks.csv)

### 8.2 Interactive Charts

- [Regional distribution chart](research_outputs/charts/chart_01_regional_distribution.html)
- [Sensor distribution chart](research_outputs/charts/chart_02_sensor_distribution.html)
- [Monthly trends chart](research_outputs/charts/chart_03_monthly_trends.html)
- [FRP distribution chart](research_outputs/charts/chart_04_frp_distribution.html)

---

## 9. Reproducibility and Validation Note

The research tables and charts were generated using `generate_research_visuals.py`.

The validated statistical summary is also available in `research_outputs/VALIDATED_RESEARCH_RESULTS.md`.

The results should be checked against the original NASA FIRMS source data, preprocessing decisions, and research definitions before formal academic submission or publication.

The system validation confirms that the tested application files and processed dataset were readable and that the specified checks completed successfully. It does not replace independent scientific validation.

---

**End of Revised Research Report - FIRELENS V3**
