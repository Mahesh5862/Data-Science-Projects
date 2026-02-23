import os
from data_loader import load_patient_data
from trial_matcher import match_trials


def find_eligible_patients_for_trial(trial):

    # 🔥 Get absolute project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    patients_folder = os.path.join(BASE_DIR, "data", "ehr_samples")

    # 🔥 Safety check (important for Streamlit Cloud)
    if not os.path.exists(patients_folder):
        print("Patients folder not found:", patients_folder)
        return []

    eligible_patients = []

    for file in os.listdir(patients_folder):

        # Skip non-JSON files
        if not file.endswith(".json"):
            continue

        patient_path = os.path.join(patients_folder, file)

        try:
            patient = load_patient_data(patient_path)

            # Safety check for required keys
            if "age" not in patient or "conditions" not in patient:
                continue

            matches = match_trials(patient, [trial])

            if matches:
                eligible_patients.append({
                    "patient_id": file,
                    "age": patient.get("age"),
                    "conditions": patient.get("conditions"),
                    "score": matches[0].get("score", 0)
                })

        except Exception as e:
            # Skip broken patient files safely
            continue

    # Sort by best score
    eligible_patients = sorted(
        eligible_patients,
        key=lambda x: x["score"],
        reverse=True
    )

    return eligible_patients
