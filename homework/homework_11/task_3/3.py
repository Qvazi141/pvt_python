# Реализовать программу с базой учащихся группы (данные хранятся в файле).
# Записи по учащемуся должны быть представлены отдельным классом с полями: имя, фамилия, пол, возраст.
# Программа должна предусматривать поиск по одному или нескольким полям базы.
# Результат выводить в удобочитаемом виде с порядковым номером записи.
# Скрипт программы должен принимать параметр,
# который определяет формат хранения и реализации БД: в текстовом файле с определенной структурой; в файле json.
import json, uuid


class BD:
    bd_structure = ['Name', 'Family', 'Sex', 'Age']

    def __init__(self):
        self.bd_id = uuid.uuid4()
        self.bd_type = "txt"
        self.bd_name = "bd"
        self.bd_in_dict = {}
        self.obj_list = []

    # выбор режима bd
    def inp_type(self):
        try:
            user_type = input("Input bd type txt/json: ")
            if user_type != "txt":
                if user_type != "json":
                    raise TypeError
            return user_type
        except TypeError:
            print("BD type error, must be 'txt' or 'json'")
            exit(0)


    def bd_connections(self):
        self.bd_type = self.inp_type()
        self.bd_initializations()

    # открытие и сохранение базы данных в словарь
    def bd_initializations(self):
        if self.bd_type == "txt":
            with open("{0}.{1}".format(self.bd_name, self.bd_type), 'r', encoding='utf-8') as f:
                try:
                    temp = f.readlines()
                    temp = [i.split() for i in temp]
                    # сохранения текстовой базы в словарь
                    self.bd_in_dict = {str(i): {element: temp[i][id+1] for id, element in enumerate(BD.bd_structure)} for i in range(len(temp))}
                    temp.clear()
                    for student_id in self.bd_in_dict:
                        self.create_student(student_id)  # создание обьектов для записей базы данных
                except IndexError:
                    print("Bd structure error")
        if self.bd_type == "json":
            with open("{0}.{1}".format(self.bd_name, self.bd_type), 'r', encoding='utf-8') as f:
                try:
                    self.bd_in_dict = json.load(f)
                    for student_id in self.bd_in_dict:
                        self.create_student(student_id)  # создание обьектов для записей базы данных
                except ValueError:
                    print("Bd structure error")

    # создание обьектов класса Student
    def create_student(self, student_id):
        self.obj_list.append(Student(student_id,
                                     self.bd_in_dict[student_id]["Name"],
                                     self.bd_in_dict[student_id]["Family"],
                                     self.bd_in_dict[student_id]["Sex"],
                                     self.bd_in_dict[student_id]["Age"])
                             )

    # вывод bd
    @property
    def print_bd(self):
        for i in self.obj_list:
            print(i.print_information)

    @property
    def find(self):
        fields = input("Input fields for find Name/Family/Sex/Age: ").title().split('/')
        fields = {field: input("Input {}: ".format(field)).lower() for field in fields}
        for student in self.bd_in_dict:
            for field in fields:
                if fields.get(field) == self.bd_in_dict[student].get(field).lower():
                    student_id = student
                    for i in self.obj_list:
                        if i.student_id == student_id:
                            print(i.print_information)


class Student():
    def __init__(self, student_id, name, family, sex, age):
        self.student_id = student_id
        self.name = name
        self.family = family
        self.sex = sex
        self.age = age

    # вывод информации о студенте
    @property
    def print_information(self):
        return ("{0}:\n  Name: {1},\n  Family: {2},\n  Sex: {3},\n  "
                "Age: {4}".format(self.student_id, self.name, self.family, self.sex, self.age))


def print_menu():
    print("Main menu:")
    print("\thelp - for print menu")
    print("\tprint - for print bd")
    print("\tfind - for find student")
    print("\texit - for close program")


if __name__ == "__main__":
    new_bd = BD()
    new_bd.bd_connections()
    application_exit = False
    print_menu()
    while not application_exit:
        cursor = input(">>>")
        if cursor == "help":
            print_menu()
        elif cursor == "print":
            new_bd.print_bd
        elif cursor == "find":
            new_bd.find
        elif cursor == "exit":
            application_exit = True
