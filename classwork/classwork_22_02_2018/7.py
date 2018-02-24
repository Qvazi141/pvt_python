# Пользователь вводит строку и символ.
# В строке найти все вхождения этого символа и перевести его в верхний регистр,
# а также удалить часть строки, начиная с последнего вхождения этого символа и до конца.


def inp():
    symbol = input('Input symbol: ')
    string = input('Input string: ')
    return symbol[0], string


def string_convection(symbol, string):
    string = string.replace(symbol, symbol.upper())
    index = string[::-1].index(symbol.upper())
    return string[:len(string)-index]


if __name__ == '__main__':
    s, s1 = inp()
    print(string_convection(s, s1))
