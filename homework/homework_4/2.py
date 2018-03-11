# Найти и вывести все гласные буквы (без повторений),
# которые встречаются в самом коротком слове.
# Текст запрашивается у пользователя. Алфавит использовать любой.


def inp():
    return input('Input string: ')


def del_punctuation(string):
    string = string.replace('.', '').replace('!', '').replace('?', '').replace(',', '')
    return string


def short_word_search(string):
    string = del_punctuation(string)
    string = string.split()
    short_word = string[0]
    for i in string:
        if len(i) < len(short_word):
            short_word = i
    return short_word


def vowels_count(word):
    vowels = ('A', 'E', 'I', 'O', 'U', 'Y')
    word = word.upper()
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count


if __name__ == '__main__':
    print('The number of vowels in the shortest word:\
     {}'.format(vowels_count(short_word_search(inp()))))
