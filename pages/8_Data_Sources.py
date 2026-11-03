
import streamlit as st

st.title("🛰️ Data Sources")
st.caption("Understanding where FIRELENS data comes from and how it is used.")

st.markdown("""
## 1. Primary Data Source

FIRELENS uses historical satellite-based active fire detection records
associated with NASA's **Fire Information for Resource Management System
(FIRMS)**.

NASA FIRMS distributes active fire information from satellite instruments
including MODIS and VIIRS. These observations help identify locations with
thermal signatures consistent with active fires or other thermal anomalies.

**Official source:**  
https://firms.modaps.eosdis.nasa.gov/
""")

st.divider()

st.markdown("## 2. Satellite Instruments")

col1, col2 = st.columns(2)

with col1:
    st.subheader("MODIS")
    st.write("""
    **Moderate Resolution Imaging Spectroradiometer**

    - Operates aboard the Terra and Aqua satellites.
    - Provides active fire detection observations.
    - FIRELENS dataset records: **2,700**
    - Share of dataset: **21.08%**
    """)

with col2:
    st.subheader("VIIRS")
    st.write("""
    **Visible Infrared Imaging Radiometer Suite**

    - Provides satellite-based active fire observations.
    - Used aboard the Suomi-NPP and other compatible platforms.
    - FIRELENS dataset records: **10,109**
    - Share of dataset: **78.92%**
    """)

st.info(
    "The figures above describe the sensor categories recorded in the "
    "FIRELENS dataset. They are detection-record counts, not counts of "
    "independent fire events."
)

st.divider()

st.markdown("## 3. Study Dataset")

st.markdown("""
The current FIRELENS analysis focuses on two Indonesian provinces over
a three-month historical observation period.
""")

a, b, c = st.columns(3)

a.metric("Total Records", "12,809")
b.metric("Study Regions", "2")
c.metric("Observation Period", "3 months")

st.markdown("""
| Parameter | Description |
|---|---|
| Study period | 1 August – 31 October 2024 |
| Region 1 | Riau |
| Region 2 | Central Kalimantan |
| Satellite categories | MODIS and VIIRS |
| Main observation type | Active fire detections |
| Analysis approach | Exploratory spatial and temporal analysis |
""")

st.caption(
    "Dataset used by the application: "
    "`data/processed/regional_detections_exploratory.csv`"
)

st.divider()

st.markdown("## 4. Variables Used in FIRELENS")

variables = [
    ("latitude", "Geographic latitude of a detection record."),
    ("longitude", "Geographic longitude of a detection record."),
    ("acquisition_date", "Date associated with the satellite observation."),
    ("sensor", "Satellite instrument category, such as MODIS or VIIRS."),
    ("frp", "Fire Radiative Power (FRP), expressed in megawatts (MW)."),
    ("study_region_label", "Study-region classification used in FIRELENS."),
]

for name, description in variables:
    with st.expander(name):
        st.write(description)

st.divider()

st.markdown("## 5. Data Access and Documentation")

st.markdown("""
Explore the official resources below:

- [NASA FIRMS — Active Fire Data](https://firms.modaps.eosdis.nasa.gov/active_fire/)
- [NASA FIRMS — Archive Download](https://firms2.modaps.eosdis.nasa.gov/download/)
- [NASA FIRMS — Tutorials and Resources](https://firms.modaps.eosdis.nasa.gov/tutorials/)
- [NASA Earthdata](https://www.earthdata.nasa.gov/)
""")

st.divider()

st.markdown("## 6. Data Attribution")

st.markdown("""
FIRELENS acknowledges NASA's Fire Information for Resource Management
System (FIRMS) as the source of the satellite active fire detection
information used in this exploratory project.

Suggested dataset acknowledgement:

> Active fire detection data were obtained from NASA's Fire Information
> for Resource Management System (FIRMS).

Users conducting formal academic work should consult the official NASA
FIRMS **Acknowledgements & Citation** guidance and the documentation
for the specific data products used.
""")

st.markdown(
    "[NASA FIRMS — Acknowledgements & Citation](https://firms.modaps.eosdis.nasa.gov/)"
)

st.divider()

st.markdown("## 7. Important Data Considerations")

st.warning("""
- Satellite detection records do not necessarily represent unique fire events.
- MODIS and VIIRS have different instrument characteristics and observation
  properties.
- A satellite detection is not, by itself, confirmation of a ground-level fire.
- Fire Radiative Power is not a direct measurement of burned area or total damage.
- The dataset covers a historical period and is not a real-time monitoring feed.
""")

st.markdown("""
---

**FIRELENS**  
*Making Satellite Fire Data Understandable and Accessible to Everyone.*

An independent exploratory research project. FIRELENS is not an official
NASA product and is not affiliated with or endorsed by NASA.
""")
