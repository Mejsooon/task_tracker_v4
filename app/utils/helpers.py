from app.core.database import get_session
from sqlalchemy import text


def clear_screen():
    print("\n" * 10)


def get_next_id(prefix: str, table: str) -> str:
    with get_session() as session:
        row = session.execute(
            text(f"SELECT id FROM {table} ORDER BY id DESC LIMIT 1")
        ).fetchone()

    if not row:
        return f"{prefix}001"

    number = int(row[0][len(prefix):])
    return f"{prefix}{number + 1:03d}"


def read_multiline(prompt: str):
    if prompt:
        print(prompt)
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return "\n".join(lines)