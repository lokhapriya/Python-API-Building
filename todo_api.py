from fastapi import FastAPI
from fastapi import HTTPException

from models import TodoList
from models import TodoListUpdate

from standard_todo_service import StandardTodoService
from soft_todo_delete import SoftDeleteTodoService

app = FastAPI()

# Used for Create, Read and Update
standard_service = StandardTodoService()


@app.post("/lists")
def create_list(todo: TodoList):

    return standard_service.create_list(todo.model_dump())


@app.get("/lists")
def get_lists():

    return standard_service.get_lists()


@app.put("/lists/{list_id}")
def update_list(
    list_id: int,
    todo: TodoListUpdate
):

    updated = standard_service.update_list(
        list_id,
        todo.name
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return updated


@app.delete("/lists/{list_id}")
def delete_list(
    list_id: int,
    strategy: str = "STANDARD"
):

    if strategy.upper() == "SOFT":
        service = SoftDeleteTodoService()
    else:
        service = StandardTodoService()

    deleted = service.delete_list(list_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return deleted