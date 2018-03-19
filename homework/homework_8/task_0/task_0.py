# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка.


# Функция для записи текста в файлпострочно, возвращает имя файла
def to_write(file_name):
    q = True
    with open(file_name, "w") as f:
        while q:
            string = input("Input string: ")
            q = False if string == "" else f.write(string + '\n')
    return file_name


# Функция для тестирования def to_write
def test_to_write(file_name, test_file = "test_file.txt"):
    with open(file_name) as f:
        try:
            with open(test_file) as test_f:
                if f.read() == test_f.read():
                    print("Test passed")
        except:
            print("File for test not found")


if __name__ == "__main__":
    my_filename = "my_file.txt"
    to_write(my_filename)
    test_to_write(my_filename)
