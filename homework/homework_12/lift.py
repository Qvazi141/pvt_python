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

    def commands(self):
        print("Commands:")
        print("help - for print commands")
        print("lift - for lift")
        print("[lift1] - [lift2] - for sub lift")
        print("q - for quit elevator")
        print("exit - for exit program")


if __name__ == "__main__":
    app_close = False
    count = int(input("Enter the number of elevators: "))
    elevators = []
    for i in range(count):
        elevators.append(Elevator(input("Enter elevator {} name: ".format(i+1))))
    while not app_close:
        print("-"*20)
        print("Total number of lifts: {}".format(Elevator.total))
        for i in range(count):
            print("Elevator {0}: name - {1}, number of lifts - {2}".format(i+1, elevators[i].name, elevators[i].floor))
        elevator = int(input("Enter lift for do: ")) - 1
        elevator_exit = False
        elevators[elevator].commands()
        while not elevator_exit:
            command = input(">>> ")
            if command == "help":
                elevators[elevator].commands()
            elif command == "lift":
                elevators[elevator].lift()
            elif command == "q":
                elevator_exit = True
            elif command == "exit":
                elevator_exit = True
                app_close = True


