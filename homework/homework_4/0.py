# Написать программу, которая предлагает пользователю ввести список
# чисел, после чего  запрашивает число для которого нужно посчитать
# сколько раз оно встречается в списке.


def my_count(x, l):
    count = 0
    for i in l:
        if i == x:
            count += 1
    return count


def inp():
    s = []
    while True:
        x = input('Enter number: ')
        if x == '':
            break
        elif x.isnumeric():
            s.append(int(x))
    x = int(input('Input number to count: '))
    return s, x


if __name__ == '__main__':
    my_list, number = inp()
    print('Count: {}'.format(my_count(number, my_list)))
