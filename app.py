
import streamlit as st

st.set_page_config(
    page_title="FIRELENS",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

navigation = st.navigation(pages)
navigation.run()
