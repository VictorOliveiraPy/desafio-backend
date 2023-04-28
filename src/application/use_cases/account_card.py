from sqlalchemy.orm import Session

from src.domain.entities.account import CardCreate
from src.domain.models.credit_card import CreditCard
from src.repositories.person_repository import PersonRepository


class AccountCardUseCase:
    def __init__(self, db: Session):
        self.repository = PersonRepository(db)

    def create_card(self, user: CardCreate) -> CardCreate:
        created_card = CreditCard(**user.dict())
        created_card_model = self.repository.create(created_card)
        return created_card_model

    def get_cards_by_creator(self, creator_id: int):
        get_card_model = self.repository.get_by_id(creator_id)
        return get_card_model

