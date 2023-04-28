from typing import Type

from sqlalchemy.orm import Session

from src.domain.models.credit_card import CreditCard


class CreditCardRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, card: CreditCard) -> CreditCard:
        self.db.add(card)
        self.db.commit()
        self.db.refresh(card)
        return card

    def get_all(self) -> list[Type[CreditCard]]:
        return self.db.query(CreditCard).all()

    def get_by_id(self, card_id: int) -> Type[CreditCard] | None:
        return self.db.query(CreditCard).filter(CreditCard.id == card_id).first()
