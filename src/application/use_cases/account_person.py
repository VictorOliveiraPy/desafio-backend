from sqlalchemy.orm import Session

from src.domain.entities.person import PersonCreate
from src.domain.models.person import Person
from src.repositories.person_repository import PersonRepository


class AccountPersonUseCase:
    def __init__(self, db: Session):
        self.repository = PersonRepository(db)

    def create_person(self, user: PersonCreate) -> PersonCreate:
        created_user = Person(**user.dict())
        created_user_model = self.repository.create(created_user)
        return created_user_model

    def get_users_by_creator(self, creator_id: int):
        created_user_model = self.repository.get_by_id(creator_id)
        return created_user_model
