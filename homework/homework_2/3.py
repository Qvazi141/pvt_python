# Если среди трех чисел А,В,С имеется хотя бы одно
# четное вычислить максимальное, иначе - минимальное

print('Введите 3 числа:')
a, b, c = [int(input()) for i in range(3)]
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print('Максимальное введенное число: ', max(a, b, c))
else:
    print('Минимальное введенное число: ', min(a, b, c))