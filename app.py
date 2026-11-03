
import streamlit as st

# ==================================================
# FIRELENS V5 — MAIN NAVIGATION
# ==================================================

st.set_page_config(
    page_title="FIRELENS | Satellite Fire Research",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# GLOBAL BRANDING
# --------------------------------------------------

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,0.2);
}

[data-testid="stSidebar"] h1 {
    color: #269b79;
}

.stApp {
    font-family: 'Segoe UI', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION STRUCTURE
# --------------------------------------------------

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
    ],
}

# --------------------------------------------------
# RUN NAVIGATION
# --------------------------------------------------

navigation = st.navigation(pages)
navigation.run()
