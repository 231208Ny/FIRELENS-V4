
import streamlit as st

# --------------------------------------------------
# FIRELENS V5 — ABOUT PROJECT
# --------------------------------------------------

st.markdown("""
<style>
.about-hero {
    padding: 38px 32px;
    border-radius: 18px;
    background: linear-gradient(125deg, #102b32, #174b45, #246451);
    color: white;
    margin-bottom: 25px;
}
.about-hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
}
.about-hero p {
    font-size: 17px;
    color: #d8ebe4;
}
.about-card {
    padding: 22px;
    border: 1px solid rgba(128,128,128,0.25);
    border-radius: 14px;
    margin-bottom: 15px;
}
.about-label {
    color: #49a889;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 1px;
}
.metric-card {
    padding: 18px;
    border-radius: 12px;
    background: rgba(90,150,120,0.10);
    text-align: center;
}
.metric-number {
    font-size: 29px;
    font-weight: bold;
}
.metric-caption {
    font-size: 13px;
    opacity: 0.75;
}
</style>
""", unsafe_allow_html=True)


# HERO SECTION
st.markdown("""
<div class="about-hero">
    <div class="about-label">ABOUT THE PROJECT</div>
    <h1>🔥 FIRELENS</h1>
    <p>
        Making Satellite Fire Data Understandable
        and Accessible to Everyone.
    </p>
    <p>
        An exploratory satellite-based wildfire detection
        research and information platform.
    </p>
</div>
""", unsafe_allow_html=True)


# INTRODUCTION
st.markdown("## What is FIRELENS?")

st.write("""
FIRELENS is an exploratory research platform designed to
make satellite-based active fire detection information
more understandable, accessible, and useful.

The platform transforms historical satellite detection
records into interactive visualizations, geographical
exploration tools, statistical summaries, and research
insights.

FIRELENS aims to bridge the gap between complex satellite
data and the people and institutions who may benefit from
understanding it.
""")


# PROJECT OBJECTIVES
st.markdown("## Our Objectives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-card">
        <h3>🌍 Public Accessibility</h3>
        <p>
        Present satellite fire detection information
        through accessible visualizations and
        straightforward explanations for the public.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-card">
        <h3>📊 Data Exploration</h3>
        <p>
        Enable users to explore geographical patterns,
        temporal distributions, satellite sensors,
        and Fire Radiative Power (FRP).
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h3>🔬 Research Support</h3>
        <p>
        Provide analytical tools and structured
        information that can support exploratory
        research and further investigation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-card">
        <h3>🤝 Shared Understanding</h3>
        <p>
        Encourage informed discussions among researchers,
        environmental organizations, public institutions,
        and communities.
        </p>
    </div>
    """, unsafe_allow_html=True)


# STUDY OVERVIEW
st.markdown("## Research Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">12,809</div>
        <div class="metric-caption">Detection Records</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">2</div>
        <div class="metric-caption">Study Regions</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">3 Months</div>
        <div class="metric-caption">Study Period</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="about-card">
    <h3>📍 Geographical Scope</h3>
    <ul>
        <li>Riau, Indonesia</li>
        <li>Central Kalimantan, Indonesia</li>
    </ul>
    <h3>📅 Temporal Scope</h3>
    <p>1 August – 31 October 2024</p>
</div>
""", unsafe_allow_html=True)


# DATA SOURCES
st.markdown("## Data Sources")

st.write("""
The research uses historical active fire detection records
from NASA's Fire Information for Resource Management System
(FIRMS).
""")

st.markdown("""
<div class="about-card">
    <h3>🛰️ Satellite Instruments</h3>
    <ul>
        <li><b>VIIRS:</b> Visible Infrared Imaging Radiometer Suite</li>
        <li><b>MODIS:</b> Moderate Resolution Imaging Spectroradiometer</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "[NASA FIRMS — Official Data Portal](https://firms.modaps.eosdis.nasa.gov/)"
)

st.markdown(
    "[NASA Earthdata](https://www.earthdata.nasa.gov/)"
)


# PUBLIC AND RESEARCH MODE
st.markdown("## Two Ways to Explore FIRELENS")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-card">
        <h3>🌍 Public Mode</h3>
        <p>
        Designed for general audiences who want to
        understand historical fire detection patterns
        through maps, charts, and simplified summaries.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h3>🔬 Research Mode</h3>
        <p>
        Designed for deeper exploration through filters,
        statistical analysis, geographical comparisons,
        FRP analysis, and data downloads.
        </p>
    </div>
    """, unsafe_allow_html=True)


# LIMITATIONS
st.markdown("## Research Scope & Limitations")

st.warning("""
**Important research considerations**

- FIRELENS uses historical data from August to October 2024.
- The platform is not a real-time fire monitoring or
  emergency alert system.
- Satellite detection records do not necessarily represent
  unique individual fire events.
- MODIS and VIIRS observations have different sensor
  characteristics.
- Study-region boundaries are approximate.
- Fire Radiative Power (FRP) is not a direct measurement
  of burned area or total environmental damage.
- Spatial and temporal proximity alone cannot establish
  whether detections belong to the same fire event.
- The findings should be interpreted as exploratory
  observations rather than causal conclusions.
""")


# DISCLAIMER
st.markdown("## Disclaimer")

st.write("""
FIRELENS is an independent exploratory research project.
It is not an official NASA product and is not affiliated
with or endorsed by NASA.

NASA FIRMS is acknowledged as the source of the
underlying satellite active fire detection information.

The platform is intended for educational, informational,
and research exploration purposes. It should not be used
as the sole basis for emergency response or operational
decision-making.
""")


# FOOTER
st.divider()

st.markdown("""
<div style="text-align:center; padding:15px 0;">
    <h3>🔥 FIRELENS</h3>
    <p>
        Making Satellite Fire Data Understandable
        and Accessible to Everyone.
    </p>
    <p style="font-size:12px; opacity:0.65;">
        Independent Exploratory Research Platform |
        Historical Dataset: 2024
    </p>
</div>
""", unsafe_allow_html=True)
