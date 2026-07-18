from base_to_do_service import BaseTodoService
from standard_todo_service import StandardTodoService
from soft_todo_delete import SoftDeleteTodoService


class TodoServiceFactory:

    @staticmethod
    def get_service(strategy: str) -> BaseTodoService:

        if strategy.upper() == "SOFT":
            return SoftDeleteTodoService()

        return StandardTodoService()