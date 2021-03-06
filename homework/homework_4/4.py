# Начальный вклад в банке равен 1000 BYN.
# Через каждый месяц размер вклада увеличивается на P-процентов
# (P - вещественное число, 0 < P < 25). Значение P запрашивается у пользователя.
# По данному P определить, через сколько месяцев размер вклада
# превысит 1100 BYN и вывести найденное количество месяцев и итоговый размер вклада.


def month_count(deposit, percent):
    count_month = 0
    while deposit < 1100:
        deposit += deposit * percent / 100
        count_month += 1
    return count_month


if __name__ == '__main__':
    d = 1000
    p = float(input('Введите процентную ставку (0 < P < 25): '))
    print('Размер вклада превысит 1100 BYN через {} месяцев'.format(month_count(d, p)))