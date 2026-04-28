from app.models.models import User
from app.core.database import get_session


def find_by_username(username: str) -> User | None:
    with get_session() as session:
        return session.query(User).filter_by(username=username).first()


def save(user: User) -> None:
    with get_session() as session:
        session.add(user)
        session.commit()