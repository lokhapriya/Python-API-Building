from fastapi import FastAPI, HTTPException

from models_new import (
    TodoList,
    TodoListUpdate,
    TodoService,
)

app = FastAPI()

service = TodoService()


# ---------------- GET ALL ---------------- #

@app.get("/lists")
def get_lists():
    return service.get_lists()


# ---------------- CREATE ---------------- #

@app.post("/lists")
def create_list(todo: TodoList):
    return service.create_list(todo.model_dump())


# ---------------- UPDATE ---------------- #

@app.put("/lists/{list_id}")
def update_list(list_id: int, data: TodoListUpdate):

    result = service.update_list(list_id, data.name)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return result


# ---------------- DELETE ---------------- #

@app.delete("/lists/{list_id}")
def delete_list(list_id: int):

    result = service.delete_list(list_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="List not found"
        )

    return result


# ---------------- SEARCH (Open/Closed Principle) ---------------- #

@app.get("/lists/search/{keyword}")
def search_list(keyword: str):
    return service.search_list(keyword)