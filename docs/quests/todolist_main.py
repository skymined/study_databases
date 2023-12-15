
# from todolist_functions import todolistproblem
# set = todolistproblem()

# set.mongo("todos_list")
# set.mongo("participants")
# set.mongo("participants_todos")


from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient["local"]
collection = database[self.collection]
self.todo_list.append(self.collection.find({}, {}))
