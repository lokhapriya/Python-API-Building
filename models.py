from typing import Optional

from pydantic import BaseModel


class TodoList(BaseModel):
    name: str


class TodoListUpdate(BaseModel):
    name: Optional[str] = None