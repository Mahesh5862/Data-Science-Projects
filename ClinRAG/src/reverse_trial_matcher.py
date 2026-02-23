import os
from src.data_loader import load_patient_data
from src.trial_matcher import match_trials


def find_eligible_patients_for_trial(trial):

    # 🔥 Get absolute project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    patients_folder = os.path.join(BASE_DIR, "data", "ehr_samples")

    # 🔥 Safety check
    if not os.path.exists(patients_folder):
        return []

    eligible_patients = []

    for file in os.listdir(patients_folder):
        patient_path = os.path.join(patients_folder, file)

        patient = load_patient_data(patient_path)
        matches = match_trials(patient, [trial])

        if matches:
            eligible_patients.append({
                "patient_id": file,
                "age": patient["age"],
                "conditions": patient["conditions"],
                "score": matches[0]["score"]
            })

    return eligible_patients
