# Ввести три числа А,В,С. Удвоить каждое из них, если А>=В>=С, иначе поменять значения А и В.
print('Введите a, b, c:')
a, b, c = [int(input()) for i in range(3)]
if a >= b >= c:
    print(a*2, b*2, c*2, sep=' ')
else:
    a, b = b, a
    print(a, b, c, sep=' ')
