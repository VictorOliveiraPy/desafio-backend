from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseSchema(BaseModel):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class CardCreate(BaseSchema):
    id: str
    title: str
    pan: str
    expiry_mm: str
    expiry_yyyy: str
    security_code: str
    date: str


class TransferBase(BaseModel):
    user_id: int
    friend_id: int
    value: int
    date: str
    from_card_id: Optional[int] = None


class Transfer(TransferBase):
    id: int
    from_card: Optional[CardCreate] = None
