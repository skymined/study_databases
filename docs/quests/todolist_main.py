
from todolist_functions import todolistproblem
set = todolistproblem()

set.mongo("todos_list", "participants", "participants_todos")
set.doit()