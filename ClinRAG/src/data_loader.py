import json
from datetime import datetime


def calculate_age(birth_date):
    birth = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    return today.year - birth.year - (
        (today.month, today.day) < (birth.month, birth.day)
    )


def load_patient_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    patient_info = {
        "age": None,
        "gender": None,
        "id": None,
        "conditions": [],
        "observations": []
    }

    if data["resourceType"] == "Bundle":
        for entry in data["entry"]:
            resource = entry["resource"]

            # PATIENT
            if resource["resourceType"] == "Patient":
                birth_date = resource.get("birthDate", None)
                gender = resource.get("gender", None)
                patient_id = resource.get("id", None)

                if birth_date:
                    age = calculate_age(birth_date)
                else:
                    age = None

                patient_info["age"] = age
                patient_info["gender"] = gender
                patient_info["id"] = patient_id

            # CONDITIONS
            elif resource["resourceType"] == "Condition":
                try:
                    condition = resource["code"]["coding"][0]["display"]
                    patient_info["conditions"].append(condition)
                except:
                    pass

            # OBSERVATIONS
            elif resource["resourceType"] == "Observation":
                try:
                    obs_name = resource["code"]["coding"][0]["display"]
                    value = resource.get("valueQuantity", {}).get("value", None)

                    if value:
                        patient_info["observations"].append(
                            {obs_name: value}
                        )
                except:
                    pass

    return patient_info