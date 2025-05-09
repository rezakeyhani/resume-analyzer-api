from fastapi import APIRouter, HTTPException
from app.models import JobApplication
from app.schemas import JobApplicationCreate, JobApplicationResponse
import json
from typing import List
from pathlib import Path

router = APIRouter()
DATA_FILE = Path("app/storage.json")

def load_data() -> List[JobApplication]:
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            raw = json.load(f)
            return [JobApplication(**item) for item in raw]
    return []

def save_data(data: List[JobApplication]):
    with open(DATA_FILE, "w") as f:
        json.dump([item.to_dict() for item in data], f, indent=4)

@router.post("/applications/", response_model=JobApplicationResponse)
def create_application(app_data: JobApplicationCreate):
    data = load_data()
    new_id = max([item.id for item in data], default=0) + 1
    app = JobApplication(id=new_id, **app_data.dict())
    data.append(app)
    save_data(data)
    return app.to_dict()

@router.get("/applications/", response_model=List[JobApplicationResponse])
def get_applications():
    data = load_data()
    return [item.to_dict() for item in data]

@router.get("/applications/{app_id}", response_model=JobApplicationResponse)
def get_application(app_id: int):
    data = load_data()
    for item in data:
        if item.id == app_id:
            return item.to_dict()
    raise HTTPException(status_code=404, detail="Application not found")