from typing import Optional

from pydantic import Field

from src.domain.entities.account import BaseSchema


class PersonCreate(BaseSchema):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birthday: str
    password: str = Field(..., min_length=3, max_length=50)
    username: str = Field(..., min_length=3, max_length=50)
    user_id: str
