# Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
# При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
# Если производить вычитание у лифта,
# который еще не совершал поднятий, должна быть выведена ошибка неправильной операции.
# Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
# Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
# При строчных операциях необходимо вывести детальную информацию по лифту:
# наименование, количество поднятий и процент от общего количества поднятий всех лифтов.
import re


class Elevator:
    total = 0  # подсчет общего кол-ва вызовов

    def __init__(self, name=None):
        self._name = name  # имя лифта
        self.floor = 0  # кол-во вызовов

    def lift(self):
        Elevator.total += 1
        print("Lift up!")
        self.floor += 1

    # Переопределение операции "-"
    def __sub__(self, other):
        try:
            if self.floor == 0:
                raise ValueError
            else:
                return self.floor - other.floor
        except ValueError:
            return "Lift at the 0 floor"

    # Переопределение операции "+"
    def __add__(self, other):
        return self.floor + other.floor

    # Переопределение операции ">"
    def __gt__(self, other):
        if self.floor > other.floor:
            return "True"
        else:
            return "False"

    # Переопределение операции "<"
    def __lt__(self, other):
        if self.floor < other.floor:
            return "True"
        else:
            return "False"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        flag = True
        while flag:
            if re.match(r"^[\w\.-]+$", value):
                flag = False
                self._name = value
            else:
                print("Name is not valid")
                value = input("Enter elevator name: ").lower()

    # вывод статистики по лифту, переопределение строкового представления
    def __str__(self):
        return ("{0}\nStatistics:\nElevator name - {1},"
                " number of lifts - {2}\n{3}").format("-" * 20, self._name, self.floor, "-" * 20)

# вывод доступных команд
def help():
    print("Commands:")
    print("help - for print commands")
    print("[name] lift - for lift")
    print("[name1] - [name2] - for sub elevator")
    print("[name1] + [name2] - for add elevator")
    print("[name1] > [name2] - for operation >")
    print("[name1] < [name2] - for operation <")
    print("[name] stat - for print statistics")
    print("total - for print total lift")
    print("exit - for exit program")


# поиск имен лифтов из ввода пользователя
def input_parsing(operand, _elevators):
    for _elevator in _elevators:
        if _elevator.name == command.split(operand)[0].replace(' ', ''):
            elevator_1 = _elevator
        if _elevator.name == command.split(operand)[1].replace(' ', ''):
            elevator_2 = _elevator
    return elevator_1, elevator_2


if __name__ == "__main__":
    app_close = False  # выход из приложения
    count = 0  # кол-во лифтов
    elevators = []  # список лифтов
    while count <= 0 and isinstance(count, int):
        try:
            count = int(input("Enter the number of elevators: "))
            if count <= 0:
                raise ValueError
        except ValueError:
            print("Elevator count must be numeric and > 0")
    for i in range(count):
        elevators.append(Elevator())
        elevators[i].name = input("Enter elevator {} name: ".format(i+1)).lower()
    print(">>> Enter help - for print commands.")
    # ---------------------------------------------------------------------------
    # вход в интерактив
    while not app_close:
        command = input(">>> ").lower()
        if re.match(r"^help$", command):
            help()
        if re.match(r"^[\w\.-]+\slift$", command):
            for elevator in elevators:
                if elevator.name == command[:command.index(" lift")]:
                    elevator.lift()
        if re.match(r"^[\w\.-]+(\s)?-(\s)?[\w\.-]+$", command):
            try:
                l1, l2 = input_parsing("-", elevators)
                print(l1 - l2)
            except NameError:
                print("Elevator name does not exist")
        if re.match(r"^[\w\.-]+(\s)?\+(\s)?[\w\.-]+$", command):
            try:
                l1, l2 = input_parsing("+", elevators)
                print(l1 + l2)
            except NameError:
                print("Elevator name does not exist")
        if re.match(r"^[\w\.-]+(\s)?>(\s)?[\w\.-]+$", command):
            try:
                l1, l2 = input_parsing(">", elevators)
                print(l1 > l2)
            except NameError:
                print("Elevator name does not exist")
        if re.match(r"^[\w\.-]+(\s)?<(\s)?[\w\.-]+$", command):
            try:
                l1, l2 = input_parsing("<", elevators)
                print(l1 < l2)
            except NameError:
                print("Elevator name does not exist")
        if re.match(r"^[\w\.-]+\sstat$", command):
            for elevator in elevators:
                if elevator.name == command[:command.index(" stat")]:
                    print(elevator)
        if re.match(r"^total$", command):
            print("Total lift: {}".format(Elevator.total))
        if re.match("^exit$", command):
            app_close = True


