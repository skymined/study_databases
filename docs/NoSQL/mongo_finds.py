from pymongo import MongoClient

# mongodb에 접속 -> 자원에 대한 class 를 받아냄. 이때 class는 mongodbclient
mongoclient = MongoClient("mongodb://localhost:27017")  # 변수에 넣어야 함. 이때 이 변수는 클래스 변수임. 

# database 연결
database = mongoclient['local']

# collection에 작업
collection = database['posts']

# insert 작업
documents = collection.find({}, {"_id":1, "title":1, "likes":1})

#cast cursor to list
list_documents = list(documents)
print("list_documents length : {}".format(len(list_documents)))
for document in documents :
    print("document : {}".format(document))
    pass
pass