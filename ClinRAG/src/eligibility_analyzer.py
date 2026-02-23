import re


def extract_bmi(patient_data):
    for obs in patient_data["observations"]:
        for key in obs:
            if "body mass index" in key.lower():
                return obs[key]
    return None


def check_bmi_exclusion(criteria_text, patient_data):
    bmi = extract_bmi(patient_data)
    if bmi is None:
        return None

    # Look for BMI limit in criteria
    match = re.search(r"bmi\s*[>≥]\s*(\d+)", criteria_text.lower())
    if match:
        limit = float(match.group(1))
        if bmi > limit:
            return f"Excluded: BMI {bmi} exceeds limit {limit}"
        else:
            return f"BMI {bmi} within allowed limit {limit}"

    return None


def analyze_trial_eligibility(patient_data, trial):
    report = []

    criteria_text = trial["criteria"]

    # BMI check
    bmi_check = check_bmi_exclusion(criteria_text, patient_data)
    bmi = extract_bmi(patient_data)
    if bmi is not None:
        report.append(f"Patient BMI: {bmi}")
        if bmi_check:
            report.append(bmi_check)

    # Age check (extra safety)
    if trial["min_age"] and patient_data["age"] < trial["min_age"]:
        report.append("Excluded: Below minimum age")

    if trial["max_age"] and patient_data["age"] > trial["max_age"]:
        report.append("Excluded: Above maximum age")

    if not report:
        report.append("No obvious exclusion detected")

    return report