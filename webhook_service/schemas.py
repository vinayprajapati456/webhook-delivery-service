from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class SubscriptionCreate(BaseModel):
    target_url: HttpUrl
    secret: Optional[str] = None
    event_types: Optional[List[str]] = None

class SubscriptionOut(BaseModel):
    id: UUID
    target_url: HttpUrl
    secret: Optional[str]
    event_types: Optional[List[str]]
    created_at: datetime

    class Config:
        orm_mode = True