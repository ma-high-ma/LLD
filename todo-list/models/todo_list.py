class TodoList:
    def __init__(self, id, name, tasks=None):
        self.id = id
        self.name = name
        self.tasks = tasks if tasks else []
