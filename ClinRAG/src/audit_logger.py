import csv
from datetime import datetime


def log_trial_evaluation(patient, trial, risk_result):

    file_path = "../audit_log.csv"

    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            patient["id"],
            trial["nct_id"],
            risk_result["raw_score"],
            risk_result["confidence"],
            risk_result["risk_level"]
        ])