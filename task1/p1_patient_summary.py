"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]


def total_patients(patient_records):
    """Return the total number of patients."""
    return len(patient_records)
    
    


def average_age(patient_records):
    """Return the average patient age."""
    ages = [patient["age"]for patient in patient_records]
    t_patients = len(patients)
    t_age = sum(ages)
    average = t_age/t_patients
    return average
    
   
    

def count_active_patients(patient_records):
    """Return the number of active patients."""
    activate = [patient["active"] for patient in patient_records if patient["active"] == True ]
    return len(activate)


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    con = [patient["condition"]for patient in patient_records]
    unique = set(con)
    return sorted(list(unique))

def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    diction = {}
    for patient in patient_records:
        if patient["condition"] in diction:
            diction[patient["condition"]] += 1
        else:
            diction[patient["condition"]] = 1
            
    return diction
    


if __name__ == "__main__":
    print("Total_patients: ", total_patients(patients))
    print("Average_age: ",average_age(patients))
    print("Active_patients: ",count_active_patients(patients))
    print("Unique_conditions: ",unique_conditions(patients))
    print("Count_by_condition: ",count_by_condition(patients))
