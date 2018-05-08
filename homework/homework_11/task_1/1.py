# Реализовать программу, которая отображает дерево каталогов.
# Путь к целевому каталогу запрашивается у пользователя. В программе не должно использоваться циклов
from os import listdir, path


def inp():
    try:
        my_path = input("Enter path: ")
        if not path.exists(my_path):
            raise FileExistsError
        return my_path
    except FileExistsError:
        print("Path does not exist")


def print_tree(my_path, count = 0):
    count += 2
    for element in listdir(my_path):
        if path.isdir("\\".join([my_path, element])):
            print("|{0}{1}".format("_" * count, element))
            print_tree("\\".join([my_path, element]), count)
        else:
            print("|{0}{1}".format("_" * count, element))


if __name__ == "__main__":
    print_tree(inp())
