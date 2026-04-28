from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from contextlib import contextmanager
from config import DB_URL

engine = create_engine(DB_URL, echo=False)  # echo=True pokazuje generowane SQL-e (przydatne przy debugowaniu)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    """Tworzy wszystkie tabele na podstawie modeli (zastępuje schema.sql)."""
    from app.models import models  # import konieczny żeby Base "wiedziała" o modelach
    Base.metadata.create_all(engine)