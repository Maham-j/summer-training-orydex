from pydantic import BaseModel, Field



class PatientCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=120)
    condition: str = Field(..., min_length=1)
    risk_score: int = Field(..., ge=0, le=100  )
    active: bool = Field(default=True)


class PatientRead(BaseModel):
    id: int 
    name: str  = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=120)
    condition: str = Field(..., min_length=1)
    risk_score: int = Field(..., ge=0, le=100  )
    active: bool = Field(default=True)

class PatientUpdate(BaseModel):
    name: str |None = Field(default=None, min_length=1, max_length=100)
    age: int |None = Field(default=None, ge=0, le=120)
    condition: str |None = Field(default=None, min_length=1)
    risk_score: int |None = Field(default=None, ge=0, le=100  )
    active: bool |None = Field(default=True)