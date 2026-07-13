from abc import ABC, abstractmethod


class BaseTodoService(ABC):

    def __init__(self):
        self.todo_lists = []
        self.next_id = 1

    @abstractmethod
    def create_list(self, data):
        """
        Create a new todo list.
        """
        pass

    @abstractmethod
    def get_lists(self):
        """
        Return all todo lists.
        """
        pass

    @abstractmethod
    def update_list(self, list_id, name):
        """
        Update an existing todo list.
        """
        pass

    @abstractmethod
    def delete_list(self, list_id):
        """
        Delete a todo list.
        """
        pass