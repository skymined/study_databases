
from todolist_functions import todolistproblem
set = todolistproblem()

# collection 불러오기
set.mongo("todos_list", "participants", "participants_todos")

#todolist 실행
set.doit()