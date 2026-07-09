"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""
    patient = patients.get(patient_id)
    if patient:
        return patient["contact"]["city"]
    return None


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    patients[patient_id]["condition"] = new_condition





def build_patient_summary():
    """Build and return a summary dictionary."""
    names = []
    conditions = []
    cities = []
    phone_nos = []
    ages = []
    
    for data in patients.values():
        names.append(data["name"])
        conditions.append(data["condition"])
        cities.append(data["contact"]["city"])
        phone_nos.append(data["contact"]["phone"])
        ages.append(data["age"])
    
    total = len(names)
    
    return {
        "total": total,
        "names": names,
        "conditions": conditions,
        "cities": cities,
        "phone_nos": phone_nos,
        "ages": ages,
    }
if __name__ == "__main__":
    print(get_patient_city(2))
    print(patients[1])
    print(build_patient_summary())
