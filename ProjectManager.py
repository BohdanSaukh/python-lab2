from Manager import Manager
from Project import Project

class ProjectManager(Manager, Project):
    def __init__(self, id, name, position, salary, department,
                 project_id, project_name, start_date, end_date, status):
        Manager.__init__(self, id, name, position, salary, department)
        Project.__init__(self, project_id, project_name, start_date, end_date, status)

    def show_info(self):
        print(f"\n--- Project Manager Info ---")
        Manager.show_info(self)
        print(f"Managing project '{self.name}' (status: {self.status})")