from sqlalchemy.orm import Session, sessionmaker

from .orm import Base, engine


def get_db() -> Session:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
