from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: str # U001, maksymalnie 1000 użytkowników
    name: str
    username: str
    password: str


@dataclass
class Task:
    id: str
    user_id: str # Do kogo przypisany jest ten task
    task_difficulty: str
    task_description: str
    additional_notes: Optional[str] = ""
    status: str = "active"