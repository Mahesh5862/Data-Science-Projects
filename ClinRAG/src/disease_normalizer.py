import re


def clean_condition(condition_text):
    """
    Remove brackets like (disorder), (finding), etc.
    """
    cleaned = re.sub(r"\(.*?\)", "", condition_text)
    return cleaned.strip().lower()


def load_icd_codes(file_path):
    icd_dict = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(" ", 1)

            if len(parts) == 2:
                code = parts[0]
                description = parts[1].lower()
                icd_dict[description] = code

    return icd_dict


def normalize_conditions(patient_conditions, icd_dict):
    normalized = []

    for condition in patient_conditions:
        cleaned = clean_condition(condition)

        for icd_desc in icd_dict.keys():
            if cleaned in icd_desc:
                normalized.append({
                    "original": condition,
                    "normalized": icd_desc,
                    "icd_code": icd_dict[icd_desc]
                })
                break

    return normalized


if __name__ == "__main__":
    from data_loader import load_patient_data
    import os

    patient_file = "../data/ehr_samples/" + os.listdir("../data/ehr_samples/")[0]
    patient = load_patient_data(patient_file)

    icd_dict = load_icd_codes("../data/icd_mapping/icd10cm_codes_2025.txt")

    normalized = normalize_conditions(patient["conditions"], icd_dict)

    print("Normalized Conditions:")
    for n in normalized:
        print(n)