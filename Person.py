class Person:
    object_count = 0

    def __init__(self, id, name):
        self.__id = id
        self.name = name
        Person.object_count += 1

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def show_info(self):
        print(f"ID: {self.__id}, Name: {self.name}")

    @staticmethod
    def show_count():
        print(f"Total created persons: {Person.object_count}")