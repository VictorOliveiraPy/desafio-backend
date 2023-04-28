from typing import Optional

from pydantic import BaseModel


class CreditCard(BaseModel):
    id: Optional[int]
    card_id: str
