def generate_eligibility_reasoning(patient_data, trial):

    reasoning = []
    reasoning.append("Eligibility Analysis Report")
    reasoning.append("-" * 40)

    # Age reasoning
    
    min_age = trial.get("min_age")
    max_age = trial.get("max_age")

    if min_age is not None and max_age is not None:
        if min_age <= patient_data["age"] <= max_age:
            reasoning.append(
                f"✔ Age {patient_data['age']} is within allowed range {min_age}–{max_age}."
            )
        else:
            reasoning.append(
                f"❌ Age {patient_data['age']} is outside allowed range {min_age}–{max_age}."
            )
    else:
        reasoning.append("⚠ Age criteria not available in trial data.")
    # Condition reasoning
    matched_condition = False

    for condition in trial["conditions"]:
        condition_lower = condition.lower()

        for pc in patient_data["conditions"]:
            pc_clean = pc.strip().split(",")[0].lower()

            if pc_clean in condition_lower or condition_lower in pc_clean:
                reasoning.append(
                    f"✔ Condition '{pc_clean}' matches trial condition '{condition}'."
                )
                matched_condition = True

    if not matched_condition:
        reasoning.append("❌ No matching condition found.")

    reasoning.append("\nFinal Decision: Possibly Eligible (manual review required).")

    # 🔥 IMPORTANT: MUST RETURN STRING
    return "\n".join(reasoning)