
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


## 먼저 3개의 collection을 name 한 후에 그 name한 것을 이용해서 진행
## 참여자 이름 입력할 경우 collection에 해당되는 것이 업로드 되고 id가 생성됨
## 생성된 id를 find 해서 리스트에 저장