def calculate_risk_score(patient, trial, explanation):

    score = 0
    max_score = 5

    min_age = trial.get("min_age")
    max_age = trial.get("max_age")

    # Safe Age Check
    if min_age is not None and max_age is not None:
        if min_age <= patient["age"] <= max_age:
            score += 1

    # Condition match check
    matched = False
    for condition in trial.get("conditions", []):
        condition_lower = condition.lower()
        for pc in patient.get("conditions", []):
            pc_clean = pc.strip().split(",")[0].lower()
            if pc_clean in condition_lower or condition_lower in pc_clean:
                matched = True
                score += 2
                break
        if matched:
            break

    # Basic reasoning bonus
    if "✔" in explanation:
        score += 1

    confidence = round(score / max_score, 2)

    if confidence >= 0.7:
        risk_level = "LOW"
    elif confidence >= 0.4:
        risk_level = "MODERATE"
    else:
        risk_level = "HIGH"

    return {
        "risk_level": risk_level,
        "confidence": confidence
    }