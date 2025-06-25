import streamlit as st
from estimator import estimate_price

st.set_page_config(page_title="Roofing AI Estimator", layout="centered")

st.title("🏠 Roofing Estimate Calculator - Northern California")
st.markdown("""
Welcome! Instantly estimate your roofing project cost. Enter your project details below and click **Estimate Cost** to get an itemized, AI-powered estimate. 
""")

st.header("Enter Project Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Roof area (sqft)", min_value=100, max_value=10000, value=2000, step=50)
    material = st.selectbox("Roofing Material", ["asphalt", "tile", "metal"], index=0)
    stories = st.number_input("Number of Stories", min_value=1, max_value=5, value=1, step=1)

with col2:
    roof_type = st.selectbox("Roof Type", ["gable", "hip", "flat"], index=0)
    pitch = st.selectbox("Roof Pitch", ["low", "med", "high"], index=0)
    email = st.text_input("Contact Email (optional)")

st.markdown(":arrow_down_small: All estimates are for demonstration only. For a formal quote, contact your local roofing contractor.")

if st.button("Estimate Cost"):
    price = estimate_price(area, material, stories, pitch)
    st.success(f"Estimated Total Cost: **${price:,.2f}**")
    st.markdown(f"**Project Summary:**\n- Area: `{int(area)}` sqft\n- Material: `{material}`\n- Stories: `{int(stories)}`\n- Roof Type: `{roof_type}`\n- Pitch: `{pitch}`")
    st.info("""
**Note:** Actual cost may vary based on roof condition, local code, and site inspection.\nContact us for a detailed, on-site evaluation.
""")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit | 2024")