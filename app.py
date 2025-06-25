import streamlit as st
from datetime import date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(
    page_title="Roofing Estimate Pro",
    page_icon=":house_with_garden:",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {background-color: #eef3fa;}
    .main-card {
        background: #f7faff;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.12);
        padding: 2rem 2.5rem 2rem 2.5rem;
        margin-top: 1rem;
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 1.5em;
        color: #273c75;
    }
    .streamlit-expanderContent {
        background-color: #f4f7fb !important;
        color: #273c75 !important;
        border-radius: 12px !important;
        padding: 1.2em !important;
    }
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        color: #2d98da !important;
    }
    /* Make all widget labels dark and bold for better readability */
    label, .stTextInput>label, .stSelectbox>label, .stNumberInput>label, .stRadio>label {
        color: #222 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #2d98da;'>Roofing Estimate Pro</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Expert Roofing. Honest Estimates.")
    st.caption("Quick, reliable, and professional roof estimates.")
    st.divider()

    # 1. Property Details
    st.markdown('<div class="section-header">🏠 Property Details</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        property_type = st.selectbox("Property Type", ["Residential", "Commercial"])
        roof_type = st.selectbox("Roof Type", ["Pitched", "Flat", "Other"])
        stories = st.number_input("Number of Stories", min_value=1, max_value=5, value=2)
    with col2:
        complexity = st.selectbox(
            "Roof Complexity", ["Simple (1-2 planes)", "Average (Some valleys/dormers)", "Complex (Many planes, valleys, dormers)"]
        )
        accessibility = st.selectbox("Roof Accessibility", ["Easy", "Moderate", "Difficult"])
        install_date = st.date_input("Preferred Start Date", value=date.today())
    # Roof overview photos uploader (after 'complexity' input)
    roof_overview_photos = st.file_uploader(
        "Upload overall roof photos (optional):",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="roof_overview_photos"
    )
    if roof_overview_photos:
        st.markdown("**Photo preview:**")
        for img in roof_overview_photos:
            st.image(img, width=200)

    st.divider()

    # 2. Roof Measurements
    st.markdown('<div class="section-header">📏 Roof Measurements</div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        area = st.number_input("Total Roof Area (sq. ft.)", min_value=0, step=100, value=2000)
        pitch = st.selectbox("Roof Pitch", ["Low", "Medium", "Steep"])
    with col4:
        perimeter = st.number_input("Roof Perimeter (ft)", min_value=0, step=10, value=180)
        edge_length = st.number_input("Edge/Trim Length (ft)", min_value=0, step=10, value=80)

    st.divider()

    # 3. Material Choices
    st.markdown('<div class="section-header">🧱 Material Choices</div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    with col5:
        shingle = st.selectbox("Shingle/Material Type", ["Asphalt", "Metal", "Clay Tile", "Slate", "Wood Shake", "Synthetic", "Other"])
        underlayment = st.selectbox("Underlayment Type", ["Standard", "Premium"])
        insulation = st.radio("Add Insulation?", ["Yes", "No"])
    with col6:
        gutter = st.radio("Replace Gutters/Downspouts?", ["Yes", "No"])
        flashing = st.number_input("Flashing Required (ft)", min_value=0, step=5, value=50)
        ventilation = st.radio("Roof Ventilation Upgrade?", ["Yes", "No"])

    st.divider()

    # 4. Existing Roof Assessment
    st.markdown('<div class="section-header">🔎 Existing Roof Assessment</div>', unsafe_allow_html=True)
    col7, col8 = st.columns(2)
    with col7:
        removal_needed = st.radio("Remove Existing Roof?", ["Yes", "No"])
        # Custom logic for roof_layers selectbox
        if removal_needed == "Yes":
            roof_layers = st.selectbox("Number of Roof Layers to Remove", [1, 2, 3], index=0)
        else:
            roof_layers = 0
        decking = st.selectbox("Roof Decking Condition", ["Good", "Minor Repairs Needed", "Replace Decking"])
    with col8:
        damage = st.text_area("Visible Damage (rot, leaks, mold)?", height=68)
        # Damage photos uploader (after 'damage' input)
        damage_photos = st.file_uploader(
            "Upload photos of visible roof damage (if any):",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="damage_photos"
        )
        if damage_photos:
            st.markdown("**Photo preview:**")
            for img in damage_photos:
                st.image(img, width=200)
        special_equipment = st.radio("Special Equipment Required?", ["No", "Crane", "Scaffold", "Other"])
        # Special equipment photos uploader (after 'special_equipment' input)
        special_photos = st.file_uploader(
            "Upload photos showing roof accessibility/complexity (optional):",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="special_photos"
        )
        if special_photos:
            st.markdown("**Photo preview:**")
            for img in special_photos:
                st.image(img, width=200)

    st.divider()

    # 5. Add-ons / Upgrades
    st.markdown('<div class="section-header">✨ Add-ons & Upgrades</div>', unsafe_allow_html=True)
    col9, col10 = st.columns(2)
    with col9:
        skylight = st.radio("Skylight Install/Replace?", ["No", "Yes"])
        solar = st.radio("Solar Panel Prep/Install?", ["No", "Prep Only", "Install"])
    with col10:
        ice_shield = st.radio("Ice & Water Shield?", ["Yes", "No"])
        notes = st.text_area("Additional Notes / Requests", placeholder="Let us know about any unique requirements...")

    st.divider()

    # 6. Customer Contact Info
    st.markdown('<div class="section-header">📞 Contact Information</div>', unsafe_allow_html=True)
    cust_name = st.text_input("Full Name")
    cust_email = st.text_input("Email Address")
    cust_phone = st.text_input("Phone Number")
    address = st.text_area("Project Address")

    st.divider()

    # Button
    submit = st.button("Get Instant Estimate 🚀")

    # --- Simple estimate logic ---
    def calc_material_cost():
        base_cost = {
            "Asphalt": 3,
            "Metal": 7,
            "Clay Tile": 10,
            "Slate": 12,
            "Wood Shake": 8,
            "Synthetic": 6,
            "Other": 7,
        }
        cost_per_sqft = base_cost[shingle]
        if underlayment == "Premium":
            cost_per_sqft += 0.75
        if insulation == "Yes":
            cost_per_sqft += 0.7
        return cost_per_sqft * area

    def calc_labor_cost():
        labor_per_sqft = 2.5
        if pitch == "Steep":
            labor_per_sqft += 1.2
        if complexity == "Complex (Many planes, valleys, dormers)":
            labor_per_sqft += 0.8
        if accessibility == "Difficult":
            labor_per_sqft += 1.0
        return labor_per_sqft * area

    def calc_addons():
        addons = 0
        if removal_needed == "Yes":
            addons += roof_layers * area * 0.6
        if gutter == "Yes":
            addons += perimeter * 7
        if skylight == "Yes":
            addons += 1200
        if solar == "Install":
            addons += 3500
        elif solar == "Prep Only":
            addons += 700
        if ventilation == "Yes":
            addons += 400
        if ice_shield == "Yes":
            addons += 500
        if special_equipment != "No":
            addons += 500
        if flashing > 0:
            addons += flashing * 3
        return addons

    def calc_total():
        material = calc_material_cost()
        labor = calc_labor_cost()
        addons = calc_addons()
        fees = 350
        waste = area * 0.2
        total = material + labor + addons + fees + waste
        return material, labor, addons, fees, waste, total

    def save_to_sheet(row_data):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('roofing-estimator-app-55e6691c472f.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_key("1VtlMgjNNc2PgCxbtHn6Yi4Ovrjf0IJP69zijvogAi-Q").sheet1
        sheet.append_row(row_data)

    if submit:
        if not cust_name or not cust_email or not address:
            st.warning("Please fill in your name, email, and project address to receive an estimate.")
        else:
            material, labor, addons, fees, waste, total = calc_total()
            st.success("✅ Estimate Ready!")
            st.markdown(
                f"<div style='background-color:#eafaf1; color:#20bf6b; border-radius:10px; text-align:center; font-size:1.4rem; padding:0.7em 0; margin-bottom:10px;'><b>Total Estimate: ${total:,.2f}</b></div>",
                unsafe_allow_html=True
            )
            with st.expander("See Full Estimate Breakdown"):
                st.markdown(
                    f"""
                    <div style='color:#273c75; font-size: 1.05rem;'>
                    <ul>
                        <li><b>Materials:</b> ${material:,.2f}</li>
                        <li><b>Labor:</b> ${labor:,.2f}</li>
                        <li><b>Add-ons/Upgrades:</b> ${addons:,.2f}</li>
                        <li><b>Permit/Inspection Fees:</b> ${fees:,.2f}</li>
                        <li><b>Waste Disposal:</b> ${waste:,.2f}</li>
                        <hr style="border: 1px solid #c9d6ec;">
                        <li><b>Total:</b> <span style="color:#20bf6b; font-size:1.12rem">${total:,.2f}</span></li>
                    </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.info(
                "This is a preliminary estimate. Final pricing may vary based on onsite inspection and final measurements. Our team will reach out to confirm your requirements."
            )
            row_data = [
                cust_name, cust_email, cust_phone, address,
                property_type, roof_type, stories, complexity, accessibility, str(install_date),
                area, pitch, perimeter, edge_length, shingle, underlayment, insulation, gutter,
                flashing, ventilation, removal_needed, roof_layers, decking, damage, special_equipment,
                skylight, solar, ice_shield, notes, material, labor, addons, fees, waste, total
            ]
            save_to_sheet(row_data)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 2em; color: #95a5a6;">
        Roofing Estimate Pro &copy; 2025 | Powered by Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)