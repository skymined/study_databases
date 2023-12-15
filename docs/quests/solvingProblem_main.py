# quest
## 문제 풀기를 CRUD 작성
# 변수 리스트 -> DB 저장(문항과 답항 하나 레코드) -> 응답된 해답 저장
# 최소 function 2개 사용. function은 import해서 사용. function 파일을 따로 두라는 소리.
# 어떤 문제를 사용자가 어떤 답을 했는지 알려주기

# def connect(data, colle) :  # mongodb에 있는 특정 collection에 연결하기 위한 함수
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient["local"]
collection = database["solvingproblem"]

# mongodb에 있는 문제 순차적으로 나오게 하기
result_list = collection.find({}, {"question" : 1,"choices":1, "answer":1, "score":1, "_id" :0})
pass

question_list=[]
choices_list=[]
answer_list=[]
score_list=[]

for i in range(5):
    question_list.append(result_list[i]["question"])
    choices_list.append(result_list[i]["choices"])
    answer_list.append(result_list[i]["answer"])
    score_list.append(result_list[i]["score"])
    pass

# 우선 재조립 성공! 각 리스트에 각각의 내용들이 담겼음.

user_score=[]

for j in range(1,5):
    print("{}번 문제".format(j), question_list[j-1])
    for i in range(1,5) : 
        print("{}.".format(i), *choices_list[j-1][i-1])
    print(score_list[j-1],"점")
    user_answer = input("정답을 입력(번호가 아닌 답을 입력)")
    collection.update_one({"numbering":j}, { "$set":{"user_answer" : user_answer}})
    if user_answer == answer_list[j-1] :
        print("정답입니다!")
        user_score.append(20)
        collection.update_many({"numbering":j}, {"$set":{"score":20}})
    else : 
        print("오답입니다.")
        collection.update_many({"numbering":j}, {"$set":{"score" :0}})

print("당신의 점수는",sum(user_score), "점입니다.")
    
