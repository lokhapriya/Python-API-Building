from datetime import datetime, timedelta

from .standard_todo_service import StandardTodoService


class SoftDeleteTodoService(StandardTodoService):

    def delete_list(self, list_id):

        for todo in self.todo_lists:

            if todo["id"] == list_id:

                todo["is_deleted"] = True
                todo["deleted_at"] = datetime.now()

                return todo

        return None

    def get_lists(self):

        return [
            todo
            for todo in self.todo_lists
            if not todo.get("is_deleted", False)
        ]

    def purge_deleted_lists(self):

        current_time = datetime.now()

        self.todo_lists = [
            todo
            for todo in self.todo_lists
            if not (
                todo.get("is_deleted")
                and current_time - todo["deleted_at"] >= timedelta(hours=4)
            )
        ]