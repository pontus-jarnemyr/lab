from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL)
Base: DeclarativeBase = declarative_base()
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
