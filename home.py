
import streamlit as st

st.title("🔥 FIRELENS")
st.subheader("Making Satellite Fire Data Understandable and Accessible to Everyone")

st.markdown("""
Welcome to **FIRELENS**, an interactive platform for exploring
satellite-based wildfire detection data.

FIRELENS transforms complex satellite observations into accessible
visualizations and research insights for everyone.
""")

st.divider()

st.header("Explore FIRELENS")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Public Mode")
    st.write("""
    Designed for the general public and anyone who wants to understand
    wildfire activity through simple explanations, maps, and visualizations.
    """)
    st.info("Easy-to-understand data exploration")

with col2:
    st.subheader("🔬 Research Mode")
    st.write("""
    Designed for researchers, academics, and environmental organizations
    who need deeper analytical tools and detailed satellite data insights.
    """)
    st.info("Advanced analysis and research tools")

st.divider()

st.header("About the Project")

st.write("""
FIRELENS explores historical active-fire detection records from
NASA FIRMS MODIS and VIIRS satellite products.

The current research dataset covers Riau and Central Kalimantan,
Indonesia, from August to October 2024.
""")

st.warning("""
**Research note:** FIRELENS presents historical satellite detection
records. It is an exploratory research platform, not a real-time
fire alert system. A satellite detection record does not necessarily
represent a unique wildfire event.
""")

st.divider()

st.caption("FIRELENS | Satellite-Based Wildfire Detection Research Platform")
st.caption("Historical study period: August – October 2024")
