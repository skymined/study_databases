# fruit_info 리스트를 mongo 저장
# 최소 2개의 function :connect, insert

def connect(address, data, colle) :  # mongodb에 있는 특정 collection에 연결하기 위한 함수
    from pymongo import MongoClient
    mongoclient = MongoClient(address)
    database = mongoclient[data]
    collection = database[colle]
    return collection

def put_fruits(collection, fruits) : #  collection에 내용 집어넣기 위한 함수
    collection.insert_many(fruits)

# 삽입 리스트
fruits = [{"과일명": "사과", "색상": "빨강", "원산지": "한국"},
        {"과일명": "바나나", "색상": "노랑", "원산지": "필리핀"},
        {"과일명": "오렌지", "색상": "주황", "원산지": "미국"},
        {"과일명": "수박", "색상": "초록", "원산지": "한국"}]

collection = connect("mongodb://localhost:27017", "local", "fruits")
put_fruits(collection, fruits)
