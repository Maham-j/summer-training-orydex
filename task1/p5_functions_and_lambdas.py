"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    # TODO: Implement BMI formula.
    return weight_kg / height_m**2


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    # TODO: Return underweight, normal, overweight, or obese.
    if bmi < 18.5:
        return "underweight"
    elif bmi < 24.9 and bmi > 18.5:
        return "normal"
    elif bmi < 29.9 and bmi > 25:
        return "overweight"
    else:
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    # TODO: Format name.
    return name.title()


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    # TODO: Filter active patients.
    actives = [patient for patient in patient_records if patient["active"]]
    return actives


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    # TODO: Sort patients by weight_kg.
    return sorted(patient_records, key=lambda patient: patient["weight_kg"])


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.
    print(calculate_bmi(68, 1.65))
    print(classify_bmi(25))
    print(format_name("ayesha khan"))
    print(get_active_patients(patients))
    print(sort_patients_by_weight(patients))
