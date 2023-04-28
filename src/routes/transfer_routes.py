from fastapi import Depends

from src.domain.entities.account import Transfer
from src.infrastructure.database.session import get_db
from src.main import Session


def transfer_money(transfer: Transfer, db: Session = Depends(get_db)):
    ...
