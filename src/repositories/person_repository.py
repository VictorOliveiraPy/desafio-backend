from typing import Type

from sqlalchemy.orm import Session

from src.domain.models.person import Person


class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: Person) -> Person:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all(self) -> list[Type[Person]]:
        return self.db.query(Person).all()

    def get_by_id(self, user_id: int) -> Type[Person] | None:
        return self.db.query(Person).filter(Person.id == user_id).first()

    def find_user_and_friend(self, card_id, friend_id):
        user = self.db.query(Person).filter_by(user_id=card_id).first()

        # Encontrando a pessoa que receberá a transferência pelo id
        friend = self.db.query(Person).filter_by(id=friend_id).first()

        # Verificando se as duas pessoas existem
        if not user or not friend:
            return None

        return user, friend
