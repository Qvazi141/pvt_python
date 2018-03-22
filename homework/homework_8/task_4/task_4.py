# Реализовать программу, которая выводит содержимое каталога в
# файловой системе. Путь к каталогу запрашивается у пользователя.
from os import listdir


def content(path):
    """Функция возвращает список содрежимого директории"""
    return listdir(path)


def test_content(test_result=['desktop.ini', 'web-projects'], test_path = "D:\work"):
    """Функция тестирования func content."""
    result = content(test_path)
    print("Test passed") if result == test_result else print("Test not passed")

# точка входа в программу
if __name__ == "__main__":
    # test_content()
    my_path = input("Enter path: ")
    for element in content(my_path):
        print(element)