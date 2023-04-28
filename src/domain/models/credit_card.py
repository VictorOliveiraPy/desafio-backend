from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.domain.models.base import BaseModel


class CreditCard(BaseModel):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    pan = Column(String)
    expiry_mm = Column(String)
    expiry_yyyy = Column(String)
    security_code = Column(String)
    date = Column(String)
    user_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person', backref='credit_cards')
