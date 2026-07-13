from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from dependencies import get_todo_service
from models import TodoList
from models import TodoListUpdate

from base_to_do_service import BaseTodoService

app = FastAPI()


@app.post("/lists")
def create_list(
    todo: TodoList,
    service: BaseTodoService = Depends(get_todo_service)
):

    return service.create_list(todo.model_dump())


@app.get("/lists")
def get_lists(
    service: BaseTodoService = Depends(get_todo_service)
):

    return service.get_lists()


@app.put("/lists/{list_id}")
def update_list(
    list_id: int,
    todo: TodoListUpdate,
    service: BaseTodoService = Depends(get_todo_service)
):

    updated = service.update_list(
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
    service: BaseTodoService = Depends(get_todo_service)
):

    deleted = service.delete_list(list_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return deleted