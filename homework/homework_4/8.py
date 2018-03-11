# Дан список кортежей grades = [(‘Ann’, 9), (‘John’, 7), (‘Smith’, 5), (‘George’, 6) ].
# Вывести информацию об оценках по возрастанию в виде: ‘Hello Ann! Your grade is 9’


def print_grades(g):
    g.sort(key=lambda g: g[1])
    for i in grades:
        print('Hello {0}! Your grade is {1}'.format(i[0], i[1]))


if __name__ == '__main__':
    grades = [('Ann', 9), ('John', 7), ('Smith', 5), ('George', 6)]
    print_grades(grades)
