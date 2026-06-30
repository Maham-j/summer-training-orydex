from fastapi import APIRouter, HTTPException
from app.models import PatientRead
from app.models import PatientCreate
from app.models import PatientUpdate


router = APIRouter(prefix = "/patients", tags=["patients"])

patients: list[PatientRead] = []


@router.get("/", status_code=200)
def get_patients(active: bool | None = None, condition: str | None = None, limit: int = 10, offset: int = 0):
    results = patients

    if active is not None:
        result = [p for p in results if p.active == active]

    if condition is not None:
        results = [p for p in results if p.condition == condition]
    
    return results[offset: offset+limit]


@router.get("/{patient_id}", status_code=200)
def get_patients(patient_id: int):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not Found")   

@router.post("/", status_code=201)
def post_patient(patient: PatientCreate):
    new_patient = PatientRead(id=len(patients) + 1, **patient.model_dump())
    patients.append(new_patient)
    return new_patient
  
@router.put("/{patient_id}", status_code=200)
def put_patient(patient_id: int, updated_patient: PatientCreate):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            new_patient = PatientRead(id=patient_id, **updated_patient.model_dump())
            patients[index] = new_patient
            return new_patient   

    raise HTTPException(status_code=404, detail="The id not Found")



@router.patch("/{patient_id}", status_code=200)
def patch_patient(patient_id: int, updated_patient: PatientUpdate):
    for index, patient in enumerate(patients):
        if patient.id == patient_id:
            existing_data = patient.model_dump()
            update_data = updated_patient.model_dump(exclude_unset=True)
            existing_data.update(update_data)
            new_patient = PatientRead(**existing_data)
            patients[index] = new_patient
            return new_patient

    raise HTTPException(status_code=404, detail="The id not Found")


@router.delete("/{patient_id}", status_code=204)
def delete_patient(patient_id: int):
    for index,patient in enumerate(patients):
        if patient.id == patient_id:
            patients.pop(index)
            return None   
    raise HTTPException(status_code=404, detail="The id not Found")