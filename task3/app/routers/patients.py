from fastapi import APIRouter, HTTPException, Depends
from app.models import PatientRead, PatientCreate, PatientUpdate, Patient
from sqlmodel import Session, select
from app.database import get_session
from app.auth import get_current_user



router = APIRouter(prefix = "/patients", tags=["patients"])


@router.get("/", status_code=200)
def get_patients(active: bool | None = None, condition: str | None = None, limit: int = 10, offset: int = 0, session: Session = Depends(get_session)):
    query = select(Patient)
    
    if active is not None:
        query = query.where(Patient.active == active)
    
    if condition is not None:
        query = query.where(Patient.condition == condition)
    
    results = session.exec(query.offset(offset).limit(limit)).all()
    return results


@router.get("/{patient_id}", status_code=200)
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/", status_code=201)
def post_patient(patient: PatientCreate, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    new_patient = Patient(**patient.model_dump())
    session.add(new_patient)
    session.commit()
    session.refresh(new_patient)
    return new_patient


@router.put("/{patient_id}", status_code=200)
def put_patient(patient_id: int, updated_patient: PatientCreate, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    for key, value in updated_patient.model_dump().items():
        setattr(patient, key, value)
    
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.put("/{patient_id}", status_code=200)
def put_patient(patient_id: int, updated_patient: PatientCreate, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    for key, value in updated_patient.model_dump().items():
        setattr(patient, key, value)
    
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient


@router.delete("/{patient_id}", status_code=204)
def delete_patient(patient_id: int, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    session.delete(patient)
    session.commit()
    return None