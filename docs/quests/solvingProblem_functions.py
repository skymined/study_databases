
# list 불러오기

class solvingproblem() :  # solvingproblem class 
    def __init__(self,collection) -> None:
        self.question_list=[]
        self.choices_list=[]
        self.answer_list=[]
        self.score_list=[]
        self.user_score=[]
        self.id_list=[]
        self.collection=collection
        pass

    def mongo (self): #mongodb 불러오기. collection은 변수로 설정
        from pymongo import MongoClient
        mongoclient = MongoClient("mongodb://localhost:27017")
        database = mongoclient["local"]
        self.collection = database[self.collection]

    def makeit(self,quest, choice, answer, score, id): #불러온 값들 재조립하는 과정 function
        result_list = self.collection.find({}, {quest : 1, choice:1, answer:1, score:1, id:1})
        for i in range(5):
            self.question_list.append(result_list[i][quest])
            self.choices_list.append(result_list[i][choice])
            self.answer_list.append(result_list[i][answer])
            self.score_list.append(result_list[i][score])
            self.id_list.append(result_list[i][id])
            pass
    
    def updateit(self): # 문제와 답을 보여주고 사용자의 답을 update하는 함수 제작
        for j in range(1,6):
            print("{}번 문제".format(j), self.question_list[j-1])
            for i in range(1,5) : 
                print("{}.".format(i), *self.choices_list[j-1][i-1])
            print(self.score_list[j-1],"점")
            user_answer = input("정답을 입력(번호가 아닌 답을 입력) : ")
            self.collection.update_one({"_id": self.id_list[j-1]}, { "$set":{"user_answer" : user_answer}})
            if user_answer == self.answer_list[j-1] :
                print("정답입니다!")
                self.user_score.append(20)
                self.collection.update_one({"_id":self.id_list[j-1]}, {"$set":{"score":20}})
            else : 
                print("오답입니다.")
                self.collection.update_one({"_id":self.id_list[j-1]}, {"$set":{"score" :0}})
            print("당신의 점수는",sum(self.user_score), "점입니다.")

