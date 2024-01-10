from models.todo_list import TodoList
from services.task import TaskService


class TodoListService:
    UserTodoListMap = {}
    TodoListMap = {}

    def create(self, id, user_id, name):
        todo_list = TodoList(id=id, name=name)
        self.TodoListMap[todo_list.id] = todo_list
        self.UserTodoListMap[user_id] = todo_list
        return todo_list

    def add_task(self, todo_list_id, task_obj):
        todo_list = self.TodoListMap[todo_list_id]
        todo_list.tasks.append(task_obj)

    def show(self, todo_list_id, status=None):
        todo_list = self.TodoListMap[todo_list_id]
        tasks = todo_list.tasks

        print("Tasks under Todo List ", todo_list_id ," : ")

        for task in tasks:
            if not status or task.status == status:
                self.print_task(task_obj=task)
        return

    def print_task(self, task_obj):
        print("ID: ", task_obj.id, " Title: ", task_obj.title, " tags: ", task_obj.tags, " due_date: ",
              task_obj.due_date, " status: ", task_obj.status, " created_at: ", task_obj.created_at, " modified_at: ", task_obj.modified_at, "completed_on: ", task_obj.completed_on)

# User -> Todo List -> Tasks

# Manager -> TodoList Service -> Task :check
# Manager -> Task Service, TodoList Service
