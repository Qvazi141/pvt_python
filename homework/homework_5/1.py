# Дана целая матрица А(N,N). Составить программу подсчета среднего арифметического значения элементов матрицы.


# функция инициализация двухмерного списка
def initialization(dimension):
    return [[int(input('Input element {0} {1}: '.format(i, j))) for j in range(dimension)] for i in range(dimension)]


# Функция вывода матрицы
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end='  ')
        print()


# функция подсчета среднего арифметического значения элементов матрицы.
def average(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            sum += matrix[i][j]
    return sum / len(matrix)**2


if __name__ == '__main__':
    n = int(input('Input N: '))
    a = initialization(n)
    print_matrix(a)
    print('Arithmetic mean of matrix elements: {}'.format(average(a)))