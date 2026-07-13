from base_to_do_service import BaseTodoService
from standard_todo_service import StandardTodoService
# from services.soft_delete_todo_service import SoftDeleteTodoService


def get_todo_service() -> BaseTodoService:
    return StandardTodoService()

    # For another client simply change to:
    # return SoftDeleteTodoService()