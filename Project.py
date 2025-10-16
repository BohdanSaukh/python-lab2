class Project:
    def __init__(self, id, name, start_date, end_date, status):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.tasks = []

    def show_info(self):
        print(f"Project: {self.name}, Status: {self.status}")
        for t in self.tasks:
            t.show_info()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task '{task.title}' to project '{self.name}'")