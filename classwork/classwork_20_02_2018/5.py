# На вход поступают две строки. Необходимо выяснить, является ли вторая строка подстрокой первой.
s1 = input('Введите строку 1: ')
s2 = input('Введите строку 2: ')
if s2 in s1:
    print('Является')
else:
    print('Не является')