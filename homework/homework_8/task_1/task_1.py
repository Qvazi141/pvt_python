# В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов и слов.


def read_for_count(file_name):
    """Функция для подсчета количества слов, символов в каждой строке текстового файла,
    функция возвращает кол-во строк и dict{№ : symbol_count, word_count}"""
    count = 1
    dict_for_return = {}
    with open(file_name, "r") as f:
        list_for_count = f.readlines()
    for j in list_for_count:
        dict_for_return[count] = [len(j), len(j.split())]
        count += 1
    string_count = len(dict_for_return)
    return string_count, dict_for_return


def test_read_for_count(file_name):
    """сравнивает результыт выполнения read_for_count
    с заложенными внутри функции значениями"""
    test_string_count = 9
    test_dict = {1: [32, 7], 2: [24, 4], 3: [33, 6], 4: [31, 6], 5: [1, 0], 6: [35, 7], 7: [34, 6], 8: [36, 6], 9: [35, 7]}
    string_count, dict = read_for_count(file_name)
    if string_count == test_string_count and dict == test_dict:
        print("Test passed")


if __name__ == "__main__":
    my_file_name = "my_file.txt"
    string_count, for_count = read_for_count(my_file_name)
    print("String count - {}.".format(string_count))
    for i in for_count:
        print("String № {0}: symbol count - {1}, "
              "word count {2}".format(i, for_count.get(i)[0], for_count.get(i)[1]))
    # test_read_for_count(my_file_name)
