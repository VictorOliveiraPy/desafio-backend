from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config.config import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL)
