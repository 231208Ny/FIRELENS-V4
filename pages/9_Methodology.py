
import streamlit as st

st.title("📚 Research Methodology")
st.caption(
    "Understanding the research design, data processing, "
    "analytical methods, and limitations of FIRELENS."
)

# 1. Research Design
st.header("1. Research Design")

st.markdown("""
FIRELENS applies a **quantitative, descriptive, and exploratory
research approach** to examine historical satellite-based active fire
detection records in two Indonesian provinces.

The analysis focuses on identifying spatial and temporal patterns
and exploring Fire Radiative Power (FRP) characteristics.

The study does not attempt to establish causal relationships or
estimate the total number of independent wildfire events.
""")

col1, col2, col3 = st.columns(3)

col1.metric("Study Regions", "2")
col2.metric("Observation Period", "3 months")
col3.metric("Detection Records", "12,809")

st.divider()

# 2. Study Area and Period
st.header("2. Study Area and Observation Period")

st.markdown("""
| Parameter | Description |
|---|---|
| Study Region 1 | Riau, Indonesia |
| Study Region 2 | Central Kalimantan, Indonesia |
| Start Date | 1 August 2024 |
| End Date | 31 October 2024 |
| Data Categories | MODIS and VIIRS |
| Observation Type | Satellite active fire detections |
""")

st.info(
    "The study uses a historical dataset. It does not represent "
    "current fire conditions or a real-time monitoring system."
)

st.divider()

# 3. Data Collection
st.header("3. Data Collection")

st.markdown("""
The research uses historical active fire detection information
associated with NASA's Fire Information for Resource Management
System (FIRMS).

Two satellite instrument categories are represented:

- **MODIS:** Moderate Resolution Imaging Spectroradiometer.
- **VIIRS:** Visible Infrared Imaging Radiometer Suite.

The dataset contains 12,809 detection records from the selected
study regions and observation period.
""")

st.markdown(
    "[NASA FIRMS Official Portal](https://firms.modaps.eosdis.nasa.gov/)"
)

st.divider()

# 4. Data Preprocessing
st.header("4. Data Preprocessing")

st.markdown("""
Before analysis, the dataset is organized into a consistent
structure for exploratory analysis.

The preparation process includes:

1. Organizing the records by study region.
2. Standardizing the variables used in the application.
3. Preparing acquisition dates for temporal analysis.
4. Organizing geographic coordinates for spatial exploration.
5. Preparing FRP values for statistical analysis.
6. Performing basic data quality checks.

The application uses the processed dataset:

`data/processed/regional_detections_exploratory.csv`
""")

st.warning("""
Data preprocessing does not imply that all potential differences
between satellite instruments or observation conditions have
been eliminated.
""")

st.divider()

# 5. Spatial Analysis
st.header("5. Spatial Analysis")

st.markdown("""
Spatial analysis explores the geographic distribution of satellite
detection records across Riau and Central Kalimantan.

The application uses latitude and longitude coordinates to:

- Display detection locations on an interactive map.
- Compare detection distributions between study regions.
- Explore geographic concentration patterns.
- Support exploratory regional comparisons.

The study-region boundaries are approximate bounding areas rather
than precise administrative or ecological boundaries.
""")

st.divider()

# 6. Temporal Analysis
st.header("6. Temporal Analysis")

st.markdown("""
Temporal analysis examines how detection-record counts vary
throughout the observation period.

The analysis includes:

- Monthly detection-record comparisons.
- Daily detection-record trends.
- Identification of dates with relatively high record counts.
- Comparison of temporal patterns between study regions.

These patterns describe the distribution of available satellite
observations. They should not automatically be interpreted as
changes in the number of unique wildfire events.
""")

st.divider()

# 7. Fire Radiative Power
st.header("7. Fire Radiative Power (FRP) Analysis")

st.markdown("""
Fire Radiative Power (FRP) is used as an indicator of the rate
at which radiant energy is emitted by detected fire pixels.

FIRELENS explores FRP using:

- Mean and median values.
- Standard deviation.
- Minimum and maximum values.
- Histograms and distribution comparisons.
- Comparisons between the two study regions.

FRP is expressed in megawatts (MW).

FRP is not a direct measurement of burned area, total emissions,
property damage, or the overall severity of a wildfire.
""")

st.info(
    "FRP values can be strongly right-skewed. Therefore, the median "
    "should be considered alongside the mean when interpreting "
    "regional distributions."
)

st.divider()

# 8. Data Quality Assurance
st.header("8. Data Quality Assurance")

st.markdown("""
FIRELENS includes basic quality assurance checks to assess the
consistency of the processed dataset.

The reported quality assessment includes:

| Quality Check | Result |
|---|---:|
| Checks passed | 7 |
| Flagged checks | 0 |
| Missing values | 0 |
| Exact duplicate rows | 0 |
| Automatic record removals | 0 |
""")

st.warning("""
Passing these checks does not prove that the dataset is completely
error-free. It only describes the outcomes of the implemented
quality checks.
""")

st.divider()

# 9. Interpretation
st.header("9. Interpretation Framework")

st.markdown("""
FIRELENS follows several principles when interpreting its results:

1. Detection records are not equivalent to unique fire events.
2. Differences between MODIS and VIIRS should be considered.
3. Spatial proximity alone cannot establish that records belong
   to the same fire.
4. FRP should not be interpreted as burned area or total damage.
5. Observed patterns should be described without unsupported
   causal conclusions.
6. Results should remain within the geographic and temporal scope
   of the dataset.
""")

st.divider()

# 10. Limitations
st.header("10. Research Limitations")

limitations = [
    (
        "Historical coverage",
        "The dataset only covers 1 August to 31 October 2024."
    ),
    (
        "Detection records",
        "Individual records do not necessarily represent unique fire events."
    ),
    (
        "Satellite differences",
        "MODIS and VIIRS have different instrument characteristics "
        "and observation properties."
    ),
    (
        "Approximate study boundaries",
        "Regional selection uses approximate geographic boundaries."
    ),
    (
        "FRP interpretation",
        "FRP is not a direct measure of burned area or total damage."
    ),
    (
        "Event identification",
        "Spatial and temporal proximity alone cannot confirm that "
        "multiple records belong to the same fire."
    ),
    (
        "Causal inference",
        "The exploratory analysis does not establish the causes "
        "of observed fire patterns."
    ),
]

for title, description in limitations:
    with st.expander(title):
        st.write(description)

st.divider()

# 11. Responsible Use
st.header("11. Responsible Use of Findings")

st.markdown("""
FIRELENS is an independent exploratory research and educational
platform designed to make satellite fire detection information
more understandable and accessible.

Its results should be used as supporting information for learning
and research exploration, not as the sole basis for emergency
response, public safety decisions, or operational fire management.

FIRELENS is not an official NASA product and is not affiliated
with or endorsed by NASA.
""")

st.divider()

st.markdown("""
**FIRELENS**

*Making Satellite Fire Data Understandable and Accessible to Everyone.*

Research methodology and limitations are provided to support
transparent and responsible interpretation of the dataset.
""")
