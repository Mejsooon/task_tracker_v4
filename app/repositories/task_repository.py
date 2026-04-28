from app.models.models import Task
from app.core.database import get_session


def save(task: Task) -> None:
    with get_session() as session:
        session.add(task)
        session.commit()


def find_by_id_and_status(user_id: str, status: str) -> list[Task] | None:
    with get_session() as session:
        results = (
            session.query(Task)
            .filter_by(user_id=user_id, status=status)
            .all()
        )
        return results if results else None


def make_task_complete(task: Task) -> None:
    with get_session() as session:
        db_task = session.get(Task, task.id)
        if db_task:
            db_task.status = "completed"
            session.commit()