from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from src.application.use_cases.account_card import AccountCardUseCase
from src.domain.entities.account import CardCreate
from src.infrastructure.database.session import get_db

card_router = APIRouter()


@card_router.post("/", status_code=HTTP_201_CREATED)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    usecase = AccountCardUseCase(db)
    created_user = usecase.create_card(card)
    return created_user


@card_router.get("/")
def list_users_by_creator(card_id: int, db: Session = Depends(get_db)):
    user_repository = AccountCardUseCase(db)
    accounts = user_repository.get_cards_by_creator(card_id)

    if not accounts:
        raise HTTPException(status_code=404, detail="Accounts not found")
    return accounts
