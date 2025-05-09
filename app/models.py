from datetime import datetime
from typing import Optional

class JobApplication:
    def __init__(self, id: int, company: str, position: str, status: str, date_applied: Optional[datetime] = None):
        self.id = id
        self.company = company
        self.position = position
        self.status = status
        self.date_applied = date_applied or datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "status": self.status,
            "date_applied": self.date_applied.isoformat()
        }
