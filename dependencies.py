from standard_todo_service import StandardTodoService
from soft_todo_delete import SoftDeleteTodoService
from base_to_do_service import BaseTodoService


def get_standard_todo_service() -> BaseTodoService:
    return StandardTodoService()


def get_soft_delete_todo_service() -> BaseTodoService:
    return SoftDeleteTodoService()