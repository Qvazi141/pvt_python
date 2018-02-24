# Определить, является ли введенное слово идентификатором,
# т.е. начинается ли оно с английской буквы в любом регистре
# или знака подчеркивания и не содержит других символов, кроме
# букв английского алфавита (в любом регистре), цифр и знака подчеркивания.


def inp():
    return input('Input word: ')


def check_word(word):
    word = word.upper()
    alphabet = 'abcdefjhigklmnopqrstuvwxyz'.upper()
    if word[0] in alphabet or word[0] == '_':
        for i in word[1:]:
            if i in alphabet or i.isnumeric() or i == '_':
                continue
            else:
                return 'is not an identifier'
        return 'is an identifier'
    else:
        return 'is not an identifier'


if __name__ == '__main__':
    print(check_word(inp()))
