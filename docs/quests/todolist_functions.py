
# 클래스 만들기

class todolistproblem() : #todolistproblem class
    def __init__(self, collection):
        self.collection = collection
        self.
        self.todo_list=[]

    def mongo (self): #값들 불러오기
        from pymongo import MongoClient
        mongoclient = MongoClient("mongodb://localhost:27017")
        database = mongoclient["local"]
        self.collection = database[self.collection]
        self.todo_list.append(self.collection.find({}, {}))

    # 참여자 이름 입력하고 print하기
    def doit (self) :
        while True :
            parti = input("Input Your Name: ")

            
            print("ToDo List 중 하나 선택 하세요!")
            for i in range(self.todo_list) :
                print("{}.{}".format(i,self.todo_list[i]["title"]))
            
                

    #_id #title #description