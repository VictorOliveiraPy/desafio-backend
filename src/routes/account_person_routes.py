from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from src.application.use_cases.account_person import AccountPersonUseCase
from src.domain.entities.person import PersonCreate
from src.infrastructure.database.session import get_db

account_person = APIRouter()


@account_person.post("/", status_code=HTTP_201_CREATED)
def create_account(user: PersonCreate, db: Session = Depends(get_db)):
    usecase = AccountPersonUseCase(db)
    created_user = usecase.create_person(user)
    return created_user


@account_person.get("/")
def list_users_by_creator(user_id: int, db: Session = Depends(get_db)):
    user_repository = AccountPersonUseCase(db)
    accounts = user_repository.get_users_by_creator(user_id)

    if not accounts:
        raise HTTPException(status_code=404, detail="Accounts not found")
    return accounts
