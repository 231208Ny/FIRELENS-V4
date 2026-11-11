
import streamlit as st

# ==========================================
# FIRELENS V5 — PROFESSIONAL HOME PAGE
# ==========================================

# HERO SECTION
st.markdown("""
<style>
.hero-container {
    background: linear-gradient(120deg, #123B32 0%, #269B79 100%);
    padding: 42px 36px;
    border-radius: 18px;
    color: white;
    margin-bottom: 28px;
}

.hero-container h1 {
    color: white;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-container p {
    color: #E5F5EF;
    font-size: 17px;
    line-height: 1.7;
}

.hero-label {
    color: #B9E9D7;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.section-heading {
    color: #18332D;
    font-size: 25px;
    font-weight: 750;
    margin-top: 12px;
}

.info-card {
    background: #F3F7F6;
    border: 1px solid #DCE9E4;
    border-radius: 14px;
    padding: 22px;
    min-height: 190px;
}

.info-card h3 {
    color: #18332D;
    font-size: 19px;
    margin-bottom: 12px;
}

.info-card p {
    color: #52645E;
    font-size: 14px;
    line-height: 1.7;
}

.stat-card {
    background: #F3F7F6;
    border: 1px solid #DCE9E4;
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}

.stat-number {
    color: #269B79;
    font-size: 29px;
    font-weight: 800;
}

.stat-label {
    color: #52645E;
    font-size: 13px;
    margin-top: 5px;
}

.footer-text {
    color: #71817B;
    font-size: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero-container">
    <div class="hero-label">Satellite Fire Research Platform</div>
    <h1>🔥 FIRELENS</h1>
    <p>
        Making Satellite Fire Data Understandable
        and Accessible to Everyone.
    </p>
    <p>
        Explore historical satellite-based fire detection records
        through interactive maps, accessible visualizations,
        and research-oriented analytical tools.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# INTRODUCTION
# ==========================================

st.markdown('<div class="section-heading">Understanding Fire Through Data</div>',
            unsafe_allow_html=True)

st.write("""
FIRELENS is an independent exploratory research platform that transforms
satellite-based active fire detection records into accessible information.

The platform is designed to support public understanding, data exploration,
and research activities related to historical fire detection patterns
in Indonesia.
""")


# ==========================================
# KEY STATISTICS
# ==========================================

st.markdown('<div class="section-heading">Research at a Glance</div>',
            unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">12,809</div>
        <div class="stat-label">Detection Records</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2</div>
        <div class="stat-label">Study Regions</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2</div>
        <div class="stat-label">Satellite Categories</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3 Months</div>
        <div class="stat-label">Historical Observation</div>
    </div>
    """, unsafe_allow_html=True)

st.caption(
    "Dataset coverage: 1 August – 31 October 2024 | "
    "Riau and Central Kalimantan, Indonesia"
)


# ==========================================
# EXPLORE THE PLATFORM
# ==========================================

st.divider()

st.markdown('<div class="section-heading">Explore FIRELENS</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>🌍 Public Mode</h3>
        <p>
            Discover historical fire detection patterns through
            easy-to-understand explanations, interactive maps,
            and accessible visualizations.
        </p>
        <p><b>Designed for:</b> General public and curious learners.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/1_Public_Mode.py",
        label="Explore Public Mode",
        icon="🌍",
        use_container_width=True
    )

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>🔬 Research Workspace</h3>
        <p>
            Explore geographic distributions, analytical summaries,
            data quality information, and research-oriented insights.
        </p>
        <p><b>Designed for:</b> Students, researchers, and academics.</p>
    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/6_Research_Mode.py",
        label="Explore Research Mode",
        icon="🔬",
        use_container_width=True
    )


# ==========================================
# STUDY OVERVIEW
# ==========================================

st.divider()

st.markdown('<div class="section-heading">About the Research</div>',
            unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📍 Study Regions")

    st.markdown("""
    **Riau**

    One of the two Indonesian study regions included in the
    historical satellite detection dataset.

    **Central Kalimantan**

    The second study region, included to support geographic
    and temporal comparisons.
    """)

with col2:
    st.subheader("🛰️ Data Sources")

    st.markdown("""
    FIRELENS explores active fire detection records associated
    with NASA FIRMS satellite data.

    - MODIS
    - VIIRS

    The dataset covers August to October 2024.
    """)

    st.link_button(
        "Visit NASA FIRMS",
        "https://firms.modaps.eosdis.nasa.gov/",
        use_container_width=True
    )


# ==========================================
# PLATFORM PURPOSE
# ==========================================

st.divider()

st.markdown('<div class="section-heading">Our Objectives</div>',
            unsafe_allow_html=True)

obj1, obj2, obj3 = st.columns(3)

with obj1:
    st.markdown("### 🌱 Accessibility")
    st.write("""
    Making complex satellite fire information
    easier to understand and explore.
    """)

with obj2:
    st.markdown("### 📊 Data Exploration")
    st.write("""
    Presenting historical spatial and temporal
    patterns through interactive visualizations.
    """)

with obj3:
    st.markdown("### 🎓 Research Support")
    st.write("""
    Supporting educational activities and
    exploratory research with transparent limitations.
    """)


# ==========================================
# RESEARCH DISCLAIMER
# ==========================================

st.divider()

st.warning("""
**Important Research Note**

FIRELENS presents historical satellite detection records,
not a real-time fire alert system.

A detection record does not necessarily represent a unique
wildfire event. Satellite observations, Fire Radiative Power (FRP),
and geographic patterns must be interpreted within the limitations
of the dataset.

FIRELENS is an independent exploratory research project.
It is not an official NASA product and is not affiliated with
or endorsed by NASA.
""")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""
<div class="footer-text">
    <b>FIRELENS</b><br>
    Making Satellite Fire Data Understandable and Accessible to Everyone.<br>
    Historical Research Dataset | Indonesia | 2024
</div>
""", unsafe_allow_html=True)
