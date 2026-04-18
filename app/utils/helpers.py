def clear_screen():
    print("\n" * 10)


def get_next_id(prefix: str, table: list):
    from app.core.database import execute
    row = execute(f"SELECT id FROM {table} ORDER BY id DESC LIMIT 1", fetch="one")
    # Wynikiem tego zapytania będzie słownik np: {"id": U003}

    if not row:
        return f"{prefix}001"

    number = int(row["id"][len(prefix):]) # row["id"] wywołuje wartośc przypisaną do tego klucza -> U003
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