# Написать программу “Калькулятор“,
# которая умеет выполнять простые арифметические операции (сложение, вычитание, умножение, деление)
# над двумя числами. Числа запрашиваются у пользователя “Enter first operand:“,
# “Enter second operand:“. Операция также запрашивается “Enter operator:” где указывается
# ‘+’, ‘-’, ‘/’, ‘*’. Результат вывести в виде, например, “Result: 12".
# Если пользователь ввел, отличную от разрешенных, операцию результат должен быть
# ‘Result: NaN’ (NaN - сокр. от Not a Number).
a, b = float(input('Enter first operand: ')), float(input('Enter second operand: '))
op = input('Enter operator: ')
if op == '+':
    print('Result: {0}'.format(a+b))
elif op == '-':
    print('Result: {0}'.format(a-b))
elif op == '*':
    print('Result: {0}'.format(a*b))
elif op == '/':
    print('Result: {0}'.format(a/b))
else:
    print('Result: NaN')