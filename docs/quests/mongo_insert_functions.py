# fruit_info 리스트를 mongo 저장
# 최소 2개의 function :connect, insert

def connect() :
    from pymongo import MongoClient
    mongoclient = MongoClient("mongodb://localhost:27017")
    database = mongoclient['local']
    collection = database['fruits']
    return collection

def put_fruits(collection, fruits) :
    collection.insert_many(fruits)


fruits = ({"과일명": "사과", "색상": "빨강", "원산지": "한국"},
        {"과일명": "바나나", "색상": "노랑", "원산지": "필리핀"},
        {"과일명": "오렌지", "색상": "주황", "원산지": "미국"},
        {"과일명": "수박", "색상": "초록", "원산지": "한국"})

collection = connect()
put_fruits(collection, fruits)
