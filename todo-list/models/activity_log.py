class ActivityLog:
    def __init__(self, todo_list_id, task_id, activity, created_at, user_id, type):
        self.todo_list_id = todo_list_id
        self.task_id = task_id
        self.activity = activity
        self.created_at = created_at
        self.user_id = user_id
        self.type = type
