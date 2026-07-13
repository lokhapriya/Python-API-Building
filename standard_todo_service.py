from .base_to_do_service import BaseTodoService


class StandardTodoService(BaseTodoService):

    def create_list(self, data):

        todo = {
            "id": self.next_id,
            "name": data["name"]
        }

        self.todo_lists.append(todo)
        self.next_id += 1

        return todo

    def get_lists(self):
        return self.todo_lists

    def update_list(self, list_id, name):

        for todo in self.todo_lists:

            if todo["id"] == list_id:

                if name is not None:
                    todo["name"] = name

                return todo

        return None

    def delete_list(self, list_id):

        for index, todo in enumerate(self.todo_lists):

            if todo["id"] == list_id:
                return self.todo_lists.pop(index)

        return None