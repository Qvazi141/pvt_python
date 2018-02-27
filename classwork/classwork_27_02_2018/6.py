# Дана квадратная матрица А(N,N). Составить программу подсчета количества положительных элементов,
# расположенных выше главной диагонали.


# функция инициализация двухмерного списка
def initialization(dimension):
    return [[int(input('Input elemet {0} {1}: '.format(i, j))) for j in range(dimension)] for i in range(dimension)]


# функция подсчета положительных элементов, выше главной диагонали
def positive_count(matrix):
    count = 0
    for i in range(n):
        for j in range(n):
            if j > i and matrix[i][j] > 0:
                count += 1
    return count


# Функция вывода матрицы
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end='  ')
        print()


if __name__ == '__main__':
    n = int(input('Input N: '))
    a = initialization(n)
    print_matrix(a)
    print('The number of positive elements %d' % positive_count(a))