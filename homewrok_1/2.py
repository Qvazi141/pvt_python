# Написать программу, которая выводит три переменные first_name,
# last_name, patronymic разделенные ‘|' (прямой чертой). Например “Иван|Иванович|Иванов“.
first_name = input('Enter your name: ')
patronymic = input('Enter your patronymic: ')
last_name = input('Enter your last name: ')
print('{0}|{1}|{2}'.format(first_name, patronymic, last_name))