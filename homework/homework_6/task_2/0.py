# Дан список А1..AN. Найти элемент, который чаще всего встречается, вывести его значение и количество повторений.


# функция подсчета числа повторений, каждого элемента, возвращает словарь
def find_count(my_list):
    count = {}
    for i in my_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return max(count.items(), key=lambda x: x[1])


if __name__ == '__main__':
    n = int(input('Введите N: '))
    a = [int(input()) for i in range(n)]
    print('Число {0} Повторяется {1} раз'.format(*find_count(a)))

