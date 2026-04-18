def clear_screen():
    print("\n" * 10)


def get_next_id(prefix: str, items: list):
    pass


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