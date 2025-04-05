from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str
    password: str
    created_at: datetime
    active: bool

    