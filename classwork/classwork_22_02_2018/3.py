# Вводятся строки. Определить самую длинную строку и вывести ее номер на экран.
# Если самая длинная строка повторяется несколько раз, то вывести номера всех таких строк.


def inp():
    n = int(input('Введите кол-во строк: '))
    string = [input('Введите строку {}: '.format(i+1)) for i in range(n)]
    return string


def rows_count(string):
    numbers, row_max_len = [], string[0]
    for i in range(len(string)):
        if len(row_max_len) < len(string[i]):
            row_max_len = string[i]
            numbers = [i+1]
        elif len(row_max_len) == len(string[i]):
            numbers.append(i+1)
    return numbers


if __name__ == '__main__':
    print(rows_count((inp())))
