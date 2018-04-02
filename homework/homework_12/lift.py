# Реализовать класс лифта Elevator. Класс должен обладать методом, lift, отвечающий за вызов лифта.
# При сложении/вычитании экземпляров класса должно возвращаться значение производимой математической операции.
# Если производить вычитание у лифта,
# который еще не совершал поднятий, должна быть выведена ошибка неправильной операции.
# Предусмотреть возможность сравнения какой из лифтов совершил большее количество поднятий.
# Также необходимо предусмотреть подсчет общего количества поднятий всех лифтов.
# При строчных операциях необходимо вывести детальную информацию по лифту:
# наименование, количество поднятий и процент от общего количества поднятий всех лифтов.


class Elevator:
    total = 0

    def __init__(self, name):
        self.name = name
        self.floor = 0

    def lift(self):
        Elevator.total += 1
        print("Lift up!")
        self.floor += 1

    def __sub__(self, other):
        try:
            if self.floor == 0:
                raise ValueError
            else:
                return self.floor - other
        except ValueError:
            print("Lift at the 0 floor")

    def commands(self, obj_list):
        print("-" * 20)
        print("Statistics:")
        print("Total number of lifts: {}".format(Elevator.total))
        for i in range(obj_list):
            print(
                "Elevator {0}: name - {1}, number of lifts - {2}".format(i + 1, elevators[i].name, elevators[i].floor))
        print("-" * 20)
        print("Commands:")
        print("help - for print commands and statistics")
        print("[name] lift - for lift")
        print("[name1] - [name2] - for sub lift")
        print("exit - for exit program")


if __name__ == "__main__":
    app_close = False
    count = int(input("Enter the number of elevators: "))
    elevators = []
    for i in range(count):
        elevators.append(Elevator(input("Enter elevator {} name: ".format(i+1))))
    elevators[0].commands(count)
    while not app_close:
        command = input(">>> ").split()
        if command[0] == "help":
            elevators[0].commands(count)
        elif len(command) == 2:
            if command[1] == "lift":
                for elevator in elevators:
                    if elevator.name == command[0].title():
                        elevator.lift()
        elif len(command) > 2:
            if command[1] == "-":
                l1 = filter(lambda x: x.name == command[0], elevators)
                l2 = filter(lambda x: x.name == command[2], elevators)
                print(l1-l2)
        elif command[0] == "exit":
            app_close = True


