from Person import Person

class Employee(Person):
    def __init__(self, id, name, position, salary):
        super().__init__(id, name)
        self.position = position
        self.__salary = salary
        self.tasks = []

    def get_salary(self):
        return self.__salary

    def show_info(self):
        super().show_info()
        print(f"Position: {self.position}, Salary: {self.__salary}")
        if self.tasks:
            print("Tasks:")
            for t in self.tasks:
                t.show_info()
        else:
            print("No tasks yet.")