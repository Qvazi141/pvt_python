# Преобразовать массив так, чтобы сначала шли все отрицательные элементы,
# а потом положительные(0 считать положительным). Порядок следования должен быть сохранен.


def inp():
    number = int(input('Input the list size: '))
    return [int(input('Input number: ')) for i in range(number)]

# избыточное решение
# def list_convection(my_list):
#     positive, negative = [], []
#     for i in my_list:
#         if i < 0:
#             negative.append(i)
#         else:
#             positive.append(i)
#     return negative.extend(positive)


def list_convection(my_list):
    index = 0
    for i in range(len(my_list)):
        if my_list[i] <= 0:
            tmp = my_list[i]
            my_list.remove(my_list[i])
            my_list.insert(index, tmp)
            index += 1
    return my_list


if __name__ == '__main__':
    print(list_convection(inp()))