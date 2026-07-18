from fastapi import FastAPI
from fastapi import HTTPException

from models import TodoList
from models import TodoListUpdate

from dependencies import get_todo_service
from todo_service_factory import TodoServiceFactory

app = FastAPI()

# Used for Create, Read and Update
service = get_todo_service()


@app.post("/lists")
def create_list(todo: TodoList):

    return service.create_list(todo.model_dump())


@app.get("/lists")
def get_lists():

    return service.get_lists()


@app.put("/lists/{list_id}")
def update_list(
    list_id: int,
    todo: TodoListUpdate
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
    strategy: str = "SOFT"
):

    delete_service = TodoServiceFactory.get_service(strategy)

    deleted = delete_service.delete_list(list_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return deleted