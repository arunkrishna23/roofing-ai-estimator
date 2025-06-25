# --- Imports ---
# --- Imports ---
import streamlit as st
from datetime import date
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials




st.set_page_config(
    page_title="Roofing Estimate Pro",
    page_icon=":house_with_garden:",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background: url('https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=1500&q=80') no-repeat center center fixed;
        background-size: cover;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: linear-gradient(120deg, rgba(246,211,101,0.12), rgba(32,191,107,0.13) 70%, rgba(45,51,70,0.09));
        pointer-events: none;
        z-index: 0;
        animation: bgfloat 12s linear infinite alternate;
    }
    @keyframes bgfloat {
        0% {background-position: 0% 50%;}
        100% {background-position: 100% 50%;}
    }
    .main-card {
        background: rgba(30, 42, 66, 0.96);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
        padding: 2rem 2.5rem 2rem 2.5rem;
        margin-top: 1rem;
        color: #f4f6fa;
        backdrop-filter: blur(9px) saturate(125%);
        -webkit-backdrop-filter: blur(9px) saturate(125%);
        border: 1.5px solid rgba(246, 211, 101, 0.08);
        animation: fadeinup 1.4s cubic-bezier(.21,1.06,.81,.99);
    }
    @keyframes fadeinup {
        0% {opacity:0; transform:translateY(32px);}
        100% {opacity:1; transform:translateY(0);}
    }
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 1.5em;
        color: #f6d365;
        letter-spacing: 0.03em;
        text-shadow: 0 2px 6px rgba(0,0,0,0.1);
        cursor: default;
    }
    .section-header:hover {
        filter: brightness(1.24) drop-shadow(0 0 16px #f6d365ee);
        transition: filter 0.25s;
    }
    .streamlit-expanderContent {
        background-color: #22304e !important;
        color: #fff !important;
        border-radius: 12px !important;
        padding: 1.2em !important;
    }
    .streamlit-expanderHeader {
        font-weight: 700 !important;
        color: #f6d365 !important;
    }
    /* Make all widget labels bold and bright for readability */
    label, .stTextInput>label, .stSelectbox>label, .stNumberInput>label, .stRadio>label {
        color: #fff !important;
        font-weight: 700 !important;
        font-size: 1.08rem !important;
        text-shadow: 0 1px 6px rgba(0,0,0,0.10);
    }
    /* Make radio button options bold and bright */
    .stRadio div[role="radiogroup"] > div {
        color: #f6d365 !important;
        font-weight: 700 !important;
        font-size: 1.08rem !important;
        text-shadow: 0 1px 6px rgba(0,0,0,0.15);
    }
    /* Make warning/info boxes stand out */
    .stAlert, .stNotification, .stInfo {
        background: #252a38 !important;
        color: #ffd97a !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        border: 1px solid #ffd180 !important;
    }
    h1.animated-header {
        background: linear-gradient(90deg, #f6d365, #20bf6b, #f6d365);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 0.3em;
        user-select: none;
        position: relative;
        overflow: hidden;
    }
    h1.animated-header::after {
        content: "";
        position: absolute;
        top: 0; left: -75%;
        width: 50%;
        height: 100%;
        background: linear-gradient(120deg, rgba(255,255,255,0.18) 0%, rgba(246,211,101,0.35) 60%, rgba(255,255,255,0.12) 100%);
        transform: skewX(-25deg);
        animation: shine 2.8s infinite;
    }
    @keyframes shine {
        0% { left: -75%; }
        80% { left: 120%; }
        100% { left: 120%; }
    }
    .stButton button:hover::after {
        content: "⬇️";
        margin-left: 12px;
    }
    /* Pulse animation for section headers on hover (already present, increase glow) */
    .section-header:hover {
        filter: brightness(1.24) drop-shadow(0 0 16px #f6d365ee);
        transition: filter 0.25s;
    }
    /* Animate the main-card on page load */
    .main-card {
        animation: fadeinup 1.4s cubic-bezier(.21,1.06,.81,.99);
    }
    @keyframes fadeinup {
        0% {opacity:0; transform:translateY(32px);}
        100% {opacity:1; transform:translateY(0);}
    }
    /* Make the Contact Us footer button gently pulse */
    .footer-glow-btn {
        animation: pulseGlow 2.3s infinite alternate;
        box-shadow: 0 2px 14px #f6d36566,0 2px 8px #20bf6b33;
    }
    @keyframes pulseGlow {
        0% {box-shadow: 0 2px 14px #f6d36533,0 2px 4px #20bf6b22;}
        100% {box-shadow: 0 4px 24px #f6d36599,0 2px 16px #20bf6b55;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown("<h1 class='animated-header' style='text-align: center;'>Roofing Estimate Pro</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Expert Roofing. Honest Estimates.")
    st.caption("Quick, reliable, and professional roof estimates.", unsafe_allow_html=True)
    st.markdown("<style> .stCaption {color: #f9fafc !important;} </style>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

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
        damage = st.text_area("Visible Damage (rot, leaks, mold)?", height=68)
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
    with col8:
        # --- Manual Assessment UI grouped together at top of col8 ---
        with st.container():
            st.markdown("**Manual Assessment:** Use the sliders below to rate the % damage in each area.")
            overall_damage = st.slider("Overall Roof Surface Damage (%)", 0, 100, 0, 5)
            decking_damage = st.slider("Decking/Substrate Damage (%)", 0, 100, 0, 5)
            flashing_damage = st.slider("Flashing/Edge Damage (%)", 0, 100, 0, 5)
            gutter_damage = st.slider("Gutter/Downspout Damage (%)", 0, 100, 0, 5)
            vent_damage = st.slider("Ventilation Obstruction/Damage (%)", 0, 100, 0, 5)
            insulation_damage = st.slider("Insulation/Underlayment Damage (%)", 0, 100, 0, 5)
            manual_factors = {
                "Overall Roof Surface Damage (%)": overall_damage,
                "Decking/Substrate Damage (%)": decking_damage,
                "Flashing/Edge Damage (%)": flashing_damage,
                "Gutter/Downspout Damage (%)": gutter_damage,
                "Ventilation Obstruction/Damage (%)": vent_damage,
                "Insulation/Underlayment Damage (%)": insulation_damage,
            }
            avg_damage_percent = sum(manual_factors.values()) / len(manual_factors)
            st.info(f"Average assessed roof damage: **{avg_damage_percent:.1f}%**")
            damage_percent = avg_damage_percent

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
        # Manual assessment: use damage_percent to add proportional surcharge
        if damage_percent and damage_percent > 0:
            addons += (damage_percent / 100) * 2500
        return addons

    def calc_total():
        material = calc_material_cost()
        labor = calc_labor_cost()
        addons = calc_addons()
        fees = 350
        waste = area * 0.2
        total = material + labor + addons + fees + waste
        return material, labor, addons, fees, waste, total

    # def save_to_sheet(row_data):
    #     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    #     creds = ServiceAccountCredentials.from_json_keyfile_name('roofing-estimator-app-55e6691c472f.json', scope)
    #     client = gspread.authorize(creds)
    #     sheet = client.open_by_key("1VtlMgjNNc2PgCxbtHn6Yi4Ovrjf0IJP69zijvogAi-Q").sheet1
    #     sheet.append_row(row_data)

    if submit:
        if not cust_name.strip() or not cust_email.strip() or not address.strip():
            st.warning("Please fill in your name, email, and project address to receive an estimate.")
        else:
            material, labor, addons, fees, waste, total = calc_total()
            st.success("✅ Estimate Ready!")
            st.markdown(
                f"<div style='background-color:#2d3346; color:#f6d365; border-radius:10px; text-align:center; font-size:1.4rem; padding:0.7em 0; margin-bottom:10px;'><b>Total Estimate: ${total:,.2f}</b></div>",
                unsafe_allow_html=True
            )
            with st.expander("See Full Estimate Breakdown"):
                st.markdown(
                    f"""
                    <div style='color:#fff; font-size: 1.05rem;'>
                    <ul>
                        <li><b>Materials:</b> ${material:,.2f}</li>
                        <li><b>Labor:</b> ${labor:,.2f}</li>
                        <li><b>Add-ons/Upgrades:</b> ${addons:,.2f}</li>
                        <li><b>Permit/Inspection Fees:</b> ${fees:,.2f}</li>
                        <li><b>Waste Disposal:</b> ${waste:,.2f}</li>
""",
                    unsafe_allow_html=True
                )
                # Add Manual Damage Surcharge line if applicable
                if damage_percent and damage_percent > 0:
                    st.markdown(
                        f"<li><b>Manual Damage Surcharge:</b> <span style='color:#f6d365;'>${(damage_percent/100)*2500:,.2f}</span> <span style='font-size:0.95em; color:#fff;'>(Manual assessment, {damage_percent:.1f}% average damage)</span></li>",
                        unsafe_allow_html=True
                    )
                st.markdown(
                    """
                        <hr style="border: 1px solid #c9d6ec;">
                        <li><b>Total:</b> <span style="color:#f6d365; font-size:1.12rem">${total:,.2f}</span></li>
                    </ul>
                    </div>
                    """.replace("${total:,.2f}", f"${total:,.2f}"),
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
            # save_to_sheet(row_data)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 2em; color: #95a5a6;">
        Roofing Estimate Pro &copy; 2025 | Powered by Streamlit
        <br>
        <a href="mailto:roofing.ai.estimator@gmail.com" class="footer-glow-btn" style="display:inline-block;margin-top:1em;padding:0.5em 1.6em;background:linear-gradient(92deg,#f6d365,#20bf6b 65%);color:#212b36;font-weight:700;border-radius:22px;text-decoration:none;font-size:1.07rem;letter-spacing:0.01em;transition:box-shadow 0.3s;">Contact Us</a>
    </div>
    """,
    unsafe_allow_html=True,
)