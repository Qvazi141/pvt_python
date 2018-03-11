# Сжать список, удалив из него все 0 и заполнить освободившиеся справа элементы значениями -1.


def inp():
    number = int(input('Input the list size: '))
    return [int(input('Input number: ')) for i in range(number)]


def remove_zero(my_list):
    while my_list.count(0) != 0:
        my_list.remove(0)
        my_list.append(-1)
    return my_list


if __name__ == '__main__':
    print(remove_zero(inp()))
