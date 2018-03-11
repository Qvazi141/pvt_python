# Дана строка ‘Hello!Anthony!Have!A!Good!Day!’.
# Создать список, состоящий из отдельных слов [‘HELLO’, ‘ANTHONY’, ‘HAVE’, ‘A’, ‘GOOD’, ‘DAY’].
s1 = 'Hello!Anthony!Have!A!Good!Day!'
s1 = s1.upper().split('!')
if s1[-1] == '':
    s1 = s1[:-1]
print(s1)
