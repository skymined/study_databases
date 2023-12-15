# quest
## 문제 풀기를 CRUD 작성
# 변수 리스트 -> DB 저장(문항과 답항 하나 레코드) -> 응답된 해답 저장
# 최소 function 2개 사용. function은 import해서 사용. function 파일을 따로 두라는 소리.
# 어떤 문제를 사용자가 어떤 답을 했는지 알려주기

# def connect(data, colle) :  # mongodb에 있는 특정 collection에 연결하기 위한 함수

from solvingProblem_functions import solvingproblem

set = solvingproblem("solvingproblem") #solvingproblem_function에 있는 클래스 instance

# 각 함수들 사용
set.mongo() # mongo collection 불러오기
set.makeit("question", "choices", "answer", "score", "_id") # parameter 쓰고 싶어서 괜히 넣어보기
set.updateit() # 답을 받아서 mongodb에 update하기
