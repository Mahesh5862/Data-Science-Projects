import os
from src.data_loader import load_patient_data
from src.trial_matcher import match_trials


def find_eligible_patients_for_trial(trial, patients_folder="data/ehr_samples"):

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