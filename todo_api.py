from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from dependencies import (
    get_standard_todo_service,
    get_soft_delete_todo_service
)

from models import TodoList
from models import TodoListUpdate

from base_to_do_service import BaseTodoService
from soft_todo_delete import SoftDeleteTodoService

app = FastAPI()


# ---------------- STANDARD CRUD ---------------- #

@app.post("/lists")
def create_list(
    todo: TodoList,
    service: BaseTodoService = Depends(get_standard_todo_service)
):

    return service.create_list(todo.model_dump())


@app.get("/lists")
def get_lists(
    service: BaseTodoService = Depends(get_standard_todo_service)
):

    return service.get_lists()


@app.put("/lists/{list_id}")
def update_list(
    list_id: int,
    todo: TodoListUpdate,
    service: BaseTodoService = Depends(get_standard_todo_service)
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
    service: BaseTodoService = Depends(get_standard_todo_service)
):

    deleted = service.delete_list(list_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return deleted


# ---------------- SOFT DELETE ---------------- #

@app.delete("/soft-delete/lists/{list_id}")
def soft_delete_list(
    list_id: int,
    service: BaseTodoService = Depends(get_soft_delete_todo_service)
):

    deleted = service.delete_list(list_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return deleted


@app.get("/soft-delete/lists")
def get_soft_delete_lists(
    service: BaseTodoService = Depends(get_soft_delete_todo_service)
):

    return service.get_lists()


@app.delete("/soft-delete/purge")
def purge_deleted_lists(
    service: SoftDeleteTodoService = Depends(get_soft_delete_todo_service)
):

    service.purge_deleted_lists()

    return {
        "message": "Deleted lists older than 4 hours have been permanently removed."
    }