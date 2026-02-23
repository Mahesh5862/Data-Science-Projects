import json


def parse_age(age_string):
    if age_string is None:
        return None
    return int(age_string.split()[0])


def load_trials(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    trials = []

    for study in data.get("studies", []):
        try:
            protocol = study["protocolSection"]

            nct_id = protocol["identificationModule"]["nctId"]
            conditions = protocol["conditionsModule"].get("conditions", [])
            eligibility = protocol["eligibilityModule"]

            min_age = parse_age(eligibility.get("minimumAge"))
            max_age = parse_age(eligibility.get("maximumAge"))
            criteria = eligibility.get("eligibilityCriteria", "")

            trials.append({
                "nct_id": nct_id,
                "conditions": conditions,
                "min_age": min_age,
                "max_age": max_age,
                "criteria": criteria
            })

        except:
            continue

    return trials


def match_trials(patient_data, trials):

    evaluated = []
    patient_conditions = [c.lower() for c in patient_data["conditions"]]

    for trial in trials:

        score = 0
        condition_match = False
        age_match = True  # default True if no age restriction

        # ---------------- CONDITION MATCH ----------------
        for trial_condition in trial["conditions"]:
            trial_condition_lower = trial_condition.lower()

            for pc in patient_conditions:
                pc_core = pc.split(",")[0].strip()

                if pc_core in trial_condition_lower or trial_condition_lower in pc_core:
                    condition_match = True
                    score += 3
                    break

            if condition_match:
                break

        if not condition_match:
            continue

        # ---------------- AGE MATCH ----------------
        min_age = trial.get("min_age")
        max_age = trial.get("max_age")

        if min_age is not None:
            if patient_data["age"] >= min_age:
                score += 1
            else:
                age_match = False

        if max_age is not None:
            if patient_data["age"] <= max_age:
                score += 1
            else:
                age_match = False

        if not age_match:
            continue

        # ---------------- ELIGIBILITY STATUS ----------------
        status = "Eligible" if condition_match and age_match else "Possibly Eligible"

        evaluated.append({
            "nct_id": trial["nct_id"],
            "conditions": trial["conditions"],
            "min_age": min_age,
            "max_age": max_age,
            "score": score,
            "eligibility_status": status,
            "criteria": trial["criteria"]
        })

    evaluated = sorted(evaluated, key=lambda x: x["score"], reverse=True)

    return evaluated