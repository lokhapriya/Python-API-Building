from datetime import datetime, timedelta

from standard_todo_service import StandardTodoService
from db_connection import todo_collection
from bson.objectid import ObjectId


class SoftDeleteTodoService(StandardTodoService):

    def __init__(self):
        pass


    def delete_list(self, list_id):

        result = todo_collection.update_one(
            {
                "_id": ObjectId(list_id)
            },
            {
                "$set": {
                    "is_deleted": True,
                    "deleted_at": datetime.now()
                }
            }
        )


        if result.modified_count == 1:

            deleted_todo = todo_collection.find_one(
                {
                    "_id": ObjectId(list_id)
                }
            )

            deleted_todo["_id"] = str(deleted_todo["_id"])

            return deleted_todo


        return None



    def get_lists(self):

        todos = list(
            todo_collection.find(
                {
                    "is_deleted": {
                        "$ne": True
                    }
                }
            )
        )


        for todo in todos:
            todo["_id"] = str(todo["_id"])


        return todos



    def purge_deleted_lists(self):

        cutoff_time = datetime.now() - timedelta(hours=4)


        result = todo_collection.delete_many(
            {
                "is_deleted": True,
                "deleted_at": {
                    "$lte": cutoff_time
                }
            }
        )


        return {
            "deleted_count": result.deleted_count
        }