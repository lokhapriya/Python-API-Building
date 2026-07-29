from standard_todo_service import StandardTodoService
from soft_todo_delete import SoftDeleteTodoService


class DeleteServiceFactory:

    def __init__(self, shared_todo_lists):

        self.standard_service = StandardTodoService(shared_todo_lists)
        self.soft_delete_service = SoftDeleteTodoService(shared_todo_lists)

    def get_service(self, strategy: str):

        if strategy.upper() == "SOFT":
            return self.soft_delete_service

        return self.standard_service