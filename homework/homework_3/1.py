# Исключить из списка А1..AN максимальный элемент.
n = int(input('Введите размерность списка: '))
l1 = [int(input()) for i in range(n)]
l1.remove(max(l1))
print(l1)
