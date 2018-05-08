# В текстовый файл построчно записаны фамилия и имя учащихся класса
# и его оценка за контрольную. Вывести на экран всех учащихся, чья
# оценка меньше 3 баллов и посчитать средний балл по классу.


def more_than(file_name, number):
    """Функция находит оценки меньше 3 и возвращает строки, в виде генератора"""
    with open(file_name, "r", encoding='utf-8') as f:
        class_list = f.readlines()
    return filter(lambda x: int(x[-2]) < number, class_list)


def test_more_than_3(file_name):
    """"тестирование функции more_than_3"""
    test_number = 3
    test = ["Каролева Таня 1\n", "Сергеева Татьяна 2\n", "Кузнецов Антон 1\n", "Кароль Михаил 1\n"]
    result = list(more_than(file_name, test_number))
    if test == result:
        print("Test passed")


if __name__ == "__main__":
    my_file_name = "my_file.txt"
    for i in more_than(my_file_name, 3):
        print(i, end="")
    # test_more_than_3(my_file_name)