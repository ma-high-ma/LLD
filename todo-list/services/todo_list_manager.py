from constants import ActivityType
from models.activity_log import ActivityLog
from services.activity_log import ActivityLogService
from services.task import TaskService
from services.todo_list import TodoListService


class TodoListManager:
    def __init__(self, user_id):
        self.user_id = user_id

    def create_todo_list(self, id, user_id, name):
        return TodoListService().create(id, user_id, name)

    def create_task(self, task_id, todo_list_id, title, tags, due_date=None, completed_on=None):
        task = TaskService().create(id=task_id, tags=tags, due_date=due_date, completed_on=completed_on, title=title)
        TodoListService().add_task(todo_list_id=todo_list_id, task_obj=task)

        activity_message = f"{ActivityType.CREATED} Task"
        self.perform_post_create_or_update(message=activity_message, task_id=task_id, type=ActivityType.CREATED)

        return task

    def update_task(self, task_id, key, value):
        task = TaskService().update(task_id, key, value)

        activity_message = f"{ActivityType.UPDATED} {key} to {value}"

        self.perform_post_create_or_update(message=activity_message, task_id=task_id, type=ActivityType.UPDATED)

        return task

    def update_task_status(self, task_id, status):
        task = TaskService().update_status(task_id=task_id, status=status)
        activity_message = f"{ActivityType.UPDATED} status to {status}"

        self.perform_post_create_or_update(message=activity_message, task_id=task_id, type=ActivityType.UPDATED)

        return task

    def show_tasks(self, todo_list_id, status=None):
        return TodoListService().show(todo_list_id=todo_list_id, status=status)

    def perform_post_create_or_update(self, message, task_id, type):
        todo_list_id = TodoListService.UserTodoListMap[self.user_id]
        ActivityLogService().create(todo_list_id=todo_list_id, task_id=task_id, activity=message,
                                    user_id=self.user_id, type=type)

    def show_analytics(self, start_date, end_date, type):
        todo_list_id = TodoListService.UserTodoListMap[self.user_id]
        ActivityLogService().aggregate_by_type(todo_list_id=todo_list_id, type=type, start_date=start_date, end_date=end_date)


