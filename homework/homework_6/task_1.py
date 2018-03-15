# Написать программу нахождения простых чисел, используя решето Эратосфена.
# Для каждой из пользовательских функций написать функцию-тест.


def eratosthenes(index_range):
    input_list = [True]*index_range
    for i in range(2, index_range):
            for j in range(i*2, index_range, i):
                input_list[j] = False
    result = [i for i in range(2, index_range) if input_list[i]]
    return result


def test_eratosthenes(test_index=30, test_result=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]):
    test = eratosthenes(test_index)
    if test == test_result:
        print('test passed')


if __name__ == '__main__':
    n = int(input("Введите N:"))
    # test_eratosthenes()
    print(eratosthenes(n))
