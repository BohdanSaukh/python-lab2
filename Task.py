class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline

    def show_info(self):
        print(f"Task: {self.title}, Deadline: {self.deadline}")