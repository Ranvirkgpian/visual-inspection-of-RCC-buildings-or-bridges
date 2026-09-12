import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="RCC Visual Inspection Dashboard",
    page_icon="🏗️",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "observations" not in st.session_state:
    st.session_state.observations = []

# -----------------------------
# Title
# -----------------------------
st.title("🏗️ RCC Visual Inspection Dashboard")
st.caption("AI/ML-SIS Vibe Coding Assignment – RCC Structure Visual Inspection")

# -----------------------------
# Structure Information
# -----------------------------
st.header("1. Structure Information")

col1, col2, col3 = st.columns(3)

with col1:
    structure_id = st.text_input(
        "Structure ID",
        value="RCC-001"
    )

with col2:
    inspection_date = st.date_input(
        "Inspection Date",
        value=date.today()
    )

with col3:
    inspector = st.text_input(
        "Inspector Name"
    )

structure_type = st.selectbox(
    "Structure Type",
    [
        "G+2 RCC Residential Building",
        "RCC T-Beam Bridge"
    ]
)

# -----------------------------
# Observation Input
# -----------------------------
st.header("2. Add Inspection Observation")

col1, col2 = st.columns(2)

with col1:
    floor = st.selectbox(
        "Floor / Level",
        [
            "Ground Floor",
            "First Floor",
            "Second Floor",
            "Roof",
            "External Area",
            "Foundation/Plinth"
        ]
    )

    component = st.selectbox(
        "Component",
        [
            "Column",
            "Beam",
            "Floor Slab",
            "Roof Slab",
            "Staircase",
            "Balcony/Projection",
            "Masonry Wall/Interface",
            "Foundation/Plinth",
            "External RCC Surface"
        ]
    )

    location = st.text_input(
        "Location",
        placeholder="Example: Grid A-2 east face"
    )

with col2:
    defect = st.selectbox(
        "Defect Type",
        [
            "Cracks",
            "Spalling",
            "Exposed Reinforcement",
            "Corrosion Staining",
            "Dampness/Leakage",
            "Honeycombing",
            "Deformation",
            "Surface Deterioration",
            "No Significant Visible Defect",
            "Other"
        ]
    )

    severity = st.selectbox(
        "Severity / Condition",
        [
            "Good",
            "Minor",
            "Moderate",
            "Severe"
        ]
    )

    action = st.selectbox(
        "Recommended Action",
        [
            "Routine Monitoring",
            "Routine Maintenance",
            "Repair / Maintenance Attention",
            "Detailed Inspection / NDT Recommended",
            "Urgent Professional Assessment"
        ]
    )

remarks = st.text_area(
    "Remarks",
    placeholder="Describe the observed condition..."
)

if st.button("➕ Add Observation", type="primary"):

    observation = {
        "Floor": floor,
        "Component": component,
        "Location": location,
        "Defect": defect,
        "Severity": severity,
        "Recommended Action": action,
        "Remarks": remarks
    }

    st.session_state.observations.append(observation)

    st.success("Observation added successfully.")

# -----------------------------
# Sample Cases
# -----------------------------
st.header("3. Sample Test Cases")

if st.button("Load Sample Cases"):

    st.session_state.observations = [

        {
            "Floor": "Ground Floor",
            "Component": "Column",
            "Location": "Grid A-2 east face",
            "Defect": "Cracks",
            "Severity": "Minor",
            "Recommended Action": "Routine Monitoring",
            "Remarks": "Fine visible crack observed."
        },

        {
            "Floor": "First Floor",
            "Component": "Beam",
            "Location": "Grid B-3 soffit",
            "Defect": "Spalling",
            "Severity": "Moderate",
            "Recommended Action": "Repair / Maintenance Attention",
            "Remarks": "Concrete spalling observed at beam soffit."
        },

        {
            "Floor": "Second Floor",
            "Component": "Column",
            "Location": "Grid C-1 external face",
            "Defect": "Corrosion Staining",
            "Severity": "Moderate",
            "Recommended Action": "Detailed Inspection / NDT Recommended",
            "Remarks": "Rust staining indicates possible reinforcement corrosion."
        },

        {
            "Floor": "Roof",
            "Component": "Roof Slab",
            "Location": "NW corner",
            "Defect": "Dampness/Leakage",
            "Severity": "Severe",
            "Recommended Action": "Urgent Professional Assessment",
            "Remarks": "Significant dampness and leakage observed."
        },

        {
            "Floor": "Ground Floor",
            "Component": "Staircase",
            "Location": "Central stair flight",
            "Defect": "No Significant Visible Defect",
            "Severity": "Good",
            "Recommended Action": "Routine Monitoring",
            "Remarks": "No significant visible defect observed."
        }
    ]

    st.success("Sample cases loaded.")

# -----------------------------
# Observation Table
# -----------------------------
st.header("4. Inspection Observations")

if st.session_state.observations:

    df = pd.DataFrame(st.session_state.observations)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.info("No observations added yet.")

# -----------------------------
# Condition Index
# -----------------------------
st.header("5. Visual Condition Summary")

if st.session_state.observations:

    df = pd.DataFrame(st.session_state.observations)

    severity_penalty = {
        "Good": 0,
        "Minor": 1,
        "Moderate": 3,
        "Severe": 5
    }

    df["Penalty"] = df["Severity"].map(severity_penalty)

    average_penalty = df["Penalty"].mean()

    condition_index = max(
        0,
        min(100, 100 - average_penalty * 20)
    )

    total = len(df)
    severe = len(df[df["Severity"] == "Severe"])
    moderate = len(df[df["Severity"] == "Moderate"])
    attention = len(
        df[
            df["Severity"].isin(
                ["Moderate", "Severe"]
            )
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Observations",
        total
    )

    col2.metric(
        "Severe",
        severe
    )

    col3.metric(
        "Moderate",
        moderate
    )

    col4.metric(
        "Need Attention",
        attention
    )

    st.metric(
        "Visual Condition Index",
        f"{condition_index:.1f}/100"
    )

    # Recommendation
    if severe > 0:
        st.error(
            "⚠️ Recommendation: Urgent professional assessment "
            "is recommended because severe observations were recorded."
        )

    elif moderate > 0:
        st.warning(
            "⚠️ Recommendation: Repair/maintenance attention "
            "and detailed inspection should be considered."
        )

    else:
        st.success(
            "✅ Recommendation: Condition appears generally good "
            "based on the recorded visual observations."
        )

    st.caption(
        "Note: The Visual Condition Index is a documentation and "
        "prioritisation aid only. It is not a structural safety assessment."
    )

# -----------------------------
# CSV Export
# -----------------------------
st.header("6. Export Report")

if st.session_state.observations:

    df = pd.DataFrame(st.session_state.observations)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Observations as CSV",
        data=csv,
        file_name="rcc_inspection_observations.csv",
        mime="text/csv"
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "RCC Visual Inspection Dashboard | "
    "Developed using Python and Streamlit"
)
