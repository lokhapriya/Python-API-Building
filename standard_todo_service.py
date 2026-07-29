from base_to_do_service import BaseTodoService
from db_connection import todo_collection
from bson.objectid import ObjectId


class StandardTodoService(BaseTodoService):

    def __init__(self):
        pass


    def create_list(self, data):

        todo = {
            "name": data["name"]
        }

        result = todo_collection.insert_one(todo)

        todo["_id"] = str(result.inserted_id)

        return todo


    def get_lists(self):

        todos = list(todo_collection.find())

        for todo in todos:
            todo["_id"] = str(todo["_id"])

        return todos


    def update_list(self, list_id, name):

        result = todo_collection.update_one(
            {
                "_id": ObjectId(list_id)
            },
            {
                "$set": {
                    "name": name
                }
            }
        )


        if result.modified_count == 1:

            updated_todo = todo_collection.find_one(
                {
                    "_id": ObjectId(list_id)
                }
            )

            updated_todo["_id"] = str(updated_todo["_id"])

            return updated_todo


        return None


    def delete_list(self, list_id):

        result = todo_collection.delete_one(
            {
                "_id": ObjectId(list_id)
            }
        )


        if result.deleted_count == 1:

            return {
                "message": "Todo deleted successfully",
                "id": list_id
            }


        return None