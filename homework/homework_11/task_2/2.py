# Реализовать программу подсчета площади, периметра, объема геометрических фигур
# (треугольник, прямоугольник, квадрат, трапеция, окружность).
# Если одна из фигур не поддерживает вычисление одного из свойств,
# в программе должно быть вызвано исключение с человеко-читабельным сообщением и корректно обработано.


class Figure:
    pi = 3.1415

    def area_find(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def perimeter_find(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def scope(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def input_sides(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not have sides")

    def input_radius(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not have sides")


class FourSidedFigure(Figure):
    pass


class Trapeze(FourSidedFigure):
    def __init__(self):
        self.name = "Trapeze"
        self.a, self.b, self.c, self.d  = 0, 0, 0, 0

    def input_sides(self):
        try:
            self.a = int(input("Enter side A: "))
            if self.a <= 0 or not isinstance(self.a, int):
                raise ValueError
            self.b = int(input("Enter side B: "))
            if self.b <= 0 or not isinstance(self.b, int):
                raise ValueError
            self.c = int(input("Enter side C: "))
            if self.c <= 0 or not isinstance(self.c, int):
                raise ValueError
            self.d = int(input("Enter side D: "))
            if self.d <= 0 or not isinstance(self.d, int):
                raise ValueError
            if not self._check_trapeze():
                raise ValueError
        except ValueError:
            print("Value Error")
            self.a, self.b, self.c, self.d = 0, 0, 0, 0

    def __str__(self):
        return "{0}. Sides: A - {1}, B - {2}, C - {3}, D - {4}".format(self.name, self.a, self.b, self.c, self.d)

    def area_find(self):
        try:
            s = (self.a + self.b) / 2 * (self.c**2 - (((self.b-self.a)**2 + self.c**2 - self.d**2) / 2*(self.b - self.a))**2)**0.5
            if s == 0:
                raise ValueError
            print("Area: {}".format(s))
        except ValueError:
            print("Something went wrong, because the area is 0")

    def perimeter_find(self):
        print("Perimeter: {}".format(self.a + self.b + self.c + self.d))

    # проверка существования трапеции
    def _check_trapeze(self):
        max_el = max(self.a, self.b, self.c, self.d)
        l = [self.a, self.b, self.c, self.d]
        l.remove(max_el)
        if sum(l) > max_el:
            return True
        else:
            print("Trapeze does not exist")
            return False


class Rectangle(FourSidedFigure):
    def __init__(self):
        self.name = "Rectangle"
        self.a, self.b = 0, 0

    def input_sides(self):
        try:
            self.a = int(input("Enter side A: "))
            if self.a <= 0 or not isinstance(self.a, int):
                raise ValueError
            self.b = int(input("Enter side B: "))
            if self.b <= 0 or not isinstance(self.b, int):
                raise ValueError
        except ValueError:
            print("Value Error")
            self.a, self.b = 0, 0

    def __str__(self):
        return "{0}. Sides: A - {1}, B - {2}".format(self.name, self.a, self.b)

    def area_find(self):
        print("Area: {}".format(self.a*self.b))

    def perimeter_find(self):
        print("Perimeter: {}".format(self.a*2 + self.b*2))


class Square(FourSidedFigure):
    def __init__(self):
        self.name = "Square"
        self.a = 0

    def input_sides(self):
        try:
            self.a = int(input("Enter side A: "))
            if self.a <= 0 or not isinstance(self.a, int):
                raise ValueError
        except ValueError:
            print("Value Error")
            self.a = 0

    def __str__(self):
        return "{0}. Sides: A - {1}".format(self.name, self.a)

    def area_find(self):
        print("Area: {}".format(self.a**2))

    def perimeter_find(self):
        print("Perimeter: {}".format(self.a*4))


class Circle(Figure):
    def __init__(self):
        self.name = "Circle"
        self.r = 0

    def input_radius(self):
        try:
            self.r = int(input("Input radius: "))
            if self.r <= 0 or not isinstance(self.r, int):
                raise ValueError
        except ValueError:
            print("Value Error")
            self.r = 0

    def __str__(self):
        return "{0}. Radius - {1}".format(self.name, self.r)

    def area_find(self):
        print("Area: {}".format(Figure.pi*self.r**2))

    def perimeter_find(self):
        print("Perimeter: {}".format(2*Figure.pi*self.r))


class Triangle(Figure):
    def __init__(self):
        self.name = "Triangle"
        self.a, self.b, self.c = 0, 0, 0

    def input_sides(self):
        try:
            self.a = int(input("Enter side A: "))
            if self.a <= 0 or not isinstance(self.a, int):
                raise ValueError
            self.b = int(input("Enter side B: "))
            if self.b <= 0 or not isinstance(self.b, int):
                raise ValueError
            self.c = int(input("Enter side C: "))
            if self.c <= 0 or not isinstance(self.c, int):
                raise ValueError
            if not self._check_triangle():
                raise ValueError
        except ValueError:
            print("Value Error")
            self.a, self.b, self.c = 0, 0, 0

    def __str__(self):
        return "{0}. Sides: A - {1}, B - {2}, C - {3}".format(self.name, self.a, self.b, self.c)

    def _check_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            print("Triangle does not exist")
            return False

    def area_find(self):
        p = (self.a + self.b + self.c) / 2
        print("Area: {}".format((p*(p-self.a)*(p-self.b)*(p-self.c))**0.5))

    def perimeter_find(self):
        print("Perimeter: {}".format(self.a + self.b + self.c))


# меню
def print_menu():
    print("Main menu:")
    print("help - for print menu")
    print("area - for print figure area")
    print("perimetr - for print figure perimetr")
    print("scope - for print figure scope")
    print("q - for quit the figure")
    print("exit - for exit the program")


# работа с фигурой
def select_menu(figure):
    print("-" * 40)
    print_menu()
    close_figure = False
    print("-" * 40)
    print(figure)
    while not close_figure:
        print("-" * 20)
        command = input(">>> ")
        if command == "help":
            print_menu()
        elif command == "area":
            obj.area_find()
        elif command == "perimetr":
            obj.perimeter_find()
        elif command == "scope":
            obj.scope()
        elif command == "q":
            close_figure = True
        elif command == "exit":
            return True
    return False


if __name__ == "__main__":
    application_exit = False
    while not application_exit:
        print("Enter the shape to create: triangle, square, rectangle, trapeze, circle")
        shape = input(">>> ")
        if shape == "triangle":
            obj = Triangle()
            obj.input_sides()
            if obj.a != 0 and obj.b != 0 and obj.c != 0:
                application_exit = select_menu(obj)
        elif shape == "square":
            obj = Square()
            obj.input_sides()
            if obj.a != 0:
                application_exit = select_menu(obj)
        elif shape == "rectangle":
            obj = Rectangle()
            obj.input_sides()
            if obj.a != 0 and obj.b != 0:
                application_exit = select_menu(obj)
        elif shape == "trapeze":
            obj = Trapeze()
            obj.input_sides()
            if obj.a != 0 and obj.b != 0 and obj.c != 0 and obj.d != 0:
                application_exit = select_menu(obj)
        elif shape == "circle":
            obj = Circle()
            obj.input_radius()
            if obj.r != 0:
                application_exit = select_menu(obj)
        elif shape == "exit":
            application_exit = True