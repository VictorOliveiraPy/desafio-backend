from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.config import settings
from src.domain.models.base import Base
from src.routes import account_card_routes, account_person_routes

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(account_person_routes.account_person, prefix="/account/person", tags=["account"])
app.include_router(account_card_routes.card_router, prefix="/account/card", tags=["accounts"])
