# функция инициализация двухмерного списка
def initialization(n, m):
    return [[float(input('Input element {0} {1}: '.format(i, j))) for j in range(m)] for i in range(n)]


# Функция вывода матрицы
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='  ')
        print()


# функция проверки условия р1<=a(i,j)<=p2, возвращает словарь адрес:значение
def check_matrix(p1, p2, matrix):
    my_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if p1 <= matrix[i][j] <= p2:
                my_dict['a({0},{1})'.format(i, j)] = matrix[i][j]
    return my_dict


def start():
    """ Дана вещественная матрица А(3,4). Составить программу подсчета количества элементов матрицы,
    удовлетворяющих условию р1<=a(i,j)<=p2. Значения р1 и р2 запрашиваются у пользователя."""
    a = initialization(3, 4)
    print_matrix(a)
    b, v = [float(input('Input p{}: '.format(i+1))) for i in range(2)]
    d = check_matrix(b, v, a)
    print('Количество элементов, удовлетворяяющих условию равно: {}'.format(len(d)))  # вывод количества элементов
    print(d)  # вывод элементов
