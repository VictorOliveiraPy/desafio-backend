
from sqlalchemy import Column, Integer, String

from src.domain.models.base import BaseModel


class Person(BaseModel):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)
    password = Column(String)
    username = Column(String)
    user_id = Column(String)
