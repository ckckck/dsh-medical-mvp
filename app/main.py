from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI(title="dsh Medical Agent MVP")

class EDPatient(BaseModel):
    pat_name: str
    visit_no: str
    los_hours: float
    bed_code: str | None
    status: str

# Mock data for demo
MOCK_PATIENTS = [
    {"pat_name": "张某", "visit_no": "ED20261119001", "los_hours": 5.2, "bed_code": "R01", "status": "RESCUE"},
    {"pat_name": "李某", "visit_no": "ED20261119002", "los_hours": 3.1, "bed_code": "O12", "status": "OBSERVATION"},
]

@app.get("/api/ed/los-alerts", response_model=List[EDPatient])
def get_ed_los_alerts(threshold_hours: float = 4.0):
    """Return patients with ED length of stay exceeding threshold."""
    return [p for p in MOCK_PATIENTS if p["los_hours"] > threshold_hours]

@app.get("/")
def root():
    return {"message": "dsh Medical Agent MVP - ED LOS Monitoring"}
