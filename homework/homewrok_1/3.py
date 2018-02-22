# Написать программу, которая запрашивает у пользователя два целочисленных числа,
# и выводит результат вида “The sum of 1 and 3 is 4”.
a, b = int(input('Input a: ')), int(input('Input b: '))
print('The sum of {0} and {1} is {2}'.format(a, b, a+b))