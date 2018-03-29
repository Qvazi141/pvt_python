class Elevator:
    total = 0

    def __init__(self, name):
        self.name = name
        self.count_up = 0
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
        print("lift - for lift")
        print("[lift1] - [lift2] - for sub lift")



if __name__ == "__main__":
    app_close = True
    count = int(input("Enter lift number: "))
    elevators = {}
    commands = {
        "lift":
        "total":
        ""
    }
    for i in range(count):
        elevators[i+1] = Elevator()
    while app_close:
        lift = input("Enter lift for do: ")
        lift_exit = True
            while lift_exit:

