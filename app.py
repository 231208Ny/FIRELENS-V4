
import streamlit as st

# =====================================================
# FIRELENS V5 — MAIN APPLICATION
# Satellite Fire Research Platform
# =====================================================


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="FIRELENS | Satellite Fire Research",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================================
# 2. GLOBAL STYLING
# =====================================================

st.markdown("""
<style>

/* General typography */
.stApp {
    font-family: 'Segoe UI', sans-serif;
}

/* Hide default Streamlit elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128, 128, 128, 0.2);
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Button styling */
.stButton > button,
.stLinkButton > a {
    border-radius: 9px;
    font-weight: 600;
    transition: 0.2s ease;
}

/* Metric styling */
[data-testid="stMetric"] {
    background-color: rgba(38, 155, 121, 0.05);
    border: 1px solid rgba(38, 155, 121, 0.15);
    padding: 14px;
    border-radius: 12px;
}

/* Expander styling */
[data-testid="stExpander"] {
    border-radius: 10px;
}

/* Mobile responsiveness */
@media screen and (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. SIDEBAR BRANDING
# =====================================================

with st.sidebar:

    st.markdown("---")

    st.title("🔥 FIRELENS")

    st.caption("SATELLITE FIRE RESEARCH PLATFORM")

    st.caption("Version 5.0 | Research Edition")

    st.divider()


# =====================================================
# 4. PAGE NAVIGATION
# =====================================================

pages = {

    "FIRELENS": [

        st.Page(
            "home.py",
            title="Home",
            icon="🏠",
            default=True
        ),

        st.Page(
            "pages/1_Public_Mode.py",
            title="Public Mode",
            icon="🌍"
        ),

        st.Page(
            "pages/7_About_Project.py",
            title="About Project",
            icon="ℹ️"
        ),

        st.Page(
            "pages/8_Data_Sources.py",
            title="Data Sources",
            icon="🛰️"
        ),

    ],

    "Research Workspace": [

        st.Page(
            "pages/6_Research_Mode.py",
            title="Research Mode",
            icon="🔬"
        ),

        st.Page(
            "pages/2_Geographic_Analysis.py",
            title="Geographic Analysis",
            icon="🗺️"
        ),

        st.Page(
            "pages/3_Advanced_Analytics.py",
            title="Advanced Analytics",
            icon="📊"
        ),

        st.Page(
            "pages/4_Data_Quality.py",
            title="Data Quality",
            icon="🛡️"
        ),

        st.Page(
            "pages/5_Research_Insights.py",
            title="Research Insights",
            icon="💡"
        ),

        st.Page(
            "pages/9_Methodology.py",
            title="Research Methodology",
            icon="📚"
        ),

    ],

}


# =====================================================
# 5. APPLICATION EXECUTION
# =====================================================

navigation = st.navigation(pages)

navigation.run()
