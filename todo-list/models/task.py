class Task:
    def __init__(self, id, title, status, due_date, completed_on, tags, created_at, modified_at=None):
        self.id = id
        self.title = title
        self.status = status
        self.due_date = due_date
        self.completed_on = completed_on
        self.tags = tags if tags else []
        self.created_at = created_at
        self.modified_at = modified_at
