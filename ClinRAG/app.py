import streamlit as st
import pandas as pd


from src.reverse_trial_matcher import find_eligible_patients_for_trial
from src.data_loader import load_patient_data
from src.disease_normalizer import load_icd_codes, normalize_conditions
from src.dynamic_trial_fetcher import fetch_trials
from src.trial_matcher import load_trials, match_trials
from src.rag_eligibility_engine import generate_eligibility_reasoning
from src.risk_scoring import calculate_risk_score
from src.risk_disclosure import generate_risk_disclosure

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="ClinRAG™",
    page_icon="🏥",
    layout="wide"
)

# ================== PROFESSIONAL UI STYLE ==================

st.markdown("""
<style>

/* Background */
body {
    background-color: #0b1420;
}

/* Header */
.header-container {
    padding: 30px;
    border-radius: 16px;
    background: linear-gradient(90deg, #0f4c81, #002147);
    color: white;
    text-align: center;
    margin-bottom: 40px;
}

/* Main Title */
.main-title {
    font-size: 56px;
    font-weight: 800;
    color: white;
}

/* Subtitle */
.subtitle {
    font-size: 20px;
    color: #d9e6f2;
}

/* Section Headers */
h2, h3 {
    color: #1e90ff !important;
}

/* Buttons */
div.stButton > button {
    background-color: #1e90ff;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px 25px;
    border: none;
}

div.stButton > button:hover {
    background-color: #187bcd;
}

</style>
""", unsafe_allow_html=True)

# ================== HEADER ==================

st.markdown("""
<div class="header-container">
    <div class="main-title">ClinRAG™</div>
    <div class="subtitle">
        AI-Powered Clinical Trial Recruitment Intelligence System
    </div>
</div>
""", unsafe_allow_html=True)

# ================== MODE SELECTION ==================

mode = st.radio(
    "Select System Mode",
    ["Patient Screening", "Trial Recruitment"]
)

# ======================================================
# 🟢 MODE 1 — PATIENT SCREENING
# ======================================================

if mode == "Patient Screening":

    st.header("Patient → Trial Screening")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    patients_folder = os.path.join(BASE_DIR, "data", "ehr_samples")
    patient_files = os.listdir(patients_folder)

    selected_patient_file = st.selectbox(
        "Select Patient Record",
        patient_files
    )

    patient_path = os.path.join(patients_folder, selected_patient_file)
    patient = load_patient_data(patient_path)

    icd_path = os.path.join(BASE_DIR, "data", "icd_mapping", "icd10cm_codes_2025.txt")
    icd_dict = load_icd_codes(icd_path)
    normalized = normalize_conditions(patient["conditions"], icd_dict)
    patient["conditions"] = [n["normalized"] for n in normalized]

    st.subheader("Patient Details")
    st.write("Age:", patient["age"])
    st.write("Gender:", patient["gender"])
    st.write("Conditions:", patient["conditions"])

    if patient["conditions"]:

        selected_condition = st.selectbox(
            "Select Condition",
            patient["conditions"]
        )

        if st.button("Find Matching Trials"):

            save_file = os.path.join(BASE_DIR, "data", "clinical_trials", "dynamic_trials.json")
            fetch_trials(selected_condition, save_file)

            #save_file = os.path.join(BASE_DIR, "data", "clinical_trials", "dynamic_trials.json")
            trials = load_trials(save_file)
            matches = match_trials(patient, trials)

            if matches:

                df = pd.DataFrame(matches)
                st.dataframe(df[["nct_id", "score", "eligibility_status"]])

                selected_trial = matches[0]

                st.subheader("Top Trial Details")
                st.write("Trial ID:", selected_trial["nct_id"])
                st.write("Score:", selected_trial["score"])
                st.write("Eligibility:", selected_trial["eligibility_status"])

                explanation = generate_eligibility_reasoning(patient, selected_trial)
                risk_result = calculate_risk_score(patient, selected_trial, explanation)

                with st.expander("AI Eligibility Explanation"):
                    st.write(explanation)

                st.write("Risk Level:", risk_result["risk_level"])
                st.write("Confidence:", risk_result["confidence"])

            else:
                st.warning("No trials found.")


# ======================================================
# 🔵 MODE 2 — TRIAL RECRUITMENT
# ======================================================
# ======================================================
# 🔵 MODE 2 — TRIAL RECRUITMENT
# ======================================================

if mode == "Trial Recruitment":

    st.header("Trial → Patient Recruitment Engine")

    # ---------------- GET ALL DISEASES FROM PATIENT DATABASE ----------------

    patients_folder = os.path.join(BASE_DIR, "data", "ehr_samples")
    patient_files = os.listdir(patients_folder)

    all_conditions = []

    for file in patient_files:
        patient_path = os.path.join(patients_folder, file)
        patient = load_patient_data(patient_path)
        all_conditions.extend(patient.get("conditions", []))

    # Remove duplicates
    unique_conditions = sorted(list(set(all_conditions)))

    # Disease Dropdown
    selected_disease = st.selectbox(
        "Select Disease",
        unique_conditions
    )

    if st.button("Search Clinical Trials"):

        save_file = "data/clinical_trials/dynamic_trials.json"
        fetch_trials(selected_disease, save_file)

        trials = load_trials(save_file)

        if trials:

            trial_ids = [t["nct_id"] for t in trials]

            selected_trial_id = st.selectbox(
                "Select Trial",
                trial_ids
            )

            selected_trial = next(
                t for t in trials if t["nct_id"] == selected_trial_id
            )

            st.subheader("Selected Trial Details")
            st.write("Trial ID:", selected_trial["nct_id"])
            st.write("Min Age:", selected_trial.get("min_age"))
            st.write("Max Age:", selected_trial.get("max_age"))
            st.write("Conditions:", selected_trial["conditions"])

            st.subheader("Scanning Patient Database...")

            eligible_patients = find_eligible_patients_for_trial(selected_trial)

            if eligible_patients:
                df = pd.DataFrame(eligible_patients)
                st.dataframe(df, width="stretch")
            else:
                st.warning("No eligible patients found.")

        else:
            st.warning("No trials retrieved.")

# ================== FOOTER ==================

st.markdown("---")
st.caption(generate_risk_disclosure())
