from pymongo import MongoClient

# mongodb에 접속 -> 자원에 대한 class 를 받아냄. 이때 class는 mongodbclient
mongoclient = MongoClient("mongodb://localhost:27017")  # 변수에 넣어야 함. 이때 이 변수는 클래스 변수임. 

# database 연결
database = mongoclient['local']

# collection에 작업
collection = database['fruits']

# insert 작업 -> NoSQL에서는 리스트를 넣을 수 있음
mixed_fruit = {"과일명": "오렌지", "색상": ["주황색", "갈색", "노란색"] , "원산지": "미국"}
collection.insert_one(mixed_fruit)


pass