from base_to_do_service import BaseTodoService
from standard_todo_service import StandardTodoService
from soft_todo_delete import SoftDeleteTodoService


# --------------------------------------------------
# Toggle the implementation here
# --------------------------------------------------

service: BaseTodoService = StandardTodoService()

# service: BaseTodoService = SoftDeleteTodoService()


def get_todo_service() -> BaseTodoService:
    return service