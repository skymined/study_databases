from pymongo import MongoClient

# mongodb에 접속 -> 자원에 대한 class 를 받아냄. 이때 class는 mongodbclient
mongoclient = MongoClient("mongodb://localhost:27017")  # 변수에 넣어야 함. 이때 이 변수는 클래스 변수임. 

# database 연결
database = mongoclient['local']

# collection에 작업
collection = database['fruits']

# insert 작업 -> NoSQL에서는 리스트를 넣을 수 있음
mixed_fruit = {"과일명": "오렌지", 
               "색상": ["주황색", "갈색", "노란색"] ,
               "원산지": "미국"}
result = collection.insert_one(mixed_fruit)

# 분리 입력(fruits, fruits_colors)
# insert_fruits 작업 진행
dict_fruit = {"과일명": "오렌지", 
               "원산지": "미국"}
result = collection.insert_one(dict_fruit)  # result는 class

# _id: ObjectId("657bf131affad6eaf45ab53e")
print("result.inserted_id : {}".format(result.inserted_id))
inserted_id = result.inserted_id # 클래스에 있는 애랑 파일안에 사용하고 있는 애


# insert fruits_colors 작업 진행
[{"fruits_id" : ObjectId("657bf131affad6eaf45ab53e"),"색상" : "주황색"}
 , {"fruits_id" : ObjectId("657bf131affad6eaf45ab53e"), "색상" : "갈색"}
 , {"fruits_id" : ObjectId("657bf131affad6eaf45ab53e"), "색상" : "노란색"}]


fruits_colors = [{"색상" : "주황색"}
 ,{"색상" : "갈색"}
 ,{"색상" : "노란색"}]

list_fruits_colors = list()
for dict_color in fruits_colors :
    dict_color["fruits_id"] = inserted_id
    list_fruits_colors.append(dict_color)
    pass

# collection fruits_colors
collection_fruits_colors = database["fruits_colors"]

collection_fruits_colors.insert_many(list_fruits_colors)

#find from fruits_colors
collection_fruits_colors.find({"fruits_id" : { "$eq" : inserted_id }})