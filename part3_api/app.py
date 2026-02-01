from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class BloodPressure(BaseModel):
	# Keep the input within the range
    systolic: int = Field(...,gt=0, lt=300)
    diastolic: int = Field(..., gt=0, lt=300)

class (BaseModel):
    blood_pressure: BloodPressure
    fasting_glucose: int = Field(..., ge=0, le=150)
    bmi: float=Field(..., ge=0, le=100)
    age: int=Field(..., ge=0, le=120)

class RiskAssessmentResponse(BaseModel):
    risk_level: str
    risk_factors: List[str]

def assess_risk(
    systolic: int,
    diastolic: int,
    fasting_glucose: int,
    bmi: float,
)->RiskAssessmentResponse:
    """
    Assess the cardiovascular risk based on provided data
    """
    high_risk = False
    moderate_risk = False
    risk_factors = []


	# Assess logic
    if systolic >= 140 and diastolic >= 90:
        high_risk = True
    elif systolic >= 130 and diastolic >= 80:
        moderate_risk = True
    risk_factors.append(f"Blood pressure elevated ({systolic}/{diastolic} mmHg)")

    if fasting_glucose >= 126:
        high_risk = True
        risk_factors.append(f"Fasting glucose in diabetes threshold range ({fasting_glucose} mg/dL)")
    elif fasting_glucose >= 100:
        moderate_risk = True
        risk_factors.append(f"Fasting glucose in prediabetes range ({fasting_glucose} mg/dL)")
    else:
        risk_factors.append(f"Fasting glucose in range ({fasting_glucose} mg/dL)")

    if bmi >= 30:
        high_risk = True
    elif bmi >= 25:
        moderate_risk = True

    if high_risk == True:
        risk_level = "High Risk"
    elif moderate_risk == True:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    return RiskAssessmentResponse(risk_level=risk_level, risk_factors=risk_factors)
    

@app.post("/api/assess-cv-risk", response_model = RiskAssessmentResponse)
def assess_cv_risk(request: RiskAssessmentRequest):
    """
    POST endpoint to assess cardiovascular risk
	request should be type of RishAssessmentRequest, asking for complete and valid input
    """
    try:
        blood_pressure = request.blood_pressure
        return assess_risk(
            systolic=blood_pressure.systolic,
            diastolic=blood_pressure.diastolic,
            fasting_glucose=request.fasting_glucose,
            bmi=request.bmi
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))
