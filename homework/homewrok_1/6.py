# Написать программу “Калькулятор“,
# которая умеет выполнять простые арифметические операции (сложение, вычитание, умножение, деление)
# над двумя числами. Числа запрашиваются у пользователя “Enter first operand:“,
# “Enter second operand:“. Операция также запрашивается “Enter operator:” где указывается
# ‘+’, ‘-’, ‘/’, ‘*’. Результат вывести в виде, например, “Result: 12".
# Если пользователь ввел, отличную от разрешенных, операцию результат должен быть
# ‘Result: NaN’ (NaN - сокр. от Not a Number).


def calc(a, b, op):
    if op == '+':
        rez = a+b
    elif op == '-':
        rez = a-b
    elif op == '*':
        rez = a*b
    elif op == '/':
        rez = a/b
    else:
        rez = 'NaN'
    return rez

# не знал как обработать ввод, пользователи не всегда вводят целочисленный значения,
# а в выводе должны быть и целочистленные и вещественные, простое окргуление я отбросил,
# так как терялась бы дробная часть при вводе, в итоге вот такой решение с конструкцией try / except


while True:
    first, second = input('Enter first operand: '), input('Enter second operand: ')
    operator = input('Enter operator: ')
    try:
        print('Result: ', calc(int(first), int(second), operator))
    except ValueError:
        print('Result: ', calc(float(first), float(second), operator))
    s = input('Do you wish to execute one more operation? y/n: ')
    if s == 'y':
        continue
    elif s == 'n':
        break
    else:
        print('Wrong input!')
        break

