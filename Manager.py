from Employee import Employee

class Manager(Employee):
    def __init__(self, id, name, position, salary, department):
        super().__init__(id, name, position, salary)
        self.department = department
        self.projects = []

    def assign_task(self, employee, task):
        employee.tasks.append(task)
        print(f"{self.position} {self.name} assigned '{task.title}' to {employee.name}")

    def generate_report(self, project):
        print(f"{self.name} created a report for project '{project.name}'")

    def show_info(self):
        super().show_info()
        print(f"Department: {self.department}, Projects: {len(self.projects)}")