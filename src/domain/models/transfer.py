from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from src.domain.models.base import BaseModel


class Transfer(BaseModel):
    __tablename__ = 'transfer'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))
    friend_id = Column(Integer, ForeignKey('person.id'))
    value = Column(Integer)
    date = Column(DateTime, default=datetime.utcnow)
    from_card_id = Column(Integer, ForeignKey('credit_card.id'))
    from_card = relationship('CreditCard', foreign_keys=[from_card_id])

    def __repr__(self):
        return f'<Transfer(user_id={self.user_id}, friend_id={self.friend_id}, value={self.value}, date={self.date}, from_card_id={self.from_card_id})>'
