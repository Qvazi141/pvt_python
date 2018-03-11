# Написать программу, запрашивающую у пользователя строку с текстом и разделитель.
# Необходимо вывести список слов с их длиной в начале слова, например, 5hello.
# Для каждой из пользовательских функций написать функцию-тест.


def find_len(string, separator):
    list_for_work = string.split(separator)
    return list(map(lambda x: str(len(x))+x, list_for_work))


if __name__ == '__main__':
    my_string = input('Enter string: ')
    my_separator = input('Enter separator: ')
    print(find_len(my_string, my_separator))
