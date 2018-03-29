class Figure:
    def print_name(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def area_find(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def perimeter(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def scope(self):
        try:
            raise NotImplementedError()
        except NotImplementedError:
            print("This shape does not support this operation")

    def inp_params(self):
        try:
            a = int(input("Enter side A: "))
            if a < 0 or not isinstance(a, int):
                raise ValueError
            b = int(input("Enter side B: "))
            if b < 0 or not isinstance(b, int):
                raise ValueError
            c = int(input("Enter side C: "))
            if c < 0 or not isinstance(c, int):
                raise ValueError
            d = int(input("Enter side D: "))
            if c < 0 or not isinstance(d, int):
                raise ValueError
            return a, b, c, d
        except ValueError:
            print("Value error")


class Triangle(Figure):
    def __init__(self):
        self.a, self.b, self.c = self.inp_params()

    def inp_params(self):
        try:
            a = int(input("Enter side A: "))
            if a < 0 or not isinstance(a, int):
                raise ValueError
            b = int(input("Enter side B: "))
            if b < 0 or not isinstance(b, int):
                raise ValueError
            c = int(input("Enter side C: "))
            if c < 0 or not isinstance(c, int):
                raise ValueError
            return a, b, c
        except ValueError:
            print("Value error")

    def area_find(self):
        print("Area: {}".format(1/2*self.a*self.h))

    def perimeter_find(self):
        print("Perimeter: {}".format(self.a + self.b + self.c))


if __name__ == "__main__":
    t1 = Triangle()
    t1.area_find()
    t1.perimeter_find()
