# Для двух чисел Х,У определить, являются ли они корнями уравнения А*X^4+D*X^2+C=0

x = int(input('Input x: '))
y = int(input('Input y: '))
a = int(input('Input A: '))
b = int(input('Input B: '))
c = int(input('Input C: '))
if a*x**4 + b*y**2+c == 0:
    print('x: ', x, ', y: ', y, ' - являются корнями уравнения')
else:
    print('x: ', x, ', y: ', y, ' - не являются корнями уравнения')