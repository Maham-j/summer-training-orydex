"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    # TODO: Define thresholds and return label.
    if risk_score < 50:
        return "low"
    elif risk_score < 75:
        return "medium"
    else:
        return "high"


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    # TODO: Add risk labels without modifying original records.
    new = []
    for patient in patient_records:
        copy = patient.copy()
        copy["risk_label"] = label_risk(patient["risk_score"])
        new.append(copy)
    return new


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    # TODO: Build and return final report.
    labeled = add_risk_labels(patient_records)
    total = len(patient_records)
    high = [p for p in labeled if p["risk_label"] == "high" and p["active"]]

    by_risk = {}
    for p in labeled:
        label = p["risk_label"]
        if label in by_risk:
            by_risk[label] += 1
        else:
            by_risk[label] = 1
    return {
        "summary": {"total_patients": total},
        "risk_counts": by_risk,
        "active_high_risk_patients": high,
    }


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)

    # TODO: Add assertions after implementing the functions.
    report = build_triage_report(patients)
    print(report)

    # assertions
    assert report["total"] == 4
    assert report["by_risk"]["high"] == 2
    assert len(report["high_risk_active"]) == 2
    print("All assertions passed!")
