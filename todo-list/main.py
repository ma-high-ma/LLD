from datetime import datetime

from constants import TaskStatus, ActivityType
from services.task import TaskService
from services.todo_list_manager import TodoListManager
from services.user import UserService

if __name__ == '__main__':

    u = UserService()
    ts = TaskService()

    u0 = u.create(id="u0", name="User0")

    todo_manager = TodoListManager(user_id=u0.id)

    td1 = todo_manager.create_todo_list(id="td1", user_id=u0.id, name="TodoList1")
    task1 = todo_manager.create_task(task_id="t1", todo_list_id=td1.id, title="Task1", tags=["red"])
    task2 = todo_manager.create_task(task_id="t2", todo_list_id=td1.id, title="Task1", tags=["green"])

    print()
    todo_manager.show_tasks(todo_list_id=td1.id)

    print()
    todo_manager.update_task(task_id=task1.id, key="title", value="Updated task 1")
    todo_manager.update_task_status(task_id=task1.id, status=TaskStatus.COMPLETED)

    print()

    todo_manager.show_tasks(todo_list_id=td1.id)
    print()

    todo_manager.show_analytics(start_date=datetime.today().date(), end_date=datetime.today().date(), type=ActivityType.UPDATED)

    todo_manager.show_analytics(start_date=datetime.today().date(), end_date=datetime.today().date(),
                                type=ActivityType.CREATED)
