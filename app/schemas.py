from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobApplicationCreate(BaseModel):
    company: str
    position: str
    status: str

class JobApplicationResponse(JobApplicationCreate):
    id: int
    date_applied: datetime