import json


def parse_age(age_string):
    """
    Extract numeric age from strings like '18 Years'
    Returns int or None
    """
    if age_string is None:
        return None

    try:
        return int(age_string.split()[0])
    except:
        return None


def load_trials(file_path):
    """
    Load and normalize trials from ClinicalTrials API JSON
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    trials = []

    for study in data.get("studies", []):
        try:
            protocol = study.get("protocolSection", {})

            identification = protocol.get("identificationModule", {})
            conditions_module = protocol.get("conditionsModule", {})
            eligibility = protocol.get("eligibilityModule", {})

            nct_id = identification.get("nctId")
            conditions = conditions_module.get("conditions", [])

            min_age = parse_age(eligibility.get("minimumAge"))
            max_age = parse_age(eligibility.get("maximumAge"))
            criteria = eligibility.get("eligibilityCriteria", "")

            if nct_id is None:
                continue

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
    """
    Match patient against list of trials
    """

    evaluated = []

    patient_age = patient_data.get("age")
    patient_conditions = [
        c.lower().strip()
        for c in patient_data.get("conditions", [])
        if isinstance(c, str)
    ]

    for trial in trials:

        score = 0
        condition_match = False
        age_match = True  # default True if no restriction

        trial_conditions = trial.get("conditions", [])

        # ---------------- CONDITION MATCH ----------------
        for trial_condition in trial_conditions:
            trial_condition_lower = trial_condition.lower().strip()

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

        if patient_age is not None:

            if min_age is not None:
                if patient_age >= min_age:
                    score += 1
                else:
                    age_match = False

            if max_age is not None:
                if patient_age <= max_age:
                    score += 1
                else:
                    age_match = False

        if not age_match:
            continue

        # ---------------- ELIGIBILITY STATUS ----------------
        status = "Eligible" if condition_match and age_match else "Possibly Eligible"

        evaluated.append({
            "nct_id": trial.get("nct_id"),
            "conditions": trial_conditions,
            "min_age": min_age,
            "max_age": max_age,
            "score": score,
            "eligibility_status": status,
            "criteria": trial.get("criteria", "")
        })

    evaluated = sorted(evaluated, key=lambda x: x["score"], reverse=True)

    return evaluated
