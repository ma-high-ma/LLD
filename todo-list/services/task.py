from datetime import datetime

from constants import TaskStatus
from models.task import Task
from services.activity_log import ActivityLogService


class TaskService:
    TaskMap = {}

    def create(self, id, title, tags, status=TaskStatus.ACTIVE, due_date=None, completed_on=None):
        created_at = datetime.now()
        task = Task(id, title, status, due_date, completed_on, tags, created_at)
        self.TaskMap[task.id] = task
        self.post_process_task_create_or_update(task_obj=task)
        return task

    def update(self, task_id, key, value):
        task_obj = self.TaskMap[task_id]
        setattr(task_obj, key, value)
        self.post_process_task_create_or_update(task_obj=task_obj)
        return task_obj

    def update_status(self, task_id, status):
        task_obj = self.TaskMap[task_id]
        task_obj.status = status
        if status == TaskStatus.COMPLETED:
            task_obj.completed_on = datetime.now()
        self.post_process_task_create_or_update(task_obj=task_obj)
        return task_obj

    def post_process_task_create_or_update(self, task_obj):
        task_obj.modified_at = datetime.now()



